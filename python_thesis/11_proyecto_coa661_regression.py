import pandas as pd
from sklearn.base import clone
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split, cross_val_score, cross_validate, cross_val_predict
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt


def plot_regression_results(y_true, y_pred, title, scores):
    plt.plot([y_true.min(), y_true.max()],
             [y_true.min(), y_true.max()],
             '--r', linewidth=2)
    plt.scatter(y_true, y_pred, alpha=0.2)

    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().get_xaxis().tick_bottom()
    plt.gca().get_yaxis().tick_left()
    plt.gca().spines['left'].set_position(('outward', 10))
    plt.gca().spines['bottom'].set_position(('outward', 10))
    plt.gca().set_xlim([y_true.min(), y_true.max()])
    plt.gca().set_ylim([y_true.min(), y_true.max()])
    plt.gca().set_xlabel('Observados')
    plt.gca().set_ylabel('Predichos')
    extra = plt.Rectangle((0, 0), 0, 0, fc="w", fill=False,
                          edgecolor='none', linewidth=0)
    plt.legend([extra], [scores], loc='upper left')
    title = title
    plt.gca().set_title(title)
    plt.show()


def main_mlp():
    scr = 'neg_mean_squared_error'
    min_scr = 999
    for k in range(2, 3):
        print("#K:", k)
        denue_wide = pd.read_csv(f"summary/Count/denue_wide_{k}.csv")
        rezago = pd.read_csv("rezago_social/rezago_coneval.csv")
        rezago_social = rezago[["grs2015", "p2015", "Key", "irs2015", "lat", "lon", "alt"]]
        df = pd.merge(rezago_social, denue_wide, on=['Key'])
        df.drop(['Key'], axis=1, inplace=True)
        y = df['irs2015']
        y2 = df['grs2015']
        X = df.iloc[:, 6:].div((df.p2015 / 1000), axis=0)
        X["p2015"] = rezago_social["p2015"]
        X["lat"] = rezago_social["lat"]
        X["lon"] = rezago_social["lon"]
        X["alt"] = rezago_social["alt"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y2, test_size=0.20,
                                                            random_state=0)
        rezago_lambda = lambda \
                x: 0 if x <= -1.007065 else 1 if x <= -0.325075 else 2 if x <= 0.35434 else 3 if x <= 1.717835 else 4
        for hl in [(50,)]:
            for af in ['logistic']:
                for lr in ['constant']:
                    for alp in [0.01]:
                        reg = MLPRegressor(hidden_layer_sizes=hl, activation=af, learning_rate=lr, max_iter=2000,
                                           alpha=alp, random_state=0)
                        pipe = make_pipeline(StandardScaler(), reg)
                        scores = cross_val_score(pipe, X_train, y_train, cv=10, n_jobs=-1, scoring=scr)
                        if -1 * np.mean(scores) < min_scr:
                            min_scr = -1 * np.mean(scores)
                            print(k, hl, af, lr, alp, np.mean(scores) * -1)
                            best_reg = clone(reg)
                            best_k = k
                            Xtrain, ytrain = X_train, y_train
                            Xtest, ytest = X_test, y_test
                            Xpred = X
    best_pipe = make_pipeline(StandardScaler(), best_reg)
    best_pipe.fit(Xtrain, ytrain)
    print(
        f"# {best_k}: {best_reg}, {np.mean(cross_val_score(best_pipe, Xtrain, ytrain, cv=5, n_jobs=-1, scoring=scr) * -1)}, Train:{np.mean(list(map(rezago_lambda, best_pipe.predict(Xtrain))) == ytrain.apply(rezago_lambda)) * 100}")
    print(
        f"# {best_k}: {best_reg}, {np.mean(cross_val_score(best_pipe, Xtest, ytest, cv=5, n_jobs=-1, scoring=scr) * -1)}, Test:{np.mean(list(map(rezago_lambda, best_pipe.predict(Xtest))) == ytest.apply(rezago_lambda)) * 100}")
    scores = cross_val_score(best_pipe, Xpred, y, cv=5, n_jobs=-1, scoring=scr)
    print('cv5:', np.mean(scores * -1), np.std(scores * -1),
          np.mean(list(map(rezago_lambda, best_pipe.predict(Xtest))) == ytest.apply(rezago_lambda)) * 100)
    score = cross_validate(best_pipe, X, y,
                           scoring=['r2', 'neg_mean_squared_error'],
                           n_jobs=-1, verbose=0)
    y_pred = cross_val_predict(best_pipe, X, y, n_jobs=-1, verbose=0)
    plot_regression_results(y, y_pred,
                            'Red Neuronal (MLP)',
                            (r'$R^2={:.2f} \pm {:.2f}$' + '\n' + r'$MSE={:.2f} \pm {:.2f}$')
                            .format(np.mean(score['test_r2']),
                                    np.std(score['test_r2']),
                                    -np.mean(score['test_neg_mean_squared_error']),
                                    np.std(score['test_neg_mean_squared_error'])))


def main_svm():
    scr = 'neg_mean_squared_error'
    min_scr = 999
    for k in range(2, 3):
        print("#K:", k)
        denue_wide = pd.read_csv(f"summary/Count/denue_wide_{k}.csv")
        rezago = pd.read_csv("rezago_social/rezago_coneval.csv")
        rezago_social = rezago[["grs2015", "p2015", "Key", "irs2015", "lat", "lon", "alt"]]
        df = pd.merge(rezago_social, denue_wide, on=['Key'])
        df.drop(['Key'], axis=1, inplace=True)
        y = df['irs2015']
        y2 = df['grs2015']
        X = df.iloc[:, 6:].div((df.p2015 / 1000), axis=0)
        X["p2015"] = rezago_social["p2015"]
        X["lat"] = rezago_social["lat"]
        X["lon"] = rezago_social["lon"]
        X["alt"] = rezago_social["alt"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y2, test_size=0.20, random_state=0)
        rezago_lambda = lambda \
                x: 0 if x <= -1.007065 else 1 if x <= -0.325075 else 2 if x <= 0.35434 else 3 if x <= 1.717835 else 4
        for kr in ['rbf']:
            for g in ['auto']:
                for c in [1]:
                    reg = SVR(C=c, kernel=kr, gamma=g)
                    pipe = make_pipeline(StandardScaler(), reg)
                    scores = cross_val_score(pipe, X_train, y_train, cv=10, n_jobs=-1, scoring=scr)
                    if -1 * np.mean(scores) < min_scr:
                        min_scr = -1 * np.mean(scores)
                        print(k, c, kr, g, np.mean(scores) * -1)
                        best_reg = clone(reg)
                        best_k = k
                        Xtrain, ytrain = X_train, y_train
                        Xtest, ytest = X_test, y_test
                        Xpred = X
    best_pipe = make_pipeline(StandardScaler(), best_reg)
    best_pipe.fit(Xtrain, ytrain)
    print(
        f"# {best_k}: {best_reg}, {np.mean(cross_val_score(best_pipe, Xtrain, ytrain, cv=5, n_jobs=-1, scoring=scr) * -1)}, Train:{np.mean(list(map(rezago_lambda, best_pipe.predict(Xtrain))) == ytrain.apply(rezago_lambda)) * 100}")
    print(
        f"# {best_k}: {best_reg}, {np.mean(cross_val_score(best_pipe, Xtest, ytest, cv=5, n_jobs=-1, scoring=scr) * -1)}, Test:{np.mean(list(map(rezago_lambda, best_pipe.predict(Xtest))) == ytest.apply(rezago_lambda)) * 100}")
    scores = cross_val_score(best_pipe, Xpred, y, cv=5, n_jobs=-1, scoring=scr)
    print('cv5:', np.mean(scores * -1), np.std(scores * -1),
          np.mean(list(map(rezago_lambda, best_pipe.predict(Xtest))) == ytest.apply(rezago_lambda)) * 100)
    score = cross_validate(best_pipe, X, y,
                           scoring=['r2', 'neg_mean_squared_error'],
                           n_jobs=-1, verbose=0)
    y_pred = cross_val_predict(best_pipe, X, y, n_jobs=-1, verbose=0)
    plot_regression_results(y, y_pred,
                            'Máquina de Soporte Vectorial (SVM)',
                            (r'$R^2={:.2f} \pm {:.2f}$' + '\n' + r'$MSE={:.2f} \pm {:.2f}$')
                            .format(np.mean(score['test_r2']),
                                    np.std(score['test_r2']),
                                    -np.mean(score['test_neg_mean_squared_error']),
                                    np.std(score['test_neg_mean_squared_error'])))


def main_rf():
    scr = 'neg_mean_squared_error'
    min_scr = 999
    for k in range(2, 3):
        print("#K:", k)
        denue_wide = pd.read_csv(f"summary/Count/denue_wide_{k}.csv")
        rezago = pd.read_csv("rezago_social/rezago_coneval.csv")
        rezago_social = rezago[["grs2015", "p2015", "Key", "irs2015", "lat", "lon", "alt"]]
        df = pd.merge(rezago_social, denue_wide, on=['Key'])
        df.drop(['Key'], axis=1, inplace=True)
        y = df['irs2015']
        y2 = df['grs2015']
        X = df.iloc[:, 6:].div((df.p2015 / 1000), axis=0)
        X["p2015"] = rezago_social["p2015"]
        X["lat"] = rezago_social["lat"]
        X["lon"] = rezago_social["lon"]
        X["alt"] = rezago_social["alt"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y2, test_size=0.20, random_state=0)
        rezago_lambda = lambda \
                x: 0 if x <= -1.007065 else 1 if x <= -0.325075 else 2 if x <= 0.35434 else 3 if x <= 1.717835 else 4
        for ne in [250]:
            for cri in ['mse']:
                for mf in ['auto']:
                    for md in [25]:
                        reg = RandomForestRegressor(n_estimators=ne, max_features=mf, criterion=cri, max_depth=md,
                                                    random_state=0)
                        pipe = make_pipeline(StandardScaler(), reg)
                        scores = cross_val_score(pipe, X_train, y_train, cv=10, n_jobs=-1, scoring=scr)
                        if -1 * np.mean(scores) < min_scr:
                            min_scr = -1 * np.mean(scores)
                            print(k, ne, cri, mf, md, np.mean(scores) * -1)
                            best_reg = clone(reg)
                            best_k = k
                            Xtrain, ytrain = X_train, y_train
                            Xtest, ytest = X_test, y_test
                            Xpred = X
    best_pipe = make_pipeline(StandardScaler(), best_reg)
    best_pipe.fit(Xtrain, ytrain)
    print(
        f"# {best_k}: {best_reg}, {np.mean(cross_val_score(best_pipe, Xtrain, ytrain, cv=5, n_jobs=-1, scoring=scr) * -1)}, Train:{np.mean(list(map(rezago_lambda, best_pipe.predict(Xtrain))) == ytrain.apply(rezago_lambda)) * 100}")
    print(
        f"# {best_k}: {best_reg}, {np.mean(cross_val_score(best_pipe, Xtest, ytest, cv=5, n_jobs=-1, scoring=scr) * -1)}, Test:{np.mean(list(map(rezago_lambda, best_pipe.predict(Xtest))) == ytest.apply(rezago_lambda)) * 100}")
    scores = cross_val_score(best_pipe, Xpred, y, cv=5, n_jobs=-1, scoring=scr)
    print('cv5:', np.mean(scores * -1), np.std(scores * -1),
          np.mean(list(map(rezago_lambda, best_pipe.predict(Xtest))) == ytest.apply(rezago_lambda)) * 100)
    score = cross_validate(best_pipe, X, y,
                           scoring=['r2', 'neg_mean_squared_error'],
                           n_jobs=-1, verbose=0)
    y_pred = cross_val_predict(best_pipe, X, y, n_jobs=-1, verbose=0)
    plot_regression_results(y, y_pred,
                            'Bosque Aleatorio (RF)',
                            (r'$R^2={:.2f} \pm {:.2f}$' + '\n' + r'$MSE={:.2f} \pm {:.2f}$')
                            .format(np.mean(score['test_r2']),
                                    np.std(score['test_r2']),
                                    -np.mean(score['test_neg_mean_squared_error']),
                                    np.std(score['test_neg_mean_squared_error'])))


if __name__ == '__main__':
    main_mlp()
    main_svm()
    main_rf()
