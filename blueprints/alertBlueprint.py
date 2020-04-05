from flask import Blueprint,request,url_for,redirect,session
from models.item import Item
from models.alert import Alert
from models.stores import Stores
from models.user import requires_login

from flask import render_template
import json
alertsBp=Blueprint('alertBp',__name__)





@alertsBp.route('/')
@requires_login
def index():
    all = Alert.getMany('user_name',session['n'])
    return render_template('alerts/showalerts.html',a=all)



@alertsBp.route('/add',methods=['POST','GET'])
@requires_login
def addAlert():
    if request.method == 'POST':
        u=request.form.get('url')
        l=request.form.get('limit')
        n=request.form.get('name')
        s=Stores.getByUrl(u)
        i = Item(u,s.tag_name,s.que,s.trim)
        i.load_price()
        i.addToDb()
        a= Alert(n,i._id,float(l),session['n'])
        a.savetodb()
        return "cee ya soon"
    return render_template('alerts/newalert.html')
    


@alertsBp.route('/allAlerts')
@requires_login
def all():
    return render_template('alerts/showalerts.html',a=Alert.all())



@alertsBp.route('/edit/<string:id>',methods=['POST','GET'])
@requires_login
def edit(id):
    a= Alert.getById(id)
    if request.method == 'POST':
        p = request.form.get('p')
        a.updatePriceLimit(float(p))
        return redirect(url_for('alertBp.all'))

    return render_template('alerts/edit.html',a=a)