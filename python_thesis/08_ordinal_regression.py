from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, label_binarize
import numpy as np
import pandas as pd
from mord import LogisticIT, LogisticAT
from sklearn.base import clone
from matplotlib import pyplot as plt
from itertools import cycle



def main_at():
    min_mae = 9999
    for folder in ["Count"]:
        for k in range(2, 3):
            denue_wide = pd.read_csv(f"summary/{folder}/denue_wide_{k}.csv")
            rezago = pd.read_csv("rezago_social/rezago_social.csv")
            rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL"]]
            df = pd.merge(rezago_social, denue_wide, on=['Key'])
            df.drop(['Key'], axis=1, inplace=True)
            y = df['lgc00_15cl3']
            X = df.iloc[:, 2:].div((df.POB_TOTAL / 1000), axis=0)
            print(f'# {folder} {k} {X.shape}')
            X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.20,
                                                                random_state=0)
            for c in [0, 0.0001, 0.001, 0.01, 0.1, 0.5, 1.0, 2, 10.0, 100.0, 1000.0]:
                clf = LogisticAT(alpha=c)
                pipeline = make_pipeline(StandardScaler(), clf)
                scores = cross_val_score(pipeline, X_train, y_train, cv=10, n_jobs=-1,
                                         scoring='neg_mean_absolute_error') * -1
                print('\t#', k, c, np.mean(scores))
                if np.mean(scores) < min_mae:
                    min_mae = np.mean(scores)
                    best_clf = clone(clf)
                    best_folder = folder
                    best_k = k
                    Xtrain, ytrain = X_train, y_train
                    Xtest, ytest = X_test, y_test
    print(best_clf, min_mae)
    best_pipe = make_pipeline(StandardScaler(), best_clf)
    best_pipe.fit(Xtrain, ytrain)
    print(f"# {best_folder}, {best_k}: {best_clf} Train:{best_pipe.score(Xtrain, ytrain) * 100}")  # Check
    print(f"# {best_folder}, {best_k}: {best_clf} Test:{best_pipe.score(Xtest, ytest) * 100}")  # Check


# LogisticIT(alpha=100.0) 0.7007536517144929
# Count, 4: LogisticIT(alpha=100.0) Train:75.92875318066157
# Count, 4: LogisticIT(alpha=100.0) Test:67.6829268292683

def main_it():
    max_accuracy = 0
    for folder in ["Count"]:
        for k in range(2, 7):
            denue_wide = pd.read_csv(f"summary/{folder}/denue_wide_{k}.csv")
            rezago = pd.read_csv("rezago_social/rezago_social.csv")
            rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL"]]
            df = pd.merge(rezago_social, denue_wide, on=['Key'])
            df.drop(['Key'], axis=1, inplace=True)
            y = df['lgc00_15cl3']
            X = df.iloc[:, 2:].div((df.POB_TOTAL / 1000), axis=0)
            print(f'# {folder} {k} {X.shape}')
            X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.20,
                                                                random_state=0)
            for c in [0, 0.0001, 0.001, 0.01, 0.1, 0.5, 1.0, 2, 10.0, 100.0, 1000.0]:
                print('\t#', k, c)
                clf = LogisticIT(alpha=c)
                pipeline = make_pipeline(StandardScaler(), clf)
                scores = cross_val_score(pipeline, X_train, y_train, cv=10, n_jobs=-1)
                if np.mean(scores) > max_accuracy:
                    max_accuracy = np.mean(scores)
                    best_clf = clone(clf)
                    best_folder = folder
                    best_k = k
                    Xtrain, ytrain = X_train, y_train
                    Xtest, ytest = X_test, y_test
    print(best_clf, max_accuracy)
    best_pipe = make_pipeline(StandardScaler(), best_clf)
    best_pipe.fit(Xtrain, ytrain)
    print(f"# {best_folder}, {best_k}: {best_clf} Train:{best_pipe.score(Xtrain, ytrain) * 100}")
    print(f"# {best_folder}, {best_k}: {best_clf} Test:{best_pipe.score(Xtest, ytest) * 100}")


if __name__ == '__main__':
    main_it()
