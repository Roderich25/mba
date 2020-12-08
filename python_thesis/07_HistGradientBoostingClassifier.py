from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingClassifier
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler


# HGB
# k:2, f:Count, cl:lgc00_15cl3, sq:True, sc:True, t:1, c:0, p:0, min=0.5175, mean=0.5614, median=0.5702, max=0.6053, std=0.0314
# k:2, f:Count, cl:lgc00_15cl3, sq:True, sc:True, t:1, c:0.01, p:0, min=0.5263, mean=0.5667, median=0.5614, max=0.614, std=0.0291
# k:2, f:Count, cl:lgc00_15cl3, sq:True, sc:True, t:1, c:0.1, p:0, min=0.5088, mean=0.5649, median=0.5614, max=0.6053, std=0.0345
# k:2, f:Count, cl:lgc00_15cl3, sq:True, sc:True, t:1, c:0.5, p:0, min=0.5351, mean=0.5702, median=0.5789, max=0.6053, std=0.0266
# k:2, f:Count, cl:lgc00_15cl3, sq:True, sc:True, t:1, c:10.0, p:0, min=0.5263, mean=0.5789, median=0.5789, max=0.6404, std=0.0388
# k:2, f:Count, cl:lgc00_15cl3, sq:False, sc:True, t:1, c:0.001, p:0, min=0.5351, mean=0.5912, median=0.5877, max=0.6491, std=0.0387
# k:2, f:Count, cl:lgc00_15cl3, sq:False, sc:True, t:1, c:0.01, p:0, min=0.5263, mean=0.593, median=0.5965, max=0.6404, std=0.0417
# k:2, f:Count, cl:lgc00_15cl3, sq:False, sc:True, t:1, c:100.0, p:0, min=0.5789, mean=0.6228, median=0.6228, max=0.6842, std=0.036
# k:2, f:Count_Personal, cl:lgc00_15cl3, sq:False, sc:True, t:1, c:100.0, p:0, min=0.5702, mean=0.6316, median=0.6316, max=0.7018, std=0.0426
# k:2, f:Count_Personal, cl:lgc00_15cl3, sq:False, sc:True, t:1, c:1000.0, p:0, min=0.5789, mean=0.6351, median=0.6316, max=0.6842, std=0.0402
# k:3, f:Count_Personal, cl:lgc00_15cl3, sq:False, sc:True, t:1, c:100.0, p:0, min=0.5702, mean=0.6404, median=0.6491, max=0.7018, std=0.0433


# LR
# k:3, f:Count_Personal, cl:lgc00_15cl3, sq:False, sc:True, t:1, mc:ovr, c:0.1, p:0, min=0.5877, mean=0.6175, median=0.614, max=0.6491, std=0.0197
# k:3, f:Count_Personal, cl:lgc00_15cl3, sq:False, sc:True, t:1, mc:ovr, c:0.5, p:0, min=0.5877, mean=0.6211, median=0.6053, max=0.6579, std=0.0274
# k:4, f:Count_Personal, cl:lgc00_15cl3, sq:False, sc:True, t:1, mc:multinomial, c:0.1, p:0, min=0.5965, mean=0.6281, median=0.6228, max=0.6754, std=0.0264

def main_hgbc():
    thresh = 0.5
    max_accuracy = thresh
    for k in [5]:
        for folder in ["Count", "Count_Personal"]:
            for cl in ["lgc00_15cl3"]:
                for sq in [True, False]:
                    for sc in [True]:
                        for t in [1]:
                            print(f"# k:{k}, f:{folder}, cl:{cl}, sq:{sq}, sc:{sc}, t:{t}")
                            # FOLDER & CODIGO
                            denue_wide = pd.read_csv(f"summary/{folder}/denue_wide_{k}.csv")
                            rezago = pd.read_csv("rezago_social/rezago_social.csv")
                            rezago_social = rezago[[cl, "Key", "POB_TOTAL"]]
                            df = pd.merge(rezago_social, denue_wide, on=['Key'])
                            # Oaxaca
                            # df = df[df['Key'].apply(lambda x: str(x).startswith("20") and len(str(x)) == 5)]
                            df.drop(['Key'], axis=1, inplace=True)
                            df.drop([col for col, val in df.sum().iteritems() if val <= t], axis=1, inplace=True)
                            y = df[cl]
                            X = df.iloc[:, 2:]
                            if sq:
                                X = X.apply(np.sqrt)
                            # Conteo escalado por población/1000
                            if sc:
                                X = X.div((df.POB_TOTAL / 1000), axis=0)
                            # Particion de datos
                            if X.shape[1] > 1:
                                X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y,
                                                                                    test_size=0.10,
                                                                                    random_state=0)
                                # Ajuste modelo
                                for c in [0, 0.0001, 0.001, 0.01, 0.1, 0.5, 1.0, 2, 5, 10.0, 100.0, 1000.0]:
                                    clf = HistGradientBoostingClassifier(l2_regularization=c)
                                    for p, pipe in enumerate([make_pipeline(clf)]):
                                        scores = cross_val_score(pipe, X_train, y_train, cv=10, n_jobs=-1)
                                        if np.min(scores) > thresh:
                                            scores = cross_val_score(pipe, X, y, cv=5, n_jobs=-1)
                                            if np.mean(scores) >= max_accuracy:
                                                max_accuracy = np.mean([np.mean(scores), np.median(scores)])
                                                print(
                                                    f"# k:{k}, f:{folder}, cl:{cl}, sq:{sq}, sc:{sc}, t:{t}, c:{c}, p:{p}, min={round(np.min(scores), 4)}, mean={round(np.mean(scores), 4)}, median={round(np.median(scores), 4)}, max={round(np.max(scores), 4)}, std={round(np.std(scores), 4)}")


def main_lr():
    thresh = 0.5
    max_accuracy = thresh
    for k in [2, 3, 4, 5, 6]:
        for folder in ["Count", "Count_Personal"]:
            for cl in ["lgc00_15cl3"]:
                for sq in [True, False]:
                    for sc in [True]:
                        for t in [1]:
                            print(f"# k:{k}, f:{folder}, cl:{cl}, sq:{sq}, sc:{sc}, t:{t}")
                            # FOLDER & CODIGO
                            denue_wide = pd.read_csv(f"summary/{folder}/denue_wide_{k}.csv")
                            rezago = pd.read_csv("rezago_social/rezago_social.csv")
                            rezago_social = rezago[[cl, "Key", "POB_TOTAL"]]
                            df = pd.merge(rezago_social, denue_wide, on=['Key'])
                            # Oaxaca
                            df = df[df['Key'].apply(lambda x: str(x).startswith("20") and len(str(x)) == 5)]
                            df.drop(['Key'], axis=1, inplace=True)
                            df.drop([col for col, val in df.sum().iteritems() if val <= t], axis=1, inplace=True)
                            y = df[cl]
                            X = df.iloc[:, 2:]
                            if sq:
                                X = X.apply(np.sqrt)
                            # Conteo escalado por población/1000
                            if sc:
                                X = X.div((df.POB_TOTAL / 1000), axis=0)
                            # Particion de datos
                            if X.shape[1] > 1:
                                X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y,
                                                                                    test_size=0.10,
                                                                                    random_state=0)
                                # Ajuste modelo
                                for mc in ['ovr', 'multinomial']:
                                    for c in [0.0001, 0.001, 0.01, 0.1, 0.5, 1.0, 2, 5, 10.0, 100.0, 1000.0]:
                                        clf = LogisticRegression(solver='lbfgs', multi_class=mc, penalty='l2', C=c,
                                                                 max_iter=25000)
                                        for p, pipe in enumerate([make_pipeline(clf)]):
                                            scores = cross_val_score(pipe, X_train, y_train, cv=10, n_jobs=-1)
                                            if np.min(scores) > thresh:
                                                scores = cross_val_score(pipe, X, y, cv=5, n_jobs=-1)
                                                if np.mean(scores) >= max_accuracy:
                                                    max_accuracy = np.mean([np.mean(scores), np.median(scores)])
                                                    print(
                                                        f"# k:{k}, f:{folder}, cl:{cl}, sq:{sq}, sc:{sc}, t:{t}, mc:{mc}, c:{c}, p:{p}, min={round(np.min(scores), 4)}, mean={round(np.mean(scores), 4)}, median={round(np.median(scores), 4)}, max={round(np.max(scores), 4)}, std={round(np.std(scores), 4)}")


def main_svc():
    thresh = 0.5
    max_accuracy = thresh
    for k in [2, 3, 4, 5, 6]:
        for folder in ["Count", "Count_Personal"]:
            for cl in ["lgc00_15cl3"]:
                for sq in [True, False]:
                    for sc in [True]:
                        for t in [1]:
                            print(f"# k:{k}, f:{folder}, cl:{cl}, sq:{sq}, sc:{sc}, t:{t}")
                            # FOLDER & CODIGO
                            denue_wide = pd.read_csv(f"summary/{folder}/denue_wide_{k}.csv")
                            rezago = pd.read_csv("rezago_social/rezago_social.csv")
                            rezago_social = rezago[[cl, "Key", "POB_TOTAL"]]
                            df = pd.merge(rezago_social, denue_wide, on=['Key'])
                            # Oaxaca
                            # df = df[df['Key'].apply(lambda x: str(x).startswith("20") and len(str(x)) == 5)]
                            df.drop(['Key'], axis=1, inplace=True)
                            df.drop([col for col, val in df.sum().iteritems() if val <= t], axis=1, inplace=True)
                            y = df[cl]
                            X = df.iloc[:, 2:]
                            if sq:
                                X = X.apply(np.sqrt)
                            # Conteo escalado por población/1000
                            if sc:
                                X = X.div((df.POB_TOTAL / 1000), axis=0)
                            # Particion de datos
                            if X.shape[1] > 1:
                                X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y,
                                                                                    test_size=0.10,
                                                                                    random_state=0)
                                # Ajuste modelo
                                for kr in ['poly']:
                                    for g in [0.0001, 0.001, 0.01, 0.1, 0.5, 1.0, 2, 5, 10.0, 100.0, 1000.0]:
                                        for c in [0.0001, 0.001, 0.01, 0.1, 0.5, 1.0, 2, 5, 10.0, 100.0, 1000.0]:
                                            clf = SVC(kernel=kr, gamma=g, C=c)
                                            for p, pipe in enumerate([make_pipeline(clf)]):
                                                scores = cross_val_score(pipe, X_train, y_train, cv=10, n_jobs=-1)
                                                if np.min(scores) > thresh:
                                                    scores = cross_val_score(pipe, X, y, cv=5, n_jobs=-1)
                                                    if np.mean(scores) >= max_accuracy:
                                                        max_accuracy = np.mean([np.mean(scores), np.median(scores)])
                                                        print(
                                                            f"# k:{k}, f:{folder}, cl:{cl}, sq:{sq}, sc:{sc}, t:{t}, k:{kr}, g:{g}, c:{c}, min={round(np.min(scores), 4)}, mean={round(np.mean(scores), 4)}, median={round(np.median(scores), 4)}, max={round(np.max(scores), 4)}, std={round(np.std(scores), 4)}")


if __name__ == '__main__':
    main_hgbc()
