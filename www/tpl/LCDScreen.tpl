<div class="col-xs-12">
<div class="col-xs-0 col-md-3"></div>
<div id="card" class="col-xs-12 col-md-6">
	<paper-icon-button icon="help" class="help" onclick="help.open()"></paper-icon-button>
	<h2 class="title">LCD Screen</h2>
	<form is="iron-form" action="/setLCDScreen" method="POST">
		<h4>Display settings:</h4>
		<div><paper-input name="line1" label="First line" value="{{lcd["firstLine"]}}" char-counter maxLength="16"></paper-input></div>
		<div><paper-input name="line2" label="Second line" value="{{lcd["secondLine"]}}" char-counter maxLength="16"></paper-input></div>
		<paper-button class="col-xs-12" raised id="submit" onclick="Polymer.dom(event).localTarget.parentElement.submit(); saveToast.open()">Set LCD screen!</paper-button>
		<paper-toast id="saveToast" text="Screen set!"></paper-toast>
	</form>
	<paper-toast duration="0" id="help" text="Enter a string of up too 16 charatcers in either or both of the text boxes. Click the set button and this will display the entered text on the LCD screen.c">
		<paper-icon-button icon="close" class="closeBtn" onclick="help.toggle()">
	</paper-toast>
</div>
<div class="col-xs-0 col-md-3"></div>
</div>
