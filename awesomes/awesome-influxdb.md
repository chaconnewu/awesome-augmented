<h1>
 awesome-influxdb
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<p>
 A curated list of awesome projects, libraries, tools, etc. related to
 <a href="https://influxdata.com/">
  InfluxDB
 </a>
 .
This list focuses on libraries, tools, etc. supporting InfluxDB version 0.9 and up.
</p>
<p>
 Want to make this list better?
Take a look at our page on
 <a href="CONTRIBUTING.md">
  contributing
 </a>
 and then open a pull request!
</p>
<h2>
 Reference material
</h2>
<p>
 If you know of any particularly useful blog posts, talks, slides, etc. that belong in this list, please open a pull request!
</p>
<ul>
 <li>
  <a href="https://docs.influxdata.com/influxdb/v0.10/">
   Official documentation
  </a>
 </li>
 <li>
  <a href="http://www.refactorium.com/distributed_systems/InfluxDB-and-Jepsen-Chapter-II-Where-is-influxdb-on-the-cap-scale/">
   Jepsen and InfluxDB, Chapter II. Where is InfluxDB on the CAP scale?
  </a>
  - Technical writeup from Balint Pato on running Jepsen Tests against InfluxDB v0.10
 </li>
</ul>
<h2>
 Client libraries
</h2>
<h3>
 Official
</h3>
<ul>
 <li>
  <a href="https://github.com/influxdata/influxdb/tree/master/client">
   Go
  </a>
  - Go client for InfluxDB, contained as package within main InfluxDB repo
 </li>
 <li>
  <a href="https://github.com/influxdata/influxdb-java">
   Java
  </a>
  <sup>
   &#9733 146, pushed 4 days ago
  </sup>
  - Java client for InfluxDB
 </li>
 <li>
  <a href="https://github.com/influxdata/influxdb-php">
   PHP
  </a>
  <sup>
   &#9733 69, pushed 12 days ago
  </sup>
  - PHP client for InfluxDB
 </li>
 <li>
  <a href="https://github.com/influxdata/influxdb-python">
   Python
  </a>
  <sup>
   &#9733 324, pushed 8 days ago
  </sup>
  - Python client for InfluxDB
 </li>
 <li>
  <a href="https://github.com/influxdata/influxdb-ruby">
   Ruby
  </a>
  <sup>
   &#9733 167, pushed 9 days ago
  </sup>
  - Ruby client for InfluxDB
 </li>
</ul>
<h3>
 Unofficial
</h3>
<ul>
 <li>
  <a href="https://github.com/olauzon/capacitor">
   capacitor
  </a>
  <sup>
   &#9733 56, pushed 172 days ago
  </sup>
  - A Clojure client for InfluxDB
 </li>
 <li>
  <a href="https://github.com/mmaul/cl-influxdb">
   cl-influxdb
  </a>
  <sup>
   &#9733 10, pushed 230 days ago
  </sup>
  - Common Lisp interface to the Time Series Database InfluxDB
 </li>
 <li>
  <a href="https://github.com/gossiperl/erflux">
   erflux
  </a>
  <sup>
   &#9733 15, pushed 167 days ago
  </sup>
  - InfluxDB client for Erlang
 </li>
 <li>
  <a href="https://github.com/lexmag/fluxter">
   fluxter
  </a>
  <sup>
   &#9733 7, pushed 2 days ago
  </sup>
  - An InfluxDB writer for Elixir
 </li>
 <li>
  <a href="https://github.com/gobwas/influent">
   influent
  </a>
  <sup>
   &#9733 26, pushed 132 days ago
  </sup>
  - InfluxDB Javascript driver
 </li>
 <li>
  <a href="https://github.com/gobwas/influent.rs">
   influent.rs
  </a>
  <sup>
   &#9733 6, pushed 75 days ago
  </sup>
  - InfluxDB Rust driver
 </li>
 <li>
  <a href="https://github.com/johanvandenbroek/InfluxDB-Client-LabVIEW">
   InfluxDB-Client-LabVIEW
  </a>
  <sup>
   &#9733 0, pushed 242 days ago
  </sup>
  - LabVIEW client for InfluxDB
 </li>
 <li>
  <a href="https://github.com/maoe/influxdb-haskell">
   influxdb-haskell
  </a>
  <sup>
   &#9733 23, pushed 20 days ago
  </sup>
  - Haskell client library for InfluxDB
 </li>
 <li>
  <a href="https://github.com/nblumhardt/influxdb-lineprotocol">
   influxdb-lineprotocol
  </a>
  - A .NET library for efficiently sending points to InfluxDB
 </li>
 <li>
  <a href="https://github.com/ziyasal/InfluxDB.Net">
   InfluxDB.NET
  </a>
  <sup>
   &#9733 58, pushed 65 days ago
  </sup>
  - .NET client for InfluxDB
 </li>
 <li>
  <a href="https://github.com/corley/influxdb-php-sdk">
   InfluxDB PHP SDK
  </a>
  <sup>
   &#9733 61, pushed 22 days ago
  </sup>
  - UDP/IP or HTTP adapters for read and write data
 </li>
 <li>
  <a href="https://github.com/dleutnant/influxdbr">
   influxdbr
  </a>
  <sup>
   &#9733 11, pushed 28 days ago
  </sup>
  - R library for InfluxDB
 </li>
 <li>
  <a href="https://github.com/mneudert/instream">
   instream
  </a>
  <sup>
   &#9733 40, pushed 3 days ago
  </sup>
  - InfluxDB driver for Elixir
 </li>
 <li>
  <a href="https://github.com/node-influx/node-influx">
   node-influx
  </a>
  <sup>
   &#9733 258, pushed 3 days ago
  </sup>
  - InfluxDB Node.js Client
 </li>
 <li>
  <a href="https://github.com/mediocre/node-influx-udp">
   node-influx-udp
  </a>
  <sup>
   &#9733 13, pushed 174 days ago
  </sup>
  - Write to InfluxDB using its UDP interface
 </li>
 <li>
  <a href="https://github.com/paulgoldbaum/scala-influxdb-client">
   scala-influxdb-client
  </a>
  <sup>
   &#9733 21, pushed 40 days ago
  </sup>
  - Asynchronous InfluxDB client for Scala
 </li>
</ul>
<h2>
 Collecting data into InfluxDB
</h2>
<h3>
 Projects
</h3>
<h4>
 Dedicated
</h4>
<p>
 Tools whose primary or sole purpose is to feed data into InfluxDB.
</p>
<ul>
 <li>
  <a href="https://github.com/abrander/agento">
   agento
  </a>
  <sup>
   &#9733 7, pushed 28 days ago
  </sup>
  - Client/server collecting near realtime metrics from Linux hosts
 </li>
 <li>
  <a href="https://github.com/ccpgames/aggregateD">
   aggregateD
  </a>
  <sup>
   &#9733 8, pushed 6 days ago
  </sup>
  - A
  <a href="http://docs.datadoghq.com/guides/dogstatsd/">
   dogstatsD
  </a>
  inspired metrics and event aggregation daemon for InfluxDB
 </li>
 <li>
  <a href="https://github.com/att-innovate/charmander">
   Charmander
  </a>
  <sup>
   &#9733 35, pushed 48 days ago
  </sup>
  - Charmander is a lab environment for measuring and analyzing resource-scheduling algorithms
 </li>
 <li>
  <a href="https://github.com/poxet/Influx-Capacitor">
   Influx-Capacitor
  </a>
  <sup>
   &#9733 25, pushed 5 days ago
  </sup>
  - Influx-Capacitor collects metrics from windows machines using Performance Counters. Data is sent to influxDB to be viewable by grafana
 </li>
 <li>
  <a href="https://github.com/zensqlmonitor/influxdb-sqlserver">
   influxdb-sqlserver
  </a>
  <sup>
   &#9733 8, pushed 59 days ago
  </sup>
  - Collect Microsoft SQL Server metrics for reporting to InfluxDB and visualize them with Grafana
 </li>
 <li>
  <a href="https://github.com/paulstuart/influxsnmp">
   influxsnmp
  </a>
  <sup>
   &#9733 53, pushed 13 days ago
  </sup>
  - Poll network devices via SNMP and save the data in InfluxDB
 </li>
 <li>
  <a href="https://github.com/kpacha/mesos-influxdb-collector">
   mesos-influxdb-collector
  </a>
  <sup>
   &#9733 7, pushed 2 days ago
  </sup>
  - Lightweight
  <a href="https://mesos.apache.org/">
   mesos
  </a>
  stats collector for InfluxDB
 </li>
 <li>
  <a href="https://github.com/shirou/mqforward">
   mqforward
  </a>
  <sup>
   &#9733 16, pushed 75 days ago
  </sup>
  -
  <a href="http://mqtt.org/">
   MQTT
  </a>
  to influxdb forwarder
 </li>
 <li>
  <a href="https://github.com/grempe/nest_poller">
   nest_poller
  </a>
  <sup>
   &#9733 0, pushed 238 days ago
  </sup>
  - A simple hack to retrieve and publish some statistics about
  <a href="https://nest.com/">
   Nest
  </a>
  devices to an InfluxDB instance
 </li>
 <li>
  <a href="https://github.com/fss1/ntp_checker">
   ntp_checker
  </a>
  <sup>
   &#9733 1, pushed 8 days ago
  </sup>
  - compares internal NTP sources and warns if the offset between servers exceeds a definable (fraction of) seconds
 </li>
 <li>
  <a href="https://github.com/novaquark/sysinfo_influxdb">
   sysinfo_influxdb
  </a>
  <sup>
   &#9733 87, pushed 308 days ago
  </sup>
  - Collect and send system (linux) info to InfluxDB
 </li>
 <li>
  <a href="https://github.com/influxdata/telegraf">
   Telegraf
  </a>
  <sup>
   &#9733 1255, pushed 2 days ago
  </sup>
  - (Official) plugin-driven server agent for reporting metrics into InfluxDB
 </li>
 <li>
  <a href="https://github.com/timdorr/tesla-trip/blob/master/lib/tesla_stream_reader.rb">
   tesla-streamer
  </a>
  - Streams data from Tesla Model S to InfluxDB (
  <a href="https://github.com/timdorr/tesla-trip/blob/master/lib/tasks/tesla.rake#L12-L16">
   rake task
  </a>
  )
 </li>
</ul>
<h4>
 Non-dedicated
</h4>
<p>
 Tools that generate data that feed into multiple backends, InfluxDB included.
</p>
<ul>
 <li>
  <a href="https://github.com/google/cadvisor">
   cAdvisor
  </a>
  <sup>
   &#9733 3861, pushed 2 days ago
  </sup>
  - Analyzes resource usage and performance characteristics of running containers
 </li>
 <li>
  <a href="https://github.com/BBC-News/cloudwatch-sender">
   cloudwatch-sender
  </a>
  <sup>
   &#9733 36, pushed 204 days ago
  </sup>
  - Send metrics to InfluxDB/Graphite from
  <a href="https://aws.amazon.com/cloudwatch/">
   Amazon Cloudwatch
  </a>
 </li>
 <li>
  <a href="https://github.com/Xorlev/crankshaftd">
   crankshaftd
  </a>
  <sup>
   &#9733 3, pushed 70 days ago
  </sup>
  - Simple Go agent to ingest streaming data from
  <a href="https://github.com/Netflix/Turbine">
   Turbine
  </a>
  via SSE and push it into StatsD as a gauge or to InfluxDB
 </li>
 <li>
  <a href="https://github.com/gatling/gatling">
   gatling
  </a>
  <sup>
   &#9733 2375, pushed 7 days ago
  </sup>
  - Async Scala-Akka-Netty based Stress Tool
 </li>
 <li>
  <a href="https://github.com/nicolargo/glances">
   Glances
  </a>
  <sup>
   &#9733 4968, pushed 2 days ago
  </sup>
  - Glances an Eye on your system
 </li>
 <li>
  <a href="https://github.com/shawn-sterling/graphios">
   Graphios
  </a>
  <sup>
   &#9733 212, pushed 40 days ago
  </sup>
  - A program to send nagios perf data to graphite (carbon) / statsd / librato / influxDB
 </li>
 <li>
  <a href="https://github.com/kubernetes/heapster">
   heapster
  </a>
  <sup>
   &#9733 640, pushed 4 days ago
  </sup>
  - Monitor container resource usage of a
  <a href="http://kubernetes.io/">
   Kubernetes
  </a>
  cluster
 </li>
 <li>
  <a href="https://github.com/mozilla-services/heka">
   heka
  </a>
  <sup>
   &#9733 3045, pushed 4 days ago
  </sup>
  - General purpose data collection and processing tool
 </li>
 <li>
  <a href="https://github.com/precurse/internet_data_usage">
   internet
   <em>
    data
   </em>
   usage
  </a>
  <sup>
   &#9733 1, pushed 165 days ago
  </sup>
  - Python based application to pull data plan usage for different carriers such as Telus and Koodo
 </li>
 <li>
  <a href="https://github.com/jmxtrans/jmxtrans">
   jmxtrans
  </a>
  <sup>
   &#9733 896, pushed 2 days ago
  </sup>
  - Effectively the missing connector between speaking to a JVM via JMX on one end and whatever logging / monitoring / graphing package that you can dream up on the other end.
 </li>
 <li>
  <a href="https://github.com/pstadler/metrics.sh">
   metrics.sh
  </a>
  <sup>
   &#9733 25, pushed 70 days ago
  </sup>
  - Collect and forward metrics using portable shell scripts
 </li>
 <li>
  <a href="https://github.com/riemann/riemann">
   Riemann
  </a>
  <sup>
   &#9733 2818, pushed 13 days ago
  </sup>
  - A network event stream processing system, in Clojure
 </li>
 <li>
  <a href="https://github.com/etsy/statsd-jvm-profiler">
   statsd-jvm-profiler
  </a>
  <sup>
   &#9733 177, pushed 39 days ago
  </sup>
  - Simple JVM Profiler Using StatsD
 </li>
 <li>
  <a href="https://github.com/armon/statsite">
   statsite
  </a>
  <sup>
   &#9733 1295, pushed 10 days ago
  </sup>
  - C implementation of statsd
 </li>
</ul>
<h3>
 Libraries
</h3>
<p>
 Libraries to collect data and feed into InfluxDB.
</p>
<ul>
 <li>
  <a href="https://github.com/robey/crow-metrics">
   crow-metrics
  </a>
  <sup>
   &#9733 15, pushed 75 days ago
  </sup>
  - small metrics collector for node servers
 </li>
 <li>
  <a href="https://github.com/bitmazk/django-influxdb-metrics">
   django-influxdb-metrics
  </a>
  <sup>
   &#9733 27, pushed 9 days ago
  </sup>
  - A reusable Django app that sends metrics about your project to InfluxDB
 </li>
 <li>
  <a href="https://github.com/beberlei/metrics">
   metrics
  </a>
  <sup>
   &#9733 153, pushed 90 days ago
  </sup>
  - (PHP) Simple library that abstracts different metrics collectors. "I find this necessary to have a consistent and simple metrics (functional) API that doesn't cause vendor lock-in"
 </li>
 <li>
  <a href="https://github.com/fennm/pyVsphereInflux">
   pyVsphereInflux
  </a>
  <sup>
   &#9733 2, pushed 63 days ago
  </sup>
  - A library and supporting script for pulling data from
  <a href="https://www.vmware.com/products/vsphere">
   vSphere
  </a>
  and inserting it into InfluxDB
 </li>
 <li>
  <a href="https://github.com/arussellsaw/telemetry">
   telemetry
  </a>
  <sup>
   &#9733 73, pushed 325 days ago
  </sup>
  - metric reporting for Go applications
 </li>
</ul>
<h4>
 Hooks
</h4>
<p>
 Hooks for other logging libraries to output to InfluxDB.
</p>
<ul>
 <li>
  <a href="https://github.com/vrischmann/go-metrics-influxdb">
   go-metrics-influxdb
  </a>
  <sup>
   &#9733 11, pushed 24 days ago
  </sup>
  - A reporter for the
  <a href="https://github.com/rcrowley/go-metrics">
   go-metrics library
  </a>
  which will post the metrics to InfluxDB
 </li>
 <li>
  <a href="https://github.com/Abramovic/logrus_influxdb">
   logrus_influxdb
  </a>
  <sup>
   &#9733 5, pushed 4 days ago
  </sup>
  - InfluxDB Hook for
  <a href="https://github.com/Sirupsen/logrus">
   Logrus
  </a>
 </li>
</ul>
<h3>
 Plugins
</h3>
<p>
 Plugins to allow other standalone tools to send their data into InfluxDB.
</p>
<ul>
 <li>
  <a href="https://github.com/joker1007/embulk-output-influxdb">
   embulk-output-influxdb
  </a>
  <sup>
   &#9733 0, pushed 230 days ago
  </sup>
  - InfluxDB output plugin for
  <a href="https://github.com/embulk/embulk">
   Embulk
  </a>
 </li>
 <li>
  <a href="https://github.com/travelping/exometer_influxdb">
   exometer_influxdb
  </a>
  <sup>
   &#9733 12, pushed 32 days ago
  </sup>
  -
  <a href="https://github.com/Feuerlabs/exometer">
   Exometer
  </a>
  reporter for InfluxDB
 </li>
 <li>
  <a href="https://github.com/fangli/fluent-plugin-influxdb">
   fluent-plugin-influxdb
  </a>
  <sup>
   &#9733 59, pushed 3 days ago
  </sup>
  - A buffered output plugin for
  <a href="http://www.fluentd.org/">
   fluentd
  </a>
  and InfluxDB
 </li>
 <li>
  <a href="https://github.com/shaharke/influx-nagios-plugin">
   influx-nagios-plugin
  </a>
  <sup>
   &#9733 20, pushed 195 days ago
  </sup>
  -
  <a href="https://www.nagios.org/">
   Nagios
  </a>
  plugin for querying monitoring stats from InfluxDB
 </li>
 <li>
  <a href="https://github.com/mre/kafka-influxdb">
   kafka-influxdb
  </a>
  <sup>
   &#9733 67, pushed 50 days ago
  </sup>
  - A
  <a href="https://kafka.apache.org/">
   Kafka
  </a>
  consumer for InfluxDB written in Python
 </li>
 <li>
  <a href="https://github.com/logstash-plugins/logstash-output-influxdb">
   logstash-output-influxdb
  </a>
  <sup>
   &#9733 15, pushed 13 days ago
  </sup>
  - Community-maintained
  <a href="https://www.elastic.co/products/logstash">
   Logstash
  </a>
  plugin to output metrics to InfluxDB
 </li>
 <li>
  <a href="https://github.com/davidB/metrics-influxdb">
   metrics-influxdb
  </a>
  <sup>
   &#9733 129, pushed 21 days ago
  </sup>
  - A reporter for
  <a href="http://www.dropwizard.io/0.9.1/docs/">
   dropwizard
  </a>
  metrics which announces measurements to an InfluxDB server
 </li>
 <li>
  <a href="https://github.com/savoirfairelinux/mod-influxdb">
   mod-influxdb
  </a>
  <sup>
   &#9733 13, pushed 8 days ago
  </sup>
  -
  <a href="http://www.shinken-monitoring.org/">
   Shinken
  </a>
  module for exporting data to InfluxDB
 </li>
 <li>
  <a href="https://github.com/sensu-plugins/sensu-plugins-influxdb">
   sensu-plugins-influxdb
  </a>
  <sup>
   &#9733 3, pushed 7 days ago
  </sup>
  -
  <a href="https://sensuapp.org/">
   Sensu
  </a>
  InfluxDB Plugins
 </li>
 <li>
  <a href="https://github.com/bernd/statsd-influxdb-backend">
   statsd-influxdb-backend
  </a>
  <sup>
   &#9733 143, pushed 14 days ago
  </sup>
  - A naive InfluxDB backend for StatsD
 </li>
</ul>
<h3>
 Import tools
</h3>
<p>
 Tools to import a fixed set of data into InfluxDB.
</p>
<ul>
 <li>
  <a href="https://github.com/adejoux/nmon2influxdb">
   nmon2influxdb
  </a>
  <sup>
   &#9733 12, pushed 12 days ago
  </sup>
  - Import
  <a href="http://nmon.sourceforge.net/pmwiki.php">
   nmon
  </a>
  file into InfluxDB
 </li>
</ul>
<h3>
 Other tools
</h3>
<ul>
 <li>
  <a href="https://github.com/DominionCider/influx-08-shim">
   influx-08-shim
  </a>
  <sup>
   &#9733 0, pushed 98 days ago
  </sup>
  - A tiny proxy server shim to ease the InfluxDB 0.8->0.9 transition
 </li>
</ul>
<h2>
 Consuming data from InfluxDB
</h2>
<h3>
 Dashboards and visualization
</h3>
<ul>
 <li>
  <a href="https://influxdata.com/time-series-platform/chronograf/">
   Chronograf
  </a>
  - Official InfluxDB data visualization tool (closed source)
 </li>
 <li>
  <a href="https://github.com/facette/facette">
   facette
  </a>
  <sup>
   &#9733 811, pushed 27 days ago
  </sup>
  - Time series data visualization and graphing software
 </li>
 <li>
  <a href="https://github.com/vrecan/FluxDash">
   FluxDash
  </a>
  <sup>
   &#9733 5, pushed 34 days ago
  </sup>
  - Terminal based InfluxDB dashboard
 </li>
 <li>
  <a href="https://github.com/grafana/grafana">
   grafana
  </a>
  <sup>
   &#9733 9533, pushed 1 days ago
  </sup>
  - Gorgeous metric viz, dashboards & editors for Graphite, InfluxDB & OpenTSDB
 </li>
 <li>
  <a href="https://github.com/ostrost/ostent">
   ostent
  </a>
  <sup>
   &#9733 61, pushed 4 days ago
  </sup>
  - collects and displays system metrics and optionally relays to Graphite and/or InfluxDB
 </li>
</ul>
<h3>
 Other tools
</h3>
<ul>
 <li>
  <a href="https://github.com/amwelch-oss/hubot-influxdb-alerts">
   hubot-influxdb-alerts
  </a>
  <sup>
   &#9733 7, pushed 139 days ago
  </sup>
  - Create and manage alerts in your chatroom using
  <a href="https://hubot.github.com/">
   hubot
  </a>
  and influxdb
 </li>
 <li>
  <a href="https://github.com/joshrendek/influx-alert">
   influx-alert
  </a>
  <sup>
   &#9733 12, pushed 204 days ago
  </sup>
  - A tool to query InfluxDB and send alerts based on a YAML config
 </li>
 <li>
  <a href="https://github.com/nathanielc/morgoth">
   Morgoth
  </a>
  <sup>
   &#9733 101, pushed 47 days ago
  </sup>
  - Metric anomaly detection
 </li>
</ul>
<h2>
 Provisioning InfluxDB
</h2>
<p>
 Tools, libraries, etc. to help you get InfluxDB running without installing it by hand.
</p>
<ul>
 <li>
  <a href="https://github.com/bdangit/chef-influxdb">
   chef-influxdb
  </a>
  <sup>
   &#9733 40, pushed 1 days ago
  </sup>
  - Chef cookbook for InfluxDB
 </li>
 <li>
  <a href="https://github.com/n1tr0g/golja-influxdb">
   golja-influxdb
  </a>
  <sup>
   &#9733 8, pushed 8 days ago
  </sup>
  - Puppet module for InfluxDB
 </li>
 <li>
  <a href="https://github.com/saltstack-formulas/influxdb-formula">
   influxdb-formula
  </a>
  <sup>
   &#9733 3, pushed 375 days ago
  </sup>
  - Installs and configures the InfluxDB timeseries database
 </li>
 <li>
  <a href="https://github.com/pivotal-cf-experimental/influxdb-release">
   influxdb-release
  </a>
  <sup>
   &#9733 1, pushed 35 days ago
  </sup>
  - Experimental BOSH release for InfluxDB
 </li>
 <li>
  <a href="https://github.com/palkan-ansible/influxdb">
   palkan-ansible/influxdb
  </a>
  <sup>
   &#9733 4, pushed 32 days ago
  </sup>
  - Installs InfluxDB 0.9.X on Ansible
 </li>
 <li>
  <a href="https://github.com/tutumcloud/influxdb">
   tutum-docker-influxdb
  </a>
  <sup>
   &#9733 183, pushed 22 days ago
  </sup>
  - Docker image to run an out-of-the-box InfluxDB server
 </li>
</ul>
<h2>
 Queries
</h2>
<ul>
 <li>
  <a href="https://github.com/corley/dbal-influxdb">
   dbal-influxdb
  </a>
  <sup>
   &#9733 9, pushed 307 days ago
  </sup>
  - Doctrine DBAL for InfluxDB
 </li>
 <li>
  <a href="https://github.com/undr/influxdb-arel">
   Influxdb::Arel
  </a>
  <sup>
   &#9733 7, pushed 413 days ago
  </sup>
  - Influxdb::Arel is a SQL AST manager for InfluxDB dialect. It simplifies the generation of complex SQL queries
 </li>
 <li>
  <a href="https://github.com/palkan/influxer">
   influxer
  </a>
  <sup>
   &#9733 31, pushed 6 days ago
  </sup>
  - InfluxDB ActiveRecord-style
 </li>
</ul>
<h2>
 Other awesome lists
</h2>
<h3>
 Awesome lists that include links to InfluxDB
</h3>
<ul>
 <li>
  <a href="https://github.com/onurakpolat/awesome-bigdata">
   awesome-bigdata
  </a>
  <sup>
   &#9733 3106, pushed 12 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/obazoud/awesome-dashboard">
   awesome-dashboard
  </a>
  <sup>
   &#9733 152, pushed 119 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/igorbarinov/awesome-data-engineering">
   awesome-data-engineering
  </a>
  <sup>
   &#9733 467, pushed 24 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/numetriclabz/awesome-db">
   awesome-db
  </a>
  <sup>
   &#9733 209, pushed 30 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/avelino/awesome-go">
   awesome-go
  </a>
  <sup>
   &#9733 12513, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/kahun/awesome-sysadmin">
   awesome-sysadmin
  </a>
  <sup>
   &#9733 12207, pushed 4 days ago
  </sup>
 </li>
</ul>
<h3>
 Lists of awesome lists that include awesome-influxdb
</h3>
<ul>
 <li>
  <a href="https://github.com/sindresorhus/awesome">
   awesome
  </a>
  <sup>
   &#9733 34522, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jnv/lists">
   lists
  </a>
  <sup>
   &#9733 3765, pushed 2 days ago
  </sup>
 </li>
</ul>
<h2>
 License
</h2>
<p>
 <a href="https://creativecommons.org/publicdomain/zero/1.0/">
  <img alt="CC0" src="https://licensebuttons.net/p/zero/1.0/88x31.png"/>
 </a>
</p>
<p>
 To the extent possible under law, the authors and contributors have waived all copyright and related or neighboring rights to awesome-influxdb.
</p>
