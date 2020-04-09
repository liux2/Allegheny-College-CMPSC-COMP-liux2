import re
import csv
import spacy
import lyricsgenius
from os import listdir
from music_main import db
from os.path import isfile, join
from music_main.models import Lyrics
from spacy_langdetect import LanguageDetector
from music_main.text_proc import word_bag_list, compare_sum


def song_csv():
    """Utilize lyrics csv"""
    song_list = []
    playlist_files = [f for f in listdir("playlist/") if isfile(join("playlist/", f))]
    for file in playlist_files:
        with open("playlist/" + file, "r",) as l:
            csv_reader = csv.reader(l)
            # Skip the header
            next(csv_reader)
            for row in l:
                row_list = row.replace('"', "").replace("\n", "").split(",")
                song_list.append(row_list)
    return song_list


def get_lyrics(song_title, song_artist):
    # query the song
    genius = lyricsgenius.Genius(
        "oEVqU7niYZJeTMsZAy_lPCNKEasIE0_yp18SZ6b2yCbElD-LcI5Th2btmbck4haS"
    )
    song = genius.search_song(song_title, song_artist)
    if song is not None:
        lyrics_pattern = re.findall(r"[0-9][\/][0-9]", song.lyrics)
        # song.lyrics is type str
        if len(lyrics_pattern) < 2:
            return song.lyrics
        else:
            return None


def check_language(check_text):
    # load language model
    lang = spacy.load("en")
    lang.add_pipe(LanguageDetector(), name="language_detector", last=True)
    doc_check = lang(check_text)
    if doc_check._.language["language"] == "en":
        return True


def commit_music_db(song_title, song_author_str, song_lyrics_str, lyrics_sum_json):
    lyrics = Lyrics(
        song=song_title,
        song_author=song_author_str,
        song_lyrics=song_lyrics_str,
        lyrics_sum=lyrics_sum_json,
    )
    db.session.add(lyrics)
    db.session.commit()


def lyrics_main():
    for item in song_csv():
        lyrics_str = get_lyrics(item[0], item[1])
        if lyrics_str is not None and check_language(lyrics_str):
            lyrics_sum_list = word_bag_list(lyrics_str)
            commit_music_db(item[0], item[1], lyrics_str, lyrics_sum_list)
