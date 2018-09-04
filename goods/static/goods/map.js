minemap.domainUrl = 'http://www.minedata.cn/';
minemap.dataDomainUrl = 'http://www.minedata.cn/';
minemap.spriteUrl = 'http://www.minedata.cn//minemapapi/v2.0.0/sprite/sprite';
minemap.serviceUrl = 'http://www.minedata.cn//service';
minemap.accessToken = '0317afa73fa54fd4828d3f76c64381f0';
minemap.solution = 7750;

let map = new minemap.Map({
    container: 'map',
    style: "http://www.minedata.cn/service/solu/style/id/7750",
    center: [116.3974049,39.9088741],
    zoom: 11,
    pitch: 0,
    logoControl:true /*logo控件是否显示，不加该参数时默认显示*/
});


$("#navarrow").click(function(){
    $("#navpath").toggle();
    if($("#navpath").is(':visible')) {
        $("#product_list").hide();
    }
    else {
        $("#product_list").show();
    }
    $("#input_now").empty();
    $("#detail").empty();
});

$(".line-search-exchange").click(function(){
    let nav_from=$("#nav-from").val();
    $("#nav-from").val($("#nav-to").val());
    $("#nav-to").val(nav_from);
});

let locations=[];

/**
 * 加载时显示商品类型图标
 */
let good_list=document.getElementsByClassName("good_list");
showgoodmarker();
function showgoodmarker() {
    for(let i=0;i<good_list.length;i++) {
        let good_list_id = good_list[i].id;
        let category =good_list[i].getElementsByClassName('category')[0].innerText;
        let image_good;
        switch(category)
        {
            case "c01":
                image_good="url('/static/goods/images/camera.png')";
                break;
            case "c02":
                image_good="url('/static/goods/images/book.png')";
                break;
            case "c03":
                image_good="url('/static/goods/images/clothing.png')";
                break;
            case "c04":
                image_good="url('/static/goods/images/bass.png')";
                break;
            case "c05":
                image_good="url('/static/goods/images/bike.png')";
                break;
            case "c06":
                image_good="url('/static/goods/images/taxi.png')";
                break;
            case "c07":
                image_good="url('/static/goods/images/maps-and-flags.png')";
                break;
        }
        let large_category =good_list[i].getElementsByClassName('large-category')[0].innerText;
        switch(large_category)
        {
            case "b01":
                good_list[i].getElementsByClassName('large-category')[0].innerText="租";
                break;
            case "b02":
                good_list[i].getElementsByClassName('large-category')[0].innerText="卖";
                break;
            case "b03":
                good_list[i].getElementsByClassName('large-category')[0].innerText="送";
                break;
        }
        let coordis_x=good_list[i].getElementsByClassName('coordis_x')[0].innerText;
        let coordis_y=good_list[i].getElementsByClassName('coordis_y')[0].innerText;
        let title = good_list[i].getElementsByClassName('good-title')[0].innerText;

        let el = document.createElement('div');
        el.id = good_list_id;
        el.style["background-image"] = image_good;
        el.style.width = "32px";
        el.style.height = "32px";
        el.style.cursor = "pointer";
        el.style['position']='relative';
        let popup = new minemap.Popup({offset:[0,-32]}).setHTML("<div>"+title+"</div>");
        let marker = new minemap.Marker(el, {offset: [-16,-32]}).setLngLat([coordis_x,coordis_y]).setPopup(popup).addTo(map);
    }
}

/**
 * 添加导航菜单 ,可选值有  top-left  top-right bottom-left bottom-right
 */
map.addControl(new minemap.Navigation(),"bottom-right");
map.addControl(new minemap.Scale(),"top-right");


/**实时识别输入框信息 */
$(".input_it").bind("input propertychange",function(event){
    let input_id=$(this).attr("id");
    let input_now_top;
    if(input_id=="searchText") {
        $("#navpath").hide();
        input_now_top=45;
    }
    else {
        input_now_top=205;
    }

    if($(this).val()!='') {
        minemap.service.querySmartTipsResult('110000',$(this).val(),'all',10,function(error,results){
            let obj=JSON.parse(JSON.stringify(results));
            $("#input_now").empty();
            $("#input_now").css({"position":"absolute","top":input_now_top,"z-index":100,"box-sizing":"border-box","background-color":"#fff","box-shadow":"-1px 1px 2px 1px #f3f3f3"});

            for (let i in obj.data.rows) {
                $("#input_now").append("<li class='suggestion'><span class='smt_val'>"+obj.data.rows[i].name+"</span><span class='smt_district'>"+obj.data.rows[i].area+"</span></li>");
            }

            $(".suggestion").css({"height":"30px","line-height":"30px","width":"320px","box-sizing":"border-box","overflow":"hidden","border-right":"1px solid #e7e7e7"});
            $(".suggestion").mouseover(function(){
                $(this).css({"background":"#f3f3f3","cursor":"pointer"});
            });
            $(".suggestion").mouseout(function(){
                $(this).css({"cursor":"default","background":"#fff"});
            });
            
            $(".suggestion").click(function(){
                $("#"+input_id).val($(this).children('.smt_val').text());
                if(input_id=="searchText") {
                    $("#searchbtn").click();
                }
                $("#input_now").empty();
            });
        });
    }
    else {
        $("#input_now").empty();
        $("#detail").empty();
    }
});


$("#form_input").bind("input propertychange",function(event){
    if($(this).val()!='') {
        minemap.service.querySmartTipsResult('110000',$(this).val(),'all',10,function(error,results){
            let obj=JSON.parse(JSON.stringify(results));
            $("#input_form_now").empty();
            $("#input_form_now").css({"position":"absolute","top":"30px","z-index":100,"box-sizing":"border-box","background-color":"#fff","box-shadow":"-1px 1px 2px 1px #f3f3f3"});

            for (let i in obj.data.rows) {
                $("#input_form_now").append("<li class='suggestion'><span class='smt_val'>"+obj.data.rows[i].name+"</span><span class='smt_district'>"+obj.data.rows[i].area+"</span></li>");
            }

            $(".suggestion").css({"height":"30px","line-height":"30px","width":"320px","box-sizing":"border-box","overflow":"hidden","border-right":"1px solid #e7e7e7"});
            $(".suggestion").mouseover(function(){
                $(this).css({"background":"#f3f3f3","cursor":"pointer"});
            });
            $(".suggestion").mouseout(function(){
                $(this).css({"cursor":"default","background":"#fff"});
            });

            $(".suggestion").click(function(){
                $("#form_input").val($(this).children('.smt_val').text());
                $("#search_form").click();
                $("#input_form_now").empty();
            });
        });
    }
    else {
        $("#input_form_now").empty();
        //$("#detail").empty();
    }
});

/**手动在地图上添加点 */
let coordinate_x;
let coordinate_y;
$("#addPoint").click(function(){
    $(".close").click();
    map.getCanvas().style.cursor = 'crosshair';
    map.on("click",function(e){
        map.removeMarkers();
        var lngLat = e.lngLat;
        coordinate_x=lngLat.lng;
        coordinate_y=lngLat.lat;

        let el = document.createElement('div');
        el.id='marker';
        el.style['background-image'] = "url('/static/goods/images/maps-and-flags.png')";
        el.style['background-size']='cover';
        el.style.width='32px';
        el.style.height='32px';
        el.style.cursor='pointer';
        el.style['position']='relative';
        el.setAttribute("class",'map-marker');

        let marker = new minemap.Marker(el, {offset: [-16,-32]}).setLngLat(lngLat).addTo(map);

        $("#publish").click();
    });
});

/**表单搜索位置功能 */
$("#search_form").click(function () {
    $("#input_form_now").empty();
    map.removeMarkers();
    let searchText=document.getElementById("form_input").value;
    minemap.service.queryAllSearchResult('110000',searchText,1,10,function(error,results){
        let obj=JSON.parse(JSON.stringify(results));
        locations=[];
        let coordis=obj.data.rows[0].geom_display.coordinates;
        let text=obj.data.rows[0].name;
        let id=obj.data.rows[0].id;
        locations.push({id: id, title: text, loc: coordis});
        markerAndList();
        let coordis_x=locations[0].loc[0]-0.008;
        let coordis_y=locations[0].loc[1];
        map.flyTo({
            center: [coordis_x,coordis_y],
            zoom: 14
        });
        $(".map-marker").click();
        $("input[name='coordinate_x']").val(coordis_x);
        $("input[name='coordinate_y']").val(coordis_y);
    });
})

/**搜索位置功能 */
let detail=document.getElementById("detail");
let searchbtn=document.getElementById("searchbtn");

searchbtn.onclick=function(){
    $("#input_now").empty();
    $("#detail").empty();
    $("#navpath").hide();
    map.removeMarkers();
    if(detail.childNodes.length>0) {
        detail.removeChild(detail.childNodes[0]);
    }
    var ul=document.createElement("ul");
    detail.appendChild(ul);
    let searchText=document.getElementById("searchText").value;
    minemap.service.queryAllSearchResult('110000',searchText,1,10,function(error,results){  
        let obj=JSON.parse(JSON.stringify(results));
        locations=[];
        for(let i in obj.data.rows){
            let coordis=obj.data.rows[i].geom_display.coordinates;
            let text=obj.data.rows[i].name;
            let id=obj.data.rows[i].id
            locations.push({id: id, title: text, loc: coordis});

            let list=document.createElement("li");
            list.setAttribute("data-rel-li",obj.data.rows[i].id);
            list.innerHTML="名字："+obj.data.rows[i].name+"<br>地点："+obj.data.rows[i].address+"<br>电话："+obj.data.rows[i].tel;
            let ul=detail.getElementsByTagName("ul")[0];
            ul.appendChild(list);
        }
        markerAndList();
    });
}

function markerAndList(){
    map.flyTo({
        center: locations[0].loc,
        zoom: 14
    });

    $(".minemap-canvas-container").unbind("click").click(function(){
        $(".map-marker").unbind("click").click(function(){
            let id=$(this).attr("id");
            $(".map-marker").mouseout();
            $(this).css({"background-image":"url('/static/goods/images/maps-and-flags-blue.png')"});
            $(this).unbind("mouseout");
            
            $("#detail ul li").each(function(){
                if($(this).attr("data-rel-li")==id){
                    $(this).mouseover();
                }
                else {
                    $(this).mouseout();
                }
            });
        });
    });

    $(".minemap-canvas-container").unbind("mouseover").mouseover(function(){
        $(".map-marker").unbind("mouseover").mouseover(function() {
            $(this).css({"background-image":"url('/static/goods/images/maps-and-flags-blue.png')"});
        });
    });
    $(".minemap-canvas-container").unbind("mouseout").mouseout(function(){
        $(".map-marker").unbind("mouseout").mouseout(function() {
            $(this).css({"background-image":"url('/static/goods/images/maps-and-flags.png')"});
        });
    });

    $("#detail ul li").mouseover(function(){
        $(this).css({"background":"#f3f3f3","cursor":"pointer"});
    });
    $("#detail ul li").mouseout(function(){
        $(this).css({"background":"#fff"});
    });

    $("#detail ul li").click(function(){
        let id=$(this).attr("data-rel-li");
        $("#"+id).click();
    });
    
    let markerList=[];
    map.addMarkers(showMarkers(markerList));
}

function showMarkers(markerList){
    for (let i in locations){
        let latlon=locations[i].loc;
        let el = document.createElement('div');
        el.id=locations[i].id;
        el.style['background-image'] = "url('/static/goods/images/maps-and-flags.png')";
        el.style['background-size']='cover';
        el.style.width='32px';
        el.style.height='32px';
        el.style.cursor='pointer';
        el.style['position']='relative';
        el.setAttribute("class",'map-marker');
    
        let popup = new minemap.Popup({offset:[0,-32]}).setHTML("<div>"+locations[i].title+"</div>");
        let marker = new minemap.Marker(el, {offset: [-16,-32]}).setLngLat(latlon).setPopup(popup).addTo(map);
        markerList.push(marker);
    }
    return markerList;
}

/**导航功能 */
$(".navbtn").click(function(){
    let text_from=$("#nav-from").val();
    let text_to=$("#nav-to").val();
    $("#input_now").empty();
    let coordinates_from;
    let coordinates_to;
    let click_btn=$(this).attr('id');
    
    minemap.service.queryAllSearchResult('110000',text_from,1,10,function(error,results){  
        let obj=JSON.parse(JSON.stringify(results));
        coordinates_from=obj.data.rows[0].geom_display.coordinates;
        minemap.service.queryAllSearchResult('110000',text_to,1,10,function(error,results){  
            let obj=JSON.parse(JSON.stringify(results));
            coordinates_to=obj.data.rows[0].geom_display.coordinates;
            if(click_btn=='nav-bus') {
                minemap.service.queryRouteBusResult2('110000',coordinates_from.toString(),coordinates_to.toString(),0,1,0,function(error,results) {
                    let obj=JSON.parse(JSON.stringify(results));
                    if(obj.data.rows.length>0) {
                        let routelatlons_value='';
                        for(let i in obj.data.rows[0].routelatlons) {
                            routelatlons_value+=obj.data.rows[0].routelatlons[i].value;
                        }
                        let routelatons=routelatlons_value.split(";");
                        let routelatons_final=[];
                        for(let i in routelatons) {
                            routelatons_final.push(routelatons[i].split(","));
                        }
                        showNavLine(routelatons_final);
                    }
                });
            }
            else if(click_btn=='nav-drive') {
                minemap.service.queryRouteDrivingResult3(coordinates_from.toString(),coordinates_to.toString(),'',2,'',function(error,results) {
                    let obj=JSON.parse(JSON.stringify(results));
                    if(obj.data.rows.length>0) {
                        let routelatlons_value=obj.data.rows[0].routelatlon;
                        /*let routelatlons_value='';
                        for(let i in obj.data.rows[0].item) {
                            routelatlons_value+=obj.data.rows[0].item[i].routelatlon;
                        }*/
                        let routelatons=routelatlons_value.split(";");
                        let routelatons_final=[];
                        for(let i in routelatons) {
                            routelatons_final.push(routelatons[i].split(","));
                        }
                        showNavLine(routelatons_final);
                    }
                });
            }
        });

    });
        
});

function showNavLine(routelatons_final){
    if(map.getLayer("navline")) {
        map.removeLayer("navline");
        map.removeSource("navlineSource");
    }
    
    for(let n in routelatons_final) {
        for(let j in routelatons_final[n]) {
            routelatons_final[n][j]=parseFloat(routelatons_final[n][j]);
        }
    }
    
    map.addSource("navlineSource", {
        "type": "geojson",
        "data": {
            "type": "Feature",
            "properties": {},
            "geometry": {
                "type": "LineString",
                "coordinates": routelatons_final
            }
        }
    });

    map.addLayer({
        "id": "navline",
        "type": "line",
        "source": "navlineSource",
        "paint": {
            "line-color": "#006df0",
            "line-width": 5
        }
    });
}


$("#publish").click(function(){
    $("input[name='coordinate_x']").val(coordinate_x);
    $("input[name='coordinate_y']").val(coordinate_y);
});


/** 页脚button*/
document.getElementById("hide-listings").onclick=function(){
    map.removeMarkers();
};
document.getElementById("show-listings").onclick=function(){
    let markerList=[];
    map.addMarkers(showMarkers(markerList));
    showgoodmarker();
};

function toggle(id){
    if(map.isStyleLoaded()){
        map.accessToken="0317afa73fa54fd4828d3f76c64381f0";
        map.solution = id;
        map.setStyle("http://www.minedata.cn/service/solu/style/id/"+id);
    }
} 

