from Unsplash import Unsplash
from mastodon import Mastodon
import asyncio
import os
import tweepy as tw
import requests
class Bot:
    def __init__(self) -> None:
        self.unsplash = Unsplash()
        self.mastodon=Mastodon(access_token=os.getenv("MASTODON_TOKEN"),api_base_url=os.getenv("MASTODON_APP_INSTANCE"))
        
        """ oauth = tw.OAuthHandler(os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET"))
        oauth.set_access_token(os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_TOKEN_SECRET"))
        self.twitter = tw.API(oauth, wait_on_rate_limit=True) """
        
        
    def run(self):
        asyncio.run(self.post())
            
    async def post(self):
        while True:
        
            pic=self.unsplash.search_keyword("turtle")[0]
            
            # Download pic
            response = requests.get(pic.url, stream=True)
            
            media=self.mastodon.media_post(media_file=response.content,mime_type="image/jpeg")
            self.mastodon.status_post(status=pic.url,media_ids=media)
            
            #self.twitter.update_status_with_media("Hello World!",pic)
            await asyncio.sleep(3600) # 1 hour