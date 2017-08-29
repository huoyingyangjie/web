import sqlalchemy as sa
from app import db,models

investor=models.Investor("jack")
db.session.add(investor)
db.session.commit()
contracts=models.Contract_prc("jack","ag1708",1,2,3,4,5)

db.session.add(contracts)
db.session.commit()

root = models.User('root', '123456')
db.session.add(root)
db.session.commit()

investor=models.Investor("yangjie")
db.session.add(investor)
db.session.commit()

contracts=models.Contract_prc("yangjie","ag1709",1,2,3,4,5)

db.session.add(contracts)
db.session.commit()