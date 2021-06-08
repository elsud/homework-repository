"""Creates 4 function to write info about top 10 most expensive,
with lowest P/E ratio, with highest year growth and with highest
potential profit in percents companies.
Info writes as json in file in current directory or in given to function path.
"""
import heapq
import json

from homework10.main import update_companies_dict

companies = update_companies_dict()


def get_most_expensive(path: str = "homework10/most_expensive.json") -> None:
    """Gets top 10 the most expensive companies and writes json
    with their codes, names and prices.
    :param path: path to file to write json
    :type path: str
    """
    top = heapq.nlargest(10, companies.items(), key=lambda x: x[1]["price"])
    json_top = []
    for item in top:
        code = item[1]["code"]
        name = item[0]
        price = round(item[1]["price"], 2)
        json_top.append(
            {
                "code": code,
                "name": name,
                "price": price,
            }
        )
    with open(path, "w") as fi:
        json.dump(json_top, fi)


def get_lowest_ratio(path: str = "homework10/lowest_ratio.json") -> None:
    """Gets top 10 companies with the lowest P/E ratio and writes json
    with their codes, names and P/E ratio.
    :param path: path to file to write json
    :type path: str
    """
    top = heapq.nsmallest(10, companies.items(), key=lambda x: x[1]["ratio"])
    json_top = []
    for item in top:
        code = item[1]["code"]
        name = item[0]
        ratio = item[1]["ratio"]
        json_top.append(
            {
                "code": code,
                "name": name,
                "P/E": ratio,
            }
        )
    with open(path, "w") as fi:
        json.dump(json_top, fi)


def get_max_growth(path: str = "homework10/max_growth.json") -> None:
    """Gets top 10 companies with the largest year growth and writes json
    with their codes, names and year growthes.
    :param path: path to file to write json
    :type path: str
    """
    top = heapq.nlargest(10, companies.items(), key=lambda x: x[1]["growth"])
    json_top = []
    for item in top:
        code = item[1]["code"]
        name = item[0]
        growth = item[1]["growth"]
        json_top.append(
            {
                "code": code,
                "name": name,
                "growth": growth,
            }
        )
    with open(path, "w") as fi:
        json.dump(json_top, fi)


def get_max_profit(path: str = "homework10/max_profit.json") -> None:
    """Gets top 10 companies with the largest potential profit and writes json
    with their codes, names and potential profits.
    :param path: path to file to write json
    :type path: str
    """
    top = heapq.nlargest(10, companies.items(), key=lambda x: x[1]["profit"])
    json_top = []
    for item in top:
        code = item[1]["code"]
        name = item[0]
        profit = str(round(item[1]["profit"], 2)) + "%"
        json_top.append(
            {
                "code": code,
                "name": name,
                "potential profit": profit,
            }
        )
    with open(path, "w") as fi:
        json.dump(json_top, fi)
