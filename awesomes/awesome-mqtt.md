<h1>
 Awesome MQTT
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
 <a href="https://travis-ci.org/hobbyquaker/awesome-mqtt">
  <img alt="Build Status" src="https://travis-ci.org/hobbyquaker/awesome-mqtt.svg?branch=master"/>
 </a>
</h1>
<blockquote>
 <p>
  A curated list of MQTT related stuff.
 </p>
</blockquote>
<p>
 MQTT is a lightweight client-server publish/subscribe messaging protocol, optimized for high-latency or unreliable networks. This protocol is a good choice for Internet of Things applications, Telemetry, Sensor Networks, Smart Metering, Home Automation, Messaging and Notfication Services.
</p>
<h2>
 Table of Contents
</h2>
<ul>
 <li>
  <a href="#community-resources">
   Community Resources
  </a>
 </li>
 <li>
  <a href="#broker">
   Broker
  </a>
 </li>
 <li>
  <a href="#tools">
   Tools
  </a>
 </li>
 <li>
  <a href="#clients">
   Clients
  </a>
 </li>
 <li>
  <a href="#scripting">
   Scripting
  </a>
 </li>
 <li>
  <a href="#interfaces">
   Interfaces
  </a>
  <ul>
   <li>
    <a href="#makers">
     Makers
    </a>
   </li>
   <li>
    <a href="#industry">
     Industry
    </a>
   </li>
   <li>
    <a href="#telephony-pbx">
     Telephony, PBX
    </a>
   </li>
   <li>
    <a href="#operating-system">
     Operating System
    </a>
   </li>
   <li>
    <a href="#monitoring">
     Monitoring
    </a>
   </li>
   <li>
    <a href="#location-tracking">
     Location Tracking
    </a>
   </li>
   <li>
    <a href="#logging">
     Logging
    </a>
   </li>
   <li>
    <a href="#smart-home-building-automation">
     Smart Home, Building Automation
    </a>
   </li>
   <li>
    <a href="#smart-home-software">
     Smart Home Software
    </a>
   </li>
   <li>
    <a href="#misc-software">
     Misc Software
    </a>
   </li>
   <li>
    <a href="#lighting">
     Lighting
    </a>
   </li>
   <li>
    <a href="#home-entertainment">
     Home Entertainment
    </a>
   </li>
   <li>
    <a href="#gadgets">
     Gadgets
    </a>
   </li>
   <li>
    <a href="#smart-metering">
     Smart Metering
    </a>
   </li>
   <li>
    <a href="#messaging">
     Messaging
    </a>
   </li>
   <li>
    <a href="#visualization">
     Visualization
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#architecture">
   Architecture
  </a>
 </li>
</ul>
<h3>
 Community Resources
</h3>
<ul>
 <li>
  <a href="http://mqtt.org/">
   mqtt.org
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/mqtt/mqtt.github.io/wiki">
   MQTT community wiki
  </a>
  .
 </li>
 <li>
  <a href="https://groups.google.com/forum/#!forum/mqtt">
   Google Groups: MQTT
  </a>
  .
 </li>
 <li>
  <a href="irc://irc.freenode.net/mqtt">
   IRC channel #mqtt on the freenode network
  </a>
  .
 </li>
 <li>
  <a href="http://moxd.io/2015/10/public-mqtt-brokers/">
   A list of public brokers
  </a>
  .
 </li>
 <li>
  <a href="http://forkbomb-blog.de/category/mqtt">
   Forkbomb Blog (Dominik Obermaier)
  </a>
 </li>
</ul>
<h3>
 Broker
</h3>
<ul>
 <li>
  <a href="http://emqtt.io/">
   eMQTT
  </a>
  - The Massively Scalable MQTT Broker written in Erlang/OTP.
 </li>
 <li>
  <a href="https://github.com/beerfactory/hbmqtt">
   hbmqtt
  </a>
  <span>
   &#9733 56, pushed 22 days ago
  </span>
  - Python MQTT broker using asyncio.
 </li>
 <li>
  <a href="http://www.hivemq.com/">
   HiveMQ
  </a>
  - Java based commercial MQTT Broker.
 </li>
 <li>
  <a href="https://github.com/andsel/moquette">
   Moquette
  </a>
  <span>
   &#9733 311, pushed 8 days ago
  </span>
  - Java MQTT lightweight broker.
 </li>
 <li>
  <a href="http://www.mosca.io/">
   Mosca
  </a>
  - Mosca is a node.js mqtt broker, which can be used Standalone or Embedded in another Node.js application.
 </li>
 <li>
  <a href="http://mosquitto.org/">
   Mosquitto
  </a>
  - "The" Open Source MQTT Broker.
 </li>
 <li>
  <a href="http://zhen.org/categories/surgemq/">
   SurgeMQ
  </a>
  - High Performance MQTT Server and Client Libraries in Go.
 </li>
 <li>
  <a href="https://vernemq.com/">
   VerneMQ
  </a>
  - an Apache2 licensed distributed MQTT broker, developed in Erlang.
 </li>
 <li>
  <a href="https://www.rabbitmq.com/mqtt.html">
   RabbitMQ MQTT Adapter
  </a>
  - MQTT Adapter for RabbitMQ
 </li>
</ul>
<h3>
 Tools
</h3>
<ul>
 <li>
  <a href="https://github.com/hobbyquaker/mqtt-admin/">
   mqtt-admin
  </a>
  - Web based MQTT frontend.
  <a href="https://hobbyquaker.github.io/mqtt-admin/">
   Direct Link
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/chirino/mqtt-benchmark">
   mqtt-benchmark
  </a>
  <span>
   &#9733 90, pushed 1509 days ago
  </span>
  - A benchmarking tool for MQTT Servers.
 </li>
 <li>
  <a href="https://github.com/F-Secure/mqtt_fuzz">
   mqtt-fuzz
  </a>
  <span>
   &#9733 23, pushed 361 days ago
  </span>
  - A simple fuzzer for the MQTT protocol.
 </li>
 <li>
  <a href="http://mqttfx.jfx4ee.org/">
   MQTT.fx
  </a>
  - MQTT.fx is a MQTT Client written in Java based on Eclipse Paho. Supports scripting.
 </li>
 <li>
  <a href="https://github.com/ckrey/MQTTInspector">
   MQTTInspector
  </a>
  <span>
   &#9733 40, pushed 70 days ago
  </span>
  - A general MQTT testing app for iOS (iPhone and iPad).
 </li>
 <li>
  <a href="https://chrome.google.com/webstore/detail/mqttlens/hemojaaeigabkbcookmlgmdigohjobjm">
   MQTTLens
  </a>
  - A Google Chrome application, which connects to a MQTT broker and is able to subscribe and publish to MQTT topics.
 </li>
 <li>
  <a href="https://github.com/remakeelectric/mqtt-malaria">
   mqtt-malaria
  </a>
  <span>
   &#9733 93, pushed 8 days ago
  </span>
  - scalability and load testing utilities for MQTT environments.
 </li>
 <li>
  <a href="http://kamilfb.github.io/mqtt-spy/">
   mqtt-spy
  </a>
  - Java based MQTT frontend. Supports scripting.
 </li>
 <li>
  <a href="https://github.com/dsell/mqtt-utils">
   mqtt-utils
  </a>
  <span>
   &#9733 2, pushed 925 days ago
  </span>
  - a collection of MQTT utilities.
 </li>
</ul>
<h3>
 Clients
</h3>
<ul>
 <li>
  <a href="https://github.com/emqtt/CocoaMQTT">
   CocoaMQTT
  </a>
  <span>
   &#9733 217, pushed 6 days ago
  </span>
  - MQTT for iOS and OS X written with Swift.
 </li>
 <li>
  <a href="https://github.com/emqtt/emqttc">
   emqttc
  </a>
  <span>
   &#9733 36, pushed 8 days ago
  </span>
  - Asynchronous Erlang MQTT Client.
 </li>
 <li>
  <a href="https://github.com/flightonary/Moscapsule">
   Moscapsule
  </a>
  <span>
   &#9733 96, pushed 24 days ago
  </span>
  - MQTT Client for iOS written in Swift
 </li>
 <li>
  <a href="https://github.com/beerfactory/hbmqtt">
   hbmqtt
  </a>
  - Python MQTT client using asyncio.
 </li>
 <li>
  <a href="https://github.com/centamiv/mqtt-client">
   mqtt-client
  </a>
  <span>
   &#9733 7, pushed 348 days ago
  </span>
  - A Polymer Web Component that implements a MQTT client (uses Paho mqttws31.js).
 </li>
 <li>
  <a href="https://github.com/ckrey/MQTT-Client-Framework">
   MQTT-Client-Framework
  </a>
  <span>
   &#9733 265, pushed 6 days ago
  </span>
  - iOS native ObjectiveC MQTT Framework.
 </li>
 <li>
  <a href="https://github.com/alfert/mqttex">
   mqttex
  </a>
  <span>
   &#9733 34, pushed 355 days ago
  </span>
  - MQTT implementation in Elixir.
 </li>
 <li>
  <a href="https://github.com/mobile-web-messaging/MQTTKit">
   MQTTKit
  </a>
  <span>
   &#9733 250, pushed 235 days ago
  </span>
  - MQTT Objective-C client for iOS.
 </li>
 <li>
  <a href="http://geekscape.github.io/mqtt_lua/">
   mqtt_lua
  </a>
  - MQTT Client library for the Lua language.
 </li>
 <li>
  <a href="https://github.com/mqttjs">
   MQTT.js
  </a>
  - MQTT client for Node.js.
 </li>
 <li>
  <a href="http://www.eclipse.org/paho/">
   Paho
  </a>
  - open-source client implementations (C/C++, Java, Python, Javascript, Go, C#).
 </li>
 <li>
  <a href="https://github.com/knolleary/pubsubclient">
   pubsubclient
  </a>
  <span>
   &#9733 690, pushed 5 days ago
  </span>
  - A client library for the Arduino Ethernet Shield that provides support for MQTT.
 </li>
 <li>
  <a href="https://github.com/njh/ruby-mqtt">
   ruby-mqtt
  </a>
  <span>
   &#9733 197, pushed 1 days ago
  </span>
  - Pure Ruby gem that implements the MQTT protocol.
 </li>
</ul>
<h3>
 Scripting
</h3>
<ul>
 <li>
  <a href="https://github.com/owagner/logic4mqtt">
   logic4mqtt
  </a>
  <span>
   &#9733 4, pushed 64 days ago
  </span>
  - Java based Logic and scripting engine for use with MQTT. Uses Java's general scripting interface, so scripts can be written in a multitude of languages like Javascript, Groovy etc.
 </li>
 <li>
  <a href="https://github.com/hobbyquaker/mqtt-scripts/">
   mqtt-scripts
  </a>
  - Node.js based script runner. .
 </li>
 <li>
  <a href="http://nodered.org/">
   Node-RED
  </a>
  - A visual tool for wiring the Internet of Things.
 </li>
</ul>
<h3>
 Interfaces
</h3>
<h4>
 Makers
</h4>
<ul>
 <li>
  <a href="https://github.com/knolleary/pubsubclient">
   pubsubclient
  </a>
  - A client library for the Arduino Ethernet Shield that provides support for MQTT.
 </li>
 <li>
  <a href="https://github.com/computourist/RFM69-MQTT-client">
   RFM69-MQTT-client
  </a>
  <span>
   &#9733 52, pushed 23 days ago
  </span>
  - Arduino RFM69 based sensors and MQTT gateway.
 </li>
 <li>
  <a href="https://github.com/hobbyquaker/rpi2mqtt">
   rpi2mqtt
  </a>
  <span>
   &#9733 2, pushed 233 days ago
  </span>
  - Connect a RaspberryPis GPIOs and 1-Wire Temperature Sensors to MQTT.
 </li>
 <li>
  <a href="https://github.com/xoseperez/xbee2mqtt">
   xbee2mqtt
  </a>
  <span>
   &#9733 13, pushed 88 days ago
  </span>
  - XBee to MQTT gateway.
 </li>
</ul>
<h4>
 Industry
</h4>
<ul>
 <li>
  <a href="https://github.com/owagner/modbus2mqtt">
   modbus2mqtt
  </a>
  <span>
   &#9733 10, pushed 78 days ago
  </span>
  - Modbus master which publishes register values via MQTT.
 </li>
 <li>
  <a href="https://github.com/nzfarmer1/mqtt2opcua">
   mqtt2opcua
  </a>
  <span>
   &#9733 9, pushed 275 days ago
  </span>
  - Bi Directional MQTT to OPCUA Bridge.
 </li>
</ul>
<h4>
 Telephony, PBX
</h4>
<ul>
 <li>
  <a href="https://github.com/zeha/agi-mqtt">
   agi-mqtt
  </a>
  <span>
   &#9733 13, pushed 736 days ago
  </span>
  - Interface between Asterisk and MQTT.
 </li>
 <li>
  <a href="https://github.com/akentner/fritz2mqtt">
   fritz2mqtt
  </a>
  <span>
   &#9733 1, pushed 235 days ago
  </span>
  - Connect FRITZ!Box to MQTT.
 </li>
</ul>
<h4>
 Operating System
</h4>
<ul>
 <li>
  <a href="https://github.com/jpmens/mqtt-watchdir">
   mqttwatchdir
  </a>
  <span>
   &#9733 13, pushed 364 days ago
  </span>
  - Recursively watch a directory for modifications and publish file content to an MQTT broker.
 </li>
 <li>
  <a href="https://github.com/jpmens/mqtt-launcher">
   mqttlauncher
  </a>
  <span>
   &#9733 11, pushed 755 days ago
  </span>
  - Execute shell commands triggered by published MQTT messages.
 </li>
 <li>
  <a href="https://github.com/oskarhagberg/mqtt-os-status">
   mqtt-os-status
  </a>
  <span>
   &#9733 4, pushed 756 days ago
  </span>
  - Operating-system related data, published to an MQTT broker at fixed intervals.
 </li>
 <li>
  <a href="https://github.com/eschava/psmqtt">
   psmqtt
  </a>
  <span>
   &#9733 6, pushed 16 days ago
  </span>
  - Utility reporting system health and status via MQTT
 </li>
</ul>
<h4>
 Monitoring
</h4>
<ul>
 <li>
  <a href="https://github.com/jpmens/check-mqtt">
   check-mqtt
  </a>
  <span>
   &#9733 6, pushed 115 days ago
  </span>
  - A Nagios/Icinga plugin for checking connectivity to an MQTT broker.
 </li>
 <li>
  <a href="https://github.com/jpmens/notify-by-mqtt">
   notify-by-mqtt
  </a>
  <span>
   &#9733 6, pushed 693 days ago
  </span>
  - a Nagios/Icinga notification module which wraps data into JSON and fires it off to an MQTT broker.
 </li>
</ul>
<h4>
 Location tracking
</h4>
<ul>
 <li>
  <a href="http://owntracks.org/">
   Owntracks
  </a>
  - Location tracking and geofencing for MQTT.
 </li>
</ul>
<h4>
 Logging
</h4>
<ul>
 <li>
  <a href="https://github.com/jpmens/mqtt2graphite">
   mqtt2graphite
  </a>
  <span>
   &#9733 39, pushed 135 days ago
  </span>
  - Subscribe to MQTT topics and push to Graphite's Carbon server.
 </li>
 <li>
  <a href="https://github.com/hobbyquaker/influx4mqtt">
   influx4mqtt
  </a>
  <span>
   &#9733 3, pushed 303 days ago
  </span>
  - Subscribe to MQTT topics and insert into InfluxDB.
 </li>
</ul>
<h4>
 Smart Home, Building Automation
</h4>
<ul>
 <li>
  <a href="https://github.com/hobbyquaker/cul2mqtt">
   cul2mqtt
  </a>
  <span>
   &#9733 0, pushed 234 days ago
  </span>
  - Interface between
  <a href="http://shop.busware.de/product_info.php/cPath/1/products_id/29">
   Busware CUL
  </a>
  (868MHz RF-Devices like ELV FS20, HMS, EM, ...) and MQTT.
 </li>
 <li>
  <a href="https://github.com/owagner/eno2mqtt">
   eno2mqtt
  </a>
  <span>
   &#9733 3, pushed 10 days ago
  </span>
  - Interface between an Enocean USB300 (TCM310) adapter and MQTT.
 </li>
 <li>
  <a href="https://github.com/owagner/hm2mqtt">
   hm2mqtt
  </a>
  <span>
   &#9733 10, pushed 65 days ago
  </span>
  - Interface between EQ-3's Homematic line of smarthome devices and MQTT.
 </li>
 <li>
  <a href="https://github.com/owagner/knx2mqtt">
   knx2mqtt
  </a>
  <span>
   &#9733 5, pushed 229 days ago
  </span>
  - Interface between the KNX home automation standard and MQTT. .
 </li>
 <li>
  <a href="https://github.com/cgHome/mqtt-dss-bridge">
   mqtt-dss-bridge
  </a>
  <span>
   &#9733 2, pushed 222 days ago
  </span>
  - MQTT digitalSTROM-Server Bridge.
 </li>
</ul>
<h5>
 Smart Home Software
</h5>
<ul>
 <li>
  <a href="http://fhem.de/fhem.html">
   fhem
  </a>
  has a
  <a href="http://fhem.de/commandref.html#MQTT">
   MQTT module
  </a>
  since V5.6 .
 </li>
 <li>
  <a href="https://github.com/hobbyquaker/homekit2mqtt">
   homekit2mqtt
  </a>
  <span>
   &#9733 3, pushed 119 days ago
  </span>
  - Interface between
  <a href="https://github.com/KhaosT/HAP-NodeJS">
   HAP-NodeJS
  </a>
  and MQTT.
 </li>
 <li>
  <a href="https://github.com/ioBroker">
   ioBroker
  </a>
  has a
  <a href="https://github.com/ioBroker/ioBroker.mqtt">
   MQTT adapter
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/openhab">
   openhab
  </a>
  has a
  <a href="https://github.com/openhab/openhab/wiki/MQTT-Binding">
   MQTT binding
  </a>
  .
 </li>
</ul>
<h4>
 Misc Software
</h4>
<ul>
 <li>
  Tasker (Automation for Android)
  <a href="https://play.google.com/store/apps/details?id=net.nosybore.mqttpublishplugin">
   MQTT Publisher Plugin
  </a>
 </li>
</ul>
<h4>
 Lighting
</h4>
<ul>
 <li>
  <a href="https://github.com/owagner/chromoflex2mqtt">
   chromoflex2mqtt
  </a>
  <span>
   &#9733 1, pushed 150 days ago
  </span>
  - Control Chromoflex USP3 RGB LED modules via MQTT
 </li>
 <li>
  <a href="https://github.com/owagner/hue2mqtt">
   hue2mqtt
  </a>
  <span>
   &#9733 14, pushed 62 days ago
  </span>
  - Interface between the Philips Hue bridge and MQTT.
 </li>
 <li>
  <a href="https://github.com/hobbyquaker/mqtt-dmx-sequencer">
   mqtt-dmx-sequencer
  </a>
  <span>
   &#9733 1, pushed 234 days ago
  </span>
  - Control DMX devices via Art-Net by MQTT.
 </li>
</ul>
<h4>
 Home Entertainment
</h4>
<ul>
 <li>
  <a href="https://github.com/hobbyquaker/airtunes2mqtt">
   airtunes2mqtt
  </a>
  <span>
   &#9733 2, pushed 234 days ago
  </span>
  - MQTT controlled Multi-Room Audio with Airplay/Airtunes Devices.
 </li>
 <li>
  <a href="https://github.com/owagner/kodi2mqtt">
   kodi2mqtt
  </a>
  <span>
   &#9733 17, pushed 2 days ago
  </span>
  - Interface between a Kodi mediacenter instance and MQTT.
 </li>
 <li>
  <a href="https://github.com/hobbyquaker/lirc2mqtt">
   lirc2mqtt
  </a>
  <span>
   &#9733 2, pushed 177 days ago
  </span>
  - Send and receive infrared via
  <a href="www.lirc.org">
   LIRC
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/owagner/onkyo2mqtt">
   onkyo2mqtt
  </a>
  <span>
   &#9733 3, pushed 331 days ago
  </span>
  - Interface between Onkyo AVR's EISCP network remote protocol and MQTT. Uses the onkyo-eiscp library.
 </li>
 <li>
  <a href="https://github.com/gordonjcp/xbmc-mqtt">
   xbmc2mqtt
  </a>
  <span>
   &#9733 4, pushed 413 days ago
  </span>
  - A simple plugin for XBMC to listen for a particular topic on an MQTT broker, and display a popup message
 </li>
 <li>
  <a href="https://github.com/akentner/yamaha-avr2mqtt">
   yamaha-avr2mqtt
  </a>
  <span>
   &#9733 1, pushed 126 days ago
  </span>
  .
 </li>
</ul>
<h4>
 Gadgets
</h4>
<ul>
 <li>
  <a href="https://github.com/hobbyquaker/flowerpower2mqtt">
   flowerpower2mqtt
  </a>
  <span>
   &#9733 0, pushed 191 days ago
  </span>
  - Publish measurements from
  <a href="http://www.parrot.com/usa/products/flower-power/">
   Parrot Flower Power
  </a>
  plant sensors to MQTT.
 </li>
</ul>
<h4>
 Smart Metering
</h4>
<ul>
 <li>
  <a href="https://github.com/hobbyquaker/bcontrol2mqtt">
   bcontrol2mqtt
  </a>
  <span>
   &#9733 0, pushed 234 days ago
  </span>
  - Publish measurements from
  <a href="http://www.tq-group.com/produkte/produktdetail/prod/energy-manager/extb/Main/">
   TQ Energy Manager
  </a>
  to MQTT.
 </li>
</ul>
<h4>
 Messaging
</h4>
<ul>
 <li>
  <a href="https://github.com/dobermai/mqtt-irc-bot">
   mqtt-irc-bot
  </a>
  <span>
   &#9733 10, pushed 183 days ago
  </span>
  - A MQTT to IRC / IRC to MQTT bridge or bot.
 </li>
 <li>
  <a href="https://github.com/jpmens/mqttwarn">
   mqttwarn
  </a>
  <span>
   &#9733 382, pushed 13 days ago
  </span>
  - Subscribe to MQTT topics (with wildcards) and notifiy pluggable services.
 </li>
 <li>
  <a href="https://github.com/knolleary/twitter-to-mqtt">
   twitter-to-mqtt
  </a>
  <span>
   &#9733 9, pushed 1231 days ago
  </span>
  - A python daemon that uses the Twitter Streaming API to access tweets and republishes them to an MQTT topic.
 </li>
</ul>
<h4>
 Visualization
</h4>
<ul>
 <li>
  <a href="https://github.com/fabaff/mqtt-panel">
   mqtt-panel
  </a>
  <span>
   &#9733 83, pushed 79 days ago
  </span>
  - A web interface for MQTT.
 </li>
</ul>
<h3>
 Architecture
</h3>
<ul>
 <li>
  <a href="https://github.com/mqtt-smarthome/mqtt-smarthome">
   mqtt-smarthome
  </a>
  <span>
   &#9733 30, pushed 148 days ago
  </span>
  - Smart home automation with MQTT as the central message bus - Architectural proposal.
 </li>
</ul>
<h2>
 Contribute
</h2>
<p>
 Contributions welcome! Read the
 <a href="contributing.md">
  contribution guidelines
 </a>
 first.
</p>
<h2>
 License
</h2>
<p>
 <a href="http://creativecommons.org/publicdomain/zero/1.0/">
  <img alt="CC0" src="http://i.creativecommons.org/p/zero/1.0/88x31.png"/>
 </a>
</p>
