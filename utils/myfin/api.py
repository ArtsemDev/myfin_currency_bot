from typing import Literal

from aiohttp import ClientSession
from bs4 import BeautifulSoup as bs


class MyfinAPI(object):

    BASE_URL: str = 'https://myfin.by'

    @classmethod
    async def _get(cls, url: str, params: dict = None) -> str:
        async with ClientSession(base_url=cls.BASE_URL) as session:
            async with session.get(url=url, params=params) as response:
                if response.status == 200:
                    return await response.text()

    @classmethod
    def _get_currency(cls, html: str, currency: str) -> dict:
        currencies_index = {
            'USD': {
                'buy': 1,
                'sell': 2
            },
            'EUR': {
                'buy': 3,
                'sell': 4
            },
            'RUR': {
                'buy': 5,
                'sell': 6
            }
        }
        soup = bs(html, 'lxml')
        tags_tr = soup.find_all('tr', class_='c-currency-table__main-row')
        data = {}
        for tag in tags_tr:
            tds = tag.find_all('td')
            name = tds[0].find('img', class_='load_image')['alt']
            data[name] = {
                currency: {
                    'buy': tds[currencies_index[currency]['buy']].get_text(),
                    'sell': tds[currencies_index[currency]['sell']].get_text()
                }
            }
        return data

    @classmethod
    async def currency(cls, currency: Literal['USD', 'EUR', 'RUR'] = 'USD', city: str = 'minsk') -> dict:
        html = await cls._get(f'/currency/{city}')
        if html:
            return cls._get_currency(html, currency)


if __name__ == '__main__':
    import asyncio
    asyncio.run(MyfinAPI.currency('USD'))
