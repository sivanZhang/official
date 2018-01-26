$(document).ready(function(){
    /* 视频弹出框 */
    $('.pic-list img').on("click",function(){
        $('.high_definition').show();
        $('#pic_wall').attr('src','');
    var imgSrc=$(this).attr('src')
        $('#pic_wall').attr('src',imgSrc);
    });
    /* 关闭按钮 */
    $('.close').on("click",function(){
        $('.high_definition').hide();
    });
})