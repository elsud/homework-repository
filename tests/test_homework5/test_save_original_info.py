from homework5.save_original_info import custom_sum


def test_decorated_function_saved_original_documentation():
    original_doc = "This function can sum any objects which have __add___"
    assert custom_sum.__doc__ == original_doc


def test_decorated_function_saved_original_name():
    assert custom_sum.__name__ == "custom_sum"


def test_has_function_attribut_with_link_to_original_function():
    assert custom_sum.__getattribute__("__original_func")


def test_original_function_work_without_printing(capsys):
    without_print = custom_sum.__original_func
    without_print(1, 2, 3, 4)
    out, _err = capsys.readouterr()
    assert not out


def test_decorated_function_prints_result(capsys):
    custom_sum(1, 2, 3, 4)
    out, _err = capsys.readouterr()
    assert out == "10\n"


def test_results_of_original_and_decorated_functions_are_equal():
    without_print = custom_sum.__original_func
    assert without_print(1, 2, 3, 4) == custom_sum(1, 2, 3, 4) == 10
    assert without_print([1], [3]) == custom_sum([1], [3]) == [1, 3]
