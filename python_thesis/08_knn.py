from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.metrics import accuracy_score, plot_confusion_matrix
from sklearn.model_selection import train_test_split

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


def main():
    max_acc_model_1 = 0
    max_acc_model_2 = 0
    max_acc_model_3 = 0
    max_acc_model_4 = 0
    for folder in ["Count_Personal", "Count"]:
        for i in range(1, 7):
            for c in ["lgc00_15cl3"]:
                print(f'########### {i}:{c}:{folder} ##########')
                denue_wide = pd.read_csv(f"summary/{folder}/denue_wide_{i}.csv")
                rezago = pd.read_csv("rezago_social/rezago_social.csv")
                rezago_social = rezago[[c, "Key"]]  # , "LAT", "LON"]]#
                rezago_social.rename(columns={c: 'Rezago'}, inplace=True)

                df = pd.merge(rezago_social, denue_wide, on=['Key'])
                df.drop(['Key'], axis=1, inplace=True)

                print(df.shape)
                y = df['Rezago']
                X = df.drop(['Rezago'], axis=1)
                X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.20, random_state=1)

                # Modelling
                # KNN 0.64
                # SVC RBF 0.5426
                # LDA 0.59
                # QDA 0.57

                clf = LinearDiscriminantAnalysis()
                clf = clf.fit(X_train, y_train)
                predictions = clf.predict(X_test)
                if accuracy_score(y_test, predictions) > max_acc_model_1:
                    max_acc_model_1 = accuracy_score(y_test, predictions)
                    print("LDA:", accuracy_score(y_test, predictions))
                    plot_confusion_matrix(clf, X_test, y_test, normalize='true')
                    plt.title(f"LDA {i}:{c}:{folder}, {accuracy_score(y_test, predictions)}")
                    plt.show()

                clf = QuadraticDiscriminantAnalysis()
                clf = clf.fit(X_train, y_train)
                predictions = clf.predict(X_test)
                if accuracy_score(y_test, predictions) > max_acc_model_2:
                    max_acc_model_2 = accuracy_score(y_test, predictions)
                    print("QDA:", accuracy_score(y_test, predictions))
                    plot_confusion_matrix(clf, X_test, y_test, normalize='true')
                    plt.title(f"QDA {i}:{c}:{folder}, {accuracy_score(y_test, predictions)}")
                    plt.show()

                for sol in ['lbfgs']:
                    for pen in ['l2']:
                        for cr in np.arange(0.001, 10, .5):
                            clf = LogisticRegression(solver=sol, multi_class='auto', max_iter=10000, penalty=pen, C=cr)
                            clf = clf.fit(X_train, y_train)
                            predictions = clf.predict(X_test)
                            if accuracy_score(y_test, predictions) > max_acc_model_3:
                                max_acc_model_3 = accuracy_score(y_test, predictions)
                                print(f"LogisticRegression {sol},{pen},{cr}:", accuracy_score(y_test, predictions))
                                plot_confusion_matrix(clf, X_test, y_test, normalize='true')
                                plt.title(
                                    f"LR {sol} {pen},{cr} - {i}:{c}:{folder}, {accuracy_score(y_test, predictions)}")
                                plt.show()

                for sol in ['saga']:
                    for pen in ['l1']:
                        for cr in np.arange(0.001, 10, .5):
                            clf = LogisticRegression(solver=sol, multi_class='auto', max_iter=10000, penalty=pen, C=cr)
                            clf = clf.fit(X_train, y_train)
                            predictions = clf.predict(X_test)
                            if accuracy_score(y_test, predictions) > max_acc_model_4:
                                max_acc_model_4 = accuracy_score(y_test, predictions)
                                print(f"LogisticRegression {sol},{pen},{cr}:", accuracy_score(y_test, predictions))
                                plot_confusion_matrix(clf, X_test, y_test, normalize='true')
                                plt.title(
                                    f"LR {sol} {pen},{cr} - {i}:{c}:{folder}, {accuracy_score(y_test, predictions)}")
                                plt.show()


if __name__ == '__main__':
    main()
