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
    <a href="#smart-home-hardware-interfaces">
     Smart Home Hardware Interfaces
    </a>
   </li>
   <li>
    <a href="#smart-home-integration-software">
     Smart Home Integration Software
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
  </ul>
 </li>
 <li>
  <a href="#visualization-dashboards">
   Visualization, Dashboards
  </a>
 </li>
 <li>
  <a href="#architecture-convention">
   Architecture, Convention
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
</ul>
<h4>
 Blogs
</h4>
<ul>
 <li>
  <a href="http://forkbomb-blog.de/category/mqtt">
   Dominik Obermaier (Forkbomb Blog)
  </a>
 </li>
 <li>
  <a href="http://jpmens.net/">
   Jan-Piet Mens
  </a>
 </li>
 <li>
  <a href="http://knolleary.net/">
   Nick O'Leary
  </a>
 </li>
</ul>
<h3>
 Broker
</h3>
<ul>
 <li>
  <a href="http://activemq.apache.org/">
   ActiveMQ
  </a>
  - A fast Java multiprotocol messaging and Integration Patterns server.
 </li>
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
  - Python MQTT broker using asyncio.
  <sup>
   &#9733 56, pushed 147 days ago
  </sup>
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
  - Java MQTT lightweight broker.
  <sup>
   &#9733 311, pushed 133 days ago
  </sup>
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
  <a href="https://www.rabbitmq.com/mqtt.html">
   RabbitMQ
  </a>
  - RabbitMQ offers a MQTT Adapter.
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
</ul>
<h3>
 Tools
</h3>
<ul>
 <li>
  <a href="https://github.com/shafreeck/imqtt">
   imqtt
  </a>
  - Interactive MQTT packet manipulation shell based on IPython.
 </li>
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
  - A benchmarking tool for MQTT Servers.
  <sup>
   &#9733 90, pushed 1634 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/F-Secure/mqtt_fuzz">
   mqtt-fuzz
  </a>
  - A simple fuzzer for the MQTT protocol.
  <sup>
   &#9733 23, pushed 486 days ago
  </sup>
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
  - A general MQTT testing app for iOS (iPhone and iPad).
  <sup>
   &#9733 40, pushed 196 days ago
  </sup>
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
  - scalability and load testing utilities for MQTT environments.
  <sup>
   &#9733 93, pushed 133 days ago
  </sup>
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
  - a collection of MQTT utilities.
  <sup>
   &#9733 2, pushed 1051 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/bastlirna/mqtt-wall">
   mqtt-wall
  </a>
  - Subscription only web-based client – like Twitter wall for MQTT.
 </li>
 <li>
  <a href="https://github.com/bapowell/python-mqtt-client-shell">
   Python MQTT Client Shell
  </a>
  - a text console-based, interactive shell for exercising various tasks associated with MQTT client communications.
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
  - MQTT for iOS and OS X written with Swift.
  <sup>
   &#9733 217, pushed 131 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/emqtt/emqttc">
   emqttc
  </a>
  - Asynchronous Erlang MQTT Client.
  <sup>
   &#9733 36, pushed 133 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/flightonary/Moscapsule">
   Moscapsule
  </a>
  - MQTT Client for iOS written in Swift
  <sup>
   &#9733 96, pushed 149 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/beerfactory/hbmqtt">
   hbmqtt
  </a>
  - Python MQTT client using asyncio.
 </li>
 <li>
  <a href="https://m2mqtt.wordpress.com/">
   M2Mqtt
  </a>
  - a MQTT client available for all .Net platforms (.Net Framework, .Net Compact Framework and .Net Micro Framework) and WinRT platforms (Windows 8.1, Windows Phone 8.1 and Windows 10).
 </li>
 <li>
  <a href="https://github.com/mgdm/Mosquitto-PHP">
   Mosquitto-PHP
  </a>
  - A wrapper for the Mosquitto MQTT client library for PHP.
 </li>
 <li>
  <a href="https://github.com/centamiv/mqtt-client">
   mqtt-client
  </a>
  - A Polymer Web Component that implements a MQTT client (uses Paho mqttws31.js).
  <sup>
   &#9733 7, pushed 473 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/ckrey/MQTT-Client-Framework">
   MQTT-Client-Framework
  </a>
  - iOS, OSX, tvOS native ObjectiveC MQTT Client Framework.
  <sup>
   &#9733 265, pushed 131 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jnguillerme/mqtt.dart">
   mqtt.dart
  </a>
  - dart mqtt client.
 </li>
 <li>
  <a href="https://github.com/mqttjs/mqtt-elements">
   mqtt-elements
  </a>
  - Polymer elements for MQTT.
 </li>
 <li>
  <a href="https://github.com/alfert/mqttex">
   mqttex
  </a>
  - MQTT implementation in Elixir.
  <sup>
   &#9733 34, pushed 480 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/mobile-web-messaging/MQTTKit">
   MQTTKit
  </a>
  - MQTT Objective-C client for iOS.
  <sup>
   &#9733 250, pushed 360 days ago
  </sup>
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
  - A client library for the Arduino Ethernet Shield that provides support for MQTT.
  <sup>
   &#9733 690, pushed 130 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/njh/ruby-mqtt">
   ruby-mqtt
  </a>
  - Pure Ruby gem that implements the MQTT protocol.
  <sup>
   &#9733 197, pushed 127 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Tingenek/tcl-mqtt">
   tcl-mqtt
  </a>
  - Small library to connect to a matt broker. Very, very basic.
 </li>
 <li>
  <a href="http://jamiei.com/blog/code/mqtt-client-library-for-delphi/">
   TMQTTClient
  </a>
  - MQTT Client Library for Delphi.
 </li>
 <li>
  <a href="https://wolfssl.com/wolfSSL/Products-wolfmqtt.html">
   wolfMQTT
  </a>
  - a client implementation of the MQTT written in C for embedded use. It supports SSL/TLS via the wolfSSL library.
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
  - Java based Logic and scripting engine for use with MQTT. Uses Java's general scripting interface, so scripts can be written in a multitude of languages like Javascript, Groovy etc.
  <sup>
   &#9733 4, pushed 189 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/hobbyquaker/mqtt-scripts/">
   mqtt-scripts
  </a>
  - Node.js based script runner.
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
  - Arduino RFM69 based sensors and MQTT gateway.
  <sup>
   &#9733 52, pushed 149 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/hobbyquaker/rpi2mqtt">
   rpi2mqtt
  </a>
  - Connect a RaspberryPis GPIOs and 1-Wire Temperature Sensors to MQTT.
  <sup>
   &#9733 2, pushed 358 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/xoseperez/xbee2mqtt">
   xbee2mqtt
  </a>
  - XBee to MQTT gateway.
  <sup>
   &#9733 13, pushed 213 days ago
  </sup>
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
  - Modbus master which publishes register values via MQTT.
  <sup>
   &#9733 10, pushed 203 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/nzfarmer1/mqtt2opcua">
   mqtt2opcua
  </a>
  - Bi Directional MQTT to OPCUA Bridge.
  <sup>
   &#9733 9, pushed 400 days ago
  </sup>
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
  - Interface between Asterisk and MQTT.
  <sup>
   &#9733 13, pushed 861 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/akentner/fritz2mqtt">
   fritz2mqtt
  </a>
  - Connect FRITZ!Box to MQTT.
  <sup>
   &#9733 1, pushed 360 days ago
  </sup>
 </li>
</ul>
<h4>
 Operating System
</h4>
<ul>
 <li>
  <a href="https://github.com/jpmens/mqtt-launcher">
   mqttlauncher
  </a>
  - Execute shell commands triggered by published MQTT messages.
  <sup>
   &#9733 11, pushed 880 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/oskarhagberg/mqtt-os-status">
   mqtt-os-status
  </a>
  - Operating-system related data, published to an MQTT broker at fixed intervals.
  <sup>
   &#9733 4, pushed 881 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/hobbyquaker/mqttpc">
   mqttpc
  </a>
  - Control processes via MQTT. Ability to send signals via MQTT and to publish stdout/stderr or pipe MQTT payloads into stdin.
 </li>
 <li>
  <a href="https://github.com/jpmens/mqtt-watchdir">
   mqttwatchdir
  </a>
  - Recursively watch a directory for modifications and publish file content to an MQTT broker.
  <sup>
   &#9733 13, pushed 490 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/eschava/psmqtt">
   psmqtt
  </a>
  - Utility reporting system health and status via MQTT
  <sup>
   &#9733 6, pushed 141 days ago
  </sup>
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
  - A Nagios/Icinga plugin for checking connectivity to an MQTT broker.
  <sup>
   &#9733 6, pushed 240 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jpmens/notify-by-mqtt">
   notify-by-mqtt
  </a>
  - a Nagios/Icinga notification module which wraps data into JSON and fires it off to an MQTT broker.
  <sup>
   &#9733 6, pushed 818 days ago
  </sup>
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
  <a href="https://github.com/jpmens/mqttcollect">
   mqttcollect
  </a>
  - collectd "Exec" plugin for MQTT.
 </li>
 <li>
  <a href="https://github.com/Graylog2/graylog-plugin-mqtt">
   graylog-plugin-mqtt
  </a>
  - MQTT Input Plugin for Graylog.
 </li>
 <li>
  <a href="https://github.com/jpmens/mqtt2graphite">
   mqtt2graphite
  </a>
  - Subscribe to MQTT topics and push to Graphite's Carbon server.
  <sup>
   &#9733 39, pushed 260 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/hobbyquaker/influx4mqtt">
   influx4mqtt
  </a>
  - Subscribe to MQTT topics and insert into InfluxDB.
  <sup>
   &#9733 3, pushed 428 days ago
  </sup>
 </li>
</ul>
<h4>
 Smart Home Hardware Interfaces
</h4>
<ul>
 <li>
  <a href="https://github.com/hobbyquaker/cul2mqtt">
   cul2mqtt
  </a>
  - Interface between
  <a href="http://shop.busware.de/product_info.php/cPath/1/products_id/29">
   Busware CUL
  </a>
  (868MHz RF-Devices like ELV FS20, HMS, EM, ...) and MQTT.
  <sup>
   &#9733 0, pushed 359 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/owagner/eno2mqtt">
   eno2mqtt
  </a>
  - Interface between an Enocean USB300 (TCM310) adapter and MQTT.
  <sup>
   &#9733 3, pushed 136 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/owagner/hm2mqtt">
   hm2mqtt
  </a>
  - Interface between EQ-3's Homematic line of smarthome devices and MQTT.
  <sup>
   &#9733 10, pushed 190 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/owagner/knx2mqtt">
   knx2mqtt
  </a>
  - Interface between the KNX home automation standard and MQTT.
  <sup>
   &#9733 5, pushed 354 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/cgHome/mqtt-dss-bridge">
   mqtt-dss-bridge
  </a>
  - MQTT digitalSTROM-Server Bridge.
  <sup>
   &#9733 2, pushed 347 days ago
  </sup>
 </li>
</ul>
<h4>
 Smart Home Integration Software
</h4>
<ul>
 <li>
  <a href="http://fhem.de/fhem.html">
   FHEM
  </a>
  has a
  <a href="http://fhem.de/commandref.html#MQTT">
   MQTT module
  </a>
  since V5.6.
 </li>
 <li>
  <a href="https://home-assistant.io/">
   Home Assistant
  </a>
  has a MQTT component.
 </li>
 <li>
  <a href="https://github.com/hobbyquaker/homekit2mqtt">
   homekit2mqtt
  </a>
  - Interface between
  <a href="https://github.com/KhaosT/HAP-NodeJS">
   HAP-NodeJS
  </a>
  and MQTT. Control MQTT connected devices with Siri or HomeKit Apps.
  <sup>
   &#9733 3, pushed 245 days ago
  </sup>
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
  <a href="https://github.com/net-commander/windows-dist">
   Net-Commander
  </a>
  has built in MQTT connectivity.
 </li>
 <li>
  <a href="https://github.com/openhab">
   openHAB
  </a>
  has a
  <a href="https://github.com/openhab/openhab/wiki/MQTT-Binding">
   MQTT binding
  </a>
  .
 </li>
 <li>
  <a href="https://pimatic.org/">
   pimatic
  </a>
  has a MQTT plugin.
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
  - Control Chromoflex USP3 RGB LED modules via MQTT
  <sup>
   &#9733 1, pushed 275 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/owagner/hue2mqtt">
   hue2mqtt
  </a>
  - Interface between the Philips Hue bridge and MQTT.
  <sup>
   &#9733 14, pushed 187 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/hobbyquaker/mqtt-dmx-sequencer">
   mqtt-dmx-sequencer
  </a>
  - Control DMX devices via Art-Net by MQTT.
  <sup>
   &#9733 1, pushed 359 days ago
  </sup>
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
  - MQTT controlled Multi-Room Audio with Airplay/Airtunes Devices.
  <sup>
   &#9733 2, pushed 359 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/owagner/kodi2mqtt">
   kodi2mqtt
  </a>
  - Interface between a Kodi mediacenter instance and MQTT.
  <sup>
   &#9733 17, pushed 127 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/hobbyquaker/lgtv2mqtt">
   lgtv2mqtt
  </a>
  - Interface between LG WebOS Smart TVs and MQTT.
 </li>
 <li>
  <a href="https://github.com/hobbyquaker/lirc2mqtt">
   lirc2mqtt
  </a>
  - Send and receive infrared via
  <a href="www.lirc.org">
   LIRC
  </a>
  .
  <sup>
   &#9733 2, pushed 302 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/owagner/onkyo2mqtt">
   onkyo2mqtt
  </a>
  - Interface between Onkyo AVR's EISCP network remote protocol and MQTT. Uses the onkyo-eiscp library.
  <sup>
   &#9733 3, pushed 456 days ago
  </sup>
 </li>
 <li>
  <a href="https://wiki.videolan.org/Documentation:Modules/mqtt/">
   VLC MQTT Module
  </a>
  - Control VLC via MQTT.
 </li>
 <li>
  <a href="https://github.com/gordonjcp/xbmc-mqtt">
   xbmc2mqtt
  </a>
  - A simple plugin for XBMC to listen for a particular topic on an MQTT broker, and display a popup message.
  <sup>
   &#9733 4, pushed 538 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/akentner/yamaha-avr2mqtt">
   yamaha-avr2mqtt
  </a>
  <sup>
   &#9733 1, pushed 251 days ago
  </sup>
 </li>
</ul>
<h4>
 Gadgets
</h4>
<ul>
 <li>
  <a href="https://github.com/hobbyquaker/dashbutton2mqtt">
   dashbutton2mqtt
  </a>
  - Publish dash button presses to MQTT.
 </li>
 <li>
  <a href="https://github.com/hobbyquaker/flowerpower2mqtt">
   flowerpower2mqtt
  </a>
  - Publish measurements from
  <a href="http://www.parrot.com/usa/products/flower-power/">
   Parrot Flower Power
  </a>
  plant sensors to MQTT.
  <sup>
   &#9733 0, pushed 317 days ago
  </sup>
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
  - Publish measurements from
  <a href="http://www.tq-group.com/produkte/produktdetail/prod/energy-manager/extb/Main/">
   TQ Energy Manager
  </a>
  to MQTT.
  <sup>
   &#9733 0, pushed 359 days ago
  </sup>
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
  - A MQTT to IRC / IRC to MQTT bridge or bot.
  <sup>
   &#9733 10, pushed 308 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jpmens/mqttwarn">
   mqttwarn
  </a>
  - Subscribe to MQTT topics (with wildcards) and notifiy pluggable services.
  <sup>
   &#9733 382, pushed 138 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/knolleary/twitter-to-mqtt">
   twitter-to-mqtt
  </a>
  - A python daemon that uses the Twitter Streaming API to access tweets and republishes them to an MQTT topic.
  <sup>
   &#9733 9, pushed 1356 days ago
  </sup>
 </li>
</ul>
<h3>
 Visualization, Dashboards
</h3>
<ul>
 <li>
  <a href="https://github.com/hardillb/d3-MQTT-Topic-Tree">
   d3-MQTT-Topic-Tree
  </a>
  - A MQTT Topic Tree viewer using the d3 collapsable tree and MQTT over websockets
 </li>
 <li>
  <a href="https://github.com/node-red/node-red-dashboard">
   node-red-dashboard
  </a>
  - A dashboard UI for Node-RED.
 </li>
 <li>
  <a href="https://github.com/fabaff/mqtt-panel">
   mqtt-panel
  </a>
  - A web interface for MQTT.
  <sup>
   &#9733 83, pushed 204 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jpmens/mqtt-svg-dash">
   mqtt-svg-dash
  </a>
  - Subscribe to MQTT, extract JSON from a message and make lights blink on an SVG page.
 </li>
</ul>
<p>
 Other tools that can be used to create Visualization/Dashboards can be found under
 <a href="#smart-home-integration-software">
  Smart Home Integration Software
 </a>
</p>
<h3>
 Architecture, Convention
</h3>
<ul>
 <li>
  <a href="https://github.com/marvinroger/homie">
   Homie
  </a>
  - A lightweight MQTT convention for the IoT
 </li>
 <li>
  <a href="https://github.com/mqtt-smarthome/mqtt-smarthome">
   mqtt-smarthome
  </a>
  - Smart home automation with MQTT as the central message bus - Architectural proposal.
  <sup>
   &#9733 30, pushed 273 days ago
  </sup>
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
