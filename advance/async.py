import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            return await res.text()


async def main():
    urls = ['https://www.programiz.com','https://www.geeksforgeeks.org']
    tasks = [fetch(url) for url in urls]
    res = await asyncio.gather(*tasks)
    for i,res_ in enumerate(res):
        print(f'Response {i+1} from {urls[i]}: {res_[:100]}')

asyncio.run(main())