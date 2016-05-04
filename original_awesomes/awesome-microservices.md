<h1>
 Awesome Microservices
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<p>
 A curated list of Microservice Architecture related principles and technologies.
</p>
<p>
 <!-- START doctoc generated TOC please keep comment here to allow auto update -->
 <!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
 <strong>
  Table of Contents
 </strong>
</p>
<ul>
 <li>
  <a href="#platforms">
   Platforms
  </a>
 </li>
 <li>
  <a href="#runtimes">
   Runtimes
  </a>
 </li>
 <li>
  <a href="#service-toolkits">
   Service Toolkits
  </a>
  <ul>
   <li>
    <a href="#agnostic">
     Agnostic
    </a>
   </li>
   <li>
    <a href="#c">
     C
    </a>
   </li>
   <li>
    <a href="#c-1">
     C++
    </a>
   </li>
   <li>
    <a href="#d">
     D
    </a>
   </li>
   <li>
    <a href="#erlang-vm">
     Erlang VM
    </a>
   </li>
   <li>
    <a href="#go">
     Go
    </a>
   </li>
   <li>
    <a href="#haskell">
     Haskell
    </a>
   </li>
   <li>
    <a href="#java-vm">
     Java VM
    </a>
   </li>
   <li>
    <a href="#nodejs">
     Node.js
    </a>
   </li>
   <li>
    <a href="#perl">
     Perl
    </a>
   </li>
   <li>
    <a href="#php">
     PHP
    </a>
   </li>
   <li>
    <a href="#python">
     Python
    </a>
   </li>
   <li>
    <a href="#ruby">
     Ruby
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#capabilities">
   Capabilities
  </a>
  <ul>
   <li>
    <a href="#api-gateways--edge-services">
     API Gateways / Edge Services
    </a>
   </li>
   <li>
    <a href="#configuration-and-discovery">
     Configuration and Discovery
    </a>
   </li>
   <li>
    <a href="#security">
     Security
    </a>
   </li>
   <li>
    <a href="#elasticity">
     Elasticity
    </a>
   </li>
   <li>
    <a href="#messaging">
     Messaging
    </a>
   </li>
   <li>
    <a href="#serialization">
     Serialization
    </a>
   </li>
   <li>
    <a href="#storage">
     Storage
    </a>
   </li>
   <li>
    <a href="#reactivity">
     Reactivity
    </a>
   </li>
   <li>
    <a href="#resilience">
     Resilience
    </a>
   </li>
   <li>
    <a href="#testing">
     Testing
    </a>
   </li>
   <li>
    <a href="#monitoring-and-debugging">
     Monitoring and Debugging
    </a>
   </li>
   <li>
    <a href="#logging">
     Logging
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#it-automation--provisioning">
   IT Automation / Provisioning
  </a>
 </li>
 <li>
  <a href="#deployment-and-continuous-integration">
   Deployment and Continuous Integration
  </a>
  <ul>
   <li>
    <a href="#on-prem">
     On-prem
    </a>
   </li>
   <li>
    <a href="#hosted">
     Hosted
    </a>
   </li>
   <li>
    <a href="#lightweight">
     Lightweight
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#containers">
   Containers
  </a>
 </li>
 <li>
  <a href="#documentation--modeling">
   Documentation & Modeling
  </a>
  <ul>
   <li>
    <a href="#rest-apis">
     REST APIs
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#standards--recommendations">
   Standards / Recommendations
  </a>
  <ul>
   <li>
    <a href="#world-wide-web">
     World Wide Web
    </a>
   </li>
   <li>
    <a href="#http11">
     HTTP/1.1
    </a>
   </li>
   <li>
    <a href="#http2">
     HTTP/2
    </a>
   </li>
   <li>
    <a href="#coap">
     CoAP
    </a>
   </li>
   <li>
    <a href="#rpc">
     RPC
    </a>
   </li>
   <li>
    <a href="#messaging-1">
     Messaging
    </a>
   </li>
   <li>
    <a href="#security-1">
     Security
    </a>
   </li>
   <li>
    <a href="#service-discovery">
     Service Discovery
    </a>
   </li>
   <li>
    <a href="#data-formats">
     Data Formats
    </a>
   </li>
   <li>
    <a href="#vocabularies">
     Vocabularies
    </a>
   </li>
   <li>
    <a href="#unicode">
     Unicode
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#real-life-stories">
   Real Life Stories
  </a>
 </li>
 <li>
  <a href="#theory">
   Theory
  </a>
  <ul>
   <li>
    <a href="#articles--papers">
     Articles & Papers
    </a>
   </li>
   <li>
    <a href="#tutorials">
     Tutorials
    </a>
   </li>
   <li>
    <a href="#books">
     Books
    </a>
   </li>
   <li>
    <a href="#sites">
     Sites
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#emerging-technologies">
   Emerging Technologies
  </a>
 </li>
 <li>
  <a href="#license">
   License
  </a>
 </li>
 <li>
  <a href="#contributing">
   Contributing
  </a>
 </li>
 <li>
  <a href="#acknowledgments">
   Acknowledgments
  </a>
 </li>
</ul>
<p>
 <!-- END doctoc generated TOC please keep comment here to allow auto update -->
</p>
<h2>
 Platforms
</h2>
<ul>
 <li>
  <a href="https://github.com/CiscoCloud/microservices-infrastructure">
   Cisco Microservices
  </a>
  - Modern platform for rapidly deploying globally distributed services.
 </li>
 <li>
  <a href="https://github.com/cocaine">
   Cocaine
  </a>
  - A cloud platform enabling you to build your own PaaS clouds.
 </li>
 <li>
  <a href="http://deis.io/">
   Deis
  </a>
  - Open source application platform for public and private clouds.
 </li>
 <li>
  <a href="http://fabric8.io/">
   Fabric8
  </a>
  - Open source integration platform for deep management of Java Containers (JVMs).
 </li>
 <li>
  <a href="https://github.com/hailocab/h2">
   H2
  </a>
  - Hailo's microservices platform.
  <sup>
   108 GitHub links in total 406 links, &#9733 240, pushed 189 days ago
  </sup>
 </li>
 <li>
  <a href="https://hook.io/">
   Hook.io
  </a>
  - Open source hosting platform for microservices.
 </li>
 <li>
  <a href="http://lattice.cf/">
   Lattice
  </a>
  - Open source project for running containerized workloads on a cluster. Lattice bundles up http load-balancing, a cluster scheduler, log aggregation/streaming and health management into an easy-to-deploy and easy-to-use package.
 </li>
 <li>
  <a href="https://netflix.github.io/">
   Netflix OSS
  </a>
  - Netflix open source software ecosystem.
 </li>
 <li>
  <a href="https://github.com/spring-cloud/spring-cloud-netflix">
   Spring Cloud Netflix
  </a>
  - Provides Netflix OSS integrations for Spring Boot apps through autoconfiguration and binding to the Spring Environment and other Spring programming model idioms.
  <sup>
   108 GitHub links in total 406 links, &#9733 351, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="http://vamp.io/">
   VAMP
  </a>
  - Build, deploy and manage microservices with power and ease.
 </li>
</ul>
<h2>
 Runtimes
</h2>
<ul>
 <li>
  <a href="http://akka.io/">
   Akka
  </a>
  - Toolkit and runtime for building highly concurrent, distributed, and resilient message-driven applications on the JVM.
 </li>
 <li>
  <a href="http://baratine.io/">
   Baratine
  </a>
  - Platform for building a network of loosely-coupled POJO microservices.
 </li>
 <li>
  <a href="https://github.com/erlang/otp">
   Erlang/OTP
  </a>
  - Programming language used to build massively scalable soft real-time systems with requirements on high availability.
  <sup>
   108 GitHub links in total 406 links, &#9733 4467, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="http://twitter.github.io/finagle">
   Finagle
  </a>
  - Extensible RPC system for the JVM, used to construct high-concurrency servers.
 </li>
 <li>
  <a href="https://github.com/Netflix/karyon">
   Karyon
  </a>
  - The nucleus or the base container for applications and services built using the NetflixOSS ecosystem.
  <sup>
   108 GitHub links in total 406 links, &#9733 337, pushed 47 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/lagom/lagom">
   Lagom
  </a>
  - Reactive microservices for the JVM.
  <sup>
   108 GitHub links in total 406 links, &#9733 612, pushed 0 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/aol/micro-server">
   Microserver
  </a>
  - Java 8 native, zero configuration, standards based, battle hardened library to run Java REST microservices.
  <sup>
   108 GitHub links in total 406 links, &#9733 484, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="http://orbit.bioware.com/">
   Orbit
  </a>
  - Modern framework for JVM languages that makes it easier to build and maintain distributed and scalable online services.
 </li>
 <li>
  <a href="http://scalecube.io">
   Service Fabric I/O
  </a>
  - A microservices framework for the rapid development of distributed, resilient, reactive applications at scale.
 </li>
 <li>
  <a href="http://vertx.io/">
   Vert.X
  </a>
  - Toolkit for building reactive applications on the JVM.
 </li>
</ul>
<h2>
 Service Toolkits
</h2>
<h3>
 Agnostic
</h3>
<ul>
 <li>
  <a href="https://github.com/apex/apex">
   Apex
  </a>
  - Tool for deploying and managing AWS Lambda functions. With shims for languages not yet supported by Lambda, you can use Golang out of the box.
  <sup>
   108 GitHub links in total 406 links, &#9733 2443, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="http://coap.technology/impls.html">
   CoAP
  </a>
  - Constrained Application Protocol implementations.
 </li>
 <li>
  <a href="http://www.grpc.io/">
   GRPC
  </a>
  - A high performance, open source, general RPC framework that puts mobile and HTTP/2 first. Libraries in C, C++, Java, Go, Node.js, Python, Ruby, Objective-C, PHP and C#.
 </li>
</ul>
<h3>
 C
</h3>
<ul>
 <li>
  <a href="https://kore.io/">
   Kore
  </a>
  - Easy to use web application framework for writing scalable web APIs in C.
 </li>
 <li>
  <a href="https://github.com/wolkykim/libasyncd/">
   Libasyncd
  </a>
  - Embeddable event-based asynchronous HTTP server library for C.
 </li>
 <li>
  <a href="http://libslack.org/">
   Libslack
  </a>
  -  Provides a generic agent oriented programming model, run time selection of locking strategies, functions that make writing daemons trivial and simplify the implementation of network servers and clients, &c.
 </li>
 <li>
  <a href="http://lwan.ws/">
   Lwan
  </a>
  - High-performance and scalable web server.
 </li>
 <li>
  <a href="https://github.com/davidmoreno/onion">
   Onion
  </a>
  - C library to create simple HTTP servers and web applications.
  <sup>
   108 GitHub links in total 406 links, &#9733 1013, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Adaptv/ribs2">
   RIBS2
  </a>
  - Library which allows building high-performance internet serving systems.
  <sup>
   108 GitHub links in total 406 links, &#9733 89, pushed 439 days ago
  </sup>
 </li>
</ul>
<h3>
 C++
</h3>
<p>
 <!-- #c-1 anchor -->
</p>
<ul>
 <li>
  <a href="https://github.com/sgieseking/anyrpc">
   AnyRPC
  </a>
  - Provides a common system to work with a number of different remote procedure call standards, including: JSON-RPC, XML-RPC, MessagePack-RPC.
  <sup>
   108 GitHub links in total 406 links, &#9733 8, pushed 162 days ago
  </sup>
 </li>
 <li>
  <a href="https://capnproto.org/cxxrpc.html">
   Cap’n Proto RPC
  </a>
  - The Cap’n Proto C++ RPC implementation.
 </li>
 <li>
  <a href="http://cppmicroservices.org/">
   C++ Micro Services
  </a>
  - An OSGi-like C++ dynamic module system and service registry.
 </li>
 <li>
  <a href="https://github.com/endurox-dev/endurox/">
   Enduro/X
  </a>
  - XATMI based service framework for GNU/Linux.
 </li>
 <li>
  <a href="https://github.com/splunk/pion">
   Pion
  </a>
  - C++ framework for building lightweight HTTP interfaces.
  <sup>
   108 GitHub links in total 406 links, &#9733 203, pushed 32 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/oktal/pistache">
   Pistache
  </a>
  - A high-performance REST toolkit written in C++.
  <sup>
   108 GitHub links in total 406 links, &#9733 65, pushed 27 days ago
  </sup>
 </li>
 <li>
  <a href="http://pocoproject.org/">
   Poco
  </a>
  - C++ class libraries for building network-based applications and servers.
 </li>
 <li>
  <a href="https://github.com/datasift/served">
   Served
  </a>
  - C++ library for building high-performance RESTful web servers.
  <sup>
   108 GitHub links in total 406 links, &#9733 211, pushed 111 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/stefanocasazza/ULib">
   ULib
  </a>
  - Highly optimized class framework for writing C++ applications.
  <sup>
   108 GitHub links in total 406 links, &#9733 326, pushed 6 days ago
  </sup>
 </li>
</ul>
<h3>
 D
</h3>
<ul>
 <li>
  <a href="http://vibed.org/">
   Vibe.d
  </a>
  - Asynchronous I/O that doesn’t get in your way, written in D.
 </li>
</ul>
<h3>
 Erlang VM
</h3>
<h4>
 Elixir
</h4>
<ul>
 <li>
  <a href="http://www.phoenixframework.org/">
   Phoenix
  </a>
  - Framework for building HTML5 apps, API backends and distributed systems.
 </li>
 <li>
  <a href="https://github.com/elixir-lang/plug">
   Plug
  </a>
  - A specification and conveniences for composable modules between web applications.
  <sup>
   108 GitHub links in total 406 links, &#9733 819, pushed 2 days ago
  </sup>
 </li>
</ul>
<h4>
 Erlang
</h4>
<ul>
 <li>
  <a href="https://github.com/ninenines/cowboy">
   Cowboy
  </a>
  - Small, fast, modular HTTP server written in Erlang.
  <sup>
   108 GitHub links in total 406 links, &#9733 3131, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/videlalvaro/gen_microservice">
   Gen Microservice
  </a>
  - This library solves the problem of implementing microservices with Erlang.
  <sup>
   108 GitHub links in total 406 links, &#9733 64, pushed 356 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/mochi/mochiweb">
   Mochiweb
  </a>
  - Erlang library for building lightweight HTTP servers.
  <sup>
   108 GitHub links in total 406 links, &#9733 1367, pushed 6 days ago
  </sup>
 </li>
</ul>
<h3>
 Go
</h3>
<ul>
 <li>
  <a href="http://gin-gonic.github.io/gin/">
   Gin
  </a>
  - Web framework written in Golang.
 </li>
 <li>
  <a href="https://github.com/goadesign/goa">
   Goa
  </a>
  - Design-based HTTP microservices in Go.
  <sup>
   108 GitHub links in total 406 links, &#9733 738, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/gocraft/web">
   Gocraft
  </a>
  - A toolkit for building web apps. Includes routing, middleware stacks, logging and monitoring.
  <sup>
   108 GitHub links in total 406 links, &#9733 1042, pushed 124 days ago
  </sup>
 </li>
 <li>
  <a href="https://goji.io/">
   Goji
  </a>
  - Minimalistic and flexible request multiplexer for Go.
 </li>
 <li>
  <a href="https://github.com/go-kit/kit">
   Go kit
  </a>
  - Distributed programming toolkit for microservices in the modern enterprise.
  <sup>
   108 GitHub links in total 406 links, &#9733 3967, pushed 6 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.gorillatoolkit.org/">
   Gorilla
  </a>
  - Web toolkit for the Go programming language.
 </li>
 <li>
  <a href="https://github.com/koding/kite">
   Kite
  </a>
  - Microservices framework in Go.
  <sup>
   108 GitHub links in total 406 links, &#9733 1067, pushed 18 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/docker/libchan">
   Libchan
  </a>
  - Ultra-lightweight networking library which lets network services communicate in the same way that goroutines communicate using channels.
  <sup>
   108 GitHub links in total 406 links, &#9733 2011, pushed 148 days ago
  </sup>
 </li>
 <li>
  <a href="https://go-macaron.com/">
   Macaron
  </a>
  - Modular web framework in Go.
 </li>
 <li>
  <a href="https://github.com/micro/micro">
   Micro
  </a>
  - A microservices toolchain in Go.
  <sup>
   108 GitHub links in total 406 links, &#9733 1822, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/codegangsta/negroni">
   Negroni
  </a>
  - Idiomatic HTTP middleware for Golang.
  <sup>
   108 GitHub links in total 406 links, &#9733 3592, pushed 14 days ago
  </sup>
 </li>
</ul>
<h3>
 Haskell
</h3>
<ul>
 <li>
  <a href="https://github.com/scotty-web/scotty">
   Scotty
  </a>
  - Micro web framework inspired by Ruby's Sinatra, using WAI and Warp.
  <sup>
   108 GitHub links in total 406 links, &#9733 893, pushed 14 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/yesodweb/yesod">
   Yesod
  </a>
  - The Haskell RESTful web framework.
  <sup>
   108 GitHub links in total 406 links, &#9733 1458, pushed 1 days ago
  </sup>
 </li>
</ul>
<h3>
 Java VM
</h3>
<h4>
 Clojure
</h4>
<ul>
 <li>
  <a href="https://github.com/weavejester/compojure">
   Compojure
  </a>
  - A concise routing library for Ring/Clojure.
  <sup>
   108 GitHub links in total 406 links, &#9733 2883, pushed 57 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/weavejester/duct">
   Duct
  </a>
  - Minimal framework for building web applications in Clojure, with a strong emphasis on simplicity.
  <sup>
   108 GitHub links in total 406 links, &#9733 329, pushed 39 days ago
  </sup>
 </li>
 <li>
  <a href="http://clojure-liberator.github.io/liberator/">
   Liberator
  </a>
  - Library that helps you expose your data as resources while automatically complying with all the relevant requirements of the HTTP specification.
 </li>
 <li>
  <a href="https://modularity.org/">
   Modularity
  </a>
  - JUXT's Clojure-based modular system.
 </li>
 <li>
  <a href="https://github.com/danielsz/system">
   System
  </a>
  - Built on top of Stuart Sierra's component library, offers a set of readymade components.
  <sup>
   108 GitHub links in total 406 links, &#9733 350, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/otto-de/tesla-microservice">
   Tesla
  </a>
  - Common basis for some of Otto.de's Clojure microservices.
  <sup>
   108 GitHub links in total 406 links, &#9733 119, pushed 20 days ago
  </sup>
 </li>
</ul>
<h4>
 Java
</h4>
<ul>
 <li>
  <a href="https://github.com/airlift/airlift">
   Airlift
  </a>
  - Framework for building REST services in Java.
  <sup>
   108 GitHub links in total 406 links, &#9733 151, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://dropwizard.github.io/">
   Dropwizard
  </a>
  - Java framework for developing ops-friendly, high-performance, RESTful web services.
 </li>
 <li>
  <a href="https://jersey.java.net/">
   Jersey
  </a>
  - RESTful Web Services in Java. JAX-RS (JSR 311 & JSR 339) Reference Implementation.
 </li>
 <li>
  <a href="https://github.com/wso2/msf4j">
   MSF4J
  </a>
  - High throughput & low memory footprint Java microservices framework.
  <sup>
   108 GitHub links in total 406 links, &#9733 81, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/advantageous/qbit">
   QBit
  </a>
  - Reactive programming library for building microservices.
  <sup>
   108 GitHub links in total 406 links, &#9733 403, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="https://ratpack.io/">
   Ratpack
  </a>
  - Set of Java libraries that facilitate fast, efficient, evolvable and well tested HTTP applications. specific support for the Groovy language is provided.
 </li>
 <li>
  <a href="http://restlet.com/">
   Restlet
  </a>
  - Helps Java developers build web APIs that follow the REST architecture style.
 </li>
 <li>
  <a href="http://projects.spring.io/spring-boot/">
   Spring Boot
  </a>
  - Makes it easy to create stand-alone, production-grade Spring based applications.
 </li>
</ul>
<h4>
 Scala
</h4>
<ul>
 <li>
  <a href="http://doc.akka.io/docs/akka/current/scala/http">
   Akka HTTP
  </a>
  - Open source toolkit for building REST/HTTP-based integration layers on top of Scala and Akka (will replace Spray).
 </li>
 <li>
  <a href="https://github.com/tumblr/colossus">
   Colossus
  </a>
  - I/O and microservice library for Scala.
  <sup>
   108 GitHub links in total 406 links, &#9733 765, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="http://twitter.github.io/finatra/">
   Finatra
  </a>
  - Fast, testable, Scala HTTP services built on Twitter-Server and Finagle.
 </li>
 <li>
  <a href="https://www.playframework.com/">
   Play
  </a>
  - The high velocity web framework for Java and Scala.
 </li>
 <li>
  <a href="http://www.scalatra.org/">
   Scalatra
  </a>
  - Simple, accessible and free web micro-framework.
 </li>
 <li>
  <a href="https://github.com/skinny-framework/skinny-micro">
   Skinny Micro
  </a>
  - Micro-web framework to build servlet applications in Scala.
  <sup>
   108 GitHub links in total 406 links, &#9733 43, pushed 38 days ago
  </sup>
 </li>
 <li>
  <a href="http://spray.io/">
   Spray
  </a>
  - Open source toolkit for building REST/HTTP-based integration layers on top of Scala and Akka.
 </li>
</ul>
<h3>
 Node.js
</h3>
<ul>
 <li>
  <a href="http://www.actionherojs.com/">
   Actionhero
  </a>
  - Multi-transport Node.js API server with integrated cluster capabilities and delayed tasks.
 </li>
 <li>
  <a href="https://github.com/wprl/baucis">
   Baucis
  </a>
  - To build and maintain scalable HATEOAS/Level 3 REST APIs.
  <sup>
   108 GitHub links in total 406 links, &#9733 563, pushed 57 days ago
  </sup>
 </li>
 <li>
  <a href="http://expressjs.com/">
   Express
  </a>
  - Fast, unopinionated, minimalist web framework for Node.js
 </li>
 <li>
  <a href="https://github.com/GraftJS/graft">
   Graft
  </a>
  - Full-stack javascript through microservices.
  <sup>
   108 GitHub links in total 406 links, &#9733 202, pushed 276 days ago
  </sup>
 </li>
 <li>
  <a href="http://hapijs.com/">
   Hapi
  </a>
  - A rich framework for building applications and services.
 </li>
 <li>
  <a href="http://koajs.com/">
   Koa
  </a>
  - Next generation web framework for Node.js
 </li>
 <li>
  <a href="http://loopback.io/">
   Loopback
  </a>
  - Node.js framework for creating APIs and easily connecting to backend data sources.
 </li>
 <li>
  <a href="http://github.com/zeithq/micro">
   Micro
  </a>
  - Asynchronous HTTP microservices.
 </li>
 <li>
  <a href="https://github.com/czerwonkabartosz/Micro-Whalla">
   Micro-Whalla
  </a>
  - A simple, fast framework for writing microservices in Node.js communicate using RPC / IPC.
  <sup>
   108 GitHub links in total 406 links, &#9733 21, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="http://restify.com/">
   Restify
  </a>
  - Node.js module built specifically to enable you to build correct REST web services.
 </li>
 <li>
  <a href="http://senecajs.org/">
   Seneca
  </a>
  - A microservices toolkit for Node.js
 </li>
 <li>
  <a href="https://github.com/serverless/serverless">
   Serverless
  </a>
  - Build and maintain web, mobile and IoT applications running on AWS Lambda and API Gateway (formerly known as JAWS).
  <sup>
   108 GitHub links in total 406 links, &#9733 8016, pushed 2 days ago
  </sup>
 </li>
</ul>
<h3>
 Perl
</h3>
<ul>
 <li>
  <a href="http://mojolicio.us/">
   Mojolicious
  </a>
  - Next generation web framework for Perl.
 </li>
</ul>
<h3>
 PHP
</h3>
<ul>
 <li>
  <a href="https://api-platform.com/">
   API Platform
  </a>
  - API-first web framework on top of Symfony with JSON-LD, Schema.org and Hydra support.
 </li>
 <li>
  <a href="https://phalconphp.com/">
   Phalcon
  </a>
  - Full-stack PHP framework delivered as a C-extension.
 </li>
 <li>
  <a href="http://silex.sensiolabs.org/">
   Silex
  </a>
  - Micro-framework based on the Symfony components.
 </li>
</ul>
<h3>
 Python
</h3>
<ul>
 <li>
  <a href="http://flask.pocoo.org/">
   Flask
  </a>
  - Python framework for microservices based on Werkzeug and Jinja 2.
 </li>
 <li>
  <a href="https://github.com/onefinestay/nameko">
   Nameko
  </a>
  - Python framework for building microservices.
  <sup>
   108 GitHub links in total 406 links, &#9733 813, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.tornadoweb.org/">
   Tornado
  </a>
  - Web framework and asynchronous networking library.
 </li>
 <li>
  <a href="http://webpy.org/">
   web.py
  </a>
  - Minimalist web framework for Python.
 </li>
</ul>
<h3>
 Ruby
</h3>
<ul>
 <li>
  <a href="https://github.com/hanami">
   Hanami
  </a>
  - A modern web framework for Ruby.
 </li>
 <li>
  <a href="https://github.com/rightscale/praxis">
   Praxis
  </a>
  - Framework for both designing and implementing APIs.
  <sup>
   108 GitHub links in total 406 links, &#9733 240, pushed 49 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/wardrop/Scorched">
   Scorched
  </a>
  - Light-weight web framework for Ruby.
  <sup>
   108 GitHub links in total 406 links, &#9733 220, pushed 71 days ago
  </sup>
 </li>
</ul>
<h2>
 Capabilities
</h2>
<h3>
 API Gateways / Edge Services
</h3>
<ul>
 <li>
  <a href="http://camel.apache.org/">
   Camel
  </a>
  - Empowers you to define routing and mediation rules in a variety of domain-specific languages, including a Java-based fluent API, Spring or Blueprint XML configuration files, and a Scala DSL.
 </li>
 <li>
  <a href="https://github.com/eBay/fabio">
   Fabio
  </a>
  - A fast, modern, zero-conf load balancing HTTP/S router for deploying microservices managed by Consul.
  <sup>
   108 GitHub links in total 406 links, &#9733 1874, pushed 6 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.haproxy.org/">
   HAProxy
  </a>
  - Reliable, high Performance TCP/HTTP load balancer.
 </li>
 <li>
  <a href="https://getkong.org/">
   Kong
  </a>
  - Open source management layer for APIs.
 </li>
 <li>
  <a href="https://github.com/eBay/Neutrino">
   Neutrino
  </a>
  - Extensible software load balancer.
  <sup>
   108 GitHub links in total 406 links, &#9733 176, pushed 25 days ago
  </sup>
 </li>
 <li>
  <a href="http://openresty.org/">
   OpenResty
  </a>
  - Fast web application server built on top of Nginx.
 </li>
 <li>
  <a href="http://tengine.taobao.org/">
   Tengine
  </a>
  - A distribution of Nginx with some advanced features.
 </li>
 <li>
  <a href="http://traefik.io/">
   Træfɪk
  </a>
  - A modern HTTP reverse proxy and load balancer made to deploy microservices with ease.
 </li>
 <li>
  <a href="https://tyk.io/">
   Tyk
  </a>
  - Open source, fast and scalable API gateway, portal and API management platform.
 </li>
 <li>
  <a href="https://github.com/vulcand/vulcand">
   Vulcand
  </a>
  - Programmatic load balancer backed by Etcd.
  <sup>
   108 GitHub links in total 406 links, &#9733 1910, pushed 8 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Netflix/zuul">
   Zuul
  </a>
  - An edge service that provides dynamic routing, monitoring, resiliency, security, and more.
  <sup>
   108 GitHub links in total 406 links, &#9733 964, pushed 27 days ago
  </sup>
 </li>
</ul>
<h3>
 Configuration and Discovery
</h3>
<ul>
 <li>
  <a href="https://www.consul.io/">
   Consul
  </a>
  - Service discovery and configuration made easy. Distributed, highly available, and datacenter-aware.
 </li>
 <li>
  <a href="https://github.com/Netflix/denominator">
   Denominator
  </a>
  - Portably control DNS clouds using java or bash.
  <sup>
   108 GitHub links in total 406 links, &#9733 226, pushed 144 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/ha/doozerd">
   Doozer
  </a>
  - Highly-available, completely consistent store for small amounts of data. When the data changes, it can notify connected clients immediately.
  <sup>
   108 GitHub links in total 406 links, &#9733 2663, pushed 48 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/coreos/etcd">
   Etcd
  </a>
  - Highly-available key-value store for shared configuration and service discovery.
  <sup>
   108 GitHub links in total 406 links, &#9733 9440, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Netflix/eureka/wiki/Eureka-at-a-glance">
   Eureka
  </a>
  - REST based service that is primarily used in the AWS cloud for locating services for the purpose of load balancing and failover of middle-tier servers.
 </li>
 <li>
  <a href="https://github.com/gliderlabs/registrator">
   Registrator
  </a>
  - Service registry bridge for Docker. Supports pluggable service registries, which currently includes Consul, etcd and SkyDNS 2.
  <sup>
   108 GitHub links in total 406 links, &#9733 2104, pushed 6 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/nanopack/shaman">
   Shaman
  </a>
  - Small, lightweight, api-driven DNS server.
  <sup>
   108 GitHub links in total 406 links, &#9733 24, pushed 77 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/skynetservices/skydns">
   SkyDNS
  </a>
  - Distributed service for announcement and discovery of services built on top of etcd. It utilizes DNS queries to discover available services.
  <sup>
   108 GitHub links in total 406 links, &#9733 1124, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/airbnb/smartstack-cookbook">
   SmartStack
  </a>
  - Airbnb's automated service discovery and registration framework.
  <sup>
   108 GitHub links in total 406 links, &#9733 161, pushed 427 days ago
  </sup>
 </li>
 <li>
  <a href="http://cloud.spring.io/spring-cloud-config/">
   Spring Cloud Config
  </a>
  - Provides server and client-side support for externalized configuration in a distributed system.
 </li>
 <li>
  <a href="https://zookeeper.apache.org/">
   ZooKeeper
  </a>
  - Open source server which enables highly reliable distributed coordination.
 </li>
</ul>
<h3>
 Security
</h3>
<ul>
 <li>
  <a href="https://github.com/spotify/crtauth">
   Crtauth
  </a>
  - A public key backed client/server authentication system.
  <sup>
   108 GitHub links in total 406 links, &#9733 65, pushed 60 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/coreos/dex">
   Dex
  </a>
  - Opinionated auth/directory service with pluggable connectors. OpenID Connect provider and third-party OAuth 2.0 delegation.
  <sup>
   108 GitHub links in total 406 links, &#9733 645, pushed 7 days ago
  </sup>
 </li>
 <li>
  <a href="http://jwt.io/">
   JWT
  </a>
  - JSON Web Tokens are an open, industry standard RFC 7519 method for representing claims securely between two parties.
 </li>
 <li>
  <a href="https://github.com/keycloak/keycloak">
   Keycloak
  </a>
  - Full-featured and extensible auth service. OpenID Connect provider and third-party OAuth 2.0 delegation.
  <sup>
   108 GitHub links in total 406 links, &#9733 481, pushed 0 days ago
  </sup>
 </li>
 <li>
  <a href="http://oauth.net/2/">
   OAuth
  </a>
  - Provides specific authorization flows for web applications, desktop applications, mobile phones, and living room devices. Many implementations.
 </li>
 <li>
  <a href="http://openid.net/developers/libraries/">
   OpenID Connect
  </a>
  - Libraries, products, and tools implementing current OpenID specifications and related specs.
 </li>
 <li>
  <a href="https://github.com/osiam/osiam">
   OSIAM
  </a>
  - Open source identity and access management implementing OAuth 2.0 and SCIMv2.
  <sup>
   108 GitHub links in total 406 links, &#9733 38, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.simplecloud.info/">
   SCIM
  </a>
  - System for Cross-domain Identity Management.
 </li>
 <li>
  <a href="https://www.vaultproject.io/">
   Vault
  </a>
  - Secures, stores, and tightly controls access to tokens, passwords, certificates, API keys, and other secrets in modern computing.
 </li>
</ul>
<h3>
 Elasticity
</h3>
<ul>
 <li>
  <a href="https://github.com/mesos/chronos">
   Chronos
  </a>
  - Fault tolerant job scheduler for Mesos which handles dependencies and ISO8601 based schedules.
  <sup>
   108 GitHub links in total 406 links, &#9733 3185, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Netflix/Fenzo">
   Fenzo
  </a>
  - Extensible scheduler for Mesos frameworks.
  <sup>
   108 GitHub links in total 406 links, &#9733 291, pushed 18 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.paralleluniverse.co/galaxy/">
   Galaxy
  </a>
  - Open source high-performance in-memory data-grid.
 </li>
 <li>
  <a href="http://reverbrain.com/grape/">
   Grape
  </a>
  - Realtime processing pipeline.
 </li>
 <li>
  <a href="http://hazelcast.org/">
   Hazelcast
  </a>
  - Open source in-memory data-grid. Allows you to distribute data and computation across servers, clusters and geographies, and to manage very large data sets or high data ingest rates. Mature technology.
 </li>
 <li>
  <a href="http://helix.apache.org/">
   Helix
  </a>
  - Generic cluster management framework used for the automatic management of partitioned, replicated and distributed resources hosted on a cluster of nodes.
 </li>
 <li>
  <a href="http://ignite.apache.org/">
   Ignite
  </a>
  - High-performance, integrated and distributed in-memory platform for computing and transacting on large-scale data sets in real-time, orders of magnitude faster than possible with traditional disk-based or flash technologies.
 </li>
 <li>
  <a href="https://mesosphere.github.io/marathon/">
   Marathon
  </a>
  - Deploy and manage containers (including Docker) on top of Apache Mesos at scale.
 </li>
 <li>
  <a href="https://mesos.apache.org/">
   Mesos
  </a>
  - Abstracts CPU, memory, storage, and other compute resources away from machines (physical or virtual), enabling fault-tolerant and elastic distributed systems to easily be built and run effectively.
 </li>
 <li>
  <a href="https://www.nomadproject.io/">
   Nomad
  </a>
  - Distributed, highly available, datacenter-aware scheduler.
 </li>
 <li>
  <a href="https://github.com/onyx-platform/onyx">
   Onyx
  </a>
  - Distributed, masterless, high performance, fault tolerant data processing for Clojure.
  <sup>
   108 GitHub links in total 406 links, &#9733 1205, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/boundary/ordasity">
   Ordasity
  </a>
  - Designed to spread persistent or long-lived workloads across several machines.
  <sup>
   108 GitHub links in total 406 links, &#9733 348, pushed 490 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/mrniko/redisson">
   Redisson
  </a>
  - Distributed and scalable Java data structures on top of Redis server.
  <sup>
   108 GitHub links in total 406 links, &#9733 1135, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://www.serfdom.io/">
   Serf
  </a>
  - Decentralized solution for cluster membership, failure detection and orchestration.
 </li>
</ul>
<h3>
 Messaging
</h3>
<ul>
 <li>
  <a href="http://zeromq.org/">
   ØMQ
  </a>
  - Brokerless intelligent transport layer.
 </li>
 <li>
  <a href="http://activemq.apache.org/">
   ActiveMQ
  </a>
  - Powerful open source messaging and integration patterns server.
 </li>
 <li>
  <a href="https://github.com/real-logic/Aeron">
   Aeron
  </a>
  - Efficient reliable UDP unicast, UDP multicast, and IPC message transport.
  <sup>
   108 GitHub links in total 406 links, &#9733 1743, pushed 8 days ago
  </sup>
 </li>
 <li>
  <a href="http://activemq.apache.org/apollo/">
   Apollo
  </a>
  - Faster, more reliable, easier to maintain messaging broker built from the foundations of the original ActiveMQ.
 </li>
 <li>
  <a href="https://github.com/mcollina/ascoltatori">
   Ascoltatori
  </a>
  - Pub/sub library for Node.
  <sup>
   108 GitHub links in total 406 links, &#9733 233, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="http://kr.github.io/beanstalkd/">
   Beanstalk
  </a>
  - Simple, fast work queue.
 </li>
 <li>
  <a href="https://github.com/antirez/disque">
   Disque
  </a>
  - Distributed message broker.
  <sup>
   108 GitHub links in total 406 links, &#9733 5070, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="http://kafka.apache.org/">
   Kafka
  </a>
  - Publish-subscribe messaging rethought as a distributed commit log.
 </li>
 <li>
  <a href="https://github.com/zeromq/malamute">
   Malamute
  </a>
  - ZeroMQ enterprise messaging broker.
  <sup>
   108 GitHub links in total 406 links, &#9733 142, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/nanopack/mist">
   Mist
  </a>
  - A distributed, tag-based pub/sub service.
  <sup>
   108 GitHub links in total 406 links, &#9733 455, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.mosca.io/">
   Mosca
  </a>
  - MQTT broker as a module.
 </li>
 <li>
  <a href="http://mosquitto.org/">
   Mosquitto
  </a>
  - Open source message broker that implements the MQTT protocol.
 </li>
 <li>
  <a href="http://nanomsg.org/">
   Nanomsg
  </a>
  - Socket library that provides several common communication patterns for building distributed systems.
 </li>
 <li>
  <a href="https://nats.io/">
   NATS
  </a>
  - Open source, high-performance, lightweight cloud messaging system.
 </li>
 <li>
  <a href="http://nsq.io/">
   NSQ
  </a>
  - A realtime distributed messaging platform.
 </li>
 <li>
  <a href="https://qpid.apache.org/">
   Qpid
  </a>
  - Cross-platform messaging components built on AMQP.
 </li>
 <li>
  <a href="https://www.rabbitmq.com/">
   RabbitMQ
  </a>
  - Open source Erlang-based message broker that just works.
 </li>
 <li>
  <a href="https://verne.mq">
   VerneMQ
  </a>
  - Open source, scalable, Erlang-based MQTT broker.
 </li>
</ul>
<h3>
 Serialization
</h3>
<ul>
 <li>
  <a href="https://github.com/ochrons/boopickle">
   BooPickle
  </a>
  - Binary serialization library for efficient network communication. For Scala and Scala.js
  <sup>
   108 GitHub links in total 406 links, &#9733 138, pushed 47 days ago
  </sup>
 </li>
 <li>
  <a href="https://capnproto.org/">
   Cap’n Proto
  </a>
  - Insanely fast data interchange format and capability-based RPC system.
 </li>
 <li>
  <a href="http://cbor.io/">
   CBOR
  </a>
  - Implementations of the CBOR standard (RFC 7049) in many languages.
 </li>
 <li>
  <a href="http://uscilab.github.io/cereal/">
   Cereal
  </a>
  - C++11 library for serialization.
 </li>
 <li>
  <a href="https://github.com/dakrone/cheshire">
   Cheshire
  </a>
  - Clojure JSON and JSON SMILE encoding/decoding.
  <sup>
   108 GitHub links in total 406 links, &#9733 777, pushed 21 days ago
  </sup>
 </li>
 <li>
  <a href="http://etch.apache.org/">
   Etch
  </a>
  - Cross-platform, language and transport-independent framework for building and consuming network services.
 </li>
 <li>
  <a href="https://github.com/alibaba/fastjson">
   Fastjson
  </a>
  - Fast JSON Processor.
  <sup>
   108 GitHub links in total 406 links, &#9733 4946, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/pquerna/ffjson">
   Ffjson
  </a>
  - Faster JSON serialization for Go.
  <sup>
   108 GitHub links in total 406 links, &#9733 1253, pushed 7 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/RuedigerMoeller/fast-serialization">
   FST
  </a>
  - Fast java serialization drop in-replacemen.
  <sup>
   108 GitHub links in total 406 links, &#9733 540, pushed 21 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/FasterXML/jackson">
   Jackson
  </a>
  -  A multi-purpose Java library for processing JSON data format.
  <sup>
   108 GitHub links in total 406 links, &#9733 1883, pushed 22 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/FasterXML/jackson-module-afterburner">
   Jackson Afterburner
  </a>
  - Jackson module that uses bytecode generation to further speed up data binding (+30-40% throughput for serialization, deserialization).
  <sup>
   108 GitHub links in total 406 links, &#9733 82, pushed 28 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/EsotericSoftware/kryo">
   Kryo
  </a>
  - Java serialization and cloning: fast, efficient, automatic.
  <sup>
   108 GitHub links in total 406 links, &#9733 1847, pushed 9 days ago
  </sup>
 </li>
 <li>
  <a href="http://msgpack.org/">
   MessagePack
  </a>
  - Efficient binary serialization format.
 </li>
 <li>
  <a href="http://www.protostuff.io/">
   Protostuff
  </a>
  - A serialization library with built-in support for forward-backward compatibility (schema evolution) and validation.
 </li>
 <li>
  <a href="https://github.com/harrah/sbinary">
   SBinary
  </a>
  - Library for describing binary formats for Scala types.
  <sup>
   108 GitHub links in total 406 links, &#9733 78, pushed 149 days ago
  </sup>
 </li>
 <li>
  <a href="http://thrift.apache.org/">
   Thrift
  </a>
  - The Apache Thrift software framework, for scalable cross-language services development.
 </li>
</ul>
<h3>
 Storage
</h3>
<ul>
 <li>
  <a href="http://www.aerospike.com/">
   Aerospike
  </a>
  - High performance NoSQL database delivering speed at scale.
 </li>
 <li>
  <a href="https://www.arangodb.com/">
   ArangoDB
  </a>
  - A distributed free and open source database with a flexible data model for documents, graphs, and key-values.
 </li>
 <li>
  <a href="http://www.couchbase.com/">
   Couchbase
  </a>
  - A distributed database engineered for performance, scalability, and simplified administration.
 </li>
 <li>
  <a href="https://crate.io/">
   Crate
  </a>
  - Scalable SQL database with the NoSQL goodies.
 </li>
 <li>
  <a href="http://www.datomic.com/">
   Datomic
  </a>
  - Fully transactional, cloud-ready, distributed database.
 </li>
 <li>
  <a href="http://druid.io/">
   Druid
  </a>
  - Fast column-oriented distributed data store.
 </li>
 <li>
  <a href="https://www.elastic.co/products/elasticsearch">
   Elasticsearch
  </a>
  - Open source distributed, scalable, and highly available search server.
 </li>
 <li>
  <a href="http://reverbrain.com/elliptics/">
   Elliptics
  </a>
  - Fault tolerant distributed key/value storage.
 </li>
 <li>
  <a href="http://geode.incubator.apache.org/">
   Geode
  </a>
  - Open source, distributed, in-memory database for scale-out applications.
 </li>
 <li>
  <a href="http://www.memsql.com/">
   MemSQL
  </a>
  - High-performance, in-memory database that combines the horizontal scalability of distributed systems with the familiarity of SQL.
 </li>
 <li>
  <a href="https://parquet.apache.org/">
   Parquet
  </a>
  - Columnar storage format available to any project in the Hadoop ecosystem, regardless of the choice of data processing framework, data model or programming language.
 </li>
 <li>
  <a href="https://github.com/reborndb/reborn">
   Reborn
  </a>
  - Distributed database fully compatible with redis protocol.
  <sup>
   108 GitHub links in total 406 links, &#9733 507, pushed 53 days ago
  </sup>
 </li>
 <li>
  <a href="http://rethinkdb.com/">
   RethinkDB
  </a>
  - Open source, scalable database that makes building realtime apps easier.
 </li>
 <li>
  <a href="https://github.com/ssbc/docs">
   Secure Scuttlebutt
  </a>
  - P2P database of message-feeds.
  <sup>
   108 GitHub links in total 406 links, &#9733 47, pushed 82 days ago
  </sup>
 </li>
 <li>
  <a href="http://tachyon-project.org/">
   Tachyon
  </a>
  - Memory-centric distributed storage system, enabling reliable data sharing at memory-speed across cluster frameworks.
 </li>
</ul>
<h3>
 Reactivity
</h3>
<ul>
 <li>
  <a href="https://github.com/softwaremill/reactive-kafka">
   Reactive Kafka
  </a>
  - Reactive Streams API for Apache Kafka.
 </li>
 <li>
  <a href="http://reactivex.io/">
   ReactiveX
  </a>
  - API for asynchronous programming with observable streams. Available for idiomatic Java, Scala, C#, C++, Clojure, JavaScript, Python, Groovy, JRuby, and others.
 </li>
 <li>
  <a href="https://github.com/aol/simple-react">
   Simple React
  </a>
  - Powerful future streams & asynchronous data structures for Java 8.
 </li>
</ul>
<h3>
 Resilience
</h3>
<ul>
 <li>
  <a href="https://github.com/Netflix/Hystrix">
   Hystrix
  </a>
  - Latency and fault tolerance library designed to isolate points of access to remote systems, services and 3rd party libraries, stop cascading failure and enable resilience in complex distributed systems where failure is inevitable.
  <sup>
   108 GitHub links in total 406 links, &#9733 5815, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="http://pathod.net/">
   Pathod
  </a>
  - Crafted malice for tormenting HTTP clients and servers.
 </li>
 <li>
  <a href="http://raftconsensus.github.io/">
   Raft Consensus
  </a>
  - Consensus algorithm that is designed to be easy to understand. It's equivalent to Paxos in fault-tolerance and performance.
 </li>
 <li>
  <a href="http://resilient-http.github.io/">
   Resilient HTTP
  </a>
  - A smart HTTP client with super powers like fault tolerance, dynamic server discovery, auto balancing and reactive recovery, designed for distributed systems.
 </li>
 <li>
  <a href="https://github.com/tomakehurst/saboteur">
   Saboteur
  </a>
  - Causing deliberate network mayhem for better resilience.
  <sup>
   108 GitHub links in total 406 links, &#9733 217, pushed 249 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Netflix/SimianArmy">
   Simian Army
  </a>
  - Suite of tools for keeping your cloud operating in top form. Chaos Monkey, the first member, is a resiliency tool that helps ensure that your applications can tolerate random instance failures.
  <sup>
   108 GitHub links in total 406 links, &#9733 3979, pushed 34 days ago
  </sup>
 </li>
</ul>
<h3>
 Testing
</h3>
<ul>
 <li>
  <a href="https://mitmproxy.org/">
   Mitmproxy
  </a>
  - An interactive console program that allows traffic flows to be intercepted, inspected, modified and replayed.
 </li>
 <li>
  <a href="http://www.mbtest.org/">
   Mountebank
  </a>
  - Cross-platform, multi-protocol test doubles over the wire.
 </li>
 <li>
  <a href="https://github.com/vcr/vcr">
   VCR
  </a>
  - Record your test suite's HTTP interactions and replay them during future test runs for fast, deterministic, accurate tests. See the list of ports for implementations in other languages.
  <sup>
   108 GitHub links in total 406 links, &#9733 2930, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/epam/Wilma">
   Wilma
  </a>
  - Combined HTTP/HTTPS service stub and transparent proxy solution.
  <sup>
   108 GitHub links in total 406 links, &#9733 10, pushed 6 days ago
  </sup>
 </li>
 <li>
  <a href="http://wiremock.org/">
   WireMock
  </a>
  - Flexible library for stubbing and mocking web services. Unlike general purpose mocking tools it works by creating an actual HTTP server that your code under test can connect to as it would a real web service.
 </li>
</ul>
<h3>
 Monitoring and Debugging
</h3>
<ul>
 <li>
  <a href="https://www.elastic.co/products/beats">
   Beats
  </a>
  - Lightweight shippers for Elasticsearch & Logstash.
 </li>
 <li>
  <a href="https://collectd.org/">
   Collectd
  </a>
  - The system statistics collection daemon.
 </li>
 <li>
  <a href="https://github.com/yelp/elastalert">
   Elastalert
  </a>
  - Easy & flexible alerting for Elasticsearch.
  <sup>
   108 GitHub links in total 406 links, &#9733 1777, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="http://ganglia.info/">
   Ganglia
  </a>
  - A scalable distributed monitoring system for high-performance computing systems such as clusters and grids.
 </li>
 <li>
  <a href="http://grafana.org/">
   Grafana
  </a>
  - An open source, feature rich metrics dashboard and graph editor for
Graphite, InfluxDB & OpenTSDB.
 </li>
 <li>
  <a href="http://graphite.wikidot.com/">
   Graphite
  </a>
  - Scalable realtime graphing.
 </li>
 <li>
  <a href="https://github.com/eBay/parallec">
   Parallec
  </a>
  - Fast parallel asynchronous HTTP/SSH/TCP/Ping client Java library.
  <sup>
   108 GitHub links in total 406 links, &#9733 326, pushed 10 days ago
  </sup>
 </li>
 <li>
  <a href="http://prometheus.io/">
   Prometheus
  </a>
  - An open source service monitoring system and time series database.
 </li>
 <li>
  <a href="https://github.com/eBay/restcommander">
   REST Commander
  </a>
  - Fast parallel asynchronous HTTP client as a service to monitor and manage HTTP endpoints.
  <sup>
   108 GitHub links in total 406 links, &#9733 715, pushed 119 days ago
  </sup>
 </li>
 <li>
  <a href="http://riemann.io/">
   Riemann
  </a>
  - Monitors distributed systems.
 </li>
 <li>
  <a href="https://github.com/sensu">
   Sensu
  </a>
  - Monitoring for today's infrastructure.
 </li>
 <li>
  <a href="https://github.com/RisingStack/trace-nodejs">
   Trace
  </a>
  - A visualised stack trace platform designed for microservices.
  <sup>
   108 GitHub links in total 406 links, &#9733 283, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="https://www.elastic.co/products/watcher">
   Watcher
  </a>
  - Alerting for Elasticsearch.
 </li>
 <li>
  <a href="http://www.zabbix.com/">
   Zabbix
  </a>
  - Open source enterprise-class monitoring solution.
 </li>
</ul>
<h3>
 Logging
</h3>
<ul>
 <li>
  <a href="http://www.fluentd.org/">
   Fluentd
  </a>
  - Open source data collector for unified logging layer.
 </li>
 <li>
  <a href="https://www.graylog.org/">
   Graylog
  </a>
  - Fully integrated open source log management platform.
 </li>
 <li>
  <a href="https://www.elastic.co/products/kibana">
   Kibana
  </a>
  - Flexible analytics and visualization platform.
 </li>
 <li>
  <a href="https://www.elastic.co/products/logstash">
   Logstash
  </a>
  - Tool for managing events and logs.
 </li>
 <li>
  <a href="https://github.com/Netflix/suro/wiki">
   Suro
  </a>
  - Distributed data pipeline which enables services for moving, aggregating, routing, storing data.
 </li>
</ul>
<h2>
 IT Automation / Provisioning
</h2>
<ul>
 <li>
  <a href="http://www.ansible.com/">
   Ansible
  </a>
  - Radically simple IT automation platform that makes your applications and systems easier to deploy.
 </li>
 <li>
  <a href="https://www.chef.io/chef/">
   Chef
  </a>
  - Automate how you build, deploy, and manage your infrastructure.
 </li>
 <li>
  <a href="https://github.com/spotify/helios">
   Helios
  </a>
  - Docker container orchestration platform.
  <sup>
   108 GitHub links in total 406 links, &#9733 1406, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://www.ottoproject.io/">
   Otto
  </a>
  - Development and deployment made easy.
 </li>
 <li>
  <a href="https://www.packer.io/">
   Packer
  </a>
  - Tool for creating identical machine images for multiple platforms from a single source configuration.
 </li>
 <li>
  <a href="https://puppetlabs.com/">
   Puppet
  </a>
  - From provisioning bare metal & launching containers to new ways to manage infrastructure as code.
 </li>
 <li>
  <a href="https://github.com/saltstack/salt">
   Salt
  </a>
  - Infrastructure automation and management system.
  <sup>
   108 GitHub links in total 406 links, &#9733 6489, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="https://www.terraform.io/">
   Terraform
  </a>
  - Provides a common configuration to launch infrastructure, from physical and virtual servers to email and DNS providers.
 </li>
</ul>
<h2>
 Deployment and Continuous Integration
</h2>
<h3>
 On-prem
</h3>
<ul>
 <li>
  <a href="https://github.com/gilt/ionroller">
   ION-Roller
  </a>
  - AWS immutable deployment framework for web services.
  <sup>
   108 GitHub links in total 406 links, &#9733 143, pushed 22 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/github/janky">
   Janky
  </a>
  - Continuous integration server built on top of Jenkins and Hubot.
  <sup>
   108 GitHub links in total 406 links, &#9733 2451, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="http://jenkins-ci.org/">
   Jenkins
  </a>
  - Extensible open source continuous integration server.
 </li>
 <li>
  <a href="https://github.com/nearform/nscale">
   Nscale
  </a>
  - Open toolkit supporting configuration, build and deployment of connected container sets.
  <sup>
   108 GitHub links in total 406 links, &#9733 293, pushed 314 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/DatawiseIO/Project6">
   Project 6
  </a>
  - Software for deploying and managing Docker containers across a cluster of hosts, with a focus on simplifying network and storage configurations for on-premises environments.
  <sup>
   108 GitHub links in total 406 links, &#9733 21, pushed 175 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/rancher/rancher">
   Rancher
  </a>
  - Open source platform for operating Docker in production.
  <sup>
   108 GitHub links in total 406 links, &#9733 3327, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="http://mojo.codehaus.org/rpm-maven-plugin/">
   RPM Maven
  </a>
  - Allows artifacts from one or more projects to be packaged in an RPM for distribution.
 </li>
</ul>
<h3>
 Hosted
</h3>
<ul>
 <li>
  <a href="http://aws.amazon.com/codedeploy/">
   AWS CodeDeploy
  </a>
  - Deployment service that enables developers to automate the deployment of applications to instances and to update the applications as required.
 </li>
 <li>
  <a href="http://aws.amazon.com/opsworks/">
   AWS OpsWorks
  </a>
  - Provides a simple and flexible way to create and manage stacks and applications.
 </li>
 <li>
  <a href="https://codeship.com/">
   Codeship
  </a>
  - Hosted continuous delivery platform that takes care
of the testing and deployment process.
 </li>
 <li>
  <a href="https://travis-ci.org/">
   Travis
  </a>
  - Continuous integration and deployment service.
 </li>
</ul>
<h3>
 Lightweight
</h3>
<ul>
 <li>
  <a href="https://github.com/puniverse/capsule">
   Capsule
  </a>
  - Packaging and deployment tool for JVM applications.
  <sup>
   108 GitHub links in total 406 links, &#9733 910, pushed 11 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/nathanmarz/kafka-deploy">
   Kafka Deploy
  </a>
  - Automated deploy for a Kafka cluster on AWS.
  <sup>
   108 GitHub links in total 406 links, &#9733 98, pushed 1551 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/flosell/lambdacd">
   LambdaCD
  </a>
  - A library to define a continuous delivery pipeline in code.
  <sup>
   108 GitHub links in total 406 links, &#9733 208, pushed 14 days ago
  </sup>
 </li>
</ul>
<h2>
 Containers
</h2>
<ul>
 <li>
  <a href="http://aws.amazon.com/ecs/">
   AWS ECS
  </a>
  - Easily run and manage Docker-enabled applications across a cluster of Amazon EC2 instances.
 </li>
 <li>
  <a href="https://coreos.com/">
   CoreOS
  </a>
  - Open source lightweight operating system based on the Linux kernel and designed for providing infrastructure to clustered deployments.
 </li>
 <li>
  <a href="https://dcos.io/">
   DC/OS
  </a>
  - Open source orchestration system (built on top of Mesos and Marathon) for automatically distributing and running containers on several computers.
 </li>
 <li>
  <a href="https://www.docker.com/">
   Docker
  </a>
  - Open platform for distributed applications for developers and sysadmins.
 </li>
 <li>
  <a href="http://kubernetes.io/">
   Kubernetes
  </a>
  - Open source orchestration system for Docker containers.
 </li>
 <li>
  <a href="https://linuxcontainers.org/">
   Linux Containers
  </a>
  - The umbrella project behind LXC, LXD, LXCFS and CGManager.
 </li>
 <li>
  <a href="https://github.com/rancher/os">
   RancherOS
  </a>
  - The smallest, easiest way to run Docker in production at scale.
  <sup>
   108 GitHub links in total 406 links, &#9733 2240, pushed 3 days ago
  </sup>
 </li>
</ul>
<h2>
 Documentation & Modeling
</h2>
<h3>
 REST APIs
</h3>
<ul>
 <li>
  <a href="https://github.com/danielgtaylor/aglio">
   Aglio
  </a>
  - API Blueprint renderer with theme support that outputs static HTML.
  <sup>
   108 GitHub links in total 406 links, &#9733 1850, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://apiblueprint.org/">
   API Blueprint
  </a>
  - Tools for your whole API lifecycle. Use it to discuss your API with others. Generate documentation automatically. Or a test suite. Or even some code.
 </li>
 <li>
  <a href="https://github.com/mbryzek/apidoc">
   Apidoc
  </a>
  - Beautiful documentation for REST services.
  <sup>
   108 GitHub links in total 406 links, &#9733 127, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="http://raml.org/">
   RAML
  </a>
  - RESTful API Modeling Language, a simple and succinct way of describing practically-RESTful APIs.
 </li>
 <li>
  <a href="https://github.com/tripit/slate">
   Slate
  </a>
  - Beautiful static documentation for your API.
  <sup>
   108 GitHub links in total 406 links, &#9733 9557, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="http://projects.spring.io/spring-restdocs/">
   Spring REST Docs
  </a>
  - Document RESTful services by combining hand-written documentation with auto-generated snippets produced with Spring MVC Test.
 </li>
 <li>
  <a href="http://swagger.io/">
   Swagger
  </a>
  - A simple yet powerful representation of your RESTful API.
 </li>
</ul>
<h2>
 Standards / Recommendations
</h2>
<h3>
 World Wide Web
</h3>
<ul>
 <li>
  <a href="http://www.w3.org/TR/webarch/">
   W3C.REC-Webarch
  </a>
  - Architecture of the World Wide Web, Volume One.
 </li>
 <li>
  <a href="https://tools.ietf.org/html/rfc3986">
   RFC3986
  </a>
  - Uniform Resource Identifier (URI): Generic Syntax.
 </li>
 <li>
  <a href="https://tools.ietf.org/html/rfc6570">
   RFC6570
  </a>
  - URI Template.
 </li>
 <li>
  <a href="https://tools.ietf.org/html/rfc7320">
   RFC7320
  </a>
  - URI Design and Ownership.
 </li>
</ul>
<h3>
 HTTP/1.1
</h3>
<ul>
 <li>
  <a href="https://tools.ietf.org/html/rfc7230">
   RFC7230
  </a>
  - Message Syntax and Routing.
 </li>
 <li>
  <a href="https://tools.ietf.org/html/rfc7231">
   RFC7231
  </a>
  - Semantics and Content.
 </li>
 <li>
  <a href="https://tools.ietf.org/html/rfc7232">
   RFC7232
  </a>
  - Conditional Requests.
 </li>
 <li>
  <a href="https://tools.ietf.org/html/rfc7233">
   RFC7233
  </a>
  - Range Requests.
 </li>
 <li>
  <a href="https://tools.ietf.org/html/rfc7234">
   RFC7234
  </a>
  - Caching.
 </li>
 <li>
  <a href="https://tools.ietf.org/html/rfc7235">
   RFC7235
  </a>
  - Authentication.
 </li>
</ul>
<h3>
 HTTP/2
</h3>
<ul>
 <li>
  <a href="https://tools.ietf.org/html/rfc7540">
   RFC7540
  </a>
  - Hypertext Transfer Protocol Version 2.
 </li>
</ul>
<h3>
 CoAP
</h3>
<ul>
 <li>
  <a href="http://coap.technology/spec.html">
   RFC7252
  </a>
  - The Constrained Application Protocol (CoAP) is a specialized web transfer protocol for use with constrained nodes and constrained networks in the Internet of Things.
 </li>
</ul>
<h3>
 RPC
</h3>
<ul>
 <li>
  <a href="http://bert-rpc.org/">
   BERT-RPC 1.0
  </a>
  - An attempt to specify a flexible binary serialization and RPC protocol that are compatible with the philosophies of dynamic languages.
 </li>
 <li>
  <a href="http://www.jsonrpc.org/specification">
   JSON-RPC 2.0
  </a>
  - A stateless, light-weight remote procedure call (RPC) protocol.
 </li>
</ul>
<h3>
 Messaging
</h3>
<ul>
 <li>
  <a href="http://www.amqp.org/">
   AMQP
  </a>
  - Advanced Message Queuing Protocol.
 </li>
 <li>
  <a href="http://mqtt.org/">
   MQTT
  </a>
  - MQ Telemetry Transport.
 </li>
 <li>
  <a href="https://stomp.github.io/">
   STOMP
  </a>
  - Simple Text Oriented Messaging Protocol.
 </li>
</ul>
<h3>
 Security
</h3>
<ul>
 <li>
  <a href="https://tools.ietf.org/html/rfc5246">
   RFC5246
  </a>
  - The Transport Layer Security (TLS) Protocol Version 1.2.
 </li>
 <li>
  <a href="https://tools.ietf.org/html/rfc6066">
   RFC6066
  </a>
  - TLS Extensions.
 </li>
 <li>
  <a href="https://tools.ietf.org/html/rfc6347">
   RFC6347
  </a>
  - Datagram Transport Layer Security Version 1.2.
 </li>
 <li>
  <a href="https://tools.ietf.org/html/rfc6749">
   RFC6749
  </a>
  - The OAuth 2.0 authorization framework.
 </li>
 <li>
  <a href="https://tools.ietf.org/html/rfc7515">
   RFC7515
  </a>
  - JSON Web Signature (JWS) represents content secured with digital signatures or Message Authentication Codes (MACs) using JSON-based data structures.
 </li>
 <li>
  <a href="https://tools.ietf.org/html/rfc7519">
   RFC7519
  </a>
  - JSON Web Token (JWT) is a compact, URL-safe means of representing claims to be transferred between two parties.
 </li>
 <li>
  <a href="https://tools.ietf.org/html/rfc7642">
   RFC7642
  </a>
  - SCIM: Definitions, overview, concepts, and requirements.
 </li>
 <li>
  <a href="https://tools.ietf.org/html/rfc7643">
   RFC7643
  </a>
  - SCIM: Core Schema, provides a platform-neutral schema and extension model for representing users and groups.
 </li>
 <li>
  <a href="https://tools.ietf.org/html/rfc7644">
   RFC7644
  </a>
  - SCIM: Protocol, an application-level, REST protocol for provisioning and managing identity data on the web.
 </li>
 <li>
  <a href="http://openid.net/connect/">
   OIDCONN
  </a>
  - OpenID Connect 1.0 is a simple identity layer on top of the OAuth 2.0 protocol. It allows clients to verify the identity of the end-user based on the authentication performed by an Authorization Server, as well as to obtain basic profile information about the end-user in an interoperable and REST-like manner.
 </li>
</ul>
<h3>
 Service Discovery
</h3>
<ul>
 <li>
  <a href="https://tools.ietf.org/html/draft-kelly-json-hal-07">
   HAL-DRAFT
  </a>
  - The JSON Hypertext Application Language (HAL) is a standard which establishes conventions for expressing hypermedia controls, such as links, with JSON.
  <sup>
   DRAFT
  </sup>
 </li>
 <li>
  <a href="http://www.hydra-cg.com/">
   Hydra
  </a>
  - Specifications for interoperable, hypermedia-driven Web APIs.
 </li>
 <li>
  <a href="http://www.w3.org/Submission/wadl/">
   WADL
  </a>
  - The Web Application Description Language specification.
 </li>
 <li>
  <a href="http://www.w3.org/TR/wsdl20/">
   WSDL
  </a>
  - The Web Services Description Language Version 2.0 spec.
 </li>
</ul>
<h3>
 Data Formats
</h3>
<ul>
 <li>
  <a href="https://tools.ietf.org/html/rfc4627">
   RFC4627
  </a>
  - JavaScript Object Notation (JSON).
 </li>
 <li>
  <a href="http://tools.ietf.org/search/rfc7049">
   RFC7049
  </a>
  - Concise Binary Object Representation (CBOR).
 </li>
 <li>
  <a href="http://bsonspec.org/">
   BSON
  </a>
  - Bin­ary JSON (BSON).
 </li>
 <li>
  <a href="http://json-ld.org/">
   JSON-LD
  </a>
  - JSON for Linking Data.
 </li>
 <li>
  <a href="https://github.com/FIXTradingCommunity/fix-simple-binary-encoding">
   SBE
  </a>
  - Simple Binary Encoding (SBE).
  <sup>
   108 GitHub links in total 406 links, &#9733 15, pushed 62 days ago
  </sup>
 </li>
 <li>
  <a href="http://wiki.fasterxml.com/SmileFormatSpec">
   SMILE
  </a>
  - JSON-compatible binary data format.
 </li>
 <li>
  <a href="https://github.com/msgpack/msgpack/blob/master/spec.md">
   MSGPACK
  </a>
  - MessagePack Specification.
 </li>
</ul>
<h3>
 Vocabularies
</h3>
<ul>
 <li>
  <a href="http://lov.okfn.org/">
   LOV
  </a>
  - Linked open vocabularies.
 </li>
 <li>
  <a href="http://schema.org/">
   Schema.org
  </a>
  - Collaborative, community activity with a mission to create, maintain, and promote schemas for structured data on the Internet, on web pages, in email messages, and beyond.
 </li>
</ul>
<h3>
 Unicode
</h3>
<ul>
 <li>
  <a href="http://www.unicode.org/versions/Unicode8.0.0/">
   UNIV8
  </a>
  - The Unicode Consortium. The Unicode Standard, Version 8.0.0, (Mountain View, CA: The Unicode Consortium, 2015. ISBN 978-1-936213-10-8).
 </li>
 <li>
  <a href="https://tools.ietf.org/html/rfc3629">
   RFC3629
  </a>
  - UTF-8, a transformation format of ISO 10646.
 </li>
</ul>
<h2>
 Real Life Stories
</h2>
<ul>
 <li>
  <a href="http://blog.cleancoder.com/uncle-bob/2014/10/01/CleanMicroserviceArchitecture.html">
   Clean microservice architecture
  </a>
 </li>
 <li>
  <a href="https://rclayton.silvrback.com/failing-at-microservices">
   Failing at microservices
  </a>
 </li>
 <li>
  <a href="https://blog.pivotal.io/labs/labs/how-to-talk-to-your-friends-about-microservices">
   How to talk to your friends about microservices
  </a>
 </li>
 <li>
  <a href="https://blog.yourkarma.com/building-microservices-at-karma">
   How we build microservices at Karma
  </a>
 </li>
 <li>
  <a href="http://philcalcado.com/2015/09/08/how_we_ended_up_with_microservices.html">
   How we ended up with microservices at SoundCloud
  </a>
 </li>
 <li>
  <a href="https://www.thoughtworks.com/insights/blog/microservices-lessons-frontline">
   Microservices: lessons from the frontline
  </a>
 </li>
 <li>
  <a href="http://martinfowler.com/bliki/MonolithFirst.html">
   Monolith first
  </a>
 </li>
 <li>
  <a href="http://www.infoq.com/news/2015/04/scaling-microservices-gilt">
   Scaling microservices at Gilt with Scala, Docker and AWS
  </a>
 </li>
</ul>
<h2>
 Theory
</h2>
<h3>
 Articles & Papers
</h3>
<ul>
 <li>
  <a href="http://akfpartners.com/techblog/2008/05/08/splitting-applications-or-services-for-scale/">
   AKF Scale Cube
  </a>
  - Model depicting the dimensions to scale a service.
 </li>
 <li>
  <a href="http://db.cs.berkeley.edu/papers/cidr11-bloom.pdf">
   CALM
  </a>
  - Consistency as logical monotonicity. :small
  <em>
   orange
  </em>
  diamond:
  <sup>
   PDF
  </sup>
 </li>
 <li>
  <a href="http://martinfowler.com/bliki/CanaryRelease.html">
   Canary Release
  </a>
  - Technique to reduce the risk of introducing a new software version in production by slowly rolling out the change to a small subset of users before rolling it out to the entire infrastructure and making it available to everybody.
 </li>
 <li>
  <a href="http://blog.thislongrun.com/2015/03/the-cap-theorem-series.html">
   CAP Theorem
  </a>
  -  States that it is impossible for a distributed computer system to simultaneously provide all three of the following guarantees: Consistency, Availability and Partition tolerance.
 </li>
 <li>
  <a href="https://msdn.microsoft.com/en-us/library/dn600223.aspx">
   Cloud Design Patterns
  </a>
  - Contains twenty-four design patterns that are useful in cloud-hosted applications. Includes: Circuit Breaker, Competing Consumers, CQRS, Event Sourcing, Gatekeeper, Cache-Aside, etc.
 </li>
 <li>
  <a href="http://alistair.cockburn.us/Hexagonal+architecture">
   Hexagonal Architecture
  </a>
  - Allows an application to equally be driven by users, programs, automated test or batch scripts, and to be developed and tested in isolation from its eventual run-time devices and databases.
 </li>
 <li>
  <a href="http://martinfowler.com/articles/microservices.html">
   Microservice Architecture
  </a>
  - Particular way of designing software applications as suites of independently deployable services.
 </li>
 <li>
  <a href="http://www.oracle.com/technetwork/issue-archive/2015/15-mar/o25architect-2458702.html">
   Microservices and SOA
  </a>
  - Similarities, differences, and where we go from here.
 </li>
 <li>
  <a href="https://dzone.com/refcardz/getting-started-with-microservices">
   Microservices RefCard
  </a>
  - Getting started with microservices.
 </li>
 <li>
  <a href="http://martinfowler.com/articles/microservice-trade-offs.html">
   Microservices Trade-Offs
  </a>
  - Guide to ponder costs and benefits of the mircoservices architectural style.
 </li>
 <li>
  <a href="http://www.reactivemanifesto.org/">
   Reactive Manifesto
  </a>
  - Reactive systems definition.
 </li>
 <li>
  <a href="http://www.reactive-streams.org/">
   Reactive Streams
  </a>
  - Initiative to provide a standard for asynchronous stream processing with non-blocking back pressure.
 </li>
 <li>
  <a href="http://resources.1060research.com/docs/2015/Resource-Oriented-Computing-Adaptive-Systems-ROCAS-1.2.pdf">
   ROCAS
  </a>
  - Resource Oriented Computing for Adaptive Systems. :small
  <em>
   orange
  </em>
  diamond:
  <sup>
   PDF
  </sup>
 </li>
 <li>
  <a href="http://ceur-ws.org/Vol-746/IWSECO2011-6-DengYu.pdf">
   SECO
  </a>
  - Understanding software ecosystems:
a strategic modeling approach. :small
  <em>
   orange
  </em>
  diamond:
  <sup>
   PDF
  </sup>
 </li>
 <li>
  <a href="https://www.nginx.com/blog/service-discovery-in-a-microservices-architecture/">
   Service Discovery in a Microservice Architecture
  </a>
  - Overview of discovery and registration patterns.
 </li>
 <li>
  <a href="http://martinfowler.com/articles/microservice-testing/">
   Testing Strategies in a Microservice Architecture
  </a>
  - Approaches for managing the additional testing complexity of multiple independently deployable components.
 </li>
 <li>
  <a href="http://monkey.org/~marius/funsrv.pdf">
   Your Server as a Function
  </a>
  - Describes three abstractions which combine to present a powerful programming model for building safe, modular, and efficient server software: Composable futures, services and filters. :small
  <em>
   orange
  </em>
  diamond:
  <sup>
   PDF
  </sup>
 </li>
</ul>
<h3>
 Tutorials
</h3>
<ul>
 <li>
  <a href="https://game-on.org/">
   Game On!
  </a>
  - Microservices architecture explained in the context of an old-school text-based adventure game.
 </li>
 <li>
  <a href="https://aws.amazon.com/blogs/compute/microservices-without-the-servers/">
   Microservices without the Servers
  </a>
  - Step by step demo-driven talk about serverless architecture.
 </li>
 <li>
  Microservices in C#:
  <a href="http://insidethecpu.com/2015/07/17/microservices-in-c-part-1-building-and-testing/">
   Part 1
  </a>
  ,
  <a href="http://insidethecpu.com/2015/07/31/microservices-in-c-part-2-consistent-message-delivery/">
   Part 2
  </a>
  ,
  <a href="http://insidethecpu.com/2015/08/14/microservices-in-c-part-3-queue-pool-sizing/">
   Part 3
  </a>
  ,
  <a href="http://insidethecpu.com/2015/08/28/microservices-in-c-part-4-scaling-out/">
   Part 4
  </a>
  ,
  <a href="http://insidethecpu.com/2015/09/11/microservices-in-c-part-5-autoscaling/">
   Part 5
  </a>
  .
 </li>
 <li>
  <a href="https://blog.codeship.com/packer-ansible/">
   Using Packer and Ansible to build immutable infrastructure
  </a>
 </li>
</ul>
<h3>
 Books
</h3>
<ul>
 <li>
  <a href="https://www.nginx.com/wp-content/uploads/2015/01/Building_Microservices_Nginx.pdf">
   Building Microservices
  </a>
  - Building Microservices: Designing Fine-grained Systems. Sam Newman. Preview Edition. :small
  <em>
   orange
  </em>
  diamond:
  <sup>
   PDF
  </sup>
 </li>
 <li>
  <a href="http://www.redbooks.ibm.com/abstracts/sg248275.html?Open">
   Microservices from Theory to Practice
  </a>
  - Microservices from Theory to Practice: Creating Applications in IBM Bluemix Using the Microservices Approach. IBM Redbooks publication.
 </li>
 <li>
  <a href="http://pivotal.io/platform/migrating-to-cloud-native-application-architectures-ebook">
   Migrating to Cloud Native Application Architectures
  </a>
  - This O’Reilly report defines the unique characteristics of cloud native application architectures such as microservices and twelve-factor applications.
 </li>
 <li>
  <a href="http://theartofscalability.com/">
   The Art of Scalability
  </a>
  - The Art of Scalability: Scalable Web Architecture, Processes, and Organizations for the Modern Enterprise. Martin L. Abbott, Michael T. Fisher.
 </li>
</ul>
<h3>
 Sites
</h3>
<ul>
 <li>
  <a href="http://martinfowler.com/microservices/">
   Microservices Resource Guide
  </a>
  - Martin Fowler's choice of articles, videos, books, and podcasts that can teach you more about the microservices architectural style.
 </li>
 <li>
  <a href="http://microservices.io/">
   Microservice Patterns
  </a>
  - Microservice architecture patterns and best practices.
 </li>
</ul>
<h2>
 Emerging Technologies
</h2>
<ul>
 <li>
  <a href="https://github.com/blockstack/blockchain-id/wiki">
   Blockchain ID
  </a>
  - A unique identifier that is secured by a blockchain. Blockchain IDs are simultaneously secure, human-meaningful, and decentralized, thereby squaring Zooko's triangle.
 </li>
 <li>
  <a href="http://blocknet.co/">
   Blocknet
  </a>
  - The Blocknet makes possible to deliver microservices over a blockchain-based P2P network architecture.
 </li>
 <li>
  <a href="http://edgware-fabric.org/">
   Edgware Fabric
  </a>
  - Lightweight, agile service bus for systems at the edge of the network, in the physical world.
 </li>
 <li>
  <a href="http://www.multichain.com/">
   MultiChain
  </a>
  - Open platform for building blockchains.
 </li>
 <li>
  <a href="http://nodered.org/">
   Node-RED
  </a>
  - Visual tool for wiring together hardware devices, APIs and online services in new and interesting ways.
 </li>
 <li>
  <a href="http://www.ponylang.org/">
   Pony
  </a>
  - Open source, object-oriented, actor-model, capabilities-secure, high performance programming language.
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
<h2>
 Contributing
</h2>
<p>
 Please, read the
 <a href="https://github.com/mfornos/awesome-microservices/blob/master/CONTRIBUTING.md">
  Contribution Guidelines
 </a>
 before submitting your suggestion.
</p>
<p>
 Feel free to
 <a href="https://github.com/mfornos/awesome-microservices/issues">
  open an issue
 </a>
 or
 <a href="https://github.com/mfornos/awesome-microservices/pulls">
  create a pull request
 </a>
 with your additions.
</p>
<p>
 :star2: Thank you!
</p>
<h2>
 Acknowledgments
</h2>
<p>
 Table of contents generated with
 <a href="https://github.com/thlorenz/doctoc">
  DocToc
 </a>
</p>
