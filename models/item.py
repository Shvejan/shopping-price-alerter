from bs4 import BeautifulSoup
import requests
import uuid
from common.db import *
from dataclasses import dataclass,field
@dataclass(eq=False)
class Item(object):
    collection:str = field(init=False,default="items")
    url :str
    tag:str
    que :dict
    trim :int
    price : float =field(default=None)
    _id:str = field(default_factory=lambda :uuid.uuid4().hex)


    def __reper__(self):
        return f"<Item {self.url}>"

    def load_price(self):
        req=requests.get(self.url)
        cont=req.content
        s=BeautifulSoup(cont,"html.parser")
        e=s.find(self.tag,self.que)
        x=(e.text.strip()[self.trim:].replace(",",""))
        self.price = float(x)
        return self.price

    def json(self):
        return {
            "_id":self._id,
            "url":self.url,
            "tag":self.tag,
            "que":self.que,
            'trim':self.trim,
            'price':self.price
        }
    
    def addToDb(self):
        DB.insert(self.collection,self.json())


    @classmethod
    def getById(cls,id):
        x=DB.find_one("items",{'_id':id})
        return cls(**x)

    @classmethod
    def all(cls):
        allItems = DB.find(cls.collection,{})
        return [cls(**i) for i in allItems]


