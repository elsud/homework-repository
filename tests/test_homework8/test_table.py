from homework8.table import TableData

presidents = TableData(database_name="example.sqlite", table_name="presidents")


def test_get_item_returns_table_row_for_given_name():
    assert presidents["Yeltsin"] == ("Yeltsin", 999, "Russia")


def test_get_non_existing_item_returns_empty_result():
    assert not presidents["No one"]


def test_check_existing_name_in_table():
    assert "Yeltsin" in presidents


def test_check_not_existing_name_in_table_returns_false():
    assert "No one" not in presidents


def test_len_gives_amount_of_table_rows():
    assert len(presidents) == 3


def test_iteration_over_rows_of_table():
    for president in presidents:
        assert isinstance(president, dict)


def test_iteration_over_rows_with_access_by_key():
    names = ("Yeltsin", "Trump", "Big Man Tyrone")
    for president in presidents:
        assert president["name"] in names
