$(function(){
    /* 循环得出小计 */
    /* for(var i=0;i<$('.item').length;i++){
        var number =$('.price-sum').eq(i).parents('.item').find('.nub').text(),
            price = $('.price-sum').eq(i).parents('.item').find('.price').text(),
            sum = number*price
        $('.price-sum').eq(i).text(sum);
    } */
    $(".price-sum").each(function(){
        var number =$(this).parents('.item').find('.nub').text(),
            price = $(this).parents('.item').find('.price').text(),
            sum = number*price
            $(this).text(sum);
      });

      /* 关闭弹出窗 */
      $('#cancel').on('click',function () {
          $(this).parents('.pop_wrap').hide();
      })
})
//显示上传的
$('#picture').change(function(){
    var name=  $(this).val();
    $(this).prev().text(name);
})