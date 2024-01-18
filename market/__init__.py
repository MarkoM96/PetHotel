from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

#--------------------------------------------------------------------------------------------
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db' #ovo je iz tekst.txt fajla, ako ne radi samo nek ostan market.db

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(project_root, 'instance', 'market.db') ---project_root moram da podesim,nisam probao da li ovo radi
# app.config znaci da flask prepoznaje bazu podataka i da je popuni sa ovim informacijama i nazove market.db
app.config['SECRET_KEY'] = '9dbfb7a880122be9718a2a57'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
app.app_context().push() 
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
from market import routes 

#--------------------------------------------------------------------------------------------

# da bi pokretali server sa python run.py - moramo u ovom fajlu imati importovane -routes- da bi python prvo
# pokrenuo taj fajl, nakon toga server ce raditi kako treba, ali moramo imati definisano dole -app- 
# da bi python znao sta je flask klasa a sta baza podataka

db.create_all() # <-- Add this line to create the tables in the database