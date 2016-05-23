<div class="col-xs-0 col-md-3"></div>
<div class="col-xs-12 col-md-6">
<div id="card">
	<style is="custom-style">
		paper-slider {
			width: 100%;
		}
	</style>
	<paper-icon-button icon="help" class="help" onclick="help.open()"></paper-icon-button>
	<h2 id="title">Thermostat</h2>
	<h4>Current room temp: {{temp["roomTemp"]}}</h4>
	<h4>Heating status: {{temp["heating"]}}</h4>
	<h4>Target Temperature:</h4>
	<form is="iron-form" action="/setTargetTemp" method="POST">
		<paper-slider name="targetSlider" pin min="10" max="30" value="{{temp["target"]}}" editable></paper-slider>
		<paper-button class="col-xs-12" raised id="submit" onclick="Polymer.dom(event).localTarget.parentElement.submit(); setToast.open();">Set Temp!</paper-button>
	</form>
	<paper-toast id="setToast" text="Target temp set!"></paper-toast>
	<paper-toast duration="0" id="help" text="Set the target temp using the slider then click the set button. If the current room temperature is lower, the heating will be turned on.">
		<paper-icon-button icon="close" class="closeBtn" onclick="help.toggle()">
	</paper-toast>
</div>
</div>
<div class="col-xs-0 col-md-3"></div>
