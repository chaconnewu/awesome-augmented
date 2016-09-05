<h1>
 Awesome Vert.x
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<p>
 <a href="http://vertx.io">
  <img align="right" src="logo-sm.png" width="250"/>
 </a>
</p>
<p>
 <em>
  Awesome Vert.x
 </em>
 is a list of awesome frameworks, libraries or other components for use with or that use
 <a href="https://github.com/eclipse/vert.x">
  Vert.x
 </a>
 version 3.
</p>
<p>
 If you want your component to appear here send a pull request to this repository to add it.
</p>
<p>
 Please note that we can't vouch for the stability or production-worthiness of everything on this list unless it has
the icon
 <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
  next to it. This icon means the component is part of the official
  <a href="http://vert-x3.github.io/docs/">
   Vert.x stack
  </a>
  .
 </img>
</p>
<p>
 For Vert.x version 2 check
 <a href="./vert-x2.md">
  this page
 </a>
 .
</p>
<h2>
 Contents
</h2>
<ul>
 <li>
  <a href="#web-frameworks">
   Web Frameworks
  </a>
 </li>
 <li>
  <a href="#authentication-authorisation">
   Authentication Authorisation
  </a>
 </li>
 <li>
  <a href="#database-clients">
   Database Clients
  </a>
 </li>
 <li>
  <a href="#integration">
   Integration
  </a>
 </li>
 <li>
  <a href="#middleware">
   Middleware
  </a>
 </li>
 <li>
  <a href="#language-support">
   Language Support
  </a>
 </li>
 <li>
  <a href="#reactive">
   Reactive
  </a>
 </li>
 <li>
  <a href="#sync-thread-non-block">
   Sync Thread Non Block
  </a>
 </li>
 <li>
  <a href="#vertx-event-bus-clients">
   Vert.x Event Bus Clients
  </a>
 </li>
 <li>
  <a href="#cluster-managers">
   Cluster Managers
  </a>
 </li>
 <li>
  <a href="#cloud-support">
   Cloud Support
  </a>
 </li>
 <li>
  <a href="#docker">
   Docker
  </a>
 </li>
 <li>
  <a href="#microservices">
   Microservices
  </a>
 </li>
 <li>
  <a href="#search-engines">
   Search Engines
  </a>
 </li>
 <li>
  <a href="#service-factory">
   Service Factory
  </a>
 </li>
 <li>
  <a href="#dependency-injection">
   Dependency Injection
  </a>
 </li>
 <li>
  <a href="#testing">
   Testing
  </a>
 </li>
 <li>
  <a href="#development-tools">
   Development Tools
  </a>
 </li>
 <li>
  <a href="#miscellaneous">
   Miscellaneous
  </a>
 </li>
 <li>
  <a href="#distribution">
   Distribution
  </a>
 </li>
 <li>
  <a href="#examples">
   Examples
  </a>
 </li>
 <li>
  <a href="#deployment">
   Deployment
  </a>
 </li>
 <li>
  <a href="#utilities">
   Utilities
  </a>
 </li>
</ul>
<h2>
 Web Frameworks
</h2>
<ul>
 <li>
  <a href="https://github.com/vert-x3/vertx-web">
   Vert.x Web
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
   - Full featured web toolkit for Vert.x.
  </img>
 </li>
 <li>
  <a href="https://github.com/englishtown/vertx-jersey">
   Vert.x Jersey
  </a>
  - Create JAX-RS
  <a href="https://jersey.java.net/">
   Jersey
  </a>
  resources in Vert.x.
 </li>
 <li>
  <a href="https://github.com/aesteve/vertx-nubes">
   Vert.x Nubes
  </a>
  - Provides an annotation layer on top of Vert.x Web.
 </li>
 <li>
  <a href="https://github.com/kohesive/kovert">
   Kovert
  </a>
  - Invisible REST framework for Kotlin + Vert.x Web.
 </li>
 <li>
  <a href="https://github.com/codesipcoffee/restvertx">
   RestVertx
  </a>
  - Easily build HTTP services in Vert.x using Java.
 </li>
 <li>
  <a href="https://github.com/spriet2000/vertx-handlers-http">
   Handlers
  </a>
  - Open web framework for Vert.x.
 </li>
 <li>
  <a href="https://github.com/advantageous/qbit">
   QBit
  </a>
  - REST and WebSocket method call marshaling and reactive library.
  <sup>
   &#9733 403, pushed 128 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/swisspush/vertx-rest-storage">
   vertx-rest-storage
  </a>
  - Persistence for REST resources in the filesystem or a redis database.
 </li>
 <li>
  <a href="https://github.com/isaiah/jubilee">
   Jubilee
  </a>
  - A rack compatible Ruby HTTP server built on Vert.x 3.
 </li>
 <li>
  <a href="https://github.com/katharsis-project/katharsis-vertx">
   katharsis-vertx
  </a>
  -
  <a href="http://jsonapi.org/">
   JSONAPI
  </a>
  implementation for Vert.x 3.
 </li>
</ul>
<h2>
 Authentication Authorisation
</h2>
<ul>
 <li>
  <a href="https://github.com/vert-x3/vertx-auth/tree/master/vertx-auth-jdbc">
   Vert.x Auth JDBC
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
   - Vert.x authentication/authorisation JDBC based.
  </img>
 </li>
 <li>
  <a href="https://github.com/vert-x3/vertx-auth/tree/master/vertx-auth-jwt">
   Vert.x Auth JWT
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
   - Vert.x Authorisation based on JSON Web Tokens.
  </img>
 </li>
 <li>
  <a href="https://github.com/vert-x3/vertx-auth/tree/master/vertx-auth-shiro">
   Vert.x Auth Shiro
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
   - Vert.x AuthN/AuthZ based on
   <a href="http://shiro.apache.org/">
    Apache Shiro
   </a>
   .
  </img>
 </li>
 <li>
  <a href="https://github.com/pac4j/vertx-pac4j">
   Vert.x-Pac4j
  </a>
  - Vert.x authentication/authorisation implemented using
  <a href="http://www.pac4j.org/">
   pac4j
  </a>
  .
 </li>
</ul>
<h2>
 Database Clients
</h2>
<p>
 <em>
  Clients for connecting to databases
 </em>
</p>
<ul>
 <li>
  <p>
   Relational Databases
  </p>
  <ul>
   <li>
    <a href="https://github.com/vert-x3/vertx-jdbc-client">
     JDBC
    </a>
    <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
     - Asynchronous interface around a JDBC datasource.
    </img>
   </li>
   <li>
    <a href="https://github.com/vert-x3/vertx-mysql-postgresql-client">
     MySQL
    </a>
    - Asynchronous client for MySQL.
   </li>
   <li>
    <a href="https://github.com/vert-x3/vertx-mysql-postgresql-client">
     PostgreSQL
    </a>
    - Asynchronous client for PostgreSQL.
   </li>
   <li>
    <a href="https://github.com/susom/database">
     database
    </a>
    - Client for Oracle, PostgreSQL, SQL Server, HyperSQL, etc. designed for security, correctness, and ease of use.
   </li>
  </ul>
 </li>
 <li>
  <p>
   NoSQL Databases
  </p>
  <ul>
   <li>
    <a href="https://github.com/vert-x3/vertx-mongo-client">
     MongoDB
    </a>
    <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
     - An asynchronous client for interacting with a MongoDB database.
    </img>
   </li>
   <li>
    <a href="https://github.com/vert-x3/vertx-redis-client">
     Redis
    </a>
    <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
     - Asynchronous API to interact with Redis.
    </img>
   </li>
   <li>
    <a href="https://github.com/englishtown/vertx-cassandra">
     Cassandra
    </a>
    - Asynchronous API to interact with Cassandra and Cassandra Mapping.
   </li>
   <li>
    <a href="https://github.com/cstamas/vertx-orientdb">
     OrientDB
    </a>
    - Non-blocking OrientDB server integration.
   </li>
   <li>
    <a href="https://github.com/etourdot/vertx-marklogic">
     MarkLogic
    </a>
    - Asynchronous client for Marklogic Database Server.
   </li>
  </ul>
 </li>
 <li>
  <p>
   <a href="https://github.com/BraintagsGmbH/vertx-pojo-mapper">
    vertx-pojo-mapper
   </a>
   - Non-blocking POJO mapping for MySQL and MongoDB.
  </p>
 </li>
</ul>
<h2>
 Integration
</h2>
<ul>
 <li>
  <p>
   Server-Sent Events
  </p>
  <ul>
   <li>
    <a href="https://github.com/mariomac/jeasse">
     jEaSSE
    </a>
    - Java Easy SSE. A simple, lightweight implementation of SSE.
   </li>
  </ul>
 </li>
 <li>
  <p>
   Mail
  </p>
  <ul>
   <li>
    <a href="https://github.com/vert-x3/vertx-mail-client">
     SMTP
    </a>
    <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
     - Async SMTP client.
    </img>
   </li>
   <li>
    <a href="https://github.com/cinterloper/vertx-smtp-server">
     vertx-smtp-server
    </a>
    - SMTP server bridging to EventBus.
   </li>
  </ul>
 </li>
 <li>
  <p>
   REST
  </p>
  <ul>
   <li>
    <a href="https://github.com/hubrick/vertx-rest-client">
     Vertx REST Client
    </a>
    - A REST client for vertx with support for RxJava and request caching.
   </li>
  </ul>
 </li>
 <li>
  <p>
   Messaging
  </p>
  <ul>
   <li>
    <a href="https://github.com/vert-x3/vertx-amqp-bridge">
     AMQP 1.0
    </a>
    <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
     - Interact with AMQP 1.0 servers using the Vert.x Producer and Consumer APIs.
    </img>
   </li>
   <li>
    <a href="https://github.com/vert-x3/vertx-rabbitmq-client">
     RabbitMQ
    </a>
    <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
     - A RabbitMQ client (AMQP 0.9.1).
    </img>
   </li>
   <li>
    <a href="https://github.com/cyngn/vertx-kafka">
     kafka
    </a>
    - Kafka client for consuming and producing messages.
   </li>
   <li>
    <a href="https://github.com/hubrick/vertx-kafka-service">
     Kafka Service
    </a>
    - Kafka producer and consumer with retry logic.
   </li>
   <li>
    <a href="https://github.com/cinterloper/vertx-salt">
     SaltStack
    </a>
    - A bi-directional bridge between the SaltStack event system and the Vert.x event bus.
   </li>
   <li>
    <a href="https://github.com/dano/vertx-zeromq">
     ZeroMQ
    </a>
    - ZeroMQ Event Bus bridge.
   </li>
   <li>
    <a href="https://github.com/GruppoFilippetti/vertx-mqtt-broker">
     MQTT Broker
    </a>
    - MQTT Broker (MQTT ver. 3.1.1 and 3.1 compliant).
   </li>
   <li>
    <a href="https://github.com/TextBack/vertx-azure-servicebus">
     Azure ServiceBus
    </a>
    - Azure
    <a href="https://azure.microsoft.com/en-us/services/service-bus/">
     ServiceBus
    </a>
    producer and consumer (fully async, doesn't use Microsoft Azure SDK).
   </li>
  </ul>
 </li>
 <li>
  <p>
   JavaEE
  </p>
  <ul>
   <li>
    <a href="https://github.com/vert-x3/vertx-jca">
     JCA adaptor
    </a>
    <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
     - Java Connector Architecture Adaptor for the Vert.x event bus.
    </img>
   </li>
   <li>
    <a href="https://github.com/weld/weld-vertx">
     Weld
    </a>
    - Brings the CDI programming model into the Vert.x ecosystem (register CDI observer methods as Vert.x message consumers, CDI-powered Verticles, define routes in a declarative way, etc.).
   </li>
  </ul>
 </li>
 <li>
  <p>
   Meteor
  </p>
  <ul>
   <li>
    <a href="https://github.com/jmusacchio/vertxbus/">
     Meteor
    </a>
    - Meteor integration support through Vert.x event bus.
   </li>
  </ul>
 </li>
 <li>
  <p>
   Metrics
  </p>
  <ul>
   <li>
    <a href="https://github.com/tsegismont/vertx-monitor">
     Hawkular metrics
    </a>
    -
    <a href="http://www.hawkular.org/">
     Hawkular
    </a>
    implementation of the Vert.x Metrics SPI.
   </li>
   <li>
    <a href="https://github.com/vert-x3/vertx-dropwizard-metrics">
     DropWizard metrics
    </a>
    <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
     - Metrics implementation using DropWizard metrics.
    </img>
   </li>
   <li>
    <a href="https://github.com/cyngn/vertx-opentsdb">
     OpenTsDb Metrics
    </a>
    -
    <a href="http://opentsdb.net/">
     OpenTsDb
    </a>
    metrics client for Vert.x.
   </li>
   <li>
    <a href="https://github.com/cyngn/vertx-bosun">
     Bosun Monitoring
    </a>
    -
    <a href="https://bosun.org/">
     Bosun
    </a>
    client library for Vert.x.
   </li>
  </ul>
 </li>
 <li>
  <p>
   Netflix - Hystrix
  </p>
  <ul>
   <li>
    <a href="https://github.com/kennedyoliveira/hystrix-vertx-metrics-stream.git">
     Hystrix Metrics Stream
    </a>
    - Emits metrics for Hystrix Dashboard from a Vertx application with
    <a href="https://github.com/Netflix/Hystrix">
     Hystrix
    </a>
    .
   </li>
  </ul>
 </li>
 <li>
  <p>
   Dart
  </p>
  <ul>
   <li>
    <a href="https://github.com/wem/vertx-dart-sockjs">
     Vert.x Dart SockJS
    </a>
    -
    <a href="https://www.dartlang.org/">
     Dart
    </a>
    integration for
    <a href="http://vertx.io/docs/vertx-web/java/#_sockjs_event_bus_bridge">
     Vert.x SockJS bridge
    </a>
    and plain SockJS with use of dart:js.
   </li>
  </ul>
 </li>
</ul>
<h2>
 Middleware
</h2>
<ul>
 <li>
  <a href="https://github.com/swisspush/gateleen">
   Gateleen
  </a>
  - Middleware library based on Vert.x to build advanced JSON/REST communication servers
 </li>
</ul>
<h2>
 Language Support
</h2>
<p>
 <em>
  Programming language support for Vert.x
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/vert-x3/vertx-lang-ceylon">
   Ceylon
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
   - Ceylon support.
  </img>
 </li>
 <li>
  <a href="https://github.com/vert-x3/vertx-lang-groovy">
   Groovy
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
   - Groovy support.
  </img>
 </li>
 <li>
  <a href="https://github.com/eclipse/vert.x">
   Java
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
   - Vert.x main repository (including the Java API).
  </img>
 </li>
 <li>
  <a href="https://github.com/vert-x3/vertx-lang-js">
   JavaScript
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
   - JavaScript support.
  </img>
 </li>
 <li>
  <a href="https://github.com/vert-x3/vertx-lang-python">
   Python
  </a>
  - Python support.
 </li>
 <li>
  <a href="https://github.com/vert-x3/vertx-lang-ruby">
   Ruby
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
   - Ruby support.
  </img>
 </li>
 <li>
  <a href="https://github.com/vert-x3/vertx-lang-scala">
   Scala
  </a>
  - Scala support.
 </li>
 <li>
  <a href="https://github.com/michel-kraemer/vertx-lang-typescript">
   TypeScript
  </a>
  - TypeScript support.
 </li>
 <li>
  <a href="https://github.com/cy6erGn0m/vertx3-lang-kotlin">
   Kotlin
  </a>
  - Kotlin support.
 </li>
</ul>
<p>
 <em>
  Language extensions
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/aesteve/grooveex">
   Grooveex
  </a>
  - Syntaxic sugar + utilities (DSL builders, etc.) on top of
  <a href="https://github.com/vert-x3/vertx-lang-groovy">
   vertx-lang-groovy
  </a>
  .
 </li>
</ul>
<h2>
 Reactive
</h2>
<ul>
 <li>
  <a href="https://github.com/vert-x3/vertx-reactive-streams">
   Reactive Streams
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
   - Vert.x Reactive Streams.
  </img>
 </li>
 <li>
  <a href="https://github.com/vert-x3/vertx-rx">
   Reactive Extensions
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
   - Vert.x Reactive Extensions.
  </img>
 </li>
 <li>
  <a href="https://github.com/cyngn/vertx-util">
   vertx-util
  </a>
  - Light weight promises & latches for Vert.x.
 </li>
 <li>
  <a href="https://github.com/advantageous/qbit">
   QBit
  </a>
  - Async typed actor-like lib that runs easily in Vert.x Async Callbacks. Callback management.
 </li>
</ul>
<h2>
 Sync Thread Non Block
</h2>
<ul>
 <li>
  <a href="https://github.com/vert-x3/vertx-sync">
   Sync
  </a>
  - Synchronous but non-OS-thread-blocking verticles.
 </li>
</ul>
<h2>
 Vert.x Event Bus Clients
</h2>
<p>
 <em>
  Clients to connect applications to the Vert.x event bus
 </em>
</p>
<ul>
 <li>
  <a href="https://www.npmjs.com/package/vertx3-eventbus-client">
   JavaScript
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
   - JavaScript event bus client.
  </img>
 </li>
 <li>
  <a href="https://github.com/julien3/vertxbuspp">
   C++11
  </a>
  - C++11 event bus client.
 </li>
 <li>
  <a href="https://github.com/saffron-technology/vertx-eventbusbridge">
   Java
  </a>
  - Java implementation of vertxbus.js.
 </li>
 <li>
  <a href="https://github.com/abdlquadri/vertx-eventbus-java">
   Java
  </a>
  - Java and Android Event Bus Client.
 </li>
 <li>
  <a href="https://github.com/cinterloper/vxc">
   CLI
  </a>
  - Command-line binary client for Vert.x event bus - pipe in JSON, emit JSON.
 </li>
</ul>
<h2>
 Cluster Managers
</h2>
<p>
 <em>
  Implementations of the Vert.x cluster manager SPI
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/vert-x3/vertx-hazelcast">
   Hazelcast Cluster Manager
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
   - Hazelcast cluster manager.
  </img>
 </li>
 <li>
  <a href="https://github.com/vert-x3/vertx-ignite">
   Ignite Cluster Manager
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
   - Ignite cluster manager.
  </img>
 </li>
 <li>
  <a href="https://github.com/vert-x3/vertx-jgroups">
   JGroups Cluster Manager
  </a>
  - JGroups cluster manager.
 </li>
 <li>
  <a href="https://github.com/stream1984/vertx-zookeeper">
   Zookeeper Cluster Manager
  </a>
  - Zookeeper cluster manager.
 </li>
 <li>
  <a href="https://github.com/atomix/atomix-vertx">
   Atomix Cluster Manager
  </a>
  - An
  <a href="http://atomix.io">
   Atomix
  </a>
  based cluster manager implementation for Vert.x 3.
 </li>
</ul>
<h2>
 Cloud Support
</h2>
<ul>
 <li>
  <a href="https://github.com/vert-x3/vertx-openshift-diy-quickstart">
   OpenShift DIY cartridge
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
   - OpenShift DIY Cartridge using Vert.x.
  </img>
 </li>
 <li>
  <a href="https://github.com/vert-x3/vertx-openshift-cartridge">
   OpenShift Vert.x cartridge
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
   - OpenShift Vert.x Cartridge using Vert.x.
  </img>
 </li>
</ul>
<h2>
 Docker
</h2>
<ul>
 <li>
  <a href="https://github.com/vert-x3/vertx-stack/tree/master/stack-docker">
   Docker images
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
   - Docker images for Vert.x.
  </img>
 </li>
</ul>
<h2>
 Microservices
</h2>
<ul>
 <li>
  <a href="https://github.com/vert-x3/vertx-service-discovery">
   Service Discovery
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Service Discovery">
   - Vert.x Service Discovery.
  </img>
 </li>
 <li>
  <a href="https://github.com/vert-x3/vertx-circuit-breaker">
   Circuit Breaker
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Circuit Breaker">
   - Vert.x Circuit Breaker.
  </img>
 </li>
 <li>
  <a href="https://github.com/vert-x3/vertx-service-discovery">
   Service Discovery - Consul
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Service Discovery - Consul">
   -
   <a href="https://www.consul.io/">
    Consul
   </a>
   extension to Vert.x Service Discovery.
  </img>
 </li>
 <li>
  <a href="https://github.com/vert-x3/vertx-service-discovery">
   Service Discovery - Docker links
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Service Discovery - Docker Links">
   -
   <a href="https://www.docker.com/">
    Docker
   </a>
   extension to Vert.x Service Discovery.
  </img>
 </li>
 <li>
  <a href="https://github.com/vert-x3/vertx-service-discovery">
   Service Discovery - Kubernetes
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Service Discovery - Kubernetes">
   -
   <a href="http://kubernetes.io/">
    Kubernetes
   </a>
   extension to Vert.x Service Discovery.
  </img>
 </li>
 <li>
  <a href="https://github.com/vert-x3/vertx-service-discovery">
   Service Discovery - Redis backend
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Service Discovery - Redis backend">
   -
   <a href="http://redis.io/">
    Redis
   </a>
   storage backend for Vert.x Service Discovery.
  </img>
 </li>
 <li>
  <a href="https://github.com/engagingspaces/vertx-graphql-service-discovery">
   Vert.x GraphQL Service Discovery
  </a>
  -
  <a href="http://graphql.org/">
   GraphQL
  </a>
  service discovery and querying for your Vert.x microservices.
 </li>
</ul>
<h2>
 Search Engines
</h2>
<ul>
 <li>
  <a href="https://github.com/englishtown/vertx-elasticsearch-service">
   Vert.x Elasticsearch Service
  </a>
  - Vert.x 3
  <a href="https://www.elastic.co/">
   Elasticsearch
  </a>
  service with event bus proxying.
 </li>
 <li>
  <a href="https://github.com/englishtown/vertx-solr-service">
   Vert.x Solr Service
  </a>
  - Vert.x 3 Solr service with event bus proxying.
 </li>
</ul>
<h2>
 Service Factory
</h2>
<ul>
 <li>
  <a href="https://github.com/vert-x3/vertx-service-factory">
   Service Factory
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
   - Vert.x Service Factory.
  </img>
 </li>
 <li>
  <a href="https://github.com/vert-x3/vertx-maven-service-factory">
   Maven Service Factory
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
   - Maven Vert.x Service Factory.
  </img>
 </li>
 <li>
  <a href="https://github.com/vert-x3/vertx-http-service-factory">
   HTTP Service Factory
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
   - Vert.x HTTP Service Factory.
  </img>
 </li>
 <li>
  <a href="https://github.com/mellster2012/vertx-nodejs-service-factory">
   Node.js Service Factory
  </a>
  - Vert.x Node.js Service Factory.
 </li>
 <li>
  <a href="https://github.com/cstamas/vertx-sisu">
   Eclipse SISU Service Factories
  </a>
  - Vert.x integration with
  <a href="https://www.eclipse.org/sisu/">
   Eclipse SISU
  </a>
  DI container offering alternatives for
  <code>
   vertx-service-factory
  </code>
  and
  <code>
   vertx-maven-service-factory
  </code>
  .
 </li>
</ul>
<h2>
 Dependency Injection
</h2>
<ul>
 <li>
  <a href="https://github.com/englishtown/vertx-guice">
   Vert.x Guice
  </a>
  - Vert.x verticle factory for Guice dependency injection.
 </li>
 <li>
  <a href="https://github.com/englishtown/vertx-hk2">
   Vert.x HK2
  </a>
  - Vert.x verticle factory for HK2 dependency injection.
 </li>
 <li>
  <a href="https://github.com/amoAHCP/spring-vertx-ext">
   Spring Vert.x Extension
  </a>
  - Vert.x verticle factory for Spring DI injection.
 </li>
 <li>
  <a href="https://github.com/rworsnop/vertx-beans">
   Vert.x Beans
  </a>
  - Inject Vert.x objects as beans into your Spring application.
 </li>
 <li>
  <a href="https://github.com/advantageous/qbit">
   QBit
  </a>
  - QBit works with Spring DI and Spring Boot (and of course Vertx). Allows you to use QBit, Vertx, Spring DI and Spring Boot in the same application.
 </li>
 <li>
  <a href="https://github.com/cstamas/vertx-sisu">
   Vert.x Eclipse SISU
  </a>
  - Vert.x integration with
  <a href="https://www.eclipse.org/sisu/">
   Eclipse SISU
  </a>
  DI container.
 </li>
</ul>
<h2>
 Testing
</h2>
<ul>
 <li>
  <a href="https://github.com/vert-x3/vertx-unit">
   Vert.x Unit
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
   - Async polyglot unit testing for Vert.x.
  </img>
 </li>
</ul>
<h2>
 Development Tools
</h2>
<ul>
 <li>
  <a href="https://github.com/dazraf/vertx-hot">
   Vert.x Hot
  </a>
  - A Maven plugin for the hot-deploy of Maven Vert.x projects.
 </li>
</ul>
<h2>
 Miscellaneous
</h2>
<ul>
 <li>
  <a href="https://github.com/vietj/vertx-childprocess">
   Vert.x Child Process
  </a>
  - Spawn child process from Vert.x.
 </li>
 <li>
  <a href="https://github.com/swisspush/vertx-redisques">
   vertx-redisques
  </a>
  - A highly scalable redis-persistent queuing system for Vert.x.
 </li>
</ul>
<h2>
 Distribution
</h2>
<ul>
 <li>
  <a href="https://github.com/vert-x3/vertx-stack">
   Vert.x Stack
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
   - Vert.x + the endorsed modules.
  </img>
 </li>
</ul>
<h2>
 Examples
</h2>
<ul>
 <li>
  <a href="https://github.com/vert-x3/vertx-examples">
   Vert.x examples
  </a>
  <img alt="(stack)" height="16px" src="https://rawgit.com/vert-x3/vertx-awesome/d93d327/vertx-favicon.svg" title="Vert.x Stack">
   - The official Vert.x examples including web examples, how to use the official database clients, etc.
  </img>
 </li>
 <li>
  <a href="https://github.com/aesteve/vertx-feeds">
   Vert.x feeds
  </a>
  - Example of an RSS aggregator built using Vert.x, Gradle, MongoDB, Redis, Handlebars templates, AngularJS, the event bus and SockJS.
 </li>
 <li>
  <a href="https://github.com/aesteve/vertx-markdown-service">
   Vert.x Markdown service
  </a>
  - Example on how to use
  <a href="https://github.com/vert-x3/vertx-service-proxy">
   service-proxy
  </a>
  with Gradle.
 </li>
 <li>
  <a href="https://github.com/advantageous/vertx-node-ec2-eventbus-example">
   Example using event bus and service proxies to connect vertx and node
  </a>
  - Step by step example with wiki description showing how to connect Vert.x and Node using event bus and service proxies.
 </li>
</ul>
<h2>
 Deployment
</h2>
<ul>
 <li>
  <a href="https://github.com/msoute/vertx-deploy-tools">
   Vert.x Deploy Application
  </a>
  - (Seamless) deploy to AWS based Vert.x application clusters.
 </li>
</ul>
<h2>
 Utilities
</h2>
<ul>
 <li>
  <a href="https://github.com/LisiLisenok/Chime">
   Chime
  </a>
  - Time scheduler working on Vert.x event bus allowing for scheduling with
  <em>
   cron-style
  </em>
  and
  <em>
   interval
  </em>
  timers.
 </li>
 <li>
  <a href="https://github.com/diabolicallabs/vertx-cron">
   Vert.x Cron
  </a>
  - Schedule events with cron specifications. Has event bus and Observable versions.
 </li>
 <li>
  <a href="https://github.com/aesteve/vertx-pojo-config">
   Vert.x POJO config
  </a>
  - Allows for mapping between standard JSON configuration and a (type-safe) configuration Java bean. Also allows the configuration bean to be validated through JSR 303.
 </li>
 <li>
  <a href="https://github.com/gchauvet/vertx-async">
   Vert.x Async
  </a>
  - Portage of caolan/async nodejs module to Vert.x framework that provides helpers methods for common async patterns.
 </li>
</ul>
<h2>
 Community
</h2>
<ul>
 <li>
  <a href="https://groups.google.com/forum/?fromgroups#!forum/vertx">
   User Group
  </a>
  - Discuss all user issues related to
  <em>
   using
  </em>
  Vert.x.
 </li>
 <li>
  <a href="https://groups.google.com/forum/?fromgroups#!forum/vertx-dev">
   Developer Group
  </a>
  - A group for Vert.x core
  <em>
   developers
  </em>
  and
  <em>
   contributors
  </em>
  .
 </li>
 <li>
  <a href="https://webchat.freenode.net/?channels=#vertx">
   IRC channel
  </a>
  - This is our day-to-day office: #vertx on freenode.net.
 </li>
 <li>
  <a href="https://github.com/vert-x3/issues/issues">
   Issues
  </a>
  - Vert.x core issue tracker.
 </li>
 <li>
  <a href="https://github.com/vert-x3/wiki/wiki">
   Wiki
  </a>
  - Contains useful information about Vert.x.
 </li>
 <li>
  <a href="http://vertx.io/materials/">
   Learning Materials
  </a>
  - A list of articles and presentations on Vert.x.
 </li>
 <li>
  <a href="http://vertx.io/blog/">
   Blog
  </a>
  - The official Vert.x blog containing many tutorials and other information.
 </li>
</ul>
<h2>
 Contribute
</h2>
<p>
 Contributions welcome! Read the
 <a href="CONTRIBUTING.md">
  contribution guidelines
 </a>
 first.
</p>
