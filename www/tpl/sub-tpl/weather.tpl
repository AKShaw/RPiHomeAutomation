<div id="card" style="background: linear-gradient(#{{weather["color"][0]}}, #{{weather["color"][1]}}); color:#fff;">
	<div>
	<div class="col-xs-6">
		<h5>Location information:</h5>
		<h2 class="title">{{weather["location"]}}</h2>
		<h4>{{weather["date"][0]}} {{weather["date"][1]}}</h4>
		<h5>{{weather["status"]}}</h5>
	</div>
	<div class="col-xs-6">
		<h5>Outdoor temperatures:</h5>
		<h1 class="title">{{weather["temps"][0]}}&deg;C</h1>
		<h5>Min: {{weather["temps"][1]}}&deg;C</h5>
		<h5>Max: {{weather["temps"][2]}}&deg;C</h5>
	</div>
	</div>
	<div>
	<div class="col-xs-6">
		<h5>Wind speed: {{weather["windSpeed"]}} m/s</h5>
	</div>
	<div class="col-xs-6">
		<h5>Humidity: {{weather["humidity"]}}%</h5>
	</div>
	</div>
</div>