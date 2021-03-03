from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict, GridSearchCV
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.svm import SVC


def main_clf(metric_, clf_, grid_, range_=(2, 6), cv_=5, verb_=0, graphs=False):
    pipe = Pipeline(steps=[('clf', clf_)])
    # pipe = Pipeline(steps=[('sc', StandardScaler()), ('clf', clf_)])
    max_scoring = 0
    for k in range(*range_):
        denue_wide = pd.read_csv(f"summary/Count/denue_wide_{k}.csv")
        rezago = pd.read_csv("rezago_social/rezago_social.csv")
        rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON", "ALT", "BASSOLS"]]
        df = pd.merge(rezago_social, denue_wide, on=['Key'])
        y = rezago_social['lgc00_15cl3']
        df.drop(["lgc00_15cl3", "Key", "LAT", "LON", "ALT", "BASSOLS", "POB_TOTAL"], axis=1, inplace=True)
        X = df.div(df.sum(axis=1), axis=0)  # .div(df.POB_TOTAL, axis=0) * 1000
        #X["LAT"] = rezago_social["LAT"]
        # X["LON"] = rezago_social["LON"]
        # X["ALT"] = rezago_social["ALT"]
        # X["POB_TOTAL"] = rezago_social["POB_TOTAL"]
        dummies = pd.get_dummies(rezago_social["BASSOLS"], drop_first=True)
        X = pd.concat([X, dummies], axis=1)
        ###
        pd.set_option('display.max_columns', None)
        print(X.shape)
        print(X.columns)
        print(X.head(1))
        ###
        print(f'# CLF {k} {X.shape}')
        strat = rezago_social['lgc00_15cl3'].astype(str) + "_" + rezago_social["BASSOLS"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=strat, test_size=0.20, random_state=0)
        # verificar proporción
        clf_cv = GridSearchCV(pipe, grid_, cv=cv_, scoring=metric_, verbose=verb_)
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
    best_pipe = Pipeline(steps=[('clf', best_clf)])
    #best_pipe = Pipeline(steps=[('sc', StandardScaler()), ('clf', best_clf)])
    print('#BEST', best_pipe, max_scoring)
    best_pipe.fit(Xtrain, ytrain)
    print(f"# {best_k}: Train:{best_pipe.score(Xtrain, ytrain) * 100}")
    print(f"# {best_k}: Test:{best_pipe.score(Xtest, ytest) * 100}")
    scores = cross_val_score(best_pipe, X_, y_, cv=cv_, n_jobs=-1, scoring='accuracy')
    print(f"# {best_k}: Accuracy CV5:{np.mean(scores)} +/- {np.std(scores)}")
    scores_ = cross_val_score(best_pipe, X_, y_, cv=cv_, n_jobs=-1, scoring=metric_)
    print(f"# {best_k}: {metric_} CV5:{np.mean(scores_)} +/- {np.std(scores_)}")
    y_pred = cross_val_predict(best_pipe, X_, y_, cv=cv_)
    print(classification_report(y_, y_pred, digits=3))


if __name__ == '__main__':
    # Metrica de desempeño
    metric = 'f1_macro'

    # LR
    grid = {"clf__C": np.logspace(-4, 3, 8),
            # "clf__tol": np.logspace(-4, -1, 4),
            "clf__multi_class": ['ovr', 'multinomial']}
    clf = LogisticRegression(penalty='l2', solver='lbfgs', max_iter=10000, random_state=0)
    # main_clf(metric, clf, grid, range_=(3, 5), verb_=10)

    # SVM
    grid = [{"clf__kernel": ['rbf'],
             "clf__C": [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0],
             "clf__gamma": [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]},
            {"clf__kernel": ['sigmoid'],
             "clf__C": [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0],
             "clf__gamma": [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0],
             "clf__coef0": np.arange(0, 6, 1)},
            {"clf__kernel": ['poly'],
             "clf__gamma": [0.0001, 0.001, 0.01, 0.1, 1.0],
             "clf__degree": [2, 3, 4, 5],
             "clf__coef0": [0, 1, 2, 3, 4, 5]},
            ]
    clf = SVC(probability=True, random_state=0)
    # main_clf(metric, clf, grid, range_=(3, 5), verb_=10)

    grid = [{"clf__n_estimators": [150, 200, 250, 300, 350, 400, 450],
             "clf__criterion": ['entropy', 'gini'],
             "clf__max_features": ['sqrt', 'log2'],
             "clf__max_depth": [10, 15, 20, 25, 30, 35]}]
    clf = RandomForestClassifier(random_state=0)
    # main_clf(metric, clf, grid, range_=(2, 5), verb_=10)

    grid = {
        'clf__hidden_layer_sizes': [(200,), (300,), (400,), (500,)],
        'clf__activation': ['logistic', 'tanh', 'relu'],
        'clf__solver': ['adam'],
        'clf__alpha': np.logspace(-4, 3, 8),
        'clf__learning_rate': ['constant', 'adaptive'],
    }
    clf = MLPClassifier(random_state=0, max_iter=1500)
    # main_clf(metric, clf, grid, range_=(2, 6), verb_=10)

    grid = {
        'clf__n_estimators': np.arange(25, 401, 25),
        'clf__learning_rate': [0.01, 0.05, 0.1, 1],
    }
    clf = AdaBoostClassifier(random_state=0)
    #main_clf(metric, clf, grid, range_=(6, 7), verb_=10)

    grid = {
        'clf__max_leaf_nodes': np.arange(5, 51, 5),
        'clf__learning_rate': [0.01, 0.05, 0.1, 1],
        'clf__scoring': ['f1_macro'],
    }
    clf = HistGradientBoostingClassifier(random_state=0)
    main_clf(metric, clf, grid, range_=(2, 7), verb_=10)
