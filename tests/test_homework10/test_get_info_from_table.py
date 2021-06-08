from unittest.mock import Mock

from homework10 import get_info_from_table as g


def test_get_links(monkeypatch):
    mocked = Mock()
    mocked.table.find_all.return_value = ["1"]
    mocked.table.find_all.return_value[0] = Mock()
    mocked.table.find_all.return_value[0].get.return_value = ""
    monkeypatch.setitem(globals(), "bs4.BeautifulSoup", mocked)
    assert list(g.get_links(mocked)) == [g.LINK]


def test_get_names(monkeypatch):
    mocked = Mock()
    mocked.table.find_all.return_value = ["1"]
    mocked.table.find_all.return_value[0] = Mock()
    mocked.table.find_all.return_value[0].text = "test"
    monkeypatch.setitem(globals(), "bs4.BeautifulSoup", mocked)
    assert list(g.get_names(mocked)) == ["test"]


def test_get_prices(monkeypatch):
    mocked = Mock()
    mocked.table.find_all.return_value = ["1", "1"]
    mocked.table.find_all.return_value[1] = Mock()
    mocked.table.find_all.return_value[1].find.return_value.next = "\n1,111.1"
    rate = Mock()
    rate.return_value = 1
    monkeypatch.setitem(globals(), "bs4.BeautifulSoup", mocked)
    monkeypatch.setattr(g, "get_exchange_rate", rate)
    assert list(g.get_prices(mocked)) == [1111.1]


def test_get_year_growth(monkeypatch):
    mocked = Mock()
    mocked.table.find_all.return_value = ["1", "1"]
    mocked.table.find_all.return_value[1] = Mock()
    mocked.table.find_all.return_value[1].find_all.return_value = ["1"]
    mocked.table.find_all.return_value[1].find_all.return_value[-1] = Mock()
    mocked.table.find_all.return_value[1].find_all.return_value[-1].text = "1"
    monkeypatch.setitem(globals(), "bs4.BeautifulSoup", mocked)
    assert list(g.get_year_growth(mocked)) == ["1"]


def test_get_all_info_from_table(monkeypatch):
    soup = Mock()
    names, links, prices, growthes = Mock(), Mock(), Mock(), Mock()
    names.return_value = ("name1", "name2")
    links.return_value = ("link1", "link2")
    prices.return_value = ("price1", "price2")
    growthes.return_value = ("growth1", "growth2")
    monkeypatch.setitem(globals(), "bs4.BeautifulSoup", soup)
    monkeypatch.setattr(g, "get_names", names)
    monkeypatch.setattr(g, "get_links", links)
    monkeypatch.setattr(g, "get_prices", prices)
    monkeypatch.setattr(g, "get_year_growth", growthes)
    expected = [
        ("name1", "link1", "price1", "growth1"),
        ("name2", "link2", "price2", "growth2"),
    ]
    assert list(g.get_all_info_from_table("page")) == expected


def test_create_dict(monkeypatch):
    mocked = Mock()
    mocked.return_value = (
        ("name1", "link1", "price1", "growth1"),
        ("name2", "link2", "price2", "growth2"),
    )
    monkeypatch.setattr(g, "get_all_info_from_table", mocked)
    expected = {
        "name1": {"link": "link1", "price": "price1", "growth": "growth1"},
        "name2": {"link": "link2", "price": "price2", "growth": "growth2"},
    }
    assert g.create_dict(None) == expected
