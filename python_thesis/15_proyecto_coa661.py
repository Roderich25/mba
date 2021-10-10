import pandas as pd
from sklearn.base import clone
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc, plot_confusion_matrix
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, label_binarize
import numpy as np
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from itertools import cycle

ClasesRS = {0: 'Muy bajo', 1: 'Bajo', 2: 'Medio', 3: 'Alto', 4: 'Muy alto'}
ClasesRS2 = {'Muy bajo': 0, 'Bajo': 1, 'Medio': 2, 'Alto': 3, 'Muy alto': 4}

def main():
    max_lr = 0.5
    max_svc_l = 0.5
    max_svc_rbf = 0.5
    max_rf = 0.5
    max_mlp = 0.5

    for k in range(4, 5):
        denue_wide = pd.read_csv(f"summary/Count/denue_wide_{k}.csv")
        rezago = pd.read_csv("rezago_social/rezago_coneval.csv")
        rezago_social = rezago[["grs2015", "Key", "p2015", "lat", "lon", "alt"]]
        df = pd.merge(rezago_social, denue_wide, on=['Key'])
        df.drop(['Key'], axis=1, inplace=True)
        y = df['grs2015'].map(ClasesRS2)
        print('unique1:', np.unique(y))
        X = df.iloc[:, 5:].div((df.p2015 / 1000), axis=0)
        X["p2015"] = rezago_social["p2015"]
        X["alt"] = rezago_social["alt"]
        X["lat"] = rezago_social["lat"]
        X["lon"] = rezago_social["lon"]
        # print(X.head())

        # # Gráficos de correlación
        # print(X.head())
        # print(X.corr())
        # plt.matshow(X.corr())
        # plt.colorbar()
        # cat = {2: 'Sector', 3: 'Subsector', 4: 'Rama', 5: 'Subrama', 6: 'Clase'}
        # plt.title(f'DENUE/SCIAN a nivel {cat[k]}')
        # plt.show()

        X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.20, random_state=0)

        # Regresión Logística
        print('# ', k, "LR")
        for c in [0.01]:  # [0.0001, 0.001, 0.01, 0.1, 0.5, 1.0, 2, 10.0, 100.0, 1000.0]:
            for mc in ['multinomial']:  # ['ovr', 'multinomial']:
                clf = LogisticRegression(C=c, multi_class=mc, max_iter=10000)
                pipe = make_pipeline(StandardScaler(), clf)
                scores = cross_val_score(pipe, X_train, y_train, cv=10, n_jobs=-1)
                if np.mean(scores) > max_lr:
                    max_lr = np.mean(scores)
                    print(f'# {k}, {clf}, {c}, {mc},{np.mean(scores)}, {np.median(scores)}, {np.std(scores)}')
                    scores = cross_val_score(pipe, X_test, y_test, cv=5, n_jobs=-1)
                    print(f'# {k}, {clf}, {c}, {mc},{np.mean(scores)}, {np.median(scores)}, {np.std(scores)}\n')
                    best_clf = clone(clf)
                    best_k = k
                    Xtrain, ytrain = X_train, y_train
                    Xpred, ypred = X, y
        best_pipe = make_pipeline(StandardScaler(), best_clf)
        best_pipe.fit(Xtrain, ytrain)
        scores = cross_val_score(best_pipe, Xpred, ypred, cv=5, n_jobs=-1)
        print(f"# Best {best_k}: {best_clf} CV5:{np.mean(scores)} +/- {np.std(scores)}")

        # Curva ROC
        print('unique:', np.unique(y))
        y_bin = label_binarize(y, classes=[0, 1, 2, 3, 4])
        n_classes = y_bin.shape[1]
        y_score = cross_val_predict(best_pipe, X, y, cv=10, method='predict_proba')
        fpr = dict()
        tpr = dict()
        roc_auc = dict()
        for i in range(n_classes):
            fpr[i], tpr[i], _ = roc_curve(y_bin[:, i], y_score[:, i])
            roc_auc[i] = auc(fpr[i], tpr[i])
        colors = cycle(['green', 'blue', 'yellow', 'orange', 'red'])
        for i, color in zip(range(n_classes), colors):
            plt.plot(fpr[i], tpr[i], color=color, lw=2,
                     label='Curva ROC de la clase: {0} (area = {1:0.4f})'
                           ''.format(ClasesRS[i], roc_auc[i]))
        plt.plot([0, 1], [0, 1], 'k--', lw=2)
        plt.xlim([-0.05, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('Tasa de Falsos Positivos')
        plt.ylabel('Tasa de Verdaderos Positivos')
        plt.title(f"Regresión Logística (LR)\nDENUE/SCIAN a nivel Rama")
        plt.legend(loc="lower right")
        plt.show()
        # Confusion Matrix
        plot_confusion_matrix(best_pipe, X, y,
                              display_labels=['Muy bajo', 'Bajo', 'Medio', 'Alto', 'Muy alto'],
                              cmap=plt.cm.Blues,
                              normalize='true')
        plt.title(f"Regresión Logística (LR)\nDENUE/SCIAN a nivel Rama")
        plt.show()


        # # SVM Lineal
        # print('# ', k, "SVM Linear")
        # for c in [0.01]:  # [.0001, 0.001, 0.01, 0.1, 0.5, 1.0, 2, 10.0, 100.0, 1000.0]:
        #     for kn in ['linear']:
        #         clf = SVC(kernel=kn, C=c)
        #         pipe = make_pipeline(StandardScaler(), clf)
        #         scores = cross_val_score(pipe, X_train, y_train, cv=10, n_jobs=-1)
        #         if np.mean(scores) > max_svc_l:
        #             max_svc_l = np.mean(scores)
        #             print(f'# {k}, {clf}, {c}, {kn},{np.mean(scores)}, {np.median(scores)}, {np.std(scores)}')
        #             scores = cross_val_score(pipe, X_test, y_test, cv=5, n_jobs=-1)
        #             print(f'# {k}, {clf}, {c}, {kn},{np.mean(scores)}, {np.median(scores)}, {np.std(scores)}\n')
        #             best_clf = clone(clf)
        #             best_k = k
        #             Xtrain, ytrain = X_train, y_train
        #             Xpred, ypred = X, y
        # best_pipe = make_pipeline(StandardScaler(), best_clf)
        # best_pipe.fit(Xtrain, ytrain)
        # scores = cross_val_score(best_pipe, Xpred, ypred, cv=5, n_jobs=-1)
        # print(f"# Best {best_k}: {best_clf} CV5:{np.mean(scores)} +/- {np.std(scores)}")

        # SVM rbf
        print('# ', k, "SVM RBF")
        for c in [10]:  # [.0001, 0.001, 0.01, 0.1, 0.5, 1.0, 2, 10.0, 100.0, 1000.0]:
            for g in [0.001]:  # [.0001, 0.001, 0.01, 0.1, 0.5, 1.0, 2, 10.0, 100.0, 1000.0]:
                for kn in ['rbf']:
                    clf = SVC(kernel=kn, C=c, gamma=g, probability=True)
                    pipe = make_pipeline(StandardScaler(), clf)
                    scores = cross_val_score(pipe, X_train, y_train, cv=10, n_jobs=-1)
                    if np.mean(scores) > max_svc_rbf:
                        max_svc_rbf = np.mean(scores)
                        print(f'# {k}, {clf}, {c}, {kn}, {np.mean(scores)}, {np.median(scores)}, {np.std(scores)}')
                        scores = cross_val_score(pipe, X_test, y_test, cv=5, n_jobs=-1)
                        print(f'# {k}, {clf}, {c}, {kn}, {np.mean(scores)}, {np.median(scores)}, {np.std(scores)}\n')
                        best_clf = clone(clf)
                        best_k = k
                        Xtrain, ytrain = X_train, y_train
                        Xpred, ypred = X, y
        best_pipe = make_pipeline(StandardScaler(), best_clf)
        best_pipe.fit(Xtrain, ytrain)
        scores = cross_val_score(best_pipe, Xpred, ypred, cv=5, n_jobs=-1)
        print(f"# Best {best_k}: {best_clf} CV5:{np.mean(scores)} +/- {np.std(scores)}")
        # Curva ROC
        print('unique:', np.unique(y))
        y_bin = label_binarize(y, classes=[0, 1, 2, 3, 4])
        n_classes = y_bin.shape[1]
        y_score = cross_val_predict(best_pipe, X, y, cv=10, method='predict_proba')
        fpr = dict()
        tpr = dict()
        roc_auc = dict()
        for i in range(n_classes):
            fpr[i], tpr[i], _ = roc_curve(y_bin[:, i], y_score[:, i])
            roc_auc[i] = auc(fpr[i], tpr[i])
        colors = cycle(['green', 'blue', 'yellow', 'orange', 'red'])
        for i, color in zip(range(n_classes), colors):
            plt.plot(fpr[i], tpr[i], color=color, lw=2,
                     label='Curva ROC de la clase: {0} (area = {1:0.4f})'
                           ''.format(ClasesRS[i], roc_auc[i]))
        plt.plot([0, 1], [0, 1], 'k--', lw=2)
        plt.xlim([-0.05, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('Tasa de Falsos Positivos')
        plt.ylabel('Tasa de Verdaderos Positivos')
        plt.title(f"Máquina de Soporte Vectorial (SVM)\nDENUE/SCIAN a nivel Rama")
        plt.legend(loc="lower right")
        plt.show()
        # Confusion Matrix
        plot_confusion_matrix(best_pipe, X, y,
                              display_labels=['Muy bajo', 'Bajo', 'Medio', 'Alto', 'Muy alto'],
                              cmap=plt.cm.Blues,
                              normalize='true')
        plt.title(f"Máquina de Soporte Vectorial (SVM)\nDENUE/SCIAN a nivel Rama")
        plt.show()

        # RF
        print('# ', k, "RF")
        for ne in [400]:  # [50, 100, 200, 400]:
            for md in [20]:  # [5, 10, 15, 20]:
                for cri in ['gini']:  # ['gini', 'entropy']:
                    for mf in ['sqrt']:  # ['sqrt', 'log2']:
                        clf = RandomForestClassifier(max_depth=md, n_estimators=ne, criterion=cri, max_features=mf,
                                                     random_state=0)
                        pipe = make_pipeline(StandardScaler(), clf)
                        scores = cross_val_score(pipe, X_train, y_train, cv=10, n_jobs=-1)
                        if np.mean(scores) > max_rf:
                            max_rf = np.mean(scores)
                            print(
                                f'# {k}, {clf}, {ne}, {md}, {cri}, {mf}, {np.mean(scores)}, {np.median(scores)}, {np.std(scores)}')
                            scores = cross_val_score(pipe, X_test, y_test, cv=5, n_jobs=-1)
                            print(
                                f'# {k}, {clf}, {ne}, {md}, {cri}, {mf}, {np.mean(scores)}, {np.median(scores)}, {np.std(scores)}\n')
                            best_clf = clone(clf)
                            best_k = k
                            Xtrain, ytrain = X_train, y_train
                            Xpred, ypred = X, y
        best_pipe = make_pipeline(StandardScaler(), best_clf)
        best_pipe.fit(Xtrain, ytrain)
        scores = cross_val_score(best_pipe, Xpred, ypred, cv=5, n_jobs=-1)
        print(f"# Best {best_k}: {best_clf} CV5:{np.mean(scores)} +/- {np.std(scores)}")
        # Curva ROC
        print('unique:', np.unique(y))
        y_bin = label_binarize(y, classes=[0, 1, 2, 3, 4])
        n_classes = y_bin.shape[1]
        y_score = cross_val_predict(best_pipe, X, y, cv=10, method='predict_proba')
        fpr = dict()
        tpr = dict()
        roc_auc = dict()
        for i in range(n_classes):
            fpr[i], tpr[i], _ = roc_curve(y_bin[:, i], y_score[:, i])
            roc_auc[i] = auc(fpr[i], tpr[i])
        colors = cycle(['green', 'blue', 'yellow', 'orange', 'red'])
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
        # Confusion Matrix
        plot_confusion_matrix(best_pipe, X, y,
                              display_labels=['Muy bajo', 'Bajo', 'Medio', 'Alto', 'Muy alto'],
                              cmap=plt.cm.Blues,
                              normalize='true')
        plt.title(f"Bosque Aleatorio (RF)\nDENUE/SCIAN a nivel Rama")
        plt.show()

        # MLP
        print('# ', k, "MLP")
        for hl in [(250,)]:  # [(50,), (100,), (150,), (200,), (250,)]:
            for af in ['relu']:  # ['identity', 'logistic', 'tanh', 'relu']:
                for alp in [10]:  # [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]:
                    for lrt in ['constant']:  # ['constant', 'invscaling', 'adaptive']:
                        clf = MLPClassifier(hidden_layer_sizes=hl, activation=af, alpha=alp, learning_rate=lrt,
                                            random_state=0, max_iter=2000)
                        pipe = make_pipeline(StandardScaler(), clf)
                        scores = cross_val_score(pipe, X_train, y_train, cv=10, n_jobs=-1)
                        if np.mean(scores) > max_mlp:
                            max_mlp = np.mean(scores)
                            print(
                                f'# {k}, {clf}, {hl}, {af}, {alp}, {lrt}, {np.mean(scores)}, {np.median(scores)}, {np.std(scores)}')
                            scores = cross_val_score(pipe, X_test, y_test, cv=5, n_jobs=-1)
                            print(
                                f'# {k}, {clf}, {hl}, {af}, {alp}, {lrt}, {np.mean(scores)}, {np.median(scores)}, {np.std(scores)}\n')
                            best_clf = clone(clf)
                            best_k = k
                            Xtrain, ytrain = X_train, y_train
                            Xpred, ypred = X, y
        best_pipe = make_pipeline(StandardScaler(), best_clf)
        best_pipe.fit(Xtrain, ytrain)
        scores = cross_val_score(best_pipe, Xpred, ypred, cv=5, n_jobs=-1)
        print(f"# Best {best_k}: {best_clf} CV5:{np.mean(scores)} +/- {np.std(scores)}")
        # Curva ROC
        print('unique:', np.unique(y))
        y_bin = label_binarize(y, classes=[0, 1, 2, 3, 4])
        n_classes = y_bin.shape[1]
        y_score = cross_val_predict(best_pipe, X, y, cv=10, method='predict_proba')
        fpr = dict()
        tpr = dict()
        roc_auc = dict()
        for i in range(n_classes):
            fpr[i], tpr[i], _ = roc_curve(y_bin[:, i], y_score[:, i])
            roc_auc[i] = auc(fpr[i], tpr[i])
        colors = cycle(['green', 'blue', 'yellow', 'orange', 'red'])
        for i, color in zip(range(n_classes), colors):
            plt.plot(fpr[i], tpr[i], color=color, lw=2,
                     label='Curva ROC de la clase: {0} (area = {1:0.4f})'
                           ''.format(ClasesRS[i], roc_auc[i]))
        plt.plot([0, 1], [0, 1], 'k--', lw=2)
        plt.xlim([-0.05, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('Tasa de Falsos Positivos')
        plt.ylabel('Tasa de Verdaderos Positivos')
        plt.title(f"Red Neuronal (MLP)\nDENUE/SCIAN a nivel Rama")
        plt.legend(loc="lower right")
        plt.show()
        # Confusion Matrix
        plot_confusion_matrix(best_pipe, X, y,
                              display_labels=['Muy bajo', 'Bajo', 'Medio', 'Alto', 'Muy alto'],
                              cmap=plt.cm.Blues,
                              normalize='true')
        plt.title(f"Red Neuronal (MLP)\nDENUE/SCIAN a nivel Rama")
        plt.show()


if __name__ == '__main__':
    main()
