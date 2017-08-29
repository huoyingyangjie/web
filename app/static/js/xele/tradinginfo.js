/**
 * Created by jiey on 8/3/17.
 */

function tradinginfo_add() {

    var rowData=[3,21,3,4,5,6,7,8,9,10,11];
    $("#position_grid").pqGrid(
        "addRow",
        {
            rowData:rowData,
            checkEditable:false,
            history:false,

        }
    );
    console.time("tradinginfo_filter");
    //TODO:
    tradinginfo_filter();//add enable to verify!
    console.timeEnd("tradinginfo_filter");

    console.time("tradinginfo_sort");
    tradinginfo_sort();
    console.timeEnd("tradinginfo_sort");


}
function tradinginfo_sort() {

    var td_sort=$("tr td[class*='pq-col-sort-']");
    if(td_sort.length==0)
        return;
    if(td_sort.hasClass("pq-col-sort-asc")) {
        td_sort.removeClass("pq-col-sort-asc");
        td_sort.addClass("pq-col-sort-desc");
        $( "#position_grid" ).pqGrid( "option", "dataModel.sortDir", "down" );
    }
    else
    {

        td_sort.removeClass("pq-col-sort-desc");
        td_sort.addClass("pq-col-sort-asc");
         $( "#position_grid" ).pqGrid( "option", "dataModel.sortDir", "up" );
    }

    td_sort.click();

}
function tradinginfo_filter() {

    var contractfilter=$("#tradinginfo_filter_bar input[name='contract']").val().trim();

    $("#position_grid").pqGrid(
        "filter",{
            oper:"replace",
            data:[
                {dataIndx:0,condition:"equal",value:contractfilter},
            ]
        }
    );


}





$(document).ready(function () {

dataCache=[]
for(var i=0;i<1000;i++)
{
    if(i%2)
        dataCache.push(["1",i,3,4,5,6,7,8,9,10,11]);
    else
        dataCache.push(["2",i,3,4,5,6,7,8,9,10,11]);
}

    var obj={
        //sortable:true,
        filterModel:{on:true,mode:"OR",header:false},
        hoverMode:'row',
        rowBorders: true,
        columnTemplate: {editable: false},
        showBottom: true,
        showTop: true,
        virtualX:false,
        virtualY:true,
        title:"position",
        width:"100%-2",
        height:"100%-2",
        flexHeight:false,
        scrollModel: { autoFit: true },
        swipeModel: {on: false} ,
        columnTemplate: {editable: false},
        editable: false,
        selectionModel: { type: 'row' ,mode:"single" },
        pageModel: { type: "local", rPP: 10000,  rPPOptions:[50, 100, 200],strRpp: "{0}", strDisplay: "{0} to {1} of {2}" },
        numberCell:{show:false,title:"lines",resizable: false,},
        resizable: false,
        rowBorders: true,
        hwrap:false,
        wrap:false,
        colModel:[

            {title:"Lines",dataType:"integer",sortable:false,render:function(ui){
                return ui.rowIndx+1;
            },width:"1%+50",resizable: false,dataIndx:-1},

            {title:"contract",dataType:"string",sortable: true,dataIndx: 0},
            {title:"buy or sell",dataType:"string",sortable: true,dataIndx: 1},
            {title:"total position",dataType:"integer",sortable: true,dataIndx: 2},
            {title:"old position",dataType:"integer",sortable: true,dataIndx: 3},
            {title:"today positon",dataType:"integer",sortable: true,dataIndx: 4},
            {title:"available closing position",dataType:"string",sortable: true,dataIndx: 5},
            {title:"average price of position",dataType:"float",sortable: true,dataIndx: 6},
            {title:"Position gain and loss",dataType:"float",sortable: true,dataIndx: 7},
            {title:"margin be taken up",dataType:"float",sortable: true,dataIndx: 8},
            {title:"insured",dataType:"string",sortable: true,dataIndx: 9},
            {title:"exchange",dataType:"string",sortable: true,dataIndx: 10},
        ],
        dataModel:{
            data:dataCache,
            location: "local",
            sorting: "local",
        },
    }

    if($("#position_grid").length==0)
        return;

     obj.refresh = function(evt){
         $(".pq-grid-cell").enableSelection();
     };
    $("#position_grid").pqGrid(obj);
     $('.pq-cont').enableSelection();

});
$(document).ready(function () {
        return;
        var noRows =1000; //1 million.
        var dataCache = [];

        //initialize the data array.
        for (var i = 0; i < noRows; i++) {
            //dataCache[i] = [i,0,0,0];
        }
       dataCache[0]=[255,2,3,4]
       dataCache[1]=[1,3,4,5]
       dataCache[2]=[3,4,5,6]
        var obj = {
            width: "100%",

            showTop: true,
            showBottom: false,
            resizable: false,
            editable: false,
            virtualX: false,
            virtualY: true,
            scrollModel: { autoFit: true },
            swipeModel: {on: false} ,
            columnTemplate: {editable: false},
            //sortable:true,
             //numberCell: { show: false},
            selectionModel: { type: 'row' },
            //selectionModel: {type: null},
            //flexHeight: true,
            hoverMode:'row',
                rowBorders: true,
            title:"<p style='color:black'>Well</p>",
             //columnBorders:true,
           numberCell:{resizable:false, title: "<p style=''>Lines</p>",  width:40, show: false},
              hwrap:false,
              wrap:false,
            width:"100%-30",
            colModel: [
                { title: "Company", dataType: "string",sortable: true,dataIndx: 0} ,
                { title: "Notes", dataType: "integer" ,sortable: true,dataIndx : 1,render:function(ui){
                var $td = $( "#dce_futures_grid" ).pqGrid( "getCell", { rowIndx: ui.rowIndx, colIndx: ui.colIndx } );
                console.log($td.get(0).tagName);
                //$td.pqGrid("selection",{ type:'row', method:'getSelection' })
                console.log($td);
                $td.enableSelection();
                //console.log(ui.rowData[ui.colIndx]=("<p style='background:red'>"+ui.rowData[ui.colIndx]+"</p>"));
                }},
                { title: "Revenues ($ millions)", dataType: "float", align: "right", sortable: true,dataIndx : 2 },
                { title: "Profits ($ millions)", dataType: "float", align: "right" ,sortable: true,dataIndx : 3 }
            ],
            dataModel: {
                data: dataCache,
                location: "local",
                sorting: "local",


            },

        };


                       obj.refresh = function(evt){
            // $(this).pqGrid('enableSelection');
            // $('.pq-cont').enableSelection();
             $(".pq-grid-cell").enableSelection();
          //   $("div.pq-grid-cell",$dce_futures_grid).enableSelection();
           // $("tr.pq-grid-row").


           };


       $dce_futures_grid=$("#dce_futures_grid").pqGrid(obj);
       // $dce_futures_grid.enableSelection();
        //$("div.pq-grid-cell",$dce_futures_grid).enableSelection();
        $('.pq-cont').enableSelection();
    });



