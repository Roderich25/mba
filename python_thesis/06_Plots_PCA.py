from itertools import cycle, combinations
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, label_binarize
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfTransformer

# /Users/rodrigo/mac/python_thesis/venv/bin/python /Users/rodrigo/mac/python_thesis/06_Plots_PCA.py
# LR(l2), k:6, folder:Count, sq:True, sc:True, rs:False, t:51, pipe_pca:0 n:100, c:0.01, mc:multinomial, cv='5', min=0.6052631578947368, mean=0.6508771929824562, median=0.6403508771929824, max=0.7280701754385965, std=0.04239665253892834

def main_all_lr():
    maximum_accuracy = 0
    for k in range(2, 7):
        for folder in ["Count", "Count_Personal"]:
            for sq in [True, False]:
                for sc in [True, False]:
                    for rs in [True, False]:
                        for t in [0, 1, 2, 11, 26, 51, 101, 501, 1001]:
                            print(f'# {k} {folder}, {sq}, {sc}, {rs}, {t}', end='\t')
                            denue_wide = pd.read_csv(f"summary/{folder}/denue_wide_{k}.csv")
                            rezago = pd.read_csv("rezago_social/rezago_social.csv")
                            rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL"]]
                            df = pd.merge(rezago_social, denue_wide, on=['Key'])
                            # OAXACA
                            df = df[df['Key'].apply(lambda x: str(x).startswith("20") and len(str(x)) == 5)]
                            df.drop(['Key'], axis=1, inplace=True)
                            print(f'before {t}:', df.shape, ',', end=' ')
                            df.drop([col for col, val in df.sum().iteritems() if val < t], axis=1, inplace=True)
                            print(f'after {t}:', df.shape, end='\n')
                            y = df['lgc00_15cl3']
                            # print(pd.value_counts(y))  # .49,.40,.09, 282, 232, 56
                            X = df.iloc[:, 2:]
                            if sq:
                                X = X.apply(np.sqrt)
                            # Conteo escalado por población/1000
                            if sc:
                                X = X.div((df.POB_TOTAL / 1000), axis=0)
                            # Educación, Salud y Esparcimiento
                            if rs:
                                filter_col = [col for col in df if col.startswith('6') or col.startswith('71')]
                                X = X.filter(filter_col)
                            # print(X.head())

                            # Particion de datos
                            X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.10,
                                                                                random_state=0)
                            # Ajuste modelo
                            for c in [0.0001, 0.001, 0.01, 0.1, 0.5, 1.0, 2, 5, 10.0, 100.0, 1000.0]:
                                for mc in ['ovr', 'multinomial']:
                                    clf = LogisticRegression(solver='lbfgs', multi_class=mc, penalty='l2', C=c,
                                                             max_iter=10000)
                                    # Standarized features
                                    pipeline = make_pipeline(StandardScaler(), clf)
                                    scores = cross_val_score(pipeline, X_train, y_train, cv=10, n_jobs=-1)
                                    if (np.mean(scores) > (maximum_accuracy - 0.5)) and (np.mean(
                                            scores) > 0.65):  # CHECK
                                        maximum_accuracy = np.mean(scores)
                                        scores = cross_val_score(pipeline, X, y, cv=5, n_jobs=-1)
                                        if np.mean(scores) > maximum_accuracy - 0.4:
                                            print(
                                                f"LR(l2), k:{k}, folder:{folder}, sq:{sq}, sc:{sc}, rs:{rs}, t:{t}, c:{c}, mc:{mc}, cv='5', min={np.min(scores)}, mean={np.mean(scores)}, median={np.median(scores)}, max={np.max(scores)}, std={np.std(scores)}")
                                            # Curva ROC
                                            y_bin = label_binarize(y, classes=[1, 2, 3])
                                            n_classes = y_bin.shape[1]
                                            y_score = cross_val_predict(pipeline, X, y, cv=10, method='predict_proba')
                                            fpr = dict()
                                            tpr = dict()
                                            roc_auc = dict()
                                            for i in range(n_classes):
                                                fpr[i], tpr[i], _ = roc_curve(y_bin[:, i], y_score[:, i])
                                                roc_auc[i] = auc(fpr[i], tpr[i])
                                            colors = cycle(['blue', 'red', 'green'])
                                            for i, color in zip(range(n_classes), colors):
                                                plt.plot(fpr[i], tpr[i], color=color, lw=2,
                                                         label='ROC curve of class {0} (area = {1:0.6f})'
                                                               ''.format(i + 1, roc_auc[i]))
                                            plt.plot([0, 1], [0, 1], 'k--', lw=2)
                                            plt.xlim([-0.05, 1.0])
                                            plt.ylim([0.0, 1.05])
                                            plt.xlabel('Tasa de Falsos Positivos')
                                            plt.ylabel('Tasa de Verdaderos Positivos')
                                            plt.title(
                                                f"{clf}\n{k},{folder},{sq},{sc},{rs},{t},{c},{mc}\nAccuracy:{np.mean(scores)}")
                                            plt.legend(loc="lower right")
                                            plt.show()
                                            plt.close()

                                            # pca2 = PCA(n_components=2)
                                            # X_pca2 = pca2.fit_transform(X_std)
                                            # print("PCA ratio:", np.sum(pca2.explained_variance_ratio_))
                                            # print(X_pca2.shape)
                                            # colors = {3: 'red', 1: 'green', 2: 'yellow'}
                                            # plt.scatter(X_pca2[:, 0], X_pca2[:, 1], c=y.map(colors))
                                            # plt.ylabel('PCA 2')
                                            # plt.xlabel('PCA 1')
                                            # plt.title(f'{folder}, {k}, {sc}, {rs}')
                                            # plt.show()


def main_pca_rf_tfidf():
    maximum_accuracy = 0
    for k in range(2, 7):
        for folder in ["Count", "Count_Personal"]:
            for sq in [True, False]:
                for sc in [True, False]:
                    for rs in [True, False]:
                        for t in [0, 1, 2, 11, 26, 51, 101, 501, 1001]:
                            print(f'# {k} {folder}, {sq}, {sc}, {rs}, {t}', end='\t')
                            denue_wide = pd.read_csv(f"summary/{folder}/denue_wide_{k}.csv")
                            rezago = pd.read_csv("rezago_social/rezago_social.csv")
                            rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL"]]
                            df = pd.merge(rezago_social, denue_wide, on=['Key'])
                            # OAXACA
                            df = df[df['Key'].apply(lambda x: str(x).startswith("20") and len(str(x)) == 5)]
                            df.drop(['Key'], axis=1, inplace=True)
                            print(f'before {t}:', df.shape, ',', end=' ')
                            df.drop([col for col, val in df.sum().iteritems() if val < t], axis=1, inplace=True)
                            print(f'after {t}:', df.shape, end='\n')
                            y = df['lgc00_15cl3']
                            # print(pd.value_counts(y))  # .49,.40,.09, 282, 232, 56
                            X = df.iloc[:, 2:]
                            if sq:
                                X = X.apply(np.sqrt)
                            # Conteo escalado por población/1000
                            if sc:
                                X = X.div((df.POB_TOTAL / 1000), axis=0)
                            # Educación, Salud y Esparcimiento
                            if rs:
                                filter_col = [col for col in df if col.startswith('6') or col.startswith('71')]
                                X = X.filter(filter_col)

                            # Particion de datos
                            X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.10,
                                                                                random_state=0)
                            # Ajuste modelo
                            for ne in [100, 500, 1000, 2000]:
                                for md in [10, 15, 20, 25]:
                                    for cri in ['gini', 'entropy']:
                                        for mf in ['log2', 'sqrt']:
                                            clf = RandomForestClassifier(max_depth=md, n_estimators=ne,
                                                                         criterion=cri,
                                                                         max_features=mf, random_state=0)
                                            # clf = LogisticRegression(solver='lbfgs', multi_class=mc, penalty='l2', C=c,
                                            #                         max_iter=10000)
                                            # Standarized features
                                            # pipeline = make_pipeline(StandardScaler(), clf)
                                            # tf-idf
                                            pipeline = make_pipeline(TfidfTransformer(), clf)
                                            scores = cross_val_score(pipeline, X_train, y_train, cv=10, n_jobs=-1)
                                            if (np.mean(scores) > (maximum_accuracy - 0.5)) and (np.mean(
                                                    scores) > 0.66):  # CHECK
                                                maximum_accuracy = np.mean(scores)
                                                scores = cross_val_score(pipeline, X, y, cv=5, n_jobs=-1)
                                                if np.mean(scores) > maximum_accuracy - 0.4:
                                                    print(
                                                        f"{clf}, k:{k}, folder:{folder}, sq:{sq}, sc:{sc}, rs:{rs}, t:{t}, cv='5', min={np.min(scores)}, mean={np.mean(scores)}, median={np.median(scores)}, max={np.max(scores)}, std={np.std(scores)}")
                                                    # Curva ROC
                                                    y_bin = label_binarize(y, classes=[1, 2, 3])
                                                    n_classes = y_bin.shape[1]
                                                    y_score = cross_val_predict(pipeline, X, y, cv=10,
                                                                                method='predict_proba')
                                                    fpr = dict()
                                                    tpr = dict()
                                                    roc_auc = dict()
                                                    for i in range(n_classes):
                                                        fpr[i], tpr[i], _ = roc_curve(y_bin[:, i], y_score[:, i])
                                                        roc_auc[i] = auc(fpr[i], tpr[i])
                                                    colors = cycle(['blue', 'red', 'green'])
                                                    for i, color in zip(range(n_classes), colors):
                                                        plt.plot(fpr[i], tpr[i], color=color, lw=2,
                                                                 label='ROC curve of class {0} (area = {1:0.6f})'
                                                                       ''.format(i + 1, roc_auc[i]))
                                                    plt.plot([0, 1], [0, 1], 'k--', lw=2)
                                                    plt.xlim([-0.05, 1.0])
                                                    plt.ylim([0.0, 1.05])
                                                    plt.xlabel('Tasa de Falsos Positivos')
                                                    plt.ylabel('Tasa de Verdaderos Positivos')
                                                    plt.title(
                                                        f"{clf}\n{k},{folder},{sq},{sc},{rs},{t}\nAccuracy:{np.mean(scores)}")
                                                    plt.legend(loc="lower right")
                                                    plt.show()
                                                    plt.close()


def main_pca_lr():
    maximum_accuracy = 0
    combis = [cs for ls in (combinations(range(1, 10), i) for i in range(1, 10)) for cs in ls]
    for k in [6]:
        for folder in ["Count"]:
            for sq in [True, False]:
                for sc in [True]:
                    for rs in [False]:
                        for t in [0, 11, 26, 51, 101, 501, 1001]:
                            for cb, combi in enumerate(combis):
                                print(f'# {k} {folder}, {sq}, {sc}, {rs}, {t}, {cb}', end='\t')
                                denue_wide = pd.read_csv(f"summary/{folder}/denue_wide_{k}.csv")
                                rezago = pd.read_csv("rezago_social/rezago_social.csv")
                                rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL"]]
                                df = pd.merge(rezago_social, denue_wide, on=['Key'])
                                # OAXACA
                                df = df[df['Key'].apply(lambda x: str(x).startswith("20") and len(str(x)) == 5)]
                                df.drop(['Key'], axis=1, inplace=True)
                                print(f'before {t}:', df.shape, ',', end=' ')
                                df.drop([col for col, val in df.sum().iteritems() if val < t], axis=1, inplace=True)
                                print(f'after {t}:', df.shape, end='\t')
                                y = df['lgc00_15cl3']
                                # print(pd.value_counts(y))  # .49,.40,.09, 282, 232, 56
                                X = df.iloc[:, 2:]
                                if sq:
                                    X = X.apply(np.sqrt)
                                # Conteo escalado por población/1000
                                if sc:
                                    X = X.div((df.POB_TOTAL / 1000), axis=0)
                                # Educación, Salud y Esparcimiento
                                if rs:
                                    filter_col = [col for col in df if col.startswith('6') or col.startswith('71')]
                                    X = X.filter(filter_col)
                                # print(X.head())
                                if X.shape[1] > 1:
                                    # Particion de datos
                                    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.10,
                                                                                        random_state=0)
                                    # PCA components
                                    X_train_std = StandardScaler().fit_transform(X)
                                    # min
                                    min_pca = PCA(0.75)
                                    X_pca = min_pca.fit_transform(X_train_std)
                                    min_n_pca = len(min_pca.explained_variance_ratio_)
                                    # max
                                    max_pca = PCA(0.95)
                                    X_pca = max_pca.fit_transform(X_train_std)
                                    max_n_pca = len(max_pca.explained_variance_ratio_)
                                    print("pca 0.75 n_min:", min_n_pca, "pca 0.95 n_max:", max_n_pca)
                                    # Ajuste modelo
                                    for n in range(min_n_pca, max_n_pca + 1, 1):
                                        for c in [0.0001, 0.001, 0.01, 0.1, 0.5, 1.0, 2, 5, 10.0, 100.0, 1000.0]:
                                            for mc in ['ovr', 'multinomial']:
                                                clf = LogisticRegression(solver='lbfgs', multi_class=mc, penalty='l2', C=c,
                                                                         max_iter=10000)
                                                pipeline = make_pipeline(StandardScaler(), PCA(n_components=n), clf)

                                                scores = cross_val_score(pipeline, X_train, y_train, cv=10, n_jobs=-1)

                                                if (np.mean(scores) > (maximum_accuracy - 0.5)) and (np.mean(
                                                        scores) > 0.66):  # CHECK
                                                    print(f"LR(l2), k:{k}, folder:{folder}, sq:{sq}, sc:{sc}, rs:{rs}, t:{t}, pipe_pca:{cb} n:{n}, c:{c}, mc:{mc}, cv='10', min={np.min(scores)}, mean={np.mean(scores)}, median={np.median(scores)}, max={np.max(scores)}, std={np.std(scores)}")
                                                    maximum_accuracy = np.mean(scores)
                                                    scores = cross_val_score(pipeline, X, y, cv=5, n_jobs=-1)
                                                    if np.min(scores) > 6:
                                                        print(
                                                            f"LR(l2), k:{k}, folder:{folder}, sq:{sq}, sc:{sc}, rs:{rs}, t:{t}, pipe_pca:{cb} n:{n}, c:{c}, mc:{mc}, cv='5', min={np.min(scores)}, mean={np.mean(scores)}, median={np.median(scores)}, max={np.max(scores)}, std={np.std(scores)}\n")


def main_lda_lr():
    maximum_accuracy = 0
    for k in range(3, 7):
        for folder in ["Count", "Count_Personal"]:
            for sq in [True, False]:
                for sc in [True, False]:
                    for rs in [True, False]:
                        for t in [0, 1, 2, 11, 26, 51, 101, 501, 1001]:
                            for pipe_pca in range(0, 2):
                                print(f'# {k} {folder}, {sq}, {sc}, {rs}, {t}, {pipe_pca}', end='\t')
                                denue_wide = pd.read_csv(f"summary/{folder}/denue_wide_{k}.csv")
                                rezago = pd.read_csv("rezago_social/rezago_social.csv")
                                rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL"]]
                                df = pd.merge(rezago_social, denue_wide, on=['Key'])
                                # OAXACA
                                df = df[df['Key'].apply(lambda x: str(x).startswith("20") and len(str(x)) == 5)]
                                df.drop(['Key'], axis=1, inplace=True)
                                print(f'before {t}:', df.shape, ',', end=' ')
                                df.drop([col for col, val in df.sum().iteritems() if val < t], axis=1, inplace=True)
                                print(f'after {t}:', df.shape, end='\t')
                                y = df['lgc00_15cl3']
                                # print(pd.value_counts(y))  # .49,.40,.09, 282, 232, 56
                                X = df.iloc[:, 2:]
                                if sq:
                                    X = X.apply(np.sqrt)
                                # Conteo escalado por población/1000
                                if sc:
                                    X = X.div((df.POB_TOTAL / 1000), axis=0)
                                # Educación, Salud y Esparcimiento
                                if rs:
                                    filter_col = [col for col in df if col.startswith('6') or col.startswith('71')]
                                    X = X.filter(filter_col)
                                # print(X.head())

                                # Particion de datos
                                X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.10,
                                                                                    random_state=0)

                                # PCA components
                                X_train_std = StandardScaler().fit_transform(X)
                                # min
                                min_pca = PCA(0.50)
                                X_pca = min_pca.fit_transform(X_train_std)
                                min_n_pca = len(min_pca.explained_variance_ratio_)
                                # max
                                max_pca = PCA(0.95)
                                X_pca = max_pca.fit_transform(X_train_std)
                                max_n_pca = len(max_pca.explained_variance_ratio_)
                                print("pca 0.5 n_min:", min_n_pca, "pca 0.95 n_max:", max_n_pca)


if __name__ == '__main__':
    main_pca_lr()
