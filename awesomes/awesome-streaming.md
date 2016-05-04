<h2>
 Awesome Streaming
</h2>
<p>
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</p>
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
  <sup>
   &#9733 112, pushed 2 days ago
  </sup>
  [Java] - unified platform for big data stream and batch processing.
 </li>
 <li>
  <a href="http://ci.apache.org/projects/flink/flink-docs-release-0.9/apis/streaming_guide.html">
   flink-streaming
  </a>
  [Java] - system for high-throughput, low-latency data stream processing that supports stateful computation, data-driven windowing semantics and iterative stream processing.
 </li>
 <li>
  <a href="https://github.com/intel-hadoop/gearpump">
   gearpump
  </a>
  [Scala] - lightweight real-time distributed streaming engine built on Akka.
 </li>
 <li>
  <a href="https://blog.twitter.com/2015/flying-faster-with-twitter-heron">
   heron
  </a>
  - Twitter's real-time analytics platform that is fully API-compatible with Storm. Storm has been replaced by Heron at Twitter.
 </li>
 <li>
  [Kafka Streams] [Java](https://cwiki.apache.org/confluence/display/KAFKA/KIP-28+-+Add+a+processor+client) - lightweight stream processing library included in Apache Kafka (since 0.10 version).
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
  <sup>
   &#9733 127, pushed 294 days ago
  </sup>
  [Scala/Java] - mapReduce-style framework for processing fast/streaming data.
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
  <a href="http://samza.apache.org/">
   Apache Samza
  </a>
  [Scala/Java] - distributed stream processing framework that build on Kafka(messaging, storage) and YARN(fault tolerance, processor isolation, security and resource management).
 </li>
 <li>
  <a href="https://spark.apache.org/streaming/">
   spark-streaming
  </a>
  [Scala] - makes it easy to build scalable fault-tolerant streaming applications.
 </li>
 <li>
  <a href="https://github.com/ottogroup/SPQR">
   SPQR
  </a>
  <sup>
   &#9733 20, pushed 92 days ago
  </sup>
  [Java] - dynamic framework for processing high volumn data streams through pipelines.
 </li>
 <li>
  <a href="https://storm.apache.org/">
   Apache Storm
  </a>
  [Clojure/Java] - distributed real-time computation system. Storm is to stream processing what Hadoop is to batch processing.
 </li>
 <li>
  <a href="https://github.com/caskdata/tigon">
   tigon
  </a>
  <sup>
   &#9733 221, pushed 214 days ago
  </sup>
  [C++/Java] - high throughput real-time streaming processing framework built on Hadoop and HBase.
 </li>
 <li>
  <a href="https://github.com/hailstorm-hs/hailstorm">
   hailstorm
  </a>
  <sup>
   &#9733 64, pushed 692 days ago
  </sup>
  [Haskell] - distributed stream processing with exactly-once semantics based on Storm.
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
  <sup>
   &#9733 1706, pushed 88 days ago
  </sup>
  [Scala] - library that lets you write MapReduce programs that look like native Scala or Java collection transformations and execute them on a number of well-known distributed MapReduce platforms, including Storm and Scalding.
 </li>
 <li>
  <a href="https://github.com/bkirwi/coast">
   coast
  </a>
  <sup>
   &#9733 46, pushed 79 days ago
  </sup>
  [Scala] - a DSL that builds DAGs on top of Samza and provides exactly-once semantics.
 </li>
 <li>
  <a href="https://github.com/apache/incubator-beam">
   Apache Beam
  </a>
  <sup>
   &#9733 151, pushed 1 days ago
  </sup>
  [Java] - unified model and set of language-specific SDKs for defining and executing data processing workflows, and also data ingestion and integration flows, supporting Enterprise Integration Patterns (EIPs) and Domain Specific Languages (DSLs), open sourced by Google.
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
  <sup>
   &#9733 3042, pushed 1 days ago
  </sup>
  [Scala/Java] - distributed, partitioned, replicated commit log service, which provides the functionality of a messaging system, but with a unique design.
 </li>
 <li>
  <a href="https://github.com/killme2008/Metamorphosis">
   metaq
  </a>
  <sup>
   &#9733 796, pushed 416 days ago
  </sup>
  [Java] - Taobao's high available, high performance distributed messaging system
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
  <sup>
   &#9733 642, pushed 147 days ago
  </sup>
  [Java] - Linkedin's Kafka -> HDFS pipeline.
 </li>
 <li>
  <a href="https://github.com/linkedin/databus">
   databus
  </a>
  <sup>
   &#9733 1009, pushed 4 days ago
  </sup>
  [Java] - Linkedin's source-agnostic distributed change data capture system.
 </li>
 <li>
  <a href="https://github.com/apache/flume">
   flume
  </a>
  <sup>
   &#9733 619, pushed 8 days ago
  </sup>
  [Java] - distributed, reliable, and available service for efficiently collecting, aggregating, and moving large amounts of log data.
 </li>
 <li>
  <a href="https://github.com/Netflix/suro">
   suro
  </a>
  <sup>
   &#9733 503, pushed 144 days ago
  </sup>
  [Java] - data pipeline service for collecting, aggregating, and dispatching large volume of application events including log data.
 </li>
 <li>
  <a href="https://github.com/streamsets/datacollector">
   StreamSets Data Collector
  </a>
  <sup>
   &#9733 98, pushed 1 days ago
  </sup>
  [Java] - continuous big data ingestion infrastructure that reads from and writes to a large number of end-points, including S3, JDBC, Hadoop, Kafka, Cassandra and many others.
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
  <sup>
   &#9733 106, pushed 91 days ago
  </sup>
  [Scala] - mining Big Data streams using Spark Streaming from Huawei.
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
  <sup>
   &#9733 406, pushed 37 days ago
  </sup>
  [Java] - distributed streaming machine learning (ML) framework that contains a programing abstraction for distributed streaming ML algorithms.
 </li>
 <li>
  <a href="https://github.com/pmerienne/trident-ml">
   trident-ml
  </a>
  <sup>
   &#9733 335, pushed 214 days ago
  </sup>
  [Java] - realtime online machine learning library based on Trident.
 </li>
 <li>
  <a href="https://github.com/sensorstorm/StormCV">
   StormCV
  </a>
  <sup>
   &#9733 48, pushed 220 days ago
  </sup>
  [Java] - enables the use of Apache Storm for video processing by adding computer vision (CV) specific operations and data model.
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
  <sup>
   &#9733 864, pushed 5 days ago
  </sup>
  [C] - An open-source relational database that runs SQL queries continuously on streams, incrementally storing results in tables.
 </li>
 <li>
  <a href="https://github.com/epfldata/squall">
   squall
  </a>
  <sup>
   &#9733 208, pushed 9 days ago
  </sup>
  [Java] - Squall executes SQL queries on top of Storm for doing online processing.
 </li>
 <li>
  <a href="https://github.com/HuaweiBigData/StreamCQL">
   StreamCQL
  </a>
  <sup>
   &#9733 209, pushed 54 days ago
  </sup>
  [Java] - Continuous Query Language on RealTime Computation System.
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
  <sup>
   &#9733 24, pushed 14 days ago
  </sup>
  [Java] - a set of benchmarks to test Storm performance.
 </li>
 <li>
  <a href="https://github.com/yahoo/storm-perf-test">
   storm-perf-test
  </a>
  <sup>
   &#9733 56, pushed 6 days ago
  </sup>
  [Java] - a simple storm performance/stress test.
 </li>
 <li>
  <a href="https://github.com/yahoo/streaming-benchmarks">
   streaming-benchmarks
  </a>
  <sup>
   &#9733 146, pushed 19 days ago
  </sup>
  [Java] - Benchmarks for Low Latency (Streaming) solutions including Apache Storm, Apache Spark, Apache Flink, etc.
 </li>
 <li>
  <a href="https://github.com/tylertreat/Flotilla">
   flotilla
  </a>
  <sup>
   &#9733 124, pushed 101 days ago
  </sup>
  [Go] - Automated message queue orchestration for scaled-up benchmarking.
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
  <sup>
   &#9733 1743, pushed 8 days ago
  </sup>
  [Java/C++] - efficient reliable unicast and multicast message transport.
 </li>
 <li>
  <a href="https://github.com/lmco/streamflow">
   StreamFlow
  </a>
  <sup>
   &#9733 182, pushed 132 days ago
  </sup>
  [Java] - stream processing tool designed to help build and monitor processing workflows.
 </li>
 <li>
  <a href="https://github.com/romseygeek/samza-luwak">
   samza-luwak
  </a>
  <sup>
   &#9733 67, pushed 540 days ago
  </sup>
  [Java] - uses Luwak, a stored-query engine built on Lucene, to implement full-text search on streams.
 </li>
 <li>
  <a href="https://github.com/Netflix/Turbine">
   Turbine
  </a>
  <sup>
   &#9733 395, pushed 104 days ago
  </sup>
  [Java] - tool for aggregating streams of Server-Sent Event (SSE) JSON data into a single stream.
 </li>
</ul>
<h3>
 Readings
</h3>
<h4>
 Blogs
</h4>
<ul>
 <li>
  <a href="http://blog.confluent.io/">
   Confluent blog
  </a>
 </li>
 <li>
  <a href="http://ingest.tips/">
   Ingest Tips
  </a>
 </li>
</ul>
<h4>
 Articles
</h4>
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
</ol>
<h4>
 Streaming Algorithms and their applications
</h4>
<p>
 from
 <a href="http://www.vldb.org/pvldb/vol8/p2040-Kejariwal.pdf">
  Real Time Analytics: Algorithms and Systems (VLDB 2015)
 </a>
</p>
<p>
 Problem | Description | Application
------- | ----------- | -----------
Sampling | Obtain a representative set of the stream | A/B Testing
Filtering | Extract elements which meet a certain criterion | Set membership
Correlation | Find data subsets (subgraphs) in (graph) data stream which are highly correlated to a given data set | Fraud detection
 <br/>
 Estimating Cardinality | Estimate the number of distinct elements | Site audience analysis
Estimating Quantiles | Estimate quantiles of a data stream with small amount of memory | Network analysis
Estimating Moments | Estimating distribution of frequencies of different elements | Databases
Finding Frequent Elements | Identify items in a multiset with frequency more than a threshold θ | Trending Hashtags
Counting Inversions | Estimate number of inversions | Measure sortedness
Finding Subsequences | Find Longest Increasing Subsequences (LIS), Longest Common Subsequence (LCS), subsequences similar to a given query sequence | Traffic analysis
Path Analysis | Determine whether there exists a path of length ≤
 <code>
  between two nodes in a dynamic graph | Web graph analysis
Anomaly Detection | Detect anomalies in a data stream | Sensor networks
Temporal Pattern Analysis | Detect patterns in a data stream | Traffic analysis
Data Prediction | Predict missing values in a data stream | Sensor data analysis
Clustering | Cluster a data stream | Medical imaging
Graph analysis | Extract unweighted and weighted matching, vertex cover, independent sets, spanners, subgraphs (sparsification) and random walks, computing min-cut | Web graph analysis
Basic Counting Estimate |
 </code>
 m'
 <code>
  of the number
 </code>
 m
 <code>
  of 1-bits in the sliding window (of size
 </code>
 n
 <code>
  ) such that
 </code>
 |m'  − m| ≤ em
 <code>
  | Popularity Analysis
Significant One Counting | Estimate
 </code>
 m'
 <code>
  of the number
 </code>
 m
 <code>
  of 1-bits in the sliding window (of size
 </code>
 n
 <code>
  ) such that if
 </code>
 m ≥ θn
 <code>
  , then
 </code>
 |m' − m| ≤ em` | Traffic accounting
</p>
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
