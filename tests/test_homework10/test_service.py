from unittest.mock import Mock

import pytest

from homework10.service import ServiceCompanyHTML as C
from homework10.service import ServiceTableHTML as T


def test_init_service_table_html():
    page = T("a")
    assert page in T._pages


def test_get_links(monkeypatch):
    mocked = Mock()
    mocked.table.find_all.return_value = ["1"]
    mocked.table.find_all.return_value[0] = Mock()
    mocked.table.find_all.return_value[0].get.return_value = ""
    monkeypatch.setitem(globals(), "bs4.BeautifulSoup", mocked)
    expected = "https://markets.businessinsider.com"
    assert list(C.get_links(mocked)) == [expected]


def test_get_names(monkeypatch):
    mocked = Mock()
    mocked.table.find_all.return_value = ["1"]
    mocked.table.find_all.return_value[0] = Mock()
    mocked.table.find_all.return_value[0].text = "test"
    monkeypatch.setitem(globals(), "bs4.BeautifulSoup", mocked)
    assert list(C.get_names(mocked)) == ["test"]


def test_get_prices(monkeypatch):
    mocked = Mock()
    mocked.table.find_all.return_value = ["1", "1"]
    mocked.table.find_all.return_value[1] = Mock()
    mocked.table.find_all.return_value[1].find.return_value.next = "\n1,111.1"
    rate = Mock()
    rate.return_value = 1
    monkeypatch.setitem(globals(), "bs4.BeautifulSoup", mocked)
    monkeypatch.setattr(C, "get_exchange_rate", rate)
    assert list(C.get_prices(mocked)) == [1111.1]


def test_get_year_growth(monkeypatch):
    mocked = Mock()
    mocked.table.find_all.return_value = ["1", "1"]
    mocked.table.find_all.return_value[1] = Mock()
    mocked.table.find_all.return_value[1].find_all.return_value = ["1"]
    mocked.table.find_all.return_value[1].find_all.return_value[-1] = Mock()
    mocked.table.find_all.return_value[1].find_all.return_value[-1].text = "1%"
    monkeypatch.setitem(globals(), "bs4.BeautifulSoup", mocked)
    assert list(C.get_year_growth(mocked)) == [1]


def test_get_all_info_from_table(monkeypatch):
    soup = Mock()
    names, links, prices, growthes = Mock(), Mock(), Mock(), Mock()
    names.return_value = ("name1", "name2")
    links.return_value = ("link1", "link2")
    prices.return_value = ("price1", "price2")
    growthes.return_value = ("growth1", "growth2")
    monkeypatch.setitem(globals(), "bs4.BeautifulSoup", soup)
    monkeypatch.setattr(C, "get_names", names)
    monkeypatch.setattr(C, "get_links", links)
    monkeypatch.setattr(C, "get_prices", prices)
    monkeypatch.setattr(C, "get_year_growth", growthes)
    expected = [
        ("name1", "link1", "price1", "growth1"),
        ("name2", "link2", "price2", "growth2"),
    ]
    assert list(C.get_all_info_from_table("page")) == expected


def test_create_instances_from_page(monkeypatch):
    mocked = Mock()
    mocked.return_value = [
        ("name1", "link1", "price1", "growth1"),
        ("name2", "link2", "price2", "growth2"),
    ]
    monkeypatch.setattr(C, "get_all_info_from_table", mocked)
    C.create_instances_from_page(None)
    company1, company2 = C._companies
    assert company1.name == "name1"
    assert company2.price == "price2"
    assert company1.link == "link1"
    assert company2.growth == "growth2"


def test_get_code(monkeypatch):
    company = C("name", "link", "price", "growth")
    mocked = Mock()
    mocked.find.return_value.text = "\n\ntest"
    monkeypatch.setitem(globals(), "bs4.BeautifulSoup", mocked)
    company.get_code(mocked)
    assert company.code == "test"


def test_get_ratio_when_ratio_presents(monkeypatch):
    company = C("name", "link", "price", "growth")
    mocked = Mock()
    mocked.find_all.return_value = ["", "\n1,111.1\n"]
    mocked.find_all.return_value[1] = Mock()
    mocked.find_all.return_value[1].previous.previous = "\n1,111.1\n"
    monkeypatch.setitem(globals(), "bs4.BeautifulSoup", mocked)
    company.get_ratio(mocked)
    assert company.ratio == pytest.approx(1111.1)


def test_ratio_when_there_is_not_ratio(monkeypatch):
    company = C("name", "link", "price", "growth")
    mocked = Mock()
    mocked.find_all.return_value = []
    monkeypatch.setitem(globals(), "bs4.BeautifulSoup", mocked)
    company.get_ratio(mocked)
    assert company.ratio == float("inf")


def test_get_low_and_get_high_when_there_is_not_any_of_them(monkeypatch):
    company = C("name", "link", "price", "growth")
    mocked = Mock()
    mocked.find.return_value = None
    monkeypatch.setitem(globals(), "bs4.BeautifulSoup", mocked)
    assert company.get_low(mocked) is None
    assert company.get_high(mocked) is None


def test_get_low_and_get_high_when_they_present(monkeypatch):
    company = C("name", "link", "price", "growth")
    mocked = Mock()
    mocked.find.return_value.previous.previous = "test"
    monkeypatch.setitem(globals(), "bs4.BeautifulSoup", mocked)
    assert company.get_low(mocked) == "test"
    assert company.get_high(mocked) == "test"


def test_add_attributes_to_company_calculates_profit(monkeypatch):
    company = C("name", "link", "price", "growth")
    soup = Mock()
    code, ratio, high, low = Mock(), Mock(), Mock(), Mock()
    low.return_value = "10"
    high.return_value = "20"
    monkeypatch.setitem(globals(), "bs4.BeautifulSoup", soup)
    monkeypatch.setattr(C, "get_code", code)
    monkeypatch.setattr(C, "get_ratio", ratio)
    monkeypatch.setattr(C, "get_low", low)
    monkeypatch.setattr(C, "get_high", high)
    expected = ("name", "price", None, "growth", None, 100)
    assert company.add_attributes_to_company("page") == expected


def test_add_attributes_to_company_without_profit(monkeypatch):
    company = C("name", "link", "price", "growth")
    soup = Mock()
    code, ratio, high, low = Mock(), Mock(), Mock(), Mock()
    low.return_value = None
    high.return_value = None
    monkeypatch.setitem(globals(), "bs4.BeautifulSoup", soup)
    monkeypatch.setattr(C, "get_code", code)
    monkeypatch.setattr(C, "get_ratio", ratio)
    monkeypatch.setattr(C, "get_low", low)
    monkeypatch.setattr(C, "get_high", high)
    expected = ("name", "price", None, "growth", None, float("-inf"))
    assert company.add_attributes_to_company("page") == expected
