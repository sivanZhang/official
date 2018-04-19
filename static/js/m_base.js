
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
$('.group-title').each(function(){
    $(this).on('touchstart',function(){
        var display = $(this).next('.footer_links').css('display');
        $(this).next('.footer_links').slideToggle();
        if( display=='none'){
            $(this).children('.show-btn').addClass('rota');
        }else{
            $(this).children('.show-btn').removeClass('rota');
        }
    })
})
$('#link').on('touchstart',function(){
    $('nav ul').slideToggle();
    if($('nav').hasClass('act')){
        $('nav').removeClass('act');
        $(this).attr('src','/static/img/icon/category.svg')
    }else{
        $('nav').addClass('act');
        $(this).attr('src','/static/img/icon/close_nav.svg')
    }
})
//回到顶部
$('#to_top').on('touchstart',function () {
    $('html, body').animate({
        scrollTop: $('body').offset().top
    }, 300);
})
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
$(function(){
    var height = window.innerHeight;
    $('nav ul').height(height-60);
})