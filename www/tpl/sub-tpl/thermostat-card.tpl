%if (temp["heating"]=="ON"):
<div id="bodyCard" style="background: linear-gradient(#FF5722, #F44336); color:#FFF;">
%elif (temp["heating"]=="OFF"):
<div id="bodyCard" style="background: linear-gradient(#2196F3, #00695C); color:#FFF;">
%end
<h2 id="title">Thermostat</h2>
<div class="col-xs-6">
	<h4>Target temperature: {{temp["target"]}}&deg;C</h4>
	<h4>Heating Status: {{temp["heating"]}}</h4>
</div>
<div class="col-xs-6">
	<h4>Current room temperature: {{temp["roomTemp"]}}&deg;C</h4>
	<h4>Current room humidity: {{temp["roomHumidity"]}}</h4>
	<h4>Current room pressure: {{temp["roomPressure"]}}</h4>
</div>
</div>
