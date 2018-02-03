$(document).ready(function(){
   $("#sub").click(function(){
       if ( !$("#sub_agreement").is(':checked') ){
           $().errormessage("您必须接受我们的条件...");
           return;
       }
       if ( $("#sub_name").val() == '' ){
            $().errormessage("请输入您的姓名...");
            return;
        }
        if ( $("#sub_email").val() == ''){ 
            $().errormessage("请输入您的邮箱...");
            return;
        }
        else{
            if (!isEmail( $("#sub_email").val() ) ){
                $().errormessage("邮箱格式不正确...");
                return;
            }
        }
        name = $("#sub_name").val() ;
        email = $("#sub_email").val();
        data = {
            'method': 'create',
            'name': name,
            'email': email, 
            'csrfmiddlewaretoken': getCookie('csrftoken'),
        };
      
      
        $.ajax({
                type: 'post',
                url: '/subscribe/list/',
                data: data,
                success: function(result) { 
                    $().message("已提交订阅...");
                    $("#sub_email").val('');
                    $("#sub_name").val('') ;
                },
                error: function() {
                    alert('server is down!')
                }
            })
        });
});