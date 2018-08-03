$(document).ready(function() {
		if(!(/msie [6|7|8|9]/i.test(navigator.userAgent))) {
				(function() {
					window.scrollReveal = new scrollReveal({
						reset: true
					});
				})();
			};
		// 绑定表情
		$('.face-icon').SinaEmotion($('.text'));
		// 测试本地解析
	
		$("#submitbutton").click(function(){
			var inputText = $('.text').val();
			$('#info-show ul').append(reply(AnalyticEmotion(inputText)));
		});
		var html;
		function reply(content){
			html  = '<li>';
			html += '<div class="head-face">';
			html += '<img src="img/girl.png" / >';
			html += '</div>';
			html += '<div class="reply-cont">';
			html += '<p class="username">小航</p>';
			html += '<p class="comment-body">'+content+'</p>';
			html += '<p class="comment-footer">2016年10月5日　回复　点赞54　转发12</p>';
			html += '</div>';
			html += '</li>';
			return html;
		}
		function showHint() {
			var xmlhttp;
			if(window.XMLHttpRequest) {
				// IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
				xmlhttp = new XMLHttpRequest();
			} else {
				// IE6, IE5 浏览器执行代码
				xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
			}
			xmlhttp.onreadystatechange = function() {
				if(xmlhttp.readyState == 4 && xmlhttp.status == 200) {
					document.getElementById("intro_txt").innerHTML = xmlhttp.responseText;
				}
			}
			xmlhttp.open("GET", "ajax_info.txt", true);
			xmlhttp.send();
		}
		showHint()
});