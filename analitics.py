import csv
import pandas as pd

with open("./dist/spotify_futures.tsv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter="\t")
    data = list(reader)
    df = pd.DataFrame(data)
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])
    print(df)
