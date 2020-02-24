from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

## App Configritions
app = Flask(__name__)
# secret key to protect request and cookie
app.config["SECRET_KEY"] = "7ed7af258021a392ccbeae22481be085"
# utilize db
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from music_main import routes
