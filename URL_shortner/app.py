import os
from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy #flask db init
from flask_migrate import Migrate #flask db migrate -m "first migration"
import pyshorteners


app=Flask(__name__)

###################################SQL ALCHEMY#########################################################
basedir=os.path.abspath(os.path.dirname(__file__)) 
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
Migrate(app,db)

app=Flask(__name__)

###################################SQL ALCHEMY#########################################################
basedir=os.path.abspath(os.path.dirname(__file__)) 
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
Migrate(app,db)


@app.before_first_request
def create_tables():
    db.create_all()

class Urls(db.Model):
    id_ = db.Column("id_", db.Integer, primary_key=True)
    url_recieved = db.Column("long", db.String())
    short_url = db.Column("short", db.String(20))
###############------------------Create a Model----------------################################################################
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/result',methods=["GET","POST"])
def result():
    url_recieved=request.form['url']
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url_recieved)
    url = Urls(url_recieved=url_recieved, short_url=short_url)
    db.session.add(url)
    db.session.commit()
    return render_template("home.html",short_url=short_url)

@app.route('/preurls')
def pre_urls():
    Pre_urls = Urls.query.all()
    return render_template('previous_url.html', Pre_urls=Pre_urls)



if __name__=="__main__":
    
    app.run(debug=True)
