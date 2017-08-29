# -*- coding: utf-8 -*- 

from flask import render_template,flash,redirect,session,url_for,request,g
from flask_login import login_user,logout_user,current_user,login_required,AnonymousUserMixin,fresh_login_required,login_fresh
from app import app,db,lm,User
from form import LoginForm,UploadForm
import time
import view_usermg





@app.before_request
def before_request():
    g.user=current_user

@lm.user_loader
def load_user(id):
    #print id
    user=User.query.filter_by(id=id).first()
    return user


def render_template_with_authority(url,**context):
    # add authority check
    return render_template(url,**context)

@app.route('/')
@app.route('/index')
@app.route('/index.html')
@login_required
def index():

    return render_template_with_authority("index.html")
@app.route('/transaction/dce/futures.html')
def transaction_dce_futures():
    return render_template('rightlistmg/transaction/dce/futures.html')
@app.route('/transaction/dce/option.html')
def transaction_dce_option():
    return render_template('transaction/dce/option.html')

from prc.prc import PrcItem
#@app.route("/prcmg/speculation/view.html",methods=("GET","POST"))
def prcmg_view():
    #PrcItem("",dispaly=False,edit=True)
    print "prcmg_view"
    if request.method=='POST':
        print request.form
        time.sleep(20)
        return redirect("/prcmg/speculation/view.html")


    args={
        "username":"yangjie",
        "investor_prc":[],
        "contract_prc":[],
    }
    args["investor_prc"].append(PrcItem("CancelOrderLimitEnable","on",True,True))
    args["investor_prc"].append(PrcItem("MarginOccupyCheckEnable","off",True,True))
    args["investor_prc"].append(PrcItem("MarginPercentValue","on",True, True))
    args["investor_prc"].append(PrcItem("PositionCheckEnable", True, True))
    args["investor_prc"].append(PrcItem("RejectAllSell", True, True))
    args["investor_prc"].append(PrcItem("RejectAllBuy", True, True))
    args["investor_prc"].append(PrcItem("PriceTickCheckEnable", True, True))
    args["investor_prc"].append(PrcItem("PriceRangeCheckEnable", True, True))
    args["investor_prc"].append(PrcItem("RejectInvalidTickSizeEnable", True, True))
    args["investor_prc"].append(PrcItem("RejectInvalidLotSizeEnable", True, True))
    args["investor_prc"].append(PrcItem("QSThrottleEnable", True, True))
    args["investor_prc"].append(PrcItem("QSThrottleInterval", True, True))
    args["investor_prc"].append(PrcItem("QSOrdersPerInterval", True, True))
    args["investor_prc"].append(PrcItem("TotalThrottleEnable", True, True))
    args["investor_prc"].append(PrcItem("TotalThrottleInterval", True, True))
    args["investor_prc"].append(PrcItem("TotalOrdersPerInterval", True, True))
    args["investor_prc"].append(PrcItem("PriceCheckEnable", True, True))
    args["investor_prc"].append(PrcItem("allowMktOrders", True, True))
    args["investor_prc"].append(PrcItem("RestrictTrading", True, True))
    args["investor_prc"].append(PrcItem("MaxQtyEnable", True, True))


    if(request.args.get("showtype")!="edit"):
        print "user",request.args.get("username")
        #print request.args.getlist()
        args["userlist"]=[
            {
            "username":"jack",
                "create_time":"2017-6-27",
                "modified_time":"2017-6-28",
                "loaded":"yes",
            },
            {
                "username": "lily",
                "create_time": "2017-6-27",
                "modified_time": "2017-6-28",
                "loaded": "yes",
            }
        ]
        args["username"]=request.args.get("username");
        return render_template_with_authority("prcmg/speculation/prc_view.html",args=args)
    else:

        return render_template_with_authority("prcmg/speculation/prc_edit.html",args=args)
@app.route("/prcmg/speculation/create.html")
def prcmg_create():
    return render_template_with_authority("prcmg/speculation/create.html")

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    #r.headers['Cache-Control'] = 'public, max-age=0'
    return r




#from flask_cachecontrol import dont_cache,FlaskCacheControl
#flask_cache_control = FlaskCacheControl()
#flask_cache_control.init_app(app)

import  tools

@app.route("/super/<path:active_html>",methods=['GET'])
#@dont_cache()
def super_view(active_html):
    object_top=view_usermg.C_top_html()
    top_html=object_top.render();
    object_left=view_usermg.C_left_html()
    left_html=object_left.render(active_html);
    object_right=view_usermg.C_right_html()
    right_html=object_right.render(active_html);
    print active_html
    css_urls=["/static/vendor/bootstrap/css/bootstrap.min.css","/static/css/xele_nav.css",
              ]
    js_urls=["/static/vendor/jquery/jquery.min.js","/static/vendor/jqueryMigrate/jquery-migrate.js","/static/vendor/bootstrap/js/bootstrap.min.js",
             "/static/js/xele/xele_nav.js"
             ]
    css_urls.extend(object_top.css_urls)
    css_urls.extend(object_left.css_urls)
    css_urls.extend(object_right.css_urls)

    js_urls.extend(object_top.js_urls)
    js_urls.extend(object_left.js_urls)
    js_urls.extend(object_right.js_urls)

    return render_template("super.html",top_html=top_html,left_html=left_html,right_html=right_html,css_urls=tools.avoid_duplication(css_urls),js_urls=tools.avoid_duplication(js_urls));
    pass

@app.route("/usermg/view.html",methods=['GET'])
def usermg_view():
    #get url
    url=request.url
    #get username
    username="yanjige"
    #analsys url to target | args
    target=""
    #check exist
    #
    right_html=view_usermg.usermg_view();
    return render_template("super.html",args=[],username="jack",right_html=right_html,active="/usermg/view.html");
@app.route("/rolemg/view.html",methods=['GET'])
def rolemg_view():
    right_html=view_usermg.rolemg_view();
    return render_template("super.html", args=[], username="jack", right_html=right_html, active="/rolemg/view.html");

#@app.route("/prcmg/view.html",methods=['GET'])
#def prcmg_view():
#    pass
@app.route("/prcmg/speculation/investor_prc.html")
def prcmg_speculation_investorprc():
    right_html=view_usermg.C_right_html().render("a");
    return render_template("super.html", args=[], username="jack", right_html=right_html, active="/prcmg/speculation/investor_prc.html")
@app.route("/prcmg/speculation/view.html")
def prcmg_speculation_view():
    right_html=view_usermg.prcmg_view();
    return render_template("super.html", args=[], username="jack", right_html=right_html, active="/prcmg/speculation/view.html")

@app.route("/usermg/create.html")
def usermg_create():
    return render_template_with_authority("usermg/create.html")
#@app.route("/usermg/view.html")
#def usermg_view():
#    return render_template_with_authority("usermg/view.html")

#@app.route("/rolemg/view.html")
#def rolemg_view():
#    return render_template_with_authority("rolemg/view.html")

@app.route("/rolemg/create.html")
def rolemg_create():
    return render_template_with_authority("rolemg/create.html")

import json
from dataquery import cmd_parse
@app.route("/data/query.html")
def data_query():
    #cmd
    #from database query prc data by username
    print request.args
    return json.dumps(cmd_parse().query(request.args.get("cmd"),request.args.get("args")));

@app.route('/stock.html')
def stock():
    return render_template('stock.html')
@app.route('/shfekline')
def shfekline():
    return render_template('shfeKline.html')

@app.route('/kpainter')
def Kpainter():
    return render_template('kpainter.html')
@app.route('/index_bak')
def index_bak():

    return render_template('index_bak.html')
@app.route('/chat')
def chat():
    return render_template("chat.html")
@app.route('/test')
def test():
    return render_template("test.html")
@app.route('/jstest')
def jstest():
    return render_template('jstest.html')
@app.route('/testextarea')
def testextarea():
    return render_template('testextarea.html')
@app.route('/notifications.html')
def notifications():
    return render_template('notifications.html')
@app.route('/mygrid')
def mygrid():
    return render_template('mygrid.html')
@app.route('/mylongpolling')
def mylongpolling():
    return render_template('mylongpolling.html')
@app.route('/news')
def news():
    return render_template('news.html')
@app.route('/md')
def md():
    return render_template('xelemd.html')
@app.route('/login',methods=['GET','POST'])
def login():
    if request.args.get('localization') is None:
        return redirect('/login?localization=zh')
    if g.user is not None and g.user.is_authenticated:
        login_fresh()
        session['_fresh']=False
        return redirect(url_for('index'))
    if g.user.is_active==True:
        #flash('active is Ture')
        pass
    else:
        #flash('active is Flase')
        pass
    form=LoginForm()
    print form.username.data
    print form.password.data
    if form.validate_on_submit():
        print "INFO: have submit"
        user=User.query.filter_by(username=form.username.data,password=form.password.data).first()
        if(user is not None):
            #login_user(user, remember=form.remember_me.data)
            print "INFO: find user"
            login_user(load_user(user.id),form.remember_me.data,False,False)
            return redirect(request.args.get('next') or url_for('index'))
        else:
            print User.query.filter_by(username=form.username.data).first()
            if(User.query.filter_by(username=form.username.data).first() is  None):
                print "username no exist"
                form.username.errors.append("username is not exist")
            else:
                print "wrong password"
                form.password.errors.append("wrong password")
    return render_template('login.html',form=form)
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

permission_collection=[
    {
    "target":"/usermg",
    "display":True,
    "edit":True,
    "args":"jack,lily,tom",
     "check":True,
    }
]




import ctarget

def permission_authentication(url,action,args=""):


    record1={
        "id":1,
        "roleID":1,
        "target":"/usermg",
        "display":True,
        "edit":True,
        "args":"jack,lily,tom",
        "willcheck":False,

    }

    return ctarget.ctarget.self_action(url,record1,'display',args);

#import ctarget
#def exec_event_func(record,action,args):

def local_render_template(template,**context):
    with app.app_context():
        return render_template(template,)


import  ajaxreq

