"""Parsing html and putting info from it: companies' names, links,
prices and year growthes - into dictionary 'companies'.
"""
import datetime
from concurrent.futures import ProcessPoolExecutor
from typing import Generator, Iterable

import requests
from bs4 import BeautifulSoup

from homework10.main_html_getter import HTMLS

LINK = "https://markets.businessinsider.com"


def get_links(soup: BeautifulSoup) -> Generator[str, None, None]:
    """Gets links on companies' pages from table.
    :param soup: BeautifulSoup object with parsed html
    :type soup: bs4.BeautifulSoup
    :return: links on companies' urls
    :rtype: Generator
    """
    _links = soup.table.find_all("a")
    links = (LINK + link.get("href") for link in _links)
    return links


def get_names(soup: BeautifulSoup) -> Generator[str, None, None]:
    """Gets companies' names from table.
    :param soup: BeautifulSoup object with parsed html
    :type soup: bs4.BeautifulSoup
    :return: names of companies'
    :rtype: Generator
    """
    _links = soup.table.find_all("a")
    names = (link.text for link in _links)
    return names


def get_exchange_rate() -> float:
    """Gets exchange rate on current day from cbr to
    converts prices to rubles.
    :return: excange rate dollar to rubles
    :rtype: float
    """
    today = datetime.date.today().strftime("%d/%m/%Y")
    url = "http://www.cbr.ru/scripts/XML_daily.asp?date_req=" + today
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    rate = float(soup.find(id="R01235").value.text.replace(",", "."))
    return rate


def get_prices(soup: BeautifulSoup) -> Generator[float, None, None]:
    """Gets prices from table and converts it to rubles.
    :param soup: BeautifulSoup object with parsed html
    :type soup: bs4.BeautifulSoup
    :return: price in rubles
    :rtype: float
    """
    _rows = soup.table.find_all("tr")[1:]
    _prices = (row.find("br").next.strip() for row in _rows)
    rate = get_exchange_rate()
    prices = (float(price.replace(",", "")) * rate for price in _prices)
    return prices


def get_year_growth(soup: BeautifulSoup) -> Generator[str, None, None]:
    """Gets companies' year growthes in percents from table.
    :param soup: BeautifulSoup object with parsed html
    :type soup: bs4.BeautifulSoup
    :return: companies' year growthes in percents
    :rtype: Generator
    """
    _rows = soup.table.find_all("tr")[1:]
    growth = (row.find_all("span")[-1].text for row in _rows)
    return growth


def get_all_info_from_table(page: str) -> Iterable:
    """Gets all info about companies from table:
    names, links, prices in rubles and year growthes in percents.
    :param page: html
    :type page: str
    :return: zip object with names, links, prices, year growthes
    :rtype: Iterable
    """
    soup = BeautifulSoup(page, "html.parser")
    return zip(
        get_names(soup), get_links(soup), get_prices(soup), get_year_growth(soup)
    )


def create_dict(html: str) -> dict:
    """Creates dict with names of companies as keys and links,
    prices and year growthes as values.
    :param html: html text of main page
    :type html: str
    :return: dictionary with information about companies from
    one page of the table, keys are companies' names
    :rtype: dict
    """
    companies = dict()
    for name, link, price, growth in get_all_info_from_table(html):
        companies[name] = {"link": link, "price": price, "growth": growth}
    return companies


def gather_companies_info_in_dict() -> dict:
    """Using multiprocessing gathers 10 dicts with info about
    companies in one dict.
    :return: dictionary with information from table about all companies,
    keys are companies' names, values are dictionary with companies'
    links, prices and year growthes
    :rtype: dict
    """
    with ProcessPoolExecutor() as pool:
        dicts = pool.map(create_dict, HTMLS)
        companies = dict()
        for page in dicts:
            for key, value in page.items():
                companies[key] = value
    return companies
