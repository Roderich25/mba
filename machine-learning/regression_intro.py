import pandas as pd
import quandl

df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_Pct'] = (df['Adj. High']-df['Adj. Close'])/df['Adj. Close'] * 100
df['Pct_change'] = (df['Adj. Close']-df['Adj. Open'])/df['Adj. Open'] * 100
df = df[['Adj. Close', 'HL_Pct', 'Pct_change', 'Adj. Volume']]
print(df.head())
