import sys
import inspect

def ctarget_response(ctarget_dict):
    thismodule=sys.modules[__name__]
    #print thismodule
    for subctarget in  dir(thismodule) :
        subctarget_class=getattr(thismodule,subctarget)
        if inspect.isclass(subctarget_class):
            if issubclass(subctarget_class,ctarget) and subctarget_class.__name__!='ctarget':
                if hasattr(subctarget_class,'url'):
                    if ctarget_dict.has_key(subctarget_class.url):
                        assert 0;
                    ctarget_dict[subctarget_class.url]=subctarget_class
                    #print ctarget_dict[subctarget_class.url].url

#will def exception class
class CtargetException(Exception):

    def __init__(self,err):
        Exception.__init__(self)
        self.err=err

def find_action(obj,action):
    action_method_name='action_'+action
    if hasattr(obj,action_method_name):
        action_method=getattr(obj,action_method_name)
        if inspect.ismethod(action_method):
            return action_method
        else:
            raise CtargetException("no function");
    else:
        return None


class ctarget:
    ctarget_dict={}
    def __init__(self,record,action,args):
        self.record=record
        self.action=action
        self.args=args;
    @classmethod
    def self_action(cls,url,record,action,args):
        if cls.ctarget_dict.has_key(url):
            action_method = find_action(cls.ctarget_dict[url](record, action, args), action)
            if (action_method):
                return action_method()
                pass
            else:
                raise CtargetException("unknow action %s"%action)
        else:
            raise CtargetException('unknow url %s'%url);


class c_usermg(ctarget):
    url="/usermg"
    """
    1.we will guarantee all action method name with "action_"+action.This is an agreement!
    
    2.every class must have class var 'url'.it will be used to verify.
    
    """


    def action_display(self):
            return self.record.display


if __name__ == '__main__':
    ctarget_response(ctarget.ctarget_dict)
    #ctarget.self_action('/usermg',0,0,0)
    #print ctarget.self_action('/usermg', 0, 'display', 0)
    #print type(getattr(c_usermg(0,0,0),'display'))