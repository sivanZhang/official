$(document).ready(function(){
    /* 图片弹出框 */
    $('.active-img').on("click",function(){
        $('.high_definition').show();
        $('#pic_wall').attr('src','');
        var imgSrc=$(this).attr('src');
        $('#pic_wall').attr('src',imgSrc);
        /* 下一张 */
       /*  var imgIndex=$(this).index();
        $('#more').on("click",function(){
            var imgIndex=imgIndex+1;
            var nextSrc=$(".pic-list img").index(imgIndex).attr('src');
            $('#pic_wall').attr('src',nextSrc); 
        }) */
    });
    /* 关闭按钮 */
    $('.close').on("click",function(){
        $('.high_definition').hide();
    });
})