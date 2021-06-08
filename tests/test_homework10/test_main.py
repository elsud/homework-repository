from unittest.mock import Mock

import pytest

from homework10 import main


def test_get_code(monkeypatch):
    mocked = Mock()
    mocked.find.return_value.text = "\n\ntest"
    monkeypatch.setitem(globals(), "bs4.BeautifulSoup", mocked)
    assert main.get_code(mocked) == "test"


def test_get_ratio_when_ratio_presents(monkeypatch):
    mocked = Mock()
    mocked.find_all.return_value = ["", "\n1,111.1\n"]
    mocked.find_all.return_value[1] = Mock()
    mocked.find_all.return_value[1].previous.previous = "\n1,111.1\n"
    monkeypatch.setitem(globals(), "bs4.BeautifulSoup", mocked)
    assert main.get_ratio(mocked) == pytest.approx(1111.1)


def test_ratio_when_there_is_not_ratio(monkeypatch):
    mocked = Mock()
    mocked.find_all.return_value = []
    monkeypatch.setitem(globals(), "bs4.BeautifulSoup", mocked)
    assert main.get_ratio(mocked) == float("inf")


def test_get_low_and_get_high_when_there_is_not_any_of_them(monkeypatch):
    mocked = Mock()
    mocked.find.return_value = None
    monkeypatch.setitem(globals(), "bs4.BeautifulSoup", mocked)
    assert main.get_low(mocked) is None
    assert main.get_high(mocked) is None


def test_get_low_and_get_high_when_they_present(monkeypatch):
    mocked = Mock()
    mocked.find.return_value.previous.previous = "test"
    monkeypatch.setitem(globals(), "bs4.BeautifulSoup", mocked)
    assert main.get_low(mocked) == "test"
    assert main.get_high(mocked) == "test"


def test_get_all_info(monkeypatch):
    soup = Mock()
    code, ratio, high, low = Mock(), Mock(), Mock(), Mock()
    code.return_value = "code"
    ratio.return_value = "ratio"
    low.return_value = "low"
    high.return_value = "high"
    monkeypatch.setitem(globals(), "bs4.BeautifulSoup", soup)
    monkeypatch.setattr(main, "get_code", code)
    monkeypatch.setattr(main, "get_ratio", ratio)
    monkeypatch.setattr(main, "get_low", low)
    monkeypatch.setattr(main, "get_high", high)
    assert main.get_all_info("page") == ("code", "ratio", "high", "low")


def test_put_in_dict(monkeypatch):
    mocked = Mock()
    mocked.return_value = "1", "1", "1", "1"
    monkeypatch.setattr(main, "get_all_info", mocked)
    expected = {"name": {"code": "1", "ratio": "1", "profit": 0.0}}
    assert main.put_in_dict(("name", None)) == expected


def test_put_in_dict_when_there_were_not_low_and_high(monkeypatch):
    mocked = Mock()
    mocked.return_value = "1", "1", None, None
    monkeypatch.setattr(main, "get_all_info", mocked)
    expected = {"name": {"code": "1", "ratio": "1", "profit": float("-inf")}}
    assert main.put_in_dict(("name", None)) == expected
