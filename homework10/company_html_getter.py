"""Getting html for all companies with info about companies and putting it
into global variable 'COMPANIES_HTMLS' which contains tuples of
company's name and company's html.
"""
import asyncio
from typing import ContextManager, Generator, Tuple

import aiohttp

from homework10.get_info_from_table import gather_companies_info_in_dict

companies = gather_companies_info_in_dict()
urls = ((key, value["link"]) for key, value in companies.items())
COMPANIES_HTMLS = None


async def get_page(name: str, url: str, session: ContextManager) -> Tuple[str]:
    """Get html text from url.
    :param name: name of the company, we use it to add info in dict companies
    :type name: str
    :param url: url address
    :type url: str
    :param session: web session
    :type session: aiohttp.client.ClientSession
    :return: name of company and html text with info about it
    :rtype: tuple with str
    """
    async with session.get(url) as response:
        body = await response.text()
        return name, body


async def main() -> Generator[tuple, None, None]:
    """Creates tasks to get html from several urls. Puts generator
    with tuples with names of companies and htmls into global
    variable 'companies_htmls'.
    """
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(get_page(*url, session)) for url in urls]
        await asyncio.gather(*tasks)
        global COMPANIES_HTMLS
        COMPANIES_HTMLS = (task.result() for task in tasks)


asyncio.run(main())
