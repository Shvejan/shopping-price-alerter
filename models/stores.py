from models.item import Item
import uuid
from common.db import DB
from dataclasses import dataclass,field
import re

@dataclass(eq=False)
class Stores(object):

    collection: str = field(init=False,default="stores")
    name :str
    url_prefix :str
    tag_name:str
    que :dict
    trim :int
    _id:    str = field(default_factory=lambda:uuid.uuid4().hex)



    def json(self):
       return{
            "_id":self._id,
            "name":self.name,
            "url_prefix":self.url_prefix,
            "tag_name":self.tag_name,
            "que":self.que,
            'trim':self.trim

       }

    @classmethod
    def getByName(cls,n):
        return cls.findOne("name",n)

    @classmethod
    def getByUrlPref(cls,u):
        reg = {'$regex':"^{}".format(u)}
        return cls.findOne("url_prefix",reg)

    @classmethod
    def findOne(cls,k,v):
        return cls(**DB.find_one(cls.collection,{k:v}))

    def savetodb(self):
        DB.insert(self.collection,self.json())

    @classmethod
    def getById(cls,id):
        x=DB.find_one(cls.collection,{'_id':id})
        return cls(**x)

    @classmethod
    def findMany(cls,k,v):
        x=DB.find(cls.collection,{k:v})
        return [cls(**i) for i in x]
    
    @classmethod
    def all(cls):
        x=DB.find(cls.collection,{})
        return [cls(**i) for i in x]
    
    @classmethod
    def getByUrl(cls,u):
        pattern = re.compile(r'(https?://.*?/)')
        match = pattern.search(u)
        uP=match.group(1)
        return cls.getByUrlPref(uP)