[
    {
        "id": 1,
        "title": "Naruto",
        "release_date": "2002-10-03",
        "image": null,
        "rating": 8.9,
        "link": null
    },
    {
        "id": 2,
        "title": "One Piece",
        "release_date": "1999-10-20",
        "image": null,
        "rating": 8.9,
        "link": null
    },
    {
        "id": 3,
        "title": "Dragon Ball Z",
        "release_date": "1989-10-28",
        "image": null,
        "rating": 8.9,
        "link": null
    }
]
import json

def load_json_data():
    anime_dict_data = list()
    with open ("data.json","r") as json_in:
        json_data = json.load(json_in)
    anime_dict_data.extend(json_data)
    return anime_dict_data

def write_json_data(json):
    with open("data.json",w) as json_out:
        json.dump(json_data,json_out)
class AnimeItem:
     def __init__(self,id,name,release_dae,rating=None,link=None,image = None):
         self.name= name
         self.id = id
         self.rating = rating
         self.link = link
         self.release = release_dae
         self.image = image

def update(self,newdata:dict):
     for key ,value in newdata.items():
          if value
            setattr(self,key,value)

def __str__(self):
         return f"Title:{self.title}\nRelease date: {self.release_date}\nRating: {self.rating}\nLink :{self.link}"

anime1 = AnimeItem(1,"naruto")
with open("data.json","a")as f :
     data = json.dump(anime1.__dict__,f)
     

class AnimeDatabase:
    def load_data(self):
        self.animeList = load_json_data("data.json")
    
    def save_data(self):
        write_json_data("data.json",self.animeList)
        
    def load_data(self):
        self.animeList = load_json_data("data.json")
    
    def get_by_id(self,id):
        animeList = self.load_data()
        for anime in animeList:
            if anime.id == id:
                return anime
            
    def add_item(self,anime):
        

