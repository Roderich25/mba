import pandas as pd
import quandl
import math
import os

quandl.ApiConfig.api_key = os.getenv('QUANDL_API_KEY')
df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_Pct'] = (df['Adj. High']-df['Adj. Close'])/df['Adj. Close'] * 100
df['Pct_change'] = (df['Adj. Close']-df['Adj. Open'])/df['Adj. Open'] * 100
df = df[['Adj. Close', 'HL_Pct', 'Pct_change', 'Adj. Volume']]

output = 'Adj. Close'
df.fillna(-99999, inplace=True)
#test_n = int(math.ceil(0.1*len(df)))
df['label'] = df[output].shift(-2)
df.dropna(inplace=True)
print(df.head(25))