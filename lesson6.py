songs = []
artists = []
final_playlist = {}

input_songs = input("Введите названия песен через запятые (песня, песня...):\n— ")
split_input = input_songs.split(", ")
for song in split_input:
    songs.append(song.capitalize())

input_artists = input("Введите названия исполнителей через запятые (исполнитель, исполнитель...):\n— ")
split_input = input_artists.split(", ")
for artist in split_input:
    artists.append(artist.capitalize())


grouped_songs_with_artists = list(zip(songs, artists))

for song, artist in grouped_songs_with_artists:
    if artist in final_playlist:
        final_playlist[artist].append(song)
    else:
        final_playlist[artist] = [song]


print("\nВаш плейлист")
for song, artist in grouped_songs_with_artists:
    print(f"{song} — {artist}")

print("\nСгруппированный плейлист")
for artist, songs in final_playlist.items():
    print(f"{artist} — {', '.join(songs)}")