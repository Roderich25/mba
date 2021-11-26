from matplotlib.lines import Line2D
import geopandas as gpd
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping
from keras import backend as K
import matplotlib.pyplot as plt
import coral_ordinal as coral
from sklearn.metrics import accuracy_score, f1_score, mean_absolute_error, precision_score, recall_score
from keras.callbacks import EarlyStopping
from keras.initializers import GlorotUniform
from tensorflow.keras import regularizers
import tensorflow as tf
from scipy import special

denue_wide = pd.read_csv("https://raw.githubusercontent.com/Roderich25/datasets/main/denue_wide_3.csv")
rezago = pd.read_csv("https://raw.githubusercontent.com/Roderich25/datasets/main/rezago_social.csv")
rezago_social = rezago[["lgc00_15cl3_2", "Key", "POB_TOTAL", "LAT", "LON"]]
df = pd.merge(rezago_social, denue_wide, on=['Key'])

y_original = rezago_social['lgc00_15cl3_2']
y = y_original - 1
print(y)

df.drop(["lgc00_15cl3_2", "Key", "LAT", "LON"], axis=1, inplace=True)
X = df.div(df.POB_TOTAL, axis=0) * 1000
X.drop(["POB_TOTAL"], axis=1, inplace=True)
X["LAT"] = rezago_social["LAT"]
X["LON"] = rezago_social["LON"]
X["POB_TOTAL"] = rezago_social["POB_TOTAL"]
print(X.columns)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y_original, test_size=0.20, random_state=0)


def build_model(hl, af, l2, sh, nn):
    m = Sequential()
    m.add(Dense(hl, activation=af, kernel_regularizer=regularizers.l2(l2), kernel_initializer=GlorotUniform(seed=0),
                input_shape=(sh,)))
    for _ in range(nn - 1):
        m.add(
            Dense(hl, activation=af, kernel_initializer=GlorotUniform(seed=0), kernel_regularizer=regularizers.l2(l2)))
    m.add(coral.CoralOrdinal(3))
    m.compile(optimizer='adam',
              loss=coral.OrdinalCrossEntropy(num_classes=3),
              metrics=[coral.MeanAbsoluteErrorLabels()])
    return m


tf.random.set_seed(0)  # seed
for hl in [4]:  # range(4, 257, 4):
    for af in ['relu']:  # ['sigmoid', 'relu', 'tanh']:
        for l2 in [0.001]:  # [0.0, 0.0001, 0.001, 0.01]:
            for nn in [2]:  # [1, 2, 3]:
                loss_train = []
                loss_val = []
                ord_acc = []
                f1_mac = []
                mae_score = []
                kf = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
                Xtrain, ytrain = X_train.to_numpy(), y_train.to_numpy()  #
                for train, test in kf.split(Xtrain, ytrain):
                    part_X_train, X_val = Xtrain[train, :], Xtrain[test, :]
                    part_y_train, y_val = ytrain[train], ytrain[test]
                    sc = StandardScaler()
                    part_X_train = sc.fit_transform(part_X_train)
                    X_val = sc.transform(X_val)
                    model = build_model(hl, af, l2, 94, nn)
                    tf.random.set_seed(0)
                    history = model.fit(part_X_train, part_y_train, verbose=0, epochs=200,
                                        callbacks=[EarlyStopping(patience=1, restore_best_weights=True)],
                                        validation_data=(X_val, y_val))
                    loss_train.append(history.history['loss'])
                    loss_val.append(history.history['val_loss'])
                    print(len(history.history['loss']))
                    ordinal_logits = model.predict(X_val)
                    cum_probs = pd.DataFrame(ordinal_logits).apply(special.expit)
                    y_pred = cum_probs.apply(lambda x: x > 0.5).sum(axis=1).values
                    y_val_ = y_val
                    ord_acc.append(accuracy_score(y_val_, y_pred))
                    f1_mac.append(f1_score(y_val_, y_pred, average='macro'))
                    mae_score.append(mean_absolute_error(y_val_, y_pred))
                print(f'# hl:{hl}, af:{af}, l2:{l2}, nn:{nn},',
                      f'acc:{np.mean(ord_acc)}+/-{np.std(ord_acc)},',
                      f'f1:{np.mean(f1_mac)}+/-{np.std(f1_mac)},',
                      f'mae:{np.mean(mae_score)}+/-{np.std(mae_score)}')
# hl:4, af:relu, l2:0.001, nn:2, acc:0.7277353689567431+/-0.01820716928244105,
# f1:0.7113254686052193+/-0.01759715506664418, mae:0.2783715012722646+/-0.01974921924878601

tf.random.set_seed(0)  # seed
for hl in [4]:  # range(4, 257, 4):
    for af in ['relu']:  # ['sigmoid', 'relu', 'tanh']:
        for l2 in [0.001]:  # [0.0, 0.0001, 0.001, 0.01]:
            for nn in [2]:  # [1, 2, 3]:
                loss_train = []
                loss_val = []
                ord_acc = []
                f1_mac = []
                mae_score = []
                kf = StratifiedKFold(n_splits=10, shuffle=True, random_state=0)
                Xtrain, ytrain = X.to_numpy(), y.to_numpy()  #
                for train, test in kf.split(Xtrain, ytrain):
                    part_X_train, X_val = Xtrain[train, :], Xtrain[test, :]
                    part_y_train, y_val = ytrain[train], ytrain[test]
                    sc = StandardScaler()
                    part_X_train = sc.fit_transform(part_X_train)
                    X_val = sc.transform(X_val)
                    model = build_model(hl, af, l2, 94, nn)
                    tf.random.set_seed(0)
                    history = model.fit(part_X_train, part_y_train, verbose=0, epochs=200,
                                        callbacks=[EarlyStopping(patience=1, restore_best_weights=True)],
                                        validation_data=(X_val, y_val))
                    loss_train.append(history.history['loss'])
                    loss_val.append(history.history['val_loss'])
                    ordinal_logits = model.predict(X_val)
                    cum_probs = pd.DataFrame(ordinal_logits).apply(special.expit)
                    y_pred = cum_probs.apply(lambda x: x > 0.5).sum(axis=1).values
                    y_val_ = y_val
                    ord_acc.append(accuracy_score(y_val_, y_pred))
                    f1_mac.append(f1_score(y_val_, y_pred, average='macro'))
                    mae_score.append(mean_absolute_error(y_val_, y_pred))
                    print('P', precision_score(y_val_, y_pred, average=None))
                    print('S', recall_score(y_val_, y_pred, average=None))
                print(ord_acc)
                print(f1_mac)
                print(mae_score)
                print(f'# hl:{hl}, af:{af}, l2:{l2}, nn:{nn},',
                      f'acc:{np.mean(ord_acc)}+/-{np.std(ord_acc)},',
                      f'f1:{np.mean(f1_mac)}+/-{np.std(f1_mac)},',
                      f'mae:{np.mean(mae_score)}+/-{np.std(mae_score)}')
                gdf = gpd.read_file('municipios/areas_geoestadisticas_municipales.shp')
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
                txt = "Categorías de Rezago Social sugeridas por Vargas-Chanes y Váldez-Cruz (2019)."
                ax1.text(0.01, 0.01, txt, wrap=True, horizontalalignment='left', fontsize=12, **csfont)
                ax1.legend(handles=legend_elements)
                gdf = gpd.read_file('municipios/areas_geoestadisticas_municipales.shp')
                gdf['Key'] = gdf['CVE_ENT'] + gdf['CVE_MUN']
                rezago = pd.read_csv("rezago_social/rezago_social.csv")
                rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON"]]
                rezago_social['Key'] = rezago_social['Key'].astype(str).str.zfill(5)
                model = build_model(hl, af, l2, 94, nn)
                sc = StandardScaler()
                X = sc.fit_transform(X.to_numpy())
                model.fit(X, y, verbose=0, epochs=200,
                          callbacks=[EarlyStopping(monitor='loss', patience=1, restore_best_weights=True)])
                ordinal_logits = model.predict(X)
                cum_probs = pd.DataFrame(ordinal_logits).apply(special.expit)
                y_pred = cum_probs.apply(lambda x: x > 0.5).sum(axis=1).values + 1
                rezago_social['Pred'] = y_pred
                gdf = gdf.merge(rezago_social, on='Key')
                colors = {1: 'red', 2: 'yellow', 3: 'green'}
                gdf.plot(ax=ax2, color=gdf['Pred'].map(colors))
                ax2.set_xticks([])
                ax2.set_yticks([])
                txt = "Categorías predichas por modelo DLNN-ORD para 2015"
                ax2.text(0.01, 0.01, txt, wrap=True, horizontalalignment='left', fontsize=12, **csfont)
                ax2.legend(handles=legend_elements)
                plt.show()