setInterval(function() {
	var image = document.createElement("img");
	var card = document.getElementById("camContain");
	image.className = "camera";
	image.id = "frame";
	image.src= "/video_feed";
	card.appendChild(image);
}, 200);
