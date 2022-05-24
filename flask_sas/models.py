from flask_login import UserMixin
from  flask_sas import db,login_manager,app
from datetime import datetime
from flask_login import UserMixin
from flask import redirect,url_for
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)  ## handle user session 

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('signup'))
class User(db.Model,UserMixin):              #UserMixin--Authentication
    id  = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    image_filename = db.Column(db.String(20),nullable=False,default='default.jpg')
    password = db.Column(db.String(60),nullable=False)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)
    details = db.relationship('UserDetails',backref='parent',lazy=True)
    ##Reset Password token
    def get_token(self,expires_sec=300):
        serial =Serializer(app.config['SECRET_KEY'],expires_in=expires_sec)
        return serial.dumps({'user_id':self.id}).decode('utf-8')

    @staticmethod
    def verify_token(token):
        serial = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = serial.loads(token)['user_id']   ###check used exist or not.
        except:
            None
        return User.query.get(user_id)

    def __repr__(self):
        return f'{self.username} : {self.email} : {self.date_created.strftime("%d/%m/%Y, %H:%M:%S")}'
    
class UserDetails(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20),unique=True,nullable=False)
    lastname = db.Column(db.String(20),unique=True,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    def __repr__(self):
        return f'{self.firstname} : {self.lastname}'