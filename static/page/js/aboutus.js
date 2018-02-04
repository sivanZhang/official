$(document).ready(function(){
    var windowHeight = window.innerHeight;
    $('section').css('height', windowHeight - 100 + 'px');
    $('.swiper-wrapper').css('height', windowHeight+ 'px');
    /* 
     *隐藏菜单切换 
     */
    $('#show-btn').click(function(){
        $('.btn-list li').slideToggle();
    })
    /* 轮播图箭头位置 */
    var abslut = $('.logo').offset().left;
    $('.swiper-button-prev').css('left', abslut+'px')
    $('.swiper-button-next').css('right', abslut+'px')
})
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
            loop : true
    });
});