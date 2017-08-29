/**
 * Created by jiey on 7/27/17.
 */


function ajax_callback(data,status){

    //console.log($(this),this);
    this.successFunc(data,status);

    setTimeout(wrap_longpolling(this.args),this.args.timeout);
}

function ajax_get(url,callback,dataType){


    $.ajax(
        {
            url:url,async:true,cache:false,dataFilter:function (data,type) {
            return data;
        },type:"GET",success:ajax_callback,nextFunc:ajax_get,dataType:dataType,successFunc:callback,

        }
    );
}

function nullfunc(data,func) {
    console.log(data);
}
function longpolling(options) {

        if(typeof(options)=="undefined" )
        {
        console.log("undefined options");
            return;
        }
        if(Object.prototype.toString.call(options)!='[object Object]')
        {
            console.log("options is not Object");
            return ;
        }
        if(! ('url' in options))
        {
            console.log("undefined options.url");
            return;
        }
        if(!('callback' in options))
        {
            console.log("undefined options.callback");
            options.callback=nullfunc;
        }
        console.log(Object.prototype.toString.call(options.callback));
        if(!('dataType' in options))
        {
            console.log("undefined options.dataType");
            options.dataType='text';
        }
        if(!('timeout' in options))
        {
            console.log("undefined options.timeout");
            options.timeout=0;
        }

         $.ajax(
        {
            url:options.url,async:true,cache:false,dataFilter:function (data,type) {
            return data;
            },type:"GET",success:ajax_callback,dataType:options.dataType,successFunc:options.callback,args:options

            }
        );




}

function wrap_longpolling(options) {

    return function () {
        longpolling(options)
    };
}
