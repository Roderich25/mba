from matplotlib.lines import Line2D
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc, classification_report, plot_roc_curve, precision_recall_curve, \
    average_precision_score
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, label_binarize
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt, font_manager
from itertools import cycle
import geopandas as gpd
import matplotlib
import mord
import seaborn as sns
import scikitplot as skplt

matplotlib.rcParams['font.family'] = 'Times New Roman'
matplotlib.rcParams["font.weight"] = "bold"
matplotlib.rcParams["axes.labelweight"] = "bold"
from sklearn.neural_network import MLPClassifier


def main_clf(metric_, clf_, grid_, range_=(2, 7), cv_=5, verb_=False):
    pipe = Pipeline(steps=[('sc', StandardScaler()), ('clf', clf_)])
    max_scoring = 0
    for k in range(*range_):
        denue_wide = pd.read_csv(f"summary/Count/denue_wide_{k}.csv")  ###
        rezago = pd.read_csv("rezago_social/rezago_social.csv")
        rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON"]]
        df = pd.merge(rezago_social, denue_wide, on=['Key'])
        y0 = rezago_social['lgc00_15cl3']
        y = np.array([[1, 0, 0] if a == 1 else [1, 1, 0] if a == 2 else [1, 1, 1] for a in y0])
        df.drop(["lgc00_15cl3", "Key", "LAT", "LON"], axis=1, inplace=True)
        X = df.div(df.POB_TOTAL, axis=0) * 1000
        X.drop(["POB_TOTAL"], axis=1, inplace=True)
        X["LAT"] = rezago_social["LAT"]
        X["LON"] = rezago_social["LON"]
        print(f'# CLF {k} {X.shape}')
        X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.20, random_state=0)
        clf_cv = GridSearchCV(pipe, grid_, cv=5, scoring=metric_, verbose=verb_)  # cv_
        clf_cv.fit(X_train, y_train)
        if np.mean(clf_cv.best_score_) > max_scoring:
            max_scoring = clf_cv.best_score_
            print(f"\t # {k} CLF {clf_cv.best_score_} {clf_cv.best_params_}")
            best_params = clf_cv.best_params_
            best_k = k
            Xtrain, ytrain = X_train, y_train
            Xtest, ytest = X_test, y_test
            X_, y_ = X, y
    best_params_ = {k[5:]: v for k, v in best_params.items()}
    best_clf = clf_.set_params(**best_params_)
    best_pipe = Pipeline(steps=[('sc', StandardScaler()), ('clf', best_clf)])
    print('#BEST', best_pipe, max_scoring)
    best_pipe.fit(Xtrain, ytrain)
    print(f"# {best_k}: Train:{best_pipe.score(Xtrain, ytrain) * 100}")
    print(f"# {best_k}: Test:{best_pipe.score(Xtest, ytest) * 100}")
    scores = cross_val_score(best_pipe, X_, y_, cv=cv_, n_jobs=-1, scoring='accuracy')
    print(f"# {best_k}: Accuracy CV5:{np.mean(scores)} +/- {np.std(scores)}")
    scores_ = cross_val_score(best_pipe, X_, y_, cv=cv_, n_jobs=-1, scoring=metric_)
    print(f"# {best_k}: {metric_} CV5:{np.mean(scores_)} +/- {np.std(scores_)}")
    y_pred = cross_val_predict(best_pipe, X_, y_, cv=cv_)
    print(y_,y_pred)
    print(y_.shape, y_pred.shape)
    a_ = [sum(el) for el in y_]
    b_ = [sum(el) for el in y_pred]
    print(np.unique(a_),np.unique(b_))
    print(classification_report(a_, b_, digits=3))


if __name__ == '__main__':
    # Metrica de desempeño
    metric = 'f1_macro'
    # MLP
    grid = {
        'clf__hidden_layer_sizes': [(30,), (40,), (50,)],
        'clf__activation': ['relu', 'logistic'],
        'clf__solver': ['adam', 'lbfgs'],
        'clf__alpha': [0.05, 0.01],
        'clf__max_iter': [2000],
        'clf__learning_rate': ['constant', 'adaptive'],
    }
    #
    grid = {
        'clf__hidden_layer_sizes': [(40,)],
        'clf__activation': ['logistic'],
        'clf__solver': ['adam'],
        'clf__alpha': [0.05],
        'clf__max_iter': [2000],
        'clf__learning_rate': ['constant'],
    }
    clf = MLPClassifier(random_state=0)
    main_clf(metric, clf, grid, range_=(3, 4), verb_=10, cv_=10)
