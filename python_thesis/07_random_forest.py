from matplotlib.lines import Line2D
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
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


def plot_multiclass_roc(clf, X_test, y_test, n_classes, figsize=(17, 6)):
    y_score = clf.predict_proba(X_test)

    # structures
    fpr = dict()
    tpr = dict()
    roc_auc = dict()

    # calculate dummies once
    y_test_dummies = pd.get_dummies(y_test, drop_first=False).values
    for i in range(n_classes):
        fpr[i], tpr[i], _ = roc_curve(y_test_dummies[:, i], y_score[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])

    # roc for each class
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot([0, 1], [0, 1], 'k--')
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.set_xlabel('False Positive Rate')
    ax.set_ylabel('True Positive Rate')
    ax.set_title('Receiver operating characteristic example')
    for i in range(n_classes):
        ax.plot(fpr[i], tpr[i], label='ROC curve (area = %0.2f) for label %i' % (roc_auc[i], i))
    ax.legend(loc="best")
    ax.grid(alpha=.4)
    sns.despine()
    plt.show()


def main_clf(metric_, clf_, grid_, range_=(2, 7), cv_=5, verb_=False, graphs=False):
    pipe = Pipeline(steps=[('sc', StandardScaler()), ('clf', clf_)])
    max_scoring = 0
    for k in range(*range_):
        denue_wide = pd.read_csv(f"summary/Count/denue_wide_{k}.csv")  ###
        rezago = pd.read_csv("rezago_social/rezago_social.csv")
        rezago_social = rezago[["lgc00_15cl3_2", "Key", "POB_TOTAL", "LAT", "LON"]]
        df = pd.merge(rezago_social, denue_wide, on=['Key'])
        y = rezago_social['lgc00_15cl3_2']
        df.drop(["lgc00_15cl3_2", "Key", "LAT", "LON"], axis=1, inplace=True)
        X = df.div(df.POB_TOTAL, axis=0) * 1000
        X.drop(["POB_TOTAL"], axis=1, inplace=True)
        X["LAT"] = rezago_social["LAT"]
        X["LON"] = rezago_social["LON"]
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

    print(np.unique(np.array(y_pred),return_counts=True))

    if graphs:
        # plot_multiclass_roc(best_pipe, X_, y_, n_classes=3, figsize=(16, 10))
        probas = cross_val_predict(best_pipe, X_, y_, cv=cv_, method='predict_proba')
        fig, (ax1, ax2) = plt.subplots(1, 2)
        skplt.metrics.plot_roc(y_, probas, ax=ax1, title='')
        handles, labels = ax1.get_legend_handles_labels()
        # print(labels)
        labels = [lb.replace(' 1 ', ' A ').replace(' 2 ', ' M ').replace(' 3 ', ' B ') for lb in labels]
        # print(labels)
        ax1.legend(handles, labels)
        ax1.get_figure()
        ax1.set_xlabel('TFP\n(A)')
        skplt.metrics.plot_precision_recall(y_, probas, ax=ax2, title='')
        handles, labels = ax2.get_legend_handles_labels()
        # print(labels)
        labels = [lb.replace(' 1 ', ' A ').replace(' 2 ', ' M ').replace(' 3 ', ' B ') for lb in labels]
        # print(labels)
        ax2.legend(handles, labels)
        ax2.get_figure()
        ax2.set_xlabel('S\n(B)')
        plt.show()

        ### 2016
        denue_2016 = pd.read_csv(f"summary/201610/denue_wide_{best_k}.csv")  ###
        df_2016 = pd.merge(rezago_social, denue_2016, on=['Key'])
        df_2016.drop(["lgc00_15cl3_2", "Key", "LAT", "LON"], axis=1, inplace=True)
        X_2016 = df_2016.div(df.POB_TOTAL, axis=0) * 1000
        X_2016.drop(["POB_TOTAL"], axis=1, inplace=True)
        X_2016["LAT"] = rezago_social["LAT"]
        X_2016["LON"] = rezago_social["LON"]
        print(X_2016.columns)
        y_pred_2016 = best_pipe.predict(X_2016)
        ### 2017
        denue_2017 = pd.read_csv(f"summary/201711/denue_wide_{best_k}.csv")  ###
        df_2017 = pd.merge(rezago_social, denue_2017, on=['Key'])
        df_2017.drop(["lgc00_15cl3_2", "Key", "LAT", "LON"], axis=1, inplace=True)
        X_2017 = df_2017.div(df.POB_TOTAL, axis=0) * 1000
        X_2017.drop(["POB_TOTAL"], axis=1, inplace=True)
        X_2017["LAT"] = rezago_social["LAT"]
        X_2017["LON"] = rezago_social["LON"]
        y_pred_2017 = best_pipe.predict(X_2017)
        # ### 2018
        # denue_2018 = pd.read_csv(f"summary/201811/denue_wide_{best_k}.csv")  ###
        # df_2018 = pd.merge(rezago_social, denue_2018, on=['Key'])
        # df_2018.drop(["lgc00_15cl3", "Key", "LAT", "LON"], axis=1, inplace=True)
        # X_2018 = df_2018.div(df.POB_TOTAL, axis=0) * 1000
        # X_2018.drop(["POB_TOTAL"], axis=1, inplace=True)
        # X_2018["LAT"] = rezago_social["LAT"]
        # X_2018["LON"] = rezago_social["LON"]
        # y_pred_2018 = best_pipe.predict(X_2018)
        # ### 2019
        # denue_2019 = pd.read_csv(f"summary/201911/denue_wide_{best_k}.csv")  ###
        # df_2019 = pd.merge(rezago_social, denue_2019, on=['Key'])
        # df_2019.drop(["lgc00_15cl3", "Key", "LAT", "LON"], axis=1, inplace=True)
        # X_2019 = df_2019.div(df.POB_TOTAL, axis=0) * 1000
        # X_2019.drop(["POB_TOTAL"], axis=1, inplace=True)
        # X_2019["LAT"] = rezago_social["LAT"]
        # X_2019["LON"] = rezago_social["LON"]
        # y_pred_2019 = best_pipe.predict(X_2019)
        # ### 2020
        # denue_2020 = pd.read_csv(f"summary/202011/denue_wide_{best_k}.csv")  ###
        # df_2020 = pd.merge(rezago_social, denue_2020, on=['Key'])
        # df_2020.drop(["lgc00_15cl3", "Key", "LAT", "LON"], axis=1, inplace=True)
        # X_2020 = df_2020.div(df.POB_TOTAL, axis=0) * 1000
        # X_2020.drop(["POB_TOTAL"], axis=1, inplace=True)
        # X_2020["LAT"] = rezago_social["LAT"]
        # X_2020["LON"] = rezago_social["LON"]
        # y_pred_2020 = best_pipe.predict(X_2020)
        # Confusion matrix
        skplt.metrics.plot_confusion_matrix(y_, y_pred, normalize=True, title=" ")
        plt.xticks([0, 1, 2], ['B', 'M', 'A'], rotation='horizontal')
        plt.yticks([0, 1, 2], ['B', 'M', 'A'], rotation='horizontal')
        plt.xlabel('Clases predichas')
        plt.ylabel('Clases verdaderas')
        plt.show()
        # Mapa
        rezago_social['Pred'] = y_pred
        rezago_social['Pred_2016'] = y_pred_2016
        rezago_social['Pred_2017'] = y_pred_2017
        # rezago_social['Pred_2018'] = y_pred_2018
        # rezago_social['Pred_2019'] = y_pred_2019
        # rezago_social['Pred_2020'] = y_pred_2020
        rezago_social.to_csv('predictions.csv')  ###
        rezago_social['Key_'] = rezago_social['Key'].astype(str).str.zfill(5)
        gdf = gpd.read_file('municipios/areas_geoestadisticas_municipales.shp')
        gdf['Key_'] = gdf['CVE_ENT'] + gdf['CVE_MUN']
        gdf = gdf.merge(rezago_social, on='Key_')
        legend_elements = [Line2D([0], [0], marker='o', color='w', label='B',
                                  markerfacecolor='g', markersize=10, ),
                           Line2D([0], [0], marker='o', color='w', label='M',
                                  markerfacecolor='yellow', markersize=10),
                           Line2D([0], [0], marker='o', color='w', label='A',
                                  markerfacecolor='r', markersize=10)]
        csfont = {'fontname': 'Times New Roman'}
        font = font_manager.FontProperties(family='Times New Roman', weight='normal', style='normal', size=12)
        colors = {3: 'green', 2: 'yellow', 1: 'red'}
        models = {'RandomForestClassifier': 'RF', 'SCV': 'SVM', 'LogisticRegression': 'LR'}
        ###
        # gdf.plot(color=gdf['Pred_2016'].map(colors))
        # plt.xticks([])
        # plt.yticks([])
        # txt = f"Categorías predichas por modelo {models.get(clf.__class__.__name__, 'ABC')}, para el año 201X."
        # plt.text(800000, 0.01, txt, wrap=True, horizontalalignment='left', fontsize=12, **csfont)
        # plt.legend(handles=legend_elements, prop=font)
        # plt.show()
        ### Mapa
        fig, (ax1, ax2) = plt.subplots(1, 2)
        gdf.plot(ax=ax1, color=gdf['Pred_2016'].map(colors))
        ax1.set_xticks([])
        ax1.set_yticks([])
        # txt = f"(A) Clases predichas con modelo {models.get(clf.__class__.__name__, 'ABC')} en 2016"
        ax1.set_xlabel("(A)", **csfont)
        # ax1.text(800000, 0.01, txt, wrap=True, horizontalalignment='center', fontsize=12, **csfont)
        ax1.legend(handles=legend_elements, prop=font)
        gdf.plot(ax=ax2, color=gdf['Pred_2017'].map(colors))
        ax2.set_xticks([])
        ax2.set_yticks([])
        # txt = f"(B) Clases predichas con modelo {models.get(clf.__class__.__name__, 'ABC')} en 2017"
        ax2.set_xlabel("(B)", **csfont)
        # ax2.text(800000, 0.01, txt, wrap=True, horizontalalignment='center', fontsize=12, **csfont)
        ax2.legend(handles=legend_elements, prop=font)
        plt.show()

        ### Mapa
        fig, (ax1, ax2) = plt.subplots(1, 2)
        gdf.plot(ax=ax1, color=gdf['lgc00_15cl3_2'].map(colors), legend=True)
        ax1.set_xticks([])
        ax1.set_yticks([])
        # txt = "(A) Clases de acuerdo a Valdés-Cruz y Vargas-Chanes (2017)"
        ax1.set_xlabel("(A)", **csfont)
        # ax1.text(800000, 0.01, txt, wrap=True, horizontalalignment='center', fontsize=12, **csfont)
        ax1.legend(handles=legend_elements, prop=font)
        gdf.plot(ax=ax2, color=gdf['Pred'].map(colors))
        ax2.set_xticks([])
        ax2.set_yticks([])
        # txt = f"(B) Clases predichas con modelo {models.get(clf.__class__.__name__, 'ABC')} en 2015"
        ax2.set_xlabel("(B)", **csfont)
        # ax2.text(800000, 0.01, txt, wrap=True, horizontalalignment='center', fontsize=12, **csfont)
        ax2.legend(handles=legend_elements, prop=font)
        plt.show()
        # Curva ROC
        y_bin = label_binarize(y, classes=[1, 2, 3])
        n_classes = y_bin.shape[1]
        y_score = cross_val_predict(best_pipe, X_, y_, cv=cv_, method='predict_proba')
        fpr = dict()
        tpr = dict()
        roc_auc = dict()
        for i in range(n_classes):
            fpr[i], tpr[i], _ = roc_curve(y_bin[:, i], y_score[:, i])
            roc_auc[i] = auc(fpr[i], tpr[i])
        all_fpr = np.unique(np.concatenate([fpr[i] for i in range(n_classes)]))
        mean_tpr = np.zeros_like(all_fpr)
        for i in range(n_classes):
            mean_tpr += np.interp(all_fpr, fpr[i], tpr[i])
        mean_tpr /= n_classes
        fpr["macro"] = all_fpr
        tpr["macro"] = mean_tpr
        roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])
        plt.figure()
        plt.plot(fpr["macro"], tpr["macro"],
                 label='ROC macro (AUC = {0:0.3f})'
                       ''.format(roc_auc["macro"]),
                 color='navy', linestyle=':', linewidth=4)
        rezago = {1: 'B', 2: 'M', 3: 'A'}
        colors = cycle(['green', 'yellow', 'red'])
        for i, color in zip(range(n_classes), colors):
            plt.plot(fpr[i], tpr[i], color=color, lw=2,
                     label='Clase de rezago {0} (AUC = {1:0.3f})'
                           ''.format(rezago[i + 1], roc_auc[i]))
        plt.plot([0, 1], [0, 1], 'k--', lw=2)
        plt.xlim([-0.05, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('TFP', fontsize=12, **csfont)
        plt.ylabel('TVP', fontsize=12, **csfont)
        plt.legend(loc="lower right", prop=font)
        plt.show()
    return scores_


if __name__ == '__main__':
    # Metrica de desempeño
    metric = 'f1_macro'
    # Random Forest
    grid = [{"clf__n_estimators": [250],
             "clf__criterion": ['entropy'],
             "clf__max_features": ['sqrt'],
             "clf__max_depth": [20]}, ]
    clf = RandomForestClassifier(random_state=0)
    main_clf(metric, clf, grid, range_=(3, 4), graphs=False)
