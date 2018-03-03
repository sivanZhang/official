$(document).ready(function(e){
var height = window.innerHeight;
$('.swiper-container').height(height);
$('.content').height(height);
 var swiper = new Swiper('.swiper-container', {
        pagination: '.swiper-pagination',
        paginationClickable: true,
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',
        // Enable debugger
        debugger: true,
        autoplay : 5000,
        loop : true
    });
});

$(document).ready(function(){
    /* 轮播图箭头位置 */
    var abslut = $('.logo').offset().left;
    $('.swiper-button-prev').css('left', abslut+'px');
    $('.swiper-button-next').css('right', abslut+'px');
    $('.shop-link3').css('left', abslut+60+'px');
})
/* 点击显示微信群二维码 */
$('#weichat').on('click',function(){
    $('.code-wrap').fadeIn(300);
})
$('#close').on('click',function(){
    $('.code-wrap').fadeOut(300);
})
