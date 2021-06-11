import heapq
import json

from homework10.service import ServiceCompanyHTML


class Company:
    """Represents companies and gives opportunity to get
    information about most expensive companies or companies with
    the lowest ratio or max year growth or max potential profit.
    Class has variable '__cache' which stores all created instances.

    :param name: the name of the company
    :type name: str
    :param price: the price of the company's stock in rubles
    :type price: float
    :param code: the code of the company
    :type code: str
    :param growth: percent ot the company's year growth
    :type growth: float
    :param ratio: the P/E ratio of the company
    :type ratio: float
    :param profit: potential profit of the company
    :type profit: float
    """

    __cache = []

    def __init__(
        self,
        name: str,
        price: float,
        code: str,
        growth: float,
        ratio: float,
        profit: float,
    ) -> None:
        self.name = name
        self.price = price
        self.code = code
        self.growth = growth
        self.ratio = ratio
        self.profit = profit
        Company.__cache.append(self)

    @classmethod
    def get_most_expensive(cls, path: str = "homework10/most_expensive.json") -> None:
        """Gets top 10 the most expensive companies and writes json
        with their codes, names and prices. Has default path to write file to.
        :param path: path to file to write json
        :type path: str
        """
        top = heapq.nlargest(10, cls.__cache, key=lambda x: x.price)
        result = []
        for company in top:
            result.append(
                {
                    "code": company.code,
                    "name": company.name,
                    "price": company.price,
                }
            )
        with open(path, "w") as fi:
            json.dump(result, fi)

    @classmethod
    def get_lowest_ratio(cls, path: str = "homework10/lowest_ratio.json") -> None:
        """Gets top 10 companies with the lowest P/E ratio and writes json
        with their codes, names and P/E ratio. Has default path to write file to.
        :param path: path to file to write json
        :type path: str
        """
        top = heapq.nsmallest(10, cls.__cache, key=lambda x: x.ratio)
        result = []
        for company in top:
            result.append(
                {
                    "code": company.code,
                    "name": company.name,
                    "P/E ratio": company.ratio,
                }
            )
        with open(path, "w") as fi:
            json.dump(result, fi)

    @classmethod
    def get_max_growth(cls, path: str = "homework10/max_growth.json") -> None:
        """Gets top 10 companies with the largest year growth and writes json
        with their codes, names and year growthes.
        Has default path to write file to.
        :param path: path to file to write json
        :type path: str
        """
        top = heapq.nlargest(10, cls.__cache, key=lambda x: x.growth)
        result = []
        for company in top:
            result.append(
                {
                    "code": company.code,
                    "name": company.name,
                    "growth": str(company.growth) + "%",
                }
            )
        with open(path, "w") as fi:
            json.dump(result, fi)

    @classmethod
    def get_max_profit(cls, path: str = "homework10/max_profit.json") -> None:
        """Gets top 10 companies with the largest potential profit and writes
        json with their codes, names and potential profits.
        Has default path to write file to.
        :param path: path to file to write json
        :type path: str
        """
        top = heapq.nlargest(10, cls.__cache, key=lambda x: x.profit)
        result = []
        for company in top:
            result.append(
                {
                    "code": company.code,
                    "name": company.name,
                    "potential profit": str(company.profit) + "%",
                }
            )
        with open(path, "w") as fi:
            json.dump(result, fi)


if __name__ == "__main__":
    for info in ServiceCompanyHTML.all_companies_info():
        Company(*info)

    Company.get_most_expensive()
    Company.get_lowest_ratio()
    Company.get_max_growth()
    Company.get_max_profit()
