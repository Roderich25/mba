from itertools import cycle
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc, plot_confusion_matrix, f1_score
from sklearn.model_selection import cross_val_score, cross_val_predict, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, label_binarize
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from matplotlib import pyplot as plt


def main():
    for folder in ["Count", "Count_Personal"]:
        print(folder)
        for k in range(2, 7):
            for c in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.5, 3]:
                denue_wide = pd.read_csv(f"summary/{folder}/denue_wide_{k}.csv")
                rezago = pd.read_csv("rezago_social/rezago_social.csv")

                # rezago_social = rezago[["lgc00_15cl4_2", "Key", "POB_TOTAL"]]
                rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL"]]

                df = pd.merge(rezago_social, denue_wide, on=['Key'])
                df.drop(['Key'], axis=1, inplace=True)
                # y = df['lgc00_15cl4_2']
                y = df['lgc00_15cl3']
                df.POB_TOTAL = df.POB_TOTAL / 1000
                X = df.iloc[:, 2:].div(df.POB_TOTAL, axis=0)
                print(X.shape)

                sc = StandardScaler()
                X_std = sc.fit_transform(X)
                # pca = PCA(n_components=None)
                lda = LinearDiscriminantAnalysis(n_components=None)
                lda.fit_transform(X_std, y)
                expvar = np.cumsum(lda.explained_variance_ratio_)
                comp = sum([1 if q <= 0.95 else 0 for q in expvar])
                print(comp, expvar[comp - 1])
                if comp == 1:
                    comp += 1

                clf = LogisticRegression(solver='lbfgs', multi_class='multinomial', penalty='l2', C=c,
                                         max_iter=10000, random_state=0)
                # pipeline = Pipeline([('transformer', StandardScaler()), ('pca', PCA(n_components=comp)), ('estimator', clf)])
                pipeline = Pipeline(
                    [('transformer', StandardScaler()), ('pca', LinearDiscriminantAnalysis(n_components=comp)),
                     ('estimator', clf)])

                for cv in [10]:
                    scores = cross_val_score(pipeline, X, y, cv=cv, n_jobs=-1)
                if np.mean(scores) > 0.7:
                    print(
                        f"LR({folder},{k},{c}), cv={cv}, min={np.min(scores)},, mean={np.mean(scores)},median={np.median(scores)}, max={np.max(scores)}, std={np.std(scores)}")

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
                                       ''.format(i, roc_auc[i]))
                    plt.plot([0, 1], [0, 1], 'k--', lw=2)
                    plt.xlim([-0.05, 1.0])
                    plt.ylim([0.0, 1.05])
                    plt.xlabel('Tasa de Falsos Positivos')
                    plt.ylabel('Tasa de Verdaderos Positivos')
                    plt.title(clf)
                    plt.legend(loc="lower right")
                    plt.show()

                    # Confusion matrix
                    sc = StandardScaler()
                    print(clf)
                    for rs in [0]:
                        X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.10,
                                                                            random_state=rs)
                        X_train_std = sc.fit_transform(X_train)
                        X_test_std = sc.transform(X_test)
                        print('train:', len(y_train), 'test:', len(y_test))
                        clf.fit(X_train_std, y_train)
                        print('Accuracy:', clf.score(X_test_std, y_test))
                        predictions = clf.predict(X_test_std)
                        print('F1 score:', f1_score(y_test, predictions, average='weighted'))
                        plot_confusion_matrix(clf, X_test_std, y_test, normalize='true')
                        plt.title(f"Accuracy: {clf.score(X_test_std, y_test)}\nRandom state:{rs}")
                        plt.show()


if __name__ == '__main__':
    main()
