<h1>
 Awesome Security
</h1>
<p>
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</p>
<p>
 A collection of awesome software, libraries, documents, books, resources and cool stuff about security.
</p>
<p>
 Inspired by
 <a href="https://github.com/ziadoz/awesome-php">
  awesome-php
 </a>
 ,
 <a href="https://github.com/vinta/awesome-python">
  awesome-python
 </a>
 .
</p>
<p>
 Thanks to all
 <a href="https://github.com/sbilly/awesome-security/graphs/contributors">
  contributors
 </a>
 , you're awesome and wouldn't be possible without you! The goal is to build a categorized community-driven collection of very well-known resources.
</p>
<ul>
 <li>
  <a href="#awesome-security">
   Awesome Security
  </a>
  <ul>
   <li>
    <a href="#network">
     Network
    </a>
   </li>
   <li>
    <a href="#scanning--pentesting">
     Scanning / Pentesting
    </a>
   </li>
   <li>
    <a href="#monitoring--logging">
     Monitoring / Logging
    </a>
   </li>
   <li>
    <a href="#ids--ips--host-ids--host-ips">
     IDS / IPS / Host IDS / Host IPS
    </a>
   </li>
   <li>
    <a href="#honey-pot--honey-net">
     Honey Pot / Honey Net
    </a>
   </li>
   <li>
    <a href="#full-packet-capture--forensic">
     Full Packet Capture / Forensic
    </a>
   </li>
   <li>
    <a href="#sniffer">
     Sniffer
    </a>
   </li>
   <li>
    <a href="#security-information--event-management">
     Security Information & Event Management
    </a>
   </li>
   <li>
    <a href="#vpn">
     VPN
    </a>
   </li>
   <li>
    <a href="#fast-packet-processing">
     Fast Packet Processing
    </a>
   </li>
   <li>
    <a href="#endpoint">
     Endpoint
    </a>
   </li>
   <li>
    <a href="#threat-intelligence">
     Threat Intelligence
    </a>
   </li>
   <li>
    <a href="#web">
     Web
    </a>
   </li>
   <li>
    <a href="#big-data">
     Big Data
    </a>
   </li>
   <li>
    <a href="#other-awesome-lists">
     Other Awesome Lists
    </a>
   </li>
   <li>
    <a href="#other-security-awesome-lists">
     Other Security Awesome Lists
    </a>
   </li>
   <li>
    <a href="#other-common-awesome-lists">
     Other Common Awesome Lists
    </a>
   </li>
   <li>
    <a href="#contributing">
     Contributing
    </a>
   </li>
  </ul>
 </li>
</ul>
<hr/>
<h2>
 Network
</h2>
<h3>
 Scanning / Pentesting
</h3>
<ul>
 <li>
  <a href="http://www.openvas.org/">
   OpenVAS
  </a>
  - OpenVAS is a framework of several services and tools offering a comprehensive and powerful vulnerability scanning and vulnerability management solution.
 </li>
 <li>
  <a href="https://github.com/rapid7/metasploit-framework">
   Metasploit Framework
  </a>
  <sup>
   &#9733 5688, pushed 3 days ago
  </sup>
  - A tool for developing and executing exploit code against a remote target machine. Other important sub-projects include the Opcode Database, shellcode archive and related research.
 </li>
 <li>
  <a href="https://www.kali.org/">
   Kali
  </a>
  - Kali Linux is a Debian-derived Linux distribution designed for digital forensics and penetration testing. Kali Linux is preinstalled with numerous penetration-testing programs, including nmap (a port scanner), Wireshark (a packet analyzer), John the Ripper (a password cracker), and Aircrack-ng (a software suite for penetration-testing wireless LANs).
 </li>
 <li>
  <a href="https://github.com/rafael-santiago/pig">
   pig
  </a>
  <sup>
   &#9733 236, pushed 2 days ago
  </sup>
  - A Linux packet crafting tool.
 </li>
 <li>
  <a href="https://github.com/rfunix/Pompem">
   Pompem
  </a>
  <sup>
   &#9733 220, pushed 227 days ago
  </sup>
  - Pompem is an open source tool, which is designed to automate the search for exploits in major databases. Developed in Python, has a system of advanced search, thus facilitating the work of pentesters and ethical hackers. In its current version, performs searches in databases: Exploit-db, 1337day, Packetstorm Security...
 </li>
</ul>
<h3>
 Monitoring / Logging
</h3>
<ul>
 <li>
  <p>
   <a href="http://justniffer.sourceforge.net/">
    justniffer
   </a>
   - Justniffer is a network protocol analyzer that captures network traffic and produces logs in a customized way, can emulate Apache web server log files, track response times and extract all "intercepted" files from the HTTP traffic.
  </p>
 </li>
 <li>
  <p>
   <a href="http://dumpsterventures.com/jason/httpry/">
    httpry
   </a>
   - httpry is a specialized packet sniffer designed for displaying and logging HTTP traffic. It is not intended to perform analysis itself, but to capture, parse, and log the traffic for later analysis. It can be run in real-time displaying the traffic as it is parsed, or as a daemon process that logs to an output file. It is written to be as lightweight and flexible as possible, so that it can be easily adaptable to different applications.
  </p>
 </li>
 <li>
  <p>
   <a href="http://ngrep.sourceforge.net/">
    ngrep
   </a>
   - ngrep strives to provide most of GNU grep's common features, applying them to the network layer. ngrep is a pcap-aware tool that will allow you to specify extended regular or hexadecimal expressions to match against data payloads of packets. It currently recognizes IPv4/6, TCP, UDP, ICMPv4/6, IGMP and Raw across Ethernet, PPP, SLIP, FDDI, Token Ring and null interfaces, and understands BPF filter logic in the same fashion as more common packet sniffing tools, such as tcpdump and snoop.
  </p>
 </li>
 <li>
  <p>
   <a href="https://github.com/gamelinux/passivedns">
    passivedns
   </a>
   <sup>
    &#9733 655, pushed 78 days ago
   </sup>
   - A tool to collect DNS records passively to aid Incident handling, Network Security Monitoring (NSM) and general digital forensics. PassiveDNS sniffs traffic from an interface or reads a pcap-file and outputs the DNS-server answers to a log file. PassiveDNS can cache/aggregate duplicate DNS answers in-memory, limiting the amount of data in the logfile without loosing the essens in the DNS answer.
  </p>
 </li>
 <li>
  <p>
   <a href="http://sagan.quadrantsec.com/">
    sagan
   </a>
   - Sagan uses a 'Snort like' engine and rules to analyze logs (syslog/event log/snmptrap/netflow/etc).
  </p>
 </li>
 <li>
  <p>
   <a href="http://www.ossec.net/">
    OSSEC
   </a>
   -  OSSEC is an Open Source Host-based Intrusion Detection System that performs log analysis, file integrity checking, policy monitoring, rootkit detection, real-time alerting and active response. It runs on most operating systems, including Linux, MacOS, Solaris, HP-UX, AIX and Windows.
  </p>
 </li>
 <li>
  <p>
   <a href="http://www.ntop.org/products/traffic-analysis/ntop/">
    ntopng
   </a>
   - Ntopng is a network traffic probe that shows the network usage, similar to what the popular top Unix command does.
  </p>
 </li>
</ul>
<h3>
 IDS / IPS / Host IDS / Host IPS
</h3>
<ul>
 <li>
  <a href="https://www.snort.org/">
   Snort
  </a>
  - Snort is a free and open source network intrusion prevention system (NIPS) and network intrusion detection system (NIDS)created by Martin Roesch in 1998. Snort is now developed by Sourcefire, of which Roesch is the founder and CTO. In 2009, Snort entered InfoWorld's Open Source Hall of Fame as one of the "greatest [pieces of] open source software of all time".
 </li>
 <li>
  <a href="https://www.bro.org/">
   Bro
  </a>
  - Bro is a powerful network analysis framework that is much different from the typical IDS you may know.
 </li>
 <li>
  <a href="http://suricata-ids.org/">
   Suricata
  </a>
  - Suricata is a high performance Network IDS, IPS and Network Security Monitoring engine. Open Source and owned by a community run non-profit foundation, the Open Information Security Foundation (OISF). Suricata is developed by the OISF and its supporting vendors.
 </li>
 <li>
  <a href="http://blog.securityonion.net/">
   Security Onion
  </a>
  - Security Onion is a Linux distro for intrusion detection, network security monitoring, and log management. It's based on Ubuntu and contains Snort, Suricata, Bro, OSSEC, Sguil, Squert, Snorby, ELSA, Xplico, NetworkMiner, and many other security tools. The easy-to-use Setup wizard allows you to build an army of distributed sensors for your enterprise in minutes!
 </li>
 <li>
  <a href="https://github.com/marshyski/sshwatch">
   sshwatch
  </a>
  <sup>
   &#9733 12, pushed 1017 days ago
  </sup>
  - IPS for SSH similar to DenyHosts written in Python.  It also can gather information about attacker during the attack in a log.
 </li>
</ul>
<h3>
 Honey Pot / Honey Net
</h3>
<ul>
 <li>
  <a href="http://dionaea.carnivore.it/">
   Dionaea
  </a>
  - Dionaea is meant to be a nepenthes successor, embedding python as scripting language, using libemu to detect shellcodes, supporting ipv6 and tls.
 </li>
 <li>
  <a href="http://conpot.org/">
   Conpot
  </a>
  - ICS/SCADA Honeypot. Conpot is a low interactive server side Industrial Control Systems honeypot designed to be easy to deploy, modify and extend. By providing a range of common industrial control protocols we created the basics to build your own system, capable to emulate complex infrastructures to convince an adversary that he just found a huge industrial complex. To improve the deceptive capabilities, we also provided the possibility to server a custom human machine interface to increase the honeypots attack surface. The response times of the services can be artificially delayed to mimic the behaviour of a system under constant load. Because we are providing complete stacks of the protocols, Conpot can be accessed with productive HMI's or extended with real hardware. Conpot is developed under the umbrella of the Honeynet Project and on the shoulders of a couple of very big giants.
 </li>
 <li>
  <a href="https://github.com/zeroq/amun">
   Amun
  </a>
  <sup>
   &#9733 18, pushed 507 days ago
  </sup>
  - Amun Python-based low-interaction Honeypot.
 </li>
 <li>
  <a href="http://glastopf.org/">
   Glastopf
  </a>
  - Glastopf is a Honeypot which emulates thousands of vulnerabilities to gather data from attacks targeting web applications. The principle behind it is very simple: Reply the correct response to the attacker exploiting the web application.
 </li>
 <li>
  <a href="https://github.com/desaster/kippo">
   Kippo
  </a>
  <sup>
   &#9733 628, pushed 195 days ago
  </sup>
  - Kippo is a medium interaction SSH honeypot designed to log brute force attacks and, most importantly, the entire shell interaction performed by the attacker.
 </li>
 <li>
  <a href="http://kojoney.sourceforge.net/">
   Kojoney
  </a>
  - Kojoney is a low level interaction honeypot that emulates an SSH server. The daemon is written in Python using the Twisted Conch libraries.
 </li>
 <li>
  <a href="https://github.com/tnich/honssh">
   HonSSH
  </a>
  <sup>
   &#9733 50, pushed 89 days ago
  </sup>
  - HonSSH is a high-interaction Honey Pot solution. HonSSH will sit between an attacker and a honey pot, creating two separate SSH connections between them.
 </li>
 <li>
  <a href="http://sourceforge.net/projects/bifrozt/">
   Bifrozt
  </a>
  - Bifrozt is a NAT device with a DHCP server that is usually deployed with one NIC connected directly to the Internet and one NIC connected to the internal network. What differentiates Bifrozt from other standard NAT devices is its ability to work as a transparent SSHv2 proxy between an attacker and your honeypot. If you deployed an SSH server on Bifrozt’s internal network it would log all the interaction to a TTY file in plain text that could be viewed later and capture a copy of any files that were downloaded. You would not have to install any additional software, compile any kernel modules or use a specific version or type of operating system on the internal SSH server for this to work. It will limit outbound traffic to a set number of ports and will start to drop outbound packets on these ports when certain limits are exceeded.
 </li>
 <li>
  <a href="http://bruteforce.gr/honeydrive">
   HoneyDrive
  </a>
  - HoneyDrive is the premier honeypot Linux distro. It is a virtual appliance (OVA) with Xubuntu Desktop 12.04.4 LTS edition installed. It contains over 10 pre-installed and pre-configured honeypot software packages such as Kippo SSH honeypot, Dionaea and Amun malware honeypots, Honeyd low-interaction honeypot, Glastopf web honeypot and Wordpot, Conpot SCADA/ICS honeypot, Thug and PhoneyC honeyclients and more. Additionally it includes many useful pre-configured scripts and utilities to analyze, visualize and process the data it can capture, such as Kippo-Graph, Honeyd-Viz, DionaeaFR, an ELK stack and much more. Lastly, almost 90 well-known malware analysis, forensics and network monitoring related tools are also present in the distribution.
 </li>
 <li>
  <a href="http://www.cuckoosandbox.org/">
   Cuckoo Sandbox
  </a>
  - Cuckoo Sandbox is an Open Source software for automating analysis of suspicious files. To do so it makes use of custom components that monitor the behavior of the malicious processes while running in an isolated environment.
 </li>
</ul>
<h3>
 Full Packet Capture / Forensic
</h3>
<ul>
 <li>
  <a href="https://github.com/simsong/tcpflow">
   tcpflow
  </a>
  <sup>
   &#9733 516, pushed 98 days ago
  </sup>
  - tcpflow is a program that captures data transmitted as part of TCP connections (flows), and stores the data in a way that is convenient for protocol analysis and debugging. Each TCP flow is stored in its own file. Thus, the typical TCP flow will be stored in two files, one for each direction. tcpflow can also process stored 'tcpdump' packet flows.
 </li>
 <li>
  <a href="http://www.xplico.org/">
   Xplico
  </a>
  - The goal of Xplico is extract from an internet traffic capture the applications data contained. For example, from a pcap file Xplico extracts each email (POP, IMAP, and SMTP protocols), all HTTP contents, each VoIP call (SIP), FTP, TFTP, and so on. Xplico isn’t a network protocol analyzer. Xplico is an open source Network Forensic Analysis Tool (NFAT).
 </li>
 <li>
  <a href="https://github.com/aol/moloch">
   Moloch
  </a>
  <sup>
   &#9733 1389, pushed 11 days ago
  </sup>
  - Moloch is an open source, large scale IPv4 packet capturing (PCAP), indexing and database system. A simple web interface is provided for PCAP browsing, searching, and exporting. APIs are exposed that allow PCAP data and JSON-formatted session data to be downloaded directly. Simple security is implemented by using HTTPS and HTTP digest password support or by using apache in front. Moloch is not meant to replace IDS engines but instead work along side them to store and index all the network traffic in standard PCAP format, providing fast access. Moloch is built to be deployed across many systems and can scale to handle multiple gigabits/sec of traffic.
 </li>
 <li>
  <a href="http://www.openfpc.org">
   OpenFPC
  </a>
  - OpenFPC is a set of tools that combine to provide a lightweight full-packet network traffic recorder & buffering system. It's design goal is to allow non-expert users to deploy a distributed network traffic recorder on COTS hardware while integrating into existing alert and log management tools.
 </li>
 <li>
  <a href="https://github.com/USArmyResearchLab/Dshell">
   Dshell
  </a>
  <sup>
   &#9733 4652, pushed 12 days ago
  </sup>
  - Dshell is a network forensic analysis framework. Enables rapid development of plugins to support the dissection of network packet captures.
 </li>
 <li>
  <a href="https://github.com/google/stenographer">
   stenographer
  </a>
  <sup>
   &#9733 836, pushed 1 days ago
  </sup>
  - Stenographer is a packet capture solution which aims to quickly spool all packets to disk, then provide simple, fast access to subsets of those packets.
 </li>
</ul>
<h3>
 Sniffer
</h3>
<ul>
 <li>
  <a href="https://www.wireshark.org">
   wireshark
  </a>
  - Wireshark is a free and open-source packet analyzer. It is used for network troubleshooting, analysis, software and communications protocol development, and education. Wireshark is very similar to tcpdump, but has a graphical front-end, plus some integrated sorting and filtering options.
 </li>
 <li>
  <a href="http://netsniff-ng.org/">
   netsniff-ng
  </a>
  -  netsniff-ng is a free Linux networking toolkit, a Swiss army knife for your daily Linux network plumbing if you will. Its gain of performance is reached by zero-copy mechanisms, so that on packet reception and transmission the kernel does not need to copy packets from kernel space to user space and vice versa.
 </li>
</ul>
<h3>
 Security Information & Event Management
</h3>
<ul>
 <li>
  <a href="https://www.prelude-ids.org/">
   Prelude
  </a>
  - Prelude is a Universal "Security Information & Event Management" (SIEM) system. Prelude collects, normalizes, sorts, aggregates, correlates and reports all security-related events independently of the product brand or license giving rise to such events; Prelude is "agentless".
 </li>
 <li>
  <a href="https://www.alienvault.com/open-threat-exchange/projects">
   OSSIM
  </a>
  - OSSIM provides all of the features that a security professional needs from a SIEM offering – event collection, normalization, and correlation.
 </li>
</ul>
<h3>
 VPN
</h3>
<ul>
 <li>
  <a href="https://openvpn.net/">
   OpenVPN
  </a>
  - OpenVPN is an open source software application that implements virtual private network (VPN) techniques for creating secure point-to-point or site-to-site connections in routed or bridged configurations and remote access facilities. It uses a custom security protocol that utilizes SSL/TLS for key exchange.
 </li>
</ul>
<h3>
 Fast Packet Processing
</h3>
<ul>
 <li>
  <a href="http://dpdk.org/">
   DPDK
  </a>
  - DPDK is a set of libraries and drivers for fast packet processing.
 </li>
 <li>
  <a href="https://github.com/pfq/PFQ">
   PFQ
  </a>
  <sup>
   &#9733 389, pushed 1 days ago
  </sup>
  - PFQ is a functional networking framework designed for the Linux operating system that allows efficient packets capture/transmission (10G and beyond), in-kernel functional processing and packets steering across sockets/end-points.
 </li>
 <li>
  <a href="http://www.ntop.org/products/packet-capture/pf_ring/">
   PF
   <em>
    RING
   </em>
  </a>
  - PF
 </li>
</ul>
RING is a new type of network socket that dramatically improves the packet capture speed.
<li>
 <a href="http://www.ntop.org/products/packet-capture/pf_ring/pf_ring-zc-zero-copy/">
  PF
  <em>
   RING ZC (Zero Copy)
  </em>
 </a>
 - PF
</li>
RING ZC (Zero Copy) is a flexible packet processing framework that  allows you to achieve 1/10 Gbit line rate packet processing (both RX and TX) at any packet size. It implements zero copy operations including patterns for inter-process and inter-VM (KVM) communications.
<li>
 <a href="http://lxr.free-electrons.com/source/Documentation/networking/packet_mmap.txt">
  PACKET
  <em>
   MMAP/TPACKET/AF
  </em>
  PACKET
 </a>
 - It's fine to use PACKET_MMAP to improve the performance of the capture and transmission process in Linux.
</li>
<li>
 <a href="http://info.iet.unipi.it/~luigi/netmap/">
  netmap
 </a>
 - netmap is a framework for high speed packet I/O. Together with its companion VALE software switch, it is implemented as a single kernel module and available for FreeBSD, Linux and now also Windows.
</li>
<h2>
 Endpoint
</h2>
<h3>
 Configuration Management
</h3>
<ul>
 <li>
  <a href="http://www.rudder-project.org/">
   Rudder
  </a>
  - Rudder is an easy to use, web-driven, role-based solution for IT Infrastructure Automation & Compliance. Automate common system administration tasks (installation, configuration); Enforce configuration over time (configuring once is good, ensuring that configuration is valid and automatically fixing it is better); Inventory of all managed nodes; Web interface to configure and manage nodes and their configuration; Compliance reporting, by configuration and/or by node.
 </li>
</ul>
<h3>
 Authentication
</h3>
<ul>
 <li>
  <a href="https://github.com/google/google-authenticator">
   google-authenticator
  </a>
  <sup>
   &#9733 1281, pushed 16 days ago
  </sup>
  - The Google Authenticator project includes implementations of one-time passcode generators for several mobile platforms, as well as a pluggable authentication module (PAM). One-time passcodes are generated using open standards developed by the Initiative for Open Authentication (OATH) (which is unrelated to OAuth). These implementations support the HMAC-Based One-time Password (HOTP) algorithm specified in RFC 4226 and the Time-based One-time Password (TOTP) algorithm specified in RFC 6238.
  <a href="http://xmodulo.com/two-factor-authentication-ssh-login-linux.html">
   Tutorials: How to set up two-factor authentication for SSH login on Linux
  </a>
 </li>
</ul>
<h3>
 Mobile / Android /iOS
</h3>
<ul>
 <li>
  <a href="https://github.com/ashishb/android-security-awesome">
   android-security-awesome
  </a>
  <sup>
   &#9733 1007, pushed 5 days ago
  </sup>
  - A collection of android security related resources. A lot of work is happening in academia and industry on tools to perform dynamic analysis, static analysis and reverse engineering of android apps.
 </li>
 <li>
  <a href="http://wiki.secmobi.com/">
   SecMobi Wiki
  </a>
  - A collection of mobile security resources which including articles, blogs, books, groups, projects, tools and conferences. *
 </li>
</ul>
<h3>
 Forensics
</h3>
<ul>
 <li>
  <a href="https://github.com/google/grr">
   grr
  </a>
  <sup>
   &#9733 1180, pushed 11 days ago
  </sup>
  - GRR Rapid Response is an incident response framework focused on remote live forensics.
 </li>
</ul>
<h2>
 Threat Intelligence
</h2>
<ul>
 <li>
  <a href="https://www.abuse.ch/">
   abuse.ch
  </a>
  - ZeuS Tracker / SpyEye Tracker / Palevo Tracker / Feodo Tracker tracks Command&Control servers (hosts) around the world and provides you a domain- and an IP-blocklist.
 </li>
 <li>
  <a href="http://www.emergingthreats.net/open-source">
   Emerging Threats - Open Source
  </a>
  - Emerging Threats began 10 years ago as an open source community for collecting Suricata and SNORT® rules, firewall rules, and other IDS rulesets. The open source community still plays an active role in Internet security, with more than 200,000 active users downloading the ruleset daily. The ETOpen Ruleset is open to any user or organization, as long as you follow some basic guidelines. Our ETOpen Ruleset is available for download any time.
 </li>
 <li>
  <a href="http://www.phishtank.com/">
   PhishTank
  </a>
  - PhishTank is a collaborative clearing house for data and information about phishing on the Internet. Also, PhishTank provides an open API for developers and researchers to integrate anti-phishing data into their applications at no charge.
 </li>
 <li>
  <a href="http://www.spamhaus.org/">
   SBL / XBL / PBL / DBL / DROP / ROKSO
  </a>
  - The Spamhaus Project is an international nonprofit organization whose mission is to track the Internet's spam operations and sources, to provide dependable realtime anti-spam protection for Internet networks, to work with Law Enforcement Agencies to identify and pursue spam and malware gangs worldwide, and to lobby governments for effective anti-spam legislation.
 </li>
 <li>
  <a href="https://www.dshield.org/reports.html">
   Internet Storm Center
  </a>
  - The ISC was created in 2001 following the successful detection, analysis, and widespread warning of the Li0n worm. Today, the ISC provides a free analysis and warning service to thousands of Internet users and organizations, and is actively working with Internet Service Providers to fight back against the most malicious attackers.
 </li>
 <li>
  <a href="https://www.autoshun.org/">
   AutoShun
  </a>
  - AutoShun is a Snort plugin that allows you to send your Snort IDS logs to a centralized server that will correlate attacks from your sensor logs with other snort sensors, honeypots, and mail filters from around the world.
 </li>
 <li>
  <a href="http://www.malwaredomains.com/">
   DNS-BH
  </a>
  - The DNS-BH project creates and maintains a listing of domains that are known to be used to propagate malware and spyware. This project creates the Bind and Windows zone files required to serve fake replies to localhost for any requests to these, thus preventing many spyware installs and reporting.
 </li>
 <li>
  <a href="http://www.alienvault.com/open-threat-exchange/dashboard">
   AlienVault Open Threat Exchange
  </a>
  - AlienVault Open Threat Exchange (OTX), to help you secure your networks from data loss, service disruption and system compromise caused by malicious IP addresses.
 </li>
 <li>
  <a href="https://collector.torproject.org/">
   Tor Bulk Exit List
  </a>
  - CollecTor, your friendly data-collecting service in the Tor network. CollecTor fetches data from various nodes and services in the public Tor network and makes it available to the world. If you're doing research on the Tor network, or if you're developing an application that uses Tor network data, this is your place to start.
  <a href="https://www.dan.me.uk/tornodes">
   TOR Node List
  </a>
  /
  <a href="https://www.dan.me.uk/dnsbl">
   DNS Blacklists
  </a>
  /
  <a href="http://torstatus.blutmagie.de/">
   Tor Node List
  </a>
 </li>
 <li>
  <a href="http://www.leakedin.com/">
   leakedin.com
  </a>
  - The primary purpose of leakedin.com is to make visitors aware about the risks of loosing data. This blog just compiles samples of data lost or disclosed on sites like pastebin.com.
 </li>
 <li>
  <a href="https://github.com/fireeye/iocs">
   FireEye OpenIOCs
  </a>
  <sup>
   &#9733 168, pushed 64 days ago
  </sup>
  - FireEye Publicly Shared Indicators of Compromise (IOCs)
 </li>
 <li>
  <a href="http://www.openvas.org/openvas-nvt-feed.html">
   OpenVAS NVT Feed
  </a>
  - The public feed of Network Vulnerability Tests (NVTs). It contains more than 35,000 NVTs (as of April 2014), growing on a daily basis. This feed is configured as the default for OpenVAS.
 </li>
 <li>
  <a href="http://www.projecthoneypot.org/">
   Project Honey Pot
  </a>
  - Project Honey Pot is the first and only distributed system for identifying spammers and the spambots they use to scrape addresses from your website. Using the Project Honey Pot system you can install addresses that are custom-tagged to the time and IP address of a visitor to your site. If one of these addresses begins receiving email we not only can tell that the messages are spam, but also the exact moment when the address was harvested and the IP address that gathered it.
 </li>
 <li>
  <a href="https://www.virustotal.com/">
   virustotal
  </a>
  - VirusTotal, a subsidiary of Google, is a free online service that analyzes files and URLs enabling the identification of viruses, worms, trojans and other kinds of malicious content detected by antivirus engines and website scanners. At the same time, it may be used as a means to detect false positives, i.e. innocuous resources detected as malicious by one or more scanners.
 </li>
 <li>
  <a href="https://github.com/certtools/intelmq/">
   IntelMQ
  </a>
  - IntelMQ is a solution for CERTs for collecting and processing security feeds, pastebins, tweets using a message queue protocol. It's a community driven initiative called IHAP (Incident Handling Automation Project) which was conceptually designed by European CERTs during several InfoSec events. Its main goal is to give to incident responders an easy way to collect & process threat intelligence thus improving the incident handling processes of CERTs.
  <a href="https://www.enisa.europa.eu/activities/cert/support/incident-handling-automation">
   ENSIA Homepage
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/csirtgadgets/massive-octo-spice">
   CIFv2
  </a>
  <sup>
   &#9733 97, pushed 3 days ago
  </sup>
  - CIF is a cyber threat intelligence management system. CIF allows you to combine known malicious threat information from many sources and use that information for identification (incident response), detection (IDS) and mitigation (null route).
 </li>
</ul>
<h2>
 Web
</h2>
<h3>
 Organization
</h3>
<ul>
 <li>
  <a href="http://www.owasp.org">
   OWASP
  </a>
  - The Open Web Application Security Project (OWASP) is a 501(c)(3) worldwide not-for-profit charitable organization focused on improving the security of software.
 </li>
</ul>
<h3>
 Web Application Firewall
</h3>
<ul>
 <li>
  <a href="http://www.modsecurity.org/">
   ModSecurity
  </a>
  - ModSecurity is a toolkit for real-time web application monitoring, logging, and access control.
 </li>
 <li>
  <a href="https://github.com/nbs-system/naxsi">
   NAXSI
  </a>
  <sup>
   &#9733 1240, pushed 6 days ago
  </sup>
  - NAXSI is an open-source, high performance, low rules maintenance WAF for NGINX, NAXSI means Nginx Anti Xss & Sql Injection.
 </li>
 <li>
  <a href="https://www.ironbee.com/">
   ironbee
  </a>
  - IronBee is an open source project to build a universal web application security sensor. IronBee as a framework for developing a system for securing web applications - a framework for building a web application firewall (WAF).
 </li>
</ul>
<h3>
 Scanning / Pentesting
</h3>
<ul>
 <li>
  <a href="http://sqlmap.org/">
   sqlmap
  </a>
  - sqlmap is an open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers. It comes with a powerful detection engine, many niche features for the ultimate penetration tester and a broad range of switches lasting from database fingerprinting, over data fetching from the database, to accessing the underlying file system and executing commands on the operating system via out-of-band connections.
 </li>
 <li>
  <a href="https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project">
   ZAP
  </a>
  - The Zed Attack Proxy (ZAP) is an easy to use integrated penetration testing tool for finding vulnerabilities in web applications. It is designed to be used by people with a wide range of security experience and as such is ideal for developers and functional testers who are new to penetration testing. ZAP provides automated scanners as well as a set of tools that allow you to find security vulnerabilities manually.
 </li>
 <li>
  <a href="http://w3af.org/">
   w3af
  </a>
  - w3af is a Web Application Attack and Audit Framework. The project’s goal is to create a framework to help you secure your web applications by finding and exploiting all web application vulnerabilities.
 </li>
 <li>
  <a href="https://bitbucket.org/LaNMaSteR53/recon-ng">
   Recon-ng
  </a>
  - Recon-ng is a full-featured Web Reconnaissance framework written in Python. Recon-ng has a look and feel similar to the Metasploit Framework.
 </li>
 <li>
  <a href="https://github.com/trustedsec/ptf">
   PTF
  </a>
  <sup>
   &#9733 538, pushed 7 days ago
  </sup>
  - The Penetration Testers Framework (PTF) is a way for modular support for up-to-date tools.
 </li>
</ul>
<h2>
 Big Data
</h2>
<ul>
 <li>
  <a href="https://github.com/ClickSecurity/data_hacking">
   data_hacking
  </a>
  <sup>
   &#9733 256, pushed 472 days ago
  </sup>
  - Examples of using IPython, Pandas, and Scikit Learn to get the most out of your security data.
 </li>
 <li>
  <a href="https://github.com/RIPE-NCC/hadoop-pcap">
   hadoop-pcap
  </a>
  <sup>
   &#9733 142, pushed 3 days ago
  </sup>
  - Hadoop library to read packet capture (PCAP) files.
 </li>
 <li>
  <a href="http://workbench.readthedocs.org/">
   Workbench
  </a>
  - A scalable python framework for security research and development teams.
 </li>
 <li>
  <a href="https://github.com/OpenSOC/opensoc">
   OpenSOC
  </a>
  <sup>
   &#9733 338, pushed 247 days ago
  </sup>
  - OpenSOC integrates a variety of open source big data technologies in order to offer a centralized tool for security monitoring and analysis.
 </li>
 <li>
  <a href="https://github.com/endgameinc/binarypig">
   binarypig
  </a>
  <sup>
   &#9733 114, pushed 659 days ago
  </sup>
  - Scalable Binary Data Extraction in Hadoop. Malware Processing and Analytics over Pig, Exploration through Django, Twitter Bootstrap, and Elasticsearch.
 </li>
</ul>
<h2>
 Other Awesome Lists
</h2>
<h3>
 Other Security Awesome Lists
</h3>
<ul>
 <li>
  <a href="https://github.com/ashishb/android-security-awesome">
   Android Security Awesome
  </a>
  <sup>
   &#9733 1007, pushed 5 days ago
  </sup>
  - A collection of android security related resources.
 </li>
 <li>
  <a href="https://github.com/apsdehal/awesome-ctf">
   Awesome CTF
  </a>
  <sup>
   &#9733 421, pushed 34 days ago
  </sup>
  - A curated list of CTF frameworks, libraries, resources and software.
 </li>
 <li>
  <a href="https://github.com/carpedm20/awesome-hacking">
   Awesome Hacking
  </a>
  <sup>
   &#9733 510, pushed 12 days ago
  </sup>
  - A curated list of awesome Hacking tutorials, tools and resources.
 </li>
 <li>
  <a href="https://github.com/paralax/awesome-honeypots">
   Awesome Honeypots
  </a>
  <sup>
   &#9733 604, pushed 47 days ago
  </sup>
  - An awesome list of honeypot resources.
 </li>
 <li>
  <a href="https://github.com/rshipp/awesome-malware-analysis">
   Awesome Malware Analysis
  </a>
  <sup>
   &#9733 968, pushed 6 days ago
  </sup>
  - A curated list of awesome malware analysis tools and resources.
 </li>
 <li>
  <a href="https://github.com/caesar0301/awesome-pcaptools">
   Awesome PCAP Tools
  </a>
  <sup>
   &#9733 378, pushed 4 days ago
  </sup>
  - A collection of tools developed by other researchers in the Computer Science area to process network traces.
 </li>
 <li>
  <a href="https://github.com/enaqx/awesome-pentest">
   Awesome Pentest
  </a>
  <sup>
   &#9733 1859, pushed 10 days ago
  </sup>
  - A collection of awesome penetration testing resources, tools and other shiny things.
 </li>
 <li>
  <a href="https://github.com/Friz-zy/awesome-linux-containers">
   Awesome Linux Containers
  </a>
  <sup>
   &#9733 85, pushed 46 days ago
  </sup>
  - A curated list of awesome Linux Containers frameworks, libraries and software.
 </li>
 <li>
  <a href="https://github.com/meirwah/awesome-incident-response">
   Awesome Incident Response
  </a>
  <sup>
   &#9733 471, pushed 11 days ago
  </sup>
  - A curated list of resources for incident response.
 </li>
 <li>
  <a href="https://github.com/infoslack/awesome-web-hacking">
   Awesome Web Hacking
  </a>
  <sup>
   &#9733 155, pushed 27 days ago
  </sup>
  - This list is for anyone wishing to learn about web application security but do not have a starting point.
 </li>
</ul>
<h3>
 Other Common Awesome Lists
</h3>
<p>
 Other amazingly awesome lists:
</p>
<ul>
 <li>
  <a href="https://github.com/bayandin/awesome-awesomeness">
   awesome-awesomeness
  </a>
  <sup>
   &#9733 16107, pushed 7 days ago
  </sup>
  - awesome-* or *-awesome lists.
 </li>
 <li>
  <a href="https://github.com/jnv/lists">
   lists
  </a>
  <sup>
   &#9733 3765, pushed 2 days ago
  </sup>
  - The definitive list of (awesome) lists curated on GitHub.
 </li>
</ul>
<h2>
 <a href="contributing.md">
  Contributing
 </a>
</h2>
<p>
 Your contributions are always welcome!
</p>
