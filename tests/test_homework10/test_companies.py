import pytest
from homework10.companies import Company


@pytest.fixture
def create_companies():
    companies = (
        ("name0", 0, "0", 100, 100, 0),
        ("name1", 10, "1", 90, 90, 10),
        ("name2", 20, "2", 80, 80, 20),
        ("name3", 30, "3", 70, 70, 30),
        ("name4", 40, "4", 60, 60, 40),
        ("name5", 50, "5", 50, 50, 50),
        ("name6", 60, "6", 40, 40, 60),
        ("name7", 70, "7", 30, 30, 70),
        ("name8", 80, "8", 20, 20, 80),
        ("name9", 90, "9", 10, 10, 90),
        ("name10", 100, "10", 0, 0, 100),
    )
    for company in companies:
        Company(*company)


def test_get_most_expensive(create_companies, tmp_path):
    path = tmp_path / "text.json"
    Company.get_most_expensive(path)

    with open(path) as fi:
        data = fi.read()

    assert data.startswith('[{"code": "10", "name": "name10", "price": 100},')


def test_get_lowest_ratio(create_companies, tmp_path):
    path = tmp_path / "text.json"
    Company.get_lowest_ratio(path)

    with open(path) as fi:
        data = fi.read()

    assert data.startswith('[{"code": "10", "name": "name10", "P/E ratio": 0},')


def test_get_max_growth(create_companies, tmp_path):
    path = tmp_path / "text.json"
    Company.get_max_growth(path)

    with open(path) as fi:
        data = fi.read()

    assert data.startswith('[{"code": "0", "name": "name0", "growth": "100%"},')


def test_get_max_profit(create_companies, tmp_path):
    path = tmp_path / "text.json"
    Company.get_max_profit(path)

    with open(path) as fi:
        data = fi.read()

    assert data.startswith(
        '[{"code": "10", "name": "name10", "potential profit": "100%"},'
    )
