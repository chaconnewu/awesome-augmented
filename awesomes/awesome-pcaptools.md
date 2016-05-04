<h2>
 Introduction
</h2>
<p>
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
 <a href="https://travis-ci.org/caesar0301/awesome-pcaptools">
  <img alt="Build Status" src="https://travis-ci.org/caesar0301/awesome-pcaptools.svg"/>
 </a>
</p>
<p>
 This project does not contain any source code or files. I just want to make a list of tools to process pcap files in research of network traffic. For more awesome lists, see https://github.com/sindresorhus/awesome
</p>
<p>
 <strong>
  License
 </strong>
 : Apache License v2.
</p>
<blockquote>
 <ul>
  <li>
   <a href="#linuxcmds">
    Linux commands
   </a>
  </li>
  <li>
   <a href="#capture">
    Traffic Capture
   </a>
  </li>
  <li>
   <a href="#analysis">
    Traffic Analysis/Inspection
   </a>
  </li>
  <li>
   <a href="#dnstools">
    DNS Utilities
   </a>
  </li>
  <li>
   <a href="#fileextraction">
    File Extraction
   </a>
  </li>
  <li>
   <a href="#others">
    Related Projects
   </a>
  </li>
 </ul>
</blockquote>
<h2>
 Linux commands
 <a name="linuxcmds">
 </a>
</h2>
<ul>
 <li>
  <p>
   <strong>
    Bmon
   </strong>
   : (Bandwidth Monitor) is a tool similar to nload that shows the traffic load over all the network interfaces on the system. The output also consists of a graph and a section with packet level details.
   <a href="http://www.binarytides.com/blog/wp-content/uploads/2014/03 /bmon- 640x480.png">
    Screenshot
   </a>
  </p>
 </li>
 <li>
  <p>
   <strong>
    Bwm-ng
   </strong>
   : (Bandwidth Monitor Next Generation) is another very simple real time network load monitor that reports a summary of the speed at which data is being transferred in and out of all available network interfaces on the system.
   <a href="">
    Screenshot
   </a>
  </p>
 </li>
 <li>
  <p>
   <strong>
    CBM
   </strong>
   : (Color Bandwidth Meter) A tiny little simple bandwidth monitor that displays the traffic volume through network interfaces. No further options, just the traffic stats are display and updated in realtime.
   <a href="http://www.binarytides.com/blog /wp-content/uploads/2014/03/cbm.png">
    Screenshot
   </a>
  </p>
 </li>
 <li>
  <p>
   <strong>
    Collectl
   </strong>
   : reports system statistics in a style that is similar to dstat, and like dstat it is gathers statistics about various different system resources like cpu, memory, network etc. Over here is a simple example of how to use it to report network usage/bandwidth.
   <a href="">
    Screenshot
   </a>
  </p>
 </li>
 <li>
  <p>
   <strong>
    Dstat
   </strong>
   : is a versatile tool (written in python) that can monitor different system statistics and report them in a batch style mode or log the data to a csv or similar file. This example shows how to use dstat to report network bandwidth
   <a href="">
    Screenshot
   </a>
  </p>
 </li>
 <li>
  <p>
   <strong>
    Ifstat
   </strong>
   : reports the network bandwidth in a batch style mode. The output is in a format that is easy to log and parse using other programs or utilities.
   <a href="">
    Screenshot
   </a>
  </p>
 </li>
 <li>
  <p>
   <strong>
    Iftop
   </strong>
   : measures the data flowing through individual socket connections, and it works in a manner that is different from Nload. Iftop uses the pcap library to capture the packets moving in and out of the network adapter, and then sums up the size and count to find the total bandwidth under use. Although iftop reports the bandwidth used by individual connections, it cannot report the process name/id involved in the particular socket connection. But being based on the pcap library, iftop is able to filter the traffic and report bandwidth usage over selected host connections as specified by the filter.
   <a href="http://www.binarytides.com/blog/wp-content/uploads/2014/03/iftop.png">
    Screenshot
   </a>
  </p>
 </li>
 <li>
  <p>
   <strong>
    Iptraf
   </strong>
   : is an interactive and colorful IP Lan monitor. It shows individual connections and the amount of data flowing between the hosts.
   <a href="http://www.binarytides.com/blog/wp-content/uploads/2014/03/iptraf.png">
    Screenshot
   </a>
  </p>
 </li>
 <li>
  <p>
   <strong>
    Jnettop
   </strong>
   :
   <a href="http://jnettop.kubs.info/wiki/">
    Jnettop
   </a>
   is a traffic visualiser, which captures traffic going through the host it is running from and displays streams sorted by bandwidth they use.
   <a href="http://jnettop.kubs.info/wiki/?binary=internal%3A%2F%2F76195466cc3bca92f8de7b404e240844.gif">
    Screenshot
   </a>
  </p>
 </li>
 <li>
  <p>
   <strong>
    Nethogs
   </strong>
   : is a small 'net top' tool that shows the bandwidth used by individual processes and sorts the list putting the most intensive processes on top. In the event of a sudden bandwidth spike, quickly open nethogs and find the process responsible. Nethogs reports the PID, user and the path of the program.
   <a href="http://www.binarytides.com/blog/wp-content/uploads/2014/03/nethogs.png">
    Screenshot
   </a>
  </p>
 </li>
 <li>
  <p>
   <strong>
    Netload
   </strong>
   : displays a small report on the current traffic load, and the total number of bytes transferred since the program start. No more features are there. Its part of the netdiag.
   <a href="http://www.binarytides.com/blog/wp-content/uploads/2014/03/netload.png">
    Screenshot
   </a>
  </p>
 </li>
 <li>
  <p>
   <strong>
    Netwatch
   </strong>
   : is part of the netdiag collection of tools, and it too displays the connections between local host and other remote hosts, and the speed at which data is transferring on each connection.
   <a href="http://www.binarytides.com/blog/wp-content/uploads/2014/03/netwatch.png">
    Screenshot
   </a>
  </p>
 </li>
 <li>
  <p>
   <strong>
    Nload
   </strong>
   : is a commandline tool that allows users to monitor the incoming and outgoing traffic separately. It also draws outa graph to indicate the same, the scale of which can be adjusted. Easy and simple to use, and does not support many options.
   <a href="http://www.binarytides.com/blog/wp-content/uploads/2014/03/nload.png">
    Screenshot
   </a>
  </p>
 </li>
 <li>
  <p>
   <strong>
    Pktstat
   </strong>
   : displays all the active connections in real time, and the speed at which data is being transferred through them. It also displays the type of the connection, i.e. tcp or udp and also details about http requests if involved.
   <a href="http://www.binarytides.com/blog/wp-content/uploads/2014/03/pktstat.png">
    Screenshot
   </a>
  </p>
 </li>
 <li>
  <p>
   <strong>
    Slurm
   </strong>
   : is 'yet' another network load monitor that shows device statistics along with an ascii graph. It supports 3 different styles of graphs each of which can be activated using the c, s and l keys. Simple in features, slurm does not display any further details about the network load.
   <a href="http://www.binarytides.com/blog/wp-content/uploads/2014/03/slurm.png">
    Screenshot
   </a>
  </p>
 </li>
 <li>
  <p>
   <strong>
    Speedometer
   </strong>
   : Another small and simple tool that just draws out good looking graphs of incoming and outgoing traffic through a given interface.
   <a href="http://www.binarytides.com/blog/wp-content/uploads/2014/03/speedometer.png">
    Screenshot
   </a>
  </p>
 </li>
 <li>
  <p>
   <strong>
    Tcptrack
   </strong>
   : is similar to iftop, and uses the pcap library to capture packets and calculate various statistics like the bandwidth used in each connection. It also supports the standard pcap filters that can be used to monitor specific connections.
   <a href="http://www.binarytides.com/blog /wp-content/uploads/2014/03/tcptrack.png">
    Screenshot
   </a>
  </p>
 </li>
 <li>
  <p>
   <strong>
    Trafshow
   </strong>
   : reports the current active connections, their protocol and the data transfer speed on each connection. It can filter out connections using pcap type filters.
   <a href="http://www.binarytides.com/blog/wp-content/uploads/2014/03/trafshow.png">
    Screenshot
   </a>
  </p>
 </li>
 <li>
  <p>
   <strong>
    Vnstat
   </strong>
   : is bit different from most of the other tools. It actually runs a background service/daemon and keeps recording the size of data transfer all the time. Next it can be used to generate a report of the history of network usage.
   <a href="">
    Screenshot
   </a>
  </p>
 </li>
</ul>
<h2>
 Traffic Capture
 <a name="capture">
 </a>
</h2>
<ul>
 <li>
  <p>
   <a href="http://www.tcpdump.org/">
    Libpcap/Tcpdump
   </a>
   : The official site of tcpdump, a powerful command-line packet analyzer; and libpcap, a portable C/C++ library for network traffic capture.
  </p>
 </li>
 <li>
  <p>
   <a href="http://ngrep.sourceforge.net/">
    Ngrep
   </a>
   : strives to provide most of GNU grep's common features, applying them to the network layer. ngrep is a pcap-aware tool that will allow you to specify extended regular or hexadecimal expressions to match against data payloads of packets. It currently recognizes TCP, UDP and ICMP across Ethernet, PPP, SLIP, FDDI, Token Ring and null interfaces, and understands bpf filter logic in the same fashion as more common packet sniffing tools, such as tcpdump and snoop.
  </p>
 </li>
 <li>
  <p>
   <a href="https://github.com/ruedigergad/clj-net-pcap">
    clj-net-pcap
   </a>
   <span>
    &#9733 19, pushed 114 days ago
   </span>
   :
   <code>
    clj-net-pcap
   </code>
   is a packet capturing library for Clojure. clj-net-pcap uses jNetPcap and adds convenience functionality around jNetPcap for easing the usability. A
   <a href="http://ieeexplore.ieee.org/xpl/articleDetails.jsp?tp=&arnumber=6903107">
    paper on clj-net-pcap
   </a>
   was published in scope of COMPSACW 2014.
  </p>
 </li>
 <li>
  <p>
   <a href="http://jnetpcap.com">
    jNetPcap
   </a>
   : jNetPcap is a packet capturing library for Java that is available for Linux and Windows. jNetPcap leverages libpcap respectively WinPcap and employs the Java Native Interface (JNI) for using the functionality provided by libpcap/WinPcap.
  </p>
 </li>
 <li>
  <p>
   <a href="https://github.com/aol/moloch">
    Moloch
   </a>
   <span>
    &#9733 1389, pushed 11 days ago
   </span>
   : Moloch is a open source large scale full PCAP capturing, indexing and database system.
  </p>
 </li>
 <li>
  <p>
   <a href="http://www.ntop.org/products/n2disk/">
    n2disk
   </a>
   (Commercial): A multi-Gigabit network traffic recorder with indexing capabilities. n2disk is a network traffic recorder application. With n2disk you can capture full- sized network packets at multi-Gigabit rate (above 10 Gigabit/s on adequate hardware) from a live network interface, and write them into files without any packet loss.
  </p>
 </li>
 <li>
  <p>
   <a href="http://www.openfpc.org/">
    OpenFPC
   </a>
   : OpenFPC is a set of scripts that combine to provide a lightweight full-packet network traffic recorder & buffering tool. Its design goal is to allow non-expert users to deploy a distributed network traffic recorder on COTS hardware while integrating into existing alert and log tools.
  </p>
 </li>
 <li>
  <p>
   <a href="http://www.ntop.org/products/pf_ring/">
    PF
    <em>
     RING
    </em>
   </a>
   : PF
  </p>
 </li>
</ul>
RING is a new type of network socket that dramatically improves the packet capture speed. Available for Linux kernels 2.6.32 and newer. No need to patch the kernel. PF_RING-aware drivers for increased packet capture acceleration.
<li>
 <p>
  <a href="http://www.csl.sony.co.jp/person/kjc/kjc/software.html#ttt">
   TTT
  </a>
  : (Tele Traffic Tapper) is yet another descendant of tcpdump but it is capable of real-time, graphical, and remote traffic-monitoring. ttt won't replace tcpdump, rather, it helps you find out what to look into with tcpdump. ttt monitors the network and automatically picks up the main contributors of the traffic within the time window. The graphs are updated every second by default.
 </p>
</li>
<li>
 <p>
  <a href="https://tools.netsa.cert.org/yaf/yaf.html">
   Yaf
  </a>
  : It's a reliable piece of software, quite solid and able to generate flow records from pcap. This is very nice for indexing huge pcap or even doing packet capture. The recent version can even extract payloads and put in the flow records.
 </p>
</li>
<h2>
 Traffic Analysis/Inspection
 <a name="analysis">
 </a>
</h2>
<ul>
 <li>
  <p>
   <a href="https://bitbucket.org/camp0/aiengine">
    AIEngine
   </a>
   : is a next generation interactive/programmable packet inspection engine with capabilities of learning without any human intervention, NIDS functionality, DNS domain classification, network collector and many others. AIEngine also helps network/security professionals to identify traffic and develop signatures for use them on NIDS, Firewalls, Traffic classifiers and so on.
  </p>
 </li>
 <li>
  <p>
   <a href="http://bro-ids.org/">
    Bro
   </a>
   : is an open-source, Unix-based Network Intrusion Detection System (NIDS) that passively monitors network traffic and looks for suspicious activity. Bro detects intrusions by first parsing network traffic to extract its application- level semantics and then executing event-oriented analyzers that compare the activity with patterns deemed troublesome. Its analysis includes detection of specific attacks (including those defined by signatures, but also those defined in terms of events) and unusual activities (e.g., certain hosts connecting to certain services, or patterns of failed connection attempts).
  </p>
 </li>
 <li>
  <p>
   <a href="https://github.com/omriher/CapTipper">
    CapTipper
   </a>
   <span>
    &#9733 320, pushed 271 days ago
   </span>
   : Malicious HTTP traffic explorer
  </p>
 </li>
 <li>
  <p>
   <a href="https://github.com/MITRECND/chopshop">
    Chopshop
   </a>
   <span>
    &#9733 228, pushed 7 days ago
   </span>
   : is a MITRE developed framework to aid analysts in the creation and execution of pynids based decoders and detectors of APT tradecraft.
  </p>
 </li>
 <li>
  <p>
   <a href="http://www.caida.org/tools/measurement/coralreef/">
    CoralReef
   </a>
   : is a software suite developed by CAIDA to analyze data collected by passive Internet traffic monitors. It provides a programming library libcoral, similar to libpcap with extensions for ATM and other network types, which is available from both C and Perl.
  </p>
 </li>
 <li>
  <p>
   <a href="http://dpdk.org/">
    DPDK
   </a>
   : is a set of libraries and drivers for fast packet processing. It was designed to run on any processors. The first supported CPU was Intel x86 and it is now extended to IBM Power 8, EZchip TILE-Gx and ARM. It runs mostly in Linux userland. A FreeBSD port is available for a subset of DPDK features.
  </p>
 </li>
 <li>
  <p>
   <a href="http://code.google.com/p/dpkt/">
    DPKT
   </a>
   : Python packet creation/parsing library.
  </p>
 </li>
 <li>
  <p>
   <a href="https://bitbucket.org/nathanj/ecap/wiki">
    ECap
   </a>
   : (External Capture) is a distributed network sniffer with a web front- end. Ecap was written many years ago in 2005, but a post on the tcpdump-workers mailing list requested a similar application... so here it is. It would be fun to update it and work on it again if there's any interest.
  </p>
 </li>
 <li>
  <p>
   <a href="http://etherape.sourceforge.net/">
    EtherApe
   </a>
   : is a graphical network monitor for Unix modeled after etherman. Featuring link layer, ip and TCP modes, it displays network activity graphically. Hosts and links change in size with traffic. Color coded protocols display. It supports Ethernet, FDDI, Token Ring, ISDN, PPP and SLIP devices. It can filter traffic to be shown, and can read traffic from a file as well as live from the network.
  </p>
 </li>
 <li>
  <p>
   <a href="https://github.com/caesar0301/http-sniffer">
    HttpSniffer
   </a>
   <span>
    &#9733 60, pushed 225 days ago
   </span>
   : A multi-threading tool to sniff TCP flow statistics and embedded HTTP headers from PCAP file. Each TCP flow carrying HTTP is exported to text file in JSON format.
  </p>
 </li>
 <li>
  <p>
   <a href="http://www.read.seas.harvard.edu/~kohler/ipsumdump/">
    Ipsumdump
   </a>
   : summarizes TCP/IP dump files into a self-describing ASCII format easily readable by humans and programs. Ipsumdump can read packets from network interfaces, from tcpdump files, and from existing ipsumdump files. It will transparently uncompress tcpdump or ipsumdump files when necessary. It can randomly sample traffic, filter traffic based on its contents, anonymize IP addresses, and sort packets from multiple dumps by timestamp. Also, it can optionally create a tcpdump file containing actual packet data. It's also convenient to work with CLICK as a inserted module.
  </p>
 </li>
 <li>
  <p>
   <a href="http://ita.ee.lbl.gov/">
    ITA
   </a>
   : The Internet Traffic Archive is a moderated repository to support widespread access to traces of Internet network traffic, sponsored by ACM SIGCOMM. The traces can be used to study network dynamics, usage characteristics, and growth patterns, as well as providing the grist for trace- driven simulations. The archive is also open to programs for reducing raw trace data to more manageable forms, for generating synthetic traces, and for analyzing traces.
  </p>
 </li>
 <li>
  <p>
   <a href="http://code.google.com/p/libcrafter/">
    Libcrafter
   </a>
   : is a high level library for C++ designed to make easier the creation and decoding of network packets. It is able to craft or decode packets of most common network protocols, send them on the wire, capture them and match requests and replies.
  </p>
 </li>
 <li>
  <p>
   <a href="http://libnet.sourceforge.net/">
    Libnet
   </a>
   : is a collection of routines to help with the construction and handling of network packets. It provides a portable framework for low-level network packet shaping, handling and injection. Libnet features portable packet creation interfaces at the IP layer and link layer, as well as a host of supplementary and complementary functionality. Using libnet, quick and simple packet assembly applications can be whipped up with little effort.
  </p>
 </li>
 <li>
  <p>
   <a href="http://libnids.sourceforge.net/">
    Libnids
   </a>
   : designed by Rafal Wojtczuk, is an implementation of an E-component of Network Intrusion Detection System. It emulates the IP stack of Linux 2.0.x. Libnids offers IP defragmentation, TCP stream assembly and TCP port scan detection. The most valuable feature of libnids is reliability. A number of tests were conducted, which proved that libnids predicts behaviour of protected Linux hosts as closely as possible.
  </p>
 </li>
 <li>
  <p>
   <a href="http://www.vanheusden.com/multitail">
    Multitail
   </a>
   : now has a colorscheme included for monitoring the tcpdump output. It can also filter, convert timestamps to timestrings and much more.
  </p>
 </li>
 <li>
  <p>
   <a href="www.github.com/borkmann/netsniff-ng">
    Netsniff-ng
   </a>
   : Netsniff-ng is a toolkit of free Linux networking utilities, a Swiss army knife for your daily Linux network plumbing if you will.
  </p>
 </li>
 <li>
  <p>
   <a href="http://netdude.sourceforge.net/">
    NetDude
   </a>
   : (NETwork DUmp data Displayer and Editor). From their webpage, "it is a GUI-based tool that allows you to make detailed changes to packets in tcpdump tracefiles."
  </p>
 </li>
 <li>
  <p>
   <a href="http://www.netexpect.org/">
    Network Expect
   </a>
   : is a framework that allows to easily build tools that can interact with network traffic. Following a script, traffic can be injected into the network, and decisions can be taken, and acted upon, based on received network traffic. An interpreted language provides branching and high-level control structures to direct the interaction with the network. Network Expect uses libpcap for packet capture and libwireshark (from the Wireshark project) for packet dissection tasks. (GPL, BSD/Linux/OSX).
  </p>
 </li>
 <li>
  <p>
   <a href="http://www.ntop.org/">
    Ntop
   </a>
   : Ntop is a network traffic probe that shows the network usage, similar to what the popular top Unix command does. ntop is based on libpcap and it has been written in a portable way in order to virtually run on every Unix platform and on Win32 as well.
  </p>
 </li>
 <li>
  <p>
   <a href="http://www.ntop.org/products/ntop/">
    Ntopng
   </a>
   : Ntopng is the next generation version of the original ntop, a network traffic probe that shows the network usage, similar to what the popular top Unix command does. ntop is based on libpcap and it has been written in a portable way in order to virtually run on every Unix platform, MacOSX and on Win32 as well.
  </p>
 </li>
 <li>
  <p>
   <a href="https://github.com/andrewf/pcap2har">
    Pcap2har
   </a>
   <span>
    &#9733 130, pushed 242 days ago
   </span>
   : A program to convert .pcap network capture files to HTTP Archive files using library dpkt.
  </p>
 </li>
 <li>
  <p>
   <a href="https://github.com/caesar0301/pkt2flow">
    pkt2flow
   </a>
   <span>
    &#9733 35, pushed 722 days ago
   </span>
   : A simple utility to classify packets into flows. It's so simple that only one task is aimed to finish.  For Deep Packet Inspection or flow classification, it's so common to analyze the feature of one specific flow. I have make the attempt to use made-ready tools like tcpflows, tcpslice, tcpsplit, but all these tools try to either decrease the trace volume (under requirement) or resemble the packets into flow payloads (over requirement). I have not found a simple tool to classify the packets into flows without further processing.
  </p>
 </li>
 <li>
  <p>
   <a href="https://github.com/CIRCL/potiron">
    potiron
   </a>
   <span>
    &#9733 13, pushed 251 days ago
   </span>
   : Normalizes, indexes, enriches and visualizes network captures.
  </p>
 </li>
 <li>
  <p>
   <a href="http://kiminewt.github.io/pyshark/">
    pyshark
   </a>
   : A Python wrapper for tshark, allowing python packet parsing using wireshark dissectors. There are quite a few python packet parsing modules, this one is different because it doesn't actually parse any packets, it simply uses tshark's (wireshark command-line utility) ability to export XMLs to use its parsing.
  </p>
 </li>
 <li>
  <p>
   <a href="http://ita.ee.lbl.gov/html/contrib/sanitize.html">
    Sanitize
   </a>
   : Sanitize is a collection of five Bourne shell scripts for reducing tcpdump traces in order to address security and privacy concerns, by renumbering hosts and stripping out packet contents. Each script takes as input a tcpdump trace file and generates to stdout a reduced, ASCII file in fixed-column format.
  </p>
 </li>
 <li>
  <p>
   <a href="http://www.secdev.org/projects/scapy/">
    Scapy
   </a>
   : Scapy is a powerful interactive packet manipulation program. It is able to forge or decode packets of a wide number of protocols, send them on the wire, capture them, match requests and replies, and much more. It can easily handle most classical tasks like scanning, tracerouting, probing, unit tests, attacks or network discovery (it can replace hping, 85% of nmap, arpspoof, arp-sk, arping, tcpdump, tethereal, p0f, etc.). It also performs very well at a lot of other specific tasks that most other tools can't handle, like sending invalid frames, injecting your own 802.11 frames, combining technics (VLAN hopping+ARP cache poisoning, VOIP decoding on WEP encrypted channel, ...), etc.
  </p>
 </li>
 <li>
  <p>
   <a href="http://www.thedumbterminal.co.uk/software/sniff.html">
    Sniff
   </a>
   : Makes output from the tcpdump program easier to read and parse.
  </p>
 </li>
 <li>
  <p>
   <a href="http://www.snort.org/">
    Snort
   </a>
   : Snort is an open source network intrusion prevention and detection system (IDS/IPS) developed by Sourcefire, now owned by Cisco. Combining the benefits of signature, protocol and anomaly- based inspection, Snort is the most widely deployed IDS/IPS technology worldwide. With millions of downloads and approximately 500,000 registered users, Snort has become the de facto standard for IPS.
  </p>
 </li>
 <li>
  <p>
   <a href="http://code.google.com/p/socket-sentry">
    Socket Sentry
   </a>
   : Socket Sentry is a real-time network traffic monitor for KDE Plasma in the same spirit as tools like iftop and netstat.
  </p>
 </li>
 <li>
  <p>
   <a href="http://ita.ee.lbl.gov/html/contrib/tcp-reduce.html">
    TCP-Reduce
   </a>
   : TCP-Reduce is a collection of Bourne shell scripts for reducing tcpdump traces to one-line summaries of each TCP connection present in the trace. The scripts look only at TCP SYN/FIN/RST packets. Connections without SYN packets in the trace (such as those on- going at the beginning of the trace) will not appear in the summary. Garbaged packets (those missing some of their contents) are reported to stderr as bogon's and are discarded. Occasionally the script gets fooled by retransmissions with altered sequence numbers, and reports erroneous huge connection sizes - always check large connections (say 100 MB or more) for plausibility.
  </p>
 </li>
 <li>
  <p>
   <a href="http://ita.ee.lbl.gov/html/contrib/tcpdpriv.html">
    Tcpdpriv
   </a>
   : Tcpdpriv is program for eliminating confidential information (user data and addresses) from packets collected on a network interface (or, from trace files created using the -w argument to tcpdump). Tcpdpriv removes the payload of TCP and UDP, and the entire IP payload for other protocols. It implements several address scrambling methods; the sequential numbering method and its variants, and a hash method with preserving address prefix.
  </p>
 </li>
 <li>
  <p>
   <a href="https://github.com/simsong/tcpflow">
    Tcpflow
   </a>
   <span>
    &#9733 516, pushed 98 days ago
   </span>
   : A program that captures data transmitted as part of TCP connections (flows), and stores the data in a way that is convenient for protocol analysis or debugging. A program like 'tcpdump' shows a summary of packets seen on the wire, but usually doesn't store the data that's actually being transmitted. In contrast, tcpflow reconstructs the actual data streams and stores each flow in a separate file for later analysis.
   <a href="http://www.circlemud.org/jelson/software/tcpflow/">
    Original link
   </a>
   .
  </p>
 </li>
 <li>
  <p>
   <a href="http://ita.ee.lbl.gov/html/contrib/tracelook.html">
    Tcplook
   </a>
   : Tracelook is an Tcl/TK program for graphically viewing the contents of trace files created using the -w argument to tcpdump. Tracelook should look at all protocols, but presently only looks at TCP connections. The program is slow and uses system resources prodigiously.
  </p>
 </li>
 <li>
  <p>
   <a href="http://tcpreplay.synfin.net/">
    Tcpreplay
   </a>
   : Replays a pcap file on an interface using libnet.
  </p>
 </li>
 <li>
  <p>
   <a href="ftp://ftp.ee.lbl.gov/tcpslice.tar.gz">
    Tcpslice
   </a>
   : Tcpslice is a tool for extracting portions of packet trace files generated using tcpdump's -w flag. It can combine multiple trace files, and/or extract portions of one or more traces based on time.
   <a href="ftp://ftp.ee.lbl.gov/tcpslice.tar.gz">
    From the tcpdump CVS server
   </a>
   .
  </p>
 </li>
 <li>
  <p>
   <a href="http://www.icir.org/mallman/software/tcpsplit/">
    Tcpsplit
   </a>
   : A tool to break a single libpcap packet trace into some number of sub- traces, breaking the trace along TCP connection boundaries so that a TCP connection doesn't end up split across two sub-traces. This is useful for making large trace files tractable for in- depth analysis and for subsetting a trace for developing analysis on only part of a trace.
  </p>
 </li>
 <li>
  <p>
   <a href="http://www.frenchfries.net/paul/tcpstat/">
    Tcpstat
   </a>
   : Tcpstat reports certain network interface statistics much like vmstat does for system statistics. tcpstat gets its information by either monitoring a specific interface, or by reading previously saved tcpdump data from a file.
  </p>
 </li>
 <li>
  <p>
   <a href="http://tcptrace.org/index.html">
    Tcptrace
   </a>
   : A tool written by Shawn Ostermann at Ohio University, for analysis of TCP dump files. It can take as input the files produced by several popular packet- capture programs, including tcpdump, snoop, etherpeek, HP Net Metrix, and WinDump. tcptrace can produce several different types of output containing information on each connection seen, such as elapsed time, bytes and segments sent and received, retransmissions, round trip times, window advertisements, throughput, and more. It can also produce a number of graphs for further analysis.
  </p>
 </li>
 <li>
  <p>
   <a href="https://www.tracewrangler.com/">
    TraceWrangler
   </a>
   : TraceWrangler is a network capture file toolkit running on Windows (or on Linux, using WINE) that supports PCAP as well as the new PCAPng file format, which is now the standard file format used by Wireshark. The most prominent use case for TraceWrangler is the easy sanitization and anonymization of PCAP and PCAPng files (sometimes called "trace files", "capture files" or "packet captures"), removing or replacing sensitive data while being easy to use.
  </p>
 </li>
 <li>
  <p>
   <a href="http://tstat.tlc.polito.it/">
    Tstat
   </a>
   : A passive sniffer able to provide several insight on the traffic patterns at both the network and transport levels with a tremendous set of flow features.
  </p>
 </li>
 <li>
  <p>
   <a href="http://research.wand.net.nz/">
    WAND
   </a>
   : A wonderful collection of tools built on libtrace to process network traffic, which is from The University of Waikato. I love this project!
  </p>
 </li>
 <li>
  <p>
   <a href="http://www.tcpdump.org/wpcap.html">
    WinPcap
   </a>
   : An extract of a message from Guy Harris on state of WinPcap and WinDump.
  </p>
 </li>
 <li>
  <p>
   <a href="http://wiki.wireshark.org/Tools">
    Wireshark suit
   </a>
   : The well-known tool suit to support packet analyzer and protocol decoder. It also includes a few practical tools and scripts to support most of the common usage.
  </p>
 </li>
 <li>
  <p>
   <a href="http://www.xplot.org/">
    Xplot
   </a>
   : The program xplot was written in the late 1980s to support the analysis of TCP packet traces.
  </p>
 </li>
 <li>
  <p>
   <a href="https://github.com/kevthehermit/YaraPcap">
    yaraPcap
   </a>
   <span>
    &#9733 33, pushed 1009 days ago
   </span>
   : Process HTTP Pcaps With YARA
  </p>
 </li>
 <li>
  <p>
   <a href="https://github.com/MITRECND/yaraprocessor">
    yaraprocessor
   </a>
   <span>
    &#9733 55, pushed 560 days ago
   </span>
   : With yaraprocessor YARA can be run against individual packet payloads as well as a concatenation of some or all of the payloads. It was originally written for use in Chopshop, but can also be used without it.
  </p>
 </li>
</ul>
<h2>
 DNS Utilities
 <a name="dnstools">
 </a>
</h2>
<ul>
 <li>
  <p>
   <a href="https://doc.powerdns.com/md/manpages/dnsgram.1/">
    dnsgram
   </a>
   : dnsgram is a debugging tool for intermittent resolver failures. it takes one or more input PCAP files and generates statistics on 5 second segments allowing the study of intermittent resolver issues.
  </p>
 </li>
 <li>
  <p>
   <a href="https://doc.powerdns.com/md/manpages/dnsreplay.1/">
    dnsreplay
   </a>
   : Dnsreplay takes recorded questions and answers and replays them to the specified nameserver and reporting afterwards which percentage of answers matched, were worse or better. Then compares the answers and some other metrics with the actual ones with those found in the dumpfile.
  </p>
 </li>
 <li>
  <p>
   <a href="https://doc.powerdns.com/md/manpages/dnsscan.1/">
    dnsscan
   </a>
   : dnsscan takes one or more INFILEs in PCAP format and generates a list of the number of queries per query type.
  </p>
 </li>
 <li>
  <p>
   <a href="https://doc.powerdns.com/md/manpages/dnsscope.1/">
    dnsscope
   </a>
   : dnsscope takes an input PCAP and generates some simple statistics outputs these to console.
  </p>
 </li>
 <li>
  <p>
   <a href="https://doc.powerdns.com/md/manpages/dnswasher.1/">
    dnswasher
   </a>
   : dnswasher takes an input file in PCAP format and writes out a PCAP file, while obfuscating end-user IP addresses. This is useful to share data with third parties while attempting to protect the privacy of your users.
  </p>
 </li>
</ul>
<h2>
 File Extraction
 <a name="fileextraction">
 </a>
</h2>
<ul>
 <li>
  <p>
   <a href="http://chaosreader.sourceforge.net/">
    Chaosreader
   </a>
   : A freeware tool to trace TCP/UDP/... sessions and fetch application data from snoop or tcpdump logs. This is a type of "any-snarf" program, as it will fetch telnet sessions, FTP files, HTTP transfers (HTML, GIF, JPEG, ...), SMTP emails, ... from the captured data inside network traffic logs. A html index file is created that links to all the session details, including realtime replay programs for telnet, rlogin, IRC, X11 and VNC sessions; and reports such as image reports and HTTP GET/POST content reports.
  </p>
 </li>
 <li>
  <p>
   <a href="http://www.monkey.org/~dugsong/dsniff/">
    Dsniff
   </a>
   : Dsniff is a collection of tools for network auditing and penetration testing. dsniff, filesnarf, mailsnarf, msgsnarf, urlsnarf, and webspy passively monitor a network for interesting data (passwords, e-mail, files, etc.). arpspoof, dnsspoof, and macof facilitate the interception of network traffic normally unavailable to an attacker (e.g, due to layer-2 switching). sshmitm and webmitm implement active monkey-in-the-middle attacks against redirected SSH and HTTPS sessions by exploiting weak bindings in ad-hoc PKI.
  </p>
 </li>
 <li>
  <p>
   <a href="http://foremost.sourceforge.net/">
    Foremost
   </a>
   : is a console program to recover files based on their headers, footers, and internal data structures. This process is commonly referred to as data carving. Foremost can work on image files, such as those generated by dd, Safeback, Encase, etc, or directly on a drive. The headers and footers can be specified by a configuration file or you can use command line switches to specify built-in file types. These built-in types look at the data structures of a given file format allowing for a more reliable and faster recovery.
  </p>
 </li>
 <li>
  <p>
   <a href="http://justniffer.sourceforge.net/">
    Justniffer
   </a>
   : Justniffer is a network protocol analyzer that captures network traffic and produces logs in a customized way, can emulate Apache web server log files, track response times and extract all "intercepted" files from the HTTP traffic.
  </p>
 </li>
 <li>
  <p>
   <a href="http://www.netresec.com/?page=NetworkMiner">
    NetworkMiner
   </a>
   : NetworkMiner is a Network Forensic Analysis Tool (NFAT) for Windows (but also works in Linux / Mac OS X / FreeBSD). NetworkMiner can be used as a passive network sniffer/packet capturing tool in order to detect operating systems, sessions, hostnames, open ports etc. without putting any traffic on the network. NetworkMiner can also parse PCAP files for off-line analysis and to regenerate/ reassemble transmitted files and certificates from PCAP files.
  </p>
 </li>
 <li>
  <p>
   <a href="https://github.com/vikwin/pcapfex">
    pcapfex
   </a>
   <span>
    &#9733 11, pushed 62 days ago
   </span>
   - Packet CAPture Forensic Evidence eXtractor (pcapfex) is a tool that finds and extracts files from packet capture files. Its power lies in its ease of use. Just provide it a pcap file, and it will try to extract all of the files. It is an extensible platform, so additional file types to recognize and extract can be added easily.
  </p>
 </li>
 <li>
  <p>
   <a href="https://github.com/sleuthkit/scalpel">
    scalpel
   </a>
   <span>
    &#9733 103, pushed 162 days ago
   </span>
   : Scalpel is an open source data carving tool.
  </p>
 </li>
 <li>
  <p>
   <a href="http://www.snort.org/">
    Snort
   </a>
   : is an open source network intrusion prevention and detection system (IDS/IPS) developed by Sourcefire, now owned by Cisco. Combining the benefits of signature, protocol and anomaly- based inspection, Snort is the most widely deployed IDS/IPS technology worldwide.
  </p>
 </li>
 <li>
  <p>
   <a href="http://tcpick.sourceforge.net/">
    Tcpick
   </a>
   : is a textmode sniffer libpcap-based that can track, reassemble and reorder tcp streams. Tcpick is able to save the captured flows in different files or displays them in the terminal, and so it is useful to sniff files that are transmitted via ftp or http. It can display all the stream on the terminal, when the connection is closed in different display modes like hexdump, hexdump + ascii, only printable characters, raw mode and so on.
  </p>
 </li>
 <li>
  <p>
   <a href="http://tcpxtract.sourceforge.net/">
    Tcpxtract
   </a>
   : is a tool for extracting files from network traffic based on file signatures. Extracting files based on file type headers and footers (sometimes called "carving") is an age old data recovery technique.
  </p>
 </li>
 <li>
  <p>
   <a href="http://www.xplico.org/about">
    Xplico
   </a>
   : The goal of Xplico is extract from an internet traffic capture the applications data contained. For example, from a pcap file Xplico extracts each email (POP, IMAP, and SMTP protocols), all HTTP contents, each VoIP call (SIP), FTP, TFTP, and so on. Xplico isn't a network protocol analyzer. Xplico is an open source Network Forensic An alysis Tool (NFAT). Xplico is released under the GNU General Public License and with some scripts under Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0) License.
  </p>
 </li>
</ul>
<h2>
 Related Projects
 <a name="others">
 </a>
</h2>
<ul>
 <li>
  <p>
   <a href="http://www.tcpdump.org/other/bpfext42.tar.Z">
    BPF for Ultrix
   </a>
   : A distribution of BPF for Ultrix 4.2, with both source code and binary modules.
  </p>
 </li>
 <li>
  <p>
   <a href="http://www.cs.berkeley.edu/~abegel/sigcomm99/bpf+.ps">
    BPF+
   </a>
   : Exploiting Global Data-flow Optimization in a Generalized Packet Filter Architecture By Andrew Begel, Steven McCanne, and Susan Graham.
  </p>
 </li>
 <li>
  <p>
   <a href="http://ita.ee.lbl.gov/html/contrib/fft_fgn_c.html">
    FFT-FGN-C
   </a>
   : is a program for synthesizing a type of self-similar process known as fractional Gaussian noise. The program is fast but approximate. Fractional Gaussian noise is only one type of self-similar process. When using this program for synthesizing network traffic, you must keep in mind that it may be that the traffic you seek is better modeled using one of the other processes.
  </p>
 </li>
 <li>
  <p>
   <a href="http://www.haka-security.org/">
    Haka
   </a>
   : An open source security oriented language which allows to describe protocols and apply security policies on (live) captured traffic. The scope of Haka language is twofold. First of all, it allows to write security rules in order to filter/alter/drop unwanted packets and log and report malicious activities. Second, Haka features a grammar enabling to specify network protocols and their underlying state machine.
  </p>
 </li>
 <li>
  <p>
   <a href="https://github.com/RIPE-NCC/hadoop-pcap">
    RIPE-NCC Hadoop for PCAP
   </a>
   <span>
    &#9733 142, pushed 3 days ago
   </span>
   : A Hadoop library to read packet capture (PCAP) files. Bundles the code used to read PCAPs. Can be used within MapReduce jobs to natively read PCAP files. Also features a Hive Serializer/Deserializer (SerDe) to query PCAPs using SQL like commands.
  </p>
 </li>
 <li>
  <p>
   <a href="http://www.sonycsl.co.jp/person/kjc/papers/freenix2000/">
    Traffic Data Repository at the WIDE Project
   </a>
   : It becomes increasingly important for both network researchers and operators to know the trend of network traffic and to find anomaly in their network traffic. This paper describes an on-going effort within the WIDE project to collect a set of free tools to build a traffic data repository containing detailed information of our backbone traffic. Traffic traces are collected by tcpdump and, after removing privacy information, the traces are made open to the public. We review the issues on user privacy, and then, the tools used to build the WIDE traffic repository. We will report the current status and findings in the early stage of our IPv6 deployment.
  </p>
 </li>
 <li>
  <p>
   <a href="ftp://ftp.ee.lbl.gov/papers/bpf-usenix93.ps.Z">
    Usenix93 Paper on BPF
   </a>
   : The libpcap interface supports a filtering mechanism based on the architecture in the BSD packet filter. BPF is described in the 1993 Winter Usenix paper "The BSD Packet Filter: A New Architecture for User-level Packet Capture".
  </p>
 </li>
</ul>
