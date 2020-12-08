from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.base import clone
from sklearn.svm import SVC
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, label_binarize
import numpy as np
import pandas as pd
from itertools import combinations
from matplotlib import pyplot as plt
from itertools import cycle
import geopandas as gpd
from sklearn.metrics import plot_confusion_matrix


# https://www.youtube.com/watch?v=M3KTWnTrU_c&t=947s
# https://www.youtube.com/watch?v=SHAn-bT_i0I&feature=emb_logo

# sin lat lon all
# Count, 4: LogisticRegression(C=0.01, max_iter=10000, multi_class='multinomial') Train:80.91603053435115
# Count, 4: LogisticRegression(C=0.01, max_iter=10000, multi_class='multinomial') Test:73.17073170731707
#
# con lat lon all
# Count, 3: LogisticRegression(C=0.1, max_iter=10000, multi_class='multinomial') Train:79.89821882951654
# Count, 3: LogisticRegression(C=0.1, max_iter=10000, multi_class='multinomial') Test:72.5609756097561
# Count, 3: LogisticRegression(C=0.1, max_iter=10000, multi_class='multinomial') CV5:0.731788452304075 +/- 0.016619250991586138

# Count, 3: SVC(C=100.0, gamma=0.0001, probability=True) Train:79.59287531806616
# Count, 3: SVC(C=100.0, gamma=0.0001, probability=True) Test:72.96747967479675
# Count, 3: SVC(C=100.0, gamma=0.0001, probability=True) CV5:0.673994502674151 +/- 0.009681172428927055


# con lan lot comb


def main_lr():
    max_accuracy = 0
    combis = [cs for ls in (combinations(range(1, 10), i) for i in range(9, 10)) for cs in ls]
    print(len(combis))
    for folder in ["Count"]:
        for k in range(2, 7):
            for cb, combi in enumerate(combis):
                denue_wide = pd.read_csv(f"summary/{folder}/denue_wide_{k}.csv")
                rezago = pd.read_csv("rezago_social/rezago_social.csv")
                rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON", "ALT", "PER_URB", "PER_RUR"]]
                df = pd.merge(rezago_social, denue_wide, on=['Key'])
                df.drop(['Key'], axis=1, inplace=True)
                y = df['lgc00_15cl3']
                X = df.iloc[:, 7:].div((df.POB_TOTAL / 1000), axis=0)
                X["LAT"] = rezago_social["LAT"]
                X["LON"] = rezago_social["LON"]
                X["ALT"] = rezago_social["ALT"]
                X["PER_URB"] = rezago_social["PER_URB"]
                X["PER_RUR"] = rezago_social["PER_RUR"]
                # SCIAN combinations
                filter_col = ['LAT', 'LON', 'PER_RUR', 'ALT']
                for comb in combi:
                    filter_col.extend([col for col in df if col.startswith(str(comb))])
                X = X.filter(filter_col)
                # print(X.head())
                print(X.columns)
                print(f'# {folder} {k} {X.shape} {cb}')
                for c in [0.1, 0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]:
                    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.20,
                                                                        random_state=0)
                    for mc in ['multinomial']:
                        clf = LogisticRegression(solver='lbfgs', multi_class=mc, penalty='l2', C=c, max_iter=10000)
                        pipeline = make_pipeline(StandardScaler(), clf)
                        scores = cross_val_score(pipeline, X_train, y_train, cv=10, n_jobs=-1)
                        if np.mean(scores) > max_accuracy:
                            print(f"\t # LR {max_accuracy}, {k}, {cb}, {c}, {mc}")
                            max_accuracy = np.mean(scores)
                            best_clf = clone(clf)
                            best_folder = folder
                            best_k = k
                            Xtrain, ytrain = X_train, y_train
                            Xtest, ytest = X_test, y_test
                            Xpred, ypred = X, y
    print(best_clf, max_accuracy)
    best_pipe = make_pipeline(StandardScaler(), best_clf)
    best_pipe.fit(Xtrain, ytrain)
    print(f"# {best_folder}, {best_k}: {best_clf} Train:{best_pipe.score(Xtrain, ytrain) * 100}")
    print(f"# {best_folder}, {best_k}: {best_clf} Test:{best_pipe.score(Xtest, ytest) * 100}")
    scores = cross_val_score(best_pipe, Xpred, ypred, cv=5, n_jobs=-1)
    print(f"# {best_folder}, {best_k}: {best_clf} CV5:{np.mean(scores)} +/- {np.std(scores)}")

    # # Mapa
    # y_pred = best_pipe.predict(X)
    # # print(y_pred)
    # gdf = gpd.read_file('municipios/areas_geoestadisticas_municipales.shp')
    # gdf['Key'] = gdf['CVE_ENT'] + gdf['CVE_MUN']
    # rezago = pd.read_csv("rezago_social/rezago_social.csv")
    # rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON"]]
    # rezago_social['Key'] = rezago_social['Key'].astype(str).str.zfill(5)
    # rezago_social['Pred'] = y_pred
    # gdf = gdf.merge(rezago_social, on='Key')
    # colors = {1: 'green', 2: 'yellow', 3: 'red'}
    # fig, ax = plt.subplots()
    # gdf.plot(ax=ax, color=gdf['Pred'].map(colors))
    # plt.axis('off')
    # plt.title("Rezago Social predicho a nivel municipal, 2015.")
    # txt = "Predichos por modelo LR con base en categorías DENUE/SCIAN a nivel Rama."
    # plt.figtext(0.01, 0.01, txt, wrap=True, horizontalalignment='left', fontsize=12)
    # plt.show()
    #
    # # Curva ROC
    # y_bin = label_binarize(y, classes=[1, 2, 3])
    # n_classes = y_bin.shape[1]
    # y_score = cross_val_predict(best_pipe, X, y, cv=10, method='predict_proba')
    # fpr = dict()
    # tpr = dict()
    # roc_auc = dict()
    # for i in range(n_classes):
    #     fpr[i], tpr[i], _ = roc_curve(y_bin[:, i], y_score[:, i])
    #     roc_auc[i] = auc(fpr[i], tpr[i])
    # colors = cycle(['blue', 'red', 'green'])
    # for i, color in zip(range(n_classes), colors):
    #     plt.plot(fpr[i], tpr[i], color=color, lw=2,
    #              label='ROC curve of class {0} (area = {1:0.6f})'
    #                    ''.format(i + 1, roc_auc[i]))
    # plt.plot([0, 1], [0, 1], 'k--', lw=2)
    # plt.xlim([-0.05, 1.0])
    # plt.ylim([0.0, 1.05])
    # plt.xlabel('Tasa de Falsos Positivos')
    # plt.ylabel('Tasa de Verdaderos Positivos')
    # plt.title(f"Regresión Logistica L2\nDENUE/SCIAN a nivel Rama")
    # plt.legend(loc="lower right")
    # plt.show()


def main_svm():
    max_accuracy = 0
    for folder in ["Count"]:
        for k in range(3, 4):
            denue_wide = pd.read_csv(f"summary/{folder}/denue_wide_{k}.csv")
            rezago = pd.read_csv("rezago_social/rezago_social.csv")
            rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON", "ALT"]]
            df = pd.merge(rezago_social, denue_wide, on=['Key'])
            df.drop(['Key'], axis=1, inplace=True)
            y = df['lgc00_15cl3']
            X = df.iloc[:, 5:].div((df.POB_TOTAL / 1000), axis=0)
            X["LAT"] = rezago_social["LAT"]
            X["LON"] = rezago_social["LON"]
            print(f'# {folder} {k} {X.shape}')
            X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.20, random_state=0)
            for c in [1000.0]:  # [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]:
                for g in [0.0001]:  # [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]:
                    for kr in ['sigmoid']:  # ['sigmoid', 'rbf']:
                        print('\t#', c, g, kr)
                        clf = SVC(kernel=kr, gamma=g, C=c, probability=True, random_state=0)
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

    scores = cross_val_score(best_pipe, X, y, cv=5, n_jobs=-1)
    print(f"# {best_folder}, {best_k}: {best_clf} CV5:{np.mean(scores)} +/- {np.std(scores)}")

    # # Mapa
    # y_pred = best_pipe.predict(X)
    # # print(y_pred)
    # gdf = gpd.read_file('municipios/areas_geoestadisticas_municipales.shp')
    # gdf['Key'] = gdf['CVE_ENT'] + gdf['CVE_MUN']
    # rezago = pd.read_csv("rezago_social/rezago_social.csv")
    # rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON"]]
    # rezago_social['Key'] = rezago_social['Key'].astype(str).str.zfill(5)
    # rezago_social['Pred'] = y_pred
    # gdf = gdf.merge(rezago_social, on='Key')
    # colors = {1: 'green', 2: 'yellow', 3: 'red'}
    # fig, ax = plt.subplots()
    # gdf.plot(ax=ax, color=gdf['Pred'].map(colors))
    # plt.axis('off')
    # plt.title("Rezago Social predicho a nivel municipal, 2015.")
    # txt = "Predichos por modelo SVM kernel RBF con base en categorías DENUE/SCIAN a nivel Rama."
    # plt.figtext(0.01, 0.01, txt, wrap=True, horizontalalignment='left', fontsize=12)
    # plt.show()
    #
    # # Curva ROC
    # y_bin = label_binarize(y, classes=[1, 2, 3])
    # n_classes = y_bin.shape[1]
    # y_score = cross_val_predict(best_pipe, X, y, cv=10, method='predict_proba')
    # fpr = dict()
    # tpr = dict()
    # roc_auc = dict()
    # for i in range(n_classes):
    #     fpr[i], tpr[i], _ = roc_curve(y_bin[:, i], y_score[:, i])
    #     roc_auc[i] = auc(fpr[i], tpr[i])
    # colors = cycle(['blue', 'red', 'green'])
    # for i, color in zip(range(n_classes), colors):
    #     plt.plot(fpr[i], tpr[i], color=color, lw=2,
    #              label='ROC curve of class {0} (area = {1:0.6f})'
    #                    ''.format(i + 1, roc_auc[i]))
    # plt.plot([0, 1], [0, 1], 'k--', lw=2)
    # plt.xlim([-0.05, 1.0])
    # plt.ylim([0.0, 1.05])
    # plt.xlabel('Tasa de Falsos Positivos')
    # plt.ylabel('Tasa de Verdaderos Positivos')
    # plt.title(f"Máquina de Soporte Vectorial con kernel RBF\nDENUE/SCIAN a nivel Rama")
    # plt.legend(loc="lower right")
    # plt.show()


def main_rf():
    max_accuracy = 0
    for folder in ["Count"]:
        for k in range(4, 5):
            denue_wide = pd.read_csv(f"summary/{folder}/denue_wide_{k}.csv")
            rezago = pd.read_csv("rezago_social/rezago_social.csv")
            rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON", "ALT"]]
            df = pd.merge(rezago_social, denue_wide, on=['Key'])
            df.drop(['Key'], axis=1, inplace=True)
            y = df['lgc00_15cl3']
            X = df.iloc[:, 5:].div((df.POB_TOTAL / 1000), axis=0)
            X["LAT"] = rezago_social["LAT"]
            X["LON"] = rezago_social["LON"]
            print(f'# {folder} {k} {X.shape}')
            X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.20,
                                                                random_state=0)
            for ne in [300]:  # [100, 200, 300, 400]:
                for md in [30]:  # [10, 15, 20, 25, 30]:
                    for cri in ['entropy']:  # 'entropy', 'gini']:
                        for mf in ['sqrt']:  # ['sqrt', 'log2']:
                            print('#\t', k, ne, md, cri, mf)
                            clf = RandomForestClassifier(max_depth=md, n_estimators=ne, criterion=cri, max_features=mf,
                                                         random_state=0)
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
    scores = cross_val_score(best_pipe, X, y, cv=5, n_jobs=-1)
    print(f"# {best_folder}, {best_k}: {best_clf} CV5:{np.mean(scores)} +/- {np.std(scores)}")
    #
    # # Mapa
    # y_pred = best_pipe.predict(X)
    # # print(y_pred)
    # gdf = gpd.read_file('municipios/areas_geoestadisticas_municipales.shp')
    # gdf['Key'] = gdf['CVE_ENT'] + gdf['CVE_MUN']
    # rezago = pd.read_csv("rezago_social/rezago_social.csv")
    # rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON"]]
    # rezago_social['Key'] = rezago_social['Key'].astype(str).str.zfill(5)
    # rezago_social['Pred'] = y_pred
    # gdf = gdf.merge(rezago_social, on='Key')
    # colors = {1: 'green', 2: 'yellow', 3: 'red'}
    # fig, ax = plt.subplots()
    # gdf.plot(ax=ax, color=gdf['Pred'].map(colors))
    # plt.axis('off')
    # plt.title("Rezago Social predicho a nivel municipal, 2015.")
    # txt = "Predichos por el modelo RF con base en categorías DENUE/SCIAN a nivel Subrama."
    # plt.figtext(0.01, 0.01, txt, wrap=True, horizontalalignment='left', fontsize=12)
    # plt.show()
    #
    # # Curva ROC
    # y_bin = label_binarize(y, classes=[1, 2, 3])
    # n_classes = y_bin.shape[1]
    # y_score = cross_val_predict(best_pipe, X, y, cv=10, method='predict_proba')
    # fpr = dict()
    # tpr = dict()
    # roc_auc = dict()
    # for i in range(n_classes):
    #     fpr[i], tpr[i], _ = roc_curve(y_bin[:, i], y_score[:, i])
    #     roc_auc[i] = auc(fpr[i], tpr[i])
    # colors = cycle(['blue', 'red', 'green'])
    # for i, color in zip(range(n_classes), colors):
    #     plt.plot(fpr[i], tpr[i], color=color, lw=2,
    #              label='ROC curve of class {0} (area = {1:0.6f})'
    #                    ''.format(i + 1, roc_auc[i]))
    # plt.plot([0, 1], [0, 1], 'k--', lw=2)
    # plt.xlim([-0.05, 1.0])
    # plt.ylim([0.0, 1.05])
    # plt.xlabel('Tasa de Falsos Positivos')
    # plt.ylabel('Tasa de Verdaderos Positivos')
    # plt.title(f"Bosque Aleatorio (RF)\nDENUE/SCIAN a nivel Subrama")
    # plt.legend(loc="lower right")
    # plt.show()


def main_rf2():
    max_accuracy = 0
    combis = [cs for ls in (combinations(range(1, 10), i) for i in range(9, 10)) for cs in ls]
    print(len(combis))
    for folder in ["Count"]:
        for k in range(3, 6):
            for cb, combi in enumerate(combis):
                denue_wide = pd.read_csv(f"summary/{folder}/denue_wide_{k}.csv")
                rezago = pd.read_csv("rezago_social/rezago_social.csv")
                rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON", "ALT", "PER_URB", "PER_RUR"]]
                df = pd.merge(rezago_social, denue_wide, on=['Key'])
                df.drop(['Key'], axis=1, inplace=True)
                y = df['lgc00_15cl3']
                X = df.iloc[:, 7:].div((df.POB_TOTAL / 1000), axis=0)
                X["LAT"] = rezago_social["LAT"]
                X["LON"] = rezago_social["LON"]
                X["ALT"] = rezago_social["ALT"]
                X["PER_URB"] = rezago_social["PER_URB"]
                X["PER_RUR"] = rezago_social["PER_RUR"]
                # SCIAN combinations
                filter_col = ['LAT', 'LON']
                for comb in combi:
                    filter_col.extend([col for col in df if col.startswith(str(comb))])
                X = X.filter(filter_col)
                # print(X.head())
                print(X.columns)
                print(f'# {folder} {k} {X.shape} {cb}')
                X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.20,
                                                                    random_state=0)
                for ne in [100, 200, 300, 400]:
                    for md in [10, 15, 20, 25, 30]:
                        for cri in ['entropy', 'gini']:
                            for mf in ['sqrt', 'log2']:
                                print('#\t', k, ne, md, cri, mf)
                                clf = RandomForestClassifier(max_depth=md, n_estimators=ne, criterion=cri,
                                                             max_features=mf,
                                                             random_state=0)
                                pipeline = make_pipeline(StandardScaler(), clf)
                                scores = cross_val_score(pipeline, X_train, y_train, cv=10, n_jobs=-1)
                                if np.mean(scores) > max_accuracy:
                                    print(f"\t # LR {max_accuracy}, {k}, {cb}, {ne}, {md}, {cri}, {mf}")
                                    max_accuracy = np.mean(scores)
                                    best_clf = clone(clf)
                                    best_folder = folder
                                    best_k = k
                                    Xtrain, ytrain = X_train, y_train
                                    Xtest, ytest = X_test, y_test
                                    Xpred, ypred = X, y
    print(best_clf, max_accuracy)
    best_pipe = make_pipeline(StandardScaler(), best_clf)
    best_pipe.fit(Xtrain, ytrain)
    print(f"# {best_folder}, {best_k}: {best_clf} Train:{best_pipe.score(Xtrain, ytrain) * 100}")
    print(f"# {best_folder}, {best_k}: {best_clf} Test:{best_pipe.score(Xtest, ytest) * 100}")
    scores = cross_val_score(best_pipe, Xpred, ypred, cv=5, n_jobs=-1)
    print(f"# {best_folder}, {best_k}: {best_clf} CV5:{np.mean(scores)} +/- {np.std(scores)}")


def main_all():
    ClasesRS = {0: 'Bajo', 1: 'Medio', 2: 'Alto'}
    print('#### ALL ####')
    for folder in ["Count"]:
        for k in range(3, 5):
            max_accuracy = 0
            denue_wide = pd.read_csv(f"summary/{folder}/denue_wide_{k}.csv")
            rezago = pd.read_csv("rezago_social/rezago_social.csv")
            rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON", "ALT"]]
            df = pd.merge(rezago_social, denue_wide, on=['Key'])
            df.drop(['Key'], axis=1, inplace=True)
            y = df['lgc00_15cl3']
            X = df.iloc[:, 5:].div((df.POB_TOTAL / 1000), axis=0)
            X["LAT"] = rezago_social["LAT"]
            X["LON"] = rezago_social["LON"]
            print(f'# {folder} {k} {X.shape}')
            X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.20,
                                                                random_state=0)
            print(X_test.head())
            print(X.columns)
            for c in [0.1]:  # [0.0001, 0.001, 0.01, 0.1, 0.5, 1.0, 2, 10.0, 100.0, 1000.0]:
                for mc in ['multinomial']:
                    clf = LogisticRegression(solver='lbfgs', multi_class=mc, penalty='l2', C=c, max_iter=10000)
                    pipeline = make_pipeline(StandardScaler(), clf)
                    scores = cross_val_score(pipeline, X_train, y_train, cv=10, n_jobs=-1)
                    if np.mean(scores) > max_accuracy:
                        max_accuracy = np.mean(scores)
                        best_clf = clone(clf)
                        best_folder = folder
                        best_k = k
                        Xtrain, ytrain = X_train, y_train
                        Xtest, ytest = X_test, y_test
                        Xpred, ypred = X, y
            print(best_clf, max_accuracy)
            best_pipe = make_pipeline(StandardScaler(), best_clf)
            best_pipe.fit(Xtrain, ytrain)
            print(f"# {best_folder}, {best_k}: {best_clf} Train:{best_pipe.score(Xtrain, ytrain) * 100}")
            print(f"# {best_folder}, {best_k}: {best_clf} Test:{best_pipe.score(Xtest, ytest) * 100}")
            scores = cross_val_score(best_pipe, Xpred, ypred, cv=5, n_jobs=-1)
            print(f"# {best_folder}, {best_k}: {best_clf} CV5:{np.mean(scores)} +/- {np.std(scores)}")

            # Curva ROC
            y_bin = label_binarize(y, classes=[1, 2, 3])
            n_classes = y_bin.shape[1]
            y_score = cross_val_predict(best_pipe, X, y, cv=10, method='predict_proba')
            fpr = dict()
            tpr = dict()
            roc_auc = dict()
            for i in range(n_classes):
                fpr[i], tpr[i], _ = roc_curve(y_bin[:, i], y_score[:, i])
                roc_auc[i] = auc(fpr[i], tpr[i])
            colors = cycle(['blue', 'red', 'green'])
            for i, color in zip(range(n_classes), colors):
                plt.plot(fpr[i], tpr[i], color=color, lw=2,
                         label='Curva ROC de la clase: {0} (area = {1:0.4f})'
                               ''.format(ClasesRS[i], roc_auc[i]))
            plt.plot([0, 1], [0, 1], 'k--', lw=2)
            plt.xlim([-0.05, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('Tasa de Falsos Positivos')
            plt.ylabel('Tasa de Verdaderos Positivos')
            plt.title(f"Regresión Logítica (LR)\nDENUE/SCIAN a nivel Subsector")
            plt.legend(loc="lower right")
            plt.show()

            #### SVM ####
            for c in [1000.0]:  # [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]:
                for g in [0.0001]:  # [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]:
                    for kr in ['sigmoid', 'rbf']:
                        print('\t#', c, g, kr)
                        clf = SVC(kernel=kr, gamma=g, C=c, probability=True, random_state=0)
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
            scores = cross_val_score(best_pipe, X, y, cv=5, n_jobs=-1)
            print(f"# {best_folder}, {best_k}: {best_clf} CV5:{np.mean(scores)} +/- {np.std(scores)}")

            # Curva ROC
            y_bin = label_binarize(y, classes=[1, 2, 3])
            n_classes = y_bin.shape[1]
            y_score = cross_val_predict(best_pipe, X, y, cv=10, method='predict_proba')
            fpr = dict()
            tpr = dict()
            roc_auc = dict()
            for i in range(n_classes):
                fpr[i], tpr[i], _ = roc_curve(y_bin[:, i], y_score[:, i])
                roc_auc[i] = auc(fpr[i], tpr[i])
            colors = cycle(['blue', 'red', 'green'])
            for i, color in zip(range(n_classes), colors):
                plt.plot(fpr[i], tpr[i], color=color, lw=2,
                         label='Curva ROC de la clase: {0} (area = {1:0.4f})'
                               ''.format(ClasesRS[i], roc_auc[i]))
            plt.plot([0, 1], [0, 1], 'k--', lw=2)
            plt.xlim([-0.05, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('Tasa de Falsos Positivos')
            plt.ylabel('Tasa de Verdaderos Positivos')
            plt.title(f"Máquina de Soporte Vectorial (SVM)\nDENUE/SCIAN a nivel Subsector")
            plt.legend(loc="lower right")
            plt.show()

            #### RF ####
            for ne in [300]:  # [100, 200, 300, 400]:
                for md in [30]:  # [10, 15, 20, 25, 30]:
                    for cri in ['entropy']:  # 'entropy', 'gini']:
                        for mf in ['sqrt']:  # ['sqrt', 'log2']:
                            print('#\t', k, ne, md, cri, mf)
                            clf = RandomForestClassifier(max_depth=md, n_estimators=ne, criterion=cri, max_features=mf,
                                                         random_state=0)
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
            scores = cross_val_score(best_pipe, X, y, cv=5, n_jobs=-1)
            print(f"# {best_folder}, {best_k}: {best_clf} CV5:{np.mean(scores)} +/- {np.std(scores)}")

            # Mapa
            y_pred = best_pipe.predict(X)
            # print(y_pred)
            gdf = gpd.read_file('municipios/areas_geoestadisticas_municipales.shp')
            gdf['Key'] = gdf['CVE_ENT'] + gdf['CVE_MUN']
            rezago = pd.read_csv("rezago_social/rezago_social.csv")
            rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON"]]
            rezago_social['Key'] = rezago_social['Key'].astype(str).str.zfill(5)
            rezago_social['Pred'] = y_pred
            gdf = gdf.merge(rezago_social, on='Key')
            colors = {1: 'green', 2: 'yellow', 3: 'red'}
            fig, ax = plt.subplots()
            gdf.plot(ax=ax, color=gdf['Pred'].map(colors))
            plt.axis('off')
            plt.title("Rezago Social predicho a nivel municipal, 2015.")
            txt = "Predichos por el modelo RF con base en categorías DENUE/SCIAN a nivel Rama."
            plt.figtext(0.01, 0.01, txt, wrap=True, horizontalalignment='left', fontsize=12)
            plt.show()

            # Curva ROC
            y_bin = label_binarize(y, classes=[1, 2, 3])
            n_classes = y_bin.shape[1]
            y_score = cross_val_predict(best_pipe, X, y, cv=10, method='predict_proba')
            fpr = dict()
            tpr = dict()
            roc_auc = dict()
            for i in range(n_classes):
                fpr[i], tpr[i], _ = roc_curve(y_bin[:, i], y_score[:, i])
                roc_auc[i] = auc(fpr[i], tpr[i])
            colors = cycle(['blue', 'red', 'green'])
            for i, color in zip(range(n_classes), colors):
                plt.plot(fpr[i], tpr[i], color=color, lw=2,
                         label='Curva ROC de la clase: {0} (area = {1:0.4f})'
                               ''.format(ClasesRS[i], roc_auc[i]))
            plt.plot([0, 1], [0, 1], 'k--', lw=2)
            plt.xlim([-0.05, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('Tasa de Falsos Positivos')
            plt.ylabel('Tasa de Verdaderos Positivos')
            plt.title(f"Bosque Aleatorio (RF)\nDENUE/SCIAN a nivel Rama")
            plt.legend(loc="lower right")
            plt.show()


if __name__ == '__main__':
    main_all()
    # main_svm()
    # main_rf()
    # main_all()

# RandomForestClassifier(criterion='entropy', max_depth=30, max_features='sqrt',
#                        n_estimators=300, random_state=0) 0.7846990572878897
# # Count, 4: RandomForestClassifier(criterion='entropy', max_depth=30, max_features='sqrt',
#                        n_estimators=300, random_state=0) Train:100.0
# # Count, 4: RandomForestClassifier(criterion='entropy', max_depth=30, max_features='sqrt',
#                        n_estimators=300, random_state=0) Test:75.20325203252033
# # Count, 4: RandomForestClassifier(criterion='entropy', max_depth=30, max_features='sqrt',
#                        n_estimators=300, random_state=0) CV5:0.7464457801400824 +/- 0.015779792193927757

# SVC(C=1000.0, gamma=0.0001, kernel='sigmoid', probability=True) 0.7623536724334403 Count, 3: SVC(C=1000.0,
# gamma=0.0001, kernel='sigmoid', probability=True) Train:81.32315521628499 Count, 3: SVC(C=1000.0, gamma=0.0001,
# kernel='sigmoid', probability=True) Test:74.39024390243902 Count, 3: SVC(C=1000.0, gamma=0.0001, kernel='sigmoid',
# probability=True) CV5:0.7098181908499329 +/- 0.022589708124599744
