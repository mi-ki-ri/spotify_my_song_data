import csv
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

with open("./dist/spotify_futures.tsv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter="\t")
    data = list(reader)
    df = pd.DataFrame(data)
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])
    print(df.head())

    df["duration"] = df["duration"].astype(float)
    df["danceability"] = df["danceability"].astype(float)
    df["energy"] = df["energy"].astype(float)
    df["loudness"] = df["loudness"].astype(float)
    df["speechiness"] = df["speechiness"].astype(float)
    df["acousticness"] = df["acousticness"].astype(float)
    df["instrumentalness"] = df["instrumentalness"].astype(float)
    df["liveness"] = df["liveness"].astype(float)
    df["valence"] = df["valence"].astype(float)
    df["tempo"] = df["tempo"].astype(float)
    df["key"] = df["key"].astype(str)

    print(df.describe())

    # most short song
    print("most short song:\n", df[df["duration"] == df["duration"].min()]["name"])
    print("")
    # most long song
    print("most long song:\n", df[df["duration"] == df["duration"].max()]["name"])
    print("")
    # fastest tempo song
    print("fastest tempo song:\n", df[df["tempo"] == df["tempo"].max()]["name"])
    print("")
    # slowest tempo song
    print("slowest tempo song:\n", df[df["tempo"] == df["tempo"].min()]["name"])
    print("")
    # most danceable song
    print(
        "most danceable song:\n",
        df[df["danceability"] == df["danceability"].max()]["name"],
    )
    print("")
    # most energetic song
    print("most energetic song:\n", df[df["energy"] == df["energy"].max()]["name"])
    print("")
    # most loud song
    print("most loud song:\n", df[df["loudness"] == df["loudness"].max()]["name"])
    print("")
    # most speechy song
    print(
        "most speechy song:\n", df[df["speechiness"] == df["speechiness"].max()]["name"]
    )
    print("")
    # most acoustic song
    print(
        "most acoustic song:\n",
        df[df["acousticness"] == df["acousticness"].max()]["name"],
    )
    print("")
    # most instrumental song
    print(
        "most instrumental song:\n",
        df[df["instrumentalness"] == df["instrumentalness"].max()]["name"],
    )
    print("")
    # most live song
    print("most live song:\n", df[df["liveness"] == df["liveness"].max()]["name"])
    print("")
    # most happy song
    print("most happy song:\n", df[df["valence"] == df["valence"].max()]["name"])
    print("")
    # most sad song
    print("most sad song:\n", df[df["valence"] == df["valence"].min()]["name"])
    print("")
    # most used key
    print("most used key:\n", df["key"].value_counts().idxmax())
