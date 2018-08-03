$(document).ready(function() {
	$('#search').click(function() {
		$('.link').css("display", "none");

	});

	$("#satisfaction-1").click(function(){
		$.ajax({
            type: "POST",
            url: window.location.href,
            data:{'state':'nosatis'},
            success: function(data){}
        });
		alert("感谢您的评价");
		$('.up').css("display", "none");
	});
	$("#satisfaction-2").click(function(){
		$.ajax({
            type: "POST",
            url: window.location.href,
            data:{'state':'notverysatid'},
            success: function(data){}
        });
		alert("感谢您的评价");
		$('.up').css("display", "none");
	});
	$("#satisfaction-3").click(function(){
		$.ajax({
            type: "POST",
            url: window.location.href,
            data:{'state':'satis'},
            success: function(data){}
        });
		alert("感谢您的评价");
		$('.up').css("display", "none");
	});
	
});