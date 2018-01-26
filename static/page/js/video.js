$(document).ready(function(){
    /* 视频弹出框 */
    $('.video-first').on("click",function(){
        $('.v-wrap').show();
    });
    $('.close').on("click",function(){
        $(this).parent('v-wrap').hide();
    });
    
    $('.video-list').on("click",function(){
        $('.v-wrap').show();
    });

    
})