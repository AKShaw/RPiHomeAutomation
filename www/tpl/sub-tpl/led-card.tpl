<div id="card" class="ledScreen">
<h2 class="title">LED Display:</h2>
%if led["firstLine"] != "":
<h3 id="led">{{led["firstLine"]}}</h3>
%else:
<h3 id="led">&nbsp;</h3>
%end
%if led["secondLine"] != "":
<h3 id="led">{{led["secondLine"]}}</h3>
%else:
<h3 id="led">&nbsp;</h3>
%end
</div>