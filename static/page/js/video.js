$(document).ready(function(){
    $('.video-first').on("click",function(){
        $('.v-wrap').show();
    })
    $('.close').on("click",function(){
        $(this).parents('.v-wrap').hide();
    })
})