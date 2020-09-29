from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, plot_confusion_matrix
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

for folder in ["Count_Personal"]:
    for i in [5]:
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
            for hidden_layers in [(250, 250, 250,)]:
                for rs in [555, 666, 777]:
                    for max_iter in [3000]:
                        for solver in ["adam"]:
                            for activation in ["relu"]:
                                clf = MLPClassifier(solver=solver, activation=activation, max_iter=max_iter,
                                                    hidden_layer_sizes=hidden_layers, random_state=rs)
                                print(
                                    f"NN{i}:{c}:{folder}\tsolve:{solver}, af:{activation}, max_iter_{max_iter}, hl:{hidden_layers}, rs:{rs}")
                                scores = cross_val_score(clf, X, y, cv=10)
                                print(np.min(scores), np.mean(scores), np.median(scores), np.max(scores))
                                ###
                                X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.20, random_state=rs)
                                clf = MLPClassifier(solver=solver, activation=activation, max_iter=max_iter,
                                                    hidden_layer_sizes=hidden_layers, random_state=rs)
                                clf.fit(X_train, y_train)
                                plot_confusion_matrix(clf, X_test, y_test, normalize='true')
                                plt.title(f"NN{i}:{c}:{folder}\tsolve:{solver}, af:{activation}, max_iter_{max_iter}, hl:{hidden_layers}, rs:{rs}\nAccuracy{clf.score(X_test,y_test)}")
                                plt.show()

# 777
# NN3:lgc00_15cl3:Count_Personal	solve:adam,af:logistic,max_iter_1500,hl:(50,)
# 0.6341463414634146 0.7037232453957192 0.7107848017255682 0.7551020408163265

# NN3:lgc00_15cl3:Count_Personal	solve:adam,af:logistic,max_iter_2500,hl:(75,)
# 0.6422764227642277 0.7000464576074332 0.6924589347934296 0.7642276422764228

# NN3:lgc00_15cl3:Count_Personal	solve:adam,af:relu,max_iter_2000,hl:(150,)
# 0.6504065040650406 0.6910900945744152 0.7 0.7276422764227642

# NN4:lgc00_15cl3:Count_Personal	solve:adam,af:relu,max_iter_2000,hl:(100,)
# 0.6408163265306123 0.7110121121619379 0.7189397710303633 0.8130081300813008

# NN4:lgc00_15cl3:Count_Personal	solve:adam,af:relu,max_iter_2500,hl:(100,)
# 0.6408163265306123 0.7110121121619379 0.7189397710303633 0.8130081300813008

# NN4:lgc00_15cl3:Count_Personal	solve:adam,af:relu,max_iter_3000,hl:(100,)
# 0.6408163265306123 0.7110121121619379 0.7189397710303633 0.8130081300813008

# NN4:lgc00_15cl3:Count_Personal	solve:adam,af:relu,max_iter_2000,hl:(175,)
# 0.6707317073170732 0.718362369337979 0.7148498423759748 0.7967479674796748

# NN4:lgc00_15cl3:Count_Personal	solve:adam,af:relu,max_iter_2500,hl:(175,)
# 0.6707317073170732 0.718362369337979 0.7148498423759748 0.7967479674796748

# NN4:lgc00_15cl3:Count_Personal	solve:adam,af:relu,max_iter_3000,hl:(175,)
# 0.6707317073170732 0.718362369337979 0.7148498423759748 0.7967479674796748

# NN4:lgc00_15cl3:Count	solve:adam,af:relu,max_iter_2000,hl:(100,)
# 0.6775510204081633 0.7215828770532603 0.7128256180520989 0.7764227642276422

# NN4:lgc00_15cl3:Count	solve:adam,af:relu,max_iter_2500,hl:(100,)
# 0.6775510204081633 0.7215828770532603 0.7128256180520989 0.7764227642276422

# NN4:lgc00_15cl3:Count	solve:adam,af:relu,max_iter_3000,hl:(100,),
# 0.6775510204081633 0.7215828770532603 0.7128256180520989 0.7764227642276422


# 666

# NN3:lgc00_15cl3:Count_Personal	solve:adam,af:relu,max_iter_2000,hl:(300,)
# 0.6504065040650406 0.7032984901277584 0.7006304961008794 0.7601626016260162

# NN4:lgc00_15cl3:Count_Personal	solve:adam,af:relu,max_iter_2000,hl:(150,)
# 0.6544715447154471 0.711046955367513 0.7046872407499585 0.7926829268292683

# NN4:lgc00_15cl3:Count_Personal	solve:adam,af:relu,max_iter_2000,hl:(250,)
# 0.6300813008130082 0.7049294839887175 0.7032520325203252 0.8089430894308943

# NN5:lgc00_15cl3:Count_Personal	solve:adam,af:relu,max_iter_2000,hl:(250,)
# 0.6788617886178862 0.727297162767546 0.7250373320059731 0.8089430894308943

# NN5:lgc00_15cl3:Count_Personal	solve:adam,af:relu,max_iter_2500,hl:(250,)
# 0.6788617886178862 0.727297162767546 0.7250373320059731 0.8089430894308943

# NN4:lgc00_15cl3:Count	solve:adam,af:relu,max_iter_2500,hl:(100,)
# 0.6626016260162602 0.7147021735523478 0.7142857142857143 0.7845528455284553

# NN4:lgc00_15cl3:Count	solve:adam,af:relu,max_iter_2000,hl:(150,)
# 0.6666666666666666 0.7159299817487972 0.7134146341463414 0.8252032520325203


# NN4:lgc00_15cl3:Count_Personal	solve:adam,af:relu,max_iter_2000,hl:(150, 150)
# 0.6544715447154471 0.7203948896631823 0.7102040816326531 0.8048780487804879

# NN5:lgc00_15cl3:Count_Personal	solve:adam,af:relu,max_iter_2000,hl:(200, 200)
# 0.6775510204081633 0.7240501078480173 0.717479674796748 0.8170731707317073

# NN5:lgc00_15cl3:Count_Personal	solve:adam,af:relu,max_iter_2000,hl:(200, 200, 200)
# 0.6585365853658537 0.723645262983242 0.7235772357723578 0.8414634146341463


# NN5:lgc00_15cl3:Count_Personal	solve:adam, af:relu, max_iter_2000, hl:(250, 250, 250), rs:555
# 0.673469387755102 0.732570101211216 0.7270947403351584 0.8292682926829268
# NN5:lgc00_15cl3:Count_Personal	solve:adam, af:relu, max_iter_3000, hl:(250, 250, 250), rs:555
# 0.673469387755102 0.732570101211216 0.7270947403351584 0.8292682926829268


###

