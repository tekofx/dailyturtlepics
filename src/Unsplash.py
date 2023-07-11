import os 
import requests

BASE_URL="https://api.unsplash.com/"

class Photo:
    def __init__(self, id, url, width, height):
        self.id = id
        self.url = url
        self.width = width
        self.height = height
        
    def __repr__(self) -> str:
        return f"Photo(id={self.id}, url={self.url}, width={self.width}, height={self.height})"


class Unsplash:
    def __init__(self) -> None:
        self.client_id = os.getenv("UNSPLASH_ACCESS_KEY")
        

    def search_keyword(self, keyword)->list[Photo]:
        url = BASE_URL + "search/photos?query=" + keyword + "&client_id=" + self.client_id
        response = requests.get(url)
        json_data = response.json()
        output=[]
        for photo in json_data["results"]:
            output.append(Photo(photo["id"],photo["urls"]["regular"],photo["width"],photo["height"]))
        return output
        
