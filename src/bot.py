from Unsplash import Unsplash
from mastodon import Mastodon
import asyncio
import os
import tweepy as tw
import requests
from datetime import datetime, time, timedelta

class Bot:
    def __init__(self) -> None:
        self.unsplash = Unsplash()
        self.mastodon=Mastodon(access_token=os.getenv("MASTODON_TOKEN"),api_base_url=os.getenv("MASTODON_APP_INSTANCE"))
        
        
        if not os.path.isdir("data"):
            print("Creating history file")
            os.mkdir("data")
        if not os.path.isfile("data/history.txt"):
            with open("data/history.txt","w") as file:
                file.write("")
        """ oauth = tw.OAuthHandler(os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET"))
        oauth.set_access_token(os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_TOKEN_SECRET"))
        self.twitter = tw.API(oauth, wait_on_rate_limit=True) """
        
        
    def run(self):
        print("Starting bot")
        asyncio.run(self.post())
        
    async def wait_until_4pm(self):
        now = datetime.now()
        target_time = time(hour=16)
        target_datetime = datetime.combine(now.date(), target_time)

        if now.time() > target_time:
            target_datetime += timedelta(days=1)

        seconds_left = int((target_datetime - now).total_seconds())
        await asyncio.sleep(seconds_left)


            
    async def post(self):
        while True:
            # Get seconds remaingin until 4pm
            print("Waiting until 4pm")
            await self.wait_until_4pm()
            
            pics=self.unsplash.search_keyword("turtle")
            for x in pics:
                if x.id not in open("data/history.txt").read().splitlines():
                    with open("data/history.txt","a") as file:
                        file.write(x.id)
                        
                    print("Posting "+x.id)
                    # Download pic
                    response = requests.get(x.url, stream=True)
                    
                    media=self.mastodon.media_post(media_file=response.content,mime_type="image/jpeg")
                    self.mastodon.status_post(status=x.url,media_ids=media)
                    
                    #self.twitter.update_status_with_media("Hello World!",pic)
                    break
                else:
                    print("Skipping "+x.id)
            await asyncio.sleep(86400) # 1 day
            
            
            