from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@mysql:3306/blog'
app.config['SECRET_KEY']='8743920ee3253c05851680ffaa26e6dd'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager=LoginManager(app)
login_manager.login_view = 'login'

from application import routes
