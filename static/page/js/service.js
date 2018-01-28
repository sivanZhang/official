$(document).ready(function(){
    /* 点击加减号 */
    $('.show-btn').on('click',function(){
        var answer = $(this).next('.answer');
        if(answer.css('display')=='none'){
            answer.slideDown()
            $(this).text('-');
        }else{
            answer.slideUp()
            $(this).text('+');
        }
        if(answer.length<1){
            alert('该问题没有回答！');
        }
    })
})