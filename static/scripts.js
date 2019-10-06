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
	

	$('form').on('submit',function(){
		var id = $(this).attr('id');
	    var contents = $("div ."+id ).html();
		if(contents.trim().length == 0){
			alert('Please fill the div as well');
			return false;
		}
    	$('textarea#'+id).val(contents);
	    return true;
	});
	


	var state = -1;  //state = 0 text
					//state = 1 list

	$('.exchange').click(function(){
		
		var id = $(this).attr('id');

		var div_text = document.getElementsByClassName(id);
		var text = $('div.'+id).html();
		console.log(id,text);
		
		var n = text.search('<div>');
		if(n == -1)
			state = 1;	//list
		else
			state = 0;	//text
		console.log(n)

		if(state == 1){

			var p_text ='';
			$('div.'+id+' li').each(function(){
				p_text += '<div>'+$(this).text()+'</div>';
			});
		
			$('div.'+id).html(p_text);
		}
		else if (state == 0){
			var text = $('div.'+id).html().replace(/\t/g,"").replace(/\n/g,'').replace('<br>','').split('</div>');
			console.log(text);
			var li_text = '<ul>';
			for(var i=0; i< text.length; i++){
				text[i] = text[i].substring(5);
				if(text[i].length != 0){
					li_text += '<li>'+text[i].trim()+'</li>';
					console.log(text[i]);
				}
			}
			li_text += '</ul>';
			console.log($('div.'+id).html());
			$('div.'+id).html(li_text);
			console.log($('div.'+id).html(li_text));
			console.log(li_text);
		}
    });


});



