from homework7.tree import find_occurrences

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


def test_there_are_six_red_in_example_tree():
    assert find_occurrences(example_tree, "RED") == 6


def test_there_are_one_nested_key_in_example_tree():
    assert find_occurrences(example_tree, "nested_key") == 1


def test_there_are_no_fifth_in_example_tree():
    assert find_occurrences(example_tree, "fifth") == 0


def test_result_on_red_changes_with_deleting_one_red():
    new = example_tree.copy()
    del new["fourth"]
    assert find_occurrences(new, "RED") == 5


def test_is_result_correct_when_the_element_is_a_sequence():
    elem = ["RED", "BLUE"]
    assert find_occurrences(example_tree, elem) == 1


def test_is_result_correct_when_the_element_is_a_dict():
    elem = {"first": ["RED", "BLUE"]}
    assert find_occurrences(example_tree, elem) == 1


def test_is_result_correct_when_the_element_is_a_nested_dict():
    elem = {"nested_key": "RED"}
    assert find_occurrences(example_tree, elem) == 1
