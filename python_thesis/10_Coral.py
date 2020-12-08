import tensorflow as tf
import pandas as pd
import numpy as np
import coral_ordinal as coral
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from scipy import special

# Data
folder = 'Count'
for k in range(2, 7):
    denue_wide = pd.read_csv(f"summary/{folder}/denue_wide_{k}.csv")
    rezago = pd.read_csv("rezago_social/rezago_social.csv")
    rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON"]]
    df = pd.merge(rezago_social, denue_wide, on=['Key'])
    df.drop(['Key'], axis=1, inplace=True)
    y = df['lgc00_15cl3'] - 1
    X = df.iloc[:, 4:].div((df.POB_TOTAL / 1000), axis=0)
    X["LAT"] = rezago_social["LAT"]
    X["LON"] = rezago_social["LON"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, stratify=y, test_size=0.20, random_state=0)
    # print(X)
    # print(np.unique(y))

    sc = StandardScaler()  # ADD
    X_train_std = sc.fit_transform(X_train)
    X_test_std = sc.fit_transform(X_test)

    NUM_FEATURES = X.shape[1]
    NUM_CLASSES = len(np.unique(y))
    learning_rate = 0.05

    ####################################################################################
    for units in range(10, 150, 10):
        # Simple model
        print("\nSimple model:")
        simple_model = tf.keras.Sequential()
        simple_model.add(tf.keras.layers.Dense(
            units=units, activation="relu", input_shape=(NUM_FEATURES,)))
        simple_model.add(coral.CoralOrdinal(num_classes=NUM_CLASSES))
        simple_model.summary()
        simple_model.compile(loss=coral.OrdinalCrossEntropy(
            NUM_CLASSES), metrics=[coral.MeanAbsoluteErrorLabels])
        hist = simple_model.fit(
            X_train_std, y_train, validation_split=0.2, epochs=100, verbose=0)
        # print(hist.history)
        print("Evaluation")
        simple_model.evaluate(X_test_std, y_test)
        preds = simple_model.predict(X_test_std)
        probs = pd.DataFrame(coral.ordinal_softmax(preds).numpy())

        # print(probs.head(10))
        # print(y_test[:10].values)

        # Evaluate accuracy and mean absolute error
        labels_v1 = probs.idxmax(axis=1)
        print(f"# units:{units}, k:{k}")
        print("Accuracy of label version 1:", np.mean(labels_v1 == y_test.values))
        # Compare to logit-based cumulative probs
        cum_probs = pd.DataFrame(preds).apply(special.expit)
        # Calculate the labels using the style of Cao et al.
        labels_v2 = cum_probs.apply(lambda x: x > 0.5).sum(axis=1)
        print("Accuracy of label version 2:", np.mean(labels_v2 == y_test.values))
