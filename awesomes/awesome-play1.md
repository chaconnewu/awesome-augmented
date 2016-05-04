<h1>
 Awesome Play1
 <a href="https://github.com/markets/awesome-ruby">
  <img alt="play-isthe1!" src="http://img.shields.io/badge/play-isthe1-red.svg?style=flat"/>
 </a>
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<p>
 A collection of awesome Play 1.x
 <a href="#modules">
  modules
 </a>
 ,
 <a href="#tools">
  tools
 </a>
 , and
 <a href="#resources">
  resources
 </a>
 .
</p>
<blockquote>
 <p>
  Inspired by
  <a href="https://github.com/ziadoz/awesome-php">
   awesome-php
  </a>
  ,
  <a href="https://github.com/vinta/awesome-python">
   awesome-python
  </a>
  ,
  <a href="https://github.com/dypsilon/frontend-dev-bookmarks">
   frontend-dev-bookmarks
  </a>
  and
  <a href="https://github.com/markets/awesome-ruby">
   awesome-ruby
  </a>
  .
 </p>
</blockquote>
<p>
 <a href="https://github.com/PerfectCarl/awesome-play1/blob/master/CONTRIBUTING.md">
  Contributions
 </a>
 are always welcome!
</p>
<h1>
 Modules
</h1>
<p>
 Lists all the modules available with the following
 <code>
  badges
 </code>
 :
</p>
<p>
 | Badge                                                                                                                                                                                 | Meaning                                                                                                                                                                                                                      |
 <br/>
 |---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|
 <a href="http://www.playframework.com/modules/carbonate">
  <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
 </a>
 | the module is registered in
 <a href="http://www.playframework.com/modules">
  playframework.com/modules
 </a>
 . The badge points to the registered page.                                                                                      |
|
 <a href="https://github.com/PerfectCarl/play-profiler">
  <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-no-red.svg?style=flat"/>
 </a>
 | the module is
 <strong>
  not
 </strong>
 registered in
 <a href="http://www.playframework.com/modules">
  playframework.com/modules
 </a>
 . You have to add an external repository in your
 <code>
  dependencies.yml
 </code>
 file. The badge points to the official module page. |
|
 <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.db/play-db">
  <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
 </a>
 | the module is available in MavenCentral thanks to the
 <a href="https://code.google.com/p/maven-play-plugin">
  maven-play-plugin
 </a>
 . The badge poins to the maven repository of the module.                                               |
|
 <a href="https://github.com/PerfectCarl/play-profiler">
  <img alt="Updated since the play module registry was frozen" src="http://img.shields.io/badge/ -updated-ff69b4.svg?style=flat"/>
 </a>
 | the module has been updated since
 <a href="http://www.playframework.com/modules">
  playframework.com/modules
 </a>
 has been frozen. The badge points to the official module page.                                                           |
</p>
<p>
 The modules are divided in the following categories : 
 *
 <a href="#database">
  Database
 </a>
 *
 <a href="#deployment">
  Deployment
 </a>
 *
 <a href="#injectiondependencies">
  Injection/dependencies
 </a>
 *
 <a href="#language">
  Language
 </a>
 *
 <a href="#messagingevents">
  Messaging/events
 </a>
 *
 <a href="#monitoring">
  Monitoring
 </a>
 *
 <a href="#persistence">
  Persistence
 </a>
 *
 <a href="#presentation">
  Presentation
 </a>
 *
 <a href="#rest">
  Rest
 </a>
 *
 <a href="#scaffolding">
  Scaffolding
 </a>
 *
 <a href="#search">
  Search
 </a>
 *
 <a href="#security">
  Security
 </a>
 *
 <a href="#template">
  Template
 </a>
 *
 <a href="#translation">
  Translation
 </a>
 *
 <a href="#misc">
  Misc
 </a>
</p>
<p>
 If you want to contribute information about a module, please refer to the
 <a href="https://github.com/PerfectCarl/awesome-play1/blob/master/CONTRIBUTING.md#module">
  guide
 </a>
 .
</p>
<h3>
 Database
</h3>
<ul>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/carbonate">
    [carbonate]
   </a>
   <a href="https://github.com/huljas/play-carbonate">
    Carbonate
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/carbonate">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Creates and runs database migrations using Hibernate schema update to automatically generate SQL to the migrations. See this blog
  <a href="http://huljas.github.com/code/2011/04/04/managing-database-with-playcarbonate.html">
   post
  </a>
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/chronostamp">
    [chronostamp]
   </a>
   <a href="https://github.com/omaroman/chronostamp">
    Chronostamp
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/chronostamp">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Enhances Models by adding and updating timestamp fields (created
  <em>
   at & updated
  </em>
  at).
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/db">
    [db]
   </a>
   <a href="http://github.com/pepite/play--database">
    Database module
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/db">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.db/play-db">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  Export your Play! domain model to a DDL file and import a database into your Play! domain model.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/jpagen">
    [jpagen]
   </a>
   <a href="http://github.com/marcuspocus/jpagen">
    JpaGen
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/jpagen">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Generates JPA Entities and Composite keys (when needed) from metadata or a file containing a list of tables.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/liquibase">
    [liquibase]
   </a>
   <a href="https://github.com/7uc0/play-liquibase">
    Liquibase
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/liquibase">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://www.liquibase.org">
   Liquibase
  </a>
  is a simple, reliable and elegant solution for database refactoring management
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/logisimayml">
    [logisimayml]
   </a>
   <a href="http://github.com/sim51/logisima-play-yml">
    logisima-yml
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/logisimayml">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Exports your database into an yml file
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/migrate">
    [migrate]
   </a>
   <a href="http://github.com/dcardon/play-migrate">
    Database migration
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/migrate">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Maintains database versions for your project.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/multidb">
    [multidb]
   </a>
   <a href="http://github.com/dcardon/play-multidb">
    Multiple Databases
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/multidb">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Scale your application to multiple databases with a common schema.
 </li>
</ul>
<h3>
 Deployment
</h3>
<ul>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/capistrano">
    [capistrano]
   </a>
   <a href="https://github.com/mandubian/play-capistrano">
    Capistrano
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/capistrano">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Deploys a remote application using Capistrano + SSH + VCS and run it in nohup/background mode.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/cargo">
    [cargo]
   </a>
   <a href="https://github.com/dgouyette/play-cargo">
    Cargo
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/cargo">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Remotely deploys your application.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/cloudbees">
    [cloudbees]
   </a>
   <a href="https://github.com/hadashi/play-cloudbees">
    CloudBees
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/cloudbees">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Provides integration with CloudBees.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/cloudfoundry">
    [cloudfoundry]
   </a>
   <a href="https://github.com/bcourtine/play--cloudfondry">
    CloudFoundry
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/cloudfoundry">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Automatically configure the database your application is deployed in In CloudFoundry.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/dotcloud">
    [dotcloud]
   </a>
   <a href="https://github.com/lsinger/play-dotcloud">
    Dotcloud
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/dotcloud">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Deploys your application to dotcloud
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/gae">
    [gae]
   </a>
   <a href="http://github.com/guillaumebort/play-gae">
    Google App Engine
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/gae">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.gae/play-gae">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  Creates application for the Google App Engine platform.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/heroku">
    [heroku]
   </a>
   <a href="https://github.com/jamesward/play-heroku">
    Heroku
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/heroku">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Deploys your application on Heroku.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/jelastic">
    [jelastic]
   </a>
   <a href="https://github.com/Fameing/play-jelastic">
    Jelastic Deployment Support
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/jelastic">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Deploy your application in the Jelastic Platform.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/openebay">
    [openebay]
   </a>
   <a href="https://bitbucket.org/kumaresan/openebay">
    Open eBay
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/openebay">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Provides the basic plumbing to create an
  <a href="http://apps.ebay.com/">
   Open eBay Application
  </a>
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/openshift">
    [openshift]
   </a>
   <a href="https://github.com/opensas/openshift">
    Openshift
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/openshift">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Openshift is Red Hat’s free, auto-scaling, cloud-based platform-as-a-service for Java, Perl, PHP, Python, and Ruby applications.
 </li>
 <li>
  <strong>
   [play-gae-q42]
   <a href="https://github.com/Q42/play-gae">
    Q42's Google App Engine
   </a>
  </strong>
  <a href="https://github.com/Q42/play-gae">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-no-red.svg?style=flat"/>
  </a>
  Maintained module for Google App Engine integration. Should be used instead of [gae]
  <sup>
   &#9733 3, pushed 237 days ago
  </sup>
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/playapps">
    [playapps]
   </a>
   <a href="http://github.com/zenexity/play-playapps">
    playapps.net
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/playapps">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  playapps.net is a streamlined deployment environment designed to get your Play applications up and running quickly and efficiently
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/reverseproxy">
    [reverseproxy]
   </a>
   <a href="https://github.com/omaroman/reverseproxy">
    ReverseProxy
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/reverseproxy">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Configures your application to automatically switch between the HTTP and HTTPS protocols per page when used behind a front end.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/router">
    [router]
   </a>
   <a href="https://github.com/digiPlant/play-router-annotations">
    Play Router Annotations
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/router">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.router/play-router">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  Adds routes through annotations, allowing you to declare your routes in your controllers.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/stax">
    [stax]
   </a>
   <a href="http://github.com/erwan/playstax">
    Stax
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/stax">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Easy deployment to Stax cloud hosting platform (http://www.stax.net).
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/vhost">
    [vhost]
   </a>
   <a href="https://github.com/lyubo/play-vhost">
    VHost
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/vhost">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Adds some virtual hosts functionality with separate datasource and customizable application settings for each virtual host.
 </li>
</ul>
<h3>
 Injection/dependencies
</h3>
<ul>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/constretto">
    [constretto]
   </a>
   <a href="https://github.com/zapodot/constretto-play">
    Constretto
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/constretto">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.constretto/play-constretto">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  Makes integration with the Constretto configration framework easy
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/guice">
    [guice]
   </a>
   <a href="http://github.com/pk11/play-guice-module">
    Guice
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/guice">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.guice/play-guice">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  Injects Guice managed components into your application.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/ivy">
    [ivy]
   </a>
   <a href="http://github.com/pk11/play-ivy">
    Ivy dependency management
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/ivy">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Manages your dependencies with apache ivy.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/maven">
    [maven]
   </a>
   <a href="http://github.com/wangyizhuo/play-maven">
    Maven dependency management
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/maven">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Manages your dependencies with apache maven
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/spring">
    [spring]
   </a>
   <a href="http://github.com/pepite/Play--framework-Spring-module">
    Spring
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/spring">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.spring/play-spring">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  Allows to use Spring managed beans inside your play! 1.x applications.
 </li>
</ul>
<h3>
 Language
</h3>
<ul>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/googleclosure">
    [googleclosure]
   </a>
   <a href="http://code.google.com/p/mandubian-play-google-closure/">
    Google Closure
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/googleclosure">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  This module is aimed at integrating Google Closure tools with play!.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/gwt">
    [gwt]
   </a>
   <a href="http://code.google.com/p/play-framework-gwt/">
    Google Web Toolkit
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/gwt">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  This module provides a helper to simplify the integration of a GWT UI with Play as an application server.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/gwt2">
    [gwt2]
   </a>
   <a href="http://github.com/vbuzzano/play-gwt2">
    GWT2
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/gwt2">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Integrates Play with GWT
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/scala">
    [scala]
   </a>
   <a href="http://www.playframework.com/modules/scala">
    Scala
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/scala">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.scala/play-scala">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  Play Scala enables you to use the Scala language for your application keeping key properties of the Play framework
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/scalagen">
    [scalagen]
   </a>
   <a href="https://github.com/asinghal/Play-ScalaGen">
    Scala Gen
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/scalagen">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Scala code generators for the Play! framework
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/scalasecure">
    [scalasecure]
   </a>
   <a href="https://github.com/asinghal/Play-ScalaSecure">
    Scala secure
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/scalasecure">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  This module provides basic security (authentication/ authorization) for Play applications written in Scala.
 </li>
</ul>
<h3>
 Messaging/events
</h3>
<ul>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/akka">
    [akka]
   </a>
   <a href="http://github.com/dwhitney/akka">
    Akka support
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/akka">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Allows you to configure
  <a href="http://akkasource.org">
   akka
  </a>
  through The Play! framework’s conf/application.conf file.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/camel">
    [camel]
   </a>
   <a href="https://github.com/marcuspocus/play-camel">
    Camel
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/camel">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  A EIP + Messaging module for the Play! Framework
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/pusher">
    [pusher]
   </a>
   <a href="https://github.com/regisbamba/Play-Pusher">
    Pusher
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/pusher">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  This module lets you easily add realtime functionality to your Play applications with
  <a href="http://www.pusher.com">
   Pusher
  </a>
  using websockets.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/rabbitmq">
    [rabbitmq]
   </a>
   <a href="http://geeks.aretotally.in/rabbitmq-module-for-play-framework">
    RabbitMQ
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/rabbitmq">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  RabbitMQ offers a highly available and scalable, and yet lightweight, messaging system.
 </li>
</ul>
<h3>
 Monitoring
</h3>
<ul>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/accesslog">
    [accesslog]
   </a>
   <a href="https://github.com/briannesbitt/play-accesslog">
    Accesslog
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/accesslog">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.accesslog/play-accesslog">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  A Play framework module that performs request logging similar to an access log file in nginx or apache.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/betterlogs">
    [betterlogs]
   </a>
   <a href="https://github.com/sgodbillon/BetterLogs">
    BetterLogs
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/betterlogs">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Enhances the default logs adding  the class and method names, where the log has been called, its signature, the file name and the line.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/infoplay">
    [infoplay]
   </a>
   <a href="http://code.google.com/p/infoplay/">
    InfoPlay
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/infoplay">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  InfoPlay is a module which gives many informations like infophp in PHP language.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/jpastats">
    [jpastats]
   </a>
   <a href="https://github.com/eamelink/play-jpastats/">
    Jpastats
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/jpastats">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Record how many database queries were executed during a request
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/log4play">
    [log4play]
   </a>
   <a href="https://github.com/feliperazeek/log4play">
    Log4Play
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/log4play">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Provides a log4j appender which publishes log entries to an EventStream
 </li>
 <li>
  <strong>
   [play-hibernate-statistics]
   <a href="https://github.com/francisdb/play-hibernate-statistics">
    Hibernate statistics
   </a>
  </strong>
  <a href="https://github.com/francisdb/play-hibernate-statistics">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-no-red.svg?style=flat"/>
  </a>
  Displays MBean Hibernate statistics
  <sup>
   &#9733 0, pushed 1233 days ago
  </sup>
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/playerrors">
    [playerrors]
   </a>
   <a href="https://github.com/marius0/playerrors">
    Playerrors
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/playerrors">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Playerrors gathers and informs you about the errors in your production webapps, so you can fix them before your visitors get a chance to complain
 </li>
 <li>
  <strong>
   [profiler]
   <a href="https://github.com/PerfectCarl/play-profiler">
    Mini-profiler
   </a>
  </strong>
  <a href="https://github.com/PerfectCarl/play-profiler">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-no-red.svg?style=flat"/>
  </a>
  Displays a mini profiler in your application
  <sup>
   &#9733 5, pushed 630 days ago
  </sup>
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/recordtracking">
    [recordtracking]
   </a>
   <a href="https://github.com/omaroman/recordtracking">
    RecordTracking
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/recordtracking">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  RecordTracking unobtrusively tracks the creation, updating and elimination events regarding to records.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/statsd">
    [statsd]
   </a>
   <a href="https://github.com/rkroll/play-statsd/">
    Statsd
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/statsd">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  The module is a wrapper over
  <a href="https://github.com/etsy/statsd">
   StatsD
  </a>
  which allow for dead simple statistic aggregation from within play.
 </li>
</ul>
<h3>
 Persistence
</h3>
<ul>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/associations">
    [associations]
   </a>
   <a href="https://github.com/pareis/play-associations">
    Associations
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/associations">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.associations/play-associations">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  This module reduces the code to manage bi-directional associations.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/cream">
    [cream]
   </a>
   <a href="https://github.com/mfornos/Cream">
    JCR for Play!
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/cream">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  A module that seamlessly integrates Apache Jackrabbit(JCR 2.0) with Play framework
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/ebean">
    [ebean]
   </a>
   <a href="https://github.com/lyubo/play-ebean">
    EBean ORM support
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/ebean">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.ebean/play-ebean">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  Adds Ebean ORM to play!. Still in very experimental phase.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/mongo">
    [mongo]
   </a>
   <a href="http://github.com/louth/play-mongo">
    MongoDB
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/mongo">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Provides a simple, elegant solution for using models stored in mongodb. For a more complex use cases, please take a look at the morphia module.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/morphia">
    [morphia]
   </a>
   <a href="http://github.com/greenlaw110/play-morphia">
    MongoDB Integration
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/morphia">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.morphia/play-morphia">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  <a href="http://github.com/greenlaw110/play-morphia">
   <img alt="Updated since the play module registry was frozen" src="http://img.shields.io/badge/ -updated-ff69b4.svg?style=flat"/>
  </a>
  Seamlessly MongoDB access integration with Play’s Model interface.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/mybatisplay">
    [mybatisplay]
   </a>
   <a href="https://github.com/eamelink/play-navigation/wiki">
    MyBatisPlay
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/mybatisplay">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Provides support for MyBatis persistence framework.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/neo4j">
    [neo4j]
   </a>
   <a href="https://github.com/sim51/logisima-play-neo4j">
    logisima-neo4j
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/neo4j">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Integrate neo4j database into your play! project.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/objectify">
    [objectify]
   </a>
   <a href="http://code.google.com/p/play-framework-objectify/">
    Objectify
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/objectify">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Objectify is a flexible abstraction on Google App Engine/J which makes data access simple and elegant
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/orientdb">
    [orientdb]
   </a>
   <a href="https://github.com/mfornos/orientdb">
    OrientDB
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/orientdb">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  OrientDB for Play! Framework
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/redis">
    [redis]
   </a>
   <a href="https://github.com/tkral/play-redis">
    Redis
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/redis">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.redis/play-redis">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  The Redis Play! module helps you easily use Redis in your Play! applications
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/riak">
    [riak]
   </a>
   <a href="https://github.com/julienba/play-riak/">
    Riak
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/riak">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Allow to use riak-java-client in play! way.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/s3blobs">
    [s3blobs]
   </a>
   <a href="https://github.com/jamesward/S3-Blobs-module-for-Play">
    S3Blobs
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/s3blobs">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  The S3Blobs Play Framework Module provides an easy way to read an write files from Amazon S3 from within JPA entities.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/siena">
    [siena]
   </a>
   <a href="http://github.com/mandubian/play-siena">
    Siena
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/siena">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.siena/play-siena">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  <a href="http://github.com/mandubian/play-siena">
   <img alt="Updated since the play module registry was frozen" src="http://img.shields.io/badge/ -updated-ff69b4.svg?style=flat"/>
  </a>
  Enables Siena support to map your Java entities to GAE/MySQL/PostgreSQL/H2 from your play application
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/twig">
    [twig]
   </a>
   <a href="https://github.com/netmau5/Play-Twig">
    Twig
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/twig">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Twig superpowers Google App Engine’s Datastore for Play applications. Get a fluid API, in-memory joins, and asynchronous queries out of the box.
 </li>
</ul>
<h3>
 Presentation
</h3>
<ul>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/coffee">
    [coffee]
   </a>
   <a href="https://github.com/robfig/play-coffee">
    CoffeeScript
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/coffee">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.coffee/play-coffee">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  CoffeeScript is a great way to produce javascript. This module provides support for it (Java and Scala).
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/excel">
    [excel]
   </a>
   <a href="http://github.com/greenlaw110/play-excel">
    Excel
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/excel">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.excel/play-excel">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  Template based Excel report generator
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/formee">
    [formee]
   </a>
   <a href="https://github.com/omaroman/formee">
    Formee
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/formee">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Helps to write forms and add client and server side validation.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/greenscript">
    [greenscript]
   </a>
   <a href="http://github.com/greenlaw110/greenscript">
    Minimize javascript/css files
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/greenscript">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Play with your javascript/css files!
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/html5validation">
    [html5validation]
   </a>
   <a href="https://github.com/oasits/play-html5-validation">
    HTML5 Validation
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/html5validation">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Client-side form validation based on your Play framework model annotations using HTML5 attributes.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/jqueryui">
    [jqueryui]
   </a>
   <a href="https://github.com/lunatech-labs/play-module-jqueryui">
    Jqueryui
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/jqueryui">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  The jQuery UI module provides working examples of jQuery UI widgets, integrated with a Play application.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/jqvalidate">
    [jqvalidate]
   </a>
   <a href="https://github.com/murz/play-jqvalidate">
    JQuery Validation
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/jqvalidate">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Client-side form validation via jQuery, based on your model annotation
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/jqvalidation">
    [jqvalidation]
   </a>
   <a href="http://code.google.com/p/jqvalidate-play-framework/">
    Jqvalidation
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/jqvalidation">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  A jquery library API for validation, supports Ajax validation (per field or per form)
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/less">
    [less]
   </a>
   <a href="https://github.com/lunatech-labs/play-module-less">
    Less module
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/less">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.less/play-less">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  Converts
  <a href="http://lesscss.org/">
   less
  </a>
  to CSS, and handles error reporting in your Play application
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/markdown">
    [markdown]
   </a>
   <a href="https://github.com/orefalo/play-markdown">
    Markdown
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/markdown">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.markdown/play-markdown">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  Easily bring markdown contents into your application.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/menu">
    [menu]
   </a>
   <a href="http://github.com/greenlaw110/play-menu">
    Menu
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/menu">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Eases the implementation of navigation menu.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/navigation">
    [navigation]
   </a>
   <a href="https://bitbucket.org/hlassiege/play-nemrod">
    Navigation
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/navigation">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Define and display navigation menus in your Play application.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/paginate">
    [paginate]
   </a>
   <a href="http://github.com/lmcalpin/Play--Paginate">
    Paginate
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/paginate">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.paginate/play-paginate">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  A replacement for #{list} tags that allows for easy pagination.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/pdf">
    [pdf]
   </a>
   <a href="http://github.com/pepite/play--pdf">
    PDF module
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/pdf">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.pdf/play-pdf">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  Renders PDF document from your HTML templates. This module is based on the YaHP Converter library.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/pegdown">
    [pegdown]
   </a>
   <a href="https://github.com/jagregory/play-pegdown">
    PegDown Markdown
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/pegdown">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Integrates the pegdown
  <a href="https://github.com/sirthias/pegdown">
   Markdown
  </a>
  processor with your Play application
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/press">
    [press]
   </a>
   <a href="http://github.com/dirkmc/press">
    Minimize javascript/css files
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/press">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  A JavaScript, CSS and Less minimizer that is designed to be transparent to the application developer.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/sass">
    [sass]
   </a>
   <a href="http://github.com/guillaumebort/play-sass">
    Syntactically Awesome Stylesheets
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/sass">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.sass/play-sass">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  Sass makes CSS fun again. Sass is CSS, plus nested rules, variables, mixins, and more, all in a concise, readable syntax.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/table">
    [table]
   </a>
   <a href="https://github.com/julienrf/play-table">
    Table
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/table">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.table/play-table">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  Simplifies the code needed to display data in HTML tables.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/tabularasa">
    [tabularasa]
   </a>
   <a href="https://github.com/schaloner/tabula-rasa">
    Tabula Rasa
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/tabularasa">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Tabula Rasa provides support for user-customisable tables in views
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/twitterbootstrap">
    [twitterbootstrap]
   </a>
   <a href="http://www.playframework.com/modules/twitterbootstrap">
    Twitterbootstrap
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/twitterbootstrap">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Bundles up the twitter-bootstrap stylekit and the play less plugin, easing the .less files edition (changes are dynamically taken into account).
 </li>
</ul>
<h3>
 Rest
</h3>
<ul>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/jersey">
    [jersey]
   </a>
   <a href="https://bitbucket.org/psartini/play-jersey">
    Jersey
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/jersey">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Integrates Jersey into the Play! Framework.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/resteasy">
    [resteasy]
   </a>
   <a href="http://www.lunatech-labs.com/open-source/resteasy-play-module">
    RESTEasy Play! module
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/resteasy">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  The RESTEasy Play! module allows you to define JAX-RS RESTful web services in the Play! Framework using RESTEasy.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/resteasycrud">
    [resteasycrud]
   </a>
   <a href="http://www.lunatech-labs.com/open-source/resteasy-crud-play-module">
    RESTEasy CRUD module
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/resteasycrud">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  The Play! RESTEasy CRUD module which allows you to automagically generate your RESTful CRUD resources for a given model
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/swagger">
    [swagger]
   </a>
   <a href="https://github.com/wordnik/swagger-play">
    Swagger
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/swagger">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Creates a self-documenting meta-description for REST APIs which allows for code-gen, UI-sandbox, and test framework.
 </li>
</ul>
<h3>
 Scaffolding
</h3>
<ul>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/crudsiena">
    [crudsiena]
   </a>
   <a href="https://github.com/mandubian/play-crud-siena">
    CRUD for Siena
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/crudsiena">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Offers a fully usable web interface for your Siena Model objects with a few more features than default [crud] module.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/mocha">
    [mocha]
   </a>
   <a href="https://bitbucket.org/blobsmith/mocha/overview">
    Mocha
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/mocha">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  An implementation of mocha UI javascript interface for Play!
 </li>
 <li>
  <strong>
   [play-bootstrap]
   <a href="https://github.com/phaus/play-bootstrap">
    Basic bootstrap scaffolding
   </a>
  </strong>
  <a href="https://github.com/phaus/play-bootstrap">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-no-red.svg?style=flat"/>
  </a>
  Creating Bootstrap based applications (derived from the default [scaffold] module).
  <sup>
   &#9733 12, pushed 991 days ago
  </sup>
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/scaffold">
    [scaffold]
   </a>
   <a href="http://github.com/lmcalpin/Play--Scaffold">
    Scaffold
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/scaffold">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Scaffold will generate basic scaffolding for bootstrapping a project from your JPA or Senia entities
 </li>
</ul>
<h3>
 Search
</h3>
<ul>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/elasticsearch">
    [elasticsearch]
   </a>
   <a href="http://geeks.aretotally.in/play-framework-module-elastic-search-distributed-searching-with-json-http-rest-or-java">
    ElasticSearch
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/elasticsearch">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Elastic Search is a Distributed Search Solution based on Apache Lucene. This module provides an embedded Elastic Server instance for Rapid Development.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/search">
    [search]
   </a>
   <a href="http://github.com/jfp/play-search/">
    Search
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/search">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.search/play-search">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  Search allows you to have basic full text search functionalities to your JPA Model. It is based on Lucene.
 </li>
</ul>
<h3>
 Security
</h3>
<ul>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/browserid">
    [browserid]
   </a>
   <a href="https://github.com/orefalo/play-browserid">
    BrowserID
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/browserid">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  BrowserID is an experimental new way of signing into websites. The goal with BrowserID is to design something safe and easy for users and the developers.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/cas">
    [cas]
   </a>
   <a href="http://github.com/sim51/logisima-play-cas">
    logisima-cas
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/cas">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  This module is a CAS client for Play! application.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/casino">
    [casino]
   </a>
   <a href="https://github.com/reyez/casino-play">
    Casino
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/casino">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  This project provides a simple method to integrate sign-up and password recovery to your project
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/deadbolt">
    [deadbolt]
   </a>
   <a href="https://github.com/schaloner/deadbolt">
    Deadbolt
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/deadbolt">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.deadbolt/play-deadbolt">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  Deadbolt is an authorisation mechanism for defining access rights to certain controller methods or parts of a view
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/fbconnect">
    [fbconnect]
   </a>
   <a href="https://github.com/murz/play-fbconnect">
    Facebook connect
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/fbconnect">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Easily integrate Facebook based authentication into any Play framework application.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/force">
    [force]
   </a>
   <a href="https://github.com/jesperfj/play-force">
    Force.com
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/force">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Build Play! applications that integrates to Force.com. Provides OAuth authentication and REST API adapter.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/linkedin">
    [linkedin]
   </a>
   <a href="http://geeks.aretotally.in/projects/play-framework-linkedin-module">
    LinkedIn OAuth Authentication
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/linkedin">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Easily integrate LinkedIn’s OAuth authentication into your Play Framework application
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/oauth">
    [oauth]
   </a>
   <a href="http://github.com/erwan/playoauthclient">
    OAuth Client
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/oauth">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  This module provides tools to connect to an OAuth provider, such as Twitter or Google.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/recaptcha">
    [recaptcha]
   </a>
   <a href="https://github.com/orefalo/play-recaptcha">
    Recaptcha
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/recaptcha">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.recaptcha/play-recaptcha">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  Quickly integrate reCaptcha.com challenge-response test in your applications.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/securepermissions">
    [securepermissions]
   </a>
   <a href="http://www.lunatech-labs.com/open-source/secure-permissions-play-module">
    Secure Permissions
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/securepermissions">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Extends the defaut secure module to add permission checks based on the rules in the Seam Framework (based on Drools rules).
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/securesocial">
    [securesocial]
   </a>
   <a href="http://jaliss.github.com/securesocial/">
    SecureSocial
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/securesocial">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.securesocial/play-securesocial">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  SecureSocial allows you to add an authentication UI to your app that works with services based on OAuth1, OAuth2, OpenID and OpenID+OAuth hybrid protocols
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/shibboleth">
    [shibboleth]
   </a>
   <a href="https://github.com/TAMULib/Shibboleth-play">
    Shibboleth
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/shibboleth">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Allow users to login to your Play! application via Shibboleth.
 </li>
</ul>
<h3>
 Template
</h3>
<ul>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/fastergt">
    [fastergt]
   </a>
   <a href="https://github.com/mbknor/faster-groovy-templates">
    Faster Groovy Templates
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/fastergt">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.fastergt/play-fastergt">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  Replaces the default groovy template implementation with GT-Engine which is faster and uses less memory.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/japid">
    [japid]
   </a>
   <a href="http://github.com/branaway/Japid">
    Japid Template Engine
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/japid">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.japid/play-japid">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  A pure Java-based fast statically typed template engine for the Play! framework version 1.2.x.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/mustache">
    [mustache]
   </a>
   <a href="https://github.com/murz/play-mustache">
    Mustache
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/mustache">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Allows you to define logic-less template snippets that can be used server-side in your Play! views as well as client-side in your JavaScript.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/rythm">
    [rythm]
   </a>
   <a href="https://github.com/greenlaw110/play-rythm">
    Rythm Template Engine
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/rythm">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.rythm/play-rythm">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  <a href="https://github.com/greenlaw110/play-rythm">
   <img alt="Updated since the play module registry was frozen" src="http://img.shields.io/badge/ -updated-ff69b4.svg?style=flat"/>
  </a>
  PlayRythm is a Razor like template engine.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/scalate">
    [scalate]
   </a>
   <a href="http://github.com/pk11/play-scalate">
    Scalate
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/scalate">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://scalate.fusesource.org">
   Scalate
  </a>
  Template engine support.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/thymeleaf">
    [thymeleaf]
   </a>
   <a href="https://github.com/choreo/play-thymeleaf">
    Thymeleaf
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/thymeleaf">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Play framework module to use
  <a href="http://www.thymeleaf.org/">
   Thymeleaf 2.0
  </a>
  as a template engine.
 </li>
</ul>
<h3>
 Testing
</h3>
<ul>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/cobertura">
    [cobertura]
   </a>
   <a href="http://github.com/julienba/play-cobertura">
    Cobertura
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/cobertura">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.cobertura/play-cobertura">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  Integrates with Cobertura to calculate the percentage of code accessed by tests (test coverage).
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/httpmock">
    [httpmock]
   </a>
   <a href="http://github.com/zenexity/play--httpmock">
    HttpMock
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/httpmock">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Caches WebService requests to emulate them in order to overcome connection problems (lag, denial of service, HTTP errors) for fast developping.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/mockito">
    [mockito]
   </a>
   <a href="https://github.com/eamelink/play-mockito">
    Mockito
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/mockito">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.mockito/play-mockito">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  Mockito is a mocking framework that tastes really good
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/qunit">
    [qunit]
   </a>
   <a href="https://github.com/irregular-at/play-qunit">
    QUnit
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/qunit">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.qunit/play-qunit">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  The QUnit module provides integration of JUnit Javascript tests with the Play! Framework.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/spocktests">
    [spocktests]
   </a>
   <a href="http://github.com/peterlundberg/play-spock-tests">
    Spock tests
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/spocktests">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Runs
  <a href="https://code.google.com/p/spock/">
   Spock
  </a>
  specifications and to write BDD style tests (still wrapped as  junit) with the expressive power of groovy.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/springtester">
    [springtester]
   </a>
   <a href="https://github.com/digiarnie/springtester">
    spring tester
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/springtester">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.springtester/play-springtester">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  Write tests that can auto-magically inject mocks (using Mockito) into Play applications wired up using the spring module.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/tests">
    [tests]
   </a>
   <a href="https://github.com/GuyMograbi/play_test_module">
    Alternative Test module
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/tests">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  The Test Module for Play!Framework helps you write tests quicker, is a cleaner and reusable manner.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/webdrive">
    [webdrive]
   </a>
   <a href="https://github.com/rkaippully/play-webdrive">
    Webdrive
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/webdrive">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.webdrive/play-webdrive">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  WebDrive module provides Selenium 2 testing support for Play framework
 </li>
</ul>
<h3>
 Translation
</h3>
<ul>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/i18ntools">
    [i18ntools]
   </a>
   <a href="http://github.com/naholyr/i18ntools">
    I18ntools
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/i18ntools">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  This module will add some tools to ease use of i18n in your Play! projects.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/messages">
    [messages]
   </a>
   <a href="https://github.com/huljas/play-messages">
    @messages
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/messages">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.messages/play-messages">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  Module messages provides a web based tool for managing your application’s localizations.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/nemrod">
    [nemrod]
   </a>
   <a href="https://github.com/sim51/logisima-play-neo4j">
    Nemrod
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/nemrod">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  This module helps to import and export translations from your application to a Nemrod instance automatically.
 </li>
 <li>
  <strong>
   [play-i18ned]
   <a href="https://github.com/phaus/play-i18ned">
    Play-i18ned
   </a>
  </strong>
  <a href="https://github.com/phaus/play-i18ned">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-no-red.svg?style=flat"/>
  </a>
  Converts default i18n files from an Excel Sheet and the other way around.
  <sup>
   &#9733 0, pushed 665 days ago
  </sup>
 </li>
</ul>
<h3>
 Misc
</h3>
<ul>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/bespin">
    [bespin]
   </a>
   <a href="http://github.com/erwan/playbespin">
    Bespin online editor
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/bespin">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Allows you to edit all the application sources directly in the browser using bespin, the web code editor.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/bhave">
    [bhave]
   </a>
   <a href="http://bhave.org/">
    Bhave
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/bhave">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Integrates with
  <a href="http://bhave.org/">
   bhave
  </a>
  , a web-based behavior driven development (BDD) framework, for web apps, done in a funky way!
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/cheese">
    [cheese]
   </a>
   <a href="https://github.com/lmcalpin/Play--Cheese">
    Cheese
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/cheese">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Simplified API for integration your application with the CheddarGetter subscription management service.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/cms">
    [cms]
   </a>
   <a href="http://code.google.com/p/play-cms/">
    Cms
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/cms">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  A very simple embedded CMS
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/cnm">
    [cnm]
   </a>
   <a href="http://github.com/oasits/play-content-negotiation">
    Content Negotiation
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/cnm">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Helps using content types which are not directly supported by default such as VCard and Atom/RSS feeds using annotations.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/externalconfig">
    [externalconfig]
   </a>
   <a href="https://github.com/rugbyhead/externalconfig">
    External Config
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/externalconfig">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Allows easy loading of external config / properties files. This allows for easy configuration of an app deployed in a war.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/featureflags">
    [featureflags]
   </a>
   <a href="http://code.google.com/p/play-featureflags">
    Feature Flags
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/featureflags">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Enables you to easily use flags in your application that you can switch ON and OFF at runtime, using an admin screen.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/googlecheckout">
    [googlecheckout]
   </a>
   <a href="https://github.com/jagregory/play-google-checkout">
    Google Checkout
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/googlecheckout">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  Enable your Play application to integrate with Google Checkout as a merchant.
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/gravatar">
    [gravatar]
   </a>
   <a href="https://github.com/mbarbieri/play-gravatar">
    Gravatar
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/gravatar">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.gravatar/play-gravatar">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  Integrate Gravatar into your Play application
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/hazelcast">
    [hazelcast]
   </a>
   <a href="https://github.com/marcuspocus/hazelcast">
    Hazelcast
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/hazelcast">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.hazelcast/play-hazelcast">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  Dropin replacement for EhCacheImpl or MemcachedImpl from Play
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/postmark">
    [postmark]
   </a>
   <a href="https://github.com/FrostDigital/play-postmark">
    Postmark
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/postmark">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  <a href="http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.postmark/play-postmark">
   <img alt="mavenized" src="http://img.shields.io/badge/ -mavenized-blue.svg?style=flat"/>
  </a>
  Postmark module provides easy integration with postmarkapp.com for handling outgoing emails
 </li>
 <li>
  <strong>
   <a href="http://www.playframework.com/modules/useragentcheck">
    [useragentcheck]
   </a>
   <a href="https://github.com/orefalo/play-useragentcheck">
    UserAgentCheck
   </a>
  </strong>
  <a href="http://www.playframework.com/modules/useragentcheck">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-yes-green.svg?style=flat"/>
  </a>
  UserAgentCheck displays a banner to notify users when their browser is outdated.
 </li>
 <li>
  <strong>
   <a href="http://sant0s.github.io/play1-chart/">
    [play1-chart]
   </a>
   <a href="https://github.com/sant0s/play1-chart">
    Play1-Chart
   </a>
  </strong>
  <a href="https://github.com/sant0s/play1-chart">
   <img alt="registered on playframework.com/modules" src="http://img.shields.io/badge/registered-no-red.svg?style=flat"/>
  </a>
  The Chart module allows for easy generation of chart images.
 </li>
</ul>
<h1>
 Tools
</h1>
<p>
 <em>
  You know a tool that every player should use?
  <a href="https://github.com/PerfectCarl/awesome-play1/edit/master/README.md">
   Tell us!
  </a>
 </em>
</p>
<h1>
 Resources
</h1>
<ul>
 <li>
  <a href="https://code.google.com/p/maven-play-plugin/wiki/MavenizedModules">
   Mavenized modules
  </a>
  and
  <a href="https://code.google.com/p/maven-play-plugin/wiki/Usage">
   how to use them
  </a>
 </li>
 <li>
  <a href="http://www.javabeat.net/using-controllers-in-play-framework/">
   Using Play's controller
  </a>
  with a nice roundup about caching, expiration and eTags
 </li>
 <li>
  Using
  <a href="https://github.com/greenlaw110">
   Luo
  </a>
  's
  <code>
   cache4
  </code>
  <a href="http://www.playframework.com/modules/rythm-1.0.0-20121210/integration#cache4">
   annotation
  </a>
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
 To the extent possible under law,
 <a href="https://github.com/PerfectCarl">
  PerfectCarl
 </a>
 has waived all copyright and related or neighboring rights to this work.
</p>
