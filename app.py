import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def mode_and_key(mode, key):
    if mode == 1:
        mmode = "Major"
    elif mode == 0:
        mmode = "Minor"
    if key == 0:
        key = "C"
    elif key == 1:
        key = "C#"
    elif key == 2:
        key = "D"
    elif key == 3:
        key = "D#"
    elif key == 4:
        key = "E"
    elif key == 5:
        key = "F"
    elif key == 6:
        key = "F#"
    elif key == 7:
        key = "G"
    elif key == 8:
        key = "G#"
    elif key == 9:
        key = "A"
    elif key == 10:
        key = "A#"
    elif key == 11:
        key = "B"
    return key + " " + mmode


with open("./dist/spotify_futures.tsv", "w", encoding="utf-8") as f:
    f.write(
        "name\turi\tduration\tdanceability\tenergy\tkey\tloudness\tspeechiness\tacousticness\tinstrumentalness\tliveness\tvalence\ttempo\n"
    )

pllist_id = "7wPi7r7riR79uqk490n2ZG"
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.playlist_tracks(pllist_id, limit=100)
# print(results["tracks"]["items"][0]["track"]["name"])
songs = results["items"]
print(results["next"])
i = 100
while results["next"] is not None:
    results = spotify.playlist_tracks(pllist_id, limit=100, offset=i)
    songs.extend(results["items"])
    i += 100
# results = spotify.next(results["tracks"])
# songs.extend(results["items"])
#     results = spotify.next(results)
#     songs.extend(results["items"])

# print(songs)

for i, song in enumerate(songs):
    print(i, len(songs), song["track"]["name"])
    audio_features = spotify.audio_features(song["track"]["id"])

    # popularity = song["track"]["popularity"]

    for track in audio_features:
        track_feature = {
            "name": song["track"]["name"],
            "uri": song["track"]["uri"],
            "duration": float(track["duration_ms"] / 1000),
            "danceability": track["danceability"],
            "energy": track["energy"],
            "key": mode_and_key(track["mode"], track["key"]),
            "loudness": track["loudness"],
            "speechiness": track["speechiness"],
            "acousticness": track["acousticness"],
            "instrumentalness": track["instrumentalness"],
            "liveness": track["liveness"],
            "valence": track["valence"],
            "tempo": track["tempo"],
        }

        with open("./dist/spotify_futures.tsv", "a", encoding="utf-8") as f:
            f.write(
                "{name}\t{uri}\t{duration}\t{danceability}\t{energy}\t{key}\t{loudness}\t{speechiness}\t{acousticness}\t{instrumentalness}\t{liveness}\t{valence}\t{tempo}\n".format(
                    **track_feature
                )
            )

    time.sleep(0.5)
