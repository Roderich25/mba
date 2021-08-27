from sklearn.model_selection import train_test_split, KFold, StratifiedKFold
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import classification_report, accuracy_score, f1_score
from neuralnet import NeuralNetMLP
import pandas as pd
import numpy as np

# SCIAN 3
denue_wide = pd.read_csv(f"summary/Count/denue_wide_3.csv")
rezago = pd.read_csv("rezago_social/rezago_social.csv")
rezago_social = rezago[["lgc00_15cl3_2", "Key", "POB_TOTAL", "LAT", "LON"]]
df = pd.merge(rezago_social, denue_wide, on=['Key'])
y = rezago_social['lgc00_15cl3_2']
df.drop(["lgc00_15cl3_2", "Key", "LAT", "LON"], axis=1, inplace=True)
X = df.div(df.POB_TOTAL, axis=0) * 1000
X.drop(["POB_TOTAL"], axis=1, inplace=True)
X["LAT"] = rezago_social["LAT"]
X["LON"] = rezago_social["LON"]
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.20, random_state=0)


for scaler in [StandardScaler, MinMaxScaler]:
    for hid in range(34, 35):
        for rid in [0.001]:#[0, 0.0001, 0.001, 0.01, 0.1, 1]:
            for et in [0.01]:#[0.0001, 0.0005, 0.001, 0.005, 0.01]:
                kf = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
                acc_val = []
                f1_val = []
                for train, test in kf.split(X, y):
                # for train, test in kf.split(X_train, y_train):
                    Xtrain, ytrain = X.to_numpy(), y.to_numpy()
                    # Xtrain, ytrain = X_train.to_numpy(), y_train.to_numpy()
                    partial_X_train, X_val, partial_y_train, y_val = Xtrain[train, :], Xtrain[test, :], ytrain[train], \
                                                                     ytrain[test]
                    sc = scaler()
                    partial_X_train = sc.fit_transform(partial_X_train)
                    X_val = sc.transform(X_val)
                    nn = NeuralNetMLP(n_hidden=hid, epochs=56, l2=rid, eta=et, seed=0)
                    nn.fit(X_train=partial_X_train, y_train=partial_y_train, X_valid=X_val, y_valid=y_val)
                    acc_val.append(nn.eval_['valid_acc'])
                    f1_val.append(nn.eval_['valid_f1'])
                    print("\n")
                f1_mean_vec = [np.mean(k) for k in zip(*f1_val)]
                acc_mean_vec = [np.mean(k) for k in zip(*acc_val)]
                # print(' ### {', hid, rid, et, '}, max_acc:', np.max(acc_mean_vec), np.argmax(acc_mean_vec) + 1,
                #      ', max_f1:', np.max(f1_mean_vec), np.argmax(f1_mean_vec) + 1)
                print(' ### {', hid, rid, et, '}, max_acc:', np.max(acc_mean_vec[-1]), ', max_f1:', np.max(f1_mean_vec[-1]))


    # print(np.unique(nn.predict(X_test)))
