<div class="col-xs-0 col-md-3"></div>
<div class="col-xs-12 col-md-6">
<div id="card">
	<h2 id="title">Thermostat</h2>
	<h3>Target Temperature:</h3>
	<form is="iron-form" action="/setTargetTemp" method="POST">
		<paper-slider name="targetSlider" pin min="10" max="30" value="{{temp["target"]}}" editable></paper-slider>
		<paper-button raised id="submit" onclick="Polymer.dom(event).localTarget.parentElement.submit(); setToast.open(); location.reload()">Set Temp!</paper-button>
	</form>
	<h3 id="title">Current room temp: {{temp["roomTemp"]}}</h3>
	<h4>Heating status: {{temp["heating"]}}</h4>
	<paper-toast id="setToast" text="Target temp set!"></paper-toast>
</div>
</div>
<div class="col-xs-0 col-md-3"></div>
