
$(document).ready(function() {  
   $('#provice').empty();
   $.get('/area/get_provice_list/', {}, function(data) {
       var html = '';
       html = '<option value="0">请选择</option>';
       $('#provice').append(html);
       for (var i = 0; i < data.length;i++){
           html = '<option value="' +data[i]['id']+ '">'
                         +data[i]['short_name'] + '</option>';
           $('#provice').append(html);
       }  
   });
   /*
    $('.location, .menu-map-img').click(function(e) {
        e.preventDefault();
        $('#provice').empty();
         
        $.get('/area/get_provice_list/', {}, function(data) {
            var html = '';
            for (var i = 0; i < data.length;i++){
                html = '<option value="' +data[i]['id']+ '">'
                              +data[i]['short_name'] + '</option>';
                $('#provice').append(html);
            }  
        });
    })*/

    $(document).on('change','#provice', function( ) {
        
        $('#city').empty();
        $('#county').empty();
        var provinceid= $('#provice').val();
        $.get('/area/get_city_list/', {provinceid:provinceid}, function(data) {
            var html = '';
            html = '<option value="-1">-市-</option>';
            $('#city').append(html);
            for (var i = 0; i < data.length;i++){
                html = '<option value="' +data[i]['id']+ '">'
                              +data[i]['short_name'] + '</option>';
                $('#city').append(html);
            }  
        });
    });

    $(document).on('change','#city', function( ) { 
        $('#county').empty();
        var cityid= $('#city').val(); 
        $.get('/area/get_county_list/', {cityid:cityid}, function(data) {
            var html = '';
            html = '<option value="-1">-区县-</option>';
            $('#county').append(html);
            for (var i = 0; i < data.length;i++){
                html = '<option value="' +data[i]['id']+ '">'
                              +data[i]['short_name'] + '</option>';
                $('#county').append(html);
            }  
        });
    });
    $('.btn-place-select').click(function(e){
        var value_province = $('#provice').val();
        var value_city = $('#city').val();
        var value_county = $('#county').val();

        var text_province = $('#provice option:selected').text();
        var text_city = $('#city option:selected').text();
        var text_county = $('#county option:selected').text();

        var selectid   = value_province;
        var selectname = text_province;
        if ( parseInt(value_city) > -1)
        {
            selectid = value_city;
            selectname = text_city;
        }
        if ( parseInt(value_county) > -1)
        {
            selectid = value_county;
            selectname = text_county;
        }

        $.get('/area/set_locate_session/', {selectid:selectid, selectname:selectname}, function(data) {
             $('#hidlocationid').val(selectid);
             $('.location').text(selectname);
        });
    });


     $('.location, .menu-map-img').click(function(e) {
        e.preventDefault();
        $('#provice').empty();
         
        $.get('/area/get_provice_list/', {}, function(data) {
            var html = '';
            for (var i = 0; i < data.length;i++){
                html = '<option value="' +data[i]['id']+ '">'
                              +data[i]['short_name'] + '</option>';
                $('#provice').append(html);
            }  
        });
    })


// according to class
    $(document).on('change','.homepage_province', function( ) {
        
        $('.homepage_city').empty();
        $('.homepage_county').empty();
        var provinceid= $('.homepage_province').val();
        $.get('/area/get_city_list/', {provinceid:provinceid}, function(data) {
            var html = '';
            html = '<option value="-1">-市-</option>';
            $('.homepage_city').append(html);
            for (var i = 0; i < data.length;i++){
                html = '<option value="' +data[i]['id']+ '">'
                              +data[i]['short_name'] + '</option>';
                $('.homepage_city').append(html);
            }  
        });
    });

    $(document).on('change','.homepage_city', function( ) { 
        $('.homepage_county').empty();
        var cityid= $('.homepage_city').val(); 
        $.get('/area/get_county_list/', {cityid:cityid}, function(data) {
            var html = '';
            html = '<option value="-1">-区县-</option>';
            $('.homepage_county').append(html);
            for (var i = 0; i < data.length;i++){
                html = '<option value="' +data[i]['id']+ '">'
                              +data[i]['short_name'] + '</option>';
                $('.homepage_county').append(html);
            }  
        });
    }); 
});