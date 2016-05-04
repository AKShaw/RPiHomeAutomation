setInterval(function() {
	$(".camera").remove()
	var image = document.createElement("img");
	var card = $(".camContain")
	image.className = "camera";
	image.id = "frame";
	var timeNow = Math.floor(Date.now()/1000)
	image.src= "/video_feed"+"?"+ String(timeNow);
	card.append(image);
}, 1000);
