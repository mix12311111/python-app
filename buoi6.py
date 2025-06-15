import json
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
     