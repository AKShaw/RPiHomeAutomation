<div id="card bodyCard" class="lcdScreen">
<h2 class="title">LCD Display:</h2>
%if lcd["firstLine"] != "":
<h3 id="lcd">{{lcd["firstLine"]}}</h3>
%else:
<h3 id="lcd">&nbsp;</h3>
%end
%if lcd["secondLine"] != "":
<h3 id="lcd">{{lcd["secondLine"]}}</h3>
%else:
<h3 id="lcd">&nbsp;</h3>
%end
</div>
