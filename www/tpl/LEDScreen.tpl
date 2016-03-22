<div class="col-xs-12">
<div class="col-xs-0 col-md-3"></div>
<div id="card" class="col-xs-12 col-md-6"style="margin-left:auto; margin-right:auto;">
	<h2 class="title">LED Screen</h2>
	<form is="iron-form" action="/setLEDScreen" method="POST">
		<h4>Display settings:</h4>
		<div><paper-input name="line1" label="First line" value="{{led["firstLine"]}}" char-counter maxLength="16" required></paper-input></div>
		<div><paper-input name="line2" label="Second line" value="{{led["secondLine"]}}" char-counter maxLength="16" required></paper-input></div>
		<paper-button class="col-xs-12" raised id="submit" onclick="Polymer.dom(event).localTarget.parentElement.submit(); saveToast.open()">Set LED screen!</paper-button>
		<paper-toast id="saveToast" text="Screen set!"></paper-toast>
	</form>
</div>
<div class="col-xs-0 col-md-3"></div>
</div>
