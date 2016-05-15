<div class="col-md-3 col-xs-0">
</div>
<div class="col-xs-12 col-md-6">
<div id="card" class="camContain">
	<h2 id="title">Camera:</h2>
	%i=0	
	%import time
	%while True:
	<img class="camera" src="/camFeed?i={{i}}">
	%time.sleep(3.5)
	%i=i+1
	%end
</div>
</div>
<div class="col-md-3 col-xs-0">
</div>
