<div class="col-xs-12">
<div id="card">
	<h2 class="title">Configuration</h2>
	<form action="/saveConfig" method="POST">
		<h4>Location configuration:</h4>
		<div><div class="col-xs-2">Latitude:</div><div class="col-xs-10"><input name="lat" type="text" value="{{config["lat"]}}"></div></div>
		<div><div class="col-xs-2">Longtitude:</div><div class="col-xs-10"><input name="long" type="text" value="{{config["long"]}}"></div></div>
		<input value="Save Changes" type="submit">
	</form>
</div>
</div>