$(function () {

  'use strict';

  var console = window.console || { log: function () {} };
  var $image = $('#image');
  var $download = $('#download');
  var $dataX = $('#dataX');
  var $dataY = $('#dataY');
  var $dataHeight = $('#dataHeight');
  var $dataWidth = $('#dataWidth');
  var $dataRotate = $('#dataRotate');
  var $dataScaleX = $('#dataScaleX');
  var $dataScaleY = $('#dataScaleY');
  var options = {
        aspectRatio: 1 / 1,
        preview: '.img-preview',
        crop: function (e) {
          console.log(e.x);
          console.log(e.y);
          console.log(e.width);
          console.log(Math.round(e.height));
          console.log(e.rotate);
          console.log(e.scaleX);
          console.log(e.scaleY);
          
          $dataX.val(Math.round(e.x));
          $dataY.val(Math.round(e.y));
          $dataHeight.val(Math.round(e.height)); 
          $dataWidth.val(Math.round(e.width));
          $dataRotate.val(e.rotate);
          $dataScaleX.val(e.scaleX);
          $dataScaleY.val(e.scaleY); 
        },
      };



  // Cropper
  $image.on({
    'build.cropper': function (e) {
      console.log(e.type);
    },
    'built.cropper': function (e) {
      console.log(e.type);
    },
    'cropstart.cropper': function (e) {
      console.log(e.type, e.action);
    },
    'cropmove.cropper': function (e) {
      console.log(e.type, e.action);
    },
    'cropend.cropper': function (e) {
      console.log(e.type, e.action);
    },
    'crop.cropper': function (e) {
      console.log(e.type, e.x, e.y, e.width, e.height, e.rotate, e.scaleX, e.scaleY);
    },
    'zoom.cropper': function (e) {
      console.log(e.type, e.ratio);
    }
  }).cropper(options);


  // Buttons
  if (!$.isFunction(document.createElement('canvas').getContext)) {
    $('button[data-method="getCroppedCanvas"]').prop('disabled', true);
  }

  if (typeof document.createElement('cropper').style.transition === 'undefined') {
    $('button[data-method="rotate"]').prop('disabled', true);
    $('button[data-method="scale"]').prop('disabled', true);
  }


  // Download
  if (typeof $download[0].download === 'undefined') {
    $download.addClass('disabled');
  }


  // Options
  $('.docs-toggles').on('change', 'input', function () {
    var $this = $(this);
    var name = $this.attr('name');
    var type = $this.prop('type');
    var cropBoxData;
    var canvasData;

    if (!$image.data('cropper')) {
      return;
    }

    if (type === 'checkbox') {
      options[name] = $this.prop('checked');
      cropBoxData = $image.cropper('getCropBoxData');
      canvasData = $image.cropper('getCanvasData');

      options.built = function () {
        $image.cropper('setCropBoxData', cropBoxData);
        $image.cropper('setCanvasData', canvasData);
      };
    } else if (type === 'radio') {
      options[name] = $this.val();
    }

    $image.cropper('destroy').cropper(options);
  });
    // Methods for moblie
  $('.docs-buttons').on('touchstart', '[data-method]', function () {
    var $this = $(this);
    var data = $this.data();
    var $target;
    var result;

    if ($this.prop('disabled') || $this.hasClass('disabled')) {
      return;
    }

    if ($image.data('cropper') && data.method) {
      data = $.extend({}, data); // Clone a new one

      if (typeof data.target !== 'undefined') {
        $target = $(data.target);

        if (typeof data.option === 'undefined') {
          try {
            data.option = JSON.parse($target.val());
          } catch (e) {
            console.log(e.message);
          }
        }
      }

      result = $image.cropper(data.method, data.option, data.secondOption);

      switch (data.method) {
        case 'scaleX':
        case 'scaleY':
          $(this).data('option', -data.option);
          break;

        case 'getCroppedCanvas':
          if (result) {
                   $image.cropper('getCroppedCanvas').toBlob(function (blob) {
                        var formData = new FormData();

                                    formData.append('thumbnail', blob);

                                    $.ajax('/product/products/4/', {
                                        method: "POST",
                                        data: formData,
                                        processData: false,
                                        contentType: false,
                                        success: function (data) {
                                        if (data['status'] == 'OK') {
                                                data['file'] = data['file'].replace('\\', '/');
                                                $('#id_portrait_upload').css("background-image", "url(" + data['file'] + ")");
                                                $('#id_user_portrait').css("background-image", "url(" + data['file'] + ")");
                                                $('#mark').val('1');
                                                $().message(data['msg']);
                                            }
                                            else {
                                                $('.div_err').append('<label class="err_label" >' + data['msg'] + '</label>'); //
                                            }
                                        },
                                        error: function () {
                                        console.log('Upload error');
                                        }
                                    });
                     });      
          
          }

          break;
      }

      if ($.isPlainObject(result) && $target) {
        try {
          $target.val(JSON.stringify(result));
        } catch (e) {
          console.log(e.message);
        }
      }

    }
  });
  

  // Keyboard
  $(document.body).on('keydown', function (e) {

    if (!$image.data('cropper') || this.scrollTop > 300) {
      return;
    }

    switch (e.which) {
      case 37:
        e.preventDefault();
        $image.cropper('move', -1, 0);
        break;

      case 38:
        e.preventDefault();
        $image.cropper('move', 0, -1);
        break;

      case 39:
        e.preventDefault();
        $image.cropper('move', 1, 0);
        break;

      case 40:
        e.preventDefault();
        $image.cropper('move', 0, 1);
        break;
    }

  });


  // Import image
  var $inputImage = $('#inputImage');
  var URL = window.URL || window.webkitURL;
  var blobURL;

  if (URL) {
    $inputImage.change(function () {
      var files = this.files;
      var file;

      if (!$image.data('cropper')) {
        return;
      }

      if (files && files.length) {
        file = files[0];

        if (/^image\/\w+$/.test(file.type)) {
          blobURL = URL.createObjectURL(file);
          $image.one('built.cropper', function () {

            // Revoke when load complete
            URL.revokeObjectURL(blobURL);
          }).cropper('reset').cropper('replace', blobURL);
          $inputImage.val('');
        } else {
          window.alert('Please choose an image file.');
        }
      }
    });
  } else {
    $inputImage.prop('disabled', true).parent().addClass('disabled');
  }

});

/*
$(document).ready(function() {
    function getWidth() {
        if (self.innerWidth) {
            return self.innerWidth;
        }
        
        if (document.documentElement && document.documentElement.clientHeight) {
            return document.documentElement.clientWidth;
        }
        
        if (document.body) {
            return document.body.clientWidth;
        }
    }
    
    function getHeight() {
        if (self.innerHeight) {
            return self.innerHeight;
        }
        
        if (document.documentElement && document.documentElement.clientHeight) {
            return document.documentElement.clientHeight;
        }
        
        if (document.body) {
            return document.body.clientHeight;
        }
    }
    var canvasHeight = window.innerHeight * 0.45;
    $('.img-container').css('height', canvasHeight.toString()+'px');
    var screenwidth = window.innerWidth;
    var menuwidth=screenwidth*0.75;
    var coinwidth= (menuwidth-30)/3 - 5;
    menuwidth +=  7;
    //var left =  (screenwidth - menuwidth)/2-12;
    var left =  screenwidth * 0.1; 
        $('#demo_box').popmenu({
        'controller': true,       // use control button or not
        'width': menuwidth+'px',        // width of menu 
        'background': '#34495e',  // background color of menu
        'focusColor': '#1abc9c',  // hover color of menu's buttons
        'borderRadius': '10px',   // radian of angles, '0' for right angle
        'top': '0',              // pixels that move up
        'left': '-'+left,              // pixels that move left
        'iconSize': coinwidth+'px',       // size of menu's buttons
        'color': '#fff',            // color of menu's text
        'border': '1px solid #000' // border style for the menu box
     });
});

*/