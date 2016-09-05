<h2>
 Awesome Streaming
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
 <a href="https://travis-ci.org/manuzhang/awesome-streaming">
  <img alt="Build Status" src="https://travis-ci.org/manuzhang/awesome-streaming.svg?branch=master"/>
 </a>
</h2>
<p>
 A curated list of awesome
 <a href="http://radar.oreilly.com/2015/08/the-world-beyond-batch-streaming-101.html">
  streaming (stream processing)
 </a>
 frameworks, applications, readings and other resources. Inspired by
 <a href="https://github.com/sindresorhus/awesome">
  other awesome projects
 </a>
 .
</p>
<h2>
 Table of Contents
</h2>
<ul>
 <li>
  <a href="#streaming-engine">
   Streaming Engine
  </a>
 </li>
 <li>
  <a href="#iot">
   IoT
  </a>
 </li>
 <li>
  <a href="#reactive-streams">
   Reactive Streams
  </a>
 </li>
 <li>
  <a href="#dsl">
   DSL
  </a>
 </li>
 <li>
  <a href="#data-pipeline">
   Data Pipeline
  </a>
 </li>
 <li>
  <a href="#online-machine-learning">
   Online Machine Learning
  </a>
 </li>
 <li>
  <a href="#stream-sql">
   Stream SQL
  </a>
 </li>
 <li>
  <a href="#toolkit">
   Toolkit
  </a>
 </li>
 <li>
  <a href="#benchmark">
   Benchmark
  </a>
 </li>
 <li>
  <a href="#readings">
   Readings
  </a>
 </li>
</ul>
<h3>
 Streaming Engine
</h3>
<ul>
 <li>
  <a href="https://github.com/apache/incubator-apex-core">
   Apache Apex
  </a>
  [Java] - unified platform for big data stream and batch processing.
  <sup>
   &#9733 112, pushed 127 days ago
  </sup>
 </li>
 <li>
  <a href="http://ci.apache.org/projects/flink/flink-docs-release-0.9/apis/streaming_guide.html">
   Apache Flink Streaming
  </a>
  [Java] - system for high-throughput, low-latency data stream processing that supports stateful computation, data-driven windowing semantics and iterative stream processing.
 </li>
 <li>
  <a href="https://github.com/intel-hadoop/gearpump">
   Apache Gearpump
  </a>
  [Scala] - lightweight real-time distributed streaming engine built on Akka.
 </li>
 <li>
  <a href="https://ignite.apache.org/features/streaming.html">
   Apache Ignite Streaming
  </a>
  [Java] - Ignite streaming allows to process continuous never-ending streams of data in scalable and fault-tolerant fashion.
 </li>
 <li>
  <a href="https://cwiki.apache.org/confluence/display/KAFKA/KIP-28+-+Add+a+processor+client">
   Apache Kafka Streams
  </a>
  [Java] - lightweight stream processing library included in Apache Kafka (since 0.10 version).
 </li>
 <li>
  <a href="http://samza.apache.org/">
   Apache Samza
  </a>
  [Scala/Java] - distributed stream processing framework that build on Kafka(messaging, storage) and YARN(fault tolerance, processor isolation, security and resource management).
 </li>
 <li>
  <a href="https://spark.apache.org/streaming/">
   Apache Spark Streaming
  </a>
  [Scala] - makes it easy to build scalable fault-tolerant streaming applications.
 </li>
 <li>
  <a href="https://storm.apache.org/">
   Apache Storm
  </a>
  [Clojure/Java] - distributed real-time computation system. Storm is to stream processing what Hadoop is to batch processing.
 </li>
 <li>
  <a href="http://heronstreaming.io/">
   heron
  </a>
  - Twitter's real-time analytics platform that is fully API-compatible with Storm. Storm has been replaced by Heron at Twitter.
 </li>
 <li>
  <a href="http://www.slideshare.net/g9yuayon/qcon-talk-on-netflix-mantis-a-stream-processing-system">
   mantis
  </a>
  - Netflix's event stream processing system.
 </li>
 <li>
  <a href="http://research.google.com/pubs/pub41378.html">
   millwheel
  </a>
  - framework for building low-latency data-processing applications that is widely used at Google.
 </li>
 <li>
  <a href="https://github.com/walmartlabs/mupd8">
   mupd8(muppet)
  </a>
  [Scala/Java] - mapReduce-style framework for processing fast/streaming data.
  <sup>
   &#9733 127, pushed 418 days ago
  </sup>
 </li>
 <li>
  <a href="http://gopulsar.io/">
   pulsar
  </a>
  [Java] - an open-source, real-time analytics platform and stream processing framework.
 </li>
 <li>
  <a href="http://incubator.apache.org/s4/">
   s4
  </a>
  [Java] - general-purpose, distributed, scalable, fault-tolerant, pluggable platform that allows programmers to easily develop applications for processing continuous unbounded streams of data.
 </li>
 <li>
  <a href="https://github.com/ottogroup/SPQR">
   SPQR
  </a>
  [Java] - dynamic framework for processing high volumn data streams through pipelines.
  <sup>
   &#9733 20, pushed 217 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/caskdata/tigon">
   tigon
  </a>
  [C++/Java] - high throughput real-time streaming processing framework built on Hadoop and HBase.
  <sup>
   &#9733 221, pushed 338 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/hailstorm-hs/hailstorm">
   hailstorm
  </a>
  [Haskell] - distributed stream processing with exactly-once semantics based on Storm.
  <sup>
   &#9733 64, pushed 817 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/edwardcapriolo/teknek-core">
   Teknek
  </a>
  [Java] - Simple elegant stream processing with interactive prototying shell SOL (Stream Operator Language)
 </li>
 <li>
  <a href="http://concord.io/">
   concord
  </a>
  [C++] - a distributed stream processing framework built in C++ on top of Apache Mesos, designed for high performance data processing jobs that require flexibility & control.
 </li>
</ul>
<h3>
 IoT
</h3>
<ul>
 <li>
  <a href="http://sensorbee.io/">
   sensorbee
  </a>
  [Go] - lightweight stream processing engine for IoT.
 </li>
 <li>
  <a href="http://quarks-edge.github.io/">
   quarks
  </a>
  [Java] - a programming model and runtime that enables continuous streaming analytics on gateways and edge devices which can work with centralized systems to provide efficient and timely analytics across the whole IoT ecosystem: from the center to the edge, opens sourced by IBM.
 </li>
</ul>
<h3>
 Reactive Streams
</h3>
<ul>
 <li>
  <a href="http://doc.akka.io/docs/akka-stream-and-http-experimental/1.0/scala/stream-cookbook.html">
   akka-streams
  </a>
  [scala] - an implementation of
  <a href="http://www.reactive-streams.org/">
   Reactive Streams
  </a>
  in Akka.
 </li>
 <li>
  <a href="https://github.com/monifu/monifu">
   monifu
  </a>
  [scala] - high-performance Scala / Scala.js library for composing asynchronous and event-based programs.
 </li>
</ul>
<h3>
 DSL
</h3>
<ul>
 <li>
  <a href="https://github.com/twitter/summingbird">
   summingbird
  </a>
  [Scala] - library that lets you write MapReduce programs that look like native Scala or Java collection transformations and execute them on a number of well-known distributed MapReduce platforms, including Storm and Scalding.
  <sup>
   &#9733 1706, pushed 212 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/bkirwi/coast">
   coast
  </a>
  [Scala] - a DSL that builds DAGs on top of Samza and provides exactly-once semantics.
  <sup>
   &#9733 46, pushed 204 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/apache/incubator-beam">
   Apache Beam
  </a>
  [Java] - unified model and set of language-specific SDKs for defining and executing data processing workflows, and also data ingestion and integration flows, supporting Enterprise Integration Patterns (EIPs) and Domain Specific Languages (DSLs), open sourced by Google.
  <sup>
   &#9733 151, pushed 125 days ago
  </sup>
 </li>
</ul>
<h3>
 Data Pipeline
</h3>
<ul>
 <li>
  <a href="https://github.com/apache/kafka">
   Apache Kafka
  </a>
  [Scala/Java] - distributed, partitioned, replicated commit log service, which provides the functionality of a messaging system, but with a unique design.
  <sup>
   &#9733 3042, pushed 125 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/killme2008/Metamorphosis">
   metaq
  </a>
  [Java] - Taobao's high available, high performance distributed messaging system
  <sup>
   &#9733 796, pushed 540 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/bitly/nsq">
   nsq
  </a>
  [Go] - realtime distributed messaging platform designed to operate at scale, handling billions of messages per day.
 </li>
 <li>
  <a href="https://github.com/linkedin/camus">
   camus
  </a>
  [Java] - Linkedin's Kafka -> HDFS pipeline.
  <sup>
   &#9733 642, pushed 271 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/linkedin/databus">
   databus
  </a>
  [Java] - Linkedin's source-agnostic distributed change data capture system.
  <sup>
   &#9733 1009, pushed 129 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/apache/flume">
   flume
  </a>
  [Java] - distributed, reliable, and available service for efficiently collecting, aggregating, and moving large amounts of log data.
  <sup>
   &#9733 619, pushed 133 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Netflix/suro">
   suro
  </a>
  [Java] - data pipeline service for collecting, aggregating, and dispatching large volume of application events including log data.
  <sup>
   &#9733 503, pushed 268 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/streamsets/datacollector">
   StreamSets Data Collector
  </a>
  [Java] - continuous big data ingestion infrastructure that reads from and writes to a large number of end-points, including S3, JDBC, Hadoop, Kafka, Cassandra and many others.
  <sup>
   &#9733 98, pushed 125 days ago
  </sup>
 </li>
</ul>
<h3>
 Online Machine Learning
</h3>
<ul>
 <li>
  <a href="https://github.com/huawei-noah/streamDM">
   streamDM
  </a>
  [Scala] - mining Big Data streams using Spark Streaming from Huawei.
  <sup>
   &#9733 106, pushed 215 days ago
  </sup>
 </li>
 <li>
  <a href="http://jubat.us/en/">
   jubatus
  </a>
  [C++] - distributed processing framework and streaming machine learning library.
 </li>
 <li>
  <a href="https://github.com/yahoo/samoa">
   Apache Samoa
  </a>
  [Java] - distributed streaming machine learning (ML) framework that contains a programing abstraction for distributed streaming ML algorithms.
  <sup>
   &#9733 406, pushed 161 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/pmerienne/trident-ml">
   trident-ml
  </a>
  [Java] - realtime online machine learning library based on Trident.
  <sup>
   &#9733 335, pushed 339 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/sensorstorm/StormCV">
   StormCV
  </a>
  [Java] - enables the use of Apache Storm for video processing by adding computer vision (CV) specific operations and data model.
  <sup>
   &#9733 48, pushed 345 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/DataSketches/sketches-core">
   DataSketches
  </a>
  [Java] - sketches library from Yahoo!.
 </li>
</ul>
<h3>
 Stream SQL
</h3>
<ul>
 <li>
  <a href="https://github.com/pipelinedb/pipelinedb">
   pipelinedb
  </a>
  [C] - An open-source relational database that runs SQL queries continuously on streams, incrementally storing results in tables.
  <sup>
   &#9733 864, pushed 130 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/epfldata/squall">
   squall
  </a>
  [Java] - Squall executes SQL queries on top of Storm for doing online processing.
  <sup>
   &#9733 208, pushed 134 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/HuaweiBigData/StreamCQL">
   StreamCQL
  </a>
  [Java] - Continuous Query Language on RealTime Computation System.
  <sup>
   &#9733 209, pushed 178 days ago
  </sup>
 </li>
</ul>
<h3>
 Benchmark
</h3>
<ul>
 <li>
  <a href="https://github.com/intel-hadoop/storm-benchmark">
   storm-benchmark
  </a>
  [Java] - a set of benchmarks to test Storm performance.
  <sup>
   &#9733 24, pushed 139 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/yahoo/storm-perf-test">
   storm-perf-test
  </a>
  [Java] - a simple storm performance/stress test.
  <sup>
   &#9733 56, pushed 131 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/yahoo/streaming-benchmarks">
   streaming-benchmarks
  </a>
  [Java] - Benchmarks for Low Latency (Streaming) solutions including Apache Storm, Apache Spark, Apache Flink, etc.
  <sup>
   &#9733 146, pushed 144 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/tylertreat/Flotilla">
   flotilla
  </a>
  [Go] - Automated message queue orchestration for scaled-up benchmarking.
  <sup>
   &#9733 124, pushed 226 days ago
  </sup>
 </li>
</ul>
<h3>
 Toolkit
</h3>
<ul>
 <li>
  <a href="http://akka.io/">
   akka
  </a>
  [Scala] - toolkit and runtime for building highly concurrent, distributed, and resilient message-driven application on the JVM.
 </li>
 <li>
  <a href="http://quantmind.github.io/pulsar/index.html#">
   pulsar
  </a>
  [Python] - Actor based event driven concurrent framework for Python.
 </li>
 <li>
  <a href="https://github.com/real-logic/Aeron">
   aeron
  </a>
  [Java/C++] - efficient reliable unicast and multicast message transport.
  <sup>
   &#9733 1743, pushed 132 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/lmco/streamflow">
   StreamFlow
  </a>
  [Java] - stream processing tool designed to help build and monitor processing workflows.
  <sup>
   &#9733 182, pushed 256 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/romseygeek/samza-luwak">
   samza-luwak
  </a>
  [Java] - uses Luwak, a stored-query engine built on Lucene, to implement full-text search on streams.
  <sup>
   &#9733 67, pushed 665 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Netflix/Turbine">
   Turbine
  </a>
  [Java] - tool for aggregating streams of Server-Sent Event (SSE) JSON data into a single stream.
  <sup>
   &#9733 395, pushed 229 days ago
  </sup>
 </li>
</ul>
<h3>
 Readings
</h3>
<ol>
 <li>
  <a href="https://highlyscalable.wordpress.com/2013/08/20/in-stream-big-data-processing/">
   In-Stream Big Data Processing
  </a>
 </li>
 <li>
  <a href="http://radar.oreilly.com/2015/08/the-world-beyond-batch-streaming-101.html">
   The world beyond batch: Streaming 101
  </a>
  by Tyler Akidau.
 </li>
 <li>
  <a href="http://www.vldb.org/pvldb/vol8/p2040-Kejariwal.pdf">
   Real Time Analytics: Algorithms and Systems (VLDB 2015)
  </a>
 </li>
</ol>
<h2>
 License
</h2>
<p>
 <img alt="Creative Commons License" src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png"/>
</p>
<p>
 Licensed under a
 <a href="http://creativecommons.org/licenses/by-sa/4.0/">
  Creative Commons Attribution-ShareAlike 4.0 International License
 </a>
</p>
