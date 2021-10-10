from matplotlib.lines import Line2D
import geopandas as gpd
# Pandas, NumPy, Matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Scikit-learn
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, mean_absolute_error, precision_score, recall_score
# Keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.callbacks import EarlyStopping
from keras import backend as K
from sklearn.metrics import balanced_accuracy_score, accuracy_score, f1_score, classification_report
from keras.callbacks import EarlyStopping
from keras.initializers import GlorotUniform
from tensorflow.keras import regularizers
import tensorflow as tf


def ordinal_accuracy(y_true, y_pred):
    y_pred_labels = K.round(y_pred)  # redondea
    y_pred_class = K.sum(y_pred_labels, axis=-1)  # suma
    y_true_class = K.sum(y_true, axis=-1)
    return K.cast(K.equal(y_true_class, y_pred_class), K.floatx())


def build_model(hl, af, l2, sh, nn):
    m = Sequential()
    m.add(Dense(hl, activation=af, kernel_initializer=GlorotUniform(seed=0), kernel_regularizer=regularizers.l2(l2),
                input_shape=(sh,)))
    for _ in range(nn - 1):
        m.add(
            Dense(hl, activation=af, kernel_initializer=GlorotUniform(seed=0), kernel_regularizer=regularizers.l2(l2)))
    m.add(Dense(3, activation='sigmoid'))
    m.compile(optimizer='adam',
              loss='mean_squared_error',
              metrics=[ordinal_accuracy])
    return m


tf.random.set_seed(0)  # seed
for dn in [3]:
    # SCIAN 3 (nivel subsector)
    denue_wide = pd.read_csv(f"summary/Count/denue_wide_{dn}.csv")  # Carga desde repositorio GitHub
    rezago = pd.read_csv("rezago_social/rezago_social.csv")  # Carga desde repositorio GitHub
    denue_wide = pd.read_csv(
        "https://raw.githubusercontent.com/Roderich25/datasets/main/denue_wide_3.csv")  # Carga desde repositorio GitHub
    rezago = pd.read_csv(
        "https://raw.githubusercontent.com/Roderich25/datasets/main/rezago_social.csv")  # Carga desde repositorio GitHub
    rezago_social = rezago[["lgc00_15cl3_2", "Key", "POB_TOTAL", "LAT", "LON"]]
    df = pd.merge(rezago_social, denue_wide, on=['Key'])
    df = df[df['lgc00_15cl3_2'] > 0]
    y_original = df['lgc00_15cl3_2']#.map({1: 3, 2: 2, 3: 1})

    # Transformación Cheng
    onehot = np.zeros((y_original.shape[0], 3))
    for idx, val in enumerate(y_original.astype(int)):
        onehot[idx, :val] = 1.
    y_onehot = onehot
    y = y_onehot

    df.drop(["lgc00_15cl3_2", "Key", "LAT", "LON"], axis=1, inplace=True)
    X = df.div(df.POB_TOTAL, axis=0) * 1000
    X.drop(["POB_TOTAL"], axis=1, inplace=True)
    X["LAT"] = rezago_social["LAT"]
    X["LON"] = rezago_social["LON"]
    X["POB_TOTAL"] = rezago_social["POB_TOTAL"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y_original, test_size=0.20, random_state=0)
    for hl in [229]:  # range(2, 257, 1):
        for af in ['relu']:  # ['sigmoid', 'relu', 'tanh']:
            for l2 in [0.001]:  # [0, 0.0001, 0.001, 0.01, 0.1]:
                for nn in [1]:  # [1, 2, 3]:
                    loss_train = []
                    loss_val = []
                    ord_acc = []
                    f1_mac = []
                    mae_score = []
                    kf = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
                    Xtrain, ytrain = X_train.to_numpy(), y_train  #
                    # Xtrain, ytrain = X.to_numpy(), y  #
                    for train, test in kf.split(Xtrain, np.sum(ytrain, axis=1)):
                        part_X_train, X_val = Xtrain[train, :], Xtrain[test, :]
                        part_y_train, y_val = ytrain[train, :], ytrain[test, :]
                        sc = StandardScaler()
                        part_X_train = sc.fit_transform(part_X_train)
                        X_val = sc.transform(X_val)
                        model = build_model(hl, af, l2, X.shape[1], nn)
                        tf.random.set_seed(0)  # seed
                        history = model.fit(part_X_train, part_y_train, verbose=0, epochs=200,  # 15,
                                            callbacks=[EarlyStopping(patience=1, restore_best_weights=True)],
                                            validation_data=(X_val, y_val))
                        print(len(history.history['loss']))#15

                        loss_train.append(history.history['loss'])
                        loss_val.append(history.history['val_loss'])
                        y_pred = np.sum(np.round(model.predict(X_val)), axis=1)
                        y_val_ = np.sum(y_val, axis=1)
                        ord_acc.append(accuracy_score(y_val_, y_pred))
                        f1_mac.append(f1_score(y_val_, y_pred, average='macro'))
                        mae_score.append(mean_absolute_error(y_val_, y_pred))
                        # print(classification_report(y_val_, y_pred, digits=3))
                        print('P', precision_score(y_val_, y_pred, average=None))
                        print('S', recall_score(y_val_, y_pred, average=None))
                    print(ord_acc)
                    print(f1_mac)
                    print(mae_score)
                    print(f'# dn:{dn}, nn:{nn}, hl:{hl}, af:{af}, l2:{l2},',
                        f'acc:{np.mean(ord_acc)}+/-{np.std(ord_acc)},',
                        f'f1:{np.mean(f1_mac)}+/-{np.std(f1_mac)}',
                        f'mae:{np.mean(mae_score)}+/-{np.std(mae_score)}')
                    # mean_loss_train = np.array(loss_train).mean(axis=0)
                    # mean_loss_val = np.array(loss_val).mean(axis=0)
                    # epochs = range(1, 1 + len(mean_loss_val))
                    # plt.plot(epochs, mean_loss_train, 'k--', label='Entrenamiento')
                    # plt.plot(epochs, mean_loss_val, 'k', label='Validación')
                    # plt.legend()
                    # plt.show()
                    # np.save('early/ann_ord_train.npy', mean_loss_train)
                    # np.save('early/ann_ord_val.npy', mean_loss_val)
