from models.item import Item
from models.user import User

import uuid
from common.db import DB
from dataclasses import dataclass,field

@dataclass(eq=False)
class Alert(object):

    collection: str = field(init=False,default="alerts")
    name:str
    item_id :str
    priceLimit:float
    user_name:str
    _id:    str = field(default_factory=lambda:uuid.uuid4().hex)



    def __post_init__(self):
        self.item = Item.getById(self.item_id)
        self.user=User.getByName(self.user_name)
    
    def json(self):
        return {
            'name':self.name,
            "item_id":self.item_id,
            'priceLimit':self.priceLimit,
            'user_name':self.user_name,
            '_id':self._id
        }
    
    def savetodb(self):
        DB.insert(self.collection,self.json())
    


    def load_item_price(self):
        return self.item.load_price()

    def notify_if_pdrop(self):
        if self.item.price <= self.priceLimit:
            return("pricedropalert")
        else:
            return("cheapoo")

    def updatePriceLimit(self,p):
        DB.update(self.collection,{'_id': self._id},{'name':self.name,"item_id":self.item_id,'priceLimit':p,'_id':self._id})
    
    @classmethod
    def all(cls):
        allalerts = DB.find(cls.collection,{})
        return [cls(**i) for i in allalerts]


    @classmethod
    def getMany(cls,k,v):
        allalerts = DB.find(cls.collection,{k:v})
        return [cls(**i) for i in allalerts]



    @classmethod
    def getById(cls,id):
        x=DB.find_one(cls.collection,{'_id':id})
        return cls(**x)