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


def test_there_are_six_red():
    assert find_occurrences(example_tree, "RED") == 6


def test_there_are_one_nested_key():
    assert find_occurrences(example_tree, "nested_key") == 1


def test_there_are_no_fifth():
    assert find_occurrences(example_tree, "fifth") == 0


def test_result_on_red_changes_when_we_delete_one_red():
    new = example_tree.copy()
    del new["fourth"]
    assert find_occurrences(new, "RED") == 5
