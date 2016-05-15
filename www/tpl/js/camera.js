$( document ).ready(function() {
	var camContain = $(".camContain");
	var i = 0;
	setInterval(function() {
		$(".camera").remove();
		camContain.append("<img class='camera' src='/camFeed?i="+i.toString()+"'>");
		i = i+1;
	}, 1000);
});
