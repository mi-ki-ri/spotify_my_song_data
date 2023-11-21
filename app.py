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

results = spotify.playlist(pllist_id, fields="tracks,next")
# print(results["tracks"]["items"][0]["track"]["name"])
songs = results["tracks"]["items"]
print(results["tracks"]["next"])
if results["tracks"]["next"] is not None:
    results = spotify.next(results["tracks"])
    songs.extend(results["items"])
# results = spotify.next(results["tracks"])
# songs.extend(results["items"])
#     results = spotify.next(results)
#     songs.extend(results["items"])

for song in songs:
    print(song["track"]["name"])
    audio_features = spotify.audio_features(song["track"]["id"])

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
