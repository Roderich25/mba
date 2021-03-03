from matplotlib.lines import Line2D
from sklearn.metrics import f1_score, make_scorer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.base import clone
from sklearn.svm import SVC
from sklearn.metrics import roc_curve, auc, classification_report, roc_auc_score
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, label_binarize
import numpy as np
import pandas as pd
from itertools import combinations
from matplotlib import pyplot as plt
from itertools import cycle
import geopandas as gpd


def main_lr(metric):
    max_accuracy_lr = 0
    for k in range(3, 4):
        denue_wide = pd.read_csv(f"summary/Count/denue_wide_{k}.csv")
        rezago = pd.read_csv("rezago_social/rezago_social.csv")
        rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON"]]
        df = pd.merge(rezago_social, denue_wide, on=['Key'])
        df.drop(['Key'], axis=1, inplace=True)
        y = df['lgc00_15cl3']
        X = df.iloc[:, 5:].div(df.POB_TOTAL, axis=0) * 1000
        X["LAT"] = rezago_social["LAT"]
        X["LON"] = rezago_social["LON"]
        # X["POB_TOTAL"] = rezago_social["POB_TOTAL"]
        print(f'# LR {k} {X.shape}')
        X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.20, random_state=0)
        for c in [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]:
            for mc in ['multinomial']:
                clf = LogisticRegression(solver='lbfgs', multi_class=mc, penalty='l2', C=c, max_iter=10000,
                                         random_state=0)
                pipeline = make_pipeline(StandardScaler(), clf)
                scores = cross_val_score(pipeline, X_train, y_train, cv=10, n_jobs=-1, scoring=metric)
                # print(scores, np.mean(scores))
                if np.mean(scores) > max_accuracy_lr:
                    max_accuracy_lr = np.mean(scores)
                    print(f"\t # LR {max_accuracy_lr}, {k}, {c}, {mc}")
                    best_clf = clone(clf)
                    best_k = k
                    Xtrain, ytrain = X_train, y_train
                    Xtest, ytest = X_test, y_test
                    Xpred, ypred = X, y
    print(best_clf, max_accuracy_lr)
    best_pipe = make_pipeline(StandardScaler(), best_clf)
    best_pipe.fit(Xtrain, ytrain)
    print(f"# {best_k}: {best_clf} Train:{best_pipe.score(Xtrain, ytrain) * 100}")
    print(f"# {best_k}: {best_clf} Test:{best_pipe.score(Xtest, ytest) * 100}")
    scores = cross_val_score(best_pipe, Xpred, ypred, cv=5, n_jobs=-1, scoring='accuracy')
    print(f"# {best_k}: {best_clf} CV5:{np.mean(scores)} +/- {np.std(scores)}")
    scores = cross_val_score(best_pipe, Xpred, ypred, cv=5, n_jobs=-1, scoring=metric)
    print(f"# {best_k}: {best_clf} CV5:{np.mean(scores)} +/- {np.std(scores)}")
    # Classification Report
    y_pred = cross_val_predict(best_pipe, X, y, cv=10)
    print(classification_report(y, y_pred, digits=3))

    # print(roc_auc_score(y, y_pred, multi_class='ovr'))
    # Mapa
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
    # txt = "Predichos por modelo LR con base en categorías DENUE/SCIAN a nivel Subsector."
    # plt.figtext(0.01, 0.01, txt, wrap=True, horizontalalignment='left', fontsize=12)
    # plt.show()


def main_svm(metric):
    max_accuracy_svm = 0
    for k in range(3, 4):
        denue_wide = pd.read_csv(f"summary/Count/denue_wide_{k}.csv")
        rezago = pd.read_csv("rezago_social/rezago_social.csv")
        rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON"]]
        df = pd.merge(rezago_social, denue_wide, on=['Key'])
        df.drop(['Key'], axis=1, inplace=True)
        y = df['lgc00_15cl3']
        X = df.iloc[:, 5:].div(df.POB_TOTAL, axis=0) * 1000
        X["LAT"] = rezago_social["LAT"]
        X["LON"] = rezago_social["LON"]
        print(f'# SVM {k} {X.shape}')
        X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.20, random_state=42)
        for c in [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]:
            for g in [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]:
                for kr in ['rbf', 'sigmoid']:
                    print('\t#', c, g, kr)
                    clf = SVC(kernel=kr, gamma=g, C=c, probability=True, random_state=0)
                    pipeline = make_pipeline(StandardScaler(), clf)
                    # scores = cross_val_score(pipeline, X_train, y_train, cv=10, n_jobs=-1, scoring=metric)
                    scores = cross_val_score(pipeline, X_train, y_train, cv=10, n_jobs=-1,
                                             scoring=make_scorer(f1_score, average='macro', labels=[3]))
                    # print(scores, np.mean(scores))
                    if np.mean(scores) > max_accuracy_svm:
                        max_accuracy_svm = np.mean(scores)
                        print(f"\t # SVM {max_accuracy_svm}, {c}, {g}, {kr}")
                        best_clf = clone(clf)
                        best_k = k
                        Xtrain, ytrain = X_train, y_train
                        Xtest, ytest = X_test, y_test
                        Xpred, ypred = X, y
    print(best_clf, max_accuracy_svm)
    best_pipe = make_pipeline(StandardScaler(), best_clf)
    best_pipe.fit(Xtrain, ytrain)
    print(f"# {best_k}: {best_clf} Train:{best_pipe.score(Xtrain, ytrain) * 100}")
    print(f"# {best_k}: {best_clf} Test:{best_pipe.score(Xtest, ytest) * 100}")
    scores = cross_val_score(best_pipe, Xpred, ypred, cv=5, n_jobs=-1, scoring='accuracy')
    print(f"# {best_k}: {best_clf} CV5:{np.mean(scores)} +/- {np.std(scores)}")
    scores = cross_val_score(best_pipe, Xpred, ypred, cv=5, n_jobs=-1, scoring=metric)
    print(f"# {best_k}: {best_clf} CV5:{np.mean(scores)} +/- {np.std(scores)}")
    # Classification Report
    y_pred = cross_val_predict(best_pipe, X, y, cv=5)
    print(classification_report(y, y_pred, digits=3))

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
    # txt = "Predichos por modelo SVM kernel RBF con base en categorías DENUE/SCIAN a nivel Subsector."
    # plt.figtext(0.01, 0.01, txt, wrap=True, horizontalalignment='left', fontsize=12)
    # plt.show()


def main_rf(metric, mapa=False):
    max_accuracy_rf = 0
    for k in range(4, 5):
        denue_wide = pd.read_csv(f"summary/Count/denue_wide_{k}.csv")
        rezago = pd.read_csv("rezago_social/rezago_social.csv")
        rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON"]]
        df = pd.merge(rezago_social, denue_wide, on=['Key'])
        df.drop(['Key'], axis=1, inplace=True)
        y = df['lgc00_15cl3']  # .map({1: 0, 2: 0, 3: 1})
        X = df.iloc[:, 5:].div(df.POB_TOTAL, axis=0) * 1000
        X["LAT"] = rezago_social["LAT"]
        X["LON"] = rezago_social["LON"]
        print(X.head())
        print(f'# RF {k} {X.shape}')
        X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.20, random_state=0)
        for ne in [300]:
            for md in [20]:
                for cri in ['entropy']:
                    for mf in ['sqrt']:
                        print('#\t', k, ne, md, cri, mf)
                        clf = RandomForestClassifier(max_depth=md, n_estimators=ne, criterion=cri, max_features=mf,
                                                     random_state=0)
                        pipeline = make_pipeline(StandardScaler(), clf)
                        scores = cross_val_score(pipeline, X_train, y_train, cv=10, n_jobs=-1, scoring=metric)
                        if np.mean(scores) > max_accuracy_rf:
                            max_accuracy_rf = np.mean(scores)
                            print(f"\t # RF {max_accuracy_rf}, {ne}, {md}, {cri}, {mf}")
                            best_clf = clone(clf)
                            best_k = k
                            Xtrain, ytrain = X_train, y_train
                            Xtest, ytest = X_test, y_test
                            Xpred, ypred = X, y
    print(best_clf, max_accuracy_rf)
    best_pipe = make_pipeline(StandardScaler(), best_clf)
    best_pipe.fit(Xtrain, ytrain)
    print(f"# {best_k}: {best_clf} Train:{best_pipe.score(Xtrain, ytrain) * 100}")
    print(f"# {best_k}: {best_clf} Test:{best_pipe.score(Xtest, ytest) * 100}")
    scores = cross_val_score(best_pipe, Xpred, ypred, cv=5, n_jobs=-1, scoring='accuracy')
    print(f"# {best_k}: {best_clf} CV5:{np.mean(scores)} +/- {np.std(scores)}")
    scores = cross_val_score(best_pipe, Xpred, ypred, cv=5, n_jobs=-1, scoring=metric)
    print(f"# {best_k}: {best_clf} CV5:{np.mean(scores)} +/- {np.std(scores)}")
    # Classification Report
    y_pred = cross_val_predict(best_pipe, Xpred, ypred, cv=10)
    print(classification_report(ypred, y_pred, digits=3))

    #
    # csfont = {'fontname': 'Times New Roman'}
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
    # plt.title("Rezago Social predicho a nivel municipal, 2015.", **csfont)
    # txt = "Predichos por el modelo RF con base en categorías DENUE/SCIAN a nivel Rama."
    # plt.figtext(0.01, 0.01, txt, wrap=True, horizontalalignment='left', fontsize=12)
    # plt.show()
    if mapa:
        ###
        gdf = gpd.read_file('municipios/areas_geoestadisticas_municipales.shp')
        print(gdf.columns)
        gdf['Key'] = gdf['CVE_ENT'] + gdf['CVE_MUN']

        rezago = pd.read_csv("rezago_social/rezago_social.csv")
        rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON"]]
        rezago_social['Key'] = rezago_social['Key'].astype(str).str.zfill(5)

        gdf = gdf.merge(rezago_social, on='Key')
        legend_elements = [Line2D([0], [0], marker='o', color='w', label='Alto',
                                  markerfacecolor='r', markersize=15),
                           Line2D([0], [0], marker='o', color='w', label='Medio',
                                  markerfacecolor='yellow', markersize=15),
                           Line2D([0], [0], marker='o', color='w', label='Bajo',
                                  markerfacecolor='g', markersize=15)]
        csfont = {'fontname': 'Times New Roman'}
        colors = {1: 'green', 2: 'yellow', 3: 'red'}
        fig, (ax1, ax2) = plt.subplots(1, 2)
        gdf.plot(ax=ax1, color=gdf['lgc00_15cl3'].map(colors), legend=True)
        # centers.plot(ax=ax, column='capital', marker='*', markersize=1, color='black')
        # plt.axis('off')
        ax1.set_xticks([])
        ax1.set_yticks([])
        # ax1.set_title("Mapa de Rezago Social a nivel municipal, 2015.", **csfont)
        txt = "Categorías de Rezago Social sugeridas por Valdez-Cruz y Vargas-Chanes (2017)."
        ax1.text(0.01, 0.01, txt, wrap=True, horizontalalignment='left', fontsize=12, **csfont)
        ax1.legend(handles=legend_elements)
        ###
        gdf = gpd.read_file('municipios/areas_geoestadisticas_municipales.shp')
        gdf['Key'] = gdf['CVE_ENT'] + gdf['CVE_MUN']
        rezago = pd.read_csv("rezago_social/rezago_social.csv")
        rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON"]]
        rezago_social['Key'] = rezago_social['Key'].astype(str).str.zfill(5)
        rezago_social['Pred'] = y_pred
        gdf = gdf.merge(rezago_social, on='Key')
        #fig, ax = plt.subplots()
        gdf.plot(ax=ax2, color=gdf['Pred'].map(colors))
        # gdf.plot(ax=ax2, color=gdf['lgc00_15cl3'].map(colors), legend=True)
        # centers.plot(ax=ax, column='capital', marker='*', markersize=1, color='black')

        # plt.axis('off')
        ax2.set_xticks([])
        ax2.set_yticks([])
        #ax2.set_title("Mapa de Rezago Social a nivel municipal, 2015.", **csfont)
        txt = "Categorías de Rezago Social sugeridas por Valdez-Cruz y Vargas-Chanes (2017)."
        ax2.text(0.01, 0.01, txt, wrap=True, horizontalalignment='left', fontsize=12, **csfont)
        ax2.legend(handles=legend_elements)
        ###
        plt.show()
    # importance_vals = best_clf.feature_importances_
    # std = np.std([tree.feature_importances_ for tree in best_clf.estimators_],
    #              axis=0)
    # indices = np.argsort(importance_vals)[::-1]

    # Plot the feature importances of the forest
    # plt.figure()
    # plt.title("Importancia de variables de entrada (RF)")
    # plt.bar(range(X.shape[1])[:10], importance_vals[indices][:10], align="center")
    # plt.xticks(range(X.shape[1])[:10], X.columns[indices][:10])
    # plt.xlim([-1, 10])
    # plt.ylim([0, 0.1])
    # plt.show()
    # Mapa
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
    # txt = "Predichos por el modelo RF con base en categorías DENUE/SCIAN a nivel Rama."
    # plt.figtext(0.01, 0.01, txt, wrap=True, horizontalalignment='left', fontsize=12)
    # plt.show()
    #
    # Curva ROC
    # y_bin = label_binarize(y, classes=[1, 2, 3])
    # n_classes = y_bin.shape[1]
    # y_score = cross_val_predict(best_pipe, X, y, cv=10, method='predict_proba')
    # fpr = dict()
    # tpr = dict()
    # roc_auc = dict()
    # rezago = { 1:'bajo', 2:'medio', 3:'alto'}
    # for i in range(n_classes):
    #     fpr[i], tpr[i], _ = roc_curve(y_bin[:, i], y_score[:, i])
    #     roc_auc[i] = auc(fpr[i], tpr[i])
    # colors = cycle(['green', 'yellow', 'red'])
    # for i, color in zip(range(n_classes), colors):
    #     plt.plot(fpr[i], tpr[i], color=color, lw=2,
    #              label='Curva ROC para predicción de rezago {0} (area = {1:0.4f})'
    #                    ''.format(rezago[i + 1], roc_auc[i]))
    # plt.plot([0, 1], [0, 1], 'k--', lw=2)
    # plt.xlim([-0.05, 1.0])
    # plt.ylim([0.0, 1.05])
    # plt.xlabel('Tasa de Falsos Positivos')
    # plt.ylabel('Tasa de Verdaderos Positivos')
    # plt.title(f"Bosque Aleatorio (RF)\nDENUE/SCIAN a nivel Rama")
    # plt.legend(loc="lower right")
    # plt.show()


def main_rf2():
    max_accuracy_rf = 0
    for k in range(4, 5):
        denue_wide = pd.read_csv(f"summary/Count/denue_wide_{k}.csv")
        rezago = pd.read_csv("rezago_social/rezago_social.csv")
        rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON"]]
        df = pd.merge(rezago_social, denue_wide, on=['Key'])
        df.drop(['Key'], axis=1, inplace=True)
        y = df['lgc00_15cl3']
        X0 = df.iloc[:, 5:].div(df.POB_TOTAL, axis=0) * 1000
        X = pd.DataFrame()
        X["LAT"] = rezago_social["LAT"]
        X["LON"] = rezago_social["LON"]
        X["8111"] = X0["8111"]
        X["7139"] = X0["7139"]
        X["5311"] = X0["5311"]
        X["8121"] = X0["8121"]
        X["6212"] = X0["6212"]
        X["4343"] = X0["4343"]
        X["3118"] = X0["3118"]
        X["8114"] = X0["8114"]
        print(X.head())
        print(y.value_counts(normalize=True))
        print(y.value_counts(normalize=False))
        print(f'# RF {k} {X.shape}')
        X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.20, random_state=0)
        for ne in [300]:  # [100, 200, 300, 400]:
            for md in [30]:  # [10, 15, 20, 25, 30]:
                for cri in ['entropy']:  # ['entropy', 'gini']:
                    for mf in ['sqrt']:  # ['sqrt', 'log2']:
                        print('#\t', k, ne, md, cri, mf)
                        clf = RandomForestClassifier(max_depth=md, n_estimators=ne, criterion=cri, max_features=mf,
                                                     random_state=0)
                        pipeline = make_pipeline(StandardScaler(), clf)
                        scores = cross_val_score(pipeline, X_train, y_train, cv=10, n_jobs=-1)
                        if np.mean(scores) > max_accuracy_rf:
                            max_accuracy_rf = np.mean(scores)
                            print(f"\t # SVM {max_accuracy_rf}, {ne}, {md}, {cri}, {mf}")
                            best_clf = clone(clf)
                            best_k = k
                            Xtrain, ytrain = X_train, y_train
                            Xtest, ytest = X_test, y_test
                            Xpred, ypred = X, y
    print(best_clf, max_accuracy_rf)
    best_pipe = make_pipeline(StandardScaler(), best_clf)
    best_pipe.fit(Xtrain, ytrain)
    print(f"# {best_k}: {best_clf} Train:{best_pipe.score(Xtrain, ytrain) * 100}")
    print(f"# {best_k}: {best_clf} Test:{best_pipe.score(Xtest, ytest) * 100}")
    scores = cross_val_score(best_pipe, Xpred, ypred, cv=5, n_jobs=-1)
    print(f"# {best_k}: {best_clf} CV5:{np.mean(scores)} +/- {np.std(scores)}")

    importance_vals = best_clf.feature_importances_
    std = np.std([tree.feature_importances_ for tree in best_clf.estimators_],
                 axis=0)
    indices = np.argsort(importance_vals)[::-1]

    # Plot the feature importances of the forest
    plt.figure()
    plt.title("Importancia de variables de entrada (RF)")
    plt.bar(range(X.shape[1]), importance_vals[indices],
            yerr=std[indices], align="center")
    plt.xticks(range(X.shape[1]), X.columns[indices])
    plt.xlim([-1, X.shape[1]])
    plt.ylim([0, 0.5])
    plt.show()
    # Mapa
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
    # txt = "Predichos por el modelo RF con base en categorías DENUE/SCIAN a nivel Rama."
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


if __name__ == '__main__':
    # main_lr('f1_macro')
    main_rf('f1_macro')
    # main_svm()
    # main_rf('f1_weighted')
    # main_rf('balanced_accuracy')
