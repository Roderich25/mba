import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn_extra.cluster import KMedoids
from sklearn.decomposition import PCA
from collections import defaultdict

for k in range(3, 4):
    for folder in ["Count"]:
        denue_wide = pd.read_csv(f"summary/{folder}/denue_wide_{k}.csv")
        rezago = pd.read_csv("rezago_social/rezago_social.csv")
        rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL"]]
        df = pd.merge(rezago_social, denue_wide, on=['Key'])
        # OAXACA
        # df = df[df['Key'].apply(lambda x: str(x).startswith("20") and len(str(x)) == 5)]
        df.drop(['Key'], axis=1, inplace=True)
        y = df['lgc00_15cl3']
        X = df.iloc[:, 2:]
        # Conteo escalado por población/1000
        X = X.div((df.POB_TOTAL / 1000), axis=0)
        print(X.shape)
        # X.to_csv(f'/Users/rodrigo/Desktop/Ejemplo_PAM/Oaxaca_{k}_{folder}.csv', index=False)

        sc = StandardScaler()
        X_std = sc.fit_transform(X)
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(X_std)

        all = ['euclidean', 'l2', 'l1', 'manhattan', 'cityblock', 'braycurtis', 'canberra', 'chebyshev', 'correlation',
               'cosine', 'minkowski', 'sqeuclidean', 'nan_euclidean']
        for distance in ['l1', 'manhattan', 'cityblock']:
            # PCA
            print("PCA shape:", X_pca.shape, distance)
            colors = {1: 'green', 2: 'yellow', 3: 'red'}
            plt.subplot(1, 2, 1)
            plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y.map(colors))

            # KMedoids
            kmedoids = KMedoids(n_clusters=3, metric=distance, random_state=0).fit(X_std)
            plt.subplot(1, 2, 2)

            colors2 = {0: 'blue', 1: 'brown', 2: 'purple'}
            plt.scatter(X_pca[:, 0], X_pca[:, 1], c=list(map(lambda x: colors2[x], kmedoids.labels_)))

            d = defaultdict(list)
            for key, val in zip(y, kmedoids.labels_):
                d[key].append(val)

            np.set_printoptions(precision=2)
            f1 = np.unique(d[1], return_counts=True)[1]
            f2 = np.unique(d[2], return_counts=True)[1]
            f3 = np.unique(d[3], return_counts=True)[1]

            plt.suptitle(f'{k} {folder}, K-medois(k:3, dist:{distance})\nblue:{f1/ np.sum(f1)}\nbrown:{f2/ np.sum(f2)}\npurple:{f3/ np.sum(f3)}')
            plt.show()
            plt.close()
