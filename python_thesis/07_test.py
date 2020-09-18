from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score
import pandas as pd
import numpy as np

for folder in ["Count_Personal", "Count"]:
    for i in range(4, 5):
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
            # Modelling
            for rs in [777]:
                for hidden_layers in [(50,), (100,), (150,), (200,), (250,)]:
                    for max_iter in [2000, 2500, 3000]:
                        for solver in ["lbfgs", "adam"]:
                            for activation in ["logistic", "tanh", "relu"]:
                                clf = MLPClassifier(solver=solver, activation=activation, max_iter=max_iter,
                                                    hidden_layer_sizes=hidden_layers, random_state=rs)
                                print(
                                    f"NN{i}:{c}:{folder}\tsolve:{solver},af:{activation},max_iter_{max_iter},hl:{hidden_layers}")
                                scores = cross_val_score(clf, X, y, cv=10)
                                print(np.min(scores), np.mean(scores), np.median(scores), np.max(scores))

# NN3:lgc00_15cl3:Count_Personal	solve:adam,af:logistic,max_iter_1500,hl:(50,)
# 0.6341463414634146 0.7037232453957192 0.7107848017255682 0.7551020408163265

# NN3:lgc00_15cl3:Count_Personal	solve:adam,af:logistic,max_iter_2500,hl:(75,)
# 0.6422764227642277 0.7000464576074332 0.6924589347934296 0.7642276422764228

# NN3:lgc00_15cl3:Count_Personal	solve:adam,af:relu,max_iter_2000,hl:(150,)
# 0.6504065040650406 0.6910900945744152 0.7 0.7276422764227642
