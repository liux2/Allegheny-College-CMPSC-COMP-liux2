"""Test to ensure that the functions in the text_proc program are correct."""
import pytest
from music_main import text_proc


@pytest.mark.parametrize(
    "org_text",
    [
        "This is English. This is not important.",
        "This is not English. This is important.",
        "Good morning! How are you doing?",
    ],
)
def test_word_bag_list(org_text):
    """Test if the function can return a list of sentence."""
    assert len(text_proc.word_bag_list(org_text)) != 0


@pytest.mark.parametrize(
    "user_sum, lyrics_sum",
    [
        (["This is English. This is not important."], ["I'm speaking English."]),
        (["This is not English. This is important."], ["I'm speaking German."]),
        (["Good morning! How are you doing?"], ["How do you do?"]),
    ],
)
def test_compare_sum(user_sum, lyrics_sum):
    """Test if this function can return a list of scores."""
    score = text_proc.compare_sum(user_sum, lyrics_sum)
    assert type(score) == float
