
$(document).ready(function(){
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
    $('.roll-tip').click(function(){ 
        $('.div-roll-tip-up').show();
    })
    

    var advice = $('.advice');//安全使用建议
    var fitting = $('.fitting');//配件介绍
    var scene = $('.scene');//应用场景
    var parameter = $('.parameter');//技术特性
    var character = $('.character');//特性
    
    //$('.swiper-slide').css({'margin':height/2+'px ' + (width/2-20) + 'px'});
    
    $(document).scroll(function() { 
         var scrollheight = $(document).scrollTop();
         if (scrollheight > 100)
         {
             ////显示快捷按钮
             $('.scroll-tip').show('slow');
             if (scrollheight + height + 360  > $(document).height() )
             {
                 //
                 $('.scroll-down').hide('slow');
             }
             else{
                 $('.scroll-down').show('slow');
             }
         }
         else{
             ////移除 top menu的fix
             $('.scroll-tip').hide('slow');
         }

         if (scrollheight > height-60)
         { 
             //移除 top menu的fix
             $('.menu-holder').addClass('menu-hidden');
             $('.container-second-menu').addClass('second-menu-fixed');
             
             
             //场景应用菜单
             if (scrollheight > height)
             { 
                $('.panel-menu').addClass('panel-menu-fixed'); 
                //fitting-panel-menu
                $('.fitting-panel-menu').addClass('panel-menu-fixed'); 
             }
             else{
                //移除 top menu的fix 
                $('.panel-menu').removeClass('panel-menu-fixed');  
                $('.fitting-panel-menu').removeClass('panel-menu-fixed'); 
             }
         }
         else{ 
             $('.menu-holder').removeClass('menu-hidden');
             $('.container-second-menu').removeClass('second-menu-fixed');
         } 
    });

    $('.roll-tip-up').click(function(e){
        //$(document).scrollTop(height);// 
        //$(this).parent().hide( );
        $(this).parent().slideToggle();
    });
    var body = $("html, body");
        body.stop().animate({scrollTop:0}, 500, 'swing', function() { 
         //
        });
    $(document).on('click', '.scroll-down', function(){
        //
        var scrollheight = $(document).scrollTop();
        var body = $("body");
        body.animate({scrollTop:height + scrollheight+60}, '500');
    })

    $(document).on('click', '.scroll-up', function(){
        //
        var scrollheight = $(document).scrollTop();
        var body = $("body");
        body.animate({scrollTop: (scrollheight-height-60)}, '500');
    })

   
    function submenu (selectot){
        $(selectot).click(function(e){
                e.preventDefault();
                var target = $(this).attr('target');
               // $('#'+target).show('slow');
              // $('#'+target).show(  );
               $('#'+target).slideToggle(  );
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
    function sec_menu(sec )
    {
        advice.hide();
        fitting.hide();
        scene.hide();
        parameter.hide();
        character.hide();

        switch(sec)
        {
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
              advice.show();break;
        }
    }

    $('.a_secondmenu_item').click(function(e){
        //
        e.preventDefault();
        var $this = $(this);
        var sec = $this.attr('target');

        console.log(sec);
        $('.tb_secondmenu_item').removeClass('active');
        $($this.parent()).addClass('active'); 
        sec_menu(sec );
    })
})


 