$('form').submit(function(e){
    if($(this).find('input.filling').val().length==0){//检测星标Input是否为空
        e.preventDefault();
        $().message('请完成所有星标项目！');
    }
})