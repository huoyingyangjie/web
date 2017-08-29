# -*- coding: utf-8 -*-
import traceback
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI,SQLALCHEMY_TRACK_MODIFICATIONS
from flask_login import LoginManager,AnonymousUserMixin

app = Flask(__name__) #创建Flask application对象
app.config.from_object('app.config')
db=SQLAlchemy(app)
lm=LoginManager()
lm.init_app(app)
lm.login_view='login'
lm.login_message='Please login in'
lm.login_message_category='info'
lm.anonymous_user=AnonymousUserMixin
lm.session_protection='strong'
lm.refresh_view='login'
lm.needs_refresh_message='Please enter your info'
lm.needs_refresh_message_category="refresh_info"



from models import User

from app import ctarget

ctarget.ctarget_response(ctarget.ctarget.ctarget_dict);


from app import views   #引入视图，还没实现
