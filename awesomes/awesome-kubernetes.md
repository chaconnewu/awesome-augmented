<h1>
 Awesome-Kubernetes
</h1>
<p>
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
 <a href="https://travis-ci.org/ramitsurana/awesome-kubernetes">
  <img alt="Build Status" src="https://travis-ci.org/ramitsurana/awesome-kubernetes.svg?branch=master"/>
 </a>
 <a href="http://creativecommons.org/licenses/by-nc/4.0/">
  <img alt="License" src="https://img.shields.io/badge/License-CC%204.0-brightgreen.svg"/>
 </a>
</p>
<p>
 A curated list for awesome kubernetes sources Inspired by
 <a href="https://github.com/sindresorhus/awesome">
  @sindresorhus' awesome
 </a>
</p>
<p>
 <img alt="k8" src="https://cloud.githubusercontent.com/assets/8342133/13547481/fcb5ffb0-e2fa-11e5-8f75-555cea5eb7b2.png"/>
</p>
<blockquote>
 <p>
  "Talent wins games, but teamwork and intelligence wins championships."
 </p>
 <p>
  -- Michael Jordan
 </p>
</blockquote>
<p>
 Without the help from these
 <a href="https://github.com/ramitsurana/awesome-kubernetes/graphs/contributors">
  amazing contributors
 </a>
 ,
building this awesome-repo would never has been possible, Thank You very much guys !!
</p>
<p>
 <strong>
  Thanks to Gitbook.This awesome list can now be downloaded and read in the form of a book.Check it out -->  https://www.gitbook.com/book/ramitsurana/awesome-kubernetes/ .Keep Learning Keep Sharing !!
 </strong>
</p>
<p>
 <strong>
  If you see a package or project here that is no longer maintained or is not a good fit, please submit a pull request to improve this file. Thank you!
 </strong>
</p>
<h2>
 What is Kubernetes? :ship:
</h2>
<blockquote>
 <p>
  Kubernetes is an open source orchestration system for Docker containers. It handles scheduling onto nodes in a compute cluster and actively manages workloads to ensure that their state matches the users declared intentions. Using the concepts of "labels" and "pods", it groups the containers which make up an application into logical units for easy management and discovery.
 </p>
</blockquote>
<p>
 <em>
  Source:
 </em>
 <a href="http://kubernetes.io/">
  What is Kubernetes
 </a>
</p>
<h2>
 History:
</h2>
<p>
 <strong>
  Kubernetes is known to be a descendant of Google's system BORG
 </strong>
</p>
<blockquote>
 <p>
  The first unified container-management system developed at Google was the system we internally call Borg.
  It was built to manage both long-running services and batch jobs, which had previously been handled by two separate
  systems: Babysitter and the Global Work Queue. The latter’s architecture strongly influenced Borg, but was focused on
  batch jobs; both predated Linux control groups.
 </p>
</blockquote>
<p>
 <em>
  Source:
 </em>
 <a href="http://research.google.com/pubs/archive/44843.pdf">
  Kubernetes Past
 </a>
</p>
<h2>
 Date of Birth:
</h2>
<p>
 Kubernetes celebrates its birthday every year on 21st July.The project was born in the year 2015.
</p>
<h2>
 Roadmap
</h2>
<p>
 The awesome-kubernetes will now soon be available in the form of different releases and package bundles, It means that you can
download the awesome kubernetes release up to a certain period of time, The release for awesome kubernetes 2015 bundle is released.Checkout the releases column for more info.Stay tuned for more updates.
</p>
<hr/>
<h1>
 Menu
</h1>
<ul>
 <li>
  <a href="#starting-point">
   Starting Point
  </a>
 </li>
 <li>
  <a href="#main-resources">
   Main Resources
  </a>
 </li>
 <li>
  <a href="#useful-articles">
   Useful Articles
  </a>
 </li>
 <li>
  <a href="#cloud-providers">
   Cloud Providers
  </a>
 </li>
 <li>
  <a href="#components">
   Components
  </a>
 </li>
 <li>
  <a href="#related-projects">
   Related Projects
  </a>
  <ul>
   <li>
    <a href="#related-software">
     Related Software
    </a>
   </li>
   <li>
    <a href="#hypernetes">
     Hypervisor-Agnostic Docker Engine
    </a>
   </li>
   <li>
    <a href="#helm-package-manager">
     Helm Package Manager
    </a>
   </li>
   <li>
    <a href="#ubernetes">
     Ubernetes
    </a>
   </li>
   <li>
    <a href="#fabric8">
     Fabric8
    </a>
   </li>
   <li>
    <a href="#kmachine">
     kmachine
    </a>
   </li>
   <li>
    <a href="#spread">
     spread
    </a>
   </li>
   <li>
    <a href="#supergiant">
     Supergiant
    </a>
   </li>
   <li>
    <a href="#monitoring-services">
     Monitoring Services
    </a>
   </li>
   <li>
    <a href="#paasproviders">
     Paas Providers
    </a>
   </li>
   <li>
    <a href="#openshift">
     OpenShift
    </a>
   </li>
   <li>
    <a href="#deis">
     Deis
    </a>
   </li>
   <li>
    <a href="#continuousdelivery">
     Continuous Delivery
    </a>
   </li>
   <li>
    <a href="#fabric8">
     Fabric8
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#container-support">
   Container Support
  </a>
 </li>
 <li>
  <a href="#raspberry-pi">
   Raspberry Pi
  </a>
 </li>
 <li>
  <a href="#books">
   Books
  </a>
  :books:
 </li>
 <li>
  <a href="#slide-presentations">
   Slide Presentations
  </a>
 </li>
 <li>
  <a href="#videos">
   Videos
  </a>
  :tv:
  <ul>
   <li>
    <a href="#main-account">
     Main Account
    </a>
   </li>
   <li>
    <a href="#other-useful-videos">
     Other Useful videos
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#interactive-learning-environments">
   Interactive Learning Environments
  </a>
 </li>
 <li>
  <a href="#interesting-twitter-accounts">
   Interesting Twitter Accounts
  </a>
 </li>
 <li>
  <a href="#amazing-people">
   Amazing People
  </a>
 </li>
 <li>
  <a href="#connecting-with-kubernetes">
   Connecting with Kubernetes
  </a>
 </li>
 <li>
  <a href="#companies">
   Companies
  </a>
 </li>
 <li>
  <a href="#conferences">
   Conferences
  </a>
 </li>
 <li>
  <a href="#contributing">
   Contributing
  </a>
 </li>
 <li>
  <a href="#license">
   License
  </a>
 </li>
</ul>
<hr/>
<h1>
 Starting Point
</h1>
<p>
 <em>
  A place that marks the beginning of a journey
 </em>
</p>
<ul>
 <li>
  <a href="http://www.jetstack.io/new-blog/2015/6/19/are-you-ready-to-manage-your-infrastructure-like-google-kubernetes-coming-to-a-cloud-near-you">
   Are you Ready to Manage your Infrastructure like Google?
  </a>
 </li>
 <li>
  <a href="http://www.businessinsider.in/Google-is-years-ahead-when-it-comes-to-the-cloud-but-its-happy-the-world-is-catching-up/articleshow/47793327.cms">
   Google is years ahead when it comes to the cloud, but it's happy the world is catching up
  </a>
 </li>
 <li>
  <a href="https://www.ctl.io/developers/blog/post/what-is-kubernetes-and-how-to-use-it/">
   An Intro to Google’s Kubernetes and How to Use It
  </a>
  by
  <a href="https://twitter.com/rhein_wein">
   Laura Frank
  </a>
 </li>
 <li>
  <a href="http://containertutorials.com/get_started_kubernetes/index.html">
   Getting Started on Kubernetes
  </a>
  by
  <a href="https://twitter.com/rajdeepdua">
   Rajdeep Dua
  </a>
 </li>
 <li>
  <a href="https://meteorhacks.com/learn-kubernetes-the-future-of-the-cloud/">
   Kubernetes: The Future of Cloud Hosting
  </a>
  by
  <a href="https://twitter.com/meteorhacks">
   Meteorhacks
  </a>
 </li>
 <li>
  <a href="https://thevirtualizationguy.wordpress.com/tag/kubernetes/">
   Kubernetes by Google
  </a>
  by
  <a href="https://twitter.com/GastonPantana">
   Gaston Pantana
  </a>
 </li>
 <li>
  <a href="http://blog.arungupta.me/key-concepts-kubernetes/">
   Key Concepts
  </a>
  by
  <a href="https://twitter.com/arungupta">
   Arun Gupta
  </a>
 </li>
 <li>
  <a href="http://keithtenzer.com/2015/06/01/application-containers-kubernetes-and-docker-from-scratch/">
   Application Containers: Kubernetes and Docker from Scratch
  </a>
  by
  <a href="https://twitter.com/keithtenzer">
   Keith Tenzer
  </a>
 </li>
 <li>
  <a href="http://omerio.com/2015/12/18/learn-the-kubernetes-key-concepts-in-10-minutes/">
   Learn the Kubernetes Key Concepts in 10 Minutes
  </a>
  by
  <a href="https://twitter.com/omerio">
   Omer Dawelbeit
  </a>
 </li>
 <li>
  <a href="https://supergiant.io/blog/top-reasons-businesses-should-move-to-kubernetes-now">
   Top Reasons Businesses Should Move to Kubernetes Now
  </a>
  by
  <a href="https://github.com/gopherstein">
   Mike Johnston
  </a>
 </li>
 <li>
  <a href="https://deis.com/blog/2016/kubernetes-illustrated-guide/">
   The Children's Illustrated Guide to Kubernetes
  </a>
  by
  <a href="https://github.com/deis">
   Deis
  </a>
 </li>
 <li>
  <a href="https://medium.com/@mhausenblas/the-kubectl-run-command-27c68de5cb76#.mlwi5an7o">
   The ‘kubectl run’ command
  </a>
  by
  <a href="https://twitter.com/mhausenblas">
   Michael Hausenblas
  </a>
 </li>
</ul>
<h1>
 Main Resources
</h1>
<p>
 <em>
  Official resources from the Kubernetes team
 </em>
</p>
<ul>
 <li>
  <a href="http://kubernetes.io/docs/">
   Kubernetes Documentation
  </a>
 </li>
 <li>
  <a href="https://github.com/kubernetes/kubernetes/">
   Kubernetes Source
  </a>
 </li>
 <li>
  <a href="http://kubernetes.io/docs/troubleshooting/">
   Kubernetes Troubleshooting
  </a>
 </li>
</ul>
<h1>
 Useful Articles
</h1>
<p>
 <em>
  A piece of writing included with others in a newspaper, magazine, or other publication
 </em>
</p>
<ul>
 <li>
  <a href="http://www.jetstack.io/new-blog/2015/7/6/getting-started-with-a-local-deployment">
   Kubernetes: Getting Started With a Local Deployment
  </a>
 </li>
 <li>
  <a href="http://severalnines.com/blog/installing-kubernetes-cluster-minions-centos7-manage-pods-services">
   Installation on Centos 7
  </a>
 </li>
 <li>
  <a href="http://blog.arungupta.me/kubernetes-application-package-multiple-resources-together/">
   Packaging Multiple Resources together
  </a>
 </li>
 <li>
  <a href="https://www.digitalocean.com/community/tutorials/an-introduction-to-kubernetes">
   An Introduction to Kubernetes
  </a>
  by
  <a href="https://twitter.com/jmellingwood">
   Justin Ellingwood
  </a>
 </li>
 <li>
  <a href="http://www.infoq.com/articles/scaling-docker-with-kubernetes">
   Scaling Docker with Kubernetes
  </a>
  by
  <a href="https://twitter.com/csanchez">
   Carlos Sanchez
  </a>
 </li>
 <li>
  <a href="https://access.redhat.com/articles/1353773">
   Creating a Kubernetes Cluster to Run Docker Formatted Container Images
  </a>
  by
  <a href="https://twitter.com/linuxcricket">
   Chris Negus
  </a>
 </li>
 <li>
  <a href="https://www.linkedin.com/pulse/containerizing-docker-kubernetes-ramit-surana">
   Containerizing Docker on Kubernetes !!
  </a>
  by
  <a href="https://twitter.com/ramitsurana">
   Ramit Surana
  </a>
 </li>
 <li>
  <a href="https://coreos.com/blog/running-kubernetes-example-on-CoreOS-part-1/">
   Running Kubernetes Example on CoreOS, Part 1
  </a>
  by
  <a href="https://twitter.com/kelseyhightower">
   Kelsey Hightower
  </a>
 </li>
 <li>
  <a href="https://zwischenzugs.wordpress.com/2015/04/06/play-with-kubernetes-quickly-using-docker/">
   Play With Kubernetes Quickly Using Docker
  </a>
 </li>
 <li>
  <a href="http://sebgoa.blogspot.in/2015/04/1-command-to-kubernetes-with-docker.html">
   1 command to Kubernetes with Docker compose
  </a>
  by
  <a href="https://twitter.com/sebgoa">
   Sebastien Goasguen
  </a>
 </li>
 <li>
  <a href="http://containertutorials.com/get_started_kubernetes/k8s_example.html">
   Nginx Server Deployment using Kubernetes
  </a>
  by
  <a href="https://www.twitter.com/rajdeepdua">
   Rajdeep Dua
  </a>
 </li>
 <li>
  <a href="http://kamalmarhubi.com/blog/2015/08/27/what-even-is-a-kubelet/">
   What even is a kubelet?
  </a>
  by
  <a href="https://twitter.com/kamalmarhubi">
   Kamal Marhubi
  </a>
 </li>
 <li>
  <a href="http://kamalmarhubi.com/blog/2015/09/06/kubernetes-from-the-ground-up-the-api-server/">
   Kubernetes from the ground up: the API server
  </a>
  by
  <a href="https://twitter.com/kamalmarhubi">
   Kamal Marhubi
  </a>
 </li>
 <li>
  <a href="http://www.dasblinkenlichten.com/kubernetes-101-networking/">
   Kubernetes 101 – Networking
  </a>
  by
  <a href="https://twitter.com/blinken_lichten">
   Jon Langemak
  </a>
 </li>
 <li>
  <a href="http://www.dasblinkenlichten.com/dynamic-kubernetes-installationconfiguration-with-saltstack/">
   Dynamic Kubernetes installation/configuration with SaltStack
  </a>
  by
  <a href="https://twitter.com/blinken_lichten">
   Jon Langemak
  </a>
 </li>
 <li>
  <a href="http://www.dasblinkenlichten.com/deploying-kubernetes-with-saltstack/">
   Deploying Kubernetes with SaltStack
  </a>
  by
  <a href="https://twitter.com/blinken_lichten">
   Jon Langemak
  </a>
 </li>
 <li>
  <a href="http://www.dasblinkenlichten.com/logging-in-kubernetes-with-fluentd-and-elasticsearch/">
   Logging in Kubernetes with Fluentd and Elasticsearch
  </a>
  by
  <a href="https://twitter.com/blinken_lichten">
   Jon Langemak
  </a>
 </li>
 <li>
  <a href="https://developer.rackspace.com/blog/running-coreos-and-kubernetes/">
   Corekube: Running Kubernetes on CoreOS via OpenStack
  </a>
  by
  <a href="https://twitter.com/mikemetral">
   Mike Metral
  </a>
 </li>
 <li>
  <a href="http://www.weave.works/guides/networking-kubernetes-clusters-on-coreos-with-weave/">
   Networking Kubernetes Clusters on CoreOS with Weave
  </a>
  by
  <a href="https://twitter.com/weaveworks">
   Weaveworks
  </a>
 </li>
 <li>
  <a href="https://coreos.com/kubernetes/docs/latest/getting-started.html">
   CoreOS + Kubernetes Step By Step
  </a>
  by
  <a href="https://twitter.com/coreoslinux">
   Coreos
  </a>
 </li>
 <li>
  <a href="https://www.ctl.io/developers/blog/post/deploying-to-kubernetes-with-panamax/">
   Deploying to Kubernetes with Panamax
  </a>
  by
  <a href="https://twitter.com/bdehamer">
   Brian DeHamer
  </a>
 </li>
 <li>
  <a href="http://www.projectatomic.io/blog/2015/08/fun-with-kubenetes-and-atomicapp/">
   Deploy Kubernetes with a Single Command Using Atomicapp
  </a>
  by
  <a href="https://twitter.com/jasonbrooks">
   Jason Brooks
  </a>
 </li>
 <li>
  <a href="http://blog.jameskyle.org/2014/08/deploying-baremetal-kubernetes-cluster/">
   Deploying a Bare Metal Kubernetes Cluster
  </a>
  by
  <a href="https://twitter.com/jameskyle75">
   James Kyle
  </a>
 </li>
 <li>
  <a href="http://awsadvent.tumblr.com/post/104260597799/aws-advent-2014-coreos-and-kubernetes-on-aws">
   AWS Advent 2014 - CoreOS and Kubernetes on AWS
  </a>
  by
  <a href="https://twitter.com/dysinger">
   Tim Dsyinger
  </a>
 </li>
 <li>
  <a href="http://ben.straub.cc/2015/08/19/kubernetes-aws-vpc-peering/">
   Kubernetes and AWS VPC Peering
  </a>
  by
  <a href="https://twitter.com/benstraub">
   Ben Straub
  </a>
 </li>
 <li>
  <a href="https://insights.ubuntu.com/2015/07/23/deploy-a-kubernetes-development-cluster-with-juju-2/">
   Deploy a Kubernetes development cluster with Juju!
  </a>
  by
  <a href="https://twitter.com/mattatcanonical">
   Matt Bruzek
  </a>
 </li>
 <li>
  <a href="http://lollyrock.com/articles/kubernetes-vagrant/">
   Try Kubernetes with Vagrant
  </a>
  by
  <a href="https://twitter.com/chri_hartmann">
   Christoph Hartmann
  </a>
 </li>
 <li>
  <a href="http://blog.keycloak.org/2015/04/keycloak-on-kubernetes-with-openshift-3.html">
   Keycloak on Kubernetes with OpenShift 3
  </a>
  by
  <a href="https://twitter.com/mstruk2000">
   Marko Strukelj
  </a>
 </li>
 <li>
  <a href="https://ttboj.wordpress.com/2015/05/02/kubernetes-clusters-with-oh-my-vagrant/">
   Kubernetes clusters with Oh-My-Vagrant
  </a>
  by
  <a href="https://twitter.com/#!/purpleidea">
   James
  </a>
 </li>
 <li>
  <a href="http://blog.michaelhamrah.com/2015/06/fleet-unit-files-for-kubernetes-on-coreos/">
   Fleet Unit Files for Kubernetes on CoreOS
  </a>
  by
  <a href="https://twitter.com/mhamrah">
   Michael Hamrah
  </a>
 </li>
 <li>
  <a href="https://coreos.com/kubernetes/docs/latest/kubernetes-on-aws.html">
   Kubernetes on AWS
  </a>
  by
  <a href="https://twitter.com/coreoslinux">
   CoreOS
  </a>
 </li>
 <li>
  <a href="http://alanwill.me/Testing-Kubernetes-on-AWS/">
   Testing Kubernetes on AWS
  </a>
  by
  <a href="https://twitter.com/alanwill">
   Alan Will
  </a>
 </li>
 <li>
  <a href="http://blog.dutchcoders.io/kubernetes-first-steps-on-amazon-aws/">
   Kubernetes: First steps on Amazon AWS
  </a>
  by
  <a href="http://blog.dutchcoders.io/author/remco/">
   Remco
  </a>
 </li>
 <li>
  <a href="http://keithtenzer.com/2015/05/04/kubernetes-container-orchestration-through-java-apis/">
   Kubernetes Container Orchestration through Java APIs
  </a>
  by
  <a href="https://twitter.com/keithtenzer">
   Keith Tenzer
  </a>
 </li>
 <li>
  <a href="http://keithtenzer.com/2015/04/15/containers-at-scale-with-kubernetes-on-openstack/">
   Containers at Scale with Kubernetes on OpenStack
  </a>
  by
  <a href="https://twitter.com/keithtenzer">
   Keith Tenzer
  </a>
 </li>
 <li>
  <a href="http://www.dasblinkenlichten.com/installing-cadvisor-and-heapster-on-bare-metal-kubernetes/">
   Installing cAdvisor and Heapster on bare metal Kubernetes
  </a>
  by
  <a href="https://twitter.com/blinken_lichten">
   Jon Langemak
  </a>
 </li>
 <li>
  <a href="http://technologyconversations.com/2015/11/04/docker-clustering-tools-compared-kubernetes-vs-docker-swarm/">
   Docker Clustering Tools Compared: Kubernetes vs Docker Swarm
  </a>
 </li>
 <li>
  <a href="http://machinezone.github.io/research/networking-solutions-for-kubernetes/">
   Comparison of Networking Solutions for Kubernetes
  </a>
 </li>
 <li>
  <a href="https://www.sdxcentral.com/articles/news/why-docker-and-google-kubernetes-are-like-paas-done-right/2015/08/">
   Why Docker and Google Kubernetes Are Like PaaS Done Right
  </a>
 </li>
 <li>
  <a href="http://www.dasblinkenlichten.com/kubernetes-authentication-plugins-and-kubeconfig/">
   Kubernetes Authentication plugins and kubeconfig
  </a>
  by
  <a href="https://twitter.com/blinken_lichten">
   Jon Langemak
  </a>
 </li>
 <li>
  <a href="http://www.dasblinkenlichten.com/kubernetes-with-saltstack-revisited/">
   Kubernetes with SaltStack revisited
  </a>
  by
  <a href="https://twitter.com/blinken_lichten">
   Jon Langemak
  </a>
 </li>
 <li>
  <a href="http://www.devoperandi.com/kubernetes-authentication-openid-connect/">
   Kubernetes Authentication - OpenID Connect
  </a>
  by
  <a href="https://twitter.com/DevoperandI">
   Michael Ward
  </a>
 </li>
 <li>
  <a href="http://www.devoperandi.com/logging-kafka-topic-by-kubernetes-namespace/">
   Logging - Kafka topic by namespace
  </a>
  by
  <a href="https://twitter.com/DevoperandI">
   Michael Ward
  </a>
 </li>
 <li>
  <a href="http://theremotelab.com/blog/achieving-ci-cd-with-k8s/">
   Achieving CI/CD with Kubernetes
  </a>
  by
  <a href="https://twitter.com/ramitsurana">
   Ramit Surana
  </a>
 </li>
</ul>
<h1>
 Cloud Providers
</h1>
<p>
 <em>
  Coming Soon
 </em>
</p>
<ul>
 <li>
  <a href="https://cloud.google.com/compute/">
   GCE
  </a>
  - Google Compute Engine [default]
 </li>
 <li>
  [GKE] - Google Container Engine
 </li>
 <li>
  <a href="aws.amazon.com/ec2‎">
   AWS
  </a>
  - Amazon EC2
 </li>
 <li>
  <a href="https://azure.microsoft.com/en-in/">
   Azure
  </a>
  - Microsoft Azure
 </li>
 <li>
  <a href="http://www.vmware.com/products/vsphere.html">
   Vsphere
  </a>
  - VMWare VSphere
 </li>
 <li>
  <a href="https://www.rackspace.com/en-in">
   Rackspace
  </a>
  - Rackspace
 </li>
</ul>
<h1>
 Components
</h1>
<p>
 <em>
  Comprehensive list of Components of Kubernetes
 </em>
</p>
<h3>
 <a href="http://kubernetes.io/docs/user-guide/prereqs/">
  Kubectl
 </a>
</h3>
<p>
 It is a command-line tool. It lets you inspect your cluster resources, create, delete, and update components, and much more.
</p>
<p>
 <em>
  More Info
  <a href="http://kubernetes.io/docs/user-guide/kubectl-cheatsheet/">
   Kubectl Cheatsheet
  </a>
 </em>
</p>
<p>
 <em>
  Coming Soon
 </em>
</p>
<h1>
 Related Projects
</h1>
<p>
 <em>
  Kubernetes-related projects that you might find helpful
 </em>
</p>
<h2>
 Related Software
</h2>
<p>
 <em>
  Projects built to make life with Kubernetes even better, more powerful, more scalable
 </em>
</p>
<h3>
 <a href="https://github.com/hyperhq/hypernetes">
  Hypernetes
 </a>
</h3>
<p>
 Hypernetes is a secure, multi-tenant Kubernetes distro. Simply put,
</p>
<p>
 Hypernetes = Bare-metal + Hyper + Kubernetes + KeyStone + Cinder + Neutron.
</p>
<p>
 It envisions a future of "Container-as-a-Service without IaaS". The idea is to combine the orchestration power in Kubernetes and the runtime isolation in Hyper to build the truly secure multi-tenant CaaS platform.
</p>
<h3>
 <a href="https://deis.com/blog/2015/introducing-helm-for-kubernetes">
  Helm Package Manager
 </a>
</h3>
<p>
 Built by Deis and Inspired by Homebrew, apt, and NPM. Helm is a tool for working with Kubernetes-powered applications. Helm makes it easy run apps and services inside Kubernetes.
</p>
<h3>
 <a href="https://github.com/kubernetes/kubernetes/blob/master/docs/proposals/federation.md">
  Ubernetes
 </a>
</h3>
<p>
 A central design concept in Kubernetes to cluster Kubernetes across several regions.
</p>
<h3>
 <a href="http://github.com/kubernetes/minikube/">
  Minikube
 </a>
</h3>
<p>
 Minikube is a tool that makes it easy to run Kubernetes locally. Minikube runs a single-node Kubernetes cluster inside a VM on your laptop for users looking to try out Kubernetes or develop with it day-to-day.
</p>
<h3>
 <a href="https://github.com/skippbox/kmachine">
  kmachine
 </a>
</h3>
<p>
 kmachine lets you create Docker hosts on your computer, on cloud providers, and inside your own data center. It creates servers, installs Docker on them, then configures the Docker client to talk to them just like docker-machine
</p>
<h3>
 <a href="https://github.com/redspread/spread">
  spread
 </a>
</h3>
<p>
 spread is a command line tool that builds and deploys a Docker project to a Kubernetes cluster in one command. The project's goals are to:
</p>
<ul>
 <li>
  Enable rapid iteration with Kubernetes
 </li>
 <li>
  Be the fastest, simplest way to deploy Docker to production
 </li>
 <li>
  Work well for a single developer or an entire team (no more broken bash scripts!)
 </li>
</ul>
<h3>
 <a href="https://supergiant.io">
  Supergiant
 </a>
</h3>
<p>
 Supergiant is open-source and built on Kubernetes. It provisions "cost-based" server resources, load balancers, and block-level storage automatically to support stateful apps at scale with less hardware expense. The goals of the project are to make launching, managing, and scaling Kubernetes as easy as possible.
</p>
<h3>
 <a href="https://opencredo.com/introducing-kubefuse-file-system-kubernetes/">
  Kubefuse
 </a>
</h3>
<p>
 Kubernetes as a Filesystem.Its written in Python, because Python is still cool and has a solid FUSE library available for it. The fusepy library has some simple examples showing how to implement loopback and memory file systems.
</p>
<h3>
 <a href="https://docs.kubespray.io/">
  KubeSpray
 </a>
</h3>
<p>
 KubeSpray is a tool to deploy a kubernetes cluster with Ansible.
</p>
<h3>
 <a href="https://github.com/coreos/bootkube">
  Bootkube
 </a>
</h3>
<p>
 Bootkube is a helper tool for launching self-hosted Kubernetes clusters.When launched, bootkube will act as a temporary Kubernetes control-plane (api-server, scheduler, controller-manager), which operates long enough to bootstrap a replacement self-hosted control-plane.Additionally, bootkube can be used to generate all of the necessary assets for use in bootstrapping a new cluster. These assets can then be modified to support any additional configuration options.
</p>
<h3>
 <a href="https://github.com/redspread/localkube">
  Localkube
 </a>
</h3>
<p>
 It provides a Kubernetes cluster configured to run locally and optimized for rapid development.It is a single executable container process built for usage with
 <a href="https://github.com/redspread/spread">
  spread
 </a>
 .
</p>
<h3>
 <a href="https://github.com/dtan4/k8sec">
  K8sec
 </a>
</h3>
<p>
 CLI tool to manage Kubernetes Secrets easily
</p>
<h3>
 <a href="https://github.com/openai/kubernetes-ec2-autoscaler">
  Kubernetes Ec2 Autoscaler
 </a>
</h3>
<p>
 Node-level autoscaler for Kubernetes on AWS EC2 that is designed for batch jobs.
</p>
<h2>
 Monitoring Services
</h2>
<p>
 <em>
  To maintain regular surveillance over kubernetes
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/kubernetes/dashboard">
   Console
  </a>
  :
It is a general purpose, web-based UI for Kubernetes clusters. It allows to manage applications running in the cluster, troubleshoot them, as well as, manage the cluster itself.
  <sup>
   &#9733 213, pushed 127 days ago
  </sup>
 </li>
 <li>
  <a href="https://www.datadoghq.com/">
   Datadog
  </a>
  :
Datadog is a hosted monitoring and metrics platform, with built in support for Kubernetes and Docker.  Their Kubernetes integration pulls in Docker and Kubernetes events, converts labels and pod names into tags, as well as pulls metrics from Docker and CAdvisor.  This allows you to build application dashboards and alerts that display data across pods, Nodes, and services.
 </li>
 <li>
  <a href="https://github.com/kubernetes/heapster">
   Heapster
  </a>
  :
Heapster enables Container Cluster Monitoring and Performance Analysis.
Heapster currently supports Kubernetes and CoreOS natively. It can be extended to support other cluster management solutions easily. Heapster collects and interprets various signals like compute resource usage, lifecycle events, etc, and exports cluster metrics via REST endpoints.
  <sup>
   &#9733 640, pushed 128 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/kubernetes/kubedash">
   Kubedash
  </a>
  :
Performance analytics UI for Kubernetes Clusters.
The goal of Kubedash is to allow the user or an administrator of a Kubernetes cluster to easily verify and understand the performance of a cluster and jobs running within it through intuitive visualizations of aggregated metrics, derived stats and event patterns. It is not intended to be a general-purpose Kubernetes UI. Instead, kubedash uses multiple sources of information to summarize and provide high-level analytic information to users and to the cluster administrator.
  <sup>
   &#9733 130, pushed 158 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/kubernetes/kube-ui">
   Kube-ui
  </a>
  :
Container Cluster Manager from Google Web UI
  <sup>
   &#9733 123, pushed 196 days ago
  </sup>
 </li>
 <li>
  <a href="http://prometheus.io">
   Prometheus
  </a>
  :
Prometheus is an open-source systems monitoring and alerting toolkit originally built at SoundCloud. Since its inception in 2012, many companies and organizations have adopted Prometheus, and the project has a very active developer and user community. It is now a standalone open source project and maintained independently of any company.
 </li>
 <li>
  <a href="http://www.sysdig.org/">
   Sysdig
  </a>
  :
Sysdig is open source, system-level exploration: capture system state and activity from a running Linux instance, then save,  filter and analyze. Sysdig is scriptable in Lua and includes a command line interface and a powerful interactive UI, csysdig, that runs in your terminal.
 </li>
 <li>
  <a href="https://www.weave.works/products/weave-scope/">
   Weave Scope
  </a>
  :
Weave Scope is a visualization, and monitoring tool for Docker and Kubernetes. It provides a top down view into your app as well as your entire infrastructure, and allows you to diagnose any problems with your distributed containerized app, in real time, as it being deployed to a cloud provider.
 </li>
</ul>
<h2>
 PaaS Providers
</h2>
<p>
 <em>
  Kubernetes Platform as a Service providers
 </em>
</p>
<h3>
 <a href="https://www.openshift.com/">
  OpenShift
 </a>
</h3>
<p>
 OpenShift is Red Hat's Platform-as-a-Service (PaaS) that allows developers to quickly develop, host, and scale applications in a cloud environment. With OpenShift you have a choice of offerings, including online, on premise, and open source project options.
</p>
<h3>
 <a href="https://deis.com/">
  Deis Workflow
 </a>
</h3>
<p>
 Deis Workflow is an open source PaaS that makes it easy to deploy and manage applications on your own servers. Workflow builds upon Kubernetes and Docker to provide a lightweight PaaS with a Heroku-inspired workflow.
</p>
<h2>
 Continuous Delivery
</h2>
<p>
 <em>
  Build-test-deploy automated workflow software designed to make production environments more stable and life better for engineers
 </em>
</p>
<h3>
 <a href="http://fabric8.io">
  Fabric8
 </a>
</h3>
<p>
 Fabric8 DevOps provides a completely integrated open source DevOps platform which works out of the box on any Kubernetes or OpenShift environment, The entire platform is modular and based on microservices so you can use as much or as little of Fabric8 DevOps as you wish!
</p>
<h3>
 <a href="https://jenkins.io">
  Jenkins
 </a>
</h3>
<p>
 Jenkins is an automation engine with an unparalleled plugin ecosystem to support all of your favorite tools in your delivery pipelines, whether your goal is continuous integration, automated testing, or continuous delivery.
</p>
<ul>
 <li>
  <a href="https://github.com/jenkinsci/kubernetes-plugin">
   Jenkins-Kubernetes Plugin
  </a>
  by
  <a href="https://www.twitter.com/csanchez">
   Carlos Sanchez
  </a>
 </li>
 <li>
  <a href="https://cloud.google.com/solutions/automated-build-images-with-jenkins-kubernetes#kubernetes_architecture">
   Automated Image Builds with Jenkins, Packer, and Kubernetes
  </a>
 </li>
 <li>
  <a href="https://www.cloudbees.com/blog/demand-jenkins-slaves-kubernetes-and-google-container-engine">
   On-demand Jenkins slaves with Kubernetes and the Google Container Engine
  </a>
 </li>
 <li>
  <a href="http://iocanel.blogspot.in/2015/09/jenkins-setups-for-kubernetes-and.html">
   Jenkins setups for Kubernetes and Docker Workflow
  </a>
 </li>
</ul>
<h1>
 Container Support
</h1>
<p>
 <em>
  A list of linux containers supported by kubernetes.
 </em>
</p>
<h3>
 <a href="http://docker.com">
  Docker
 </a>
 :
</h3>
<p>
 Docker is an open platform for developers and sysadmins to build, ship, and run distributed applications. Consisting of Docker Engine, a portable, lightweight runtime and packaging tool, and Docker Hub, a cloud service for sharing applications and automating workflows, Docker enables apps to be quickly assembled from components and eliminates the friction between development, QA, and production environments. As a result, IT can ship faster and run the same app, unchanged, on laptops, data center VMs, and any cloud.Check out
 <a href="https://github.com/veggiemonk/awesome-docker/">
  awesome-docker
 </a>
 for more info.
</p>
<h3>
 <a href="http://coreos.com/rkt">
  Rkt
 </a>
 :
</h3>
<p>
 rkt is the next-generation container manager for Linux clusters. Designed for security, simplicity, and composability within modern cluster architectures, rkt discovers, verifies, fetches, and executes application containers with pluggable isolation. rkt can run the same container with varying degrees of protection, from lightweight, OS-level namespace and capabilities isolation to heavier, VM-level hardware virtualization.
</p>
<ul>
 <li>
  <a href="http://kubernetes.io/docs/getting-started-guides/rkt/">
   Rktnetes
  </a>
 </li>
</ul>
<h1>
 Raspberry Pi
</h1>
<p>
 <em>
  Some of the awesome findings and experiments on using Kubernetes with Raspberry Pi.Checkout
  <a href="http://kubecloud.io">
   Kubecloud
  </a>
 </em>
</p>
<ul>
 <li>
  <a href="http://kubecloud.io/kubernetes-on-arm-cluster/">
   Setting up a Kubernetes on ARM cluster
  </a>
 </li>
 <li>
  <a href="http://kubecloud.io/kubernetes-on-arm-registry/">
   Local registry in Kubernetes on ARM
  </a>
 </li>
</ul>
<h1>
 Books
</h1>
<p>
 <em>
  A written or printed work consisting of pages glued or sewn together along one side and bound in covers that provide
us with information
 </em>
</p>
<ul>
 <li>
  <a href="http://shop.oreilly.com/product/0636920043874.do">
   Kubernetes: Up and Running
  </a>
  by
  <a href="https://twitter.com/kelseyhightower">
   Kelsey Hightower
  </a>
 </li>
 <li>
  <a href="http://item.jd.com/11757034.html">
   Docker and Kubernetes Under the Hood
  </a>
  (Chinese) by
  <a href="https://twitter.com/resouer">
   Harry Zhang
  </a>
  , Jianbo Sun and ZJU SEL lab
 </li>
 <li>
  <a href="http://www.oreilly.com/webops-perf/free/kubernetes.csp">
   Kubernetes: Scheduling the Future at Cloud Scale
  </a>
  by
  <a href="http://www.linkedin.com/in/drensin">
   Dave K. Rensin
  </a>
 </li>
 <li>
  <a href="https://www.manning.com/books/kubernetes-in-action">
   Kubernetes in Action
  </a>
  by
  <a href="https://twitter.com/markoluksa">
   Marko Lukša
  </a>
 </li>
</ul>
<h1>
 Slide Presentations
</h1>
<p>
 <em>
  A slide is a single page of a presentation created with software such as PowerPoint or OpenOffice Impress.
 </em>
</p>
<ul>
 <li>
  <a href="http://www.slideshare.net/enakai/architecture-overview-kubernetes-with-red-hat-enterprise-linux-71">
   Architecture Overview
  </a>
  by
  <a href="https://twitter.com/enakai00/">
   enakai00
  </a>
 </li>
 <li>
  <a href="http://www.slideshare.net/arungupta1/package-your-java-ee-application-using-docker-and-kubernetes">
   Package your Java EE Application using Docker and Kubernetes
  </a>
  by
  <a href="https://twitter.com/arungupta">
   Arun Gupta
  </a>
 </li>
 <li>
  <a href="http://www.slideshare.net/carlossg/scaling-jenkins-with-docker-and-kubernetes">
   Scaling Jenkins with Docker and Kubernetes
  </a>
  by
  <a href="https://www.twitter.com/csanchez">
   Carlos Sanchez
  </a>
 </li>
 <li>
  <a href="http://www.slideshare.net/imesh/an-introduction-to-kubernetes">
   An Introduction to Kubernetes
  </a>
  by
  <a href="https://www.linkedin.com/in/imesh">
   Imesh Gunaratne
  </a>
 </li>
 <li>
  <a href="http://www.slideshare.net/timothysc/apache-coneu">
   Musings on Mesos: Docker, Kubernetes, and Beyond.
  </a>
  by
  <a href="http://timothysc.github.io/">
   Timothy St. Clair
  </a>
 </li>
 <li>
  <a href="http://www.slideshare.net/SatnamSingh67/2015-0605-cluster-management-with-kubernetes">
   Cluster management with Kubernetes
  </a>
  by
  <a href="https://twitter.com/satnamsingh">
   Satnam Singh
  </a>
 </li>
 <li>
  <a href="http://www.slideshare.net/ramitsurana/a-brief-study-on-kubernetes-and-its-components">
   A brief study on Kubernetes and its components
  </a>
  by
  <a href="https://www.twitter.com/ramitsurana">
   Ramit Surana
  </a>
 </li>
 <li>
  <a href="http://www.slideshare.net/dagrobie/moving-to-kubernetes-tales-from-soundcloud">
   Moving to Kubernetes - Tales from SoundCloud
  </a>
  by
  <a href="https://twitter.com/dagrobie">
   Tobias Schmidt
  </a>
 </li>
 <li>
  <a href="http://www.slideshare.net/kubecon/kubernetes-scaling-sig-k8scale">
   Kubernetes Scaling SIG (K8Scale)
  </a>
  by
  <a href="https://twitter.com/countspongebob">
   Bob Wise
  </a>
 </li>
 <li>
  <a href="http://www.slideshare.net/salv_orlando/network-oriented-kubernetes-intro">
   Network oriented Kubernetes intro
  </a>
  by
  <a href="https://twitter.com/taturiello">
   Salv Orlando
  </a>
 </li>
 <li>
  <a href="http://www.slideshare.net/ArjanSchaaf/zero-downtimejavadeploymentswithdockerandkubernetes">
   Zero downtime-java-deployments-with-docker-and-kubernetes
  </a>
  by
  <a href="https://www.linkedin.com/in/arjanschaaf">
   Arjan Schaaf
  </a>
 </li>
 <li>
  <a href="http://www.slideshare.net/mistio/kubernetes-and-coreos-athens-docker-meetup">
   Kubernetes and CoreOS @ Athens Docker meetup
  </a>
  by
  <a href="https://twitter.com/mist_io">
   Mist.io
  </a>
 </li>
 <li>
  <a href="http://www.slideshare.net/ramitsurana/achieving-cicd-with-kubernetes">
   Achieving CI/CD with Kubernetes
  </a>
  by
  <a href="https://twitter.com/ramitsurana">
   Ramit Surana
  </a>
 </li>
</ul>
<h1>
 Videos
</h1>
<p>
 <em>
  A recording of moving visual images made digitally or on videotape.
 </em>
</p>
<h3>
 Main Account
</h3>
<ul>
 <li>
  <a href="https://www.youtube.com/channel/UC_x5XG1OV2P6uZZ5FSM9Ttw">
   Google Developers
  </a>
 </li>
 <li>
  <a href="https://www.youtube.com/channel/UCZ2bu0qutTOM0tHYa_jkIwg">
   Kubernetes
  </a>
 </li>
</ul>
<h3>
 Other Useful Videos
</h3>
<ul>
 <li>
  <a href="https://www.youtube.com/watch?v=tsk0pWf4ipw">
   Google I/O 2014 - Containerizing the Cloud with Docker on Google Cloud Platform
  </a>
  by
  <a href="https://www.youtube.com/channel/UC_x5XG1OV2P6uZZ5FSM9Ttw">
   Google Developers
  </a>
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=tA8XNVPZM2w">
   Container Orchestration using CoreOS and Kubernetes
  </a>
  by
  <a href="https://twitter.com/kelseyhightower">
   Kelsey Hightower
  </a>
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=WwBdNXt6wO4">
   A Technical Overview of Kubernetes
  </a>
  by
  <a href="https://twitter.com/brendandburns">
   Bredan Burns
  </a>
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=Fcb4aoSAZ98">
   Docker Containers and Kubernetes with Brian Dorsey
  </a>
  by
  <a href="https://twitter.com/briandorsey">
   Brian Dorsey
  </a>
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=jLk1pkc7kv4">
   Alpaca Kubernetes on AWS
  </a>
  by
  <a href="https://twitter.com/fandekasp">
   Adrien Lemaire
  </a>
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=R2nj1vRjLwE">
   Arun Gupta: Package your Java applications using Docker and Kubernetes
  </a>
  by
  <a href="https://twitter.com/arungupta">
   Arun Gupta
  </a>
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=pozC9rBvAIs">
   "Managing Containers at Scale with CoreOS and Kubernetes" by Kelsey Hightower
  </a>
  by
  <a href="https://twitter.com/kelseyhightower">
   Kelsey Hightower
  </a>
 </li>
 <li>
  <a href="https://youtu.be/6a2Nirr8cI0">
   Kubernetes: The Journey So Far - Greg DeMichillie
  </a>
  by
  <a href="https://twitter.com/gregde">
   Greg DeMichillie
  </a>
 </li>
 <li>
  <a href="https://youtu.be/MuazGHiiGmA">
   DevNation 2015 - Paul Bakker - Kubernetes: Beyond the basics
  </a>
  by
  <a href="https://twitter.com/pbakker">
   Paul Bakker
  </a>
 </li>
</ul>
<h1>
 Interactive Learning Environments
</h1>
<p>
 <em>
  Learn Kubernetes using an interactive environment without requiring downloads or configuration
 </em>
</p>
<ul>
 <li>
  <a href="https://www.katacoda.com/courses/kubernetes">
   Katacoda
  </a>
 </li>
</ul>
<h1>
 Interesting Twitter Accounts
</h1>
<p>
 <em>
  Twitter is quick, it’s easy to communicate on, and is a very valuable social channel for a brand or business if you use it to its full potential, By following these news aggregators, rolling news channels, and companies, you can get the inside scoop of a story long before it hits the mainstream news outlets.
 </em>
</p>
<ul>
 <li>
  <a href="https://twitter.com/kubernetesio">
   Kubernetes
  </a>
 </li>
 <li>
  <a href="https://twitter.com/googlecloud">
   Google Cloud Platform
  </a>
 </li>
 <li>
  <a href="https://twitter.com/kubeconio">
   Kube Con
  </a>
 </li>
 <li>
  <a href="https://twitter.com/kismatic">
   Kismatic
  </a>
 </li>
 <li>
  <a href="https://twitter.com/engineyard">
   Engine Yard
  </a>
 </li>
 <li>
  <a href="https://twitter.com/Apcera">
   Apcera
  </a>
 </li>
 <li>
  <a href="https://twitter.com/coreoslinux">
   CoreOS
  </a>
 </li>
 <li>
  <a href="https://twitter.com/DevOpsSummit">
   DevOps Summit
  </a>
 </li>
 <li>
  <a href="https://twitter.com/kubeweekly">
   KubeWeekly
  </a>
 </li>
 <li>
  <a href="https://twitter.com/kubefacts">
   KubeFacts
  </a>
 </li>
 <li>
  <a href="https://twitter.com/skippbox">
   Skippbox
  </a>
 </li>
</ul>
<h1>
 Amazing People
</h1>
<ul>
 <li>
  <a href="https://twitter.com/brendandburns">
   Bredan Burns
  </a>
  , Partner Architect at Microsoft
 </li>
 <li>
  <a href="https://twitter.com/kelseyhightower">
   Kelsey Hightower
  </a>
  , Staff Developer Advocate at Google
 </li>
 <li>
  <a href="https://twitter.com/arungupta">
   Arun Gupta
  </a>
  , Vice President, Developer Relations at Couchbase
 </li>
 <li>
  <a href="https://www.twitter.com/csanchez">
   Carlos Sanchez
  </a>
  , Senior Software Engineer, CloudBees
 </li>
 <li>
  <a href="https://twitter.com/asynchio">
   Joseph Jacks
  </a>
  , VP, Technology Strategy at Kismatic, Inc
 </li>
 <li>
  <a href="https://twitter.com/jbeda">
   Joe Beda
  </a>
  , Co-founder and Technical Lead for Kubernetes
 </li>
 <li>
  <a href="https://twitter.com/preillyme">
   Patrick Reilly
  </a>
  , CEO at Kismatic, Inc. / Advisor at Mesosphere, Inc
 </li>
 <li>
  <a href="https://twitter.com/BrandonPhilips">
   Brandon Philips
  </a>
  , CTO at CoreOS
 </li>
 <li>
  <a href="https://twitter.com/eric_tune">
   Eric Tune
  </a>
  , Senior Staff Engineer at Google
 </li>
 <li>
  <a href="https://twitter.com/thockin">
   Tim Hockin
  </a>
  , Senior Staff SW Engineer / Engineering Manager at Google
 </li>
</ul>
<h1>
 Connecting with Kubernetes
</h1>
<ul>
 <li>
  <a href="http://webchat.freenode.net/?channels=google-containers">
   Freenode
  </a>
 </li>
 <li>
  <a href="https://twitter.com/kubernetesio">
   Twitter
  </a>
 </li>
 <li>
  <a href="https://plus.google.com/u/0/b/116512812300813784482/116512812300813784482">
   Google +
  </a>
 </li>
 <li>
  <a href="http://stackoverflow.com/questions/tagged/kubernetes">
   Stackoverflow
  </a>
 </li>
 <li>
  <a href="http://slack.k8s.io/">
   Slack
  </a>
 </li>
 <li>
  <a href="https://groups.google.com/forum/#!forum/google-containers">
   Mailing List
  </a>
 </li>
 <li>
  <a href="https://kismatic.com/community/introducing-kubernetes-weekly-news/">
   Newsletter
  </a>
  by
  <a href="https://kismatic.com/">
   Kismatic
  </a>
 </li>
 <li>
  <a href="https://www.reddit.com/r/kubernetes/">
   Reddit
  </a>
 </li>
 <li>
  <a href="https://github.com/kubernetes/community">
   Community
  </a>
 </li>
</ul>
<h1>
 Companies
</h1>
<p>
 <em>
  A list of companies supporting Kubernetes
 </em>
</p>
<ul>
 <li>
  <a href="https://google.com">
   Google
  </a>
 </li>
 <li>
  <a href="https://coreos.com/">
   Coreos
  </a>
 </li>
 <li>
  <a href="https://redhat.com">
   Red Hat
  </a>
 </li>
 <li>
  <a href="https://apprenda.com/">
   Apprenda
  </a>
 </li>
 <li>
  <a href="http://redspread.com/">
   RedSpread
  </a>
 </li>
</ul>
<h1>
 Conferences
</h1>
<p>
 <em>
  Some must to go and attend conferences on kubernetes
 </em>
</p>
<ul>
 <li>
  <a href="http://events.linuxfoundation.org/events/kubecon">
   Kubecon
  </a>
 </li>
 <li>
  <a href="https://container.camp/">
   Container Camp
  </a>
 </li>
 <li>
  <a href="https://cloudplatformonline.com/Next2016.html">
   GCP Next
  </a>
 </li>
 <li>
  <a href="http://dockercon.com">
   Docker Con
  </a>
 </li>
 <li>
  <a href="http://devoxx.com">
   Devoxx
  </a>
 </li>
</ul>
<h1>
 Contributing
</h1>
<p>
 Contributions are most welcome!
</p>
<p>
 This list is just getting started, please contribute to make it super awesome.
</p>
<p>
 Check out the
 <a href="https://github.com/ramitsurana/awesome-kubernetes/blob/master/CONTRIBUTING.md">
  Contributing Guidelines
 </a>
 .
</p>
<h1>
 License
</h1>
<p>
 <a href="http://creativecommons.org/licenses/by-nc/4.0/" rel="license">
  <img alt="Creative Commons License" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" style="border-width:0"/>
 </a>
 <br/>
 <span href="http://purl.org/dc/dcmitype/InteractiveResource" property="dct:title" rel="dct:type" xmlns:dct="http://purl.org/dc/terms/">
  awesome-kubernetes
 </span>
 by
 <a href="http://www.linkedin.com/in/ramitsurana" property="cc:attributionName" rel="cc:attributionURL" xmlns:cc="http://creativecommons.org">
  Ramit Surana
 </a>
 is licensed under a
 <a href="http://creativecommons.org/licenses/by-nc/4.0/" rel="license">
  Creative Commons Attribution-NonCommercial 4.0 International License
 </a>
 .
</p>
