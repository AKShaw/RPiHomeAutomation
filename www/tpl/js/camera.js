setInterval(function() {
	$(".camera").remove()
	var image = document.createElement("img");
	var card = $(".camContain")
	image.className = "camera";
	image.id = "frame";
	image.src= "/video_feed";
	card.append(image);
}, 200);
