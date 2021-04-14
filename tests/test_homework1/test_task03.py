from homework1.task03 import find_maximum_and_minimum


def test_file_with_numbers(tmpdir):
    """Testing that file with integers gives min and max of integers."""
    text = "1\n2\n3\n4\n5\n-5\n"
    temp_file = tmpdir.join("file.txt")
    with open(temp_file, "w"):
        temp_file.write(text)
    assert find_maximum_and_minimum(temp_file) == (-5, 5)


def test_file_with_one_number(tmpdir):
    """Testing that file with one integer gives that integer as min and max."""
    text = "3\n"
    temp_file = tmpdir.join("file.txt")
    with open(temp_file, "w"):
        temp_file.write(text)
    assert find_maximum_and_minimum(temp_file) == (3, 3)
