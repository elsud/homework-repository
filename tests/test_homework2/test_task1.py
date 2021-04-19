from homework2 import task1 as t1


def create_text_file(file_path, text):
    """Creating temporary file with text for test."""
    with open(file_path, "w"):
        file_path.write(text)


def test_longest_words(tmpdir):
    """Testing that we get 10 words with longest set of unique symbols."""
    text = """a, abc, abcd, abcde, abcdef, abcdefg, abcdefgh, abcdefghi,
    abcdefghij, abcdefghijk, abcdefghijkl, abcdefghijklm, abcdefghijklmn"""
    expected = [
        "abcdefghijklmn",
        "abcdefghijklm",
        "abcdefghijkl",
        "abcdefghijk",
        "abcdefghij",
        "abcdefghi",
        "abcdefgh",
        "abcdefg",
        "abcdef",
        "abcde",
    ]
    temp_file = tmpdir.join("file.txt")
    create_text_file(temp_file, text)
    assert t1.get_longest_diverse_words(temp_file) == expected


def test_rarest_char(tmpdir):
    """Testing that rarest char is the char that repeats least of all."""
    text = "aaaBBccccsss"
    expected = "B"
    temp_file = tmpdir.join("file.txt")
    create_text_file(temp_file, text)
    assert t1.get_rarest_char(temp_file) == expected


def test_count_punctuation(tmpdir):
    """Testing that text consisting of punctuation chars and a space gives
    length of text without one space element as result."""
    text = ",,,..... :::;;?!"
    expected = len(text) - 1
    temp_file = tmpdir.join("file.txt")
    create_text_file(temp_file, text)
    assert t1.count_punctuation_chars(temp_file) == expected


def test_count_non_ascii(tmpdir):
    """Testing that concatenation of ascii and non ascii text gives length of non ascii text."""
    non_ascii_text, ascii_text = "ßääüö", "  khgfhjb ihgf"
    text = ascii_text + non_ascii_text.encode("unicode_escape").decode()
    temp_file = tmpdir.join("file.txt")
    create_text_file(temp_file, text)
    assert t1.count_non_ascii_chars(temp_file) == len(non_ascii_text)


def test_most_common_non_ascii(tmpdir):
    """Testing that text with unique non ascii chars and one repeated non ascii char
    and one repeated ascii char gives repeated non ascii char."""
    text = ("ßäüö" + "Ü" * 5 + "d" * 10).encode("unicode_escape").decode()
    temp_file = tmpdir.join("file.txt")
    create_text_file(temp_file, text)
    assert t1.get_most_common_non_ascii_char(temp_file) == "Ü"
