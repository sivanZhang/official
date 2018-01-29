$(document).ready(function() {  
    $('.delete').click(function(){
        var deptid = $(this).attr("deptid");
        data = {
            'method': 'delete',
            'id': deptid, 
            'csrfmiddlewaretoken': getCookie('csrftoken'),
        }; 
        $.ajax({
            type: 'post',
            url: '/dept/list/',
            data: data,
            success: function(result) {
                HoldOn.close(); 
                if (result['status'] == 'ok')
                {
                    $().message(result['msg']);
                    setTimeout(function() {
                        location.reload();
                    }, 3000);
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
        })
    });
    fnLimited($('#phone'));
    $("#add").click(function(){
        //
        var options = {
            theme: "sk-doc",
            message: '提交中...',
            backgroundColor: "#000",
            textColor: "white"
        };
        
        var name = $('#name').val();
        var storetype = $('#storetype').val();
        var phone = $('#phone').val(); 
        var detail = CKEDITOR.instances['id_detail'].getData();
        var address = $('#address').val();
        var data_type = $('#data_type').val();
        var area = 0;
        var latitude = $('#latitude').val();
        var longitude = $('#longitude').val();
       
        if ($('#county').val() == null || $('#county').val()  == "-1")
        {
            //area = $('#county').val();
            $().errormessage('请选择区县');
            return;
        }
        if (data_type == undefined){
            data_type = 0;
        }
        area = $('#county').val();  
        data = {
            'method': 'create',
            'name': name,
            'storetype': storetype,
            'phone': phone,
            'detail': detail,
            'address': address,
            'area' :area, 
            'longitude':longitude,
            'latitude':latitude,
            'data_type':data_type,
            'csrfmiddlewaretoken': getCookie('csrftoken'),
        }; 
        HoldOn.open(options);
        $.ajax({
            type: 'post',
            url: '/dept/list/',
            data: data,
            success: function(result) {
                HoldOn.close(); 
                if (result['status'] == 'ok')
                {
                    $().message(result['msg']);
                    setTimeout(function() {
                        location.reload();
                    }, 3000);
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
        })
    })
    $('.django-ckeditor-widget').addClass('col-xs-9');
});
