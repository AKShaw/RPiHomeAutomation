<div class="col-xs-0 col-md-3">
</div>
<div id="card" class="col-xs-12 col-md-6">
	<h2 id="title">Lighting</h2>
	<form id="form" is="iron-form" action="/setLEDs" method="POST">
		<h4>RGB settings:</h4>
		R<paper-slider id="red" name="redSlider" pin min="0" max="255" value="{{rgb["red"]}}" editable></paper-slider>
		G<paper-slider id="green" name="greenSlider" pin min="0" max="255" value="{{rgb["green"]}}" editable></paper-slider>
		B<paper-slider id="blue" name="blueSlider" pin min="0" max="255" value="{{rgb["blue"]}}" editable></paper-slider>
		<h4>LED Matrix:</h4>
		%if rgb["status"]==1:
		<paper-toggle-button id="toggleBtn" checked>Off or On</paper-toggle-button>
		%elif rgb["status"]==0:
		<paper-toggle-button id="toggleBtn">Off or On</paper-toggle-button>
		%end
	</form>
</div>
<div class="col-xs-0 col-md-3">
</div>
