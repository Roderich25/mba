import datetime
import matplotlib.pyplot as plt
import numpy as np
import os
import pickle
import quandl
from matplotlib import style
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

style.use('ggplot')

quandl.ApiConfig.api_key = os.getenv('QUANDL_API_KEY')
df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_Pct'] = (df['Adj. High']-df['Adj. Close'])/df['Adj. Close'] * 100
df['Pct_change'] = (df['Adj. Close']-df['Adj. Open'])/df['Adj. Open'] * 100
df = df[['Adj. Close', 'HL_Pct', 'Pct_change', 'Adj. Volume']]


output = 'Adj. Close'
df.fillna(-99999, inplace=True)
forecast_out = 10
df['label'] = df[output].shift(-forecast_out)

X = np.array(df.drop(['label'], 1))
X = preprocessing.scale(X)
X = X[:-forecast_out]
X_last = X[-forecast_out:]
df.dropna(inplace=True)

y = np.array(df['label'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)


# clf = LinearRegression(n_jobs=-1)
# # clf = svm.SVR()
# clf.fit(X_train, y_train)
# with open('linear_regression.pickle', 'wb') as f:
#     pickle.dump(clf, f)

pickle_in = open('linear_regression.pickle', 'rb')
clf = pickle.load(pickle_in)

accuracy = clf.score(X_test, y_test)
forecast_set = clf.predict(X_last)
print(forecast_set, accuracy, forecast_out)

df['Forecast'] = np.nan
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86_400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()


