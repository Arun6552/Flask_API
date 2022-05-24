from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisfirstflask'  ###csrf token--form(hidden.tags)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/cjflask.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhostname:port'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cjpostgres:root@localhost:5432/cjflaskapp'


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'arunchaudhary6552@gmail.com'
app.config['MAIL_PASSWORD'] = 'Arun12345!@#$%'

mail = Mail(app)

from flask_sas import routes