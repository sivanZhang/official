

//  发表+存稿按钮    >>> 点击事件
$('.submit button').click(function () {
    //loading样式
    var options = {
        theme: "sk-doc",
        message: '提交中...',
        backgroundColor: "#000",
        textColor: "white"
    };
    HoldOn.open(options);//loadding函数调用
    var categoryid = $('#sel-category').val();
    var title = $('#title').val();
    var desc = $('#desc').val();
    var detail = CKEDITOR.instances['id_detail'].getData();
    var taobaourl = $('#taobaourl').val(); 
    var product = $('#productid');
       
    data = {
        'method': 'create',
        'categoryid': categoryid,
        'title': title,
        'description': desc,
        'detail': detail,
        'taobaourl' :taobaourl, 
        'status': $(this).attr('status'),
        'csrfmiddlewaretoken': getCookie('csrftoken'),
    };
    if (product.length > 0) {
        //3
        data['id'] = product.val();
        data['method'] = 'put'; //修改产品
    }

    var html = '<div class="alert alert-danger" role="alert">####</div>';
    $.ajax({
        type: 'post',
        url: '/product/products/',
        data: data,
        success: function (result) {
            HoldOn.close();
            $('.msg').append(html.replace('###', result['msg']));
        },
        error: function () {
            HoldOn.close();
            // 500
            alert('server is down!')
        }
    })
});

//  属性设置    >>> 添加属性
$('#add-pro').click(function () {
    $(".alert-text").remove();
    var pro = $('#pro').val();
    var val = $('#val').val();
    var proTr = '<tr class="parameter_tr">' +
        '<td class="key "><input type="text" value="' + pro + '"/></td>' +
        '<td class="value "><input type="text" value="' + val + '"/></td>' +
        '<td><i class="fa fa-trash-o" aria-hidden="true"></i></td>' +
        '</tr>';

    if (pro.length == 0 || val.length == 0) {
        var html = '<div class="alert-text">内容不能为空!</div>';
        $('#pro-table').before(html);
    } else {
        $('#pro-table').append(proTr);
        $('#pro,#val').val("");
    };
});

//  属性设置    >>> 删除行
$('#pro-table').on('click', '.fa-trash-o', function () {
    $(this).parent().parent().remove();
});

//  内容简介    >>> 输入字数监听     
$(".ta-wrap input").on('keyup input', function (event) {

    var val = $(this).val();
    var len = val.length;
    var count = $(this).siblings('span');

    if (len == 0) { count.text("0/50"); return; }
    if (len > 50) {
        len = 50;
        $(this).val(val.substring(0, 50));
    }
    count.text(len + "/50");
});

///以下是修改product时用到的js
