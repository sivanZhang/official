$(document).ready(function(){
    $('.years:first').addClass('act');
    $('.col-active-list:first').css('display','block');
    $('.years span').click(function(){
       if( !($(this).parent().hasClass('act'))){
        $('.col-active-list').slideUp();
        $('.years').removeClass('act');
        $(this).parent().addClass('act');
        $('.act').next('.col-active-list').slideDown();
       }
    })
})