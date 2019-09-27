import pandas as pd
import quandl, math, os
import numpy as np
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

quandl.ApiConfig.api_key = os.getenv('QUANDL_API_KEY')
df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_Pct'] = (df['Adj. High']-df['Adj. Close'])/df['Adj. Close'] * 100
df['Pct_change'] = (df['Adj. Close']-df['Adj. Open'])/df['Adj. Open'] * 100
df = df[['Adj. Close', 'HL_Pct', 'Pct_change', 'Adj. Volume']]

output = 'Adj. Close'
df.fillna(-99999, inplace=True)
df['label'] = df[output].shift(-10)
df.dropna(inplace=True)

X = np.array(df.drop(['label'], 1))
y = np.array(df['label'])

X = preprocessing.scale(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

clf = LinearRegression()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print(accuracy)
