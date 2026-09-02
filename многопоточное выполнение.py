import aiohttp
import requests
from time import time
import aiohttp
import asyncio

start_time = time()

urls = [
    "https://ya.ru",
    "https://mail.ru",
    "https://google.com"
]

hoi = []

for url in urls:
    r = requests.get(url)
    hoi.append(r.text)

# сколько времени займёт обращение к 3 сайтам в синхронном выполнении
print(f"Выполнено за: {time() - start_time}")


async def fetch(session, url):
    async with session.get(url) as resp:
        return await resp.text()

async def main():
    async with aiohttp.ClientSession() as session:
        doom = await asyncio.gather(*(fetch(session, url)))

# в многопоточном режиме обращаемся к 3 сайтам
asyncio.run(main())





