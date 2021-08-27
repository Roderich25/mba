# Pandas, NumPy
import pandas as pd
import numpy as np
# Scikit-learn
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.preprocessing import StandardScaler
# Keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.callbacks import EarlyStopping
from keras import backend as K

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
print(np.unique(y))

df.drop(["lgc00_15cl3_2", "Key", "LAT", "LON"], axis=1, inplace=True)
X = df.div(df.POB_TOTAL, axis=0) * 1000
X.drop(["POB_TOTAL"], axis=1, inplace=True)
X["LAT"] = rezago_social["LAT"]
X["LON"] = rezago_social["LON"]
# X["POB_TOTAL"] = rezago_social["POB_TOTAL"]
print(X.columns)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y_original, test_size=0.20, random_state=0)
# !pip install --force-reinstall --no-deps git+https://github.com/ck37/coral-ordinal/
import coral_ordinal as coral
from sklearn.metrics import balanced_accuracy_score, accuracy_score, f1_score
from keras.callbacks import EarlyStopping
from keras.initializers import GlorotUniform
from tensorflow.keras import regularizers
import tensorflow as tf
from scipy import special


def build_model(hl, af, l2, do):
    model = Sequential()
    model.add(Dense(hl, activation=af, kernel_regularizer=regularizers.l2(l2), kernel_initializer=GlorotUniform(seed=0),
                    input_shape=(93,)))
    model.add(Dropout(do, seed=0))
    model.add(coral.CoralOrdinal(3))
    model.compile(optimizer='adam',
                  loss=coral.OrdinalCrossEntropy(num_classes=3),
                  metrics=[coral.MeanAbsoluteErrorLabels()])
    return model


tf.random.set_seed(0)  # seed
for hl in range(2, 257, 1):
    for af in ['sigmoid', 'relu', 'tanh']:
        for l2 in [0, 0.0001, 0.001, 0.01, 0.1]:
            for do in [0.2, 0.35, 0.5]:
                ord_acc = []
                f1_mac = []
                ord_acc_2 = []
                f1_mac_2 = []
                kf = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
                Xtrain, ytrain = X_train.to_numpy(), y_train.to_numpy()  #
                #Xtrain, ytrain = X.to_numpy(), y.to_numpy()  #
                for train, test in kf.split(Xtrain, ytrain):
                    part_X_train, X_val = Xtrain[train, :], Xtrain[test, :]
                    part_y_train, y_val = ytrain[train], ytrain[test]
                    sc = StandardScaler()
                    part_X_train = sc.fit_transform(part_X_train)
                    X_val = sc.transform(X_val)
                    model = build_model(hl, af, l2, do)
                    tf.random.set_seed(0)  # seed
                    history = model.fit(part_X_train, part_y_train, verbose=0, epochs=200, validation_data=(X_val, y_val))
                    ordinal_logits = model.predict(X_val)
                    cum_probs = pd.DataFrame(ordinal_logits).apply(special.expit)
                    y_pred = cum_probs.apply(lambda x: x > 0.5).sum(axis=1).values
                    y_val_ = y_val
                    ord_acc.append(accuracy_score(y_val_, y_pred))
                    f1_mac.append(f1_score(y_val_, y_pred, average='macro'))
                    tensor_probs = coral.ordinal_softmax(ordinal_logits)
                    probs_df = pd.DataFrame(tensor_probs.numpy())
                    y_pred_2 = probs_df.idxmax(axis=1).values
                    ord_acc_2.append(accuracy_score(y_val_, y_pred_2))
                    f1_mac_2.append(f1_score(y_val_, y_pred_2, average='macro'))
                print(f'#(1,2) hl:{hl}, af:{af}, l2:{l2}, do:{do}, acc:{np.mean(ord_acc)}, f1:{np.mean(f1_mac)}, acc:{np.mean(ord_acc_2)}, f1:{np.mean(f1_mac_2)}')
