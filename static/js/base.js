
$(document).ready(function(){
    var height = window.innerHeight;
    var width = window.innerWidth;
    $('.product_sec_menu').hide();

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

$(document).ready(function () {
    var leftValue = $('.point:first').offset().left,
    topValue = $('.point:first').offset().top;
    /* 菜单下边线的样式 */
    $('.bottom-line').css('left', leftValue + 'px').css('top', topValue + 2 + 'px');
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
    $('.menu-list td').mouseenter(function(){
        $(this).find('.point').addClass('orange-point');
    })
    $('.menu-list td').mouseleave(function(){
        $(this).find('.point').removeClass('orange-point');
    })
    /* 点击页面回收悬浮菜单 */
    jQuery(document).click(function () {
        jQuery('.btn-list li').slideUp();
    })
    jQuery('#show-btn').click(function (e) {
        jQuery('.btn-list li').slideToggle();
        e.stopPropagation();
    })
    jQuery(document).click(function () {
        jQuery('#user_login_nav').slideUp();
    })

    /* 产品页箭头位置 */
    var abslut = $('.logo').offset().left;
    $('.scroll-tip').css('right', abslut+'px')
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
function isEmail(email) {
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
}

$(window).resize(function() {
    var leftValue =$('.point:first').offset().left;
    $('.bottom-line').css('left',leftValue+'px');
});
