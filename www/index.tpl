<!doctype html>

<html>
<head>
  <title>RPiHomeAutomation</title>

  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
  <meta name="mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-capable" content="yes">

  <script src="/static/bower_components/webcomponentsjs/webcomponents-lite.min.js"></script>

  <link rel="import" href="/static/bower_components/iron-icons/iron-icons.html">
  <link rel="import" href="/static/bower_components/iron-icons/hardware-icons.html">
  <link rel="import" href="/static/bower_components/iron-icons/places-icons.html">
  <link rel="import" href="/static/bower_components/iron-icons/av-icons.html">
  <link rel="import" href="/static/bower_components/iron-icon/iron-icon.html">
  <link rel="import" href="/static/bower_components/paper-toolbar/paper-toolbar.html">
  <link rel="import" href="/static/bower_components/font-roboto/roboto.html">
  <link rel="import" href="/static/bower_components/paper-button/paper-button.html">
  <link rel="import" href="/static/bower_components/paper-drawer-panel/paper-drawer-panel.html">
  <link rel="import" href="/static/bower_components/paper-header-panel/paper-header-panel.html">
  <link rel="import" href="/static/bower_components/paper-item/paper-item.html">
  <link rel="stylesheet" href="/static/styles.css">
  <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>

<body class="fullbleed">
  <paper-drawer-panel id="paperDrawerPanel">
    <paper-header-panel main>
      <paper-toolbar class="main">
        <paper-button id="menuBtn" paper-drawer-toggle><iron-icon icon="menu"></iron-icon></paper-button>
        %if area:
		<div flex>{{area}} - Control Panel</div>
		%else:
		<div flex>Home - Control Panel</div>
		%end
      </paper-toolbar>
	  <div>
        <div class="col-xs-12 col-md-4"><div id="card">{{area}}</div></div>
      </div>
    </paper-header-panel>
    
    <paper-header-panel drawer>
      <paper-toolbar class="drawer">
        <div flex>Navigation</div>
      </paper-toolbar>
      <a class="blank" href="Home"><paper-item><iron-icon class="padRight" icon="home"></iron-icon>Home</paper-item></a>
      <a class="blank" href="Sensors"><paper-item><iron-icon class="padRight" icon="hardware:developer-board"></iron-icon>Sensors</paper-item></a>
      <hr width="100%">
      <a class="blank" href="Lighting"><paper-item><iron-icon class="padRight" icon="lightbulb-outline"></iron-icon>Lighting</paper-item></a>
      <a class="blank" href="Temperature"><paper-item><iron-icon class="padRight" icon="places:ac-unit"></iron-icon>Temperature</paper-item></a>
      <a class="blank" href="Music"><paper-item><iron-icon class="padRight" icon="av:library-music"></iron-icon>Music</paper-item></a>
      <hr width="100%">
      <a class="blank" href="About"><paper-item><iron-icon class="padRight" icon="help-outline"></iron-icon>About</paper-item</a>
    </paper-header-panel>
  
  </paper-drawer-panel>
</body>
</html>
