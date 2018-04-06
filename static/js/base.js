
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
        $('#show-btn').children().removeClass('img-close');
    })
    jQuery('#show-btn').click(function (e) {
        jQuery('.btn-list li').slideToggle();
       $(this).children().toggleClass('img-close');
        e.stopPropagation();
    })
    jQuery(document).click(function () {
        jQuery('#user_login_nav').slideUp();
    })

    
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
/* 点击显示qq群二维码 */
$('#qq_group').on('click',function(){
    $('.code-wrap').eq(0).fadeIn(300);
})
$('#wei_group').on('click',function(){
    $('.code-wrap').eq(1).fadeIn(300);
})
$('.close_code').on('click',function(){
    $(this).parents('.code-wrap').fadeOut(300);
})
$('.code-bg').on('click',function(){
    $(this).parents('.code-wrap').fadeOut(300);
})

/* 
 *菜单下边线的样式
 */
$(window).load(function () {

    var leftValue = $('.point:first').offset().left,
        lineWidth = $('body').width()-leftValue;
    topValue = $('.point:first').offset().top;
    $('.bottom-line').css('width',lineWidth+ 'px').css('left', leftValue + 'px').css('top', topValue + 2 + 'px');
})
$(window).resize(function() {
    var leftValue =$('.point:first').offset().left;
    $('.bottom-line').css('left',leftValue+'px');
});
function fixedFooter(){//页面过小时，底部固定
    var docHeight=$('body').height();//整个网页的高度
    var windowHeight= $(window).height();//浏览器可视窗口的高度
    if(docHeight<windowHeight){
        $('.linkitems').css({'position':'fixed','bottom':'40px','width':'100%'});
        $('footer').css({'position':'fixed','bottom':'0px','width':'100%'});
    }
}