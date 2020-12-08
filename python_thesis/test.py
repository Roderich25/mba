from geopy.distance import distance
from encodings.aliases import aliases
import pandas as pd

print(distance((19.513465, -98.8821628), (19.5187393, -98.8765105)).meters)

alias_values = set(aliases.values())
print(alias_values)
for encoding in set(aliases.values()):
    try:
        print("...")
        df = pd.read_csv("denue/DENUE_INEGI_11_.csv", encoding=encoding, low_memory=False)
        print('successful', encoding)
        print(df[df.columns[1:3]].head(10))
    except:
        pass
# iso8859_2 iso8859_15 cp1254 iso8859_13 iso8859_14 latin_1 cp1258 cp1252 iso8859_16 cp1250 iso8859_9 iso8859_10
# clf = LogisticRegression(solver='lbfgs', multi_class='multinomial', penalty='l2', C=0.5)
# df.POB_TOTAL = df.POB_TOTAL / 1000
# X = df.iloc[:, 2:].div(df.POB_TOTAL, axis=0)