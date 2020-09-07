import pandas as pd
import sqlite3

df = pd.read_csv("rezago_social/rezago_social.csv")
conn = sqlite3.connect('denue.sqlite3')
df.to_sql('rezago', conn, if_exists='replace', index=False)
