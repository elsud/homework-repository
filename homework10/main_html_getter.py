"""Getting html for 10 pages with info about companies and putting it
into global variable 'HTMLS'.
"""
import asyncio
from typing import ContextManager

import aiohttp

LINK = "https://markets.businessinsider.com/index/components/s&p_500"
ENDS = ("", "?p=2", "?p=3", "?p=4", "?p=5", "?p=6", "?p=7", "?p=8", "?p=9", "?p=10")
urls = (LINK + end for end in ENDS)
HTMLS = None


async def get_page(url: str, session: ContextManager) -> str:
    """Get html text from url.
    :param url: url address
    :type url: str
    :param session:web session
    :type session: aiohttp.client.ClientSession
    :return: html text
    :rtype: str
    """
    async with session.get(url) as response:
        body = await response.text()
        return body


async def main() -> None:
    """Creates tasks to get html from several urls and puts generator
    with htmls in global variable 'HTMLS'.
    """
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(get_page(url, session)) for url in urls]
        await asyncio.gather(*tasks)
        global HTMLS
        HTMLS = (task.result() for task in tasks)


asyncio.run(main())
