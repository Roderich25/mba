import coral_ordinal as coral
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

# SCIAN 3
denue_wide = pd.read_csv(f"summary/Count/denue_wide_3.csv")
rezago = pd.read_csv("rezago_social/rezago_social.csv")
rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON"]]
df = pd.merge(rezago_social, denue_wide, on=['Key'])
y = rezago_social['lgc00_15cl3'] - 1
df.drop(["lgc00_15cl3", "Key", "LAT", "LON"], axis=1, inplace=True)
X = df.div(df.POB_TOTAL, axis=0) * 1000
X.drop(["POB_TOTAL"], axis=1, inplace=True)
X["LAT"] = rezago_social["LAT"]
X["LON"] = rezago_social["LON"]
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.20, random_state=0)
partition = int(X_train.shape[0] * 0.8)
sc = StandardScaler()
partial_X_train = sc.fit_transform(X_train[:partition])
X_val = sc.transform(X_train[partition:])
partial_y_train = y_train[:partition]
y_val = y_train[partition:]

NUM_CLASSES = 3
model = Sequential()
model.add(Dense(32, activation="relu"))
model.add(coral.CoralOrdinal(num_classes=NUM_CLASSES))  # Ordinal variable has 5 labels, 0 through 4.
model.compile(loss=coral.OrdinalCrossEntropy(num_classes=NUM_CLASSES),
              metrics=['accuracy'])

history = model.fit(partial_X_train, partial_y_train,
                    epochs=20,
                    validation_data=(X_val, y_val))
