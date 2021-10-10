from matplotlib.lines import Line2D
import geopandas as gpd

# Pandas, NumPy, Matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Scikit-learn
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, precision_score, recall_score
# Keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.callbacks import EarlyStopping
from keras import backend as K
from keras.utils.np_utils import to_categorical

# SCIAN 3 (nivel subsector)
denue_wide = pd.read_csv(
    "https://raw.githubusercontent.com/Roderich25/datasets/main/denue_wide_3.csv")  # Carga desde repositorio GitHub
rezago = pd.read_csv(
    "https://raw.githubusercontent.com/Roderich25/datasets/main/rezago_social.csv")  # Carga desde repositorio GitHub
rezago_social = rezago[["lgc00_15cl3_2", "Key", "POB_TOTAL", "LAT", "LON"]]
df = pd.merge(rezago_social, denue_wide, on=['Key'])
y_original = rezago_social['lgc00_15cl3_2']
# Transformación Cheng
onehot = np.zeros((y_original.shape[0], 3))
for idx, val in enumerate(y_original.astype(int)):
    onehot[idx, :val] = 1.
y_onehot = onehot
# print(np.unique(y_original))
# print(np.unique(y_onehot, axis=0))
# y = y_onehot
y = y_original - 1
# print(np.unique(y))

df.drop(["lgc00_15cl3_2", "Key", "LAT", "LON"], axis=1, inplace=True)
X = df.div(df.POB_TOTAL, axis=0) * 1000
X.drop(["POB_TOTAL"], axis=1, inplace=True)
X["LAT"] = rezago_social["LAT"]
X["LON"] = rezago_social["LON"]
X["POB_TOTAL"] = rezago_social["POB_TOTAL"]
print(X.columns)
y = to_categorical(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.20, random_state=0)

from sklearn.metrics import balanced_accuracy_score, accuracy_score, f1_score, mean_absolute_error
from keras.callbacks import EarlyStopping
from keras.initializers import GlorotUniform
from tensorflow.keras import regularizers
import tensorflow as tf


def build_model(hl, af, l2, sh):
    model = Sequential()
    ###
    model.add(Dense(hl, activation=af, kernel_regularizer=regularizers.l2(l2), kernel_initializer=GlorotUniform(seed=0),
                    input_shape=(sh,)))
    model.add(
        Dense(hl, activation=af, kernel_regularizer=regularizers.l2(l2), kernel_initializer=GlorotUniform(seed=0)))
    model.add(
        Dense(hl, activation=af, kernel_regularizer=regularizers.l2(l2), kernel_initializer=GlorotUniform(seed=0)))
    ###
    model.add(Dense(3, activation='softmax'))
    model.compile(optimizer='adam',
                  loss='mean_squared_error',
                  metrics=['accuracy'])
    return model


tf.random.set_seed(0)  # seed

for hl in [84]:
    for af in ['relu']:
        for l2 in [0.001]:
            for eps in [200]:  # 5
                loss_train = []
                loss_val = []
                ord_acc = []
                f1_mac = []
                mae_score = []
                kf = StratifiedKFold(n_splits=10, shuffle=True, random_state=0)
                Xtrain, ytrain = X.to_numpy(), y
                # Xtrain, ytrain = X_train.to_numpy(), y_train  #
                for train, test in kf.split(Xtrain, np.sum(ytrain, axis=1)):
                    part_X_train, X_val = Xtrain[train, :], Xtrain[test, :]
                    part_y_train, y_val = ytrain[train], ytrain[test]
                    sc = StandardScaler()
                    part_X_train = sc.fit_transform(part_X_train)
                    X_val = sc.transform(X_val)
                    model = build_model(hl, af, l2, sh=X_val.shape[1])
                    tf.random.set_seed(0)  # seed
                    history = model.fit(part_X_train, part_y_train, verbose=0, epochs=eps,
                                        callbacks=[EarlyStopping(patience=1, restore_best_weights=True)],
                                        validation_data=(X_val, y_val))
                    loss_train.append(history.history['loss'])
                    loss_val.append(history.history['val_loss'])
                    # print(len(history.history['val_loss']))
                    y_pred = np.argmax(model.predict(X_val), axis=1)
                    y_val_ = np.argmax(y_val, axis=1)
                    # print(y_pred)
                    # print(y_val_)
                    print('P', precision_score(y_val_, y_pred, average=None))
                    print('S', recall_score(y_val_, y_pred, average=None))

                    acc_temp = accuracy_score(y_val_, y_pred)
                    f1_temp = f1_score(y_val_, y_pred, average='macro')
                    mae_temp = mean_absolute_error(y_val_, y_pred)
                    ord_acc.append(acc_temp)
                    f1_mac.append(f1_temp)
                    mae_score.append(mae_temp)
                    # print(acc_temp, f1_temp)
                print(ord_acc)
                print(f1_mac)
                print(mae_score)
                print(f'# hl:{hl}, af:{af}, l2:{l2},',
                      f'acc:{np.mean(ord_acc)}+/-{np.std(ord_acc)},',
                      f'f1:{np.mean(f1_mac)}+/-{np.std(f1_mac)}',
                      f'mae:{np.mean(mae_score)}+/-{np.std(mae_score)}')
                #
                # mean_loss_train = np.array(loss_train).mean(axis=0)
                # mean_loss_val = np.array(loss_val).mean(axis=0)
                # epochs = range(1, 1 + len(mean_loss_val))
                # plt.plot(epochs, mean_loss_train, 'k--', label='Entrenamiento')
                # plt.plot(epochs, mean_loss_val, 'k', label='Validación')
                # plt.legend()
                # plt.show()
                # np.save('early/ann_nom_train.npy', mean_loss_train)
                # np.save('early/ann_nom_val.npy', mean_loss_val)
                # MAP
                gdf = gpd.read_file('municipios/areas_geoestadisticas_municipales.shp')
                print(gdf.columns)
                gdf['Key'] = gdf['CVE_ENT'] + gdf['CVE_MUN']
                rezago = pd.read_csv("rezago_social/rezago_social.csv")
                rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON"]]
                rezago_social['Key'] = rezago_social['Key'].astype(str).str.zfill(5)
                gdf = gdf.merge(rezago_social, on='Key')
                legend_elements = [Line2D([0], [0], marker='o', color='w', label='Alto',
                                          markerfacecolor='r', markersize=15),
                                   Line2D([0], [0], marker='o', color='w', label='Medio',
                                          markerfacecolor='yellow', markersize=15),
                                   Line2D([0], [0], marker='o', color='w', label='Bajo',
                                          markerfacecolor='g', markersize=15)]
                csfont = {'fontname': 'Times New Roman'}
                colors = {1: 'green', 2: 'yellow', 3: 'red'}
                fig, (ax1, ax2) = plt.subplots(1, 2)
                gdf.plot(ax=ax1, color=gdf['lgc00_15cl3'].map(colors), legend=True)
                ax1.set_xticks([])
                ax1.set_yticks([])
                # ax1.set_title("Mapa de Rezago Social a nivel municipal, 2015.", **csfont)
                txt = "Categorías de Rezago Social, Vargas-Chanes y Váldez-Cruz (2019)"
                ax1.text(0.01, 0.01, txt, wrap=True, horizontalalignment='left', fontsize=12, **csfont)
                ax1.legend(handles=legend_elements)
                ###
                gdf = gpd.read_file('municipios/areas_geoestadisticas_municipales.shp')
                gdf['Key'] = gdf['CVE_ENT'] + gdf['CVE_MUN']
                rezago = pd.read_csv("rezago_social/rezago_social.csv")
                rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON"]]
                rezago_social['Key'] = rezago_social['Key'].astype(str).str.zfill(5)
                #
                sc = StandardScaler()
                X = sc.fit_transform(X.to_numpy())
                model = build_model(hl, af, l2, 93)
                model.fit(X, y, verbose=0, epochs=5)
                y_pred = np.argmax(model.predict(X), axis=1) + 1
                print('CLASS:', np.unique(y_pred))
                #
                rezago_social['Pred'] = y_pred
                gdf = gdf.merge(rezago_social, on='Key')
                # fig, ax = plt.subplots()
                colors = {1: 'red', 2: 'yellow', 3: 'green'}
                gdf.plot(ax=ax2, color=gdf['Pred'].map(colors))
                ax2.set_xticks([])
                ax2.set_yticks([])
                # ax2.set_title("Mapa de Rezago Social a nivel municipal, 2015.", **csfont)
                txt = "Categorías predichas por modelo ANN-NOM para 2015"
                ax2.text(0.01, 0.01, txt, wrap=True, horizontalalignment='left', fontsize=12, **csfont)
                ax2.legend(handles=legend_elements)
                plt.show()
