$( document ).ready(function() {
	var camContain = $(".camContain");
	setInterval(function() {
		$(".camera").remove();
		var time = Date.now() / 1000 | 0;
		camContain.append("<img class='camera' src='/camFeed?i="+time+"'>");
	}, 4000);
});
