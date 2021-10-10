from matplotlib.lines import Line2D
import geopandas as gpd
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout
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


def build_model(hl, af, do, sh, nn):
    m = Sequential()
    m.add(Dense(hl, activation=af, kernel_initializer=GlorotUniform(seed=0),
                input_shape=(sh,)))
    m.add(Dropout(do, seed=0))
    for _ in range(nn - 1):
        m.add(
            Dense(hl, activation=af, kernel_initializer=GlorotUniform(seed=0)))
        m.add(Dropout(do, seed=0))
    m.add(coral.CoralOrdinal(3))
    m.compile(optimizer='adam',
              loss=coral.OrdinalCrossEntropy(num_classes=3),
              metrics=[coral.MeanAbsoluteErrorLabels()])
    return m


tf.random.set_seed(0)  # seed
for hl in range(4, 257, 4):
    for af in ['sigmoid', 'relu', 'tanh']:
        for do in [0.25, 0.5]:
            for nn in [1, 2, 3]:
                loss_train = []
                loss_val = []
                ord_acc = []
                f1_mac = []
                mae_score = []
                kf = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
                Xtrain, ytrain = X_train.to_numpy(), y_train.to_numpy()  #
                # Xtrain, ytrain = X.to_numpy(), y.to_numpy()  #
                for train, test in kf.split(Xtrain, ytrain):
                    part_X_train, X_val = Xtrain[train, :], Xtrain[test, :]
                    part_y_train, y_val = ytrain[train], ytrain[test]
                    sc = StandardScaler()
                    part_X_train = sc.fit_transform(part_X_train)
                    X_val = sc.transform(X_val)
                    model = build_model(hl, af, do, 94, nn)
                    tf.random.set_seed(0)
                    history = model.fit(part_X_train, part_y_train, verbose=0, epochs=200,
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
                    # print('P', precision_score(y_val_, y_pred, average=None))
                    # print('S', recall_score(y_val_, y_pred, average=None))
                # print(ord_acc)
                # print(f1_mac)
                # print(mae_score)
                print(f'# hl:{hl}, af:{af}, do:{do}, nn:{nn},',
                      f'acc:{np.mean(ord_acc)}+/-{np.std(ord_acc)},',
                      f'f1:{np.mean(f1_mac)}+/-{np.std(f1_mac)},',
                      f'mae:{np.mean(mae_score)}+/-{np.std(mae_score)}')
# hl:4, af:relu, l2:0.001, nn:2, acc:0.7277353689567431+/-0.01820716928244105,
# f1:0.7113254686052193+/-0.01759715506664418, mae:0.2783715012722646+/-0.01974921924878601
