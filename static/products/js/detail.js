/* 
 * 缩略图展示
 */

    var x =$('a.thumbnail_custom img').first().attr('src');
    $('#big_img').attr('src',x);

$('#big_img').height($('#big_img').width()+'px')
$('ul.thumbnail_list').on('mouseenter','a.thumbnail_custom',function(){
    var smallAttr = $(this).children().attr('src');
    var bigAttr = $('#big_img').attr('src');
    $('#big_img').attr('src',smallAttr);
});//缩略图展示end

/* ajax  立即购买*
--------------------------*/
 $('.buy-now').click(function () {
    getLogin(); 
    if ($('.act_box').length === 0) {
        $('.red_msg').remove();
        $('.rule_wrap').append('<p class="red_msg">请选择</p>');
    } else {
        var url = '/shopcar/shopcars/';
        var csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
        var ruleid = $('.act_box').attr('ruleid')
        var quantity = parseInt($('#carnum').text());
        var data = {
            'method': 'create',
            'ruleid': ruleid,
            'num': quantity,
            'csrfmiddlewaretoken': csrfmiddlewaretoken
        }
        $.ajax({
            url: url,
            type: 'post',
            data: data,
            success: function (result) {
                if (result['status'] == 'ok') {
                    $().message(result['msg']);
                    productCookie();
                    window.location.href = '/bill/bills/?new';
                }
                else {
                    $().message(result['msg']);
                }
            },
            error: function () { // 500
                $().errormessage('server is down!');
            }
        });
    }
}); 

/* 商品信息存入COOKIE */
function productCookie(){
    var products = new Array();
    var product = {};
        product.name = $('.item_name').text();
        product.rule = $('.rule_name').text();
        product.img = $('#big_img').attr('src');
        product.Price = $('.unit-price').text();
        product.ruleid = $('.rule_tr').attr('ruleid');
        product.num = $('#carnum').text();
        products.push(product);
    products = JSON.stringify(products);
    CookieUtil.set("products", products, '', "/");
    //cookie保存总价
    var sum_price = $('#total_price').text();
    CookieUtil.set("sum_price", sum_price, '', "/");
};

/* 选中规格效果
--------------------------*/
$('table.table').on('click', '.rule_tr', function () {
    $('.red_msg').remove();
    $(this).siblings().removeClass('act_box');
    $(this).addClass('act_box');
    $('.table').find('.red_msg').remove();
    $('.stock_copy').text($(this).children('.stock').text());
    $('#total_price').text($('.act_box').children('.unit-price').text() * $('.carnum').text());
});

/* 加 
--------------------------*/
$('.btn-group').on("click", '.addition', function () {
    var quantity = parseInt($(this).next().text());
    var nStock = parseInt($('.stock_copy').text());
    if (quantity >= nStock) {
        $(this).next().text(nStock)
    } else { $(this).next().text(quantity + 1); }
    //价格变动
     $('#total_price').text($('.act_box').children('.unit-price').text() * $('.carnum').text());
});

/* 减去 
--------------------------*/
$('.btn-group').on("click", '.subtraction', function () {
    var quantity = parseInt($(this).prev().text());
    if (quantity <= 1) {
        $(this).prev().text(1);
    } else {
        $(this).prev().text(quantity - 1);
    }
    //价格变动
    $('#total_price').text($('.act_box').children('.unit-price').text() * $('.carnum').text());
});

/*加入购物车提交程序封装
--------------------------*/
function ajaxSubmit() {
    var url = '/shopcar/shopcars/';
    var csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
    var ruleid = $('.act_box').attr('ruleid')
    var quantity = parseInt($('#carnum').text());
    var data = {
        'method': 'create',
        'ruleid': ruleid,
        'num': quantity,
        'csrfmiddlewaretoken': csrfmiddlewaretoken
    }
    $.ajax({
        url: url,
        type: 'post',
        data: data,
        success: function (result) {
            if (result['status'] == 'ok') {
                $().message(result['msg']);
            }
            else {
                $().message(result['msg']);
            }
        },
        error: function () { // 500
            $().errormessage('server is down!');
        }
    });
}

/*“加入购物车”按钮绑定事件*
--------------------------*/
 $('.add-cart').click(function () {
    getLogin();
    if ($('.act_box').length === 0) {
        $('.rule_wrap').find('.red_msg').remove();
        $('.rule_wrap').append('<p class="red_msg">请选择</p>');
    } else {
        ajaxSubmit();
    }
});

//bootstrap标签页
$('#myTab a').click(function (e) {
    e.preventDefault()
    $(this).tab('show')
  });

/* ajax  镶嵌评价页
--------------------------*/
var productid=$('#productid').val();
$(document).ready(function(){
    $.get("/comment/comment/?id="+productid, {}, function(result){
        $('#com_wrap').append(result);
    })
});

/* 限制价格小数点后面两位数 */
var total_price=$('#total_price').text()-0;
$('#total_price').text(total_price.toFixed(2));

/* 提交评论后刷新 */
$('#com_wrap').on('click','.publish',function(){
  window.location.reload();
})

window.onload = function(){
    var oTop = document.getElementById("to_top");
    var screenw = document.documentElement.clientWidth || document.body.clientWidth;
    var screenh = document.documentElement.clientHeight || document.body.clientHeight;
    oTop.style.left = screenw - oTop.offsetWidth +"px";
    oTop.style.top = screenh - oTop.offsetHeight + "px";
    window.onscroll = function(){
      var scrolltop = document.documentElement.scrollTop || document.body.scrollTop;
      oTop.style.top = screenh - oTop.offsetHeight + scrolltop +"px";
    }
    oTop.onclick = function(){
      document.documentElement.scrollTop = document.body.scrollTop =0;
    }
  }  
