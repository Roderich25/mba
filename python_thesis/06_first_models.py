from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, plot_confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
from matplotlib import pyplot as plt

for folder in ["Count_Personal","Count"]:
    for i in range(2, 7):
        for c in ["lgc00_15cl3", "lgc00_15cl4_2"]:
            print(f'########### {i}:{c}:{folder} ##########')
            denue_wide = pd.read_csv(f"summary/{folder}/denue_wide_{i}.csv")
            rezago = pd.read_csv("rezago_social/rezago_social.csv")
            rezago_social = rezago[[c, "Key"]]  # , "LAT", "LON"]]#
            rezago_social.rename(columns={c: 'Rezago'}, inplace=True)

            df = pd.merge(rezago_social, denue_wide, on=['Key'])
            df.drop(['Key'], axis=1, inplace=True)
            #print(df.head())

            print(df.shape)
            #print(df['Rezago'].value_counts())

            y = df['Rezago']
            X = df.drop(['Rezago'], axis=1)
            scaler = StandardScaler()
            X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.20)

            X_train = scaler.fit_transform(X_train)
            X_test = scaler.fit_transform(X_test)

            # Modelling
            clf = AdaBoostClassifier()
            clf = clf.fit(X_train, y_train)
            predictions = clf.predict(X_test)
            print("ADA:", accuracy_score(y_test, predictions))
            plot_confusion_matrix(clf, X_test, y_test, normalize='true')
            plt.title(f"ADA {i}:{c}:{folder}, {accuracy_score(y_test, predictions)}")
            plt.show()

            clf = LogisticRegression(solver='liblinear', multi_class='auto', max_iter=10000)
            clf = clf.fit(X_train, y_train)
            predictions = clf.predict(X_test)
            print("LogisticRegression:", accuracy_score(y_test, predictions))
            plot_confusion_matrix(clf, X_test, y_test, normalize='true')
            plt.title(f"LR {i}:{c}:{folder}, {accuracy_score(y_test, predictions)}")
            plt.show()

            clf = MLPClassifier(solver='lbfgs', activation='tanh')
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

            clf = KNeighborsClassifier(n_neighbors=3)
            clf = clf.fit(X_train, y_train)
            predictions = clf.predict(X_test)
            print("Knn:", accuracy_score(y_test, predictions))
            plot_confusion_matrix(clf, X_test, y_test, normalize='true')
            plt.title(f"KNN {i}:{c}:{folder}, {accuracy_score(y_test, predictions)}")
            plt.show()

            clf = RandomForestClassifier(n_estimators=10000, max_depth=10)
            clf = clf.fit(X_train, y_train)
            predictions = clf.predict(X_test)
            print("RandomForest:", accuracy_score(y_test, predictions))
            plot_confusion_matrix(clf, X_test, y_test, normalize='true')
            plt.title(f"RF {i}:{c}:{folder}, {accuracy_score(y_test, predictions)}")
            plt.show()
