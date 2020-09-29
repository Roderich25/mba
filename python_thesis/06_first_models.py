from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, plot_confusion_matrix
from sklearn.model_selection import train_test_split

import pandas as pd
from matplotlib import pyplot as plt


def main():
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
                X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.20, random_state=2012)

                # Modelling
                clf = AdaBoostClassifier(n_estimators=400)
                clf = clf.fit(X_train, y_train)
                predictions = clf.predict(X_test)
                print("ADA:", accuracy_score(y_test, predictions))
                plot_confusion_matrix(clf, X_test, y_test, normalize='true')
                plt.title(f"ADA {i}:{c}:{folder}, {accuracy_score(y_test, predictions)}")
                plt.show()

                clf = LogisticRegression(solver='lbfgs', multi_class='auto', max_iter=10000, penalty='l2')
                clf = clf.fit(X_train, y_train)
                predictions = clf.predict(X_test)
                print("LogisticRegression:", accuracy_score(y_test, predictions))
                plot_confusion_matrix(clf, X_test, y_test, normalize='true')
                plt.title(f"LR {i}:{c}:{folder}, {accuracy_score(y_test, predictions)}")
                plt.show()

                clf = MLPClassifier(solver='adam', activation='relu', hidden_layer_sizes=(250, 250, 250,),
                                    max_iter=2500)
                clf = clf.fit(X_train, y_train)
                predictions = clf.predict(X_test)
                print("NeuralNetwork:", accuracy_score(y_test, predictions))
                plot_confusion_matrix(clf, X_test, y_test, normalize='true')
                plt.title(f"NN {i}:{c}:{folder}, {accuracy_score(y_test, predictions)}")
                plt.show()

                clf = DecisionTreeClassifier()
                clf = clf.fit(X_train, y_train)
                predictions = clf.predict(X_test)
                print("DecisionTree:", accuracy_score(y_test, predictions))
                plot_confusion_matrix(clf, X_test, y_test, normalize='true')
                plt.title(f"DT {i}:{c}:{folder}, {accuracy_score(y_test, predictions)}")
                plt.show()

                clf = SVC(kernel='rbf')
                clf = clf.fit(X_train, y_train)
                predictions = clf.predict(X_test)
                print("SVC RBF:", accuracy_score(y_test, predictions))
                plot_confusion_matrix(clf, X_test, y_test, normalize='true')
                plt.title(f"SVC-RBF {i}:{c}:{folder}, {accuracy_score(y_test, predictions)}")
                plt.show()

                clf = SVC(kernel='linear')
                clf = clf.fit(X_train, y_train)
                predictions = clf.predict(X_test)
                print("SVC Linear:", accuracy_score(y_test, predictions))
                plot_confusion_matrix(clf, X_test, y_test, normalize='true')
                plt.title(f"SVC-L {i}:{c}:{folder}, {accuracy_score(y_test, predictions)}")
                plt.show()

                for k in range(5, 55, 5):
                    clf = KNeighborsClassifier(n_neighbors=k)
                    clf = clf.fit(X_train, y_train)
                    predictions = clf.predict(X_test)
                    print(f"Knn{k}:", accuracy_score(y_test, predictions))
                    plot_confusion_matrix(clf, X_test, y_test, normalize='true')
                    plt.title(f"KNN{k} {i}:{c}:{folder}, {accuracy_score(y_test, predictions)}")
                    plt.show()

                clf = RandomForestClassifier()
                clf = clf.fit(X_train, y_train)
                predictions = clf.predict(X_test)
                print("RandomForest:", accuracy_score(y_test, predictions))
                plot_confusion_matrix(clf, X_test, y_test, normalize='true')
                plt.title(f"RF {i}:{c}:{folder}, {accuracy_score(y_test, predictions)}")
                plt.show()


if __name__ == '__main__':
    main()

for sol in ['lbgfgs', 'newton-cg', 'sag', 'saga', 'none']:
    for cr in np.arange(0.1, 4, .1):
        if accuracy_score(y_test, predictions) > max_acc_model_1:
            max_acc_model_1 = accuracy_score(y_test, predictions)
            clf = LogisticRegression(solver=sol, multi_class='auto', max_iter=10000, penalty='l2',
                                     C=cr)
            clf = clf.fit(X_train, y_train)
            predictions = clf.predict(X_test)
            print(f"LogisticRegression {sol},{cr}:", accuracy_score(y_test, predictions))
            plot_confusion_matrix(clf, X_test, y_test, normalize='true')
            plt.title(f"LR {sol},{cr} - {i}:{c}:{folder}, {accuracy_score(y_test, predictions)}")
            plt.show()