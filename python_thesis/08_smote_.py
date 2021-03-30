from imblearn.over_sampling import SMOTE
import pandas as pd
import numpy as np
from imblearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score, cross_val_predict, \
    RandomizedSearchCV
from collections import Counter

# from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def main_clf(metric_, clf_, grid_, range_=(2, 3), cv_=5, verb_=False):
    max_scoring = 0
    pipe = Pipeline(steps=[('sc', StandardScaler()), ('sampling', SMOTE(random_state=0)), ('clf', clf_)])
    for k in range(*range_):
        denue_wide = pd.read_csv(f"summary/Count/denue_wide_{k}.csv")
        rezago = pd.read_csv("rezago_social/rezago_social.csv")
        rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON"]]
        df = pd.merge(rezago_social, denue_wide, on=['Key'])
        y = rezago_social['lgc00_15cl3']
        df.drop(["lgc00_15cl3", "Key", "LAT", "LON"], axis=1, inplace=True)
        X = df.div(df.POB_TOTAL, axis=0) * 1000
        X.drop(["POB_TOTAL"], axis=1, inplace=True)
        X["LAT"] = rezago_social["LAT"]
        X["LON"] = rezago_social["LON"]
        print(f'# CLF {k} {X.shape}')
        X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.20, random_state=0)
        # SMOTE
        c1 = Counter()
        # c2 = Counter()
        c1.update(y_train)
        print(c1)
        # print(X_train.shape, y_train.shape, c1)
        # sm = SMOTE(random_state=0)
        # X_train_sm, y_train_sm = sm.fit_resample(X_train, y_train.ravel())
        # c2.update(y_train_sm)
        # print(X_train.shape, y_train.shape, c2)
        # clf_cv = GridSearchCV(pipe, grid_, cv=cv_, scoring=metric_, verbose=verb_)  # cv_
        clf_cv = RandomizedSearchCV(pipe, grid_, cv=cv_, scoring=metric_, verbose=verb_, random_state=0)  # cv_
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
    best_pipe = Pipeline(steps=[('sc', StandardScaler()), ('sampling', SMOTE(random_state=0)), ('clf', best_clf)])
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
            "clf__multi_class": ['ovr', 'multinomial'],
            "clf__class_weight": [{1: 1, 2: 1, 3: 2}, {1: 1, 2: 1, 3: 3}, {1: 1, 2: 1, 3: 5}, {1: 1, 2: 1, 3: 10}],
            "clf__solver": ['lbfgs', 'saga']}
    clf = LogisticRegression(penalty='l2', random_state=0, max_iter=10000)
    main_clf(metric, clf, grid, range_=(2, 5), verb_=10)

    # RF
    grid = [{"clf__n_estimators": [100, 150, 200, 250, 300, 350, 400],
             "clf__criterion": ['entropy', 'gini'],
             "clf__max_features": ['sqrt', 'log2'],
             "clf__max_depth": [5, 10, 15, 20, 25, 30, 35, 40]}]
    clf = RandomForestClassifier(random_state=0)
    # main_clf(metric, clf, grid, range_=(3, 6), verb_=10)
