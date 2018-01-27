$(document).ready(function() {  
    $('select').change(function(){
        $("#search").submit();
    });
    $('#provice option[value="420000"]').attr('selected','selected');
    //$("#provice").text("湖南");  
});


