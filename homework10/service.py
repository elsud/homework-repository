import asyncio
import datetime
from concurrent.futures import ProcessPoolExecutor
from typing import ContextManager, Generator, Iterable, Tuple, Union

import aiohttp
import requests
from bs4 import BeautifulSoup


class ServiceTableHTML:
    """Service class to take html of several pages with partial information
    about companies. During initialization of class' instances they put themselves
    in list '_pages'. Class' variables '_link' and '_ends' give access to
    urls of pages to get html from.

    :param url: the end of the url which should add to '_link'
    :type url: str
    """

    _link = "https://markets.businessinsider.com/index/components/s&p_500"
    _ends = (
        "",
        "?p=2",
        "?p=3",
        "?p=4",
        "?p=5",
        "?p=6",
        "?p=7",
        "?p=8",
        "?p=9",
        "?p=10",
    )
    _pages = []

    def __init__(self, url: str) -> None:
        self.url = self._link + url
        ServiceTableHTML._pages.append(self)

    async def get_page(self, session: ContextManager) -> None:
        """Get html text from url and adds it to attribute 'html'.
        :param session:web session
        :type session: aiohttp.client.ClientSession
        """
        async with session.get(self.url) as response:
            self.html = await response.text()

    @classmethod
    async def top_up_htmls(cls: "ServiceTableHTML") -> None:
        """Creates tasks to get html from several pages and puts
        htmls to corresponding attibutes of class' instances.
        """
        async with aiohttp.ClientSession() as session:
            pages = (cls(url) for url in cls._ends)
            tasks = [asyncio.create_task(page.get_page(session)) for page in pages]
            await asyncio.gather(*tasks)


class ServiceCompanyHTML:
    """Service class for parsing html from ServiceTableHTML and for
    getting html companies' pages with the rest of the information
    about companies and parsing that html too. During initialization
    of class' instances they put themselves in list '_companies'.

    :param name: the name of the company
    :type name: str
    :param link: link on the company's page
    :type link: str
    :param price: price of the company's stock in rubles
    :type price: float
    :param growth: percent ot the company's year growth
    :type growth: str
    :param page: will be added later, it will be html
    :type page: None and later will be str
    :param code: the code of the company, will be added later
    :type code: None, will be string
    :param ratio: the P/E ratio of the company, will be added later
    :type ratio: None, will be float
    :param profit: potential profit of the company in percents
    :type profit: float
    """

    _companies = []

    def __init__(self, name: str, link: str, price: float, growth: str) -> None:
        self.name = name
        self.link = link
        self.price = price
        self.growth = growth
        self.page = None
        self.code = None
        self.ratio = None
        self.profit = float("-inf")
        ServiceCompanyHTML._companies.append(self)

    @staticmethod
    def get_links(soup: BeautifulSoup) -> Generator[str, None, None]:
        """Gets links on companies' pages from ServiceTableHTML html.
        :param soup: BeautifulSoup object with parsed html
        :type soup: bs4.BeautifulSoup
        :return: links on companies' urls
        :rtype: Generator
        """
        url = "https://markets.businessinsider.com"
        _links = soup.table.find_all("a")
        links = (url + link.get("href") for link in _links)
        return links

    @staticmethod
    def get_names(soup: BeautifulSoup) -> Generator[str, None, None]:
        """Gets companies' names from from ServiceTableHTML html.
        :param soup: BeautifulSoup object with parsed html
        :type soup: bs4.BeautifulSoup
        :return: names of companies'
        :rtype: Generator
        """
        _links = soup.table.find_all("a")
        names = (link.text for link in _links)
        return names

    @staticmethod
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

    @staticmethod
    def get_prices(soup: BeautifulSoup) -> Generator[float, None, None]:
        """Gets prices from ServiceTableHTML html and converts it to rubles.
        :param soup: BeautifulSoup object with parsed html
        :type soup: bs4.BeautifulSoup
        :return: price in rubles
        :rtype: float
        """
        _rows = soup.table.find_all("tr")[1:]
        _prices = (row.find("br").next.strip() for row in _rows)
        rate = ServiceCompanyHTML.get_exchange_rate()
        prices = (round(float(price.replace(",", "")) * rate, 2) for price in _prices)
        return prices

    @staticmethod
    def get_year_growth(soup: BeautifulSoup) -> Generator[str, None, None]:
        """Gets companies' year growthes in percents from ServiceTableHTML html
        and makes them floats instaed of strings.
        :param soup: BeautifulSoup object with parsed html
        :type soup: bs4.BeautifulSoup
        :return: companies' year growthes in percents
        :rtype: Generator
        """
        _rows = soup.table.find_all("tr")[1:]
        growth = (float(row.find_all("span")[-1].text[:-1]) for row in _rows)
        return growth

    @staticmethod
    def get_all_info_from_table(page: str) -> Iterable:
        """Gets all info about companies from ServiceTableHTML html:
        names, links, prices in rubles and year growthes in percents.
        :param page: html
        :type page: str
        :return: zip object with names, links, prices, year growthes
        :rtype: Iterable
        """
        soup = BeautifulSoup(page, "html.parser")
        return zip(
            ServiceCompanyHTML.get_names(soup),
            ServiceCompanyHTML.get_links(soup),
            ServiceCompanyHTML.get_prices(soup),
            ServiceCompanyHTML.get_year_growth(soup),
        )

    @classmethod
    def create_instances_from_page(cls, html: str) -> None:
        """Creates instances of ServiceCompanyHTML using
        information from ServiceTableHTML html.
        :param html: html text of main page
        :type html: str
        """
        for name, link, price, growth in cls.get_all_info_from_table(html):
            cls(name, link, price, growth)

    @classmethod
    def create_all_companies(cls) -> None:
        """Runs code of ServiceTableHTML to get html of main pages and
        creates instances of ServiceCompanyHTML with partial information
        about companies.
        """
        asyncio.run(ServiceTableHTML.top_up_htmls())
        htmls = (page.html for page in ServiceTableHTML._pages)
        for html in htmls:
            cls.create_instances_from_page(html)

    async def get_page(self, session: ContextManager) -> None:
        """Get html text from company's page and put it in
        new attribute 'page'.
        :param session: web session
        :type session: aiohttp.client.ClientSession
        """
        async with session.get(self.link) as response:
            self.page = await response.text()

    @classmethod
    async def add_all_pages(cls) -> None:
        """Creates tasks to get html from urls of all companies' pages.
        Puts html to instances' attributes 'page'.
        """
        async with aiohttp.ClientSession() as session:
            tasks = [
                asyncio.create_task(self.get_page(session)) for self in cls._companies
            ]
            await asyncio.gather(*tasks)

    def get_code(self, soup: BeautifulSoup) -> None:
        """Gets company's code and puts it in corresponding attribute.
        :param soup: BeautifulSoup object with parsed html
        :type soup: bs4.BeautifulSoup
        """
        self.code = soup.find(class_="price-section__category").text.strip()

    def get_ratio(self, soup: BeautifulSoup) -> None:
        """Gets company's P/E ratio and puts it in attribute 'ratio'.
        If there isn't P/E ratio sets the ratio's value float("inf").
        :param soup: BeautifulSoup object with parsed html
        :type soup: bs4.BeautifulSoup
        """
        ratio = soup.find_all(string="P/E Ratio")
        if len(ratio) > 1:
            self.ratio = float(ratio[1].previous.previous.strip().replace(",", ""))
        else:
            self.ratio = float("inf")

    @staticmethod
    def get_low(soup: BeautifulSoup) -> Union[str, None]:
        """Gets company's 52 week low as a string value.
        :param soup: BeautifulSoup object with parsed html
        :type soup: bs4.BeautifulSoup
        :return: 52 week low of the company or None
        :rtype: str
        """
        low = soup.find(string="52 Week Low")
        return low.previous.previous.strip() if low else None

    @staticmethod
    def get_high(soup: BeautifulSoup) -> Union[str, None]:
        """Gets company's 52 week high as a string value.
        :param soup: BeautifulSoup object with parsed html
        :type soup: bs4.BeautifulSoup
        :return: 52 week high of the company or None
        :rtype: str
        """
        high = soup.find(string="52 Week High")
        return high.previous.previous.strip() if high else None

    def add_attributes_to_company(self, page: str) -> Tuple[str, float]:
        """Gets info about company's code, P/E ratio, 52 week low, 52 week high,
        calculates potential profit if it can and sets attributes 'code',
        'ratio', 'profit'. Returns tuple with some attributes' values.
        :param page: html
        :type page: str
        :return: tuple with name, price, code, growth, P/E ratio, profit
        :rtype: tuple
        """
        soup = BeautifulSoup(page, "html.parser")
        self.get_code(soup)
        self.get_ratio(soup)
        _high = ServiceCompanyHTML.get_high(soup)
        _low = ServiceCompanyHTML.get_low(soup)
        if _high and _low:
            high = float(_high.replace(",", ""))
            low = float(_low.replace(",", ""))
            profit = (high - low) * 100 / low
            self.profit = round(profit, 2)
        return (self.name, self.price, self.code, self.growth, self.ratio, self.profit)

    @classmethod
    def all_companies_info(cls) -> Iterable:
        """Runs code of creating ServiceCompanyHTML instances with partial
        information. After that run code to get html of all
        companies' pages and using multiprocessing add attributes with
        the rest of information and returns map object with tuples
        of companies' names, prices, codes, growthes, ratios and profits.
        It will be used to create instances of Company.

        :return: map object with information about companies
        to create Company's instances
        rtype: Iterable
        """
        cls.create_all_companies()
        asyncio.run(cls.add_all_pages())
        pages = (company.page for company in cls._companies)
        with ProcessPoolExecutor() as pool:
            result = pool.map(cls.add_attributes_to_company, cls._companies, pages)
            return result
