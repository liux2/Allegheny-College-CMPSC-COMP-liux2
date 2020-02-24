import csv
import lyricsgenius


class Lyrics:
    def song_csv():
        """Utilize lyrics csv"""
        song_list = []
        with open(
            "POP Music Playlist - Best POP Hits of All Time (Updated in 2020).csv", "r",
        ) as f:
            csv_reader = csv.reader(f)
            # Skip the header
            next(csv_reader)
            for row in f:
                row_list = row.replace('"', "").replace("\n", "").split(",")
                song_list.append(row_list)
        return song_list

    def get_lyrics(song_title, song_artist):
        # query the song
        genius = lyricsgenius.Genius(
            "oEVqU7niYZJeTMsZAy_lPCNKEasIE0_yp18SZ6b2yCbElD-LcI5Th2btmbck4haS"
        )
        song = genius.search_song(song_title, song_artist)
        # song.lyrics is type str
        if "[" in song.lyrics:
            return song.lyrics
        else:
            return None


class Sum:
    """TODO: if not English"""

    def replace():
        pass


Lyrics.get_lyrics()
