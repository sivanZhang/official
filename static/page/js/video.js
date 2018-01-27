$(document).ready(function(){
    /* 视频弹出框 */
    $('.video-first').on("click",function(){
        var videoSrc = $(this).attr('data-video');
        $('.v-wrap').show();
        $('.v-wrap').children('video').attr('src',videoSrc);
    });
    $('.close').on("click",function(){
        $('.v-wrap').children('video').attr('src','');
        $(this).parent('.v-wrap').hide();
    });
    
    $('.video-list').on("click",function(){
        var videoSrc = $(this).attr('data-video');
        $('.v-wrap').show();
        $('.v-wrap').children('video').attr('src',videoSrc);
    });
})