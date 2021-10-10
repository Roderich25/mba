import pandas as pd
import numpy as np
import tensorflow as tf
from keras.utils.np_utils import to_categorical
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping
from keras.initializers import GlorotUniform
from tensorflow.keras import regularizers
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, f1_score, mean_absolute_error

denue_wide = pd.read_csv("https://raw.githubusercontent.com/Roderich25/datasets/main/denue_wide_3.csv")
rezago = pd.read_csv("https://raw.githubusercontent.com/Roderich25/datasets/main/rezago_social.csv")
rezago_social = rezago[["lgc00_15cl3_2", "Key", "POB_TOTAL", "LAT", "LON"]]
df = pd.merge(rezago_social, denue_wide, on=['Key'])
y_original = rezago_social['lgc00_15cl3_2']
y = to_categorical(y_original - 1)
df.drop(["lgc00_15cl3_2", "Key", "LAT", "LON"], axis=1, inplace=True)
X = df.div(df.POB_TOTAL, axis=0) * 1000
X.drop(["POB_TOTAL"], axis=1, inplace=True)
X["LAT"] = rezago_social["LAT"]
X["LON"] = rezago_social["LON"]
X["POB_TOTAL"] = rezago_social["POB_TOTAL"]
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.20, random_state=0)

def build_model(hl, af, l2, sh, nn):
    model = Sequential()
    model.add(Dense(hl, activation=af, kernel_regularizer=regularizers.l2(l2), kernel_initializer=GlorotUniform(seed=0),
                    input_shape=(sh,)))
    for _ in range(nn - 1):
        model.add(
            Dense(hl, activation=af, kernel_initializer=GlorotUniform(seed=0), kernel_regularizer=regularizers.l2(l2)))
    model.add(Dense(3, activation='softmax'))
    model.compile(optimizer='adam',
                  loss='mean_absolute_error',
                  metrics=['accuracy'])
    return model

X_val_train, X_val_test, y_val_train, y_val_test = train_test_split(X_train, y_train, stratify=y_train, test_size=0.20, random_state=0)
model = build_model(24, 'tanh', 0.001, X.shape[1], 3)
tf.random.set_seed(0)
history = model.fit(X_val_train, y_val_train, verbose=0, epochs=200,
                    #callbacks=[EarlyStopping(patience=1, restore_best_weights=True)],
                              validation_data=(X_val_test, y_val_test))
# print(len(history.history['loss']))
# print(len(history.history['val_loss']))
epochs = range(1, 201)
plt.plot(epochs, history.history['loss'], 'k--', label='Entrenamiento')
plt.plot(epochs, history.history['val_loss'], 'k', label='Validación')
plt.title('ANN-NOM')
plt.ylabel('función de costo')
plt.xlabel('número de pasadas')
plt.legend()
plt.show()

y_val_pred = np.argmax(model.predict(X_val_test), axis=1)
y_val_test_ = np.argmax(y_val_test, axis=1)
print('acc_temp', accuracy_score(y_val_test_, y_val_pred))
print('f1_temp', f1_score(y_val_test_, y_val_pred, average='macro'))
print('mae_temp', mean_absolute_error(y_val_test_, y_val_pred))

model = build_model(24, 'tanh', 0.001, X.shape[1], 3)
tf.random.set_seed(0)
history = model.fit(X_train, y_train, verbose=0, epochs=200,
                    # callbacks=[EarlyStopping(patience=1, restore_best_weights=True)],
                    validation_data=(X_test, y_test))
# print(len(history.history['loss']))
# print(len(history.history['val_loss']))
epochs = range(1, 201)
plt.plot(epochs, history.history['loss'], 'k--', label='Entrenamiento')
plt.plot(epochs, history.history['val_loss'], 'k', label='Validación')
plt.title('ANN-NOM')
plt.ylabel('función de costo')
plt.xlabel('número de pasadas')
plt.legend()
plt.show()

y_pred = np.argmax(model.predict(X_test), axis=1)
y_test_ = np.argmax(y_test, axis=1)
print('acc_temp', accuracy_score(y_test_, y_pred))
print('f1_temp', f1_score(y_test_, y_pred, average='macro'))
print('mae_temp', mean_absolute_error(y_test_, y_pred))

