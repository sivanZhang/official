$(document).ready(function(){
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

$('#to_next').on('click', function () {
    $('html, body').animate({
        scrollTop: $('.swiper-container').offset().top
    }, 300);
})