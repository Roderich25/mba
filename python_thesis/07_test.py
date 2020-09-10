from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, plot_confusion_matrix
from sklearn.model_selection import train_test_split
import pandas as pd
from matplotlib import pyplot as plt

for folder in ["Count_Personal", "Count"]:
    for i in range(4, 6):
        for c in ["lgc00_15cl3"]:
            print(f'########### {i}:{c}:{folder} ##########')
            denue_wide = pd.read_csv(f"summary/{folder}/denue_wide_{i}.csv")
            rezago = pd.read_csv("rezago_social/rezago_social.csv")
            rezago_social = rezago[[c, "Key"]]  # , "LAT", "LON"]]#
            rezago_social.rename(columns={c: 'Rezago'}, inplace=True)

            df = pd.merge(rezago_social, denue_wide, on=['Key'])
            df.drop(['Key'], axis=1, inplace=True)
            # print(df.head())

            print(df.shape)
            # print(df['Rezago'].value_counts())

            y = df['Rezago']
            X = df.drop(['Rezago'], axis=1)
            X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.20)

            # Modelling

            clf = LogisticRegression(solver='liblinear', multi_class='auto', max_iter=10000)
            clf = clf.fit(X_train, y_train)
            predictions = clf.predict(X_test)
            print("LogisticRegression:", accuracy_score(y_test, predictions))
            plot_confusion_matrix(clf, X_test, y_test, normalize='true')
            plt.title(f"LR {i}:{c}:{folder}, {accuracy_score(y_test, predictions)}")
            print(clf.score(X_test, y_test))
            plt.show()

            clf = MLPClassifier(solver='lbfgs', activation='tanh')
            clf = clf.fit(X_train, y_train)
            predictions = clf.predict(X_test)
            print("NeuralNetwork:", accuracy_score(y_test, predictions))
            plot_confusion_matrix(clf, X_test, y_test, normalize='true')
            plt.title(f"NN {i}:{c}:{folder}, {accuracy_score(y_test, predictions)}")
            print(clf.score(X_test, y_test))
            plt.show()
