$('form').submit(function(e){
    for(var i=0;i < $('input.filling').length ;i++){
        if($('input.filling').eq(i).val()==''){//检测星标Input是否为空
            e.preventDefault();
            var msg= $('input.filling').eq(i).attr('placeholder');
           /*  $().message('带有“ * ”的必填项目不能为空！'); */
           $().message(msg+'不能为空！');
           $('input.filling').eq(i).focus();
           break;
        }
    }
})
$('[name="phone_number"]').blur(function(){
    var myreg = /^(((13[0-9]{1})|(15[0-9]{1})|(17[0-9]{1})|(18[0-9]{1}))+\d{8})$/; 
    var mobile=$(this).val();
    if(mobile.length!=11 || !myreg.test(mobile)) 
    { 
        $('[name="phone_number"]').focus();
        $().message('请输入有效的手机号码！');
    }
})