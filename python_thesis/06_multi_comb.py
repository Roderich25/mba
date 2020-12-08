import numpy as np
import pandas as pd
from itertools import combinations
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfTransformer


# k:2, f:Count, cl:lgc00_15cl3, sq:True, sc:True, cb:58, t:0, c:0.5, mc:multinomial, p:0, min=0.5526, mean=0.5719, median=0.5789, std=0.017
# k:2, f:Count, cl:lgc00_15cl3, sq:False, sc:True, cb:3, t:0, c:0.1, mc:ovr, p:0, min=0.5351, mean=0.5825, median=0.5789, std=0.0439

# k:2, f:Count, cl:lgc00_15cl3, sq:False, sc:True, cb:15, t:0, c:0.01, mc:ovr, p:0, min=0.5614, mean=0.6088, median=0.6053, std=0.0302
# k:2, f:Count, cl:lgc00_15cl3, sq:False, sc:True, cb:15, t:0, c:0.01, mc:multinomial, p:0, min=0.5877, mean=0.6193, median=0.614, std=0.0264

# k:2, f:Count, cl:lgc00_15cl3, sq:False, sc:True, cb:22, t:0, c:0.1, mc:multinomial, p:0, min=0.6053, mean=0.6263, median=0.6228, std=0.0181
# k:2, f:Count, cl:lgc00_15cl3, sq:False, sc:True, cb:22, t:0, c:0.5, mc:ovr, p:0, min=0.614, mean=0.6281, median=0.6228, std=0.0163

# k:2, f:Count, cl:lgc00_15cl3, sq:False, sc:True, cb:42, t:0, c:0.01, mc:multinomial, p:0, min=0.5965, mean=0.6456, median=0.6404, std=0.0414
# k:2, f:Count, cl:lgc00_15cl3, sq:False, sc:True, cb:42, t:0, c:0.1, mc:ovr, p:0, min=0.614, mean=0.6509, median=0.6316, std=0.0365

# k:2, f:Count, cl:lgc00_15cl3, sq:False, sc:True, cb:128, t:0, c:0.1, mc:ovr, p:0, min=0.614, mean=0.6526, median=0.6228, std=0.046
# k:2, f:Count_Personal, cl:lgc00_15cl3, sq:False, sc:True, cb:253, t:0, c:0.01, mc:multinomial, p:0, min=0.5702, mean=0.6298, median=0.614, max=0.7544, std=0.065
# k:2, f:Count_Personal, cl:lgc00_15cl3, sq:False, sc:True, cb:323, t:0, c:0.1, mc:ovr, p:0, min=0.5789, mean=0.6246, median=0.5965, max=0.7456, std=0.0611


def main_multi_comb():
    thresh = 0.59
    combis = [cs for ls in (combinations(range(1, 10), i) for i in range(1, 10)) for cs in ls]
    max_accuracy = thresh
    for k in [2]:
        for folder in ["Count_Personal"]:
            for cl in ["lgc00_15cl3"]:
                for sq in [False]:
                    for sc in [True]:
                        for cb, combi in enumerate(combis):
                            for t in [0]:
                                print(f"# k:{k}, f:{folder}, cl:{cl}, sq:{sq}, sc:{sc}, cb:{cb}, t:{t}")
                                # FOLDER & CODIGO
                                denue_wide = pd.read_csv(f"summary/{folder}/denue_wide_{k}.csv")
                                rezago = pd.read_csv("rezago_social/rezago_social.csv")
                                rezago_social = rezago[[cl, "Key", "POB_TOTAL"]]
                                df = pd.merge(rezago_social, denue_wide, on=['Key'])
                                # Oaxaca
                                df = df[df['Key'].apply(lambda x: str(x).startswith("20") and len(str(x)) == 5)]
                                df.drop(['Key'], axis=1, inplace=True)
                                df.drop([col for col, val in df.sum().iteritems() if val < t], axis=1, inplace=True)
                                y = df[cl]
                                X = df.iloc[:, 2:]
                                if sq:
                                    X = X.apply(np.sqrt)
                                # Conteo escalado por población/1000
                                if sc:
                                    X = X.div((df.POB_TOTAL / 1000), axis=0)
                                # SCIAN combinations
                                filter_col = []
                                for comb in combi:
                                    filter_col.extend([col for col in df if col.startswith(str(comb))])
                                X = X.filter(filter_col)
                                # Particion de datos
                                if X.shape[1] > 1:
                                    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y,
                                                                                        test_size=0.10,
                                                                                        random_state=0)
                                    # Ajuste modelo
                                    for c in [0.0001, 0.001, 0.01, 0.1, 0.5, 1.0, 2, 5, 10.0, 100.0, 1000.0]:
                                        for mc in ['ovr', 'multinomial']:
                                            clf = LogisticRegression(solver='lbfgs', multi_class=mc, penalty='l2', C=c, max_iter=10000)
                                            for p, pipe in enumerate([  # make_pipeline(TfidfTransformer(), clf),
                                                make_pipeline(StandardScaler(), PCA(0.80), clf)]):  # ,
                                                # make_pipeline(StandardScaler(), clf)]):
                                                scores = cross_val_score(pipe, X_train, y_train, cv=10, n_jobs=-1)
                                                if np.min(scores) > thresh:
                                                    scores = cross_val_score(pipe, X, y, cv=5, n_jobs=-1)
                                                    if np.mean(scores) >= max_accuracy:
                                                        max_accuracy = np.mean([np.mean(scores), np.median(scores)])
                                                        print(
                                                            f"# k:{k}, f:{folder}, cl:{cl}, sq:{sq}, sc:{sc}, cb:{cb}, t:{t}, c:{c}, mc:{mc}, p:{p}, min={round(np.min(scores), 4)}, mean={round(np.mean(scores), 4)}, median={round(np.median(scores), 4)}, max={round(np.max(scores), 4)}, std={round(np.std(scores), 4)}")


if __name__ == '__main__':
    main_multi_comb()
