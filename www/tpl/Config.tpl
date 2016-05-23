<div class="col-xs-12">
<div class="col-xs-0 col-md-3"></div>
<div id="card" class="col-xs-12 col-md-6">
	<paper-icon-button icon="help" class="help" onclick="help.open()"></paper-icon-button>
	<h2 class="title">Configuration</h2>
	<form is="iron-form" action="/saveConfig" method="POST">
		<h4>Location configuration:</h4>
		<div><paper-input name="lat" label="Latitude" value="{{config["lat"]}}" required></paper-input></div>
		<div><paper-input name="long" label="Longtitude" value="{{config["long"]}}" required></paper-input></div>
		<paper-button class="col-xs-12" raised id="submit" onclick="Polymer.dom(event).localTarget.parentElement.submit(); saveToast.open()">Save config!</paper-button>
		<paper-toast id="saveToast" text="Settings have been saved!"></paper-toast>
	</form>
	<paper-toast duration="0" id="help" text="This page is used to control the location of the weather data. FInd your current lattitude and longtitude and enter them in here, and click save. This will update the location, and display the correct weather data.">
		<paper-icon-button icon="close" class="closeBtn" onclick="help.toggle()">
	</paper-toast>
</div>
<div class="col-xs-0 col-md-3"></div>
</div>
