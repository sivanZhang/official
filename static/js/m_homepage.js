$(document).ready(function(){
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
$('.sider0 img').load(function(){
    var marginLeft=0-$('.sider0 img').width()/2;
    $('.sider0 img').css('margin-left',marginLeft+'px');
})

