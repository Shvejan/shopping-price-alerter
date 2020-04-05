from flask import Blueprint,request,session,redirect,url_for
from models.item import Item
from models.alert import Alert
from models.stores import Stores
from models.user import User    


from flask import render_template
import json
usersBp=Blueprint('usersBp',__name__)

@usersBp.route('/',methods=['POST','GET'])
def reg():
    if request.method == 'POST':
        n=request.form.get('name')
        p=request.form.get('pwd')

        try:
            r=User.reg(n,p)
            if not r:
                raise Exception
            session['n']=n
        except Exception as e:
            return 'user already exists'
        return session['n']

    return render_template('users/reg.html')
    



@usersBp.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        n=request.form.get('name')
        p=request.form.get('pwd')

        try:
            if (User.validLogin(n,p)) :
                session['n']=n
                #return session['n']
                return redirect(url_for('alertBp.index'))
            else:
                return "user data wrong"
        except Exception as e:
            return "user data invalid"

    return render_template('users/login.html')
    

@usersBp.route('/logout')
def logout():
    session['n']=None
    return "loggedout"