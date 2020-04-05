from models.item import Item
import uuid
from common.db import DB
from common.utils import Utils
from dataclasses import dataclass,field
import re
from typing import Callable
from flask import session,flash,redirect,url_for,request
import functools


@dataclass(eq=False)
class User(object):

    collection: str = field(init=False,default="users")
    name :str
    pwd :str
    _id:    str = field(default_factory=lambda:uuid.uuid4().hex)



    def json(self):
       return{
            "_id":self._id,
            "name":self.name,
            "pwd":self.pwd,
       }

    @classmethod
    def getByName(cls,n):
        try:
            return cls.findOne("name",n)
        except:
            raise AttributeError("user not found")


    @classmethod
    def findOne(cls,k,v):
        return cls(**DB.find_one(cls.collection,{k:v}))

    def savetodb(self):
        DB.insert(self.collection,self.json())

    @classmethod
    def reg(cls,n,p):
        if not Utils.valid_email(n):
            raise Exception("invalid username")
        try:
            cls.getByName(n)
            return False
            #raise Exception("user already exists")
        except AttributeError as a:
            User(n,Utils.encry(p)).savetodb()
            print('regestered')
            return True

        
    
    @classmethod
    def validLogin(cls,n,p):
        if not Utils.valid_email(n):
            raise Exception("invalid username")
        try:
            c=cls.getByName(n)
            return Utils.check(p,c.pwd)
            #raise Exception("user already exists")
        except AttributeError as a:
            return False


  
    
    


def requires_login(f):
    @functools.wraps(f)
    def decorated_fn(*args,**kwargs):
        if not session.get('n'):
            flash('you need to signin','danger')
            return redirect(url_for("usersBp.login"))
        return f(*args,**kwargs)
    return decorated_fn