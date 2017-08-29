#created by jiey at 2016.10.27

from app import db
from flask_login import UserMixin

#will add one to many
class User(db.Model, UserMixin):
    __tablename__ ="user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True,nullable=False)
    password = db.Column(db.String(128), unique=True,nullable=False)
    urship=db.relationship('URrelationship',backref=db.backref('users'),lazy="dynamic")

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy import Column,String
#Base = declarative_base()
class Role(db.Model):
    __tablename__="role"
    id=db.Column(db.Integer,primary_key=True)
    rolename=db.Column(db.String(64),unique=True,nullable=False)
    urship = db.relationship('URrelationship', backref=db.backref('roles'), lazy="dynamic")
    rpship = db.relationship('RPrelationship', backref=db.backref('roles'), lazy="dynamic")
    def __init__(self,rolename):
        self.rolename=rolename
    def __repr__(self):
        return '<Role %r>'%self.rolename

class Page(db.Model):
    __tablename__="page"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255),unique=True,nullable=False)
    pagepath=db.Column(db.String(255),unique=True,nullable=False)
    functionDescription=db.Column(db.String(255),unique=True,nullable=False)
    def __init__(self,pagepath,functionDescription):
        self.pagepath=pagepath
        self.functionDescription=functionDescription
    def __repr__(self):
        return '<Page %r %r>'%(self.pagepath,self.functionDescription)

from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint,PrimaryKeyConstraint

class URrelationship(db.Model):#user and role relationship
    __tablename__="urrelationship"
    id = db.Column(db.Integer, primary_key=True)
    userID=db.Column(db.Integer,ForeignKey('user.id'))
    roleID=db.Column(db.Integer,ForeignKey('role.id'))
    __table_args = (UniqueConstraint('userID', 'roleID', name='_userID_roleID_uc'))



    def __init__(self,userID,roleID):
        self.userID=userID
        self.roleID=roleID
    def __repr__(self):
        return "<userID %r , roleID %r "%(self.userID,self.roleID)
class RPrelationship(db.Model):
    __tablename__="rprelationship"
    id = db.Column(db.Integer, primary_key=True)
    roleID=db.Column(db.Integer,ForeignKey('role.id'),unique=True)
    pageTree=db.Column(db.String(255),unique=True,nullable=False)#json
    def __init__(self,roleID,pageTree):
        self.roleID=roleID
        self.pageTree=pageTree
    def __repr__(self):
        return "<role %r , pageTree %r> "%(self.roleID,self.pageTree)

# class permission_collection(db.Model):
#     __tablename__="permission_collection"
#     id=db.Column(db.INTEGER,primary_key=True)
#     target=db.Column(db.String(255),unique=True)
#     display=db.Column(db.Boolean,nullable=False)
#     edit=db.Column(db.Boolean,nullable=False)
#     args=db.Column(db.TEXT)
#     willcheck=db.Column(db.Boolean,nullable=False)
#     #function=db.Column(db.String(255),nullable=False)
#     def __init__(self,target,display,edit,args,willcheck):
#         self.target=target;
#         self.display=display;
#         self.edit=edit;
#         self.args=args;
#         self.willcheck=willcheck;
#         #self.function=function
#
#     def __repr__(self):
#         return "<target=%r>"%(self.target)
class permission_authentication(db.Model):
    __tablename__="permission_authentication"
    __table_args__ = (
        UniqueConstraint('roleID', 'target'),
    )
    id=db.Column(db.INTEGER,primary_key=True)
    roleID=db.Column(db.INTEGER,ForeignKey("role.id"))
    target=db.Column(db.String(255))
    display=db.Column(db.Boolean,nullable=False)
    edit=db.Column(db.Boolean,nullable=False)
    args = db.Column(db.TEXT)
    willcheck=db.Column(db.Boolean,nullable=False)
    def __init__(self,roleID,target,display,edit,args,willcheck):
        self.roleID=roleID;
        self.target=target;
        self.display=display;
        self.edit=edit;
        self.args=args;
        self.willcheck=willcheck

    def __repr__(self):
        return "<id=%s roleID=%s>"%(self.id,self.roleID)


class Investor(db.Model):
    id=db.Column(db.INTEGER,primary_key=True)
    investor_id=db.Column(db.String(255),nullable=False,unique=True)
    def __init__(self,investor_id):
        self.investor_id=investor_id
    def __repr__(self):
        return "investor_id=%s",self.investor_id

    pass

class Investor_prc(db.Model):
    __tablename__="investor_prc"
    id=db.Column(db.INTEGER,primary_key=True);
    investor_id=db.Column(db.String(255),ForeignKey("investor.investor_id"));
    MarginOccupyCheckEnable=db.Column(db.Boolean)# 'off' or 'on'
    MarginPercentValue=db.Column(db.INTEGER)
    PositionCheckEnable=db.Column(db.Boolean)# 'off'  or 'on'
    RejectAllSell=db.Column(db.Boolean) # 'off'  or 'on'
    RejectAllBuy = db.Column(db.Boolean)  # 'off'  or 'on'
    PriceTickCheckEnable = db.Column(db.Boolean)  # 'off'  or 'on'
    PriceRangeCheckEnable = db.Column(db.Boolean)  # 'off'  or 'on'
    RejectInvalidTickSizeEnable = db.Column(db.Boolean)  # 'off'  or 'on'
    RejectInvalidLotSizeEnable = db.Column(db.Boolean)  # 'off'  or 'on'
    QSThrottleEnable = db.Column(db.Boolean)  # 'off'  or 'on'
    QSThrottleInterval = db.Column(db.INTEGER)  # 'off'  or 'on'
    QSOrdersPerInterval = db.Column(db.INTEGER)  # 'off'  or 'on'
    TotalThrottleEnable = db.Column(db.Boolean)  # 'off'  or 'on'
    TotalThrottleInterval=db.Column(db.INTEGER)
    TotalOrdersPerInterval=db.Column(db.INTEGER)
    PriceCheckEnable= db.Column(db.Boolean)
    allowMktOrders= db.Column(db.Boolean)
    RestrictTrading= db.Column(db.Boolean)
    MaxQtyEnable=db.Column(db.Boolean)
    def __init__(self,investor_id,MarginOccupyCheckEnable,MarginPercentValue,PositionCheckEnable,
                 RejectAllSell,RejectAllBuy,PriceTickCheckEnable,PriceRangeCheckEnable,RejectInvalidTickSizeEnable,
                 RejectInvalidLotSizeEnable,QSThrottleEnable,QSThrottleInterval,QSOrdersPerInterval,TotalThrottleEnable,
                 TotalThrottleInterval,TotalOrdersPerInterval,PriceCheckEnable,allowMktOrders,RestrictTrading,MaxQtyEnable):
        self.investor_id=investor_id;
        self.MarginOccupyCheckEnable=MarginOccupyCheckEnable
        self.MarginPercentValue,MarginPercentValue
        self.PositionCheckEnable=PositionCheckEnable
        self.RejectAllSell=RejectAllSell
        self.RejectAllBuy=RejectAllBuy
        self.PriceTickCheckEnable=PriceTickCheckEnable
        self.PriceRangeCheckEnable=PriceRangeCheckEnable
        self.RejectInvalidTickSizeEnable=RejectInvalidTickSizeEnable
        self.RejectInvalidLotSizeEnable=RejectInvalidLotSizeEnable
        self.QSThrottleEnable=QSThrottleEnable
        self.QSThrottleInterval=QSThrottleInterval
        self.QSOrdersPerInterval=QSOrdersPerInterval
        self.TotalThrottleEnable=TotalThrottleEnable
        self.TotalThrottleInterval=TotalThrottleInterval
        self.TotalOrdersPerInterval=TotalOrdersPerInterval
        self.PriceCheckEnable=PriceCheckEnable
        self.allowMktOrders=allowMktOrders
        self.RestrictTrading=RestrictTrading
        self.MaxQtyEnable=MaxQtyEnable

    def __repr__(self):
        return "<id=%s investor_id=%s>"%(self.id,self.investor_id)
class Contract_prc(db.Model):
    __tablename__='contract_prc'
    __table_args__ = (
        UniqueConstraint('investor_id', 'contract_name'),
    )
    id=db.Column(db.INTEGER,primary_key=True)
    investor_id=db.Column(db.String(255),ForeignKey("investor.investor_id"),nullable=False)
    contract_name=db.Column(db.String(255),nullable=False)
    BuyPositionLimit=db.Column(db.INTEGER,nullable=False)
    CancelTimesLimit=db.Column(db.INTEGER,nullable=False)
    LotSize=db.Column(db.INTEGER,nullable=False)
    MinPriceRangeLimit=db.Column(db.INTEGER,nullable=False)
    OpenOrderLimit=db.Column(db.INTEGER,nullable=False)
    def __init__(self,investor_id,contract_name,BuyPositionLimit,CancelTimesLimit,LotSize,MinPriceRangeLimit,OpenOrderLimit):
        self.investor_id=investor_id
        self.contract_name=contract_name
        self.BuyPositionLimit=BuyPositionLimit
        self.CancelTimesLimit=CancelTimesLimit
        self.LotSize=LotSize
        self.MinPriceRangeLimit=MinPriceRangeLimit
        self.OpenOrderLimit=OpenOrderLimit
    def __repr__(self):
        return " id=%d,investor_id=%s,contract_name=%s"%(self.id,self.investor_id,self.contract_name)
from sqlalchemy.dialects.mysql import DOUBLE
class Capital_account_info(db.Model):
    __tablename__="captial_account_info"
    id=db.Column(db.INTEGER,primary_key=True)
    investor_id=db.Column(db.String(255),ForeignKey("investor.investor_id"),nullable=False)
    StaticRightsAndInterests=db.Column(DOUBLE,nullable=False)
    CloseGainAndLoss=db.Column(DOUBLE,nullable=False)
    PositionGainAndLoss=db.Column(DOUBLE,nullable=False)
    DynamicRightsAndInterests=db.Column(DOUBLE,nullable=False)
    UsedMargin=db.Column(DOUBLE,nullable=False)
    ForzenMargin=db.Column(DOUBLE,nullable=False)
    ServiceFee=db.Column(DOUBLE,nullable=False)
    ForzenServiceFee=db.Column(DOUBLE,nullable=False)
    AvailableCaptial=db.Column(DOUBLE,nullable=False)
    Debit=db.Column(DOUBLE,nullable=False)
    Deposit=db.Column(DOUBLE,nullable=False)
    RiskDegree=db.Column(DOUBLE(6,2),nullable=False)
    def __init__(self,investor_id,StaticRightsAndInterests,CloseGainAndLoss,PositionGainAndLoss,DynamicRightsAndInterests
                 ,UsedMargin,ForzenMargin ,ServiceFee,ForzenServiceFee,AvailableCaptial,Debit,Deposit,RiskDegree):
        self.investor_id=investor_id
        self.StaticRightsAndInterests=StaticRightsAndInterests
        self.CloseGainAndLoss=CloseGainAndLoss
        self.PositionGainAndLoss=PositionGainAndLoss
        self.DynamicRightsAndInterests=DynamicRightsAndInterests
        self.UsedMargin=UsedMargin
        self.ForzenMargin=ForzenMargin
        self.ServiceFee=ServiceFee
        self.ForzenServiceFee=ForzenServiceFee
        self.AvailableCaptial=AvailableCaptial
        self.Debit=self.Debit
        self.Deposit=Deposit
        self.RiskDegree=RiskDegree
    def __repr__(self):
        return "id=%d,investor_id=%s"%(self.id,self.investor_id)








