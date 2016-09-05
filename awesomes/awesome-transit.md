<h1>
 awesome-transit
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<h5>
 A collection of awesome transit projects  :busstop: :bus::dash: :train::dash: :steam_locomotive::dash:
</h5>
<p>
 Have something to add or change? Open a
 <a href="https://github.com/luqmaan/awesome-transit/pulls">
  pull request
 </a>
 or
 <a href="https://github.com/luqmaan/awesome-transit/issues">
  issue
 </a>
 .
</p>
<hr/>
<h3>
 Table of Contents
</h3>
<ul>
 <li>
  <a href="#community">
   Community
  </a>
 </li>
 <li>
  <a href="#data">
   Data
  </a>
 </li>
 <li>
  <a href="#apis">
   APIs
  </a>
 </li>
 <li>
  <a href="#agency-tools">
   Agency Tools
  </a>
 </li>
 <li>
  <a href="#hardware">
   Hardware
  </a>
 </li>
 <li>
  <a href="#web-apps">
   Web Apps
  </a>
 </li>
 <li>
  <a href="#native-apps-open-source">
   Native Apps (open source)
  </a>
 </li>
 <li>
  <a href="#native-apps-closed-source">
   Native Apps (closed source)
  </a>
 </li>
 <li>
  <a href="#visualizations">
   Visualizations
  </a>
 </li>
 <li>
  <a href="#resources">
   Resources
  </a>
 </li>
 <li>
  <a href="#gtfs">
   GTFS
  </a>
 </li>
 <li>
  <a href="#gtfs-realtime">
   GTFS-realtime
  </a>
 </li>
 <li>
  <a href="#siri">
   SIRI
  </a>
 </li>
</ul>
<h3>
 Community
</h3>
<p>
 Places to ask questions and find other community resources.
</p>
<ul>
 <li>
  <a href="http://transitwiki.org">
   TransitWiki
  </a>
  - A community wiki for transit planners. Like this repo, but better.
 </li>
 <li>
  <a href="https://groups.google.com/forum/#!forum/transit-developers">
   Transit Developers mailing list
  </a>
 </li>
 <li>
  OneBusAway
  <ul>
   <li>
    <a href="http://groups.google.com/group/onebusaway-users">
     OneBusAway User mailing list
    </a>
   </li>
   <li>
    <a href="http://groups.google.com/group/onebusaway-developers">
     OneBusAway Developers mailing list
    </a>
   </li>
   <li>
    <a href="http://groups.google.com/group/onebusaway-api">
     OneBusAway API mailing list
    </a>
   </li>
   <li>
    <a href="https://onebusaway.herokuapp.com/">
     OneBusAway Slack chat
    </a>
   </li>
  </ul>
 </li>
</ul>
<h3>
 Data
</h3>
<ul>
 <li>
  <a href="https://transit.land/">
   Transitland
  </a>
  - Community editable list of many transit agency GTFS datasets. Also provides an API to access the data as JSON/GeoJSON and a playground to try out the data.
 </li>
 <li>
  <a href="https://github.com/scascketta/CapMetrics">
   CapMetrics
  </a>
  - Historical vehicle locations for Austin's transit agency (CapMetro). Data is collected by
  <a href="https://github.com/scascketta/capmetricsd">
   capmetricsd
  </a>
  , a Go daemon.
  <sup>
   &#9733 7, pushed 127 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.ntdprogram.gov/">
   National Transit Database
  </a>
  - Information and statistics on the transit systems of the United States, run by the Federal Transit Administration.
 </li>
 <li>
  <a href="http://transitfeeds.com/">
   TransitFeeds
  </a>
  - List of GTFS and GTFS-RT feeds.
  <a href="http://transitfeeds.com/p/capital-metro/24">
   Archives and validates
  </a>
  the GTFS feeds and allows you to preview both
  <a href="http://transitfeeds.com/p/capital-metro/24/20151015">
   GTFS
  </a>
  and
  <a href="http://transitfeeds.com/p/capital-metro/495">
   GTFS-RT
  </a>
  through the browser.
 </li>
 <li>
  <a href="https://www.mashape.com/transloc/openapi-1-2">
   TransLoc OpenAPI
  </a>
  - Real-time vehicle, route, stop, and arrival data for over 60 transit systems in the United States.
 </li>
 <li>
  <a href="http://www.gtfs-data-exchange.com/agencies">
   GTFS Data Exchange
  </a>
  - Used to be the definitive list of GTFS links. Shutdown in 2016. But 93G of data from 2008 to 2016 is available upon request.
 </li>
</ul>
<h3>
 APIs
</h3>
<p>
 Software that provides an API to transit data.
</p>
<ul>
 <li>
  <a href="http://www.navitia.io/">
   Navitia.io
  </a>
  - REST API for journey planning, stop schedules, isocrhons and lot more on US and EU.
  <a href="https://github.com/CanalTP/navitia">
   Navitia
  </a>
  is the opensource engine behind the live API.
 </li>
 <li>
  <a href="http://onebusaway.org/">
   OneBusAway
  </a>
  - A Java app that consumes GTFS and GTFS-Realtime (along with
  <a href="https://github.com/OneBusAway/onebusaway-application-modules/wiki/Real-Time-Data-Configuration-Guide">
   other formats
  </a>
  ) and turns them into an easy to use
  <a href="http://developer.onebusaway.org/modules/onebusaway-application-modules/current/api/where/index.html">
   REST API
  </a>
  .
 </li>
 <li>
  <a href="http://www.transitime.org">
   TransiTime
  </a>
  - Java application that can consume raw vehicle positions and generate prediction times in formats such as GTFS-realtime.
 </li>
 <li>
  <a href="https://github.com/eskerda/pybikes">
   pyBikes
  </a>
  - an API on worldwide bikeshare systems powering
  <a href="http://api.citybik.es">
   CityBikes
  </a>
  <sup>
   &#9733 145, pushed 131 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.opentripplanner.org/">
   OpenTripPlanner
  </a>
  - An open source platform for multi-modal and multi-agency journey planning, as well as returning information about a multi-modal graph (using data sources such as GTFS and
  <a href="http://www.openstreetmap.org/">
   OpenStreetMap
  </a>
  ).
 </li>
 <li>
  <a href="http://linkedconnections.org/">
   Linked Connections
  </a>
  - An open-source, scalable intermodal route planning engine, which allows clients to execute the route planning algorithm (as opposed to the server). Uses GTFS data.
 </li>
</ul>
<h3>
 Agency Tools
</h3>
<p>
 Tools for transit agencies.
</p>
<ul>
 <li>
  <a href="http://getremix.com/">
   Remix
  </a>
  - A webapp that lets transit agencies easily plan routes.
 </li>
</ul>
<h3>
 Hardware
</h3>
<p>
 Experimental and production transit hardware.
</p>
<ul>
 <li>
  <a href="https://github.com/herrdragon/busTrackingGps">
   Bus Tracking GPS
  </a>
  - Code for Miami prototype of a cheap open-source solution to track transit buses.
  <sup>
   &#9733 3, pushed 187 days ago
  </sup>
 </li>
</ul>
<h3>
 Web Apps
</h3>
<ul>
 <li>
  <a href="http://transitscreen.com/">
   TransitScreen
  </a>
  - Custom realtime displays of all local transportation choices
 </li>
 <li>
  <a href="http://instabus.org">
   Instabus
  </a>
  - Realtime map of Austin's (CapMetro) public transit. Has no server/backend dependency at all and runs completely on GitHub pages.
 </li>
 <li>
  <a href="http://mtabustrack.herokuapp.com/">
   Maryland MTA Real-time Vehicle Tracking
  </a>
 </li>
 <li>
  <a href="https://github.com/mecatran/OpenTripPlanner-client-gwt">
   OpenTripPlanner Client GWT
  </a>
  - A Google Web Toolkit-based web interface for OpenTripPlanner
  <sup>
   &#9733 5, pushed 269 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/conveyal/otp.js">
   OpenTripPlanner.js
  </a>
  - A Javascript-based client for OpenTripPlanner
  <sup>
   &#9733 11, pushed 168 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/OneBusAway/onebusaway-service-alerts">
   GTFS-realtime Alerts Producer Web Application
  </a>
  - A Java-based web application for producing GTFS-realtime Service Alerts.
  <sup>
   &#9733 1, pushed 1664 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Code4HR/hrt-bus-api">
   HRT BUS Web app
  </a>
  - HRT Bus API publishes real time bus data from Hampton Roads Transit through an application programming interface for developers to make apps from it.
  <sup>
   &#9733 14, pushed 144 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/vasile/transit-map">
   Transit-Map
  </a>
  - Web app that animates vehicles (markers) on a map using the public transport timetables to interpolate their positions along the routes (polylines).
  <sup>
   &#9733 217, pushed 459 days ago
  </sup>
 </li>
 <li>
  <a href="http://bikes.oobrien.com/">
   Bikeshare Map
  </a>
  - Status of all worldwide bikeshare stations
 </li>
 <li>
  <a href="http://ebongo.org">
   Bongo
  </a>
  - Real-time Transit Tracking for Iowa City, Coralville and the University of Iowa. Awesome because it combines three disparate transit systems into one UI.
 </li>
 <li>
  <a href="https://github.com/conveyal/transitive.js">
   Transitive.js
  </a>
  - Creates a customizable web map layer of transit routes using Leaflet or D3.
 </li>
</ul>
<h3>
 Native Apps (open source)
</h3>
<ul>
 <li>
  OneBusAway Apps -
  <a href="https://play.google.com/store/apps/details?id=com.joulespersecond.seattlebusbot">
   Android
  </a>
  <a href="https://github.com/OneBusAway/onebusaway-android">
   <em>
    (source code)
   </em>
  </a>
  ,
  <a href="http://www.amazon.com/gp/mas/dl/android?p=com.joulespersecond.seattlebusbot">
   Fire Phone
  </a>
  <a href="https://github.com/OneBusAway/onebusaway-android">
   <em>
    (source code)
   </em>
  </a>
  ,
  <a href="https://itunes.apple.com/us/app/onebusaway/id329380089">
   iOS
  </a>
  <a href="https://github.com/OneBusAway/onebusaway-iphone">
   <em>
    (source code)
   </em>
  </a>
  ,
  <a href="https://www.microsoft.com/en-us/store/apps/onebusaway/9nblggh0cbd9">
   Windows Phone
  </a>
  <a href="https://github.com/OneBusAway/onebusaway-windows-phone">
   <em>
    (source code)
   </em>
  </a>
  ,
  <a href="https://www.microsoft.com/en-us/store/apps/onebusaway/9wzdncrdm5pc">
   Windows 8
  </a>
  <a href="https://github.com/OneBusAway/onebusaway-windows8">
   <em>
    (source code)
   </em>
  </a>
  ,
  <a href="https://github.com/OneBusAway/onebusaway-android/pull/219">
   Google Glass GDK
  </a>
  <a href="https://github.com/OneBusAway/onebusaway-android/pull/219">
   <em>
    (source code)
   </em>
  </a>
 </li>
 <li>
  <a href="https://github.com/CUTR-at-USF/OpenTripPlanner-for-Android/wiki">
   OpenTripPlanner Android
  </a>
  - An Android app for
  <a href="http://www.opentripplanner.org/">
   OpenTripPlanner
  </a>
 </li>
 <li>
  <a href="https://github.com/opentripplanner/OpenTripPlanner-iOS">
   OpenTripPlanner iOS
  </a>
  - An iOS app for
  <a href="http://www.opentripplanner.org/">
   OpenTripPlanner
  </a>
  <sup>
   &#9733 57, pushed 1348 days ago
  </sup>
 </li>
</ul>
<h3>
 Native Apps (closed source)
</h3>
<ul>
 <li>
  <a href="http://www.allyapp.com/">
   ally
  </a>
 </li>
 <li>
  <a href="http://transitapp.com/">
   Transit App
  </a>
 </li>
 <li>
  <a href="https://citymapper.com/">
   CityMapper
  </a>
 </li>
 <li>
  <a href="http://moovitapp.com/">
   Moovit
  </a>
 </li>
 <li>
  <a href="http://www.tiramisutransit.com/">
   Tiramisu Transit
  </a>
 </li>
 <li>
  <a href="http://ridescout.com/">
   Ridescout
  </a>
 </li>
 <li>
  <a href="http://translocrider.com/">
   TransLoc Rider
  </a>
  - Real-time transit maps for over 100 transit systems.
 </li>
</ul>
<h3>
 Visualizations
</h3>
<ul>
 <li>
  <a href="http://mbtaviz.github.io/">
   Visualizing MBTA Data
  </a>
  - Interactive graphs that show how people use Boston's subway system.
 </li>
 <li>
  <a href="http://mittransportanalyst.github.io/">
   MIT COAXS
  </a>
  - Co-creative Planning of Transit Corridors using Accessibility-Based Stakeholder Engagement (shows route scenarios using
  <a href="http://www.opentripplanner.org/analyst/">
   OpenTripPlanner Analyst
  </a>
  ).
 </li>
 <li>
  <a href="http://tracker.geops.ch/">
   TRAVIC Transit Visualization Client
  </a>
  - Visualizes vehicles moving based on static GTFS data (and sometimes realtime data). Supports over 260 cities.  Github account for geOps organization is
  <a href="https://github.com/geops">
   here
  </a>
  .
 </li>
 <li>
  <a href="http://allthebuses.com/">
   Muni, this moment
  </a>
  - Realtime map of all the buses in San Francisco.
 </li>
 <li>
  <a href="http://www.tyleragreen.com/maps/new_york/">
   MTA Frequency
  </a>
  - Frequency visualization of subways and buses in New York City built using
  <a href="https://transit.land/">
   Transitland
  </a>
  .
 </li>
</ul>
<h3>
 Resources
</h3>
<ul>
 <li>
  <a href="http://faculty.washington.edu/jhullman/busUncertaintyVis.pdf">
   When(ish) is my bus? User-centered Visualizations of Uncertainty in Everyday, Mobile Predictive Systems
  </a>
  - Paper that does an amazing job answering the question of how do we communicate uncertainty in transit predictions? The paper explains the problem, existing solutions and designs a
  <a href="https://github.com/mjskay/when-ish-is-my-bus/blob/master/quantile-dotplots.md#quantile-dotplots">
   better interface for letting users know when to arrive at the bus stop
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/mjskay/when-ish-is-my-bus">
   When(ish) is my bus? Data and code
  </a>
  - The data and code (R) behind Whenish is my bus? Data includes three days of historical vehicle positions and the survey results.
 </li>
 <li>
  <a href="https://kurtraschke.com/2015/01/legacy-avl-export">
   "Legacy AVL system? It's okay, join the club." by Kurt Raschke
  </a>
  - Good discussion of options for transforming legacy AVL system data into the GTFS-realtime format.
 </li>
 <li>
  <a href="http://www.apta.com/resources/reportsandpublications/Documents/APTA-Embracing-Open-Data.pdf">
   APTA Policy Development and Research - Public Transportation Embracing Open Data
  </a>
  - APTA's discussion of the benefits and challenges of open transit data (a short summary of the below TCRP report).
 </li>
 <li>
  <a href="http://onlinepubs.trb.org/Onlinepubs/tcrp/tcrp_syn_115.pdf">
   TCRP Synthesis 115 - Open Data: Challenges and Opportunities for Transit Agencies
  </a>
  - A comprehensive report looking at the benefits and challenges of open transit data.
 </li>
</ul>
<h3>
 GTFS
</h3>
<p>
 Software that makes it easy to consume GTFS data.
</p>
<ul>
 <li>
  <a href="https://github.com/transitland/mapzen-gtfs">
   Mapzen GTFS
  </a>
  - A Python GTFS library that supports reading individual GTFS tables, or constructing a graph to represent each agency in a feed.
  <sup>
   &#9733 7, pushed 353 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/OpenTransitTools/gtfsdb">
   gtfsdb
  </a>
  - Python library for converting GTFS files into a relational database.
  <sup>
   &#9733 25, pushed 128 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/OneBusAway/onebusaway-gtfs-modules/wiki">
   OneBusAway GTFS Modules
  </a>
  - A Java-based library for reading, writing, and transforming public transit data in the GTFS format, including database support.
 </li>
 <li>
  <a href="https://github.com/TransitFeeds/GtfsToSql">
   GTFS to SQL
  </a>
  - Parses a GTFS feed into an SQL database (used in
  <a href="http://transitfeeds.com/">
   TransitFeeds.com
  </a>
  )
  <sup>
   &#9733 6, pushed 622 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/TransitFeeds/SqlToGtfs">
   SQL to GTFS
  </a>
  - Convert an SQLite file generated with "GtfsToSql" back to a zipped GTFS file.
  <sup>
   &#9733 3, pushed 630 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/geops/gtfsparser">
   Go GTFS Parser
  </a>
  - A GTFS parsing library for Go
  <sup>
   &#9733 12, pushed 196 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/OsmSharp/GTFS">
   GTFS Feed Parser
  </a>
  - .Net/Mono implementation of a GTFS parser
  <sup>
   &#9733 20, pushed 136 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/brendannee/node-gtfs">
   Node-GTFS
  </a>
  - Loads transit data in
  <a href="https://developers.google.com/transit/">
   GTFS format
  </a>
  from
  <a href="http://www.gtfs-data-exchange.com/">
   GTFS Data Exchange
  </a>
  , unzips it and stores it to a MongoDB database and provides some methods to query for agencies, routes, stops and times.
  <sup>
   &#9733 164, pushed 142 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/vasile/GTFS-viz">
   GTFS-viz
  </a>
  - Ruby script that converts a set of GTFS files into a SQLite database + GeoJSONs (needed by the
  <a href="https://github.com/vasile/transit-map">
   Transit Map
  </a>
  web application)
  <sup>
   &#9733 48, pushed 168 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/CUTR-at-USF/gtfs-osm-sync">
   GTFS-OSM-Sync
  </a>
  - A Java tool for syncrhonizing data in GTFS format with
  <a href="http://www.openstreetmap.org/">
   OpenStreetMap.org
  </a>
  .
  <sup>
   &#9733 38, pushed 213 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/bliksemlabs/bliksemintegration">
   Transmodel and IFF to GTFS
  </a>
  - Imports and syncs (Transmodel) BISON Koppelvlak1, IFF (a format written by HP/EDS, somewhat similiar to ATCO CIF) to import timetables of the railway networks. The internal pseudo-NETeX datastructure allows to export to GTFS and there are proof-of-concepts to export to other formats such as NETeX, GTFS and IFF.
  <sup>
   &#9733 1, pushed 422 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Open-Transport/synthese/wiki">
   Open-Transport SYNTHESE Convertors
  </a>
  - Converts French-Transmodel, SIRI, NETeX, HAFAS, HASTUS, VDV452, and more.
 </li>
 <li>
  <a href="http://www.chouette.mobi/">
   Chouette
  </a>
  - Converts French-Transmodel, SIRI, NETeX. See Chouette.mobi website for more info.
 </li>
 <li>
  <a href="https://github.com/atlregional/bus-router">
   bus-router
  </a>
  - Python script that generates missing shapes.txt for GTFS using routing from
  <a href="https://developers.google.com/maps/documentation/directions/">
   Google Maps Directions API
  </a>
  or
  <a href="https://github.com/Project-OSRM/osrm-backend/wiki/Server-api">
   OSRM
  </a>
  .
  <sup>
   &#9733 15, pushed 368 days ago
  </sup>
 </li>
 <li>
  <a href="http://transitwand.com/">
   TransitWand
  </a>
  - An open source web and mobile application for collecting transit data. Use it to create GTFS feeds, capture passenger counts or generate GIS datasets.
 </li>
 <li>
  <a href="https://github.com/evansiroky/gtfs-sequelize">
   gtfs-sequelize
  </a>
  - Node.js library modeling the static GTFS using
  <a href="http://sequelizejs.com/">
   sequelize.js
  </a>
  .
  <sup>
   &#9733 7, pushed 131 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/afimb/gtfslib-python">
   gtfslib-python
  </a>
  -  An open source library in python for reading GTFS files and computing various stats and indicators about Public Transport networks.
  <sup>
   &#9733 12, pushed 157 days ago
  </sup>
 </li>
</ul>
<h3>
 GTFS-realtime
</h3>
<ul>
 <li>
  <a href="https://github.com/google/gtfs-realtime-bindings">
   gtfs-realtime-bindings
  </a>
  - The official bindings for Java, .NET, Node.js, Python, and Ruby generated from the official
  <a href="https://github.com/google/gtfs-realtime-bindings/blob/master/gtfs-realtime.proto">
   GTFS-realtime protocol buffer specification
  </a>
  .
  <sup>
   &#9733 59, pushed 222 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/kurtraschke/gtfs-rt-dump">
   gtfs-rt-dump
  </a>
  - Converts protocol buffer format to plain text for easy viewing of a GTFS-realtime feed in plain text (for debugging purposes)
 </li>
 <li>
  <a href="https://github.com/mattwigway/gtfsrdb">
   gtfsrdb
  </a>
  - A Python tool that supports reading and archiving GTFS-realtime feeds into a database
  <sup>
   &#9733 32, pushed 570 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/TransitFeeds/GtfsRealTimeToSql">
   GTFS-realtime to SQL
  </a>
  - Parses a GTFS-RealTime feed into an SQL database (used in
  <a href="http://transitfeeds.com/">
   TransitFeeds.com
  </a>
  )
  <sup>
   &#9733 8, pushed 404 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/CUTR-at-USF/gtfs-realtime-validator">
   GTFS-realtime Validator
  </a>
  - A Java-based tool that validates GTFS-realtime feeds
  <sup>
   &#9733 5, pushed 323 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/OneBusAway/onebusaway-gtfs-realtime-exporter/wiki">
   GTFS-realtime Exporter
  </a>
  - A Java-based tool that assists in producing and sharing a GTFS-relatime feed.
 </li>
 <li>
  <a href="https://github.com/OneBusAway/onebusaway-gtfs-realtime-alerts-producer-demo/wiki">
   GTFS-realtime Alerts Producer Demo
  </a>
  - A Java-based demo project for producing GTFS-realtime Service Alerts.
 </li>
 <li>
  <a href="https://github.com/OneBusAway/onebusaway-service-alerts">
   GTFS-realtime Alerts Producer Web Application
  </a>
  - A Java-based web application for producing GTFS-realtime Service Alerts.
 </li>
 <li>
  <a href="https://github.com/OneBusAway/onebusaway-gtfs-realtime-trip-updates-producer-demo/wiki">
   GTFS-realtime TripUpdates & VehiclePositions Producer Demo
  </a>
  - A Java-based demo project for producing GTFS-realtime TripUpdates (estimated arrivals) and Vehicle Positions.
 </li>
 <li>
  <a href="https://github.com/OneBusAway/onebusaway-gtfs-realtime-visualizer/wiki">
   GTFS-realtime Vehicle Positions Consumer/Visualizer Demo
  </a>
  - A Java-based demo project for consuming a GTFS-realtime Vehicle Positions feed and displaying this info on a map.
 </li>
 <li>
  <a href="https://github.com/OneBusAway/onebusaway-gtfs-realtime-from-siri-cli/wiki">
   SIRI to GTFS-realtime
  </a>
  - A Java-based command-line utility to convert from the
  <a href="http://user47094.vs.easily.co.uk/siri/">
   SIRI format
  </a>
  to GTFS-realtime
 </li>
 <li>
  <a href="https://github.com/CUTR-at-USF/HART-GTFS-realtimeGenerator/wiki">
   OrbCAD SQL Server to GTFS-realtime
  </a>
  - A Java-based command-line utility that extracts vehicle positions and trip updates information from an OrbCAD SQL Server and exports them to the GTFS-realtime TripUpdates and VehiclePositions formats.
 </li>
 <li>
  <a href="https://github.com/OneBusAway/onebusaway-gtfs-realtime-from-nextbus-cli/wiki">
   NextBus API to GTFS-realtime
  </a>
  - A Java-based command-line utility to convert from the
  <a href="http://www.nextbus.com/xmlFeedDocs/NextBusXMLFeed.pdf">
   NextBus API format
  </a>
  to GTFS-realtime.
 </li>
 <li>
  <a href="https://github.com/CUTR-at-USF/bullrunner-gtfs-realtime-generator">
   Syncromatics API to GTFS-realtime
  </a>
  - A Java-based command-line utility to convert from the
  <a href="http://www.syncromatics.com/">
   Syncromatics API
  </a>
  format to GTFS-realtime TripUpdates and VehiclePositons.
  <sup>
   &#9733 0, pushed 234 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/bliksemlabs/bliksemintegration-realtime">
   KV6,15,17, and ARNU to GTFS-realtime
  </a>
  - Java-based tool to process incoming KV6,15,17 and ARNU and match them to static transit data present in a RID integration database. It then proceeds to export this data as ARNU RITinfo, GTFS(realtime) and KV78turbo
  <sup>
   &#9733 0, pushed 668 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/kurtraschke/wmata-gtfsrealtime">
   WMATA BusPositions API to GTFS-realtime
  </a>
  - Java-based tool to convert from WMATA's
  <a href="https://developer.wmata.com/docs/services/54763629281d83086473f231/operations/5476362a281d830c946a3d68">
   BusPositions API
  </a>
  and Alert RSS feeds from
  <a href="http://www.wmata.com/rider_tools/metro_service_status/rail_bus.cfm?">
   MetroAlerts
  </a>
  to GTFS-realtime TripUpdates, VehiclePositions, and Alerts feeds.
  <sup>
   &#9733 11, pushed 571 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/kurtraschke/septa-gtfsrealtime">
   SEPTA API to GTFS-realtime
  </a>
  - Java-based tool to convert
  <a href="http://www.septa.org/">
   SEPTA's
  </a>
  <a href="http://www3.septa.org/hackathon/">
   real-time bus and rail data
  </a>
  to GTFS-realtime
  <sup>
   &#9733 0, pushed 806 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/kurtraschke/ctatt-gtfsrealtime">
   CTA API to GTFS-realtime
  </a>
  - Java-based tool to convert
  <a href="http://www.transitchicago.com/">
   CTA's
  </a>
  <a href="http://www.transitchicago.com/developers/traintracker.aspx">
   Train Tracker data
  </a>
  to GTFS-realtime.
  <sup>
   &#9733 1, pushed 982 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/prashtx/ddot-avl">
   Detroit DOT to GTFS-realtime
  </a>
  - Extract real-time info from
  <a href="http://www.detroitmi.gov/How-Do-I/Locate-Transportation/Bus-Schedules">
   DDOT's
  </a>
  TransitMaster installation (database) and convert to GTFS-realtime
  <sup>
   &#9733 1, pushed 940 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/ipublic/live_transit_event_trigger">
   Live Transit Event Trigger
  </a>
  - Extracts data from
  <a href="http://www.montgomerycountymd.gov/dot-transit/">
   Ride On's
  </a>
  OrbCAD database and export as GTFS-realtime.
  <sup>
   &#9733 3, pushed 1259 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/bdferris/onebusaway-sound-transit-realtime">
   SoundTransit to GTFS-realtime
  </a>
  - Convert text file feed from
  <a href="http://www.soundtransit.org/">
   Sound Transit
  </a>
  to GTFS-realtime
  <sup>
   &#9733 2, pushed 1665 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jestin/CivicTransit">
   Civic Transit
  </a>
  - Screen-scrapes
  <a href="http://www.kcata.org/">
   KCATA’s
  </a>
  TransitMaster WebWatch installation to produce a GTFS-realtime feed.
  <sup>
   &#9733 2, pushed 1191 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/OneBusAway/onebusaway-gtfs-realtime-munin-plugin">
   GTFS-realtime Munin Plugin
  </a>
  - Provides a
  <a href="http://munin-monitoring.org/">
   Munin
  </a>
  plugin for logging information about a GTFS-realtime feed.
  <sup>
   &#9733 1, pushed 1528 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/OneBusAway/onebusaway-gtfs-realtime-nagios-plugin">
   GTFS-realtime Nagio Plugin
  </a>
  - Provides a
  <a href="https://www.nagios.org/">
   Nagios
  </a>
  plugin for monitoring a GTFS-realtime feed
  <sup>
   &#9733 1, pushed 1526 days ago
  </sup>
 </li>
</ul>
<h3>
 SIRI
</h3>
<ul>
 <li>
  <a href="https://github.com/OneBusAway/onebusaway/wiki/SIRI-Resources">
   SIRI API
  </a>
  - Java classes generated from the v1.0 and v1.3
  <a href="http://user47094.vs.easily.co.uk/siri/">
   SIRI
  </a>
  schemas.
 </li>
 <li>
  <a href="https://github.com/laidig/siri-20-java">
   SIRI 2.0 API
  </a>
  - Java classes generated from the v2.0
  <a href="http://user47094.vs.easily.co.uk/siri/">
   SIRI
  </a>
  schemas.
  <sup>
   &#9733 0, pushed 213 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/OneBusAway/onebusaway-gtfs-realtime-from-siri-cli/wiki">
   SIRI to GTFS-realtime
  </a>
  - A Java-based command-line utility to convert from the
  <a href="http://user47094.vs.easily.co.uk/siri/">
   SIRI format
  </a>
  to GTFS-realtime.
 </li>
 <li>
  <a href="https://laidig.github.io/siri-20-java/doc/">
   SIRI 2.0 Autodoc
  </a>
  - Automatically generated documentation from the (incredibly well) annotated SIRI 2.0 Schema Definition.
 </li>
 <li>
  <a href="https://github.com/bdferris/onebusaway-king-county-metro/tree/master/onebusaway-king-county-metro-legacy-avl-to-siri">
   King County Metro Legacy AVL to SIRI
  </a>
  - Java-based tool to convert
  <a href="http://metro.kingcounty.gov/">
   King County Metro's
  </a>
  Legacy AVL format to GTFS-realtime.
 </li>
</ul>
<h2>
 License
</h2>
<p>
 <a href="http://creativecommons.org/publicdomain/zero/1.0/">
  <img alt="CC0" src="http://i.creativecommons.org/p/zero/1.0/88x31.png"/>
 </a>
</p>
<p>
 To the extent possible under law, Luqmaan Dawoodjee has waived all copyright and related or neighboring rights to this work.
</p>
