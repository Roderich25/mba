#!/usr/bin/env python3
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.dates as mdates
import mplfinance as mpf
from mplfinance.original_flavor import candlestick_ohlc
import pandas as pd
import pandas_datareader.data as web

style.use("ggplot")
start = dt.datetime(2018, 1, 1)
end = dt.date.today()

df = web.DataReader("BTCUSD=X", "yahoo", start, end)
df.to_csv("btc.csv")
df = pd.read_csv("btc.csv", parse_dates=True, index_col=0)

df["200MA"] = df["Adj Close"].rolling(window=200).mean()
df["20MA"] = df["Adj Close"].rolling(window=20).mean()
df_ohlc = df["Adj Close"].resample("10D").ohlc()
print(df_ohlc.tail())
df.dropna(inplace=True)
# print(df.tail())

# ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
# ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)
# ax1.plot(df.index, df["Adj Close"])
# ax1.plot(df.index, df["200MA"])
# ax1.plot(df.index, df["20MA"])
# ax2.bar(df.index, df["Volume"])

df[["Adj Close", "200MA", "20MA"]].plot()

# candlestick_ohlc(ax, df_ohlc, width=2, colorup="g", colordown="r")
plt.show()
mpf.plot(df, type="candle", mav=(20, 200), volume=False, style="mike")
