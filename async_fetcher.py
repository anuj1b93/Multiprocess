import aiohttp
import asyncio

class AsyncFetcher:
    def __init__(self, urls):
        self.urls = urls
    
    # fetch HTML content from a website
    async def fetch_html(self,session, url):
        async with session.get(url) as response:
            return await response.text()

    # fetch content from multiple URLs asynchronously
    async def fetch_all(self):
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_html(session , url) for url in self.urls]
            return await asyncio.gather(*tasks)
