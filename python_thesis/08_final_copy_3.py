import pandas as pd
from scipy.stats import f_oneway
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score, cross_val_predict, train_test_split, GridSearchCV
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.svm import SVC


def main_clf(metric_, clf_, grid_, range_=(2, 7), cv_=5, verb_=False):
    pipe = Pipeline(steps=[('sc', StandardScaler()), ('clf', clf_)])
    max_scoring = 0
    for k in range(*range_):
        denue_wide = pd.read_csv(f"summary/Count/denue_wide_{k}.csv")
        rezago = pd.read_csv("rezago_social/rezago_social.csv")
        rezago_social = rezago[['grs2015', "lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON", "ALT", "BASSOLS"]]
        df = pd.merge(rezago_social, denue_wide, on=['Key'])
        df = df.loc[df['grs2015'].isin(['Muy bajo', 'Bajo', 'Medio', 'Alto', 'Muy alto'])]
        df['grs2015'] = df['grs2015'].map({'Muy bajo': 1, 'Bajo': 1, 'Medio': 2, 'Alto': 3, 'Muy alto': 3})
        Key_ = 'grs2015'
        y = df[Key_]
        df.drop(['grs2015', "lgc00_15cl3", "Key", "LAT", "LON", "ALT", "BASSOLS", "POB_TOTAL"], axis=1, inplace=True)
        X = df.div(df.sum(axis=1), axis=0)  # .div(df.POB_TOTAL, axis=0) * 1000
        cols = []
        for col in df.columns[1:]:
            df_new = pd.concat([y, X[col]], axis=1)
            # print(col, df_new.groupby('lgc00_15cl3').mean().to_numpy().reshape((3,)))
            a = df_new[df_new[Key_] == 1][col].to_numpy().reshape((-1,))
            b = df_new[df_new[Key_] == 2][col].to_numpy().reshape((-1,))
            c = df_new[df_new[Key_] == 3][col].to_numpy().reshape((-1,))
            F, p = f_oneway(a, b, c)
            if p < 0.05:
                cols.append(col)
        print(X.shape)
        X = X[cols]
        X["LAT"] = rezago_social["LAT"]
        X["LON"] = rezago_social["LON"]
        print(X.columns)
        print(y.value_counts())
        print(y.value_counts(normalize=True))
        print(np.unique(y))
        ###
        print(f'# CLF {k} {X.shape}')
        X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.20, random_state=0)
        clf_cv = GridSearchCV(pipe, grid_, cv=cv_, scoring=metric_, verbose=verb_)  # cv_
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
    print(classification_report(y_, y_pred, digits=3))


if __name__ == '__main__':
    # Metrica de desempeño
    metric = 'f1_macro'

    # LR
    grid = {"clf__C": np.logspace(-4, 3, 8)}
    clf = LogisticRegression(penalty='l2', random_state=0, max_iter=2000)
    main_clf(metric, clf, grid, range_=(2, 7), verb_=10)

    grid = [{"clf__kernel": ['rbf'],
             "clf__C": [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0],
             "clf__gamma": [0.0001, 0.001, 0.01, 0.1]},
            {"clf__kernel": ['sigmoid'],
             "clf__C": [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0],
             "clf__gamma": [0.0001, 0.001, 0.01, 0.1],
             "clf__coef0": np.arange(0, 6, 1)},
            {"clf__kernel": ['poly'],
             "clf__C": [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0],
             "clf__gamma": [0.0001, 0.001, 0.01, 0.1],
             "clf__degree": [2, 3, 4],
             "clf__coef0": np.arange(0, 6, 1)},
            ]
    clf = SVC(probability=True, random_state=0)
    # main_clf(metric, clf, grid, range_=(2, 6), verb_=10)

    # RF
    grid = [{"clf__n_estimators": [100, 150, 200, 250, 300, 350, 400],
             "clf__criterion": ['entropy', 'gini'],
             "clf__max_features": ['sqrt', 'log2'],
             "clf__max_depth": [3, 5, 10, 15, 20, 25, 30, 35]}]
    clf = RandomForestClassifier(random_state=0)
    # main_clf(metric, clf, grid, range_=(2, 7), verb_=10)

    grid = {
        'clf__hidden_layer_sizes': [(100,), (200,), (300,), (400,), ],
        'clf__activation': ['logistic', 'tanh', 'relu'],
        # 'clf__alpha': np.logspace(-4, 3, 8),
        # 'clf__learning_rate': ['constant', 'adaptive'],
    }
    clf = MLPClassifier(random_state=0, max_iter=2000)
    # main_clf(metric, clf, grid, range_=(2, 7), verb_=10)
