$(document).ready(function(){
	$('.notes').css('background-color','rgba(255,140,0,0.3)');


	$('ul.ulist li').on('click', function(){
		var getClass = $(this).attr('class');
		if(getClass =='trash'){
			$('#trash').css('display','block');
			$('#notes').css('display','none');
			$('.trash').css('background-color','rgba(255,140,0,0.3)');
			$('.notes').css('background-color','');
		}
		if(getClass =='notes'){
			$('#notes').css('display','block');
			$('#trash').css('display','none');
			$('.notes').css('background-color','rgba(255,140,0,0.3)');
			$('.trash').css('background-color','');
		}

	});
	
	
	var textarea_array = document.querySelectorAll('textarea');

	textarea_array.forEach(function(textarea) {
		textarea.addEventListener('keydown', function (){
		  	var el = this;
		  	setTimeout(function(){
				el.style.cssText = 'height:auto; padding:0';
				// for box-sizing other than "content-box" use:
				// el.style.cssText = '-moz-box-sizing:content-box';
				el.style.cssText = 'height:' + el.scrollHeight + 'px';
			},0);
		  
			// console.log(this,el.scrollHeight, el.style.cssText);
		});
	});
	
  $('[data-toggle="tooltip"]').tooltip();

});


