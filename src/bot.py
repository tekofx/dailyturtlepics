from Unsplash import Unsplash
from mastodon import Mastodon
import asyncio
import os

class Bot:
    def __init__(self) -> None:
        self.unsplash = Unsplash()
        self.mastodon=Mastodon(access_token=os.getenv("MASTODON_TOKEN"),api_base_url=os.getenv("MASTODON_APP_INSTANCE"))
        
        
    def run(self):
        asyncio.run(self.post())
            
    async def post(self):
        
        pic=self.unsplash.search_keyword("turtle")
        
        self.mastodon.status_post("Hello World!")
        await asyncio.wait(3600) # 1 hour