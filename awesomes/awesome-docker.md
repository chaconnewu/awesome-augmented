<h1>
 Awesome Docker
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
 <a href="https://gitter.im/veggiemonk/awesome-docker?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge">
  <img alt="Join the chat at https://gitter.im/veggiemonk/awesome-docker" src="https://badges.gitter.im/Join%20Chat.svg"/>
 </a>
 <a href="https://travis-ci.org/veggiemonk/awesome-docker">
  <img alt="Build Status" src="https://travis-ci.org/veggiemonk/awesome-docker.svg?branch=master"/>
 </a>
</h1>
<blockquote>
 <p>
  A curated list of Docker resources and projects
  Inspired by
  <a href="https://github.com/sindresorhus">
   @sindresorhus
  </a>
  '
  <a href="https://github.com/sindresorhus/awesome">
   awesome
  </a>
  and improved by these
  <strong>
   <a href="https://github.com/veggiemonk/awesome-docker/graphs/contributors">
    amazing contributors
   </a>
  </strong>
  .
 </p>
</blockquote>
<p>
 It's now a github project because it's considerably easier for other people to edit, fix and expand on Docker using Github. Just click
 <a href="https://github.com/veggiemonk/awesome-docker/edit/master/README.md">
  README.md
 </a>
 to submit a
 <a href="https://github.com/veggiemonk/awesome-docker/edit/master/README.md">
  pull request
 </a>
 .
If this list is not complete, you can
 <a href="https://github.com/veggiemonk/awesome-docker/edit/master/README.md">
  contribute
 </a>
 to make it so.
</p>
<blockquote>
 <p>
  <strong>
   Please
  </strong>
  , help organize these resources so that they are
  <em>
   easy to find
  </em>
  and
  <em>
   understand
  </em>
  for new comers. See how to
  <strong>
   <a href="https://github.com/veggiemonk/awesome-docker/blob/master/CONTRIBUTING.md">
    Contribute
   </a>
  </strong>
  for tips!
 </p>
</blockquote>
<h4>
 <em>
  If you see a link here that is not (any longer) a good fit, you can fix it by submitting a
  <a href="https://github.com/veggiemonk/awesome-docker/edit/master/README.md">
   pull request
  </a>
  to improve this file. Thank you!
 </em>
</h4>
<p>
 The creators and maintainers of this list do not receive and should not receive any form of payment to accept a change made by any contributor. The goal of this repo is to index articles, learning materials and projects, not to advertise for profit.
 <strong>
  All pull requests are merged by default
 </strong>
 and removed if inappropriate or unavailable, or fixed when necessary.
</p>
<p>
 All the links are monitored and tested with
 <a href="https://github.com/dkhamsing/awesome_bot">
  awesome_bot
 </a>
 made by
 <a href="https://github.com/dkhamsing">
  @dkhamsing
 </a>
</p>
<h1>
 What is Docker ?
</h1>
<blockquote>
 <p>
  Docker is an open platform for developers and sysadmins to build, ship, and run distributed applications. Consisting of Docker Engine, a portable, lightweight runtime and packaging tool, and Docker Hub, a cloud service for sharing applications and automating workflows, Docker enables apps to be quickly assembled from components and eliminates the friction between development, QA, and production environments. As a result, IT can ship faster and run the same app, unchanged, on laptops, data center VMs, and any cloud.
 </p>
</blockquote>
<p>
 <em>
  Source:
 </em>
 <a href="https://www.docker.com/what-docker">
  What is Docker
 </a>
</p>
<h1>
 Where to start ?
</h1>
<ul>
 <li>
  <a href="https://docs.docker.com/mac/">
   10-minute Interactive Tutorial
  </a>
 </li>
 <li>
  <a href="http://training.docker.com/">
   Docker Training
  </a>
 </li>
 <li>
  Read this complete article:
  <a href="http://etherealmind.com/basics-docker-containers-hypervisors-coreos/">
   Basics – Docker, Containers, Hypervisors, CoreOS
  </a>
 </li>
 <li>
  Watch the video:
  <a href="https://www.youtube.com/watch?v=FdkNAjjO5yQ">
   Docker for Developers
  </a>
  (54:26) by
  <a href="https://github.com/jpetazzo">
   @jpetazzo
  </a>
 </li>
 <li>
  <a href="https://github.com/odewahn/docker-jumpstart/">
   Docker Jumpstart
  </a>
  : a quick introduction
 </li>
 <li>
  <a href="http://prakhar.me/docker-curriculum/">
   Docker Curriculum
  </a>
  : A comprehensive tutorial for getting started with Docker. Teaches how to use Docker and deploy dockerized apps on AWS with Elastic Beanstalk and Elastic Container Service.
 </li>
 <li>
  <a href="docker-cheat-sheet#installation">
   Install Docker on your machine
  </a>
  and play with a few
  <a href="#useful-images">
   Useful Images
  </a>
 </li>
 <li>
  Try
  <a href="http://panamax.io/">
   Panamax: Docker Management for Humans
  </a>
  It will install a CoreOS VM with VirtualBox and has nice front end
 </li>
 <li>
  <a href="https://www.docker.com/products/docker-toolbox">
   Install Docker Toolbox
  </a>
  Docker Toolbox is an installer to quickly and easily install and setup a Docker environment on your computer. Available for both Windows and Mac, the Toolbox installs Docker Client, Machine, Compose (Mac only), Kitematic and VirtualBox.
 </li>
 <li>
  Check out:
  <a href="https://github.com/wsargent/docker-cheat-sheet">
   Docker Cheat Sheet
  </a>
  <sup>
   &#9733 5953, pushed 6 days ago
  </sup>
  by
  <a href="https://github.com/wsargent">
   @wsargent
  </a>
  <strong>
   MUST SEE
  </strong>
 </li>
 <li>
  <a href="http://project-webdev.blogspot.de">
   Project Web Dev
  </a>
  : (Article series) How to create your own website based on Docker
 </li>
 <li>
  <a href="https://blog.jessfraz.com/post/docker-containers-on-the-desktop/">
   Docker Containers on the desktop
  </a>
  by
  <a href="https://github.com/jfrazelle">
   @jfrazelle
  </a>
  ) The
  <strong>
   funniest way
  </strong>
  to
learn
about docker! (Tips: checkout her
  <a href="https://github.com/jfrazelle/dotfiles">
   dotfiles
  </a>
  and her
  <a href="https://github.com/jfrazelle/dockerfiles">
   dockerfiles
  </a>
  )
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=1qlLUf7KtAw">
   Container Hacks and Fun Images
  </a>
  by
  <a href="https://github.com/jfrazelle">
   @jfrazelle
  </a>
  @ DockerCon 2015
  <strong>
   MUST WATCH VIDEO
  </strong>
  (38:50)
 </li>
 <li>
  <a href="https://github.com/dwyl/learn-docker">
   Learn Docker
  </a>
  <sup>
   &#9733 29, pushed 259 days ago
  </sup>
  Full environment set up, screenshots, step-by-step tutorial and more resources (video, articles, cheat sheets) by
  <a href="https://github.com/dwyl">
   @dwyl
  </a>
 </li>
 <li>
  <a href="http://docker-saigon.github.io/post/Docker-Caveats/">
   Docker Caveats
  </a>
  What You Should Know About Running Docker In Production (written 11 APRIL 2016)
  <strong>
   MUST SEE
  </strong>
 </li>
</ul>
<h1>
 MENU
</h1>
<ul>
 <li>
  <a href="#what-is-docker-">
   What is Docker ?
  </a>
 </li>
 <li>
  <a href="#where-to-start-">
   Where to start ?
  </a>
 </li>
 <li>
  <a href="#menu">
   MENU
  </a>
 </li>
 <li>
  <a href="#useful-articles">
   Useful Articles
  </a>
  <ul>
   <li>
    <a href="#main-resources">
     Main Resources
    </a>
   </li>
   <li>
    <a href="#general-articles">
     General Articles
    </a>
   </li>
   <li>
    <a href="#deep-dive">
     Deep Dive
    </a>
   </li>
   <li>
    <a href="#networking">
     Networking
    </a>
   </li>
   <li>
    <a href="#metal">
     Metal
    </a>
   </li>
   <li>
    <a href="#multi-server">
     Multi-Server
    </a>
   </li>
   <li>
    <a href="#cloud-infrastructure">
     Cloud Infrastructure
    </a>
   </li>
   <li>
    <a href="#good-tips">
     Good Tips
    </a>
   </li>
   <li>
    <a href="#newsletter">
     Newsletter
    </a>
   </li>
   <li>
    <a href="#continuous-integration">
     Continuous Integration
    </a>
   </li>
   <li>
    <a href="#optimizing-images">
     Optimizing Images
    </a>
   </li>
   <li>
    <a href="#service-discovery">
     Service Discovery
    </a>
   </li>
   <li>
    <a href="#security">
     Security
    </a>
   </li>
   <li>
    <a href="#performances">
     Performances
    </a>
   </li>
   <li>
    <a href="#raspberry-pi--arm">
     Raspberry Pi & ARM
    </a>
   </li>
   <li>
    <a href="#other">
     Other
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#books">
   Books
  </a>
 </li>
 <li>
  <a href="#tools">
   Tools
  </a>
  <ul>
   <li>
    <a href="#terminal-user-interface">
     Terminal User Interface
    </a>
   </li>
   <li>
    <a href="#dev-tools">
     Dev Tools
    </a>
   </li>
   <li>
    <a href="#continuous-integration--continuous-delivery">
     Continuous Integration / Continuous Delivery
    </a>
   </li>
   <li>
    <a href="#deployment">
     Deployment
    </a>
   </li>
   <li>
    <a href="#hosting-for-repositories-registries">
     Hosting for repositories (registries)
    </a>
   </li>
   <li>
    <a href="#hosting-for-containers">
     Hosting for containers
    </a>
   </li>
   <li>
    <a href="#reverse-proxy">
     Reverse Proxy
    </a>
   </li>
   <li>
    <a href="#web-interface">
     Web Interface
    </a>
   </li>
   <li>
    <a href="#local-container-manager">
     Local Container Manager
    </a>
   </li>
   <li>
    <a href="#volume-management-and-plugins">
     Volume management and plugins
    </a>
   </li>
   <li>
    <a href="#useful-images">
     Useful Images
    </a>
   </li>
   <li>
    <a href="#dockerfile">
     Dockerfile
    </a>
   </li>
   <li>
    <a href="#storing-images">
     Storing Images
    </a>
   </li>
   <li>
    <a href="#monitoring">
     Monitoring
    </a>
   </li>
   <li>
    <a href="#networking">
     Networking
    </a>
   </li>
   <li>
    <a href="#logging">
     Logging
    </a>
   </li>
   <li>
    <a href="#deployment-and-infrastructure">
     Deployment and Infrastructure
    </a>
   </li>
   <li>
    <a href="#paas">
     PaaS
    </a>
   </li>
   <li>
    <a href="#remote-container-manager--orchestration">
     Remote Container Manager / Orchestration
    </a>
   </li>
   <li>
    <a href="#security">
     Security
    </a>
   </li>
   <li>
    <a href="#service-discovery">
     Service Discovery
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#slides">
   Slides
  </a>
 </li>
 <li>
  <a href="#videos">
   Videos
  </a>
  <ul>
   <li>
    <a href="#main-account">
     Main Account
    </a>
   </li>
   <li>
    <a href="#useful-videos">
     Useful videos
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#interesting-twitter-accounts">
   Interesting Twitter Accounts
  </a>
  <ul>
   <li>
    <a href="#people">
     People
    </a>
   </li>
  </ul>
 </li>
</ul>
<h1>
 Useful Articles
</h1>
<h2>
 Main Resources
</h2>
<ul>
 <li>
  <a href="https://blog.docker.com/docker-weekly-archives/">
   Docker Weekly
  </a>
  Huge resource
 </li>
 <li>
  <a href="https://github.com/wsargent/docker-cheat-sheet">
   Docker Cheat Sheet
  </a>
  by
  <a href="https://github.com/wsargent">
   @wsargent
  </a>
  <strong>
   MUST SEE
  </strong>
 </li>
 <li>
  <a href="https://labs.ctl.io/category/docker/">
   CenturyLink Labs
  </a>
 </li>
 <li>
  <a href="http://www.nkode.io/2014/08/24/valuable-docker-links.html">
   Valuable Docker Links
  </a>
  Very complete
 </li>
 <li>
  <a href="https://www.mindmeister.com/389671722/docker-ecosystem">
   Docker Ecosystem
  </a>
  (Mind Map)
  <strong>
   MUST SEE
  </strong>
 </li>
 <li>
  <a href="http://comp.photo777.org/wp-content/uploads/2015/09/Docker-ecosystem-8.5.1.pdf">
   Docker Ecosystem
  </a>
  (PDF)
  <strong>
   MUST SEE
  </strong>
  find it on
  <a href="http://comp.photo777.org/docker-ecosystem/">
   blog
  </a>
  by Bryzgalov Peter.
 </li>
 <li>
  <a href="https://blog.jessfraz.com/">
   Blog
  </a>
  of
  <a href="https://github.com/jfrazelle">
   @frazelledazzell
  </a>
 </li>
 <li>
  <a href="http://jpetazzo.github.io/">
   Blog
  </a>
  of
  <a href="https://github.com/jpetazzo">
   @jpetazzo
  </a>
 </li>
 <li>
  <a href="http://progrium.com/blog/">
   Blog
  </a>
  of
  <a href="https://github.com/progrium">
   @progrium
  </a>
 </li>
 <li>
  <a href="http://jasonwilder.com/">
   Blog
  </a>
  of
  <a href="https://github.com/jwilder">
   @jwilder
  </a>
 </li>
 <li>
  <a href="http://crosbymichael.com/">
   Blog
  </a>
  of
  <a href="https://github.com/crosbymichael">
   @crosbymichael
  </a>
 </li>
 <li>
  <a href="http://gliderlabs.com/blog/">
   Blog
  </a>
  of
  <a href="https://github.com/gliderlabs">
   @gliderlabs
  </a>
 </li>
 <li>
  <a href="http://sebgoa.blogspot.be/">
   Blog
  </a>
  of
  <a href="https://twitter.com/sebgoa">
   @sebgoa
  </a>
 </li>
 <li>
  <a href="https://blog.codeship.com/">
   Blog
  </a>
  of
  <a href="https://github.com/codeship">
   @codeship
  </a>
 </li>
 <li>
  <a href="https://www.digitalocean.com/community/search?q=docker&type=tutorials">
   Digital Ocean Community
  </a>
 </li>
 <li>
  <a href="http://container42.com/">
   Container42
  </a>
 </li>
 <li>
  <a href="http://container-solutions.com/blog/">
   Container solutions
  </a>
 </li>
 <li>
  <a href="http://dockone.io/">
   DockerOne
  </a>
  Docker Community (in Chinese) by
  <a href="http://dockone.io/people/%E6%9D%8E%E9%A2%96%E6%9D%B0">
   @LiYingJie
  </a>
 </li>
 <li>
  <a href="http://project-webdev.blogspot.de">
   Project Web Dev
  </a>
  : (Article series) How to create your own website based on Docker
 </li>
 <li>
  <a href="http://www.rightscale.com/blog/cloud-management-best-practices/docker-vs-vms-combining-both-cloud-portability-nirvana">
   Docker vs. VMs? Combining Both for Cloud Portability Nirvana
  </a>
 </li>
 <li>
  <a href="https://blog.jessfraz.com/post/docker-containers-on-the-desktop/">
   Docker Containers on the desktop
  </a>
  by
  <a href="https://github.com/jfrazelle">
   @jfrazelle
  </a>
  The
  <strong>
   funniest way
  </strong>
  to learn
about docker! (Tips: checkout her
  <a href="https://github.com/jfrazelle/dotfiles">
   dotfiles
  </a>
  and her
  <a href="https://github.com/jfrazelle/dockerfiles">
   dockerfiles
  </a>
  ))
 </li>
 <li>
  <a href="https://github.com/Friz-zy/awesome-linux-containers">
   Awesome Linux Container
  </a>
  <sup>
   &#9733 85, pushed 46 days ago
  </sup>
  more general about container than this repo, by
  <a href="https://github.com/Friz-zy">
   @Friz-zy
  </a>
  .
 </li>
</ul>
<h2>
 General Articles
</h2>
<ul>
 <li>
  <a href="https://serversforhackers.com/getting-started-with-docker/">
   Getting Started with Docker
  </a>
  by
  <a href="https://github.com/fideloper">
   @fideloper
  </a>
  --
  <a href="https://serversforhackers.com/editions/">
   Servers For Hackers
  </a>
  is valuable resource. At some point, every programmer finds themselves needing to know their way around a server.
 </li>
 <li>
  <a href="http://axibase.com/docker-monitoring/">
   What is Docker and how do you monitor it?
  </a>
 </li>
 <li>
  <a href="https://www.viget.com/articles/how-to-use-docker-on-os-x-the-missing-guide">
   How to Use Docker on OS X: The Missing Guide
  </a>
 </li>
 <li>
  <a href="https://ro14nd.de/Docker-for-Developers">
   Docker for (Java) Developers
  </a>
 </li>
 <li>
  <a href="https://www.nginx.com/blog/deploying-nginx-nginx-plus-docker/">
   Deploying NGINX with Docker
  </a>
 </li>
 <li>
  <a href="http://hokstad.com/docker/patterns">
   Eight Docker Development Patterns
  </a>
 </li>
 <li>
  <a href="https://allenan.com/docker-rails-dev-environment-for-osx/">
   Rails Development Environment for OS X using Docker
  </a>
 </li>
 <li>
  <a href="https://dzone.com/articles/logging-docker-what-you-need">
   Logging on Docker: What You Need to Know
  </a>
  + see the
  <a href="https://vimeo.com/123341629">
   video
  </a>
  (~50min)
 </li>
 <li>
  <a href="http://rancher.com/comparing-monitoring-options-for-docker-deployments/">
   Comparing Five Monitoring Options for Docker
  </a>
 </li>
 <li>
  <a href="http://dockermeetupsinbordeaux.github.io/docker-compose/data-container/2015/03/01/minimalistic-docker-data-container.html">
   Minimalistic data-only container for Docker Compose
  </a>
  (Written Mar 1, 2015)
 </li>
 <li>
  <a href="http://container-solutions.com/running-docker-containers-with-systemd/">
   Running Docker Containers with Systemd
  </a>
 </li>
 <li>
  <a href="https://realpython.com/blog/python/dockerizing-flask-with-compose-and-machine-from-localhost-to-the-cloud/">
   Dockerizing Flask With Compose and Machine - From Localhost to the Cloud
  </a>
  --
  <a href="https://github.com/realpython/orchestrating-docker">
   GitHub
  </a>
  Learn how to deploy an application using Docker Compose and Docker Machine (written 17 April 2015)
 </li>
 <li>
  <a href="https://medium.com/iron-io-blog/why-and-how-to-use-docker-for-development-a156c1de3b24">
   Why and How to use Docker for Development
  </a>
  (written 28 APR 2015)
 </li>
 <li>
  <a href="http://nathanleclaire.com/blog/2015/04/27/automating-docker-logging-elasticsearch-logstash-kibana-and-logspout/">
   Automating Docker Logging: ElasticSearch, Logstash, Kibana, and Logspout
  </a>
  (written 27 APR 2015)
 </li>
 <li>
  <a href="http://oliverguenther.de/2015/05/docker-host-volume-synchronization/">
   Docker Host Volume Synchronization
  </a>
  (written 1 JUN 2015)
 </li>
 <li>
  <a href="http://devbandit.com/2015/05/29/vagrant-and-docker.html">
   Multi-Service Local Development Environment with Vagrant and Docker
  </a>
  (written 29 MAY 2015)
 </li>
 <li>
  <a href="https://developer.rackspace.com/blog/dev-to-deploy-with-docker-machine-and-compose/">
   From Local Development to Remote Deployment with Docker Machine and Compose
  </a>
  (written 2 JUL 2015)
 </li>
 <li>
  <a href="http://delftswa.github.io/chapters/docker/index.html">
   Docker: Build, Ship and Run Any App, Anywhere
  </a>
  by
  <a href="https://github.com/MartijnDwars">
   Martijn Dwars
  </a>
  ,
  <a href="https://github.com/wrvangeest">
   Wiebe van Geest
  </a>
  ,
  <a href="https://github.com/gewoonrik">
   Rik Nijessen
  </a>
  , and
  <a href="https://github.com/RickWieman">
   Rick Wieman
  </a>
  from
  <a href="http://www.tudelft.nl/">
   Delft University of Technology
  </a>
  (written 2 JUL 2015)
 </li>
 <li>
  <a href="http://thenewstack.io/joining-the-docker-ship-and-go/">
   Joining the Docker Ship
  </a>
  Learn how to contribute to docker (written 9 JUL 2015)
 </li>
 <li>
  <a href="https://github.com/gesellix/pipeline-with-gradle-and-docker/blob/master/README.md">
   Continuous Deployment with Gradle and Docker
  </a>
  Describes a complete pipeline from source to production deploy (includes a complete Spring Boot example project) by
  <a href="https://github.com/gesellix">
   @gesellix
  </a>
 </li>
 <li>
  <a href="https://www.computer.org/cms/Computer.org/ComputingNow/issues/2015/09/mcd2015030024.pdf">
   Containerization and the PaaS Cloud
  </a>
  -- This article discusses the requirements that arise from having to facilitate applications through distributed multicloud platforms.
 </li>
 <li>
  <a href="https://medium.com/@rdsubhas/docker-for-development-common-problems-and-solutions-95b25cae41eb">
   Docker for Development: Common Problems and Solutions
  </a>
  by
  <a href="https://github.com/rdsubhas">
   @rdsubhas
  </a>
 </li>
 <li>
  <a href="https://www.datadoghq.com/docker-adoption/">
   Docker Adoption Data
  </a>
  A study by Datadog on the real world Docker usage stastics and deployment patterns.
 </li>
 <li>
  <a href="https://www.datadoghq.com/blog/the-docker-monitoring-problem/">
   How to monitor Docker
  </a>
  (4-part series)
 </li>
 <li>
  <a href="http://nathanleclaire.com/blog/2015/11/10/using-ansible-with-docker-machine-to-bootstrap-host-nodes/">
   Using Ansible with Docker Machine to Bootstrap Host Nodes
  </a>
  by
  <a href="https://github.com/nathanleclaire">
   @nathanleclaire
  </a>
 </li>
 <li>
  <a href="https://www.oreilly.com/ideas/swarm-v-fleet-v-kubernetes-v-mesos">
   Swarm v. Fleet v. Kubernetes v. Mesos
  </a>
  Comparing different orchestration tools. (written OCT 2015)
 </li>
 <li>
  <a href="https://blog.codeship.com/the-shortlist-of-docker-hosting">
   The Shortlist of Docker Hosting
  </a>
  There are so many specialized and optimized Docker hosting services available, it’s high time for a review to see what’s on offer (by Chris Ward).
 </li>
</ul>
<h2>
 Deep Dive
</h2>
<ul>
 <li>
  <a href="http://crosbymichael.com/creating-containers-part-1.html">
   Creating containers - Part 1
  </a>
  This is part one of a series of blog posts detailing how docker creates containers. By
  <a href="https://github.com/crosbymichael">
   @crosbymichael
  </a>
 </li>
 <li>
  <a href="http://container42.com/2014/11/18/data-only-container-madness/">
   Data-only container madness
  </a>
 </li>
</ul>
<h2>
 Networking
</h2>
<ul>
 <li>
  <a href="https://www.weave.works/using-docker-machine-with-weave-0-10/">
   Using Docker Machine with Weave 0.10
  </a>
  (written 22 APR 2015)
 </li>
 <li>
  <a href="https://blog.jessfraz.com/post/routing-traffic-through-tor-docker-container/">
   How to Route Traffic through a Tor Docker container
  </a>
  by
  <a href="https://github.com/jfrazelle">
   @jfrazelle
  </a>
  (writtent 20 JUN 2015)
 </li>
</ul>
<h2>
 Metal
</h2>
<ul>
 <li>
  <a href="http://blog.bigstep.com/big-data-performance/use-docker-full-metal-cloud/">
   How to use Docker on Full Metal
  </a>
 </li>
</ul>
<h2>
 Multi-Server
</h2>
<ul>
 <li>
  <a href="http://shortcircuit.net.au/~prologic/blog/article/2015/03/24/a-docker-based-mini-paas/">
   A Docker based mini-PaaS
  </a>
  by
  <a href="https://github.com/prologic">
   @prologic
  </a>
 </li>
 <li>
  <a href="https://www.blockbridge.com/a-scalable-web-services-demo-using-docker-swarm-compose-and-blockbridge/">
   A multi-host scalable web services demo using Docker swarm, Docker compose, NGINX, and Blockbridge
  </a>
 </li>
</ul>
<h2>
 Cloud Infrastructure
</h2>
<ul>
 <li>
  <a href="https://blog.tutum.co/2015/04/29/cloud-infrastructure-automation-for-docker-nodes/">
   Cloud Infrastructure Automation for Docker Nodes
  </a>
 </li>
</ul>
<h2>
 Good Tips
</h2>
<ul>
 <li>
  <a href="https://csabapalfi.github.io/random-docker-tips/">
   24 random docker tips
  </a>
  by
  <a href="https://github.com/csabapalfi">
   @csabapalfi
  </a>
 </li>
 <li>
  <a href="http://fabiorehm.com/blog/2014/09/11/running-gui-apps-with-docker/">
   GUI Apps with Docker
  </a>
  by
  <a href="https://github.com/fgrehm">
   @fgrehm
  </a>
 </li>
 <li>
  <a href="http://jasonwilder.com/blog/2014/03/25/automated-nginx-reverse-proxy-for-docker/">
   Automated Nginx Reverse Proxy for Docker
  </a>
  by
  <a href="https://github.com/jwilder">
   @jwilder
  </a>
 </li>
 <li>
  <a href="https://ro14nd.de/NSEnter-with-Boot2Docker">
   Using NSEnter with Boot2Docker
  </a>
 </li>
 <li>
  <a href="http://jasonwilder.com/blog/2014/10/13/a-simple-way-to-dockerize-applications/">
   A Simple Way to Dockerize Applications
  </a>
  by
  <a href="https://github.com/jwilder">
   @jwilder
  </a>
 </li>
 <li>
  <a href="http://jonathan.bergknoff.com/journal/building-good-docker-images">
   Building good docker images
  </a>
  by
  <a href="https://github.com/jbergknoff">
   @jbergknoff
  </a>
 </li>
 <li>
  <a href="http://www.slideshare.net/rightscale/docker-meetup-40826948">
   10 Things Not To Forget Before Deploying Docker In Production
  </a>
 </li>
 <li>
  <a href="http://backdrift.org/docker-cifs-howto-mount-cifs-volume-docker-container">
   Docker CIFS – How to Mount CIFS as a Docker Volume
  </a>
 </li>
 <li>
  <a href="https://blog.danivovich.com/2015/07/09/nginx-proxy-for-docker-containers/">
   Nginx Proxy for Docker
  </a>
  (written 9 JUL 2015)
 </li>
 <li>
  <a href="http://brunorocha.org/python/dealing-with-linked-containers-dependency-in-docker-compose.html">
   Dealing with linked containers dependency in docker-compose
  </a>
  by
  <a href="https://github.com/rochacbruno">
   @rochacbruno
  </a>
 </li>
 <li>
  <a href="http://www.mervine.net/notes/docker-tips">
   Docker Tips
  </a>
  by
  <a href="https://github.com/jmervine">
   @jmervine
  </a>
 </li>
 <li>
  <a href="http://toedter.com/2015/05/11/docker-on-windows-behind-a-firewall/">
   Docker on Windows behind a firewall
  </a>
  by
  <a href="https://twitter.com/kaitoedter">
   @kaitoedter
  </a>
 </li>
 <li>
  <a href="http://blog.cloud66.com/pulling-git-into-a-docker-image-without-leaving-ssh-keys-behind/">
   Pulling Git into a Docker image without leaving SSH keys behind
  </a>
  by
  <a href="https://github.com/khash">
   @khash
  </a>
 </li>
 <li>
  <a href="http://www.slideshare.net/raychaser/6-million-ways-to-log-in-docker-nyc-docker-meetup-12172014">
   6 Million Ways To Log In Docker
  </a>
  by
  <a href="https://twitter.com/raychaser">
   @raychaser
  </a>
 </li>
 <li>
  <a href="http://jrruethe.github.io/blog/2015/09/20/dockerfile-generator/">
   Dockerfile Generator
  </a>
  (ruby script)
 </li>
 <li>
  <a href="http://conferences.oreilly.com/strata/big-data-conference-ca-2015/public/schedule/detail/38521">
   Running Production Hadoop Clusters in Docker Containers
  </a>
 </li>
 <li>
  <a href="http://www.smartjava.org/content/10-practical-docker-tips-day-day-docker-usage">
   10 practical docker tips
  </a>
  (Dec 2015) by
  <a href="https://github.com/josdirksen">
   @josdirksen
  </a>
 </li>
 <li>
  <a href="http://k8s.info/cs.html">
   Kubernetes Cheatsheet
  </a>
  - A great resource for managing your Kubernetes installation
 </li>
 <li>
  <a href="http://docs.projectatomic.io/container-best-practices/">
   Container Best Practices
  </a>
  - Red Hat's Project Atomic created a Container Best Practices guide which applies to everything and is updated regurlary.
 </li>
</ul>
<h2>
 Newsletter
</h2>
<ul>
 <li>
  <a href="https://www.docker.com/">
   Docker Team
  </a>
 </li>
 <li>
  <a href="https://labs.ctl.io/">
   CenturyLink Labs
  </a>
 </li>
 <li>
  <a href="https://dashboard.tutum.co/accounts/login/">
   Tutum
  </a>
 </li>
 <li>
  <a href="http://www.devopsweekly.com">
   DevOps Weekly
  </a>
 </li>
 <li>
  <a href="http://blog.shippable.com/">
   Shippable
  </a>
 </li>
 <li>
  <a href="http://webopsweekly.com/">
   WebOps weekly
  </a>
 </li>
</ul>
<h2>
 Continuous Integration
</h2>
<ul>
 <li>
  <a href="http://ariya.ofilabs.com/2014/12/docker-and-phoenix-how-to-make-your-continuous-integration-more-awesome.html">
   Docker and Phoenix: How to Make Your Continuous Integration More Awesome
  </a>
 </li>
</ul>
<h2>
 Optimizing Images
</h2>
<ul>
 <li>
  <a href="http://blog.xebia.com/create-the-smallest-possible-docker-container/">
   Create the smallest possible Docker container
  </a>
 </li>
 <li>
  <a href="https://blog.tutum.co/2014/04/10/creating-a-docker-image-from-your-code/">
   Creating a Docker image from your code
  </a>
 </li>
 <li>
  <a href="https://www.ctl.io/developers/blog/post/optimizing-docker-images/">
   Optimizing Docker Images
  </a>
 </li>
 <li>
  <a href="https://blog.tutum.co/2014/10/22/how-to-optimize-your-dockerfile/">
   How to Optimize Your Dockerfile
  </a>
  by
  <a href="https://github.com/tutumcloud">
   @tutumcloud
  </a>
 </li>
 <li>
  <a href="https://medium.com/@kelseyhightower/optimizing-docker-images-for-static-binaries-b5696e26eb07">
   Building Docker Images for Static Go Binaries
  </a>
  by
  <a href="https://github.com/kelseyhightower">
   @kelseyhightower
  </a>
 </li>
 <li>
  <a href="http://jasonwilder.com/blog/2014/08/19/squashing-docker-images/">
   Squashing Docker Images
  </a>
  by
  <a href="https://github.com/jwilder">
   @jwilder
  </a>
 </li>
 <li>
  <a href="http://www.davidmkerr.com/2014/08/dockerfile-golf-or-optimizing-docker.html">
   Dockerfile Golf (or optimizing the Docker build process)
  </a>
 </li>
 <li>
  <a href="https://imagelayers.io/">
   ImageLayers
  </a>
  Visualize Docker images and the layers that compose them.
 </li>
 <li>
  <a href="https://github.com/cloudimmunity/docker-slim">
   DockerSlim
  </a>
  <sup>
   &#9733 499, pushed 16 days ago
  </sup>
  shrinks fat Docker images creating the smallest possible images.
 </li>
 <li>
  <a href="https://github.com/djosephsen/skinnywhale">
   SkinnyWhale
  </a>
  <sup>
   &#9733 145, pushed 189 days ago
  </sup>
  Skinnywhale helps you make smaller (as in megabytes) Docker containers.
 </li>
</ul>
<h2>
 Service Discovery
</h2>
<ul>
 <li>
  <a href="https://github.com/progrium">
   @progrium
  </a>
  Service Discovery articles series:
  <ul>
   <li>
    <a href="http://progrium.com/blog/2014/08/20/consul-service-discovery-with-docker/">
     Consul Service Discovery with Docker
    </a>
   </li>
   <li>
    <a href="http://progrium.com/blog/2014/07/29/understanding-modern-service-discovery-with-docker/">
     Understanding Modern Service Discovery with Docker
    </a>
   </li>
   <li>
    <a href="http://progrium.com/blog/2014/09/10/automatic-docker-service-announcement-with-registrator/">
     Automatic Docker Service Announcement with Registrator
    </a>
   </li>
  </ul>
 </li>
</ul>
<h2>
 Security
</h2>
<ul>
 <li>
  <a href="http://www.projectatomic.io/docs/docker-and-selinux/">
   Docker and SELinux
  </a>
 </li>
 <li>
  <a href="https://opensource.com/business/14/9/security-for-docker">
   Bringing new security features to Docker
  </a>
 </li>
 <li>
  <a href="https://github.com/GDSSecurity/Docker-Secure-Deployment-Guidelines">
   Docker Secure Deployment Guidelines
  </a>
  <sup>
   &#9733 309, pushed 453 days ago
  </sup>
 </li>
 <li>
  <a href="http://linux-audit.com/tag/docker/">
   Security Best Practices for Building Docker Images
  </a>
 </li>
 <li>
  <a href="http://fr.slideshare.net/MichaelBoelen/docker-security-are-your-containers-tightly-secured-to-the-ship">
   Docker Security: Are Your Containers Tightly Secured to the Ship? SlideShare
  </a>
 </li>
 <li>
  <a href="https://opensource.com/business/15/3/docker-security-tuning">
   Tuning Docker with the newest security enhancements
  </a>
 </li>
 <li>
  <a href="https://cisofy.com/lynis/">
   Lynis is an open source security auditing tool including Docker auditing
  </a>
 </li>
 <li>
  <a href="https://blog.docker.com/2015/05/understanding-docker-security-and-best-practices/">
   Understanding Docker security and best practices
  </a>
  (written 5 MAY 2015)
 </li>
 <li>
  <a href="https://github.com/konstruktoid/Docker/blob/master/Security/CheatSheet.adoc">
   Docker Security Cheat Sheet
  </a>
 </li>
 <li>
  <a href="https://github.com/docker-library/official-images/issues/1448">
   How CVE's are handled on Offical Docker Images
  </a>
 </li>
 <li>
  <a href="https://www.blockbridge.com/improving-docker-security-with-authenticated-volumes/">
   Improving Docker Security with Authenticated Volumes
  </a>
 </li>
</ul>
<h2>
 Performances
</h2>
<ul>
 <li>
  <a href="http://developerblog.redhat.com/2014/08/19/performance-analysis-docker-red-hat-enterprise-linux-7/">
   Performance Analysis of Docker on Red Hat Enterprise Linux 7
  </a>
 </li>
 <li>
  <a href="http://srivaths.blogspot.fr/2014/08/distrubuted-jmeter-testing-using-docker.html?m=1">
   Distrubuted JMeter testing using Docker
  </a>
 </li>
 <li>
  <a href="http://www.breakage.org/2014/09/03/nsinit-per-container-resource-monitoring-of-docker-containers-on-rhelfedora/">
   nsinit: per-container resource monitoring of Docker containers on RHEL/Fedora
  </a>
 </li>
</ul>
<h2>
 Raspberry Pi & ARM
</h2>
<ul>
 <li>
  <a href="https://resin.io/">
   git push docker containers to linux devices
  </a>
  Modern DevOps for IoT, leveraging git and Docker.
 </li>
 <li>
  <a href="http://blog.hypriot.com/">
   Docker Pirates ARMed with explosive stuff
  </a>
  Huge resource on clustering, swarm, docker, pre-installed image for SD card on Raspberry Pi
 </li>
 <li>
  <a href="http://blog.xebia.com/docker-on-a-raspberry-pi/">
   Docker on Raspberry Pi
  </a>
 </li>
 <li>
  <a href="https://www.voxxed.com/blog/2015/04/fool-proof-recipe-docker-on-the-raspberry-pi/">
   Fool-Proof Recipe: Docker on the Raspberry Pi
  </a>
  Same article as above but more opinionated.
 </li>
 <li>
  <a href="http://blog.hypriot.com/post/heavily-armed-after-major-upgrade-raspberry-pi-with-docker-1-dot-5-0/">
   Raspberry Pi with Docker 1.5.0
  </a>
 </li>
 <li>
  <a href="http://matthewkwilliams.com/index.php/2015/03/21/swarming-raspberry-pi-part-1/">
   Swarming Raspberry Pi – Part 1
  </a>
 </li>
 <li>
  <a href="http://matthewkwilliams.com/index.php/2015/03/29/swarming-raspberry-pi-part-2-registry-mirror/">
   Swarming Raspberry Pi, Part 2: Registry & Mirror
  </a>
 </li>
 <li>
  <a href="http://matthewkwilliams.com/index.php/2015/04/03/swarming-raspberry-pi-docker-swarm-discovery-options/">
   Swarming Raspberry Pi: Docker Swarm Discovery Options
  </a>
 </li>
 <li>
  <a href="http://www.instructables.com/id/Uniform-Development-by-Docker-QEMU/">
   Uniform Development by Docker & QEMU
  </a>
 </li>
 <li>
  <a href="https://github.com/umiddelb/armhf/wiki/Get-Docker-up-and-running-on-the-RaspberryPi-%28ARMv6%29-in-three-steps">
   Get Docker up and running on the RaspberryPi in three steps
  </a>
 </li>
 <li>
  <a href="https://github.com/umiddelb/armhf/wiki/Installing,-running,-using-docker-on-armhf-(ARMv7)-devices">
   Installing, running, using Docker on armhf (ARMv7) devices
  </a>
 </li>
 <li>
  <a href="http://blog.loof.fr/2015/10/how-to-run-2500-webservers-on-raspberry.html">
   How to run 2500 webservers on a Raspberry Pi
  </a>
 </li>
</ul>
<h2>
 Other
</h2>
<ul>
 <li>
  Presentation: Docker and JBoss - the perfect combination
  <ul>
   <li>
    <a href="https://www.youtube.com/watch?v=4uQ6gR_xZhE">
     Vidéo
    </a>
   </li>
   <li>
    <a href="https://goldmann.pl/presentations/2014-vjbug-docker/">
     Slides
    </a>
   </li>
   <li>
    <a href="https://github.com/goldmann/goldmann.pl/tree/master/.presentations/2014-vjbug-docker/demos">
     Code source
    </a>
   </li>
  </ul>
 </li>
</ul>
<h1>
 Books
</h1>
<ul>
 <li>
  <a href="https://dockerbook.com/">
   Docker Book
  </a>
  by James Turnbul (
  <a href="https://twitter.com/kartar">
   @kartar
  </a>
  )
 </li>
 <li>
  <a href="http://shop.oreilly.com/product/0636920036791.do">
   Docker Cookbook
  </a>
  by Sébastien Goasguen (
  <a href="https://twitter.com/sebgoa">
   @sebgoa
  </a>
  ) (Publisher: O'Reilly)
 </li>
 <li>
  <a href="http://dockercookbook.github.io/">
   Docker Cookbook
  </a>
  by Neependra Khare (
  <a href="https://twitter.com/neependra">
   @neependra
  </a>
  ) (Publisher: Packt)
 </li>
 <li>
  <a href="https://www.manning.com/books/docker-in-action">
   Docker in Action
  </a>
  by Jeff Nickoloff (
  <a href="https://twitter.com/allingeek">
   @allingeek
  </a>
  )
 </li>
 <li>
  <a href="https://www.manning.com/books/docker-in-practice">
   Docker in Practice
  </a>
  by Ian Miell (
  <a href="https://github.com/ianmiell">
   @ianmiell
  </a>
  ) and Aidan Hobson Sayers (
  <a href="https://github.com/aidanhs">
   @aidanhs
  </a>
  ). ==>
  <a href="http://docker-in-practice.github.io/">
   Website
  </a>
 </li>
 <li>
  <a href="http://newrelic.com/docker-book">
   Docker Up & Running
  </a>
  by
  <a href="https://twitter.com/relistan">
   Karl Matthias
  </a>
  and
  <a href="https://twitter.com/spkane">
   Sean P. Kane
  </a>
 </li>
 <li>
  <a href="http://shop.oreilly.com/product/0636920035671.do">
   Using Docker
  </a>
  by Adrian Mouat (
  <a href="https://twitter.com/adrianmouat">
   @adrianmouat
  </a>
  ) (Publisher: O'Reilly)
 </li>
 <li>
  <a href="https://www.openshift.com/promotions/docker-security.html">
   Docker Security
  </a>
  by Adrian Mouat (
  <a href="https://twitter.com/adrianmouat">
   @adrianmouat
  </a>
  ) (Publisher: O'Reilly)
 </li>
 <li>
  <a href="http://www.bee42.com/dockerbook/">
   Docker: Container-Infrastruktur für Microservices
  </a>
  (German) by Peter Roßbach (
  <a href="https://twitter.com/PRossbach">
   @PRossbach
  </a>
  )
 </li>
 <li>
  <a href="https://www.casadocodigo.com.br/products/livro-docker">
   Containers com Docker do desenvolvimento à produção
  </a>
  (Portuguese) by Daniel Romero (
  <a href="https://twitter.com/infoslack">
   @infoslack
  </a>
  )
 </li>
 <li>
  <a href="https://www.amazon.cn/图书/dp/B014ETH1IG">
   Docker Container and Container Cloud
  </a>
  (Chinese) by
  <a href="https://twitter.com/resouer">
   Harry Zhang
  </a>
  & Jianbo Sun & Zhejiang University SEL Laboratory
 </li>
 <li>
  <a href="https://www.openshift.com/promotions/kubernetes.html">
   Kubernetes
  </a>
  by
  <a href="http://research.google.com/pubs/DavidRensin.html">
   David Rensin
  </a>
  (Publisher: O'Reilly)
 </li>
 <li>
  <a href="http://www.amazon.com/Docker-Production-Trenches-Joe-Johnston-ebook/dp/B0141W6KYC">
   Docker in Production: Lessons from the Trenches
  </a>
  by Joe Johnston (Author), John Fiedler (Author), Milos Gajdos (Author), Antoni Batchelli (Author), Justin Cormack (Author)
 </li>
</ul>
<h1>
 Tools
</h1>
<ul>
 <li>
  <a href="https://github.com/docker/docker">
   Docker
  </a>
  <sup>
   &#9733 30916, pushed 0 days ago
  </sup>
 </li>
 <li>
  <a href="https://hub.docker.com">
   Docker Images
  </a>
 </li>
 <li>
  <a href="https://github.com/docker/compose/">
   Docker Compose
  </a>
  (Define and run multi-container applications with Docker)
 </li>
 <li>
  <a href="https://github.com/docker/machine">
   Docker Machine
  </a>
  <sup>
   &#9733 3204, pushed 3 days ago
  </sup>
  (Machine management for a container-centric world)
 </li>
 <li>
  <a href="https://github.com/docker/distribution">
   Docker Registry
  </a>
  <sup>
   &#9733 2017, pushed 4 days ago
  </sup>
  (The Docker toolset to pack, ship, store, and deliver content)
 </li>
 <li>
  <a href="https://github.com/docker/swarm">
   Docker Swarm
  </a>
  <sup>
   &#9733 3658, pushed 2 days ago
  </sup>
  (Swarm: a Docker-native clustering system)
 </li>
</ul>
<h2>
 Terminal User Interface
</h2>
<ul>
 <li>
  <a href="https://github.com/TomasTomecek/sen">
   sen
  </a>
  <sup>
   &#9733 312, pushed 2 days ago
  </sup>
  - Terminal user interface for docker engine, by
  <a href="https://github.com/TomasTomecek">
   @TomasTomecek
  </a>
 </li>
 <li>
  <a href="https://github.com/j-bennet/wharfee">
   wharfee
  </a>
  <sup>
   &#9733 377, pushed 75 days ago
  </sup>
  - Autocompletion and syntax highlighting for Docker commands.) by
  <a href="https://github.com/j-bennet">
   @j-bennet
  </a>
 </li>
 <li>
  <a href="https://github.com/yadutaf/ctop">
   ctop
  </a>
  <sup>
   &#9733 129, pushed 24 days ago
  </sup>
  - A command line / text based Linux Containers monitoring tool that works just like you expect by
  <a href="https://github.com/yadutaf">
   @yadutaf
  </a>
 </li>
 <li>
  <a href="https://github.com/moncho/dry">
   dry
  </a>
  <sup>
   &#9733 93, pushed 3 days ago
  </sup>
  - An interactive CLI for Docker containers by
  <a href="https://github.com/moncho">
   @moncho
  </a>
 </li>
 <li>
  <a href="https://github.com/docker/dockercraft">
   dockercraft
  </a>
  <sup>
   &#9733 3640, pushed 7 days ago
  </sup>
  - Docker + Minecraft = Dockercraft by
  <a href="https://github.com/docker">
   @docker
  </a>
 </li>
</ul>
<h2>
 Dev Tools
</h2>
<ul>
 <li>
  <a href="https://github.com/Alexis-benoist/draw-compose">
   draw-compose
  </a>
  <sup>
   &#9733 12, pushed 17 days ago
  </sup>
  - Utility to draw a schema of a docker compose by
  <a href="https://github.com/Alexis-benoist">
   @Alexis-benoist
  </a>
 </li>
 <li>
  <a href="https://github.com/tianon/gosu">
   GoSu
  </a>
  <sup>
   &#9733 717, pushed 14 days ago
  </sup>
  - Run this specific application as this specific user and get out of the pipeline (entrypoint script tool) by
  <a href="https://github.com/tianon">
   @tianon
  </a>
 </li>
 <li>
  <a href="https://github.com/garywiz/chaperone">
   Chaperone
  </a>
  <sup>
   &#9733 43, pushed 56 days ago
  </sup>
  - A single PID1 process designed for docker containers. Does user management, log management, startup, zombie reaping, all in one small package. by
  <a href="https://github.com/garywiz">
   @garywiz
  </a>
 </li>
 <li>
  <a href="https://github.com/jpetazzo/nsenter">
   ns-enter
  </a>
  <sup>
   &#9733 1407, pushed 15 days ago
  </sup>
  (no more ssh, enter name spaces of container) by
  <a href="https://github.com/jpetazzo">
   @jpetazzo
  </a>
 </li>
 <li>
  <a href="https://github.com/jpetazzo/squid-in-a-can">
   Squid-in-a-can
  </a>
  <sup>
   &#9733 169, pushed 47 days ago
  </sup>
  (in case of proxy problem) by
  <a href="https://github.com/jpetazzo">
   @jpetazzo
  </a>
 </li>
 <li>
  <a href="https://github.com/jwilder/docker-gen">
   docker-gen
  </a>
  <sup>
   &#9733 1359, pushed 4 days ago
  </sup>
  (Generate files from docker container meta-data) by
  <a href="https://github.com/jwilder">
   @jwilder
  </a>
 </li>
 <li>
  <a href="https://github.com/jwilder/dockerize">
   dockerize
  </a>
  <sup>
   &#9733 461, pushed 5 days ago
  </sup>
  (Utility to simplify running applications in docker containers) by
  <a href="https://github.com/jwilder">
   @jwilder
  </a>
 </li>
 <li>
  <a href="https://github.com/progrium/registrator">
   registrator
  </a>
  <sup>
   &#9733 3, pushed 259 days ago
  </sup>
  (Service registry bridge for Docker) by
  <a href="https://github.com/progrium">
   @progrium
  </a>
 </li>
 <li>
  <a href="https://github.com/swipely/dockly">
   Dockly
  </a>
  <sup>
   &#9733 175, pushed 4 days ago
  </sup>
  (Dockly is a gem made to ease the pain of packaging an application in Docker.) by
  <a href="https://github.com/swipely/">
   @swipely
  </a>
 </li>
 <li>
  <a href="https://github.com/cpuguy83/docker-volumes">
   docker-volumes
  </a>
  <sup>
   &#9733 360, pushed 265 days ago
  </sup>
  (Docker Volume Manager) by
  <a href="https://github.com/cpuguy83">
   @cpuguy83
  </a>
 </li>
 <li>
  <a href="https://github.com/projectatomic/dockerfile_lint">
   dockerfile_lint
  </a>
  <sup>
   &#9733 100, pushed 16 days ago
  </sup>
  (A rule-based 'linter' for Dockerfiles) by
  <a href="https://github.com/redhataccess">
   @redhataccess
  </a>
 </li>
 <li>
  <a href="https://github.com/clusterhq/powerstrip">
   powerstrip
  </a>
  <sup>
   &#9733 301, pushed 109 days ago
  </sup>
  (A tool for prototyping Docker extensions) by
  <a href="https://github.com/clusterhq">
   @clusterhq
  </a>
 </li>
 <li>
  <a href="https://github.com/tailhook/vagga">
   Vagga
  </a>
  <sup>
   &#9733 785, pushed 2 days ago
  </sup>
  (Vagga is a containerisation tool without daemons. It is a fully-userspace container engine inspired by Vagrant and Docker, specialized for development environments.) by
  <a href="https://github.com/tailhook/">
   @tailhook
  </a>
 </li>
 <li>
  <a href="https://github.com/apocas/dockerode">
   dockerode
  </a>
  <sup>
   &#9733 758, pushed 8 days ago
  </sup>
  (Not just another Docker Remote API node.js module) by
  <a href="https://github.com/apocas">
   @apocas
  </a>
 </li>
 <li>
  <a href="https://github.com/fsouza/go-dockerclient/">
   go-dockerclient
  </a>
  (Go HTTP client for the Docker remote API.) by
  <a href="https://github.com/fsouza/">
   @fsouza
  </a>
 </li>
 <li>
  <a href="https://github.com/lsqio/container-factory">
   container-factory
  </a>
  <sup>
   &#9733 51, pushed 363 days ago
  </sup>
  - Produces Docker images from tarballs of application source code by
  <a href="https://github.com/lsqio">
   @lsqio
  </a>
 </li>
 <li>
  <a href="https://codelift.io/">
   codelift
  </a>
  - CodeLift is an automated Docker image build utility for 'dockerizing' services by
  <a href="https://twitter.com/BoozAllen">
   @BoozAllen
  </a>
 </li>
 <li>
  <a href="https://github.com/ashmckenzie/percheron">
   percheron
  </a>
  <sup>
   &#9733 158, pushed 26 days ago
  </sup>
  - Organise your Docker containers with muscle and intelligence by
  <a href="https://github.com/ashmckenzie">
   @ashmckenzie
  </a>
 </li>
 <li>
  <a href="https://github.com/michaelsauter/crane">
   crane
  </a>
  <sup>
   &#9733 647, pushed 3 days ago
  </sup>
  - Lift containers with ease. Easy orchestration for images and containers by
  <a href="https://github.com/michaelsauter">
   @michaelsauter
  </a>
 </li>
 <li>
  <a href="https://github.com/rancher/sherdock">
   sherdock
  </a>
  <sup>
   &#9733 106, pushed 219 days ago
  </sup>
  - Automatic GC of images based on regexp by
  <a href="https://github.com/rancher">
   @rancher
  </a>
 </li>
 <li>
  <a href="https://github.com/p8952/bocker">
   bocker
  </a>
  <sup>
   &#9733 3260, pushed 251 days ago
  </sup>
  (1) - Docker implemented in 100 lines of bash by
  <a href="https://github.com/p8952">
   p8952
  </a>
 </li>
 <li>
  <a href="https://github.com/icy/bocker">
   bocker
  </a>
  <sup>
   &#9733 21, pushed 251 days ago
  </sup>
  (2) - Write Dockerfile completely in Bash. Extensible and simple. --> Reusable by
  <a href="https://github.com/icy">
   @icy
  </a>
 </li>
 <li>
  <a href="https://github.com/spotify/docker-gc">
   docker-gc
  </a>
  <sup>
   &#9733 1320, pushed 18 days ago
  </sup>
  - A cron job that will delete old stopped containers and unused images by
  <a href="https://github.com/spotify">
   @spotify
  </a>
 </li>
 <li>
  <a href="https://github.com/wercker/dlayer">
   dlayer
  </a>
  <sup>
   &#9733 64, pushed 82 days ago
  </sup>
  - Stats collector for Docker layers by
  <a href="https://github.com/wercker">
   @wercker
  </a>
 </li>
 <li>
  <a href="https://github.com/bsideup/forward2docker">
   forward2docker
  </a>
  <sup>
   &#9733 66, pushed 27 days ago
  </sup>
  - Utility to auto forward a port from localhost into ports on Docker containers running in a boot2docker VM by
  <a href="https://github.com/bsideup">
   @bsideup
  </a>
 </li>
 <li>
  <a href="https://github.com/jlhawn/dockramp">
   dockramp
  </a>
  <sup>
   &#9733 214, pushed 5 days ago
  </sup>
  - Proof of Concept: A Client Driven Docker Image Builder by
  <a href="https://github.com/jlhawn">
   @jlhawn
  </a>
 </li>
 <li>
  <a href="https://github.com/duedil-ltd/portainer">
   portainer
  </a>
  <sup>
   &#9733 118, pushed 99 days ago
  </sup>
  - Apache Mesos framework for building Docker images by
  <a href="https://github.com/tarnfeld">
   @tarnfeld
  </a>
 </li>
 <li>
  <a href="https://github.com/gesellix/gradle-docker-plugin">
   Gradle Docker plugin
  </a>
  <sup>
   &#9733 42, pushed 19 days ago
  </sup>
  - A Docker remote api plugin for Gradle by
  <a href="https://github.com/gesellix">
   @gesellix
  </a>
 </li>
 <li>
  <a href="https://github.com/gesellix/docker-client">
   Docker client
  </a>
  <sup>
   &#9733 20, pushed 2 days ago
  </sup>
  - A Docker remote api client library for the JVM, written in Groovy by
  <a href="https://github.com/gesellix">
   @gesellix
  </a>
 </li>
 <li>
  <a href="http://dropdock.io/">
   Dropdock
  </a>
  - A framework designed for Drupal to build fast, isolated development environments using Docker.
 </li>
 <li>
  <a href="https://github.com/fgrehm/devstep">
   Devstep
  </a>
  <sup>
   &#9733 179, pushed 54 days ago
  </sup>
  - Development environments powered by Docker and buildpacks by
  <a href="https://github.com/fgrehm">
   @fgrehm
  </a>
 </li>
 <li>
  <a href="https://lorry.io/">
   Lorry
  </a>
  - Lorry is a docker-compose.yml validator and composer by
  <a href="https://github.com/CenturyLinkLabs">
   @CenturyLinkLabs
  </a>
 </li>
 <li>
  <a href="http://dray.it/">
   Dray
  </a>
  - Dray is an engine for managing the execution of container-based workflows. Docker Workflow Engine - UNIX pipes for Docker by
  <a href="https://github.com/CenturyLinkLabs">
   @CenturyLinkLabs
  </a>
 </li>
 <li>
  <a href="https://github.com/benzaita/docker-do">
   docker-do
  </a>
  <sup>
   &#9733 11, pushed 174 days ago
  </sup>
  - hassle-free docker run, like
  <code>
   env
  </code>
  but for docker by
  <a href="https://github.com/benzaita">
   @benzaita
  </a>
 </li>
 <li>
  <a href="https://github.com/brikis98/docker-osx-dev">
   Docker osx dev
  </a>
  <sup>
   &#9733 1027, pushed 23 days ago
  </sup>
  - A productive development environment with Docker on OS X by
  <a href="https://github.com/brikis98">
   @brikis98
  </a>
 </li>
 <li>
  <a href="https://github.com/grammarly/rocker">
   rocker
  </a>
  <sup>
   &#9733 182, pushed 7 days ago
  </sup>
  - Extended Dockerfile builder. Supports multiple FROMs, MOUNTS, templates, etc. by
  <a href="https://github.com/grammarly">
   grammarly
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/docker-exec/dexec">
   dexec
  </a>
  <sup>
   &#9733 239, pushed 9 days ago
  </sup>
  - Command line interface for running code with Docker Exec images. https://docker-exec.github.io/ written in Go.
 </li>
 <li>
  <a href="https://github.com/polonskiy/crowdr">
   crowdr
  </a>
  <sup>
   &#9733 62, pushed 103 days ago
  </sup>
  - Tool for managing multiple Docker containers (docker-compose alternative) by
  <a href="https://github.com/polonskiy/">
   @polonskiy
  </a>
 </li>
 <li>
  <a href="https://github.com/instacart/ahab">
   ahab
  </a>
  <sup>
   &#9733 93, pushed 14 days ago
  </sup>
  - Docker event handling with Python by
  <a href="https://github.com/instacart">
   @instacart
  </a>
 </li>
 <li>
  <a href="https://github.com/konstruktoid/docker-garby">
   docker-garby
  </a>
  <sup>
   &#9733 4, pushed 58 days ago
  </sup>
  - Docker garbage collection script by
  <a href="https://github.com/konstruktoid">
   @konstruktoid
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/TechnologyAdvice/DevLab">
   DevLab
  </a>
  <sup>
   &#9733 391, pushed 128 days ago
  </sup>
  - Utility for running containerized development environments
 </li>
 <li>
  <a href="https://github.com/sindresorhus/is-docker">
   is-docker
  </a>
  <sup>
   &#9733 14, pushed 124 days ago
  </sup>
  - Check if the process is running inside a Docker container by
  <a href="https://github.com/sindresorhus/awesome">
   @sindresorhus
  </a>
 </li>
 <li>
  <a href="http://domeide.github.io/">
   Docker meets the IDE
  </a>
  - Integrating your favorite containers in the editor of your choice by
  <a href="https://github.com/domeide">
   domeide
  </a>
 </li>
 <li>
  <a href="https://github.com/getcarina/dvm">
   DVM
  </a>
  <sup>
   &#9733 112, pushed 18 days ago
  </sup>
  - Docker version manager by
  <a href="https://github.com/getcarina">
   @getcarina
  </a>
 </li>
 <li>
  <a href="https://github.com/mayflower/docker-ls">
   docker-ls
  </a>
  <sup>
   &#9733 39, pushed 19 days ago
  </sup>
  - CLI tools for browsing and manipulating docker registries by
  <a href="https://github.com/mayflower">
   @mayflower
  </a>
 </li>
 <li>
  <a href="https://github.com/cloud66/habitus">
   habitus
  </a>
  <sup>
   &#9733 116, pushed 13 days ago
  </sup>
  - A Build Flow Tool for Docker http://www.habitus.io by
  <a href="https://github.com/cloud66">
   @cloud66
  </a>
 </li>
 <li>
  <a href="https://www.composeregistry.com">
   Compose Registry
  </a>
  - A very handy search engine for Compose Files
 </li>
 <li>
  <a href="https://github.com/zzrotdesign/docker-clean">
   Docker Clean
  </a>
  <sup>
   &#9733 202, pushed 4 days ago
  </sup>
  - A script that cleans Docker containers, images and volumes by
  <a href="https://github.com/zzrotdesign">
   @zzrotdesign
  </a>
 </li>
 <li>
  <a href="https://github.com/adrianmo/powerline-docker">
   Powerline-Docker
  </a>
  <sup>
   &#9733 9, pushed 7 days ago
  </sup>
  - A Powerline segment for showing the status of Docker containers by
  <a href="https://github.com/adrianmo">
   @adrianmo
  </a>
 </li>
 <li>
  <a href="https://github.com/Microsoft/Docker-PowerShell">
   Docker-PowerShell
  </a>
  <sup>
   &#9733 73, pushed 1 days ago
  </sup>
  - PowerShell Module for Docker
 </li>
 <li>
  <a href="https://github.com/francescou/docker-compose-search">
   docker-compose-search
  </a>
  <sup>
   &#9733 6, pushed 112 days ago
  </sup>
  - A search engine for Docker Compose application stacks by
  <a href="https://github.com/francescou/">
   @francescou
  </a>
 </li>
 <li>
  <a href="https://github.com/gdiepen/docker-convenience-scripts">
   Docker Volume Clone Utility
  </a>
  <sup>
   &#9733 1, pushed 2 days ago
  </sup>
  - A Docker Utility to Clone Volumes
  <a href="https://twitter.com/gdiepen">
   @gdiepen
  </a>
 </li>
</ul>
<h2>
 Continuous Integration / Continuous Delivery
</h2>
<ul>
 <li>
  <a href="https://github.com/ciandcd/awesome-ciandcd">
   Awesome-ciandcd
  </a>
  <sup>
   &#9733 167, pushed 4 days ago
  </sup>
  - Not specific to docker but relevant.
 </li>
 <li>
  <a href="https://github.com/harbur/captain">
   Captain
  </a>
  <sup>
   &#9733 294, pushed 76 days ago
  </sup>
  - Convert your Git workflow to Docker containers ready for Continuous Delivery by
  <a href="https://github.com/harbur">
   @harbur
  </a>
 </li>
 <li>
  <a href="https://circleci.com/">
   CircleCI
  </a>
  - Push or pull Docker images from your build environment, or build and run containers right on CircleCI.
 </li>
 <li>
  <a href="https://codefresh.io">
   CodeFresh
  </a>
  - Accelerate your transition to Docker containers
 </li>
 <li>
  <a href="http://pages.codeship.com/docker">
   CodeShip
  </a>
  - Work with your established Docker workflows while automating your testing and deployment tasks with our hosted platform dedicated to speed and security.
 </li>
 <li>
  <a href="https://github.com/jenkinsci/docker-plugin/">
   Docker plugin for Jenkins
  </a>
  - The aim of the docker plugin is to be able to use a docker host to dynamically provision a slave, run a single build, then tear-down that slave.
 </li>
 <li>
  <a href="https://github.com/dockunit/platform">
   Dockunit
  </a>
  <sup>
   &#9733 35, pushed 165 days ago
  </sup>
  - Docker based integration tests. A simple Node based utility for running Docker based unit tests. By
  <a href="https://github.com/dockunit">
   @dockunit
  </a>
 </li>
 <li>
  <a href="https://github.com/drone/drone">
   Drone
  </a>
  <sup>
   &#9733 6750, pushed 1 days ago
  </sup>
  - Continuous integration server built on Docker and configured using YAML files.
 </li>
 <li>
  <a href="https://about.gitlab.com/gitlab-ci/">
   GitLab CI
  </a>
  - GitLab has integrated CI to test, build and deploy your code with the use of GitLab runners.
 </li>
 <li>
  <a href="https://github.com/gocd/gocd-docker">
   GOCD-Docker
  </a>
  <sup>
   &#9733 57, pushed 5 days ago
  </sup>
  Go Server and Agent in docker containers to provision.
 </li>
 <li>
  <a href="https://hub.jazz.net">
   IBM DevOps Services
  </a>
  - Continuous delivery using a pipeline deployment onto IBM Containers on Bluemix.
 </li>
 <li>
  <a href="https://app.shippable.com/">
   Shippable
  </a>
  - A SaaS platform for developers and DevOps teams that significantly reduces the time taken for code to be built, tested and deployed to production.
 </li>
 <li>
  <a href="https://github.com/CenturyLinkLabs/watchtower">
   Watchtower
  </a>
  <sup>
   &#9733 327, pushed 49 days ago
  </sup>
  - Automatically update running Docker containers by
  <a href="https://github.com/CenturyLinkLabs">
   @CenturyLinkLabs
  </a>
 </li>
 <li>
  <a href="https://github.com/francescou/docker-continuous-deployment">
   Microservices Continuous Deployment
  </a>
  <sup>
   &#9733 84, pushed 62 days ago
  </sup>
  - Continuous deployment of a microservices application
 </li>
</ul>
<h2>
 Deployment
</h2>
<ul>
 <li>
  <a href="https://github.com/ehazlett/conduit">
   Conduit
  </a>
  <sup>
   &#9733 75, pushed 26 days ago
  </sup>
  - Experimental deployment system for Docker by
  <a href="https://github.com/ehazlett">
   @ehazlett
  </a>
 </li>
 <li>
  <a href="https://github.com/gondor/depcon">
   depcon
  </a>
  <sup>
   &#9733 48, pushed 3 days ago
  </sup>
  - Depcon is written in Go and allows you to easily deploy Docker containers to Apache Mesos/Marathon, Amazon ECS and Kubernetes.  By
  <a href="https://github.com/gondor">
   @gonodr
  </a>
 </li>
 <li>
  <a href="https://github.com/humblec/dockit">
   dockit
  </a>
  <sup>
   &#9733 98, pushed 546 days ago
  </sup>
  - Do docker actions and Deploy gluster containers!
 </li>
 <li>
  <a href="https://lastbackend.com/">
   Last.Backend
  </a>
  - Last.Backend platform is designed for automatization of all routine work with the server and deployment of applications in one click using the visual interface.
 </li>
 <li>
  <a href="https://github.com/grammarly/rocker-compose">
   rocker-compose
  </a>
  <sup>
   &#9733 296, pushed 10 days ago
  </sup>
  - Docker composition tool with idempotency features for deploying apps composed of multiple containers.
 </li>
 <li>
  <a href="https://github.com/CenturyLinkLabs/zodiac">
   Zodiac
  </a>
  <sup>
   &#9733 133, pushed 259 days ago
  </sup>
  - A lightweight tool for easy deployment and rollback of dockerized applications. By
  <a href="https://github.com/CenturyLinkLabs">
   @CenturyLinkLabs
  </a>
 </li>
</ul>
<h2>
 Hosting for repositories (registries)
</h2>
<p>
 Securely store your Docker images.
*
 <a href="https://hub.docker.com/">
  Docker Hub
 </a>
 (provided by Docker Inc.)
*
 <a href="https://quay.io/">
  Quay.io
 </a>
 (part of CoreOS) - Secure hosting for private Docker repositories
*
 <a href="https://reesd.com/">
  Reesd
 </a>
 -  Private Docker repositories and redundant storage service by
 <a href="https://github.com/noteed">
  @noteed
 </a>
</p>
<h2>
 Hosting for containers
</h2>
<ul>
 <li>
  <a href="http://aws.amazon.com/ecs/">
   Amazon ECS
  </a>
  - A management service on EC2 that supports Docker containers.
 </li>
 <li>
  <a href="https://containership.io">
   ContainerShip Cloud
  </a>
  - Multi-Cloud Container Hosting Automation Platform.
 </li>
 <li>
  <a href="https://www.tutum.co/">
   Docker Tutum
  </a>
  (part of Docker Inc) - Simple hosting for your Docker containers. -> now Docker Cloud
 </li>
 <li>
  <a href="https://cloud.docker.com/">
   Docker Cloud
  </a>
  - Former Tutum
 </li>
 <li>
  <a href="https://cloud.google.com/container-engine/docs/">
   Google Container Engine
  </a>
  - Docker containers on Google Cloud Computing powered by
  <a href="http://kubernetes.io">
   Kubernetes
  </a>
  .
 </li>
 <li>
  <a href="https://giantswarm.io/">
   Giant Swarm
  </a>
  - Simple microservice infrastructure. Deploy your containers in seconds.
 </li>
 <li>
  <a href="https://console.ng.bluemix.net/">
   IBM Bluemix
  </a>
  - Run Docker containers in a hosted cloud environment on IBM Bluemix.
 </li>
 <li>
  <a href="https://www.openshift.com/dedicated/index.html">
   OpenShift Dedicated
  </a>
  - A hosted
  <a href="https://www.openshift.org/">
   OpenShift
  </a>
  cluster for running your Docker containers managed by Red Hat.
 </li>
 <li>
  <a href="https://www.orchardup.com/">
   Orchard
  </a>
  (part of Docker Inc) - Get a Docker host in the cloud, instantly.
 </li>
 <li>
  <a href="https://www.joyent.com/">
   Triton
  </a>
  - Elastic container-native infrastructure by Joyent.
 </li>
</ul>
<h2>
 Reverse Proxy
</h2>
<ul>
 <li>
  <a href="https://github.com/jwilder/nginx-proxy">
   nginx-proxy
  </a>
  <sup>
   &#9733 2504, pushed 2 days ago
  </sup>
  - Automated nginx proxy for Docker containers using docker-gen by
  <a href="https://github.com/jwilder">
   @jwilder
  </a>
 </li>
 <li>
  <a href="https://github.com/zchee/h2o-proxy">
   h2o-proxy
  </a>
  <sup>
   &#9733 24, pushed 118 days ago
  </sup>
  - Automated H2O reverse proxy for Docker containers. An alternative to
  <a href="https://github.com/jwilder/nginx-proxy">
   jwilder/nginx-proxy
  </a>
  by
  <a href="https://github.com/zchee">
   @zchee
  </a>
 </li>
 <li>
  <a href="https://github.com/silarsis/docker-proxy">
   docker-proxy
  </a>
  <sup>
   &#9733 70, pushed 2 days ago
  </sup>
  - Transparent proxy for docker containers, run in a docker container. By
  <a href="https://github.com/silarsis">
   @silarsis
  </a>
 </li>
 <li>
  <a href="https://github.com/mattallty/muguet">
   muguet
  </a>
  <sup>
   &#9733 116, pushed 133 days ago
  </sup>
  - DNS Server & Reverse proxy for Docker environments. By
  <a href="https://github.com/mattallty">
   @mattallty
  </a>
 </li>
 <li>
  <a href="https://traefik.io/">
   Træfɪk
  </a>
  - Automated reverse proxy and load-balancer for Docker, Mesos, Consul, Etcd... By
  <a href="https://github.com/emilevauge">
   @EmileVauge
  </a>
 </li>
</ul>
<h2>
 Web Interface
</h2>
<ul>
 <li>
  <a href="https://github.com/atc-/docker-registry-ui">
   Docker Registry Web
  </a>
  <sup>
   &#9733 548, pushed 24 days ago
  </sup>
  (A web UI for easy private/local Docker Registry integration) by
  <a href="https://github.com/atc-">
   @atc-
  </a>
 </li>
 <li>
  <a href="https://github.com/kevana/ui-for-docker">
   DockerUI
  </a>
  <sup>
   &#9733 3780, pushed 4 days ago
  </sup>
  (DockerUI is a web interface to interact with the Remote API.) by
  <a href="https://github.com/crosbymichael">
   @crosbymichael
  </a>
 </li>
 <li>
  <a href="https://github.com/SUSE/Portus">
   Portus
  </a>
  <sup>
   &#9733 756, pushed 3 days ago
  </sup>
  (Authorization service and frontend for Docker registry (v2)) by
  <a href="https://github.com/SUSE">
   @SUSE
  </a>
 </li>
 <li>
  <a href="https://github.com/Electrofenster/dockerding-on-rails">
   dockering-on-rails
  </a>
  <sup>
   &#9733 5, pushed 142 days ago
  </sup>
  Simple Web-Interface for Docker with a lot of features by
  <a href="https://github.com/Electrofenster/">
   @Electrofenster
  </a>
 </li>
 <li>
  <a href="https://github.com/ozlerhakan/rapid">
   Rapid Dashboard
  </a>
  <sup>
   &#9733 5, pushed 73 days ago
  </sup>
  (A simple query dashboard to use Docker Remote API) by
  <a href="https://github.com/ozlerhakan/">
   @ozlerhakan
  </a>
 </li>
</ul>
<h2>
 Local Container Manager
</h2>
<ul>
 <li>
  <a href="http://ianmiell.github.io/shutit/">
   Shutit
  </a>
  (a tool for building and maintaining complex Docker deployments) by
  <a href="https://github.com/ianmiell">
   @ianmiell
  </a>
 </li>
 <li>
  <a href="https://github.com/mattes/fugu">
   FuGu
  </a>
  <sup>
   &#9733 129, pushed 267 days ago
  </sup>
  (a docker run wrapper without orchestration) by
  <a href="https://github.com/mattes">
   @mattes
  </a>
 </li>
 <li>
  <a href="https://github.com/boot2docker/boot2docker">
   Boot2Docker
  </a>
  <sup>
   &#9733 6051, pushed 6 days ago
  </sup>
  (docker for OSX and Windows) -- http://boot2docker.io/
 </li>
 <li>
  <a href="https://github.com/shyiko/docker-vm">
   docker-vm
  </a>
  <sup>
   &#9733 30, pushed 281 days ago
  </sup>
  (A simple and transparent alternative to boot2docker (backed by Vagrant)) by
  <a href="https://github.com/shyiko">
   @shyiko
  </a>
 </li>
 <li>
  <a href="https://github.com/awvessel/vessel">
   Vessel
  </a>
  <sup>
   &#9733 212, pushed 291 days ago
  </sup>
  (Vessel automates the setup & use of dockerized development environments) by
  <a href="https://github.com/awvessel">
   @awvessel
  </a>
 </li>
 <li>
  <a href="http://subuser.org">
   subuser
  </a>
  (subuser makes it easy to securely and portably run graphical desktop applications in Docker)
 </li>
 <li>
  <a href="http://www.octohost.io/">
   OctoHost
  </a>
  (Simple web focused Docker based mini-PaaS server. git push to deploy your websites as needed) by
  <a href="https://github.com/octohost">
   @octohost
  </a>
 </li>
 <li>
  <a href="https://github.com/dokku/dokku">
   Dokku
  </a>
  <sup>
   &#9733 11549, pushed 4 days ago
  </sup>
  (Docker powered mini-Heroku in around 100 lines of Bash) by
  <a href="https://github.com/progrium">
   @progrium
  </a>
 </li>
 <li>
  <a href="http://docs.ansible.com/ansible/docker_module.html">
   Ansible - manage docker containers
  </a>
 </li>
 <li>
  <a href="https://www.vagrantup.com/docs/docker/basics.html">
   Vagrant - Docker provider
  </a>
  a good starting point is
  <a href="https://github.com/bubenkoff/vagrant-docker-example">
   vagrant-docker-example
  </a>
  by
  <a href="https://github.com/bubenkoff">
   @bubenkoff
  </a>
 </li>
 <li>
  <a href="https://github.com/CenturyLinkLabs/dray">
   Dray
  </a>
  <sup>
   &#9733 249, pushed 101 days ago
  </sup>
  An engine for managing the execution of container-based workflows. http://Dray.it by
  <a href="https://github.com/CenturyLinkLabs">
   @CenturyLinkLabs
  </a>
 </li>
 <li>
  <a href="https://github.com/ashmckenzie/percheron">
   percheron
  </a>
  (Organise your Docker containers with muscle and intelligence) by
  <a href="https://github.com/ashmckenzie">
   @ashmckenzie
  </a>
 </li>
 <li>
  <a href="http://dusty.gc.com/">
   Dusty
  </a>
  Managed Docker development environments on OS X
 </li>
 <li>
  <a href="https://github.com/cortexmedia/Beluga">
   Beluga
  </a>
  <sup>
   &#9733 164, pushed 216 days ago
  </sup>
  Beluga a CLI to deploy docker containers on a single server or low amount of servers. By
  <a href="https://github.com/cortexmedia">
   @cortextmedia
  </a>
 </li>
 <li>
  <a href="https://github.com/docker/libcompose">
   libcompose
  </a>
  <sup>
   &#9733 299, pushed 2 days ago
  </sup>
  A Go library for Docker Compose.
 </li>
 <li>
  <a href="https://github.com/nlf/dlite">
   DLite
  </a>
  <sup>
   &#9733 2148, pushed 5 days ago
  </sup>
  Simplest way to use Docker on OSX, no VM needed.
  <strong>
   WIP
  </strong>
  By
  <a href="https://github.com/nlf">
   @nlf
  </a>
 </li>
</ul>
<h2>
 Volume management and plugins
</h2>
<ul>
 <li>
  <a href="https://github.com/blockbridge/blockbridge-docker-volume">
   Blockbridge
  </a>
  <sup>
   &#9733 24, pushed 5 days ago
  </sup>
  - The Blockbridge plugin is a volume plugin that provides access to an extensible set of container-based persistent storage options. It supports single and multi-host Docker environments with features that include tenant isolation, automated provisioning, encryption, secure deletion, snapshots and QoS. By
  <a href="https://github.com/blockbridge">
   @blockbridge
  </a>
 </li>
 <li>
  <a href="https://github.com/rancher/convoy">
   Convoy
  </a>
  <sup>
   &#9733 335, pushed 6 days ago
  </sup>
  - an open-source Docker volume driver that can snapshot, backup and restore Docker volumes anywhere. By
  <a href="https://github.com/rancher">
   @rancher
  </a>
 </li>
 <li>
  <a href="https://github.com/ahmetalpbalkan/azurefile-dockervolumedriver">
   Azure Files Volume Driver
  </a>
  <sup>
   &#9733 2, pushed 53 days ago
  </sup>
  - A Docker volume driver that allows you to mount persistent volumes backed by Microsoft Azure File Service. By
  <a href="https://github.com/ahmetalpbalkan">
   @ahmetalpbalkan
  </a>
 </li>
 <li>
  <a href="https://github.com/leighmcculloch/docker-unison">
   Docker Unison
  </a>
  <sup>
   &#9733 87, pushed 31 days ago
  </sup>
  A docker volume container using Unison for fast two-way folder sync. Created as an alternative to slow boot2docker volumes on OS X. By
  <a href="https://github.com/leighmcculloch">
   @leighmcculloch
  </a>
 </li>
 <li>
  <a href="https://github.com/gondor/docker-volume-netshare">
   Netshare
  </a>
  <sup>
   &#9733 142, pushed 4 days ago
  </sup>
  A Docker volume plugin written in Go that supports mounting NFS, AWS EFS & CIFS volumes within a container. By
  <a href="https://github.com/gondor">
   @gondor
  </a>
 </li>
 <li>
  <a href="https://github.com/adlogix/docker-machine-nfs">
   Docker Machine NFS
  </a>
  <sup>
   &#9733 417, pushed 53 days ago
  </sup>
  Activates NFS for an existing boot2docker box created through Docker Machine on OS X.
 </li>
 <li>
  <a href="https://github.com/emccode/rexray">
   REX-Ray
  </a>
  <sup>
   &#9733 251, pushed 2 days ago
  </sup>
  Vendor agnostic storage orchestration engine to provide persistent storage for Docker containers as well as Mesos frameworks and tasks.
 </li>
 <li>
  <a href="https://github.com/CWSpear/local-persist">
   Local Persist
  </a>
  <sup>
   &#9733 33, pushed 36 days ago
  </sup>
  Specify a mountpoint for your local volumes (created via
  <code>
   docker volume create
  </code>
  ) so that files will always persist and so you can mount to different directories in different containers.
 </li>
</ul>
<h2>
 Useful Images
</h2>
<ul>
 <li>
  <a href="https://github.com/docker-library/official-images">
   Official Images from Docker Hub
  </a>
  <sup>
   &#9733 1250, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/phusion/baseimage-docker">
   Base Image
  </a>
  <sup>
   &#9733 4140, pushed 2 days ago
  </sup>
  by
  <a href="https://github.com/phusion/">
   @phusion
  </a>
 </li>
 <li>
  <a href="https://github.com/jpetazzo/docker-busybox">
   Busybox
  </a>
  <sup>
   &#9733 84, pushed 371 days ago
  </sup>
  (with either
  <code>
   buildroot
  </code>
  or Ubuntu's
  <code>
   busybox-static
  </code>
  ) by
  <a href="https://github.com/jpetazzo">
   @jpetazzo
  </a>
 </li>
 <li>
  <a href="http://www.zoobab.com/docker-openwrt-image">
   OpenWRT
  </a>
  by
  <a href="https://github.com/zoobab">
   @zoobab
  </a>
 </li>
 <li>
  <a href="https://hub.docker.com/u/phusion/">
   Phusion Docker Hub Account
  </a>
 </li>
 <li>
  <a href="https://github.com/phusion/passenger-docker">
   passenger-docker
  </a>
  <sup>
   &#9733 1921, pushed 71 days ago
  </sup>
  (Docker base images for Ruby, Python, Node.js and Meteor web apps) by
  <a href="https://github.com/phusion">
   @phusion
  </a>
 </li>
 <li>
  <a href="https://github.com/gliderlabs/docker-alpine">
   docker-alpine
  </a>
  <sup>
   &#9733 2994, pushed 8 days ago
  </sup>
  (A super small Docker base image
  <em>
   (5MB)
  </em>
  using Alpine Linux) by
  <a href="https://github.com/gliderlabs">
   @gliderlabs
  </a>
 </li>
 <li>
  <a href="https://github.com/kiyoto/docker-fluentd">
   docker-fluentd
  </a>
  <sup>
   &#9733 22, pushed 518 days ago
  </sup>
  (the Container to Log Other Containers' Logs) by
  <a href="https://github.com/kiyoto">
   @kiyoto
  </a>
 </li>
 <li>
  <a href="https://github.com/garywiz/chaperone-docker">
   chaperone-docker
  </a>
  <sup>
   &#9733 19, pushed 113 days ago
  </sup>
  (A set of images using the Chaperone process manager, including a lean Alpine image, LAMP, LEMP, and bare-bones base kits.)
 </li>
 <li>
  <a href="https://github.com/NVIDIA/nvidia-docker">
   nvidia-docker
  </a>
  <sup>
   &#9733 540, pushed 14 days ago
  </sup>
  (Build and run Docker containers leveraging NVIDIA GPUs.)
 </li>
</ul>
<h2>
 Dockerfile
</h2>
<ul>
 <li>
  <a href="https://github.com/crosbymichael/Dockerfiles">
   Collection of Dockerfiles
  </a>
  <sup>
   &#9733 241, pushed 601 days ago
  </sup>
  by
  <a href="https://github.com/crosbymichael">
   @crosbymichael
  </a>
 </li>
 <li>
  <a href="http://dockerfile.github.io/">
   Dockerfile Project
  </a>
  : Trusted Automated Docker Builds. Dockerfile Project maintains a central repository of Dockerfile for various popular open source software services runnable on a Docker container.
 </li>
 <li>
  <a href="https://github.com/komljen/dockerfile-examples">
   Dockerfile Example
  </a>
  <sup>
   &#9733 340, pushed 281 days ago
  </sup>
  by
  <a href="https://github.com/komljen">
   @komljen
  </a>
 </li>
 <li>
  <a href="https://github.com/kstaken/dockerfile-examples">
   Dockerfile Example 2
  </a>
  <sup>
   &#9733 356, pushed 155 days ago
  </sup>
  by
  <a href="https://github.com/kstaken">
   @kstaken
  </a>
 </li>
 <li>
  <a href="https://github.com/jfrazelle/dockerfiles">
   Dockerfile @jfrazelle
  </a>
  <sup>
   &#9733 2026, pushed 2 days ago
  </sup>
  by
  <a href="https://github.com/jfrazelle">
   @jfrazelle
  </a>
  <strong>
   MUST SEE
  </strong>
  for a fully containerized
desktop!
 </li>
</ul>
<h2>
 Storing Images
</h2>
<ul>
 <li>
  <a href="https://github.com/docker/distribution">
   Docker Registry v2
  </a>
  <sup>
   &#9733 2017, pushed 4 days ago
  </sup>
  (The Docker toolset to pack, ship, store, and deliver content)
 </li>
 <li>
  <a href="https://github.com/noteed/rescoyl">
   Rescoyl
  </a>
  <sup>
   &#9733 6, pushed 165 days ago
  </sup>
  (Private Docker registry) by
  <a href="https://github.com/noteed">
   @noteed
  </a>
 </li>
 <li>
  <a href="http://www.projectatomic.io/registry/">
   Atomic Registry
  </a>
  Red Hat Atomic Registry is an open source enterprise registry based on the Origin and Cockpit projects, enhancing the Docker registry library.
 </li>
</ul>
<h2>
 Monitoring
</h2>
<ul>
 <li>
  <a href="http://axibase.com/products/axibase-time-series-database/writing-data/docker-cadvisor/">
   Axibase Time-Series Database
  </a>
  (Long-term retention of container statistics and built-in dashboards for Docker. Collected with native Google cAdvisor storage driver.)
 </li>
 <li>
  <a href="https://github.com/google/cadvisor">
   cAdvisor
  </a>
  <sup>
   &#9733 3861, pushed 2 days ago
  </sup>
  (Analyzes resource usage and performance characteristics of running containers. created by
  <a href="https://github.com/google">
   @Google
  </a>
 </li>
 <li>
  <a href="https://www.datadoghq.com/">
   Datadog
  </a>
  Datadog is a full-stack monitoring service for large-scale cloud environments that aggregates metrics/events from servers, databases, and applications. It includes support for Docker, Kubernetes, and Mesos.
 </li>
 <li>
  <a href="https://github.com/dockerana/dockerana">
   Dockerana
  </a>
  <sup>
   &#9733 171, pushed 317 days ago
  </sup>
  (packaged version of Graphite and Grafana, specifically targeted at metrics from Docker.)
 </li>
 <li>
  <a href="https://github.com/icecrime/docker-mon">
   Docker-mon
  </a>
  <sup>
   &#9733 661, pushed 281 days ago
  </sup>
  (Console-based Docker monitoring) by
  <a href="https://github.com/icecrime">
   @icecrime
  </a>
 </li>
 <li>
  <a href="http://nicolargo.github.io/glances/">
   Glances
  </a>
  (A cross-platform curses-based system monitoring tool written in Python) by
  <a href="https://github.com/nicolargo">
   @nicolargo
  </a>
 </li>
 <li>
  <a href="https://github.com/vegasbrianc/docker-monitoring">
   InfluxDB, cAdvisor, Grafana
  </a>
  <sup>
   &#9733 133, pushed 6 days ago
  </sup>
  (InfluxDB Time series DB in combination with Grafana and cAdvisor) by
  <a href="https://github.com/vegasbrianc">
   @vegasbrianc
  </a>
 </li>
 <li>
  <a href="https://meros.io">
   Meros
  </a>
  Analyzes containers resources, captures logs, remote web SSH terminal and powerful DevOps alerts.
 </li>
 <li>
  <a href="http://newrelic.com/docker">
   New Relic
  </a>
  New Relics Docker Monitoring tool
 </li>
 <li>
  <a href="https://prometheus.io/">
   Prometheus
  </a>
  (Open-source service monitoring system and time series database)
 </li>
 <li>
  <a href="http://www.dynatrace.com/en/ruxit/technologies/cloud-and-microservices/docker-monitoring/">
   Ruxit
  </a>
  Monitor containerized applications without installing agents or modifying your Run commands
 </li>
 <li>
  <a href="https://github.com/tobegit3hub/seagull">
   Seagull
  </a>
  <sup>
   &#9733 1298, pushed 35 days ago
  </sup>
  (Friendly Web UI to monitor docker daemon.) by
  <a href="https://github.com/tobegit3hub">
   @tobegit3hub
  </a>
 </li>
 <li>
  <a href="https://www.site24x7.com/docker-monitoring.html">
   Site24x7
  </a>
  Docker MOnitoring for DevOps and IT is a SaaS Pay per Host model
 </li>
 <li>
  <a href="http://www.sysdig.org/">
   Sysdig
  </a>
  : An open source troubleshooting tool that provides a rich set of real-time, system-level information. It has container-specific features and is very useful in Docker environments.
 </li>
 <li>
  <a href="https://github.com/monitoringartist/Zabbix-Docker-Monitoring">
   Zabbix Docker module
  </a>
  <sup>
   &#9733 244, pushed 19 days ago
  </sup>
  : Zabbix module that provides discovery of running containers, CPU/memory/blk IO/net container metrics. Systemd Docker and LXC execution driver is also supported. It's a dynamically linked shared object library, so its performance is (~10x) better, than any script solution.
 </li>
 <li>
  <a href="https://github.com/sematext/sematext-agent-docker">
   SPM for Docker
  </a>
  <sup>
   &#9733 12, pushed 12 days ago
  </sup>
  Monitoring of host and container metrics, Docker events and logs. Automatic log parser. Anomaly Detection and alerting for metrics and logs.
  <a href="https://twitter.com/sematext">
   @sematext
  </a>
 </li>
 <li>
  <a href="https://github.com/gomex/docker-zabbix">
   Zabbix Docker
  </a>
  <sup>
   &#9733 17, pushed 162 days ago
  </sup>
  - Monitor containers automatically using zabbix LLD feature.
 </li>
 <li>
  <a href="http://blogs.splunk.com/2015/08/24/collecting-docker-logs-and-stats-with-splunk/">
   Collecting docker logs and stats with Splunk
  </a>
 </li>
</ul>
<h2>
 Networking
</h2>
<ul>
 <li>
  <a href="https://www.projectcalico.org/getting-started/docker/">
   Calico-Docker
  </a>
  - Calico is a pure layer 3 virtual network that allows containers over multiple docker-hosts to talk to each other.
 </li>
 <li>
  <a href="https://github.com/ahmetalpbalkan/wagl">
   Wagl
  </a>
  <sup>
   &#9733 260, pushed 5 days ago
  </sup>
  - DNS Service Discovery for Docker Swarm (by
  <a href="https://github.com/ahmetalpbalkan">
   @ahmetalpbalkan
  </a>
  ) http://ahmetalpbalkan.github.io/wagl/
 </li>
 <li>
  <a href="https://github.com/weaveworks/weave">
   Weave
  </a>
  <sup>
   &#9733 4182, pushed 4 days ago
  </sup>
  (The Docker network) -- Weave creates a virtual network that connects Docker containers deployed across multiple hosts.
 </li>
</ul>
<h2>
 Logging
</h2>
<ul>
 <li>
  <a href="https://github.com/kiyoto/docker-fluentd">
   Docker-Fluentd
  </a>
  <sup>
   &#9733 22, pushed 518 days ago
  </sup>
  : (Docker container to Log Other Containers' Logs. One can aggregate the logs of Docker containers running on the same host using Fluentd.) by
  <a href="https://github.com/kiyoto">
   @kiyoto
  </a>
 </li>
 <li>
  <a href="https://github.com/gocardless/logjam">
   LogJam
  </a>
  <sup>
   &#9733 110, pushed 209 days ago
  </sup>
  (Logjam is a log forwarder designed to listen on a local port, receive log entries over UDP, and forward these messages on to a log collection server (such as logstash).) by
  <a href="https://github.com/gocardless">
   @gocardless
  </a>
 </li>
 <li>
  <a href="https://github.com/gliderlabs/logspout">
   Logspout
  </a>
  <sup>
   &#9733 1794, pushed 6 days ago
  </sup>
  (Log routing for Docker container logs) by
  <a href="https://github.com/gliderlabs">
   @gliderlabs
  </a>
 </li>
 <li>
  <a href="https://github.com/sematext/sematext-agent-docker">
   Logsene for Docker
  </a>
  <sup>
   &#9733 12, pushed 12 days ago
  </sup>
  Monitoring of Metrics, Events and Logs implemented in Node.js. Integrated
  <a href="https://github.com/sematext/logagent-js">
   logagent-js
  </a>
  to detect and parse various log formats.
  <a href="https://twitter.com/sematext">
   @sematext
  </a>
 </li>
</ul>
<h2>
 Deployment and Infrastructure
</h2>
<ul>
 <li>
  <a href="https://github.com/newrelic/centurion">
   Centurion
  </a>
  <sup>
   &#9733 1592, pushed 8 days ago
  </sup>
  : Centurion is a mass deployment tool for Docker fleets. It takes containers from a Docker registry and runs them on a fleet of hosts with the correct environment variables, host volume mappings, and port mappings. By
  <a href="https://github.com/newrelic">
   @newrelic
  </a>
 </li>
 <li>
  <a href="https://github.com/brooklyncentral/clocker">
   Clocker
  </a>
  <sup>
   &#9733 395, pushed 4 days ago
  </sup>
  : Clocker creates and manages a Docker cloud infrastructure. Clocker supports single-click deployments and runtime management of multi-node applications that run as containers distributed across multiple hosts, on both Docker and Marathon. It leverages
  <a href="https://github.com/projectcalico/calico-containers">
   Calico
  </a>
  and
  <a href="https://github.com/weaveworks/weave">
   Weave
  </a>
  for networking and
  <a href="http://brooklyn.apache.org/">
   Brooklyn
  </a>
  for application blueprints. By
  <a href="https://github.com/brooklyncentral">
   @brooklyncentral
  </a>
 </li>
 <li>
  <a href="http://www.cloud66.com">
   Cloud 66
  </a>
  - Full-stack hosted container management as a service
 </li>
 <li>
  <a href="https://github.com/Perennials/deploy">
   deploy
  </a>
  <sup>
   &#9733 18, pushed 64 days ago
  </sup>
  - Git and Docker deployment tool. A middle ground between simple Docker composition tools and full blown cluster orchestration. Declarative configuration and short commands for managing (syncing, building, running) of infrastructures of more than a few services. Able to deploy whole preconfigured server or system of services with a single line (without having to scroll the line).
 </li>
 <li>
  <a href="https://github.com/netvarun/docket">
   Docket
  </a>
  <sup>
   &#9733 538, pushed 351 days ago
  </sup>
  : Custom docker registry that allows for lightning fast deploys through bittorrent by
  <a href="https://github.com/netvarun/">
   @netvarun
  </a>
 </li>
 <li>
  <a href="https://github.com/longshoreman/longshoreman">
   Longshoreman
  </a>
  <sup>
   &#9733 416, pushed 487 days ago
  </sup>
  : Longshoreman automates application deployment using Docker. Just create a Docker repository (or use a service), configure the cluster using AWS or Digital Ocean (or whatever you like) and deploy applications using a Heroku-like CLI tool. By
  <a href="https://github.com/longshoreman">
   longshoreman
  </a>
 </li>
</ul>
<h2>
 PaaS
</h2>
<ul>
 <li>
  <a href="https://github.com/deis/deis">
   Deis
  </a>
  <sup>
   &#9733 5516, pushed 1 days ago
  </sup>
  (Your PaaS, your rules) -- http://deis.io/
 </li>
 <li>
  <a href="https://github.com/dokku/dokku">
   Dokku
  </a>
  (Docker powered mini-Heroku in around 100 lines of Bash) by
  <a href="https://github.com/progrium">
   @progrium
  </a>
 </li>
 <li>
  <a href="https://github.com/flynn/flynn">
   Flynn
  </a>
  <sup>
   &#9733 4444, pushed 2 days ago
  </sup>
  (A next generation open source platform as a service) -- https://flynn.io/
 </li>
 <li>
  <a href="https://www.openshift.org/">
   OpenShift
  </a>
  (An open source PaaS built on
  <a href="http://kubernetes.io">
   Kubernetes
  </a>
  and optimized for Dockerized app development and deployment) by
  <a href="https://www.redhat.com/">
   Red Hat
  </a>
 </li>
 <li>
  <a href="https://github.com/tsuru/tsuru">
   Tsuru
  </a>
  <sup>
   &#9733 1864, pushed 1 days ago
  </sup>
  (Tsuru is an extensible and open source Platform as a Service software) -- https://tsuru.io/
 </li>
</ul>
<h2>
 Remote Container Manager / Orchestration
</h2>
<ul>
 <li>
  <a href="https://github.com/prologic/autodock">
   autodock
  </a>
  <sup>
   &#9733 30, pushed 121 days ago
  </sup>
  (Daemon for Docker Automation) by
  <a href="https://github.com/prologic">
   @prologic
  </a>
 </li>
 <li>
  <a href="https://github.com/tubesandlube/blimp">
   blimp
  </a>
  <sup>
   &#9733 17, pushed 401 days ago
  </sup>
  Uses Docker Machine to easily move a container from one Docker host to another, show containers running against all of your hosts, replicate a container across multiple hosts and more. By
  <a href="https://github.com/defermat">
   @defermat
  </a>
  and
  <a href="https://github.com/schvin">
   @schvin
  </a>
 </li>
 <li>
  <a href="https://github.com/byrnedo/capitan">
   Capitan
  </a>
  <sup>
   &#9733 14, pushed 10 days ago
  </sup>
  Composable docker orchestration with added scripting support by
  <a href="https://github.com/byrnedo">
   @byrnedo
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/citadel/citadel">
   Citadel
  </a>
  <sup>
   &#9733 430, pushed 249 days ago
  </sup>
  (Citadel is a toolkit for scheduling containers on a Docker cluster) (unmaintained)
 </li>
 <li>
  <a href="http://www.cloudslang.io/">
   CloudSlang
  </a>
  (CloudSlang is a workflow engine to create Docker process automation)
 </li>
 <li>
  <a href="https://github.com/containership/containership">
   ContainerShip
  </a>
  <sup>
   &#9733 112, pushed 9 days ago
  </sup>
  (A simple container management platform) -- [containership]
 </li>
 <li>
  <a href="https://github.com/coreos">
   CoreOS
  </a>
  (Linux for Massive Server Deployments) -- https://coreos.com/
 </li>
 <li>
  <a href="http://decking.io/">
   Decking
  </a>
  : (Decking aims to simplify the creation, organsation and running of clusters of Docker containers in a way which is familiar to developers)
 </li>
 <li>
  <a href="https://docs.mesosphere.com/usage/tutorials/containerized-app/">
   Deploying a Containerized App on a Public Node with Mesos
  </a>
  (Docker plus Mesosphere provides an easy way to automate and scale deployment of containers in a production environment)
 </li>
 <li>
  <a href="https://github.com/ClusterHQ/flocker">
   Flocker
  </a>
  <sup>
   &#9733 2285, pushed 1 days ago
  </sup>
  (Flocker is a data volume manager and multi-host Docker cluster management tool) by
  <a href="https://github.com/ClusterHQ">
   @ClusterHQ
  </a>
 </li>
 <li>
  <a href="https://github.com/marmelab/gaudi">
   Gaudi
  </a>
  <sup>
   &#9733 598, pushed 543 days ago
  </sup>
  (Gaudi allows to share multi-component applications, based on Docker,  Go, and YAM) ~~ project discontinued.
 </li>
 <li>
  <a href="https://github.com/kontena/kontena">
   Kontena
  </a>
  <sup>
   &#9733 657, pushed 1 days ago
  </sup>
  (Application Containers for Masses) -- https://www.kontena.io/
 </li>
 <li>
  <a href="http://kubernetes.io">
   Kubernetes
  </a>
  (Open source orchestration system for Docker containers by Google)  -- [kubernetes] See Also
  <a href="https://github.com/ramitsurana/awesome-kubernetes">
   awesome-kubernetes
  </a>
  by
  <a href="https://github.com/ramitsurana">
   @ramitsurana
  </a>
 </li>
 <li>
  <a href="https://github.com/toscanini/maestro">
   Maestro
  </a>
  <sup>
   &#9733 607, pushed 987 days ago
  </sup>
  (Maestro provides the ability to easily launch, orchestrate and manage mulitiple Docker containers as single unit) by
  <a href="https://github.com/toscanini">
   @tascanini
  </a>
 </li>
 <li>
  <a href="https://mesosphere.github.io/marathon/docs/">
   Marathon
  </a>
  (Marathon is a private PaaS built on Mesos. It automatically handles hardware or software failures and ensures that an app is "always on")
 </li>
 <li>
  <a href="https://www.nomadproject.io/">
   Nomad Project
  </a>
  Easily deploy applications at any scale. A Distributed, Highly Available, Datacenter-Aware Scheduler.
 </li>
 <li>
  <a href="https://github.com/CenturyLinkLabs/panamax-ui/wiki">
   Panamax
  </a>
  (Docker Management for Humans) -- [panamax.io]
 </li>
 <li>
  <a href="https://github.com/rancher/rancher">
   Rancher
  </a>
  <sup>
   &#9733 3327, pushed 3 days ago
  </sup>
  (Portable AWS-style infrastructure service for Docker) -- http://rancher.com/
 </li>
 <li>
  <a href="https://github.com/coreos/fleet">
   Fleet
  </a>
  <sup>
   &#9733 2173, pushed 4 days ago
  </sup>
  (A Distributed init System providing low-level orchestration ) -- [coreos.com]
 </li>
 <li>
  <a href="https://github.com/hashicorp/serf">
   Serf
  </a>
  <sup>
   &#9733 3510, pushed 1 days ago
  </sup>
  (Service orchestration and management tool) by
  <a href="https://github.com/hashicorp">
   @hashicorp
  </a>
 </li>
 <li>
  <a href="https://github.com/shipyard/shipyard">
   Shipyard
  </a>
  <sup>
   &#9733 4644, pushed 5 days ago
  </sup>
  (Composable Docker Management) -- http://shipyard-project.com/
 </li>
 <li>
  <a href="https://github.com/m4ce/mcollective-docker-agent">
   MCollective Docker Agent
  </a>
  <sup>
   &#9733 1, pushed 29 days ago
  </sup>
  Uses MCollective to orchestrate your Docker containers and images --
  <a href="https://github.com/m4ce">
   @m4ce
  </a>
 </li>
 <li>
  <a href="https://github.com/ElasticBox/elastickube">
   ElasticKube
  </a>
  <sup>
   &#9733 79, pushed 4 days ago
  </sup>
  open source management platform for Kubernetes.
 </li>
 <li>
  <a href="https://github.com/ciscocloud/mantl">
   Mantl
  </a>
  <sup>
   &#9733 2237, pushed 4 days ago
  </sup>
  Mantl is a modern platform for rapidly deploying globally distributed services
  <a href="http://mantl.io">
   @ciscocloud
  </a>
 </li>
</ul>
<h2>
 Security
</h2>
<ul>
 <li>
  <a href="https://github.com/docker/docker-bench-security">
   docker-bench-security
  </a>
  <sup>
   &#9733 1313, pushed 3 days ago
  </sup>
  script that checks for dozens of common best-practices around deploying Docker containers in production. By
  <a href="https://github.com/docker">
   @docker
  </a>
 </li>
 <li>
  <a href="https://github.com/docker/notary">
   notary
  </a>
  <sup>
   &#9733 617, pushed 4 days ago
  </sup>
  a server and a client for running and interacting with trusted collections. By
  <a href="https://github.com/docker">
   @docker
  </a>
 </li>
 <li>
  <a href="https://www.twistlock.com/">
   Twistlock
  </a>
  Twistlock Security Suite detects vulnerabilities, hardens container images, and enforces security policies across the lifecycle of applications.
 </li>
 <li>
  <a href="https://github.com/coreos/clair">
   Clair
  </a>
  <sup>
   &#9733 1105, pushed 5 days ago
  </sup>
  Clair is an open source project for the static analysis of vulnerabilities in appc and docker containers. By
  <a href="https://github.com/coreos">
   @coreos
  </a>
 </li>
</ul>
<h2>
 Service Discovery
</h2>
<ul>
 <li>
  <a href="https://github.com/gliderlabs/docker-consul">
   docker-consul
  </a>
  <sup>
   &#9733 875, pushed 42 days ago
  </sup>
  by
  <a href="https://github.com/progrium">
   @progrium
  </a>
 </li>
 <li>
  <a href="https://github.com/coreos/etcd">
   etcd
  </a>
  <sup>
   &#9733 9440, pushed 2 days ago
  </sup>
  : A highly-available key value store for shared configuration and service discovery by
  <a href="https://github.com/coreos">
   @coreOS
  </a>
 </li>
 <li>
  <a href="https://github.com/cpuguy83/docker-grand-ambassador">
   Docker Grand Ambassador
  </a>
  <sup>
   &#9733 181, pushed 469 days ago
  </sup>
  This is a fully dynamic docker link ambassador. +
  <a href="https://docs.docker.com/engine/articles/ambassador_pattern_linking/">
   Article
  </a>
  by
  <a href="https://github.com/cpuguy83">
   @cpuguy83
  </a>
 </li>
 <li>
  <a href="https://github.com/factorish/proxy">
   proxy
  </a>
  <sup>
   &#9733 42, pushed 373 days ago
  </sup>
  : lightweight nginx based load balancer self using service discovery provided by registrator. by
  <a href="https://github.com/factorish">
   @factorish
  </a>
 </li>
 <li>
  <a href="https://github.com/ahmetalpbalkan/wagl/">
   wagl
  </a>
  : Service discovery for docker swarm using DNS
 </li>
</ul>
<h1>
 Slides
</h1>
<ul>
 <li>
  <a href="http://www.slideshare.net/Docker">
   Docker Slideshare Account
  </a>
 </li>
 <li>
  <a href="http://www.slideshare.net/jpetazzo">
   Docker Security
  </a>
  with
  <a href="https://github.com/jpetazzo">
   @jpetazzo
  </a>
 </li>
 <li>
  <a href="http://www.slideshare.net/JohanJanssen4/hide-your-development-environment-and-application-in-a-container">
   Hide your DEV ENV in a container
  </a>
  by
  <a href="https://twitter.com/johanjanssen42">
   @johanjanssen42
  </a>
 </li>
</ul>
<h1>
 Videos
</h1>
<h2>
 Main Account
</h2>
<ul>
 <li>
  <a href="https://www.youtube.com/user/dockerrun">
   Docker Youtube Account
  </a>
 </li>
 <li>
  <a href="https://www.youtube.com/playlist?list=PL_q4Fk7SVBCIjyuCBFBItXnzGI3qBa2L1">
   CenturyLink Labs Docker Interviews
  </a>
 </li>
 <li>
  <a href="https://www.youtube.com/channel/UCvksXSnLqIVM_uFB7xyrsSg/videos">
   Container Camp
  </a>
  Conference about
  <em>
   containers
  </em>
  !!!
  <a href="https://twitter.com/containercamp">
   @containercamp
  </a>
 </li>
 <li>
  <a href="https://www.youtube.com/channel/UCOAhkxpryr_BKybt9wIw-NQ/videos">
   Quoi d'neuf Docker
  </a>
  <strong>
   FRENCH
  </strong>
  chronique vidéo sur Youtube proposant de courtes vidéos (maximum 15 minutes) sur la thématique "Docker et son écosystème"
  <a href="http://www.quoidneufdocker.xyz/">
   Site Web
  </a>
 </li>
</ul>
<h2>
 Useful videos
</h2>
<ul>
 <li>
  <a href="https://www.youtube.com/watch?v=oZ45v8AeE7k">
   Ansible and Docker HP
  </a>
  (32:38)
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=1qlLUf7KtAw">
   Container Hacks and Fun Images
  </a>
  by
  <a href="https://github.com/jfrazelle">
   @jfrazelle
  </a>
  @ DockerCon 2015 (
  <strong>
   MUST WATCH VIDEO
  </strong>
  : 38:50)
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=1jwo8-1HYYg">
   Contributing to Docker by Andrew "Tianon" Page (InfoSiftr)
  </a>
  (34:31)
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=FdkNAjjO5yQ">
   Docker for Developers
  </a>
  (54:26) by
  <a href="https://github.com/jpetazzo">
   @jpetazzo
  </a>
  <== Good introduction, context, demo
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=Glk5d5WP6MI">
   Docker in Production
  </a>
  by
  <a href="https://github.com/jpetazzo">
   @jpetazzo
  </a>
  (36:05)
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=CAewZCBT4PI">
   Docker: How to Use Your Own Private Registry
  </a>
  (15:01)
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=zWGFqMuEHdw">
   Docker and SELinux by Daniel Walsh from Red Hat
  </a>
  (40:23)
 </li>
 <li>
  <a href="https://vimeo.com/110835013">
   Extending Docker with Plugins
  </a>
  (15:21)
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=7CZFpHUPqXw">
   From Local Docker Development to Production Deployments
  </a>
  by
  <a href="https://github.com/jpetazzo">
   @jpetazzo
  </a>
  @ AWS re:Invent 2015
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=GaHzdqFithc">
   Immutable Infrastructure with Docker and EC2 by Michael Bryzek (Gilt)
  </a>
  (42:04)
 </li>
 <li>
  <a href="https://vimeo.com/123341629">
   Logging on Docker: What You Need to Know
  </a>
  (51:27)
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=6f2E6PKYb0w">
   Performance Analysis of Docker - Jeremy Eder
  </a>
  (1:36:58)
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=u5jd9YT9EsY">
   Run Any App on Mesos on Any Infrastructure Using Docker
  </a>
  (17:44)
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=IiITP3yIRd8">
   State of containers: a debate with CoreOS, VMware and Google
  </a>
  (27:38)
 </li>
 <li>
  <a href="https://sysadmincasts.com/episodes/31-introduction-to-docker">
   SysAdminCasts: Introduction to Docker
  </a>
  (15:49)
 </li>
</ul>
<h1>
 Interesting Twitter Accounts
</h1>
<ul>
 <li>
  <a href="https://twitter.com/docker">
   Docker
  </a>
 </li>
 <li>
  <a href="https://twitter.com/CenturyLinkLabs">
   CenturyLink Labs
  </a>
 </li>
 <li>
  <a href="https://twitter.com/Flux7Labs">
   Flux7Labs
  </a>
 </li>
 <li>
  <a href="https://twitter.com/tutumcloud">
   TutumCloud
  </a>
 </li>
 <li>
  <a href="https://twitter.com/ProjectAtomic">
   Project Atomic
  </a>
 </li>
 <li>
  <a href="https://twitter.com/openshift">
   OpenShift by Red Hat
  </a>
 </li>
 <li>
  <a href="https://twitter.com/YLDio">
   YLD
  </a>
 </li>
 <li>
  <a href="https://twitter.com/thenewstack">
   The New Stack
  </a>
 </li>
</ul>
<h2>
 People
</h2>
<ul>
 <li>
  <a href="https://twitter.com/solomonstre">
   Solomon Hykes
  </a>
  Founder of Docker
 </li>
 <li>
  <a href="https://twitter.com/gabrtv">
   Gabriel Monroy
  </a>
  Creator of Deis
 </li>
 <li>
  <a href="https://twitter.com/jpetazzo">
   Jérôme Petazzoni
  </a>
  Docker Developer
 </li>
 <li>
  <a href="https://twitter.com/crosbymichael">
   Michael Crosby
  </a>
  Docker Developer
 </li>
 <li>
  <a href="https://twitter.com/kartar">
   James Turnbull
  </a>
  Author of Docker Book
 </li>
 <li>
  <a href="https://twitter.com/progrium">
   Jeff Lindsay
  </a>
  Design-minded software architect
 </li>
 <li>
  <a href="https://twitter.com/frazelledazzell">
   Jessie Frazelle
  </a>
  Work @docker and uses full containerized desktop, lots of fun.
 </li>
</ul>
