from homework9.file_counter import universal_file_counter


def test_gives_zero_when_there_are_no_files_with_right_extension(tmp_path):
    assert universal_file_counter(tmp_path, "txt") == 0


def test_gives_lines_number_when_there_are_no_tokenizer(tmp_path):
    path_to_1 = tmp_path / "2lines.txt"
    path_to_2 = tmp_path / "3lines.txt"
    with open(path_to_1, "w") as fi:
        fi.write("1\n2\n")
    with open(path_to_2, "w") as fi:
        fi.write("1\n2\n3\n")
    assert universal_file_counter(tmp_path, "txt") == 5


def test_gives_tokens_number_when_there_are_tokenizer(tmp_path):
    path = tmp_path / "file.txt"
    text = "1 2 3\n4\n"
    with open(path, "w") as fi:
        fi.write(text)
    expected = len(text.split())
    assert universal_file_counter(tmp_path, "txt", str.split) == expected
