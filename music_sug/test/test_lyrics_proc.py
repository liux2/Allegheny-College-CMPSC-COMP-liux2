"""Test to ensure that the functions in the lyrics_proc program are correct."""
import pytest
from music_main import lyrics_proc


def test_song_csv():
    """Test if function can list all the files and merge them."""
    merged_song_list = lyrics_proc.song_csv()
    assert merged_song_list


@pytest.mark.parametrize(
    "song_title, song_artist",
    [
        ("Country House", "Blur"),
        ("On Top Of The World", "Imagine Dragons"),
        ("Scared To Live", "The Weeknd"),
    ],
)
def test_get_lyrics(song_title, song_artist):
    """Test if the function can return string."""
    lyrics = lyrics_proc.get_lyrics(song_title, song_artist)
    assert type(lyrics) == str


@pytest.mark.parametrize(
    "check_text", ["This is English.", "This is not English.", "Good morning!"],
)
def test_check_language_pass(check_text):
    """Test if function can detect English."""
    language_en = lyrics_proc.check_language(check_text)
    assert language_en


@pytest.mark.parametrize(
    "check_text", ["Das ist Deutsch!", "Das ist auch Deutsch!", "Wie geht's dir?"],
)
def test_check_language_fail(check_text):
    """Test if function can detect non-English."""
    language_en = lyrics_proc.check_language(check_text)
    state = language_en != True
    assert state
