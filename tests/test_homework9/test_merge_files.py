from homework9.merge_files import iter_from_file, merge_sorted_files


def test_iter_from_file_returns_iterator_through_file(tmp_path):
    path_to_file = tmp_path / "file.txt"
    with open(path_to_file, "w") as fi:
        fi.write("1\n4\n9\n")
    assert list(iter_from_file(path_to_file)) == [1, 4, 9]


def test_merge_sorted_files_merge_numbers_in_right_order(tmp_path):
    path_to_1 = tmp_path / "file1.txt"
    path_to_2 = tmp_path / "file2.txt"
    with open(path_to_1, "w") as fi:
        fi.write("3\n5\n")
    with open(path_to_2, "w") as fi:
        fi.write("1\n2\n9\n")
    iterator = merge_sorted_files([path_to_1, path_to_2])
    assert list(iterator) == [1, 2, 3, 5, 9]
