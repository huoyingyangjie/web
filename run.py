#!flask/bin/python
from app import app,db
from flask import __version__
print "flask version ",__version__
from flask_sqlalchemy import __version__
print "flask_sqlalchemy version ",__version__

app.debug = True
app.run(host='0.0.0.0',port=5001, use_reloader=False)







