<h1>
 Awesome TinkerPop
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<p>
 <img alt="alt tag" src="https://raw.githubusercontent.com/mohataher/awesome-tinkerpop/master/tinkerpop-splash.png"/>
</p>
<p>
 A curated list of only awesome TinkerPop libraries on Github.
</p>
<blockquote>
 <p>
  Apache TinkerPop™ is a graph computing framework for both graph databases (OLTP) and graph analytic systems (OLAP).
 </p>
</blockquote>
<h3>
 Table of Contents
</h3>
<ul>
 <li>
  <a href="#tinkerpop3">
   TinkerPop3
  </a>
  <ul>
   <li>
    <a href="#tinkerpop3-implementations">
     Implementations
    </a>
   </li>
   <li>
    <a href="#wrappers">
     Wrappers/Clients
    </a>
   </li>
   <li>
    <a href="#qlang">
     Query Languages
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#tinkerpop2">
   TinkerPop2
  </a>
 </li>
 <li>
  <a href="#communites">
   Communites
  </a>
 </li>
 <li>
  <a href="#people-to-follow">
   People to Follow
  </a>
 </li>
 <li>
  <a href="#tutorials-and-resources">
   Tutorials and Resources
  </a>
 </li>
 <li>
  <a href="#contributing">
   How to Contribute
  </a>
 </li>
 <li>
  <a href="#license">
   License
  </a>
 </li>
</ul>
<h3>
 <a name="tinkerpop3">
 </a>
 TinkerPop3 Libraries
</h3>
<h4>
 <a name="tinkerpop3-implementations">
 </a>
 Implementations
</h4>
<ul>
 <li>
  <a href="https://github.com/apache/tinkerpop">
   TinkerPop3 implementation
  </a>
  - Mirror of Apache TinkerPop.
 </li>
 <li>
  <a href="https://github.com/pietermartin/sqlg">
   sqlg
  </a>
  - Sqlg is a implementation of TinkerPop3 on a RDBMS.
 </li>
 <li>
  <a href="https://github.com/blazegraph/database">
   blazegraph
  </a>
  - TinkerPop3
  <a href="https://github.com/blazegraph/tinkerpop3">
   implementation
  </a>
  for Blaze Graph; a high performance graph database.
 </li>
 <li>
  <a href="https://github.com/jbmusso/tinkergraph-js">
   tinkergraph-js
  </a>
  - A pure JavaScript implementation of TinkerPop's TinkerGraph in-memory graph database.
 </li>
 <li>
  <a href="https://github.com/jbmusso/gremlin-javascript">
   gremlin-javascript
  </a>
  - JavaScript graph database client for TinkerPop3 Gremlin Server.
 </li>
 <li>
  <a href="https://github.com/rmagen/elastic-gremlin">
   Elastic Gremlin
  </a>
  - TinkerPop3 implementation on Elasticsearch backend.
 </li>
 <li>
  <a href="http://tinkerpop.apache.org/docs/current/reference/#giraphgraphcomputer">
   Hadoop (Giraph)
  </a>
  - OLAP graph processor using Giraph.
 </li>
 <li>
  <a href="http://tinkerpop.apache.org/docs/current/reference/#sparkgraphcomputer">
   Hadoop (Spark)
  </a>
  - OLAP graph processor using Spark.
 </li>
 <li>
  <a href="https://console.ng.bluemix.net/catalog/services/ibm-graph/">
   IBM Graph
  </a>
  - OLTP graph database as a service.
 </li>
 <li>
  <a href="http://tinkerpop.apache.org/docs/currentg/#neo4j-gremlin">
   Neo4j
  </a>
  - OLTP graph database.
 </li>
 <li>
  <a href="http://stardog.com/">
   Stardog
  </a>
  - RDF graph database with OLTP and OLAP support.
 </li>
 <li>
  <a href="http://tinkerpop.apache.org/docs/current/reference/#tinkergraph-gremlin">
   TinkerGraph
  </a>
  - In-memory OLTP and OLAP reference implementation.
 </li>
 <li>
  <a href="http://thinkaurelius.github.io/titan/">
   Titan
  </a>
  - Distributed OLTP and OLAP graph database with BerkeleyDB, Cassandra and HBase support.
 </li>
 <li>
  <a href="https://github.com/awslabs/dynamodb-titan-storage-backend">
   Titan (Amazon)
  </a>
  - The Amazon DynamoDB storage backend for Titan.
  <sup>
   &#9733 181, pushed 140 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/classmethod/tupl-titan-storage-backend">
   Titan (Tupl)
  </a>
  - The Tupl storage backend for Titan.
 </li>
 <li>
  <a href="https://github.com/rmagen/unipop">
   Unipop
  </a>
  - OLTP Elasticsearch and JDBC backed graph.
 </li>
 <li>
  <a href="https://github.com/PureSolTechnologies/DuctileDB">
   DuctileDB
  </a>
  - Ductile DB is a graph database based on Hadoop/HBase which provides a vast set of features.
 </li>
</ul>
<h4>
 <a name="wrappers">
 </a>
 Wrappers/Clients
</h4>
<h5>
 C# .NET
</h5>
<ul>
 <li>
  <a href="https://www.nuget.org/packages/Teva.Common.Data.Gremlin/">
   Teva Gremlin
  </a>
  (.NET - C#) - A Gremlin Server driver for .NET.
 </li>
</ul>
<h5>
 Clojure
</h5>
<ul>
 <li>
  <a href="https://github.com/clojurewerkz/ogre">
   ogre
  </a>
  - Clojure library for querying TinkerPop graphs.
 </li>
 <li>
  <a href="https://github.com/viagraphs/scalajs-gremlin-client">
   scalajs-gremlin-client
  </a>
  (scala) - A Gremlin-Server client with ad-hoc extensible, reactive, typeclass based API.
 </li>
</ul>
<h5>
 Go
</h5>
<ul>
 <li>
  <a href="https://github.com/go-gremlin/gremlin">
   go-gremlin
  </a>
  - Go graph database client for TinkerPop3 Gremlin Server.
 </li>
 <li>
  <a href="https://github.com/qasaur/gremgo">
   Gremgo
  </a>
  - A fast, efficient, and easy-to-use Go client for the TinkerPop graph database stack.
 </li>
</ul>
<h5>
 Haskell
</h5>
<ul>
 <li>
  <a href="https://github.com/nakaji-dayo/gremlin-haskell">
   gremlin-haskell
  </a>
  - Haskell graph database client for TinkerPop3 Gremlin Server.
 </li>
</ul>
<h5>
 Java
</h5>
<ul>
 <li>
  <a href="http://tinkerpop.apache.org/docs/current/reference/#connecting-via-java">
   gremlin-driver
  </a>
  (java) - A Gremlin Server driver for Java.
 </li>
 <li>
  <a href="https://github.com/neo4j-contrib/neo4j-tinkerpop-api">
   neo4j-tinkerpop-api
  </a>
  - Apache Licensed Neo4j API for TinkerPop3.
 </li>
</ul>
<h5>
 Javascript
</h5>
<ul>
 <li>
  <a href="https://github.com/RedSeal-co/ts-tinkerpop">
   ts-tinkerpop
  </a>
  - Utilities for using TinkerPop3 via the node-java API in Typescript.
 </li>
 <li>
  <a href="https://github.com/jbmusso/gremlin-javascript">
   gremlin-javascript
  </a>
  (js) - A Gremlin Server driver for JavaScript.
 </li>
</ul>
<h5>
 PHP
</h5>
<ul>
 <li>
  <a href="https://github.com/PommeVerte/gremlin-php">
   gremlin-php
  </a>
  - gremlin-server php driver compatible with TinkerPop3. It will allow you to connect to gremlin-server and it's backends (Neo4J, Titan, etc.).
 </li>
</ul>
<h5>
 Python
</h5>
<ul>
 <li>
  <a href="https://github.com/platinummonkey/mogwai">
   Mogwai
  </a>
  - TinkerPop3 Graph Database Library for Python.
 </li>
 <li>
  <a href="https://github.com/windj007/python-gremlin-rest">
   python-gremlin-rest
  </a>
  - A REST-based client for Gremlin Server.
 </li>
 <li>
  <a href="https://github.com/davebshow/gremlinclient">
   gremlinclient
  </a>
  - An asynchronous Python 2/3 client for Gremlin Server that allows for flexible coroutine syntax - Trollius, Tornado, Asyncio.
 </li>
 <li>
  <a href="https://github.com/davebshow/aiogremlin">
   aiogremlin
  </a>
  (python) - A Python 3 library based on asyncio and aiohttp that uses websockets to communicate with the Gremlin Server.
 </li>
 <li>
  <a href="http://gremlinrestclient.readthedocs.org/en/latest/">
   gremlinrestclient
  </a>
  (python) - Python 2/3 library that uses HTTP to communicate with the Gremlin Server over REST.
 </li>
 <li>
  <a href="https://github.com/ZEROFAIL/goblin">
   goblin
  </a>
  - OGM for TinkerPop3 Gremlin Server.
 </li>
</ul>
<h5>
 Reactive
</h5>
<ul>
 <li>
  <a href="https://github.com/coreyauger/reactive-gremlin">
   reactive-gremlin
  </a>
  (scala) - An Akka HTTP Websocket Connector.
 </li>
</ul>
<h5>
 Scala
</h5>
<ul>
 <li>
  <a href="https://github.com/mpollmeier/gremlin-scala">
   Gremlin Scala
  </a>
  - Scala wrapper for Apache TinkerPop3 Graph DSL.
 </li>
</ul>
<h4>
 <a name="qlang">
 </a>
 Query Languages
</h4>
<ul>
 <li>
  <a href="https://github.com/emehrkay/gremlinpy">
   gremlin-py
  </a>
  - Write pure Python Gremlin that can be sent to Gremlin Server.
 </li>
 <li>
  <a href="https://github.com/mpollmeier/gremlin-scala">
   gremlin-scala
  </a>
  - A Scala language wrapper for TinkerPop3.
 </li>
 <li>
  <a href="https://github.com/jbmusso/gremlin-template-string">
   gremlin-template-string
  </a>
  - A Javascript Gremlin language builder.
 </li>
 <li>
  <a href="https://github.com/davebshow/ipython-gremlin">
   ipython-gremlin
  </a>
  - Gremlin in IPython and Jupyter.
 </li>
 <li>
  <a href="http://ogre.clojurewerkz.org/">
   ogre
  </a>
  - A Clojure language wrapper for TinkerPop3.
 </li>
 <li>
  <a href="https://github.com/bayofmany/peapod">
   Peapod
  </a>
  - A new object-graph-wrapper for the Tinkerpop3 graph stack.
 </li>
 <li>
  <a href="https://github.com/dkuppitz/sparql-gremlin">
   sparql-gremlin
  </a>
  - A SPARQL to Gremlin traversal compiler.
 </li>
 <li>
  <a href="https://github.com/twilmes/sql-gremlin">
   sql-gremlin
  </a>
  - A SQL to Gremlin traversal compiler.
 </li>
</ul>
<h3>
 <a name="tinkerpop2">
 </a>
 TinkerPop 2 Libraries
</h3>
<ul>
 <li>
  <a href="https://github.com/Syncleus/Ferma">
   Ferma
  </a>
  - An active reworking of TinkerPop frames.
 </li>
 <li>
  <a href="https://github.com/tinkerpop/frames">
   Frames
  </a>
  - An Object to Graph Framework.
 </li>
 <li>
  <a href="https://github.com/clojurewerkz/archimedes">
   Archimedes
  </a>
  - Clojure library for Blueprints (part of the TinkerPop graph stack).
 </li>
 <li>
  <a href="https://github.com/JHUAPL/AccumuloGraph">
   AccumuloGraph
  </a>
  - An implementation of TinkerPop Blueprints using Accumulo.
 </li>
 <li>
  <a href="https://github.com/Loupi/Frontenac">
   Frontenac
  </a>
  - A .NET port of the TinkerPop Stack.
 </li>
 <li>
  <a href="https://github.com/platinummonkey/mogwai">
   Mogwai
  </a>
  - TinkerPop 2 Graph Database Library for Python.
 </li>
 <li>
  <a href="https://github.com/gjrwebber/spring-data-gremlin">
   spring-data-gremlin
  </a>
  - Spring data gremlin makes it easier to implement Graph based repositories. This module extends Spring Data to allow support for potentially any Graph database that implements the TinkerPop Blueprints 2.x API.
 </li>
 <li>
  <a href="https://github.com/anvie/blueprints-scala">
   blueprints-scala
  </a>
  - TinkerPop Blueprints Scala.
 </li>
</ul>
<h2>
 <a name="communites">
 </a>
 Communities
</h2>
<ul>
 <li>
  <a href="https://groups.google.com/forum/#!forum/gremlin-users">
   Gremlin-users
  </a>
  - Mailing list for Gremlin users.
 </li>
 <li>
  <a href="http://stackoverflow.com/questions/tagged/tinkerpop3">
   Stack Overflow
  </a>
  - Stack Overflow has a relatively active community.
 </li>
 <li>
  <a href="http://mail-archives.apache.org/mod_mbox/incubator-tinkerpop-dev/">
   TinkerPop-dev
  </a>
  - Mailing list for TP3 deverlopers.
 </li>
</ul>
<h2>
 <a name="people-to-follow">
 </a>
 People to Follow
</h2>
<ul>
 <li>
  <a href="https://markorodriguez.com/">
   Marko Rodriguez
  </a>
  - Founder of TinkerPop and Aurelius.
 </li>
 <li>
  <a href="https://twitter.com/spmallette?lang=en-gb">
   Stephen Mallette
  </a>
  - Senior developer for Gremlin, TinkerPop and Titan DB.
 </li>
 <li>
  <a href="https://about.me/daniel.kuppitz">
   Daniel Kuppitz
  </a>
  - One of the main developers of Gremlin.
 </li>
 <li>
  <a href="https://github.com/pluradj">
   Jason Plurad
  </a>
  - Senior Developer at IBM. TinkerPop committer and active on the community.
 </li>
 <li>
  <a href="https://github.com/mohataher">
   Mohamed Taher Alrefaie
  </a>
  - Maintainer of this repository.
 </li>
</ul>
<h2>
 <a name="tutorials-and-resources">
 </a>
 Tutorials and Resources
</h2>
<ul>
 <li>
  <a href="http://tinkerpop.apache.org/gremlin.html">
   Introduction to Gremlin
  </a>
  - Official introduction to the Gremlin language.
 </li>
 <li>
  <a href="https://academy.datastax.com/resources/getting-started-tinkerpop-and-gremlin">
   Datastax Introduction
  </a>
  - A tutorial provided by Datastax to Gremlin and TinkerPop3.
 </li>
 <li>
  <a href="http://www.tinkerpopbook.com/">
   TinkerPop Book
  </a>
  - A long promised book for Tinkeprop but never fulfilled until now. You cans till request a notification.
 </li>
 <li>
  <a href="http://events.linuxfoundation.org/sites/events/files/slides/ApacheCon2015TinkerPop3.pdf">
   Linux Foundation Presentation
  </a>
  - A presentation by Linux Foundation given by David Robinson at IBM aboit Apache TinkerPop3.
 </li>
 <li>
  <a href="http://tinkerpop.apache.org/docs/current/tutorials/getting-started/">
   Getting Started with TinkerPop
  </a>
  - Learn the basics of getting up and going with TinkerPop.
 </li>
 <li>
  <a href="http://tinkerpop.apache.org/docs/current/tutorials/the-gremlin-console/">
   The Gremlin Console
  </a>
  - Discusses uses cases of the Gremlin Console and usage patterns.
 </li>
 <li>
  <a href="http://tinkerpop.apache.org/docs/3.2.1-SNAPSHOT/recipes/">
   Gremlin Recipes
  </a>
  - Reference for common traversal patterns and style.
 </li>
 <li>
  <a href="http://tinkerpop.apache.org/docs/3.2.1-SNAPSHOT/tutorials/gremlin-language-variants/">
   Gremlin Language Variants
  </a>
  - Learn how to embed Gremlin in a host programming language.
 </li>
 <li>
  <a href="http://sql2gremlin.com/">
   SQL2Gremlin
  </a>
  - Learn Gremlin using typical patterns found when querying data with SQL.
 </li>
 <li>
  <a href="https://academy.datastax.com/demos/getting-started-graph-databases">
   Getting Started with Graph Databases
  </a>
  - Compares relational databases to graph databases and SQL to Gremlin.
 </li>
</ul>
<h2>
 <a name="contributing">
 </a>
 How to Contribute
</h2>
<p>
 Please follow the
 <a href="contributing.md">
  guideliness here
 </a>
 . Please, make sure your contribution and PR are awesome!
 <img alt="alt tag" src="awesome-tinkerpop.jpg"/>
</p>
<h2>
 <a name="license">
 </a>
 License
</h2>
<p>
 <a href="http://creativecommons.org/publicdomain/zero/1.0/">
  <img alt="CC0" src="https://licensebuttons.net/p/zero/1.0/88x31.png"/>
 </a>
</p>
<p>
 To the extent possible under law,
 <a href="https://github.com/mohataher">
  @mohataher
 </a>
 has waived all copyright and related or neighboring rights to this work.
</p>
