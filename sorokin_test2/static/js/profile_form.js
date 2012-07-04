$(document).ready(function(){
	 // $('#profile_form').ajaxForm();
	 
	var form = $('#profile_form')
	$('.qq-upload-button').live('click', function(){
		$('.qq-upload-list').html('')
	});
	var getAllFields = function(form){
		form = $(form)
		return form.find('input, select, textarea')
	}
	var createUploader = function(){
	    var uploader = new qq.FileUploader({
	        element: $('#photo-uploader')[0],
	        action: form.attr('upload_action'),
	        debug: false,
	        multiple: false,
	        allowedExtensions: ['jpg', 'jpeg', 'png'],
	        params : {"CSRFToken": getCookie('csrftoken')},
	        onComplete: function(id, fileName, responseJSON){
	        	if(responseJSON.success){
	        		$('.photo').attr('src', responseJSON.url)
	        	}
	        },
	        // template: $('photo_uploader_template').html(),
	        fileTemplate: '<li>' +
	                '<span class="qq-upload-file"></span>' +
	                '<span class="qq-upload-spinner"></span>' +
	                '<span class="qq-upload-size"></span>' +
	                '<a class="qq-upload-cancel" href="#">Cancel</a>' +
	            '</li>',
	    });      
	}
	createUploader();
    $('#profile_form').live('submit', function(event){
    	console.log('submit')
    	
    	$.ajax({
    		url: form.attr('action'),
    		type: form.attr('method'),
    		data: $('#profile_form').formSerialize(),
	    	success: function(data){
	    		data = $(data)
	    		if(data.find('.errorlist').length){
		    		$('#profile_form').replaceWith(data)
		    		createUploader();
	    		}else{
	    			document.location.href = $('#profile_form').attr('success_url')
	    		}
	    	},
	    	beforeSend: function(){
	    		$('#spiner').show()
	    		getAllFields('#profile_form').attr('disabled', 'disabled')
	    	}
		})
		return false
	})     
});
