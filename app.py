from flask import Flask,render_template,request,session,redirect,url_for
from blueprints.alertBlueprint import alertsBp
from blueprints.storesBlueprint import storesBp
from blueprints.usersBlueprint import usersBp

app = Flask(__name__)
app.secret_key="adsfadad"


app.register_blueprint(alertsBp,url_prefix = '/alerts')
app.register_blueprint(storesBp,url_prefix = '/stores')
app.register_blueprint(usersBp,url_prefix = '/')


app.secret_key="adsfadad"















if __name__== '__main__':
    app.run(debug=True)
