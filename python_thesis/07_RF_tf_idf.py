from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import label_binarize
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from itertools import cycle


# 5,Count,500,1000,20,entropy,sqrt


def main():
    for k in [5]:
        for folder in ["Count"]:
            for t in [500]:
                print(f'# {k}, {folder}, {t}')
                denue_wide = pd.read_csv(f"summary/{folder}/denue_wide_{k}.csv")
                rezago = pd.read_csv("rezago_social/rezago_social.csv")
                rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL"]]
                df = pd.merge(rezago_social, denue_wide, on=['Key'])
                df.drop(['Key'], axis=1, inplace=True)
                print(f'Before {t}:', df.shape)
                df.drop([col for col, val in df.sum().iteritems() if val <= t], axis=1, inplace=True)
                print(f'After {t}:', df.shape)
                y = df['lgc00_15cl3']
                X = df.iloc[:, 1:].div((df.POB_TOTAL / 1000), axis=0)
                X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.10, random_state=0)
                for ne in [1000]:
                    for md in [20]:
                        for cri in ['entropy']:
                            for mf in ['sqrt']:
                                clf = RandomForestClassifier(max_depth=md, n_estimators=ne, criterion=cri,
                                                             max_features=mf, random_state=0)
                                pipeline = make_pipeline(TfidfTransformer(), clf)


                                scores = cross_val_score(pipeline, X_train, y_train, cv=10, n_jobs=-1)
                                print(
                                    f"{clf}, {folder}, {t}, {k}, {ne}, {md}, {cri}, {mf}, cv='10', mean={np.mean(scores)}, median={np.median(scores)}, std={np.std(scores)}")
                                scores = cross_val_score(pipeline, X, y, cv=5, n_jobs=-1)
                                print(
                                    f"{clf}, {folder}, {t}, {k}, {ne}, {md}, {cri}, {mf}, cv='5', mean={np.mean(scores)}, median={np.median(scores)}, std={np.std(scores)}")
                                

                                # # Curva ROC
                                # y_bin = label_binarize(y, classes=[1, 2, 3])
                                # n_classes = y_bin.shape[1]
                                # y_score = cross_val_predict(pipeline, X, y, cv=10, method='predict_proba')
                                # fpr = dict()
                                # tpr = dict()
                                # roc_auc = dict()
                                # for i in range(n_classes):
                                #     fpr[i], tpr[i], _ = roc_curve(y_bin[:, i], y_score[:, i])
                                #     roc_auc[i] = auc(fpr[i], tpr[i])
                                # colors = cycle(['blue', 'red', 'green'])
                                # for i, color in zip(range(n_classes), colors):
                                #     plt.plot(fpr[i], tpr[i], color=color, lw=2,
                                #              label='ROC curve of class {0} (area = {1:0.6f})'
                                #                    ''.format(i+1, roc_auc[i]))
                                # plt.plot([0, 1], [0, 1], 'k--', lw=2)
                                # plt.xlim([-0.05, 1.0])
                                # plt.ylim([0.0, 1.05])
                                # plt.xlabel('Tasa de Falsos Positivos')
                                # plt.ylabel('Tasa de Verdaderos Positivos')
                                # plt.title(f"{clf}\n{folder}, {k}, {t}, {ne}, {md}, {cri}, {mf}")
                                # plt.legend(loc="lower right")
                                # plt.show()
                                # plt.close()


if __name__ == '__main__':
    main()
