<h1>
 Awesome Neo4j
</h1>
<p>
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
 <a href="https://travis-ci.org/Neueda4j/awesome-neo4j">
  <img alt="Build Status" src="https://api.travis-ci.org/Neueda4j/awesome-neo4j.svg?branch=master"/>
 </a>
</p>
<p>
 A curated list of awesome
 <a href="http://neo4j.com/">
  Neo4j
 </a>
 resources.
 <br/>
 Inspired by the
 <code>
  awesome-*
 </code>
 trend on GitHub.
</p>
<p>
 The goal is to build a categorized community-driven collection of very well-known resources.
 <br/>
 Sharing, suggestions and contributions are always welcome!
</p>
<p>
 Thanks to all
 <a href="https://github.com/Neueda4j/awesome-neo4j/graphs/contributors">
  contributors
 </a>
 .
</p>
<p>
 Maintained by
 <a href="https://neueda4j.com/">
  Neueda4j
 </a>
 .
</p>
<h1>
 Table of Contents
</h1>
<ul>
 <li>
  <a href="#basics">
   Basics
  </a>
 </li>
 <li>
  <a href="#connectors">
   Connectors
  </a>
  <ul>
   <li>
    <a href="#bolt">
     Bolt
    </a>
   </li>
   <li>
    <a href="#rest-api">
     REST API
    </a>
    <ul>
     <li>
      <a href="#java">
       Java
      </a>
     </li>
     <li>
      <a href="#ruby">
       Ruby
      </a>
     </li>
     <li>
      <a href="#python">
       Python
      </a>
     </li>
     <li>
      <a href="#php">
       PHP
      </a>
     </li>
     <li>
      <a href="#other">
       Other
      </a>
     </li>
    </ul>
   </li>
  </ul>
 </li>
 <li>
  <a href="#cloud">
   Cloud
  </a>
 </li>
 <li>
  <a href="#packages">
   Packages
  </a>
 </li>
 <li>
  <a href="#docker">
   Docker
  </a>
 </li>
 <li>
  <a href="#full-text-search">
   Full-text search
  </a>
 </li>
 <li>
  <a href="#import">
   Import
  </a>
 </li>
 <li>
  <a href="#benchmarking">
   Benchmarking
  </a>
 </li>
 <li>
  <a href="#extensions">
   Extensions
  </a>
 </li>
 <li>
  <a href="#stored-procedures">
   Stored Procedures
  </a>
 </li>
 <li>
  <a href="#development">
   Development
  </a>
 </li>
 <li>
  <a href="#editors">
   Editors
  </a>
 </li>
 <li>
  <a href="#shell">
   Shell
  </a>
 </li>
 <li>
  <a href="#visualization">
   Visualization
  </a>
 </li>
 <li>
  <a href="#tools">
   Tools
  </a>
 </li>
 <li>
  <a href="#resources">
   Resources
  </a>
  <ul>
   <li>
    <a href="#learn">
     Learn
    </a>
   </li>
   <li>
    <a href="#certification">
     Certification
    </a>
   </li>
   <li>
    <a href="#bolt-1">
     Bolt
    </a>
   </li>
   <li>
    <a href="#books">
     Books
    </a>
   </li>
   <li>
    <a href="#miscellaneous">
     Miscellaneous
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#license">
   License
  </a>
 </li>
</ul>
<p>
 Created by
 <a href="https://github.com/ekalinin/github-markdown-toc.go">
  gh-md-toc
 </a>
</p>
<h1>
 Basics
</h1>
<ul>
 <li>
  <a href="http://neo4j.com/docs/stable/">
   Official documentation
  </a>
 </li>
 <li>
  <a href="http://neo4j.com/docs/stable/cypher-refcard/">
   Cypher Refcard
  </a>
 </li>
 <li>
  <a href="http://neo4j.com/developer/get-started/">
   Developer resources
  </a>
 </li>
 <li>
  <a href="http://graphgist.neo4j.com/">
   Gists
  </a>
  - With Neo4j GraphGists you can describe and model your domain in a simple text file and render it as a rich, interactive page in any browser. Perfect to document a specific domain, use-case, question or graph problem.
 </li>
 <li>
  <a href="https://github.com/neo4j-examples">
   Neo4j Examples
  </a>
  - Examples for Neo4j and Library Usage.
 </li>
 <li>
  <a href="http://alpha.neohq.net/">
   Alpha Release Channel
  </a>
  - This microsite contains links and resources for future product releases.
 </li>
</ul>
<h1>
 Connectors
</h1>
<h2>
 Bolt
</h2>
<ul>
 <li>
  <a href="https://github.com/neo4j/neo4j-java-driver">
   neo4j-java-driver
  </a>
  - [BETA] Java driver for Neo4j binary protocol.
  <sup>
   64 GitHub links in total 118 links, &#9733 33, pushed 8 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/neo4j/neo4j-python-driver">
   neo4j-python-driver
  </a>
  - [BETA] Python driver for Neo4j binary protocol.
  <sup>
   64 GitHub links in total 118 links, &#9733 28, pushed 11 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/neo4j/neo4j-javascript-driver">
   neo4j-javascript-driver
  </a>
  - [BETA] JavaScript driver for Neo4j binary protocol.
  <sup>
   64 GitHub links in total 118 links, &#9733 53, pushed 12 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/neo4j/neo4j-dotnet-driver">
   neo4j-dotnet-driver
  </a>
  - [BETA] .Net driver for Neo4j (Bolt).
  <sup>
   64 GitHub links in total 118 links, &#9733 9, pushed 12 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/graphaware/neo4j-bolt-php">
   neo4j-bolt-php
  </a>
  - [BETA] PHP driver for Neo4j binary protocol.
  <sup>
   64 GitHub links in total 118 links, &#9733 11, pushed 6 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/cleishm/libneo4j-client">
   libneo4j-client
  </a>
  - libneo4j-client is a client library written in C for Neo4j. It is not intended as a complete driver, but rather as a foundation on which basic tools and drivers for various languages may be built. libneo4j-client takes care of all the detail of establishing a session with a Neo4j server, sending statements for evaluation, and retrieving results.
  <sup>
   64 GitHub links in total 118 links, &#9733 9, pushed 5 days ago
  </sup>
 </li>
</ul>
<h2>
 REST API
</h2>
<h3>
 Java
</h3>
<ul>
 <li>
  <a href="https://github.com/neo4j/neo4j-ogm">
   neo4j-ogm
  </a>
  - Object-Graph Mapping Library for Neo4j.
  <sup>
   64 GitHub links in total 118 links, &#9733 72, pushed 7 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/spring-projects/spring-data-neo4j">
   spring-data-neo4j
  </a>
  - Provides support to increase developer productivity in Java when using the neo4j graph database.
  <sup>
   64 GitHub links in total 118 links, &#9733 409, pushed 19 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/neo4j-contrib/neo4j-jdbc">
   neo4j-jdbc
  </a>
  - Neo4j JDBC driver.
  <sup>
   64 GitHub links in total 118 links, &#9733 74, pushed 42 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Wolfgang-Schuetzelhofer/jcypher">
   jcypher
  </a>
  - Java access to Neo4J graph databases at multiple levels of abstraction.
  <sup>
   64 GitHub links in total 118 links, &#9733 29, pushed 4 days ago
  </sup>
 </li>
</ul>
<h3>
 Ruby
</h3>
<ul>
 <li>
  <a href="https://github.com/neo4jrb/neo4j">
   neo4jrb
  </a>
  - An active model wrapper for the Neo4j Graph Database for Ruby.
  <sup>
   64 GitHub links in total 118 links, &#9733 1031, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/maxdemarzi/neography">
   neography
  </a>
  - A thin Ruby wrapper to the Neo4j Rest API.
  <sup>
   64 GitHub links in total 118 links, &#9733 589, pushed 42 days ago
  </sup>
 </li>
</ul>
<h3>
 Python
</h3>
<ul>
 <li>
  <a href="https://github.com/nigelsmall/py2neo">
   py2neo
  </a>
  - Py2neo is a comprehensive toolkit for working with Neo4j from within Python applications or from the command line.
  <sup>
   64 GitHub links in total 118 links, &#9733 452, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/robinedwards/neomodel">
   neomodel
  </a>
  - An Object Graph Mapper (OGM) for the neo4j graph database, built on the awesome py2neo.
  <sup>
   64 GitHub links in total 118 links, &#9733 181, pushed 88 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/espeed/bulbs">
   BulbFlow
  </a>
  - A Python persistence framework for graph databases like Neo4j, OrientDB and Titan.
  <sup>
   64 GitHub links in total 118 links, &#9733 555, pushed 554 days ago
  </sup>
 </li>
</ul>
<h3>
 PHP
</h3>
<ul>
 <li>
  <a href="https://github.com/jadell/neo4jphp">
   neo4jphp
  </a>
  - PHP wrapper of the Neo4j REST interface.
  <sup>
   64 GitHub links in total 118 links, &#9733 513, pushed 52 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Vinelab/NeoEloquent">
   NeoEloquent
  </a>
  - A Neo4j ORM - Based on Eloquent.
  <sup>
   64 GitHub links in total 118 links, &#9733 193, pushed 12 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/graphaware/neo4j-php-client/tree/4.0">
   neo4j-php-client
  </a>
  - PHP Client for Neo4j leveraging the Http and Bolt protocols.
 </li>
 <li>
  <a href="https://github.com/spider/spider">
   Spider
  </a>
  - A simple, flexible, and beautiful graph-data abstraction for php.
  <sup>
   64 GitHub links in total 118 links, &#9733 18, pushed 23 days ago
  </sup>
 </li>
</ul>
<h3>
 Other
</h3>
<ul>
 <li>
  <a href="https://github.com/thingdom/node-neo4j">
   node-neo4j
  </a>
  - REST API client for Node.
  <sup>
   64 GitHub links in total 118 links, &#9733 804, pushed 20 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Readify/Neo4jClient">
   Neo4jClient
  </a>
  - .NET client binding.
  <sup>
   64 GitHub links in total 118 links, &#9733 161, pushed 7 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jmcvetta/neoism">
   neoism
  </a>
  - Client for Golang.
  <sup>
   64 GitHub links in total 118 links, &#9733 246, pushed 81 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/michaelklishin/neocons">
   neocons
  </a>
  - A feature rich idiomatic Clojure client for the REST API.
  <sup>
   64 GitHub links in total 118 links, &#9733 141, pushed 116 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/nicolewhite/RNeo4j">
   RNeo4j
  </a>
  - Driver for R.
  <sup>
   64 GitHub links in total 118 links, &#9733 141, pushed 27 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/AnormCypher/AnormCypher">
   AnormCypher
  </a>
  - Scala library based on Anorm in the Play Framework.
  <sup>
   64 GitHub links in total 118 links, &#9733 104, pushed 4 days ago
  </sup>
 </li>
</ul>
<h1>
 Cloud
</h1>
<ul>
 <li>
  <a href="http://www.graphenedb.com/">
   GrapheneDB
  </a>
  - The world's first fully managed
Neo4j graph database.
 </li>
 <li>
  <a href="https://www.graphstory.com/">
   GraphStory
  </a>
  - Neo4j enterprise cloud provider
 </li>
</ul>
<h1>
 Packages
</h1>
<ul>
 <li>
  <a href="http://debian.neo4j.org/">
   Debian Packages
  </a>
 </li>
 <li>
  <a href="http://yum.neo4j.org/">
   Yum Repo
  </a>
 </li>
</ul>
<h1>
 Docker
</h1>
<ul>
 <li>
  <a href="https://github.com/neo4j/docker-neo4j">
   docker-neo4j
  </a>
  - Docker Images for the Neo4j Graph Database.
  <sup>
   64 GitHub links in total 118 links, &#9733 45, pushed 6 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/ekino/docker-neo4j-cluster">
   docker-neo4j-cluster
  </a>
  - Up & Running Neo4j cluster in no time.
  <sup>
   64 GitHub links in total 118 links, &#9733 26, pushed 83 days ago
  </sup>
 </li>
</ul>
<h1>
 Full-text search
</h1>
<ul>
 <li>
  <a href="https://github.com/graphaware/neo4j-to-elasticsearch">
   GraphAware Neo4j Elasticsearch Integration
  </a>
  - GraphAware Framework Module for Integrating Neo4j with Elasticsearch.
  <sup>
   64 GitHub links in total 118 links, &#9733 38, pushed 18 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/graphaware/graph-aided-search">
   GraphAware Graph-Aided Search
  </a>
  - Elasticsearch plugin offering Neo4j integration for Personalized Search.
  <sup>
   64 GitHub links in total 118 links, &#9733 12, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/neo4j-contrib/neo4j-elasticsearch">
   neo4j-elasticsearch
  </a>
  - Neo4j ElasticSearch Integration.
  <sup>
   64 GitHub links in total 118 links, &#9733 40, pushed 33 days ago
  </sup>
 </li>
</ul>
<h1>
 Import
</h1>
<ul>
 <li>
  <a href="https://github.com/graphaware/neo4j-importer">
   GraphAware Neo4j Importer
  </a>
  - Java importer skeleton for complicated, business-logic-heavy high-performance Neo4j imports directly from SQL databases, CSV files, etc.
  <sup>
   64 GitHub links in total 118 links, &#9733 5, pushed 38 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/sarmbruster/neo4j-csv-firehose">
   neo4j-csv-firehose
  </a>
  - Enables Neo4j’s
  <code>
   LOAD CSV
  </code>
  Cypher command to load from other datasources as well.
  <sup>
   64 GitHub links in total 118 links, &#9733 6, pushed 165 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jexp/neo4j-rdbms-import">
   neo4j-rdbms-import
  </a>
  - An automatic importer for relational databases into Neo4j.
  <sup>
   64 GitHub links in total 118 links, &#9733 18, pushed 187 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/neo4j-contrib/neo4j_doc_manager">
   Doc manager for Neo4j
  </a>
  - The Neo4j Doc Manager takes MongoDB documents and makes it easy to query them for relationships by making them available in a Neo4j graph structure, following the format specified by Mongo Connector.
  <sup>
   64 GitHub links in total 118 links, &#9733 24, pushed 40 days ago
  </sup>
 </li>
</ul>
<h1>
 Benchmarking
</h1>
<ul>
 <li>
  <a href="https://github.com/moxious/neoprofiler">
   neoprofiler
  </a>
  - Neo4J database profiling utility.
  <sup>
   64 GitHub links in total 118 links, &#9733 20, pushed 510 days ago
  </sup>
 </li>
</ul>
<h1>
 Extensions
</h1>
<ul>
 <li>
  <a href="https://github.com/graphaware/neo4j-uuid">
   GraphAware Neo4j UUID
  </a>
  - GraphAware Runtime Module that assigns a UUID to all nodes in the graph transparently.
  <sup>
   64 GitHub links in total 118 links, &#9733 19, pushed 13 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/graphaware/neo4j-changefeed">
   GraphAware Neo4j ChangeFeed
  </a>
  - A GraphAware Framework Runtime Module allowing users to find out what were the latest changes performed on the graph.
  <sup>
   64 GitHub links in total 118 links, &#9733 10, pushed 38 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/graphaware/neo4j-timetree">
   GraphAware Neo4j TimeTree
  </a>
  - Java and REST APIs for working with time-representing tree in Neo4j.
  <sup>
   64 GitHub links in total 118 links, &#9733 77, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/graphaware/neo4j-reco">
   GraphAware Neo4j Recommendation Engine
  </a>
  - Neo4j-based recommendation engine module with real-time and pre-computed recommendations.
  <sup>
   64 GitHub links in total 118 links, &#9733 118, pushed 38 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/graphaware/neo4j-noderank">
   GraphAware Neo4j NodeRank
  </a>
  - GraphAware Timer-Driven Runtime Module that executes PageRank-like algorithm on the graph.
  <sup>
   64 GitHub links in total 118 links, &#9733 15, pushed 38 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/graphaware/neo4j-algorithms">
   GraphAware Neo4j Algorithms
  </a>
  - Custom graph algorithms for Neo4j with own Java and REST APIs.
  <sup>
   64 GitHub links in total 118 links, &#9733 26, pushed 38 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/graphaware/neo4j-warmup">
   GraphAware Neo4j Warmup
  </a>
  - Simple library that warms up Neo4j caches with a single REST call.
  <sup>
   64 GitHub links in total 118 links, &#9733 9, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/graphaware/neo4j-resttest">
   GraphAware Neo4j RestTest
  </a>
  - GraphAware RestTest is a simple library for testing code that talks to Neo4j running in standalone server mode.
  <sup>
   64 GitHub links in total 118 links, &#9733 4, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/graphaware/neo4j-expire">
   GraphAware Neo4j Expire
  </a>
  - GraphAware Expire is a simple library that automatically deletes nodes and relationships from the database when they've reached their expiration date or time-to-live (TTL).
  <sup>
   64 GitHub links in total 118 links, &#9733 7, pushed 38 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/neo4j-contrib/spatial">
   Spatial
  </a>
  - Neo4j Spatial is a library of utilities for Neo4j that faciliates the enabling of spatial operations on data.
  <sup>
   64 GitHub links in total 118 links, &#9733 436, pushed 8 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Graphify/graphify">
   Graphify
  </a>
  - Graphify is a Neo4j unmanaged extension used for document and text classification using graph-based hierarchical pattern recognition.
  <sup>
   64 GitHub links in total 118 links, &#9733 261, pushed 342 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jexp/neo4j-tx-participation">
   neo4j-tx-participation
  </a>
  - This is a Neo4j Server Extension to make Neo4j REST-API participate in transactions started by the transactional Cypher endpoint.
  <sup>
   64 GitHub links in total 118 links, &#9733 3, pushed 345 days ago
  </sup>
 </li>
</ul>
<h1>
 Stored Procedures
</h1>
<ul>
 <li>
  <a href="https://github.com/neo4j-contrib/neo4j-apoc-procedures">
   Apoc : Awesome Procedures on Cypher
  </a>
  - Collection of useful procedures for Neo4j 3.x
  <sup>
   64 GitHub links in total 118 links, &#9733 46, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/graphaware/neo4j-graphgen-procedure">
   Graphgen
  </a>
  - Neo4j procedure for generating test data easily with Cypher
  <sup>
   64 GitHub links in total 118 links, &#9733 3, pushed 1 days ago
  </sup>
 </li>
</ul>
<h1>
 Development
</h1>
<ul>
 <li>
  <a href="https://m2.neo4j.org/index.html">
   Maven repositories
  </a>
  - Neo4j Maven repositories (releases, snapshots).
 </li>
 <li>
  <a href="https://github.com/graphaware/neo4j-framework">
   GraphAware Neo4j Framework
  </a>
  - GraphAware Framework speeds up development with Neo4j by providing a platform for building useful generic as well as domain-specific functionality, analytical capabilities, (iterative) graph algorithms, etc.
  <sup>
   64 GitHub links in total 118 links, &#9733 104, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/neo4j-contrib/cypher-dsl">
   cypher-dsl
  </a>
  - A Java DSL for the Cypher Query Language and an optional Query DSL mode.
  <sup>
   64 GitHub links in total 118 links, &#9733 46, pushed 138 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/fbiville/liquigraph">
   Liquigraph
  </a>
  - Database migrations management tool, based on how Liquibase works.
  <sup>
   64 GitHub links in total 118 links, &#9733 26, pushed 6 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/tinkerpop/blueprints">
   blueprints
  </a>
  - Blueprints is a collection of interfaces, implementations, ouplementations, and test suites for the property graph data model. Blueprints is analogous to the JDBC, but for graph databases.
  <sup>
   64 GitHub links in total 118 links, &#9733 1196, pushed 91 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/structr/structr">
   structr
  </a>
  - Graph Application Platform based on Neo4j.
  <sup>
   64 GitHub links in total 118 links, &#9733 365, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/graphaware/reco4php">
   Reco4PHP
  </a>
  - Neo4j based Recommendation Engine Framework for PHP.
  <sup>
   64 GitHub links in total 118 links, &#9733 25, pushed 8 days ago
  </sup>
 </li>
</ul>
<h1>
 Editors
</h1>
<ul>
 <li>
  <a href="https://github.com/Neueda4j/jetbrains-plugin-cypher">
   jetbrains-plugin-cypher
  </a>
  - Cypher plugin for Jetbrains-family IDE's.
  <sup>
   64 GitHub links in total 118 links, &#9733 23, pushed 19 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/neo4j-contrib/cypher-vim-syntax">
   cypher-vim-syntax
  </a>
  - Very basic Vim syntax for Cypher.
  <sup>
   64 GitHub links in total 118 links, &#9733 12, pushed 791 days ago
  </sup>
 </li>
</ul>
<h1>
 Shell
</h1>
<ul>
 <li>
  <a href="https://github.com/nicolewhite/cycli">
   cycli
  </a>
  - A Command Line Interface for Cypher.
  <sup>
   64 GitHub links in total 118 links, &#9733 123, pushed 8 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jexp/neo4j-shell-tools">
   neo4j-shell-tools
  </a>
  - A bunch of import/export tools for the neo4j-shell.
  <sup>
   64 GitHub links in total 118 links, &#9733 138, pushed 19 days ago
  </sup>
 </li>
</ul>
<h1>
 Visualization
</h1>
<ul>
 <li>
  <a href="https://github.com/neo4j-contrib/neoclipse">
   neoclipse
  </a>
  - Neoclipse is a tool to view, edit and explore Neo4j databases.
  <sup>
   64 GitHub links in total 118 links, &#9733 153, pushed 587 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/gephi/gephi">
   Gephi
  </a>
  - Gephi is an award-winning open-source platform for visualizing and manipulating large graphs.
  <sup>
   64 GitHub links in total 118 links, &#9733 1434, pushed 29 days ago
  </sup>
 </li>
 <li>
  <a href="http://linkurio.us/">
   Linkurious
  </a>
  - Linkurious helps search and visualize your graph data through a simple web-based interface.
 </li>
</ul>
<h1>
 Tools
</h1>
<ul>
 <li>
  <a href="http://graphgen.graphaware.com">
   Graphgen
  </a>
  - Graph Generation engine based on the Cypher DSL.
 </li>
 <li>
  <a href="https://github.com/jexp/store-utils">
   store-utils
  </a>
  - Utilities to compact, copy, fix, analyse Neo4j stores.
  <sup>
   64 GitHub links in total 118 links, &#9733 32, pushed 32 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/cohesivestack/ineo">
   ineo
  </a>
  - A simple but useful Neo4j instance manager.
  <sup>
   64 GitHub links in total 118 links, &#9733 12, pushed 20 days ago
  </sup>
 </li>
</ul>
<h1>
 Resources
</h1>
<ul>
 <li>
  <a href="http://www.opencypher.org/">
   openCypher
  </a>
  - openCypher is an open source project to bring a new public implementation of the industry’s most widely adopted graph query language: Cypher.
 </li>
</ul>
<h2>
 Learn
</h2>
<ul>
 <li>
  <a href="http://neo4j.com/graphacademy/online-course/">
   Getting Started with Neo4j
  </a>
 </li>
 <li>
  <a href="http://neo4j.com/graphacademy/online-course-prod/">
   Neo4j in Production
  </a>
 </li>
 <li>
  <a href="https://github.com/jimwebber/neo4j-tutorial">
   Neo4j Koans
  </a>
  - A koan-style tutorial in Java for Neo4j.
  <sup>
   64 GitHub links in total 118 links, &#9733 271, pushed 404 days ago
  </sup>
 </li>
</ul>
<h2>
 Certification
</h2>
<ul>
 <li>
  <a href="http://neo4j.com/graphacademy/neo4j-certification/">
   Neo4j Certification
  </a>
  - Become a Neo4j-Certified Professional.
 </li>
</ul>
<h2>
 Bolt
</h2>
<ul>
 <li>
  <a href="http://neo4j.com/docs/3.0.0-SNAPSHOT/bolt.html">
   Neo4j Bolt Protocol, Version 1
  </a>
  - This section describes the Neo4j Data Protocol, version 1. It is written primarily for those implementing client drivers as well as those who want to understand the low-level communication details of such interactions.
 </li>
 <li>
  <a href="https://github.com/nigelsmall/bolt-howto">
   bolt-howto
  </a>
  - How to Build a Neo4j Bolt Protocol Driver.
  <sup>
   64 GitHub links in total 118 links, &#9733 22, pushed 242 days ago
  </sup>
 </li>
</ul>
<h2>
 Books
</h2>
<ul>
 <li>
  <a href="http://graphdatabases.com/">
   Graph Databases
  </a>
  - The Definitive Book on Graph Databases and Introduction to Neo4j.
 </li>
 <li>
  <a href="https://www.packtpub.com/big-data-and-business-intelligence/learning-neo4j-graph-databases">
   Learning Neo4j
  </a>
  - Run blazingly fast queries on complex graph datasets with the power of the Neo4j graph database.
 </li>
 <li>
  <a href="https://www.packtpub.com/big-data-and-business-intelligence/neo4j-high-performance/">
   Neo4j High Performance
  </a>
 </li>
 <li>
  <a href="http://www.amazon.com/Programmatic-Introduction-Neo4j-Jim-Webber/dp/0321902904">
   A Programmatic Introduction to Neo4j
  </a>
  - [NOT YET BEEN RELEASED]
 </li>
</ul>
<h2>
 Miscellaneous
</h2>
<ul>
 <li>
  <a href="https://trello.com/b/2zFtvDnV/public-idea-board">
   Neo4j's Idea board
  </a>
 </li>
 <li>
  <a href="http://neo4j.com/hardware-sizing-calculator/">
   Hardware Sizing Calculator
  </a>
 </li>
</ul>
<h1>
 License
</h1>
<p>
 <a href="http://creativecommons.org/publicdomain/zero/1.0/">
  <img alt="CC0" src="https://licensebuttons.net/p/zero/1.0/88x31.png"/>
 </a>
</p>
<p>
 To the extent possible under law,
 <a href="https://github.com/Neueda4j">
  Neueda4j
 </a>
 has waived all copyright and related or neighboring rights to this work.
</p>
