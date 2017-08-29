from flask import render_template
from models import  User,Role,Contract_prc,Investor
import app

class xpage():
    page_url={}
    @classmethod
    def route(cls,url,f,*args,**kwargs):
        cls.page_url[url]=f
        return f;



def usermg_view_add():
    return render_template("rightlistmg/usermg/view/add.html")

def usermg_view_delete():

    return render_template("rightlistmg/usermg/view/delete.html");
def usermg_view_modify():
    return render_template("rightlistmg/usermg/view/modify.html")

class C_usermg_view:
    url="rightlistmg/usermg/view.html"
    css_urls=[]
    js_urls=[]
    def render(self,):
        users = User.query.all()
        add = usermg_view_add()
        delete = usermg_view_delete()
        modify = usermg_view_modify()
        return render_template(self.url, users=users, add=add, delete=delete, modify=modify);
        pass
def usermg_view():
    users = User.query.all()
    add=usermg_view_add()
    delete=usermg_view_delete()
    modify=usermg_view_modify()
    return render_template("usermg/view.html",users=users,add=add,delete=delete,modify=modify);
    pass


class C_rightlistmg_rolemg_view_add():
    url="rightlistmg/rolemg/view/add.html"
    def render(self):
        return render_template(self.url)

class C_rightlistmg_rolemg_view_delete():
    url="rightlistmg/rolemg/view/delete.html"
    def render(self):
        return render_template(self.url)

class C_rightlistmg_rolemg_view_modify():
    url="rightlistmg/rolemg/view/modify.html"
    def render(self,):
        return render_template(self.url)

class C_rightlistmg_rolemg_view():
    url="rightlistmg/rolemg/view.html"
    css_urls = []
    js_urls = []
    def render(self,):
        roles=Role.query.all()
        add=C_rightlistmg_rolemg_view_add().render();
        delete=C_rightlistmg_rolemg_view_delete().render()
        modify=C_rightlistmg_rolemg_view_modify().render();
        return render_template(self.url,roles=roles,add=add,delete=delete,modify=modify)

class C_rightlistmg_prcmg_speculation_investorprc_MarginOccupyCheckEnable():
    url="rightlistmg/prcmg/speculation/investorprc/MarginOccupyCheckEnable.html"
    def render(self):
        return render_template(self.url)




class C_rightlistmg_prcmg_speculation_investorprc_MarginPercentValue():
    url="rightlistmg/prcmg/speculation/investorprc/MarginPercentValue.html"
    def render(self):
        return render_template(self.url)


class C_rightlistmg_prcmg_speculation_investorprc_PositionCheckEnable():
    url="rightlistmg/prcmg/speculation/investorprc/PositionCheckEnable.html"
    def render(self):
        return render_template(self.url)




class C_rightlistmg_prcmg_speculation_investorprc_RejectAllBuy():
    url="rightlistmg/prcmg/speculation/investorprc/RejectAllBuy.html"
    def render(self):
        return render_template(self.url)



class C_rightlistmg_prcmg_speculation_investorprc_RejectAllSell():
    url="rightlistmg/prcmg/speculation/investorprc/RejectAllSell.html"
    def render(self):
        return render_template(self.url)
class C_rightlistmg_prcmg_speculation_investorprc_PriceTickCheckEnable():
    url="rightlistmg/prcmg/speculation/investorprc/PriceTickCheckEnable.html"
    def render(self):
        return render_template(self.url)

class C_prcmg_speculation_investorprc:
    url="rightlistmg/prcmg/speculation/investor_prc.html";
    css_urls = []
    js_urls = []
    def render(self,):
        MarginOccupyCheckEnable = C_rightlistmg_prcmg_speculation_investorprc_MarginOccupyCheckEnable().render();
        MarginPercentValue = C_rightlistmg_prcmg_speculation_investorprc_MarginPercentValue().render();
        PositionCheckEnable = C_rightlistmg_prcmg_speculation_investorprc_PositionCheckEnable().render();
        RejectAllBuy = C_rightlistmg_prcmg_speculation_investorprc_RejectAllBuy().render();
        RejectAllSell = C_rightlistmg_prcmg_speculation_investorprc_RejectAllSell().render();
        PriceTickCheckEnable = C_rightlistmg_prcmg_speculation_investorprc_PriceTickCheckEnable().render();
        return render_template(self.url,
                               MarginOccupyCheckEnable=MarginOccupyCheckEnable,
                               MarginPercentValue=MarginPercentValue,
                               PositionCheckEnable=PositionCheckEnable,
                               RejectAllBuy=RejectAllBuy,
                               RejectAllSell=RejectAllSell,
                               PriceTickCheckEnable=PriceTickCheckEnable,
                               )




class C_prcmg_speculation_contractprc_contract():
    url="rightlistmg/prcmg/speculation/contractprc/contract.html"
    def render(self,):

        contracts=Contract_prc.query.all()
        print type(contracts)
        return render_template(self.url,contracts=contracts)

class C_prcmg_speculation_contractprc_prc_prcitem_BuyPositionLimit():
    url="rightlistmg/prcmg/speculation/contractprc/prcitem/BuyPositionLimit.html"
    def render(self,):

        return render_template(self.url,)
class C_prcmg_speculation_contractprc_prc_prcitem_CancelTimesLimit():
    url="rightlistmg/prcmg/speculation/contractprc/prcitem/CancelTimesLimit.html"
    def render(self,):
        return render_template(self.url)
class C_prcmg_speculation_contractprc_prc_prcitem_LotSize():
    url="rightlistmg/prcmg/speculation/contractprc/prcitem/LotSize.html"
    def render(self,):
        return render_template(self.url)

class C_prcmg_speculation_contractprc_prc_prcitem_MinPriceRangeLimit():
    url="rightlistmg/prcmg/speculation/contractprc/prcitem/MinPriceRangeLimit.html"
    def render(self,):
        return render_template(self.url)
class C_prcmg_speculation_contractprc_prc_prcitem_OpenOrderLimit():
    url="rightlistmg/prcmg/speculation/contractprc/prcitem/OpenOrderLimit.html"
    def render(self,):
        return render_template(self.url)
class C_prcmg_speculation_contractprc_prc_prcitem_SellPositionLimit():
    url="rightlistmg/prcmg/speculation/contractprc/prcitem/SellPosition.html"
    def render(self,):
        return render_template(self.url)



class C_prcmg_speculation_contractprc_prc():
    url="rightlistmg/prcmg/speculation/contractprc/prc.html"
    def render(self):
        BuyPositionLimit=None
        CancelTimesLimit=None
        LotSize=None
        MinPriceRangeLimit=None
        OpenOrderLimit=None
        SellPositionLimit=None
        BuyPositionLimit=C_prcmg_speculation_contractprc_prc_prcitem_BuyPositionLimit().render();
        CancelTimesLimit=C_prcmg_speculation_contractprc_prc_prcitem_CancelTimesLimit().render();
        LotSize=C_prcmg_speculation_contractprc_prc_prcitem_LotSize().render();
        MinPriceRangeLimit=C_prcmg_speculation_contractprc_prc_prcitem_MinPriceRangeLimit().render();
        OpenOrderLimit=C_prcmg_speculation_contractprc_prc_prcitem_OpenOrderLimit().render();
        SellPositionLimit=C_prcmg_speculation_contractprc_prc_prcitem_SellPositionLimit();

        return render_template(self.url,
                               BuyPositionLimit=BuyPositionLimit,
                               CancelTimesLimit=CancelTimesLimit,
                               LotSize=LotSize,
                               MinPriceRangeLimit=MinPriceRangeLimit,
                               OpenOrderLimit=OpenOrderLimit,
                               SellPositionLimit=SellPositionLimit,
                               )

class C_prcmg_speculation_contractprc:
    url="rightlistmg/prcmg/speculation/contract_prc.html"
    css_urls = []
    js_urls = []
    def render(self,):
        prc=None
        contract=None
        prc=C_prcmg_speculation_contractprc_prc().render();
        contract=C_prcmg_speculation_contractprc_contract().render();
        return render_template(self.url,prc=prc,contract=contract)


from app.models import  Capital_account_info
class C_rightlistmg_trading_tradinginfo:
    url="rightlistmg/trading/tradinginfo.html"
    css_urls = ["/static/vendor/jqueryui/css/smoothness/jquery-ui-1.9.2.custom.css","/static/vendor/pqgrid/pqgrid.dev.css"]
    js_urls = ["/static/js/xele/common.js","/static/vendor/sort/timsort.js","/static/vendor/jqueryui/js/jquery-ui-1.9.2.custom.js","/static/vendor/pqgrid/pqgrid.dev.js"
                ,"/static/js/xele/longpolling.js",
               "/static/js/xele/tradinginfo.js"]
    def render(self):

        return render_template(self.url)
class C_rightlistmg_trading_allorder:

    url="rightlistmg/trading/allorder.html"
    css_urls = []
    js_urls = []
    def render(self):
        return render_template(self.url)
class C_right_html:
    url="right_html.html"
    css_urls=[]
    js_urls=[]
    def render(self,active_url):
        rightlistmg_usermg=None;
        rightlistmg_prcmg_investor_prc=None
        rightlistmg_prcmg_contract_prc=None
        rightlistmg_rolemg_view=None
        rightlistmg_trading_tradinginfo=None
        rightlistmg_trading_allorder=None
        if(active_url==C_usermg_view.url):
            print "active_url %s"%active_url
            O_usermg_view=C_usermg_view()
            rightlistmg_usermg=O_usermg_view.render();
            self.css_urls.extend(O_usermg_view.css_urls)
            self.js_urls.extend(O_usermg_view.js_urls)
        if(active_url==C_prcmg_speculation_investorprc.url):
            O_prcmg_speculation_investorprc=C_prcmg_speculation_investorprc()
            rightlistmg_prcmg_investor_prc=O_prcmg_speculation_investorprc.render();
            self.css_urls.extend(O_prcmg_speculation_investorprc.css_urls);
            self.js_urls.extend(O_prcmg_speculation_investorprc.js_urls)
        if(active_url==C_prcmg_speculation_contractprc.url):
            O_prcmg_speculation_contractprc=C_prcmg_speculation_contractprc()
            rightlistmg_prcmg_contract_prc=O_prcmg_speculation_contractprc.render();
            self.css_urls.extend(O_prcmg_speculation_contractprc.css_urls)
            self.js_urls.extend(O_prcmg_speculation_contractprc.js_urls)
        if(active_url==C_rightlistmg_rolemg_view.url):
            O_rightlistmg_rolemg_view=C_rightlistmg_rolemg_view()
            rightlistmg_rolemg_view=O_rightlistmg_rolemg_view.render();
            self.css_urls.extend(O_rightlistmg_rolemg_view.css_urls)
            self.js_urls.extend(O_rightlistmg_rolemg_view.js_urls)
        if(active_url==C_rightlistmg_trading_tradinginfo.url):
            O_rightlistmg_trading_tradinginfo=C_rightlistmg_trading_tradinginfo()
            rightlistmg_trading_tradinginfo=O_rightlistmg_trading_tradinginfo.render();
            self.css_urls.extend(O_rightlistmg_trading_tradinginfo.css_urls)
            self.js_urls.extend(O_rightlistmg_trading_tradinginfo.js_urls)
        if(active_url==C_rightlistmg_trading_allorder.url):
            O_rightlistmg_trading_allorder=C_rightlistmg_trading_allorder()
            rightlistmg_trading_allorder=O_rightlistmg_trading_allorder.render()
            self.css_urls.extend(O_rightlistmg_trading_allorder.css_urls)
            self.js_urls.extend(O_rightlistmg_trading_allorder.js_urls)
        return render_template(self.url,
                               rightlistmg_usermg=rightlistmg_usermg,
                               rightlistmg_prcmg_investor_prc=rightlistmg_prcmg_investor_prc,
                               rightlistmg_prcmg_contract_prc=rightlistmg_prcmg_contract_prc,
                               rightlistmg_rolemg_view=rightlistmg_rolemg_view,
                               rightlistmg_trading_tradinginfo=rightlistmg_trading_tradinginfo,
                               rightlistmg_trading_allorder=rightlistmg_trading_allorder,
                               )


class C_leftlistmg_dashboard():
    url="leftlistmg/dashboard.html"
    def render(self):
        return render_template(self.url)

class C_leftlistmg_usermg_view():
    url="leftlistmg/usermg/view.html"
    def render(self):
        return render_template(self.url)
class C_leftlistmg_usermg_create():
    url="leftlistmg/usermg/create.html"
    def render(self):
        return render_template(self.url)
class C_leftlistmg_usermg():
    url="leftlistmg/usermg.html"
    def render(self,):
        usermg_view=C_leftlistmg_usermg_view().render();
        usermg_create=C_leftlistmg_usermg_create().render();
        return render_template(self.url,usermg_view=usermg_view,usermg_create=usermg_create)


class C_leftlistmg_prcmg_session_investor_dce_contract():
    url="leftlistmg/prcmg/session/investor/dce/contract.html"
    def render(self):
        return render_template(self.url)

class C_leftlistmg_prcmg_session_investor_dce_prc():
    url="leftlistmg/prcmg/session/investor/dce/prc.html"
    def render(self):

        return render_template(self.url)


class C_leftlistmg_prcmg_session_investor_dce():
    url="leftlistmg/prcmg/session/investor/dce.html"
    def render(self,):

        prc=None
        contract=None

        prc=C_leftlistmg_prcmg_session_investor_dce_prc().render();
        contract=C_leftlistmg_prcmg_session_investor_dce_contract().render();
        return render_template(self.url,prc=prc,contract=contract)

class C_leftlistmg_prcmg_session_investor():
    url="leftlistmg/prcmg/session/investor.html"
    def render(self,):
        investors = Investor.query.all()
        dce=C_leftlistmg_prcmg_session_investor_dce().render();
        return render_template(self.url,investors=investors,dce=dce)

class C_leftlistmg_prcmg_session():
    url="leftlistmg/prcmg/session.html"
    def render(self):
        investor = C_leftlistmg_prcmg_session_investor().render();

        return render_template(self.url,investor=investor)

class C_leftlistmg_prcmg():
    url="leftlistmg/prcmg.html"
    def render(self,):
        session=C_leftlistmg_prcmg_session().render();
        return render_template(self.url,session=session)
class C_leftlistmg_rolemg_view():
    url="leftlistmg/rolemg/view.html"
    def render(self):
        return render_template(self.url)
class C_leftlistmg_rolemg_create():
    url="leftlistmg/rolemg/create.html"
    def render(self):
        return render_template(self.url)
class C_leftlistmg_rolemg():
    url="leftlistmg/rolemg.html"
    def render(self,):
        rolemg_view=C_leftlistmg_rolemg_view().render();
        rolemg_create=C_leftlistmg_rolemg_create().render();
        return render_template(self.url,rolemg_view=rolemg_view,rolemg_create=rolemg_create)


class C_leftlistmg_trading_session_investor_dce_allorder:
    url="leftlistmg/trading/session/investor/dce/allorder.html"
    def render(self):
        return render_template(self.url)

class C_leftlistmg_trading_session_investor_dce_tradinginfo:
    url="leftlistmg/trading/session/investor/dce/tradinginfo.html"
    def render(self):
        return render_template(self.url)

class C_leftlistmg_trading_session_investor_dce:
    url="leftlistmg/trading/session/investor/dce.html"

    def render(self):
        allorder=C_leftlistmg_trading_session_investor_dce_allorder().render();
        tradinginfo = C_leftlistmg_trading_session_investor_dce_tradinginfo().render();
        return render_template(self.url,tradinginfo=tradinginfo,allorder=allorder)
class C_leftlistmg_trading_session_investor:
    url="leftlistmg/trading/session/investor.html"
    def render(self):
        investors=Investor.query.all()
        dce=C_leftlistmg_trading_session_investor_dce().render();
        return render_template(self.url,investors=investors,dce=dce)

class C_leftlistmg_trading_session:
    url="leftlistmg/trading/session.html"
    def render(self):
        investor=C_leftlistmg_trading_session_investor().render();
        return render_template(self.url,investor=investor)
class C_leftlistmg_trading():
    url="leftlistmg/trading.html"
    def render(self):

        session=C_leftlistmg_trading_session().render()
        return render_template(self.url,session=session);

class C_left_html:
    url="left_html.html"
    css_urls = []
    js_urls = []
    def render(self,active_url):
        leftlistmg_usermg=None
        leftlistmg_prcmg=None
        leftlistmg_rolemg=None
        leftlistmg_dashboard=None
        leftlistmg_dashboard=C_leftlistmg_dashboard().render();
        leftlistmg_usermg=C_leftlistmg_usermg().render();
        leftlistmg_prcmg=C_leftlistmg_prcmg().render();
        leftlistmg_rolemg=C_leftlistmg_rolemg().render();
        leftlistmg_trading=C_leftlistmg_trading().render();

        return render_template(self.url,
                               leftlistmg_dashboard=leftlistmg_dashboard,
                               leftlistmg_usermg=leftlistmg_usermg,
                               leftlistmg_prcmg=leftlistmg_prcmg,
                                leftlistmg_rolemg=leftlistmg_rolemg,
                               leftlistmg_trading=leftlistmg_trading,
                               )


class C_top_html:
    url="top_html.html"
    css_urls = []
    js_urls = []
    def render(self):
        return render_template(self.url);
if __name__ == '__main__':
  pass

