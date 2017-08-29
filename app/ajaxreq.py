from app import app
import dataquery
import json
@app.route("/ajaxreq/get_capital_account_info<any:args>",methods=['GET'])
def ajaxrep_get_capital_account_info(args):
    #cai=dataquery.get_capital_account_info();
    return "abc";
    #return json.dumps(cai);