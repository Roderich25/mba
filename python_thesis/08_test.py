import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn_extra.cluster import KMedoids
from sklearn.decomposition import PCA

for k in range(2, 3):
    for folder in ["Count"]:
        denue_wide = pd.read_csv(f"summary/{folder}/denue_wide_{k}.csv")
        rezago = pd.read_csv("rezago_social/rezago_social.csv")
        # rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL"]]
        rezago_social = rezago[["grs2015", "Key", "POB_TOTAL"]]
        df = pd.merge(rezago_social, denue_wide, on=['Key'])
        # OAXACA
        df = df[df['Key'].apply(lambda x: str(x).startswith("20") and len(str(x)) == 5)]
        # df.drop(['Key'], axis=1, inplace=True)
        # y = df['lgc00_15cl3']
        y = df['grs2015']
        X = df.iloc[:, 2:]
        # Conteo escalado por población/1000
        # X = X.div((df.POB_TOTAL / 1000), axis=0)

        X.to_csv(f'/Users/rodrigo/Desktop/Ejemplo_PAM/Oaxaca_{k}_{folder}.csv', index=False)

        X['Class'] = y
        X['Mun'] = df.Key
        X['pop'] = df.POB_TOTAL
        X.to_csv(f'/Users/rodrigo/Desktop/Ejemplo_PAM/Oax_.csv', index=False)

        # filter = X["Class"] != ''
        X = X[~X['Mun'].isin([20057, 20427, 20407, 20140])]

        print(X.columns)
        print(X['Class'].value_counts())
        print(X.shape)
        colors = {'Muy alto': 'red', 'Muy bajo': 'green', 'Medio': 'yellow', 'Alto': 'orange', 'Bajo': 'yellowgreen',
                  '': 'black'}

        for col in ['11', '21', '22', '23', '31', '32', '33', '43', '46', '48', '49', '51', '52', '53', '54', '55',
                    '56', '61', '62', '71', '72', '81', '93']:
            plt.scatter(X['pop'], X[col], c=X['Class'].map(colors))
            plt.title(col)
            plt.show()
            plt.close()
