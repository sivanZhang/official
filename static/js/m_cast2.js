
$(document).ready(function () {

    var height = window.innerHeight;
    var width = window.innerWidth;


    //隐藏板块点击图标切换图
    $('.icon-img').on('touchstart', function () {
        var thisIcon = $(this),
            //获取下标
            thisIndex = $('.icon-img').index($(this));
        if (thisIcon.hasClass('act-icon')) {
            return;
        } else {
            thisIcon.parents('.hide-right').find('.icon-img').removeClass('act-icon');
            thisIcon.addClass('act-icon');
            thisIcon.parents('.sub-item').find('.hide-watch').hide();
            thisIcon.parents('.sub-item').find('.hide-text').hide();
            $('.hide-watch').eq(thisIndex).show();
            $('.hide-text').eq(thisIndex).show();
        }
    });

    $('.advice').hide();
    $('.parameter').hide();
    $('.scene').hide();
    $('.fitting').hide();
    $('.sub-item').hide();
    $('.scroll-tip').hide();
    $('.div-roll-tip-up').hide();
    $('.roll-tip').click(function () {
        $('.div-roll-tip-up').show();
    })


    var advice = $('.advice');//安全使用建议
    var fitting = $('.fitting');//配件介绍
    var scene = $('.scene');//应用场景
    var parameter = $('.parameter');//技术特性
    var character = $('.character');//特性



    $(document).scroll(function () {

        var scrollheight = $(document).scrollTop();
        if (scrollheight > 100) {
            ////显示快捷按钮
            $('.scroll-tip').fadeIn('slow');
        }
        else {
            $('.scroll-tip').fadeOut('slow');
        }

        if (scrollheight > height) {
            //移除 top menu的fix
            $('.menu-holder').addClass('menu-hidden');
            $('.container-second-menu').addClass('second-menu-fixed');
          
        }
        else {
            $('.menu-holder').removeClass('menu-hidden');
            $('.container-second-menu').removeClass('second-menu-fixed');
        }
    });

    $('.roll-tip-up').on('touchstart', function (e) {
        /*  $(document).scrollTop(height); */
        //$(this).parent().hide( );
        $(this).parent().slideUp();
    });
    var body = $("html, body");
    body.stop().animate({ scrollTop: 0 }, 500, 'swing', function () {
        //
    });



    /* 
     *回到顶部
     */

    $(document).on('touchstart', '.scroll-up', function () {
        $('html, body').animate({
            scrollTop: $('body').offset().top
        }, 300);
    })
    $('#to_next').on('touchstart', function () {
        $('html, body').animate({
            scrollTop: $('.container-second-menu').offset().top
        }, 300);
    })

    function submenu(selectot) {
        $(selectot).on('touchstart', function (e) {
            e.preventDefault();
            var target = $(this).attr('target');
            /* var newPos=new Object();
                 newPos.top="0"; */

            $('#' + target).fadeToggle(function () {
                /* 隐藏元素到视口顶部 */
                $('html, body').animate({
                    scrollTop: $('#' + target).offset().top - 50
                }, 600);
            });
            $('#' + target).addClass('move');
            if ($('#' + target).css('display') === 'none') {
                $('#' + target).removeClass('move');
            }
        });
    };
    $('.submenu').on('touchstart', function (e) {
        $('#more').slideToggle();
        e.stopPropagation();
    })
    jQuery(document).on('touchstart', function () {
        jQuery('#more').slideUp();
    })
    $('.back').on('touchstart', function() {
        window.location.href="/product/products/cast2/";
    })

    submenu('.product_pic_1');
    submenu('.product_pic_2');

    function sec_menu(sec) {
        advice.hide();
        fitting.hide();
        scene.hide();
        parameter.hide();
        character.hide();

        switch (sec) {
            case 'advice':
                advice.show();
                $('html, body').animate({
                    scrollTop: $('#to_next').offset().top+55
                }, 300); 
                break;
            case 'fitting':
                fitting.show();
                $('html, body').animate({
                    scrollTop: $('#to_next').offset().top+55
                }, 300); 
                break;
            case 'scene':
                scene.show();
                $('.div-roll-tip-up').hide();
                break;
            case 'parameter':
                parameter.show();
                $('html, body').animate({
                    scrollTop: $('#to_next').offset().top+55
                }, 300); 
                break;
            case 'character':
                character.show();
                break;
            default:
                advice.show(); break;
        }
    }

    $('.a_secondmenu_item').on('touchstart', function (e) {
        //
        e.preventDefault();
        var $this = $(this);
        var sec = $this.attr('target');

        console.log(sec);
        $('.tb_secondmenu_item').removeClass('active');
        $($this.parent()).addClass('active');
        sec_menu(sec);
    })
    /* 
     *直接跳转配件页
     */
    var urlStr = window.location.href;
    if (urlStr.indexOf('fromstore=1') != -1) {//检查链接中是否有此自字符串
        var $this = $('.a_secondmenu_item[target="fitting"]');
        var sec = "fitting";
        console.log(sec);
        $('.tb_secondmenu_item').removeClass('active');
        $($this.parent()).addClass('active');
        sec_menu(sec);
    }
});
/* 内容过渡浮现效果 */
$(window).scroll(function () {
    transition(1);
    transition(2);
    transition(3);
    transition(4);
});
function transition(nub) {
    var scrollTop = $(window).scrollTop(),
        windowHeight = window.innerHeight,
        elHtight = $('.show' + nub).height();
    elementOffset = $('.show' + nub).offset().top,
        distance = (elementOffset - scrollTop);
    /* = $(el).offset().top-60*/
    if (distance + elHtight <= windowHeight) {
        $('.show' + nub).parent('section').addClass('move');
    } else {
        $('.show' + nub).parent('section').removeClass('move');
    }
}
/* 隐藏板块标签页功能 */

