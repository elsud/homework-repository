"""Parsing htmls from 'COMPANIES_HTMLS' and adding info from it:
companies' codes, P/E ratios, potential profits - into
dictionary 'companies'.
"""
from concurrent.futures import ProcessPoolExecutor
from typing import Tuple, Union

from bs4 import BeautifulSoup

from homework10.company_html_getter import COMPANIES_HTMLS, companies


def get_code(soup: BeautifulSoup) -> str:
    """Gets company's code.
    :param soup: BeautifulSoup object with parsed html
    :type soup: bs4.BeautifulSoup
    :return: code of the company
    :rtype: str
    """
    code = soup.find(class_="price-section__category").text.strip()
    return code


def get_ratio(soup: BeautifulSoup) -> float:
    """Gets company's P/E ratio.
    :param soup: BeautifulSoup object with parsed html
    :type soup: bs4.BeautifulSoup
    :return: P/E ratio of the company or float("inf")
    :rtype: float
    """
    ratio = soup.find_all(string="P/E Ratio")
    if len(ratio) > 1:
        return float(ratio[1].previous.previous.strip().replace(",", ""))
    return float("inf")


def get_low(soup: BeautifulSoup) -> Union[str, None]:
    """Gets company's 52 week low as a string value.
    :param soup: BeautifulSoup object with parsed html
    :type soup: bs4.BeautifulSoup
    :return: 52 week low of the company or None
    :rtype: str
    """
    low = soup.find(string="52 Week Low")
    return low.previous.previous.strip() if low else None


def get_high(soup: BeautifulSoup) -> Union[str, None]:
    """Gets company's 52 week high as a string value.
    :param soup: BeautifulSoup object with parsed html
    :type soup: bs4.BeautifulSoup
    :return: 52 week high of the company or None
    :rtype: str
    """
    high = soup.find(string="52 Week High")
    return high.previous.previous.strip() if high else None


def get_all_info(page: str) -> Tuple[str, float, None]:
    """Gets info about company's code, P/E ratio, 52 week low, 52 week high.
    :param page: html
    :type page: str
    :return: tuple with code, P/E ratio, 52 week high, 52 week low
    :rtype: tuple
    """
    soup = BeautifulSoup(page, "html.parser")
    return get_code(soup), get_ratio(soup), get_high(soup), get_low(soup)


def put_in_dict(data: Tuple[str]) -> dict:
    """Creates dict with company's name as key and dict with
    company's code, P/E ratio and potential profit as value.
    :param data: tuple with name of company and html of its page
    :type data: tuple with str
    :return: dictionary with information about company from
    company's page
    rtype: dict
    """
    name, page = data
    code, ratio, _high, _low = get_all_info(page)
    if _high and _low:
        high = float(_high.replace(",", ""))
        low = float(_low.replace(",", ""))
        profit = (high - low) * 100 / low
    else:
        profit = float("-inf")
    return {name: {"code": code, "ratio": ratio, "profit": profit}}


def update_companies_dict() -> dict:
    """Using multiprocessing gathers all temporary companies' dicts
    created with 'put_in_dict' in map object and updates
    global dict 'companies' with info from it.
    :return: dictionary with all information about all companies,
    keys are companies' names, values are dictionary with companies'
    links, prices, year growthes, codes, P/E ratios and
    potential profits
    :rtype: dict
    """
    with ProcessPoolExecutor() as pool:
        dicts = pool.map(put_in_dict, COMPANIES_HTMLS)
        for item in dicts:
            for key, value in item.items():
                companies[key].update(value)
    return companies
