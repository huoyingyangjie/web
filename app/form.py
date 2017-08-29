from flask_wtf import Form
from wtforms import TextField,BooleanField
from wtforms.validators import DataRequired
from flask_wtf.recaptcha import RecaptchaField

from werkzeug.utils import secure_filename

from flask_wtf.file import FileField

class LoginForm(Form):
    username=TextField('username',validators=[DataRequired()])
    password=TextField('password',validators=[DataRequired()])
    remember_me=BooleanField('remember_me',default=False)
    localization=TextField('localization',default='zh')
    #recaptcha=RecaptchaField()

class UploadForm(Form):
    file=FileField()
