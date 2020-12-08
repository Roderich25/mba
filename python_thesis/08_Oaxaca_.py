from itertools import cycle
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import label_binarize, StandardScaler
import matplotlib.pyplot as plt
from sklearn.svm import SVC


def curva_roc(clf, pipeline, X, y):
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
                       ''.format(i + 1, roc_auc[i]))
    plt.plot([0, 1], [0, 1], 'k--', lw=2)
    plt.xlim([-0.05, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('Tasa de Falsos Positivos')
    plt.ylabel('Tasa de Verdaderos Positivos')
    plt.title(f"{clf}")
    plt.legend(loc="lower right")
    plt.show()


def main_hgbc():
    # FOLDER & CODIGO
    denue_wide = pd.read_csv(f"summary/Count_Personal/denue_wide_3.csv")
    rezago = pd.read_csv("rezago_social/rezago_social.csv")
    rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL"]]
    df = pd.merge(rezago_social, denue_wide, on=['Key'])
    # Oaxaca
    df = df[df['Key'].apply(lambda x: str(x).startswith("20") and len(str(x)) == 5)]
    df.drop(['Key'], axis=1, inplace=True)
    y = df["lgc00_15cl3"]
    X = df.iloc[:, 2:]
    # Conteo escalado por población/1000
    X = X.div((df.POB_TOTAL / 1000), axis=0)
    # Ajuste modelo
    clf = HistGradientBoostingClassifier(l2_regularization=100)
    pipeline = make_pipeline(clf)
    scores = cross_val_score(clf, X, y, cv=5, n_jobs=-1)
    print(
        f"# {clf}\tmean:{round(np.mean(scores), 4)}, median:{round(np.median(scores), 4)}, std:{round(np.std(scores), 4)}")
    curva_roc(clf, pipeline, X, y)


def main_lr():
    # FOLDER & CODIGO
    denue_wide = pd.read_csv(f"summary/Count_Personal/denue_wide_4.csv")
    rezago = pd.read_csv("rezago_social/rezago_social.csv")
    rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL"]]
    df = pd.merge(rezago_social, denue_wide, on=['Key'])
    # Oaxaca
    df = df[df['Key'].apply(lambda x: str(x).startswith("20") and len(str(x)) == 5)]
    df.drop(['Key'], axis=1, inplace=True)
    y = df["lgc00_15cl3"]
    X = df.iloc[:, 2:]
    # Conteo escalado por población/1000
    X = X.div((df.POB_TOTAL / 1000), axis=0)
    # Ajuste modelo
    clf = LogisticRegression(solver='lbfgs', multi_class='multinomial', penalty='l2', C=0.1,
                             max_iter=10000)
    pipeline = make_pipeline(clf)
    scores = cross_val_score(pipeline, X, y, cv=5, n_jobs=-1)
    print(
        f"# {clf}\tmean:{round(np.mean(scores), 4)}, median:{round(np.median(scores), 4)}, std:{round(np.std(scores), 4)}")
    curva_roc(clf, pipeline, X, y)


def main_svc():
    # FOLDER & CODIGO
    denue_wide = pd.read_csv(f"summary/Count/denue_wide_3.csv")
    rezago = pd.read_csv("rezago_social/rezago_social.csv")
    rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL"]]
    df = pd.merge(rezago_social, denue_wide, on=['Key'])
    # Oaxaca
    df = df[df['Key'].apply(lambda x: str(x).startswith("20") and len(str(x)) == 5)]
    df.drop(['Key'], axis=1, inplace=True)
    y = df["lgc00_15cl3"]
    X = df.iloc[:, 2:]
    # Conteo escalado por población/1000
    X = X.div((df.POB_TOTAL / 1000), axis=0)
    # Ajuste modelo
    clf = SVC(kernel='rbf', gamma=0.01, C=1, probability=True)
    pipeline = make_pipeline(StandardScaler(), clf)
    scores = cross_val_score(pipeline, X, y, cv=5, n_jobs=-1)
    print(
        f"# {clf}\tmean:{round(np.mean(scores), 4)}, median:{round(np.median(scores), 4)}, std:{round(np.std(scores), 4)}")
    curva_roc(clf, pipeline, X, y)
    # Ajuste modelo
    clf = SVC(kernel='rbf', gamma=0.01, C=1, probability=True)
    pipeline = make_pipeline(clf)
    scores = cross_val_score(pipeline, X, y, cv=5, n_jobs=-1)
    print(
        f"# {clf}\tmean:{round(np.mean(scores), 4)}, median:{round(np.median(scores), 4)}, std:{round(np.std(scores), 4)}")
    curva_roc(clf, pipeline, X, y)

def main_rf():
    # FOLDER & CODIGO
    denue_wide = pd.read_csv(f"summary/Count_Personal/denue_wide_4.csv")
    rezago = pd.read_csv("rezago_social/rezago_social.csv")
    rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL"]]
    df = pd.merge(rezago_social, denue_wide, on=['Key'])
    # Oaxaca
    df = df[df['Key'].apply(lambda x: str(x).startswith("20") and len(str(x)) == 5)]
    df.drop(['Key'], axis=1, inplace=True)
    y = df["lgc00_15cl3"]
    X = df.iloc[:, 2:]
    # Conteo escalado por población/1000
    X = X.div((df.POB_TOTAL / 1000), axis=0)
    # Ajuste modelo
    clf = RandomForestClassifier(n_estimators=500, criterion='gini', max_features='sqrt', random_state=0)
    pipeline = make_pipeline(clf)
    scores = cross_val_score(pipeline, X, y, cv=5, n_jobs=-1)
    print(
        f"# {clf}\tmean:{round(np.mean(scores), 4)}, median:{round(np.median(scores), 4)}, std:{round(np.std(scores), 4)}")
    curva_roc(clf, pipeline, X, y)


if __name__ == '__main__':
    main_rf()
    main_svc()
    main_lr()
    main_hgbc()
