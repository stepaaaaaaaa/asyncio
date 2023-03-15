import asyncio
import requests
import time

async def get_data_from_api(api_url):
    response = requests.get(api_url)
    return response.json()

async def main():
    api_urls = [
        'https://api.covid19api.com/summary', # короче мне лень еще 9 апишок искать
    ]

    futures = [asyncio.ensure_future(get_data_from_api(url)) for url in api_urls]
    results = await asyncio.gather(*futures)

    for result in results:
        print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
