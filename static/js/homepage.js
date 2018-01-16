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
        debugger: true
    });
});

$(document).ready(function(){
/* 
 *隐藏菜单切换 
 */
    $('#show-btn').click(function(){
        $('.btn-list li').slideToggle();
    })
})


