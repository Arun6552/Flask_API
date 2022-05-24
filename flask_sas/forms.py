from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,EqualTo,Email
class RegistrationForm(FlaskForm):
    username = StringField(label='Username',validators=[DataRequired(),Length(min = 3, max = 20 )])
    email = StringField(label='Email',validators=[DataRequired(),Email()])
    password = PasswordField(label='Password',validators=[DataRequired(),Length(min = 5, max = 20 )])
    confirm_password = PasswordField(label='Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField(label='Sign Up',validators=[DataRequired()])

class LoginForm(FlaskForm):
    email = StringField(label='Email',validators=[DataRequired()])
    password = PasswordField(label='Password',validators=[DataRequired()])
    submit = SubmitField(label='Login',validators=[DataRequired()])
    
class ResetRequestForm(FlaskForm):
    email = StringField(label='Email',validators=[DataRequired(),Email()])
    submit = SubmitField(label='Reset Password',validators=[DataRequired()])
    
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(f'that {email.data} does not exists.')
        

class ResetPasswordForm(FlaskForm):
    password = PasswordField(label='Password',validators=[DataRequired(),Length(min = 5, max = 20 )])
    confirm_password = PasswordField(label='Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField(label='Change Password')
    
class AccountUpdateForm(FlaskForm):
    firstname = StringField(label='First Name',validators=[DataRequired(),Length(min = 3, max = 20 )])
    lastname = StringField(label='Last Name',validators=[DataRequired(),Length(min = 3, max = 20 )])
    username = StringField(label='Username',validators=[DataRequired(),Length(min = 3, max = 20 )])
    email = StringField(label='Email',validators=[DataRequired(),Email()])
    picture = FileField(label="Update Profile Picture",validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField(label='Update Account',validators=[DataRequired()])
    
