from flask import Blueprint,request
from models.item import Item
from models.alert import Alert
from models.stores import Stores

from flask import render_template
import json
storesBp=Blueprint('storesBp',__name__)

@storesBp.route('/',methods=['POST','GET'])
def addStore():
    if request.method == 'POST':
        n=request.form.get('name')
        u=request.form.get('url')
        ta=request.form.get('tag')
        i=request.form.get('identifier')
        p=request.form.get('property_name')
        t=int(request.form.get('trim'))
        Stores(n,u,ta,{i:p},t).savetodb()
        
        return "added"
    return render_template('stores/addStore.html')
    

