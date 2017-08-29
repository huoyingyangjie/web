



import json
from app.models import Capital_account_info

def get_capital_account_info(investor_id=None):
    if investor_id:
        return Capital_account_info.query.filter_by(investor_id=investor_id).first()
    else:
        return Capital_account_info.query.all()


class cmd_parse:
    def __init__(self):
        self.query_ret = {
        "ret_code":  255,
        "ret_value": "unknow cmd",
            }
        self.cmd_dict={
        "QUERY_USER_PRC":self.QUERY_USER_PRC,
        }
    def query(self,cmd,args):
        if cmd in self.cmd_dict:
                self.cmd_dict[cmd](args);
        return self.query_ret;
    def QUERY_USER_PRC(self,args):
        print "args",args
        self.query_ret["ret_code"]=0;
        self.query_ret["ret_value"]={
            "investor_prc":[
                {
                    "name":"CancelOrderLimitEnable",
                    "value":"off",
                    "display":True,
                    "edit":False,
                    "type":"checkbox",
                },
                {
                    "name": "CancelOrderLimitEnable",
                    "value": "off",
                    "display": True,
                    "edit": False,
                    "type": "checkbox",
                },
                {
                    "name": "CancelOrderLimitEnable",
                    "value": "off",
                    "display": True,
                    "edit": False,
                    "type": "checkbox",
                },
                {
                    "name": "CancelOrderLimitEnable",
                    "value": "off",
                    "display": True,
                    "edit": False,
                    "type": "checkbox",
                },
                {
                    "name": "CancelOrderLimitEnable",
                    "value": "off",
                    "display": True,
                    "edit": False,
                    "type": "checkbox",
                },
                {
                    "name": "CancelOrderLimitEnable",
                    "value": "off",
                    "display": True,
                    "edit": False,
                    "type": "checkbox",
                },
            ],
            "contract_prc":[
                {
                    "name":"ag1702",
                    "value":[
                        {
                            "name":"CancelTimesLimit",
                            "value":123,
                            "display": True,
                            "edit": False,
                            "type": "input",
                        }
                    ],
                }
            ],
        }


        pass


