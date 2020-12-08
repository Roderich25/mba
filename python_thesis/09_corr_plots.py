import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

folder = 'Count'
for k in [2, 6]:
    denue_wide = pd.read_csv(f"summary/{folder}/denue_wide_{k}.csv")
    rezago = pd.read_csv("rezago_social/rezago_social.csv")
    rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON"]]
    df = pd.merge(rezago_social, denue_wide, on=['Key'])
    df.drop(['Key'], axis=1, inplace=True)
    y = df['lgc00_15cl3'] - 1
    X = df.iloc[:, 5:].div((df.POB_TOTAL / 1000), axis=0)
    print(X.shape)
    X["LAT"] = rezago_social["LAT"]
    X["LON"] = rezago_social["LON"]
    # X["ALT"] = rezago_social["ALT"]
    # X["POB_TOTAL"] = rezago_social["POB_TOTAL"]
    print(X)
    print(X.corr())
    plt.matshow(X.corr())
    plt.colorbar()
    cat = {2: 'Sector', 3: 'Subsector', 4: 'Rama', 5: 'Subrama', 6: 'Clase'}
    plt.title(f'DENUE/SCIAN 2015 a nivel {cat[k]}')
    plt.show()
