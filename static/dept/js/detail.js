$(document).ready(function() {  
    fnLimited($('#phone'));
    doubleclick = false;//避免双击的代码
    $("#send").click(function(){
        if (doubleclick == false){
            doubleclick =true;
        }
        else{
            return;
        }

        //
        var options = {
            theme: "sk-doc",
            message: '提交中...',
            backgroundColor: "#000",
            textColor: "white"
        };
        
        var deptid = $('#deptid').val();
        var phone = $('#phone').val();
        
        var phone_mark = verify_phone(phone);
        if (!phone_mark)
        { 
            $().errormessage('手机格式不正确');
            return;
        }
        var sec=60;
        $("#send").attr({"disabled":"disabled"});
        var inter = setInterval(function(){
            sec --;
            if (sec ==0){
                $("#send").removeAttr("disabled");
                $("#send").val("已发送");
                clearInterval(inter);
            }
            else{
                $("#send").val(sec.toString() +"后重新发送..."); 
            } 
        }, 1000); 
        data = {
            
            'deptid': deptid,
            'phone': phone, 
            'csrfmiddlewaretoken': getCookie('csrftoken'),
        }; 
        HoldOn.open(options);
        $.ajax({
            type: 'post',
            url: '/dept/send/',
            data: data,
            success: function(result) {
                HoldOn.close(); 
                if (result['status'] == 'ok')
                {
                    $().message(result['msg']);
                }
                else{
                    $().errormessage(result['msg'])
                }
            },
            error: function() {
                HoldOn.close(); 
                // 500
                alert('server is down!')
            }
        });
        doubleclick = false;
    }) 
});
