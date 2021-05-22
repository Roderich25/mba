from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from neuralnet import NeuralNetMLP
import pandas as pd
import numpy as np

# SCIAN 3
denue_wide = pd.read_csv(f"summary/Count/denue_wide_3.csv")
rezago = pd.read_csv("rezago_social/rezago_social.csv")
rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON"]]
df = pd.merge(rezago_social, denue_wide, on=['Key'])
y = rezago_social['lgc00_15cl3']
df.drop(["lgc00_15cl3", "Key", "LAT", "LON"], axis=1, inplace=True)
X = df.div(df.POB_TOTAL, axis=0) * 1000
X.drop(["POB_TOTAL"], axis=1, inplace=True)
X["LAT"] = rezago_social["LAT"]
X["LON"] = rezago_social["LON"]
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.20, random_state=0)
#  Partición de validación
partition = int(X_train.shape[0] * 0.8)
print(X_train.shape, partition)
sc = StandardScaler()
partial_X_train = sc.fit_transform(X_train[:partition])
X_val = sc.transform(X_train[partition:])
partial_y_train = y_train[:partition]
y_val = y_train[partition:]
X_test = sc.transform(X_test)
nn = NeuralNetMLP(n_hidden=64, epochs=20, shuffle=False)
nn.fit(X_train=partial_X_train, y_train=partial_y_train,
       X_valid=X_val, y_valid=y_val)
print('\n', classification_report(y_test, nn.predict(X_test)))
