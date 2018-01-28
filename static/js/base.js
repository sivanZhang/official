
$(document).ready(function(){
    //
    var height = window.innerHeight;
    var width = window.innerWidth;
    $('.wechat_div').hide();
    $('.product_sec_menu').hide();
    //$('.swiper-container').height(height);
    //$('.swiper-slide').css({'margin':height/2+'px ' + (width/2-20) + 'px'});
    $('.wechat').hover(function(){
        $('.wechat_div').show();
    });
    $( ".wechat" ).mouseout(function() {
         $('.wechat_div').hide();
    });

    $('.a_store').click(function(){
    //  体验店点击事件
    
    });

    $('.store_sec_menu').hide();
    
    $('.a_store').click(function(e){
        //体验店菜单点击了
        var store_show = $('.store_sec_menu').is(":visible");
        var product_show = $('.product_sec_menu').is(":visible");
        e.preventDefault();
        
        if (store_show)
        { 
            $('.store_sec_menu').hide();
        }
        else{
            if(product_show)
            {
                $('.product_sec_menu').hide();
            }
            $('.store_sec_menu').show();
        }
    });

    $('.product_sec_menu').hide();
    $('.a_product').click(function(e){
        // cast菜单点击了
        e.preventDefault();
        var product_show = $('.product_sec_menu').is(":visible");
        var store_show = $('.store_sec_menu').is(":visible");
        if (product_show)
        { 
            $('.product_sec_menu').hide();
        }
        else{
            if(store_show)
            {
                $('.store_sec_menu').hide();
            }
            $('.product_sec_menu').show();
        }
    }); 
   
    //
   
         $('.bussiness_img_hove').hover(
            function() {
                // Called when the mouse enters the element
                $(this).attr({'src':'/static/img/bussiness-1.png'});
            },
            function() {
                // Called when the mouse leaves the element
                $(this).attr({'src':'/static/img/bussiness.png'});
            });

            $('.store_img_hove').hover(
            function() {
                // Called when the mouse enters the element
                $(this).attr({'src':'/static/img/store-1.png'});
            },
            function() {
                // Called when the mouse leaves the element
                $(this).attr({'src':'/static/img/store.png'});
            });


            $('.cast_img_hove').hover(
            function() {
                // Called when the mouse enters the element
                $(this).attr({'src':'/static/img/cast-1.png'});
            },
            function() {
                // Called when the mouse leaves the element
                $(this).attr({'src':'/static/img/cast.png'});
            });

            $('.castdock_img_hove').hover(
            function() {
                // Called when the mouse enters the element
                $(this).attr({'src':'/static/img/castdock-1.png'});
            },
            function() {
                // Called when the mouse leaves the element
                $(this).attr({'src':'/static/img/castdock.png'});
            });

            //底部菜单hover in and out
            $('.tr_menu').hide();
            $('.sidemenu').click(
            function() {
               // Called when the mouse enters the element
               var menu_show = $('.tr_menu').is(":visible");
                if (menu_show)
                { 
                    $('.tr_menu').hide('slow');
                    $('.sidemenu').attr({'src':'/static/img/menu.png'});
                }
                else{ 
                    $('.tr_menu').show('slow');
                    $('.sidemenu').attr({'src':'/static/img/menu_close.png'});
                }
            });
   
    
})
$(document).ready(function(){
    /* 菜单下边线的样式 */
    var leftValue =$('.point:first').offset().left;
    $('.bottom-line').css('left',leftValue+'px');
})
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
/* 
 *返回按钮
 */
$(document).ready(function() {
    $('i.back').click(function() {
        history.back();
    });
});
/* 验证 */
//手机号码验证
function verify_phone(phone) {
    var pattern = /^1[34578]\d{9}$/; 
    return pattern.test(phone); 
}
//数字验证
function fnLimited(inputLimited){
    inputLimited.keydown(function (e) {
        // Allow: backspace, delete, tab, escape, enter and .
        if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 110, 190]) !== -1 ||
             // Allow: Ctrl+A, Command+A
            (e.keyCode === 65 && (e.ctrlKey === true || e.metaKey === true)) || 
             // Allow: home, end, left, right, down, up
            (e.keyCode >= 35 && e.keyCode <= 40)) {
                 // let it happen, don't do anything
                 return;
        }
        // Ensure that it is a number and stop the keypress
        if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
            e.preventDefault();
        }
    });
}