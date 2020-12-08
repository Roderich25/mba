from itertools import cycle

from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, label_binarize
from sklearn.model_selection import GridSearchCV, train_test_split, cross_val_score, cross_val_predict
from sklearn.metrics import accuracy_score, plot_confusion_matrix, roc_curve, auc, f1_score
from sklearn.svm import SVC
import pandas as pd
import numpy as np
from sklearn.base import clone
from matplotlib import pyplot as plt

from sklearn.base import BaseEstimator
import numpy as np


class OrdinalClassifier():

    def __init__(self, clf):
        self.clf = clf
        self.clfs = {}
        self._estimator_type = 'classifier'

    def fit(self, X, y):
        self.unique_class = np.sort(np.unique(y))
        self.classes_ = list(range(len(self.unique_class)))
        if self.unique_class.shape[0] > 2:
            for i in range(self.unique_class.shape[0] - 1):
                # for each k - 1 ordinal value we fit a binary classification problem
                binary_y = (y > self.unique_class[i]).astype(np.uint8)
                clf = clone(self.clf)
                clf.fit(X, binary_y)
                self.clfs[i] = clf

    def predict_proba(self, X):
        clfs_predict = {k: self.clfs[k].predict_proba(X) for k in self.clfs}
        predicted = []
        for i, y in enumerate(self.unique_class):
            if i == 0:
                # V1 = 1 - Pr(y > V1)
                predicted.append(1 - clfs_predict[y][:, 1])
            elif y in clfs_predict:
                # Vi = Pr(y > Vi-1) - Pr(y > Vi)
                predicted.append(clfs_predict[y - 1][:, 1] - clfs_predict[y][:, 1])
            else:
                # Vk = Pr(y > Vk-1)
                predicted.append(clfs_predict[y - 1][:, 1])
        return np.vstack(predicted).T

    def predict(self, X):
        return np.argmax(self.predict_proba(X), axis=1)


class OrdClass(BaseEstimator):
    """
    Helper class that solves ordinal classification (classes that have an order to them eg cold,warm,hot)
    """

    def __init__(self, classifier=None, clf_args=None):
        """
        y needs to be a number that start from 0 and increments by 1
        classifier object needs to be able to return a probability
        """
        self.classifier = classifier
        self.clfs = []
        self.clf_args = clf_args
        self.final_prob = None
        self._estimator_type = 'classifier'

    def fit(self, X, y, **fit):
        self.X = X
        self.y = y
        import copy
        no_of_classifiers = np.max(self.y)  # since y starts from 0
        self.classes_ = list(range(no_of_classifiers + 1))
        if isinstance(self.clf_args, list):
            # for pipelines
            c = self.classifier(self.clf_args)
        elif isinstance(self.clf_args, dict):
            # for normal estimators
            c = self.classifier(**self.clf_args)
        else:
            c = self.classifier

        for i in range(no_of_classifiers):
            # make a copy of y because we want to change the values of y
            copy_y = np.copy(self.y)
            # make a binary classification here
            copy_y[copy_y <= i] = 0
            copy_y[copy_y > i] = 1
            classifier = copy.deepcopy(c)
            classifier.fit(self.X, copy_y, **fit)
            self.clfs.append(classifier)
        return self

    def predict_proba(self, test):
        prob_list = []
        final_prob = []
        length = len(self.clfs)
        for clf in self.clfs:
            prob_list.append(clf.predict_proba(test)[:, 1])
        for i in range(length + 1):
            if i == 0:
                final_prob.append(1 - prob_list[i])
            elif i == length:
                final_prob.append(prob_list[i - 1])
            else:
                final_prob.append(prob_list[i - 1] - prob_list[i])
        answer = np.array(final_prob).transpose()
        self.final_prob = answer
        return answer

    def predict(self, test):
        self.predict_proba(test)
        return np.argmax(self.final_prob, axis=1)

    def score(self, X, y, sample_weight=None):
        from sklearn.metrics import accuracy_score
        return accuracy_score(y, self.predict(X), sample_weight=sample_weight)


def main_ord():
    for folder in ["Count", "Count_Personal"]:
        for k in range(2, 6):
            for C in [0.0001, 0.001, 0.01, 0.1, 0.5, 1.0, 2.0, 10.0, 100.0, 1000.0]:
                denue_wide = pd.read_csv(f"summary/{folder}/denue_wide_{k}.csv")
                rezago = pd.read_csv("rezago_social/rezago_social.csv")
                rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL"]]
                df = pd.merge(rezago_social, denue_wide, on=['Key'])
                df.drop(['Key'], axis=1, inplace=True)
                y = df['lgc00_15cl3'] - 1
                X = df.iloc[:, 2:].div((df.POB_TOTAL / 1000), axis=0)
                X['pop'] = df.POB_TOTAL
                clf = LogisticRegression(solver='lbfgs', multi_class='multinomial', penalty='l2', C=C, max_iter=10000)
                # pipeline = make_pipeline(StandardScaler(), OrdinalClassifier(clf))
                pipeline = make_pipeline(StandardScaler(), OrdClass(classifier=clf))

                X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.10, random_state=0)
                pipeline.fit(X_train, y_train)
                y_pred = pipeline.predict(X_test)
                # print('Accuracy:', accuracy_score(y_test, y_pred))

                # Crossvalidation
                scores = cross_val_score(pipeline, X_train, y_train, cv=10, n_jobs=-1)
                if np.mean(scores) > 0.72:
                    print(
                        f"{clf}, {folder}, {k}, cv=10, mean={np.mean(scores)}, median={np.median(scores)}, std={np.std(scores)}")
                    # Curva ROC
                    y_bin = label_binarize(y_train, classes=[0, 1, 2])
                    n_classes = y_bin.shape[1]
                    y_score = cross_val_predict(pipeline, X_train, y_train, cv=10, method='predict_proba')
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
                    plt.title(f"{clf}\n{folder}, {k}")
                    plt.legend(loc="lower right")
                    plt.show()

                    # Confusion matrix
                    print('F1 score:', f1_score(y_test, y_pred, average='weighted'))
                    plot_confusion_matrix(pipeline, X_test, y_test, normalize='true')
                    plt.title(f"{clf})\n{folder}, {k}, accuracy: {accuracy_score(y_test, y_pred)}")
                    plt.show()


# Count,3,0.5

def main():
    for folder in ["Count", "Count_Personal"]:
        for k in range(2, 6):
            denue_wide = pd.read_csv(f"summary/{folder}/denue_wide_{k}.csv")
            rezago = pd.read_csv("rezago_social/rezago_social.csv")
            rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL"]]
            df = pd.merge(rezago_social, denue_wide, on=['Key'])
            df.drop(['Key'], axis=1, inplace=True)
            y = df['lgc00_15cl3']
            # df.POB_TOTAL = df.POB_TOTAL / 1000
            X = df.iloc[:, 2:].div((df.POB_TOTAL / 1000), axis=0)
            X['pop'] = df.POB_TOTAL
            # print(X.head())
            print(X.shape)
            X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.10, random_state=1)
            pipe_svc = make_pipeline(StandardScaler(), SVC(random_state=1))
            param_range = [0.0001, 0.001, 0.01, 0.1, 0.5, 1.0, 2, 10.0, 100.0, 1000.0]
            param_grid = [{'svc__C': param_range, 'svc__kernel': ['linear']},
                          {'svc__C': param_range, 'svc__gamma': param_range, 'svc__kernel': ['rbf']}]

            print(f"SVC({folder},{k})")
            gs = GridSearchCV(estimator=pipe_svc, param_grid=param_grid, scoring='accuracy', cv=10, n_jobs=-1)
            gs = gs.fit(X_train, y_train)
            print(gs.best_score_)
            print(gs.best_params_)
            # Best
            clf = gs.best_estimator_
            clf.fit(X_train, y_train)
            print(folder, k, 'Test accuracy: %.3f' % clf.score(X_test, y_test))


if __name__ == '__main__':
    main()
