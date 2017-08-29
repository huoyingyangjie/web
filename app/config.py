import os
basedir=os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:Accelecom.123@localhost:3306/Xprc"
SQLALCHEMY_TRACK_MODIFICATIONS = False
CSRF_ENABLED = True
SECRET_KEY = 'you will never guess'
RECAPTCHA_PUBLIC_KEY = '6Ld02QoUAAAAALsjJNX01gUGVxJbCGgIOqs9xrwn'
RECAPTCHA_PRIVATE_KEY = '6Ld02QoUAAAAAOmbekb87DmGz84k1LoZ1j0KGs5q'

pageTree=[
    [{}]

]
