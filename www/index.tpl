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
  <link rel="import" href="/static/bower_components/iron-icons/image-icons.html">
  <link rel="import" href="/static/bower_components/iron-icon/iron-icon.html">
  <link rel="import" href="/static/bower_components/paper-toolbar/paper-toolbar.html">
  <link rel="import" href="/static/bower_components/font-roboto/roboto.html">
  <link rel="import" href="/static/bower_components/paper-button/paper-button.html">
  <link rel="import" href="/static/bower_components/paper-drawer-panel/paper-drawer-panel.html">
  <link rel="import" href="/static/bower_components/paper-header-panel/paper-header-panel.html">
  <link rel="import" href="/static/bower_components/paper-item/paper-item.html">
  <link rel="import" href="/static/bower_components/iron-form/iron-form.html">
  <link rel="import" href="/static/bower_components/paper-input/paper-input.html">
  <link rel="import" href="/static/bower_components/paper-toast/paper-toast.html">
  <link rel="import" href="/static/bower_components/paper-slider/paper-slider.html">
  <link rel="import" href="/static/bower_components/paper-toggle-button/paper-toggle-button.html">
  <link rel="stylesheet" href="/static/styles.css">
  <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.2/jquery.min.js"></script>

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
		%if area=="Home" or area=="":
		%	include("www/tpl/Home.tpl")
		%elif area=="Lighting":
		%	include("www/tpl/Lighting.tpl")
		%elif area=="Thermostat":
		%	include("www/tpl/Thermostat.tpl")
		%elif area=="Camera":
		%	include("www/tpl/Camera.tpl")
		%elif area=="LCDScreen":
		%	include("www/tpl/LCDScreen.tpl")
		%elif area=="Config":
		%	include("www/tpl/Config.tpl")
		%elif area=="About":
		%	include("www/tpl/About.tpl")
		%end
      </div>
    </paper-header-panel>
    
    <paper-header-panel drawer id="drawer">
      <paper-toolbar class="drawer">
        <div flex>Navigation</div>
      </paper-toolbar>
      <a class="blank" href="Home"><paper-item><iron-icon class="padRight" icon="home"></iron-icon>Home</paper-item></a>
      <hr width="100%">
      <a class="blank" href="Lighting"><paper-item><iron-icon class="padRight" icon="lightbulb-outline"></iron-icon>Lighting</paper-item></a>
      <a class="blank" href="Thermostat"><paper-item><iron-icon class="padRight" icon="places:ac-unit"></iron-icon>Thermostat</paper-item></a>
      <a class="blank" href="Camera"><paper-item><iron-icon class="padRight" icon="image:camera-alt"></iron-icon>Camera</paper-item></a>
      <a class="blank" href="LCDScreen"><paper-item><iron-icon class="padRight" icon="check-box-outline-blank"></iron-icon>LCD Screen</paper-item></a>
      <hr width="100%">
	  <a class="blank" href="Config"><paper-item><iron-icon class="padRight" icon="build"></iron-icon>Configuration</paper-item</a>
      <a class="blank" href="About"><paper-item><iron-icon class="padRight" icon="help-outline"></iron-icon>About</paper-item</a>
    </paper-header-panel>
  
  </paper-drawer-panel>
  <script src="/static/tpl/js/lighting.js"></script>
  <!--<script src="/static/tpl/js/camera.js"></script>--!>
</body>
</html>
