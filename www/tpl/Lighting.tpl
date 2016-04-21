<div class="col-xs-0 col-md-3">
</div>
<div id="card" class="col-xs-12 col-md-6">
	<h2 id="title">Lighting</h2>
	<style is="custom-style">
	  paper-slider.red {
	    --paper-slider-knob-color: var(--paper-red-500);
	    --paper-slider-active-color: var(--paper-red-500);
	  }
	  paper-slider.green {
	    --paper-slider-knob-color: var(--paper-green-500);
	    --paper-slider-active-color: var(--paper-green-500);
	  }
	  paper-slider.blue {
	    --paper-slider-knob-color: var(--paper-light-blue-500);
	    --paper-slider-active-color: var(--paper-light-blue-500);
	  }
       	  paper-slider {
            width: 100%;
          }
	  paper-slider.small{
	    width:10%;
	    margin:auto;
            --paper-slider-height:10px;
	  }
	</style>
	<form is="iron-form" action="/setLEDs" method="POST">
		<h4>RGB settings:</h4>
		R<paper-slider class="red" name="redSlider" pin min="0" max="255" value="{{rgb["red"]}}" editable></paper-slider>
		G<paper-slider class="green" name="greenSlider" pin min="0" max="255" value="{{rgb["green"]}}" editable></paper-slider>
		B<paper-slider class="blue" name="blueSlider" pin min="0" max="255" value="{{rgb["blue"]}}" editable></paper-slider>
		<h4>Off/On:</h4>
		%#<paper-slider class="small" name="onOff" pin min="0" max="1" value="{{rgb["status"]}}"></paper-slider>
		<paper-toggle-button name="onOff" checked>On/off</paper-toggle-button>
		<paper-button raised id="submit" onclick="Polymer.dom(event).localTarget.parentElement.submit(); setToast.open();">Set RGB!</paper-button>
	</form>
	<paper-toast id="setToast" text="Set lighting settings!"></paper-toast>
</div>
<div class="col-xs-0 col-md-3">
</div>
