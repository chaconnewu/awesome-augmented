<h1>
 Awesome SDN
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
 <a href="https://travis-ci.org/sdnds-tw/awesome-sdn">
  <img alt="Build Status" src="https://travis-ci.org/sdnds-tw/awesome-sdn.svg?branch=master"/>
 </a>
</h1>
<p>
 A awesome list about Software Defined Network (SDN)
</p>
<ul>
 <li>
  <a href="#awesome-sdn">
   Awesome SDN
  </a>
  <ul>
   <li>
    <a href="#introduction">
     Introduction
    </a>
   </li>
   <li>
    <a href="#network-operating-system">
     Network Operating System
    </a>
   </li>
   <li>
    <a href="#install-enviroment">
     Install Enviroment
    </a>
   </li>
   <li>
    <a href="#software-switch">
     Software Switch
    </a>
   </li>
   <li>
    <a href="#network-virtualization">
     Network Virtualization
    </a>
   </li>
   <li>
    <a href="#protocol">
     Protocol
    </a>
   </li>
   <li>
    <a href="#controller">
     Controller
    </a>
   </li>
   <li>
    <a href="#simulatoremulator">
     Simulator/Emulator
    </a>
   </li>
   <li>
    <a href="#language">
     Language
    </a>
   </li>
   <li>
    <a href="#library">
     Library
    </a>
   </li>
   <li>
    <a href="#test">
     Test
    </a>
   </li>
   <li>
    <a href="#nfv">
     NFV
    </a>
   </li>
   <li>
    <a href="#misc">
     Misc
    </a>
   </li>
  </ul>
 </li>
</ul>
<h1>
 Introduction
</h1>
<p>
 Software-defined networking (SDN) is an approach to computer networking that allows network administrators to manage network services through abstraction of higher-level functionality.
  Wiki :
 <a href="https://en.wikipedia.org/wiki/Software-defined_networking">
  Software-defined networking
 </a>
</p>
<h1>
 Network Operating System
</h1>
<ul>
 <li>
  <a href="http://www.pica8.com/products/picos">
   PicOS
  </a>
  - A SDN OS for white box switches Layer-2/3 feature set with support for OpenFlow, OVSDB, and other protocols.
 </li>
 <li>
  <a href="https://opennetlinux.org">
   OpenNetworkLinux
  </a>
  - A Linux distribution for "bare metal" switches, that is, network forwarding devices built from commodity components.
 </li>
 <li>
  <a href="http://www.openswitch.net">
   OpenSwitch
  </a>
  - A linux network oerating system from Hewlett-Packard.
 </li>
</ul>
<h1>
 Install Enviroment
</h1>
<ul>
 <li>
  <a href="http://onie.org/">
   ONIE
  </a>
  - ONIE enables a bare metal network switch ecosystem where end users have a choice among different network operating systems.
 </li>
</ul>
<h1>
 Software Switch
</h1>
<ul>
 <li>
  <a href="http://openvswitch.org/">
   OpenvSwtich
  </a>
  - Open vSwitch is a production quality, multilayer virtual switch.
 </li>
 <li>
  <a href="http://www.projectfloodlight.org/indigo/">
   Indigo
  </a>
  - Indigo is an open source project aimed at enabling support for OpenFlow on physical and hypervisor switches.
 </li>
 <li>
  <a href="https://github.com/CPqD/ofsoftswitch13">
   CPqD
  </a>
  - An OpenFlow 1.3 compatible user-space software switch implementation
  <sup>
   &#9733 135, pushed 68 days ago
  </sup>
 </li>
 <li>
  <a href="https://lagopus.github.io">
   Lagopus
  </a>
  - A high-performance software OpenFlow 1.3 switch.
 </li>
 <li>
  <a href="https://github.com/FlowForwarding/LINC-Switch">
   LINC-Switch
  </a>
  - A pure OpenFlow software switch written in Erlang
  <sup>
   &#9733 178, pushed 251 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/SnabbCo/snabbswitch">
   snabbswitch
  </a>
  - An open source virtualized Ethernet networking stack.
 </li>
</ul>
<h1>
 Network Virtualization
</h1>
<ul>
 <li>
  <a href="https://github.com/opennetworkinglab/flowvisor">
   FlowVisor
  </a>
  - An OpenFlow controller that acts as a hypervisor/proxy between a switch and multiple controllers. Can slice multiple switches in parallel, effectively slicing a network.
  <sup>
   &#9733 89, pushed 958 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/opennetworkinglab/OpenVirteX">
   OpenVirtex
  </a>
  - A network hypervisor that can create multiple virtual and programmable networks on top of a single physical infrastructure.
  <sup>
   &#9733 34, pushed 396 days ago
  </sup>
 </li>
</ul>
<h1>
 Protocol
</h1>
<ul>
 <li>
  <a href="https://www.opennetworking.org/sdn-resources/openflow">
   OpenFlow
  </a>
  - A communications protocol that gives access to the forwarding plane of a network switch or router over the network.
 </li>
 <li>
  <a href="https://www.opennetworking.org/technical-communities/areas/specification/1928-of-config">
   OF-Config
  </a>
  - OpenFlow Management and Configuration Protocol
 </li>
 <li>
  <a href="https://tools.ietf.org/html/rfc7047">
   OVSDB
  </a>
  - A communication protocol which used to manage the OpenvSwitch database.
 </li>
 <li>
  <a href="http://www.poforwarding.org/">
   POF
  </a>
  - Protocol Oblivious Forwarding
 </li>
</ul>
<h1>
 Controller
</h1>
<ul>
 <li>
  <a href="www.noxrepo.org">
   NOX
  </a>
  - An open source development platform for C++-based software-defined networking (
  <em>
   SDN
  </em>
  ) control applications.
 </li>
 <li>
  <a href="https://github.com/gaberger/NodeFLow">
   NodeFlow
  </a>
  - An OpenFlow Controller Node Style.
  <sup>
   &#9733 48, pushed 1408 days ago
  </sup>
 </li>
 <li>
  <a href="onosproject.org">
   ONOS
  </a>
  - Open Network Operating System.
 </li>
 <li>
  <a href="https://www.opendaylight.org">
   OpenDaylight
  </a>
  - OpenDaylight Platform
 </li>
 <li>
  <a href="www.noxrepo.org/pox">
   POX
  </a>
  - A networking software platform written in Python
 </li>
 <li>
  <a href="https://osrg.github.io/ryu">
   Ryu
  </a>
  - A component-based software defined networking framework.
 </li>
 <li>
  <a href="http://www.projectfloodlight.org/floodlight/">
   Floodlight
  </a>
  - A java-based openflow controller.
 </li>
 <li>
  <a href="https://github.com/BRCDcomm/BVC/">
   Vyatta
  </a>
  - The first commercial Controller built directly from OpenDaylight.
 </li>
 <li>
  <a href="http://www.opencontrail.org/">
   OpenContrail
  </a>
  - A SDN project that utilizes SDN & NFV and provides all the necessary components for network virtualization.
 </li>
 <li>
  <a href="http://openiris.etri.re.kr/">
   IRIS
  </a>
  - A Resursive SDN Openflow Controller created by SDN Research Section, ETRI.
 </li>
 <li>
  <a href="http://www.openmul.org/openmul-controller.html">
   Open MUL
  </a>
  - A lightweight SDN/Openflow controller written almost entirely in C from scratch.
 </li>
 <li>
  <a href="https://github.com/globalnoc/oess">
   OESS
  </a>
  - The Open Exchange Software Suite to configure and control OpenFlow Enabled switches.
  <sup>
   &#9733 13, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/kandoo/beehive-netctrl">
   Beehive Network Controller
  </a>
  - A distributed SDN controller built on top of Beehive. It supports OpenFlow but can be easily extended for other southbound protocols.
  <sup>
   &#9733 14, pushed 51 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/ravel-net/ravel">
   Ravel
  </a>
  - A software-defined networking (SDN) controller that uses a standard SQL database to represent the network.
  <sup>
   &#9733 2, pushed 50 days ago
  </sup>
 </li>
</ul>
<h1>
 Simulator/Emulator
</h1>
<ul>
 <li>
  <a href="http://mininet.org/">
   Mininet
  </a>
  - An Instant Virtual Network on your Laptop (or other PC)
 </li>
 <li>
  <a href="http://github.com/dlinknctu/opennet">
   OpenNet
  </a>
  - A simulator for software-defined wireless local area network
 </li>
 <li>
  <a href="http://www.estinet.com/products.php?lv1=13&sn=13">
   EstiNet
  </a>
  - A world-renowned software tool for network planning
 </li>
 <li>
  <a href="https://www.nsnam.org/">
   ns-3
  </a>
  - A discrete-event network simulator that supports openflow environment.
 </li>
</ul>
<h1>
 Language
</h1>
<ul>
 <li>
  <a href="http://p4.org/">
   P4
  </a>
  - A declarative language for expressing how packets are processed by the pipeline of a network forwarding element such as a switch, NIC, router or network function appliance.
 </li>
 <li>
  <a href="https://github.com/frenetic-lang/frenetic">
   Frenetic
  </a>
  - The Frenetic Programming Language and Runtime System
  <sup>
   &#9733 89, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.frenetic-lang.org/pyretic/">
   Pyretic
  </a>
  - Pyretic is one member of the Frenetic family of SDN programming languages.
 </li>
</ul>
<h1>
 Library
</h1>
<ul>
 <li>
  <a href="https://github.com/floodlight/loxigen">
   loxigen
  </a>
  - LoxiGen is a tool that generates OpenFlow protocol libraries for a number of languages.
  <sup>
   &#9733 51, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/rlenglet/openfaucet">
   openfaucet
  </a>
  - openfaucet is a pure Python implementation of the OpenFlow 1.0.0
protocol, based on Twisted.
  <sup>
   &#9733 30, pushed 1301 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/TrafficLab/oflib-node">
   oflib-node
  </a>
  - Oflib-node is an OpenFlow protocol library for Node. It converts between OpenFlow wire protocol messages and Javascript objects.
  <sup>
   &#9733 12, pushed 1599 days ago
  </sup>
 </li>
 <li>
  <a href="https://bitbucket.org/openflowj/openflowj">
   OpenFlowJ
  </a>
  - A Java implementation of low-level OpenFlow packet marshalling/unmarshalling and IO operations.
 </li>
 <li>
  <a href="http://haskell.cs.yale.edu/other-projects/nettle/">
   nettle
  </a>
  - A Haskell library for working with the OpenFlow protocol.
 </li>
 <li>
  <a href="https://github.com/frenetic-lang/ocaml-openflow">
   OCaml OpenFlow
  </a>
  - A serialization and protocol library for OpenFlow.
  <sup>
   &#9733 9, pushed 292 days ago
  </sup>
 </li>
</ul>
<h1>
 Test
</h1>
<ul>
 <li>
  <a href="https://github.com/floodlight/oftest">
   oftest
  </a>
  - OpenFlow Testing Framework
  <sup>
   &#9733 47, pushed 6 days ago
  </sup>
 </li>
 <li>
  <a href="https://ucb-sts.github.com/sts/">
   STS
  </a>
  - SDN Troubleshooting System, simulates network devices, allowing programmatically test cases generation.
 </li>
 <li>
  <a href="https://code.google.com/archive/p/nice-of/">
   nice-of
  </a>
  - A tool to test OpenFlow controller application for the NOX controller platform.
 </li>
 <li>
  <a href="http://www.opensdncore.org/">
   OpenSDNCore
  </a>
  - Virtualisation Testbed for NFV/SDN Environment.
 </li>
</ul>
<h1>
 NFV
</h1>
<ul>
 <li>
  <a href="https://www.opnfv.org">
   OPNFV
  </a>
  - Accelerating NFV's evolution through an integrated, open platform.
 </li>
</ul>
<h1>
 Misc
</h1>
<ul>
 <li>
  <a href="http://opencord.org">
   Central Office Re-architected as a Datacenter, CORD
  </a>
  - Reference Implementation of a Service Delivery Platform that Provides Cloud Economies and Agility.
 </li>
 <li>
  <a href="https://www.open-o.org">
   OPEN-Orchestrator Project, Open-O
  </a>
 </li>
 <li>
  <a href="https://osm.etsi.org/welcome/">
   Open Source MANO Community, OSM
  </a>
 </li>
 <li>
  <a href="http://att.com/ecomp">
   Enhanced Controller Orchestration Management Policy, ECOMP
  </a>
  - Operations management framework.
 </li>
</ul>
