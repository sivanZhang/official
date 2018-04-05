$( "#submit" ).on('click', function( event ) { 
    //event.preventDefault();
    var righthtml = '<label id="password-error" class="error " for="password">XXXX</label>';
    var lefthtml = '<label id="password-error" class="error ml" for="password">XXXX</label>';
    email = $("");
    var name = $("#name").val();
    if ($.trim(name) == ''){
        $('.name-error').append(righthtml.replace("XXXX", "请输入姓名..."));
        return false;
    }
    
    if( !verify_phone($("#phone").val())){
        $('.phone-error').append(lefthtml.replace("XXXX", "手机格式不正确..."));
        return false;
    }
/*
    if (!isEmail(email)){
        $('.email-error').append(righthtml.replace("XXXX", "邮箱格式不正确..."));
        return;
    } 
*/
    $( "#buy-form" ).submit();
  });


  fnLimited($('#phone'));