def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order
             in which they were chosen.
    """
    playlist = []
    free_space = max_size
    if songs[0][2] <= free_space:
        playlist.append(songs[0][0])
        free_space -= songs[0][2]
    else:
        return playlist

    sorted_songs = sorted(songs, key=lambda x: x[2])
    for i in range(len(sorted_songs)):
        if sorted_songs[i][2] <= free_space and sorted_songs[i][0] not in playlist:
            playlist.append(sorted_songs[i][0])
            free_space -= sorted_songs[i][2]

    return playlist

print(song_playlist([('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)], 11))