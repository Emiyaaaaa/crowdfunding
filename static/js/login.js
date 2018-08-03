$(document).ready(function() {
				$("#fadein").addClass("animated fadeIn")
				$(".login").click(function() {
					$(".login_background").css("display", "block")
					$(".login_box").css("display", "block")
				});
				$(".login_background").click(function(){
					$(".login_background").css("display", "none")
					$(".login_box").css("display", "none")
				});
			});