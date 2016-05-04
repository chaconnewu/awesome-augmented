<h1>
 Awesome REST
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<p>
 A collaborative list of great resources about RESTful API architecture, development, test, and performance. Feel free to contribute to this on-going list.
</p>
<ul>
 <li>
  <a href="#design">
   Design
  </a>
 </li>
 <li>
  <a href="#standards">
   Standards
  </a>
 </li>
 <li>
  <a href="#clients">
   Clients
  </a>
  <ul>
   <li>
    <a href="#php-clients">
     PHP
    </a>
   </li>
   <li>
    <a href="#javascript-clients">
     Client-side JavaScript
    </a>
   </li>
   <li>
    <a href="#nodejs-clients">
     Node.js
    </a>
   </li>
   <li>
    <a href="#ruby-clients">
     Ruby
    </a>
   </li>
   <li>
    <a href="#go-clients">
     Go
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#servers">
   Servers
  </a>
  <ul>
   <li>
    <a href="#directly-on-top-of-a-rmdb">
     Directly On Top Of A RMDB
    </a>
   </li>
   <li>
    <a href="#nodejs">
     Node.js
    </a>
   </li>
   <li>
    <a href="#php">
     PHP
    </a>
   </li>
   <li>
    <a href="#symfony2">
     Symfony2
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
   <li>
    <a href="#go">
     Go
    </a>
   </li>
   <li>
    <a href="#java">
     Java
    </a>
   </li>
   <li>
    <a href="#haskell">
     Haskell
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#testing">
   Testing
  </a>
  <ul>
   <li>
    <a href="#querying">
     Querying
    </a>
   </li>
   <li>
    <a href="#mocking">
     Mocking
    </a>
   </li>
   <li>
    <a href="#public-rest-apis-to-use-in-tests">
     Public REST APIs To Use In Tests
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#documentation">
   Documentation
  </a>
 </li>
 <li>
  <a href="#saas-tools">
   SaaS Tools
  </a>
 </li>
 <li>
  <a href="#miscellaneous">
   Miscellaneous
  </a>
 </li>
</ul>
<h2>
 Design
</h2>
<ul>
 <li>
  <a href="https://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm">
   Architectural Styles and
the Design of Network-based Software Architectures
  </a>
  - Roy Fielding's dissertation defining REST
 </li>
 <li>
  <a href="https://github.com/interagent/http-api-design">
   HTTP API design guide extracted from work on the Heroku Platform API
  </a>
  <sup>
   &#9733 11388, pushed 6 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api">
   Best Practices for Designing a Pragmatic RESTful API
  </a>
 </li>
 <li>
  <a href="http://blog.octo.com/en/design-a-rest-api/">
   How to design a REST API?
  </a>
  - Full guide tackling security, pagination, filtering, versioning, partial answers, CORS, etc.
 </li>
 <li>
  <a href="http://martinfowler.com/articles/enterpriseREST.html">
   Enterprise Integration Using REST
  </a>
  by the famous Martin Fowler
 </li>
 <li>
  <a href="http://timelessrepo.com/haters-gonna-hateoas">
   HATEOAS
  </a>
  - Clear explanation on what HATEOAS is, and why you should use it.
 </li>
 <li>
  <a href="http://www.infoq.com/articles/webber-rest-workflow/">
   How to GET a cup of coffee
  </a>
 </li>
</ul>
<h2>
 Standards
</h2>
<ul>
 <li>
  <a href="http://jsonapi.org/">
   JSON API
  </a>
  - Standard for building APIs in JSON.
 </li>
 <li>
  <a href="http://raml.org/">
   RAML
  </a>
  - Simple and succinct way to describe RESTful API.
 </li>
 <li>
  <a href="http://labs.omniti.com/labs/jsend">
   JSend
  </a>
  - Simple specification that lays down some rules for how JSON responses from web servers should be formatted.
 </li>
 <li>
  <a href="http://www.odata.org/">
   OData
  </a>
  - Open protocol to allow the creation and consumption of queryable and interoperable RESTful APIs. Quite complex.
 </li>
 <li>
  <a href="http://stateless.co/hal_specification.html">
   HAL
  </a>
  - Simple format that gives a consistent and easy way to hyperlink between resources in your API (see:
  <a href="#hateoas">
   HATEOAS
  </a>
  ).
 </li>
 <li>
  <a href="http://json-ld.org/">
   JSON-LD
  </a>
  - Standard for describing Linked Data and hypermedia relations in JSON (W3C).
 </li>
 <li>
  <a href="http://www.hydra-cg.com/">
   Hydra
  </a>
  - Vocabulary for Hypermedia-Driven Web APIs (W3C).
 </li>
 <li>
  <a href="http://schema.org">
   Schema.org
  </a>
  - Collection of schemas describing common data models.
 </li>
 <li>
  <a href="https://openapis.org/">
   OpenAPI
  </a>
  - Formerly known as the Swagger Specification, OpenAPI specifcation is the world’s most popular description format for defining Restful APIs.
 </li>
</ul>
<h2>
 Clients
</h2>
<h3>
 PHP Clients
</h3>
<ul>
 <li>
  <a href="http://guzzle.readthedocs.org/en/latest/">
   Guzzle
  </a>
  - HTTP client and framework for consuming RESTful web services.
 </li>
 <li>
  <a href="https://github.com/kriswallsmith/buzz">
   Buzz
  </a>
  <sup>
   &#9733 1233, pushed 26 days ago
  </sup>
  - Another lightweight HTTP client.
 </li>
 <li>
  <a href="https://github.com/Mashape/unirest-php">
   unirest for PHP
  </a>
  <sup>
   &#9733 786, pushed 4 days ago
  </sup>
  - Simplified, lightweight HTTP client library.
 </li>
</ul>
<h3>
 JavaScript Clients
</h3>
<ul>
 <li>
  <a href="https://github.com/mgonto/restangular">
   restangular
  </a>
  <sup>
   &#9733 7448, pushed 24 days ago
  </sup>
  - AngularJS service to handle REST API properly and easily.
 </li>
 <li>
  <a href="https://github.com/marmelab/restful.js">
   restful.js
  </a>
  <sup>
   &#9733 520, pushed 66 days ago
  </sup>
  - JS client for interacting with server-side RESTful resources.
 </li>
 <li>
  <a href="https://github.com/basti1302/traverson">
   traverson
  </a>
  <sup>
   &#9733 166, pushed 5 days ago
  </sup>
  - A Hypermedia API/HATEOAS Client for Node.js and the Browser
 </li>
 <li>
  <a href="https://github.com/mulesoft/raml-client-generator">
   raml-client-generator
  </a>
  <sup>
   &#9733 88, pushed 21 days ago
  </sup>
  - Generates static client libs for js.
 </li>
</ul>
<h3>
 Node.js Clients
</h3>
<ul>
 <li>
  <a href="https://github.com/danwrong/restler">
   restler
  </a>
  <sup>
   &#9733 1783, pushed 36 days ago
  </sup>
  - REST client library for node.js.
 </li>
 <li>
  <a href="https://github.com/Mashape/unirest-nodejs">
   unirest for Node.js
  </a>
  <sup>
   &#9733 515, pushed 57 days ago
  </sup>
  - Simplified, lightweight HTTP client library.
 </li>
</ul>
<h3>
 Ruby Clients
</h3>
<ul>
 <li>
  <a href="https://github.com/rest-client/rest-client">
   RESTClient
  </a>
  <sup>
   &#9733 3324, pushed 2 days ago
  </sup>
  - Simple HTTP and REST client for Ruby, inspired by microframework syntax for specifying actions.
 </li>
 <li>
  <a href="https://github.com/balvig/spyke">
   Spyke
  </a>
  <sup>
   &#9733 439, pushed 113 days ago
  </sup>
  - Interact with REST services in an ActiveRecord-like manner.
 </li>
 <li>
  <a href="https://github.com/excon/excon">
   excon
  </a>
  <sup>
   &#9733 723, pushed 36 days ago
  </sup>
  - Usable, fast, simple Ruby HTTP 1.1. It works great as a general HTTP(s) client and is particularly well suited to usage in API clients.
 </li>
</ul>
<h3>
 Go Clients
</h3>
<ul>
 <li>
  <a href="https://github.com/bndr/gopencils">
   gopencils
  </a>
  <sup>
   &#9733 342, pushed 103 days ago
  </sup>
  - Small and simple package to easily consume REST APIs.
 </li>
</ul>
<h2>
 Servers
</h2>
<h3>
 Directly On Top Of A RMDB
</h3>
<ul>
 <li>
  <a href="https://github.com/begriffs/postgrest">
   postgrest
  </a>
  <sup>
   &#9733 6716, pushed 2 days ago
  </sup>
  - Serve a fully RESTful API directly from an existing PostgreSQL database.
 </li>
 <li>
  <a href="http://blog.ulf-wendel.de/2014/mysql-5-7-http-plugin-mysql/">
   MySQL HTTP plugin
  </a>
  - Simple REST-like / CRUD server for any MySQL database.
 </li>
</ul>
<h3>
 Node.js
</h3>
<ul>
 <li>
  <a href="https://github.com/restify/node-restify">
   node-restify
  </a>
  <sup>
   &#9733 4970, pushed 4 days ago
  </sup>
  - Framework specifically meant for REST API.
 </li>
 <li>
  <a href="http://sailsjs.org/">
   Sails.js
  </a>
  - Node.js Web framework embedding a command to generate automatically a REST API.
 </li>
 <li>
  <a href="https://github.com/jspears/mers">
   mers
  </a>
  <sup>
   &#9733 335, pushed 317 days ago
  </sup>
  - Express service exposing Mongoose finders as RESTful API.
 </li>
 <li>
  <a href="https://github.com/wprl/baucis">
   Baucis
  </a>
  <sup>
   &#9733 563, pushed 57 days ago
  </sup>
  - Build scalable REST API based on your Mongoose entities.
 </li>
 <li>
  <a href="https://github.com/flatiron/resourceful">
   flatiron/resourceful
  </a>
  <sup>
   &#9733 348, pushed 477 days ago
  </sup>
  - Isomorphic Resource engine for JavaScript.
 </li>
 <li>
  <a href="http://loopback.io/">
   loopback
  </a>
  - Powerful Node.js framework for creating APIs and easily connecting to backend data sources.
 </li>
 <li>
  <a href="http://feathersjs.com/">
   Feathers
  </a>
  - is a real-time, micro-service web framework that gives you control over your data via RESTful resources, sockets and flexible plug-ins.
 </li>
</ul>
<h3>
 PHP
</h3>
<ul>
 <li>
  <a href="https://github.com/marmelab/microrest.php">
   Microrest
  </a>
  <sup>
   &#9733 164, pushed 215 days ago
  </sup>
  - Micro-web application providing a REST API on top of any relational database.
 </li>
 <li>
  <a href="https://github.com/willdurand/Negotiation">
   Negotiation
  </a>
  <sup>
   &#9733 319, pushed 56 days ago
  </sup>
  - Content negotiation library.
 </li>
 <li>
  <a href="https://github.com/leedavis81/drest">
   Drest
  </a>
  <sup>
   &#9733 71, pushed 56 days ago
  </sup>
  - Library for exposing Doctrine entities as REST resource endpoints.
 </li>
 <li>
  <a href="https://github.com/Luracast/Restler">
   Restler
  </a>
  <sup>
   &#9733 1074, pushed 4 days ago
  </sup>
  - Lightweight framework to expose PHP methods as RESTful web API.
 </li>
 <li>
  <a href="https://github.com/blongden/hal">
   HAL
  </a>
  <sup>
   &#9733 164, pushed 36 days ago
  </sup>
  - Hypertext Application Language (HAL) builder library.
 </li>
 <li>
  <a href="https://github.com/zfcampus/zf-apigility-skeleton">
   Apigility
  </a>
  <sup>
   &#9733 431, pushed 34 days ago
  </sup>
  - API builder built with Zend Framework 2.
 </li>
 <li>
  <a href="https://github.com/phprest/phprest">
   phprest
  </a>
  <sup>
   &#9733 281, pushed 163 days ago
  </sup>
  - Specialized REST microframework for PHP.
 </li>
 <li>
  <a href="https://github.com/willdurand/Hateoas">
   Hateoas
  </a>
  <sup>
   &#9733 628, pushed 35 days ago
  </sup>
  - PHP library to support implementing representations for HATEOAS REST web services.
 </li>
</ul>
<h4>
 Symfony2
</h4>
<ul>
 <li>
  <a href="http://williamdurand.fr/2012/08/02/rest-apis-with-symfony2-the-right-way/">
   REST APIs with Symfony2: the Right Way
  </a>
  - Complete guide to build a state-of-the-art REST API with Symfony2 framework.
 </li>
 <li>
  <a href="https://github.com/FriendsOfSymfony/FOSRestBundle">
   FOSRestBundle
  </a>
  <sup>
   &#9733 1337, pushed 1 days ago
  </sup>
  - Bundle handling view, routing, error handling, etc. for your REST API.
 </li>
 <li>
  <a href="https://github.com/stanlemon/rest-bundle">
   stanlemon/rest-bundle
  </a>
  <sup>
   &#9733 122, pushed 9 days ago
  </sup>
  - Build a REST API based on Doctrine entities using conventions over configuration.
 </li>
 <li>
  <a href="http://lakion.com/lionframe">
   lakion/Lionframe
  </a>
  - Glu between several community libraries to ease API development.
 </li>
 <li>
  <a href="https://github.com/willdurand/BazingaHateoasBundle">
   BazingaHateoasBundle
  </a>
  <sup>
   &#9733 164, pushed 61 days ago
  </sup>
  - Integrate the
  <a href="https://github.com/willdurand/Hateoas">
   Hateoas
  </a>
  library into a Symfony2 application.
 </li>
 <li>
  <a href="https://github.com/gimler/symfony-rest-edition">
   Symfony REST Edition
  </a>
  <sup>
   &#9733 471, pushed 32 days ago
  </sup>
  - Start with a Symfony2 application with all REST-friendly bundles pre-configured.
 </li>
 <li>
  <a href="https://github.com/marmelab/NgAdminGeneratorBundle">
   NgAdminGeneratorBundle
  </a>
  <sup>
   &#9733 66, pushed 364 days ago
  </sup>
  - Boostrap ng-admin configuration based on
  <code>
   stanlemon/rest-bundle
  </code>
  .
 </li>
 <li>
  <a href="https://github.com/dunglas/DunglasApiBundle">
   DunglasApiBundle
  </a>
  - Build a REST API which follow Hydra/JSON-LD specification.
 </li>
 <li>
  <a href="https://github.com/api-platform/api-platform">
   API Platform
  </a>
  <sup>
   &#9733 653, pushed 10 days ago
  </sup>
  - Specialize Symfony edition for the creation of hypermedia REST APIs.
 </li>
</ul>
<h3>
 Python
</h3>
<ul>
 <li>
  <a href="http://www.django-rest-framework.org/">
   Django REST framework
  </a>
  - Powerful and flexible toolkit that makes it easy to build Web APIs.
 </li>
 <li>
  <a href="http://tastypieapi.org/">
   django-tastypie
  </a>
  - Creating delicious APIs for Django apps.
 </li>
 <li>
  <a href="http://flask-restful.readthedocs.org/">
   flask-restful
  </a>
  - Extension for Flask that adds support for quickly building REST APIs.
 </li>
 <li>
  <a href="https://flask-restless.readthedocs.org/en/latest/">
   flask-restless
  </a>
  - Flask extension for generating ReSTful APIs for database models defined with SQLAlchemy (or Flask-SQLAlchemy).
 </li>
 <li>
  <a href="https://github.com/jeffknupp/sandman">
   sandman
  </a>
  <sup>
   &#9733 2219, pushed 63 days ago
  </sup>
  - Automated REST APIs for existing database-driven systems.
 </li>
 <li>
  <a href="http://restless.readthedocs.org/en/latest/">
   restless
  </a>
  - Framework agnostic REST framework based on lessons learned from TastyPie.
 </li>
 <li>
  <a href="https://github.com/RueLaLa/savory-pie/">
   savory-pie
  </a>
  - REST API building library (django, and others).
 </li>
 <li>
  <a href="http://python-eve.org/">
   Python Eve
  </a>
  - Eve is an open source Python REST API framework designed for human beings. It allows to effortlessly build and deploy highly customizable, fully featured RESTful Web Services.
 </li>
 <li>
  <a href="https://ramses.readthedocs.org/en/stable/">
   Ramses
  </a>
  - Makes RAML files executable by generating production-ready APIs from them at runtime.
 </li>
</ul>
<h3>
 Ruby
</h3>
<ul>
 <li>
  <a href="http://intridea.github.io/grape/">
   Grape
  </a>
  - Opinionated micro-framework for creating REST-like APIs in Ruby.
 </li>
</ul>
<h3>
 Go
</h3>
<ul>
 <li>
  <a href="https://github.com/manishrjain/gocrud">
   gocrud
  </a>
  <sup>
   &#9733 249, pushed 159 days ago
  </sup>
  : Go library to simplify creating, updating and deleting arbitrary depth structured data — to make building REST services fast and easy.
 </li>
 <li>
  <a href="https://github.com/ant0ine/go-json-rest">
   go-json-rest
  </a>
  <sup>
   &#9733 2302, pushed 2 days ago
  </sup>
  - Thin layer on top of
  <code>
   net/http
  </code>
  that helps building RESTful APIs easily.
 </li>
 <li>
  <a href="https://github.com/dougblack/sleepy">
   sleepy
  </a>
  <sup>
   &#9733 597, pushed 739 days ago
  </sup>
  - RESTful micro-framework written in Go.
 </li>
 <li>
  <a href="https://github.com/yookoala/restit">
   restit
  </a>
  - Go micro framework to help writing RESTful API integration test.
 </li>
 <li>
  <a href="https://github.com/codehack/go-relax">
   go-relax
  </a>
  <sup>
   &#9733 121, pushed 39 days ago
  </sup>
  - Framework of pluggable components to build RESTful API's.
 </li>
 <li>
  <a href="https://github.com/ungerik/go-rest">
   go-rest
  </a>
  <sup>
   &#9733 88, pushed 221 days ago
  </sup>
  - Small and evil REST framework for Go.
 </li>
 <li>
  <a href="https://github.com/emicklei/go-restful">
   go-restful
  </a>
  <sup>
   &#9733 1586, pushed 3 days ago
  </sup>
  - A declarative highly readable framework for building restful API's.
 </li>
 <li>
  <a href="https://github.com/bahlo/goat">
   Goat
  </a>
  <sup>
   &#9733 84, pushed 27 days ago
  </sup>
  - Minimalistic REST API server in Go.
 </li>
 <li>
  <a href="https://github.com/resoursea/api">
   Resoursea
  </a>
  <sup>
   &#9733 24, pushed 457 days ago
  </sup>
  - REST framework for quickly writing resource based services.
 </li>
 <li>
  <a href="https://github.com/cosiner/zerver">
   Zerver
  </a>
  <sup>
   &#9733 127, pushed 18 days ago
  </sup>
  - Zerver is a expressive, modular, feature completed RESTful framework.
 </li>
</ul>
<h3>
 Java
</h3>
<ul>
 <li>
  <a href="https://github.com/RestExpress/RestExpress">
   RestExpress
  </a>
  <sup>
   &#9733 597, pushed 4 days ago
  </sup>
  - Netty-based, highly performant, lightweight, container-less, plugin-extensible, framework that is ideal for microservice architectures.
 </li>
</ul>
<h3>
 Haskell
</h3>
<ul>
 <li>
  <a href="https://github.com/silkapp/rest">
   Rest for Haskell
  </a>
  <sup>
   &#9733 336, pushed 7 days ago
  </sup>
  - This package allows you to create REST APIs in Haskell. These APIs can be run in different web frameworks. They can also be used to automatically generate documentation as well as client libraries.
 </li>
</ul>
<h2>
 Testing
</h2>
<h3>
 Querying
</h3>
<ul>
 <li>
  <a href="https://www.hurl.it/">
   Hurl.it
  </a>
  - Make HTTP requests with a simple web-based HTTP client -- like
  <code>
   curl
  </code>
  in the cloud.
 </li>
 <li>
  <a href="https://github.com/jkbrzt/httpie">
   httpie
  </a>
  <sup>
   &#9733 22333, pushed 5 days ago
  </sup>
  - Command line HTTP client, far more dev-friendly than
  <code>
   curl
  </code>
  .
 </li>
 <li>
  <a href="https://chrome.google.com/webstore/detail/postman-rest-client/fdmmgilgnpjigdojojpjoooidkmcomcm">
   Postman REST Client
  </a>
  - Chrome extension essential to test manually REST API.
 </li>
 <li>
  <a href="https://github.com/micha/resty">
   resty
  </a>
  <sup>
   &#9733 1885, pushed 23 days ago
  </sup>
  - Little command line REST client that you can use in pipelines (bash or zsh).
 </li>
 <li>
  <a href="https://github.com/stedolan/jq">
   jq
  </a>
  <sup>
   &#9733 6555, pushed 19 days ago
  </sup>
  - Command line JSON processor, to use in combination with a command-line HTTP client like cURL.
 </li>
 <li>
  <a href="http://www.httpmaster.net">
   HttpMaster
  </a>
  - GUI tool for testing REST APIs and services. Windows OS only.
 </li>
 <li>
  <a href="https://github.com/cloudhead/http-console">
   Http-console
  </a>
  <sup>
   &#9733 1216, pushed 367 days ago
  </sup>
  - Command line interface for HTTP that let you
  <em>
   speak HTTP like a local
  </em>
 </li>
</ul>
<h3>
 Mocking
</h3>
<ul>
 <li>
  <a href="http://requestb.in/">
   RequestBin
  </a>
  - Inspect and debug webhook requests sent by your clients or third-party APIs.
 </li>
 <li>
  <a href="http://httpbin.org">
   httpbin
  </a>
  - HTTP request and response service - a/k/a Swiss Army Knife for HTTP.
 </li>
 <li>
  <a href="https://github.com/marmelab/FakeRest">
   FakeRest
  </a>
  <sup>
   &#9733 128, pushed 70 days ago
  </sup>
  - Patch XMLHttpRequest to fake a REST API client-side.
 </li>
 <li>
  <a href="https://github.com/typicode/json-server">
   json-server
  </a>
  <sup>
   &#9733 11821, pushed 7 days ago
  </sup>
  - Serve a REST API from fixture files using quick prototyping.
 </li>
 <li>
  <a href="http://www.mocky.io/">
   Mocky.io
  </a>
  - Free online service to create fake HTTP responses.
 </li>
 <li>
  <a href="https://github.com/bulkismaslom/swagger-api-mock">
   Swagger API Mock
  </a>
  <sup>
   &#9733 10, pushed 286 days ago
  </sup>
  - Mock RESTful API based on swagger schema
 </li>
</ul>
<h3>
 Public REST APIs To Use In Tests
</h3>
<ul>
 <li>
  <a href="http://deckofcardsapi.com">
   Deck of Cards API
  </a>
  - Open API for simulating a deck of cards.
 </li>
 <li>
  <a href="http://www.programmableweb.com/apis/directory">
   ProgrammableWeb
  </a>
  - The world's largest API repository.
 </li>
 <li>
  <a href="https://www.publicapis.com/">
   Public APIS
  </a>
  - Explore The Largest API Directory In The Galaxy.
 </li>
 <li>
  <a href="http://developer.marvel.com/">
   Marvel Comics API
  </a>
  - Query characters, stories, events about Marvel superheroes.
 </li>
 <li>
  <a href="http://jsonplaceholder.typicode.com/">
   JSON Placeholder
  </a>
  - Free online REST service that you can use whenever you need some fake data.
 </li>
</ul>
<h2>
 Documentation
</h2>
<ul>
 <li>
  <a href="http://swagger.io/">
   Swagger
  </a>
  - Documentation/querying web interface for REST APIs.
 </li>
 <li>
  <a href="http://apidocjs.com/">
   API doc
  </a>
  - Inline Documentation for RESTful web APIs.
 </li>
 <li>
  <a href="https://github.com/raml2html/raml2html">
   raml2html
  </a>
  <sup>
   &#9733 535, pushed 3 days ago
  </sup>
  - Generates HTML documentation from a RAML file.
 </li>
</ul>
<h2>
 SaaS tools
</h2>
<ul>
 <li>
  <a href="https://www.runscope.com/">
   Runscope
  </a>
  - Automated API Monitoring & Testing.
 </li>
 <li>
  <a href="https://ping-api.com/">
   Ping-API
  </a>
  - Automated API Monitoring & Testing.
 </li>
 <li>
  <a href="https://magic.import.io/">
   import.io Magic
  </a>
  - Create a REST API from any website in one click.
 </li>
 <li>
  <a href="https://apiary.io/">
   Apiary
  </a>
  - Collaborative design, instant API mock, generated documentation, integrated code samples, debugging and automated testing.
 </li>
 <li>
  <a href="https://aws.amazon.com/api-gateway/">
   Amazon API Gateway
  </a>
  - Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale.
 </li>
 <li>
  <a href="https://apigee.com">
   Apigee
  </a>
  - Apigee is the leading provider of API technology and services for enterprises and developers.
 </li>
</ul>
<h2>
 Miscellaneous
</h2>
<ul>
 <li>
  <a href="https://github.com/marmelab/ng-admin">
   ng-admin
  </a>
  <sup>
   &#9733 2751, pushed 12 days ago
  </sup>
  - Add an AngularJS admin GUI to any RESTful API.
 </li>
 <li>
  <a href="https://github.com/swagger-api/swagger-codegen">
   swagger-codegen
  </a>
  <sup>
   &#9733 2026, pushed 1 days ago
  </sup>
  - Auto generation of client libraries or server stubs given an OpenAPI speification (formerly known as the Swagger Specification).
 </li>
</ul>
<h2>
 License
</h2>
<p>
 <a href="http://creativecommons.org/licenses/by/4.0/">
  <img alt="Creative Commons License" src="http://i.creativecommons.org/l/by/4.0/88x31.png"/>
 </a>
</p>
<p>
 This work is licensed under a
 <a href="http://creativecommons.org/licenses/by/4.0/">
  Creative Commons Attribution 4.0 International License
 </a>
 .
</p>
