"""Test for task01 - Text work"""
import homework2.task01

path_data = "./tests/homework2/data.txt"


def test_most_unique_longest_words():
    """Testing data.txt: 10 unique longest words"""
    assert homework2.task01.get_longest_diverse_words(path_data) == [
        "Werkstättenlandschaft",
        "Geschichtsphilosophie",
        "Menschheitsgeschichte",
        "zoologischpolitischen",
        "Entscheidungsschlacht",
        "Mehrheitsvorstellungen",
        "politischstrategischen",
        "Souveränitätsansprüche",
        "symbolischsakramentale",
        "Wiederbelebungsübungen",
    ]


def test_rarest_char():
    """Testing data.txt: rarest symbol"""
    assert homework2.task01.get_rarest_char(path_data) == "›‹Yî’X()"


def test_count_punctuation_chars():
    """"Testing data.txt: count punctuation"""
    assert homework2.task01.count_punctuation_chars(path_data) == 5305


def test_count_non_ascii_chars():
    """Testing data.txt: count non ascii char"""
    assert homework2.task01.count_non_ascii_chars(path_data) == 2972


def test_get_most_common_non_ascii_char():
    """Testing data.txt: most common non ascii char"""
    assert homework2.task01.get_most_common_non_ascii_char(path_data) == "ä"
