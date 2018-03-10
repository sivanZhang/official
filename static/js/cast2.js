
$(document).ready(function () {
    /* 文字定位 */
    var leftValue = $('.logo').offset().left;
    $('.show1,.show3').css('right',leftValue + 'px');
    $('.show2,.show4').css('left',leftValue + 'px');
    transition (360);
    var height = window.innerHeight;
     var width = window.innerWidth;

    $('.icon-img').on('click', function () {
        var thisIcon = $(this),
            thisIndex = $(this).index(thisIcon.parents('.sub-item').find('.icon-img'));
        if (thisIcon.hasClass('act-icon')) {
            return;
        } else {
            thisIcon.parents('table').find('.icon-img').removeClass('act-icon');
            thisIcon.addClass('act-icon');
            thisIcon.parents('.sub-item').find('.hide-watch').hide();
            thisIcon.parents('.sub-item').find('.hide-watch').eq(thisIndex).show();
        }
    });
    /* var iconLength = $('.icon-img').length;
    for(var i = 0;i<iconLength;i++){
        $('.icon-img').eq(i).click(function(){
            $(this).parents('table').find('.icon-img').removeClass('act-icon');
            $(this).addClass('act-icon');
            $(this).parents('.sub-item').find('.hide-watch').hide();
            $(this).parents('.sub-item').find('.hide-watch').eq(i).show();
        })
    } */
   /*  var icon =$('.icon-img'),
        watch = $('.hide-watch');
        for(var i=0;i<icon.length;i++){
            //鼠标移入显示，移出隐藏
          ~function(i){                               //匿名函数立即执行
            $('.sub-item').on('click',icon[i],function(){
                if($(icon[i]).hasClass('act-icon')){
                    return;
                }else{
                    $(icon[i]).parents('table').find('.icon-img').removeClass('act-icon');
                    $(icon[i]).addClass('act-icon');
                }
                $(watch[i]).show();
              });   
          }(i);
        };   icon.on('click',function(){
            if($(this).hasClass('act-icon')){
                return;
            }else{
                $(this).parents('table').find('.icon-img').removeClass('act-icon');
                $(this).addClass('act-icon');
            }
            watch.show();
          });    */


          
        /* aSub.mouseenter(function(){
            $(this).show();
          });
          aSub.mouseleave(function(){
            $(this).hide();
          }); */
     /*$('.icon-img').on('click',function(){
         if($(this).hasClass('act-icon')){
            return;
        }else{
        $(this).parents('table').find('.icon-img').removeClass('act-icon');
        $(this).addClass('act-icon')
        
        } 
        $(this).parents('.sub-item').find('.hide-watch').hide();
        $(this).parents('.sub-item').find('.hide-watch').eq($(this).index()).show();
    }) */
    








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

  
    $(document).ready(function(){
        /* 轮播图箭头位置 */
        var abslut = $('.logo').offset().left;
        /* 产品页到顶部位置 */
        $('.scroll-tip').css('right', abslut+'px')
    })
    
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
/* 隐藏板块标签页功能 */
    
