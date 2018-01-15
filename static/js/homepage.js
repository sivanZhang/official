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
/* 
 *隐藏菜单切换 
 */
$(document).ready(function(){
    $('#show-btn').click(function(){
        $('.btn-list').slideToggle();
    })
})
