$(document).ready(function(){
	$('ul.ulist li').on('click',function(){
		var getClass = $(this).attr('class');
		$("#content div").text(getClass);
	});


	$("#note-text").on('input', function() {
		var scroll_height = $("#note-text").get(0).scrollHeight;
		console.log(scroll_height,'hello');
		$("#note-text").css('height', scroll_height + 'px;');
		$("#note").css('height', scroll_height + 'px;');
	});
});
