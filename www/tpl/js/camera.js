$( document ).ready(function() {
	camContain = $(".camContain")
	setInterval(function() {
		$(".camera").remove()
		camContain.append("<img class=\"camera\" src=\"/camFeed\">")
	}, 1000);
});
