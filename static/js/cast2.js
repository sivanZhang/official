
$(document).ready(function () {
    var leftValue = $('.logo').offset().left;
    $('.show1,.show3').css('right',leftValue + 'px');
    $('.show2,.show4').css('left',leftValue + 'px');
    transition (360);
    //
    var height = window.innerHeight;
    var width = window.innerWidth;
    $('.swiper-container').height(height);
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
            ////移除 top menu的fix
            $('.scroll-tip').fadeOut('slow');
        }

        if (scrollheight > height - 60) {
            //移除 top menu的fix
            $('.menu-holder').addClass('menu-hidden');
            $('.container-second-menu').addClass('second-menu-fixed');


            //场景应用菜单
            if (scrollheight > height) {
                $('.panel-menu').addClass('panel-menu-fixed');
                //fitting-panel-menu
                $('.fitting-panel-menu').addClass('panel-menu-fixed');
            }
            else {
                //移除 top menu的fix 
                $('.panel-menu').removeClass('panel-menu-fixed');
                $('.fitting-panel-menu').removeClass('panel-menu-fixed');
            }
        }
        else {
            $('.menu-holder').removeClass('menu-hidden');
            $('.container-second-menu').removeClass('second-menu-fixed');
        }
    });

    $('.roll-tip-up').click(function (e) {
       /*  $(document).scrollTop(height); */
        //$(this).parent().hide( );
        $(this).parent().slideToggle();
    });
    var body = $("html, body");
    body.stop().animate({ scrollTop: 0 }, 500, 'swing', function () {
        //
    });
    /* 
     *隐藏菜单切换 
     */
    $(document).on('click', '#show-btn', function () {
        $('.btn-list li').slideToggle();
    })
    /* 
     *回到顶部
     */
    
    $(document).on('click', '.scroll-up', function () {
        $('html, body').animate({
            scrollTop: $('body').offset().top
         }, 300);
    })

    function submenu(selectot) {
        $(selectot).click(function (e) {
            e.preventDefault();
            var target = $(this).attr('target');
           /* var newPos=new Object();
                newPos.top="0"; */
               
            $('#' + target).fadeToggle( function(){
                /* 隐藏元素到视口顶部 */
            $('html, body').animate({
                scrollTop: $('#' + target).offset().top-60
             }, 600);
            });
            $('#' + target).addClass('move');
            if( $('#' + target).css('display')==='none'){
                $('#' + target).removeClass('move');
            }
        });
    };
  
    submenu('.product_pic_1');
    submenu('.product_pic_2');
    /*
        
   $('.product_pic_1').click(function(e){
                   e.preventDefault();
                   var target = $(this).attr('target');
                  // $('#'+target).show('slow');
                  $('#sub-item11').slideToggle(  );
               });*/
    //二级菜单切换
    function sec_menu(sec) {
        advice.hide();
        fitting.hide();
        scene.hide();
        parameter.hide();
        character.hide();

        switch (sec) {
            case 'advice':
                advice.show();
                break;
            case 'fitting':
                fitting.show();
                break;
            case 'scene':
                scene.show();
                $('.div-roll-tip-up').hide();
                break;
            case 'parameter':
                parameter.show();
                break;
            case 'character':
                character.show();
                break;
            default:
                advice.show(); break;
        }
    }

    $('.a_secondmenu_item').click(function (e) {
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
     *板块高度
     */
    var windowHeight = window.innerHeight;
    $('section,.img360_holder').css('height', windowHeight+ 'px');
});
/* 内容过渡浮现效果 */
$(window).scroll(function(){
    transition (1);
    transition (2);
    transition (3);
    transition (4);
});
function transition (nub){
    var scrollTop = $(window).scrollTop(),
    windowHeight = window.innerHeight,
    elHtight =$('.show'+nub).height();
    elementOffset = $('.show'+nub).offset().top,
    distance= (elementOffset - scrollTop);
    /* = $(el).offset().top-60*/
    if(distance+elHtight<= windowHeight){
        $('.show'+nub).parent('section').addClass('move');
    }else{
        $('.show'+nub).parent('section').removeClass('move');
    }
}