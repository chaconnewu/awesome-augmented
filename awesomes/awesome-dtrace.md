<h1>
 Awesome DTrace
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<p>
 A curated list of awesome DTrace books, articles, videos, tools and resources.
</p>
<h2>
 Contents
</h2>
<ul>
 <li>
  <a href="#learn">
   Learn
  </a>
 </li>
 <li>
  <a href="#articles">
   Articles
  </a>
 </li>
 <li>
  <a href="#videos">
   Videos
  </a>
 </li>
 <li>
  <a href="#software">
   Software
  </a>
 </li>
 <li>
  <a href="#tools">
   Tools
  </a>
 </li>
 <li>
  <a href="#community">
   Community
  </a>
 </li>
 <li>
  <a href="#contributing">
   Contributing
  </a>
 </li>
</ul>
<hr/>
<h2>
 Learn
</h2>
<p>
 Recommended reading for learning DTrace.
</p>
<h3>
 Books
</h3>
<ul>
 <li>
  <a href="http://dtrace.org/guide/preface.html">
   Dynamic Tracing Guide
  </a>
  - Illumos.org DTrace guide.
 </li>
 <li>
  <a href="http://www.dtracebook.com/index.php/Main_Page">
   DTrace: Dynamic Tracing in Oracle Solaris, Mac OS X, and FreeBSD
  </a>
  - Official DTrace book.
 </li>
 <li>
  <a href="http://myaut.github.io/dtrace-stap-book/">
   Dynamic Tracing with DTrace & SystemTap
  </a>
  - A book introduces both DTrace and SystemTap.
 </li>
</ul>
<h3>
 Other
</h3>
<ul>
 <li>
  <a href="https://illumos.org/man/1m/dtrace">
   dtrace(1m) man page
  </a>
  - DTrace manual page.
 </li>
 <li>
  <a href="http://www.brendangregg.com/DTrace/DTrace-cheatsheet.pdf">
   DTrace cheatsheet
  </a>
  - DTrace cheatsheet by Brendan Gregg.
 </li>
 <li>
  <a href="http://www.brendangregg.com/DTrace/dtrace_oneliners.txt">
   DTrace one-liners
  </a>
  - DTrace one liners. Handy commands.
 </li>
 <li>
  <a href="https://wiki.freebsd.org/DTrace/One-Liners">
   DTrace one-liners (FreeBSD)
  </a>
  - DTrace one liners from FreeBSD.
 </li>
 <li>
  <a href="http://www.tablespace.net/quicksheet/dtrace-quickstart.html">
   DTrace QuickStart
  </a>
  - DTrace quick starting guide.
 </li>
 <li>
  <a href="https://github.com/NanXiao/using-dtrace-stories">
   Using DTrace stories
  </a>
  - A collection of using DTrace to debug system stories.
 </li>
</ul>
<h2>
 Articles
</h2>
<p>
 Interesting articles about DTrace and real-world use cases.
</p>
<h3>
 PID Provider
</h3>
<ul>
 <li>
  <a href="http://dtrace.org/blogs/brendan/2011/02/09/dtrace-pid-provider/">
   pid provider: entry probe
  </a>
  - DTrace PID Provider.
 </li>
 <li>
  <a href="http://dtrace.org/blogs/brendan/2011/02/11/dtrace-pid-provider-arguments/">
   pid provider: entry arguments
  </a>
  - DTrace PID Provider Arguments.
 </li>
 <li>
  <a href="http://dtrace.org/blogs/brendan/2011/02/14/dtrace-pid-provider-return/">
   pid provider: return
  </a>
  - DTrace PID Provider return.
 </li>
 <li>
  <a href="http://dtrace.org/blogs/brendan/2011/02/16/dtrace-pid-provider-instructions/">
   pid provider: instructions
  </a>
  - DTrace PID Provider Instructions.
 </li>
 <li>
  <a href="http://dtrace.org/blogs/brendan/2011/02/18/dtrace-pid-provider-overhead/">
   pid provider: overhead
  </a>
  - DTrace PID Provider Overhead.
 </li>
 <li>
  <a href="http://dtrace.org/blogs/ahl/2005/03/01/pid-provider-exposed/">
   pid provider exposed
  </a>
  - PID providers internals by Adam Leventhal.
 </li>
 <li>
  <a href="http://dtrace.org/blogs/bmc/2011/03/09/when-magic-collides/">
   When magic collides
  </a>
  - PID provider bug deep dive by Bryan Cantrill.
 </li>
</ul>
<h3>
 USDT provider
</h3>
<ul>
 <li>
  <a href="http://dtrace.org/blogs/dap/2013/11/20/understanding-dtrace-ustack-helpers/">
   Understanding DTrace ustack helpers
  </a>
  - DTrace ustack helpers.
 </li>
 <li>
  <a href="http://dtrace.org/blogs/dap/2011/12/13/usdt-providers-redux/">
   USDT Providers Redux
  </a>
  - Reference for building USDT providers in custom applications.
 </li>
</ul>
<h3>
 Sysevent provider
</h3>
<ul>
 <li>
  <a href="https://blogs.oracle.com/eschrock/entry/dtrace_sysevent_provider">
   DTrace sysevent provider
  </a>
  - Solaris/illumos sysevent provider for DTrace.
 </li>
</ul>
<h3>
 Visualization methods
</h3>
<ul>
 <li>
  <a href="http://www.brendangregg.com/flamegraphs.html">
   Flamegraphs
  </a>
  - A visualization of profiled software, allowing the most frequent code-paths to be identified quickly and accurately.
 </li>
 <li>
  <a href="http://brendangregg.com/heatmaps.html">
   Heat Maps
  </a>
  - Heat maps allow three dimensions of data to be visualized, similar to weather radar maps where color is used as a dimension.
 </li>
</ul>
<h2>
 Videos
</h2>
<p>
 Interesting videos about DTrace.
</p>
<ul>
 <li>
  <a href="https://www.youtube.com/watch?v=TgmA48fILq8">
   DTrace review
  </a>
  - Bryan Cantrill explains how to significantly improve debugging both for development and live systems with DTrace.
 </li>
</ul>
<h3>
 dtrace.conf
</h3>
<ul>
 <li>
  <p>
   <a href="https://youtu.be/RvyP61WeFdM?list=PL8516982CBF9FADCC">
    dtrace.conf 2008
   </a>
  </p>
  <ul>
   <li>
    <a href="https://www.youtube.com/watch?v=sgBCz7bXkSo&index=4&list=PL8516982CBF9FADCC">
     NFSv3 and iSCSI providers
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=1Bc2Dz8aS6s&list=PL8516982CBF9FADCC&index=5">
     DTrace for hardware
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=D8_onK0pSvA&index=8&list=PL8516982CBF9FADCC">
     Zones & DTrace
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=e55iXXYj-74&index=10&list=PL8516982CBF9FADCC">
     DTracing a Solaris build
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=yR39YqVXQOM&index=11&list=PL8516982CBF9FADCC">
     War Stories
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=uK0DjEXo99w&list=PL8516982CBF9FADCC&index=12">
     Sun Benchmarks
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=PXIGE5GFAkE&index=13&list=PL8516982CBF9FADCC">
     Erlang
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=YTNiCv9Za2Y&index=14&list=PL8516982CBF9FADCC">
     Erlang (continued)
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=4astU1_X5xM&index=15&list=PL8516982CBF9FADCC">
     Instrumenting Adobe AIR
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=8kdJDHqiByI&list=PL8516982CBF9FADCC&index=16">
     HotSpot Runtime & Java
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=p5NKcxDny_4&list=PL8516982CBF9FADCC&index=17">
     PostgreSQL: Looking Under the Hood with Solaris
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=SJykRURWgeU&list=PL8516982CBF9FADCC&index=18">
     PostgreSQL Provider
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=oYK1kgFwxk4&index=19&list=PL8516982CBF9FADCC">
     Distributed DTrace
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=OKSuox4eFrk&list=PL8516982CBF9FADCC&index=21">
     Apple Port of DTrace
    </a>
   </li>
  </ul>
 </li>
 <li>
  <p>
   <a href="https://www.youtube.com/watch?v=l_7v7Fn7uMQ&list=PL973D48F273EB0360">
    dtrace.conf 2012
   </a>
  </p>
  <ul>
   <li>
    <a href="https://www.youtube.com/watch?v=l_7v7Fn7uMQ&list=PL973D48F273EB0360">
     DTrace State of the Union
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=0QF04ivO_WE&list=PL973D48F273EB0360&index=3">
     User-Level CTF
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=CqLcj0lVnp4&index=4&list=PL973D48F273EB0360">
     Dynamic Translators
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=6NqV_Uj8Ba4&index=7&list=PL973D48F273EB0360">
     Clang Parser for DTrace
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=XD5hdaWnQM4&index=8&list=PL973D48F273EB0360">
     Visualizations
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=3Sqa8mmtnMM&index=9&list=PL973D48F273EB0360">
     Visualizations, Enabling Toolchain for Seamless USDT
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=-B6u6wY3Iro&index=10&list=PL973D48F273EB0360">
     More Visualizations
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=0ZMvSh7lUdM&list=PL973D48F273EB0360&index=11">
     DTrace in Node.js
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=4Si-7nAic2c&list=PL973D48F273EB0360&index=12">
     DTrace and Erlang
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=NElog3MvUC8&list=PL973D48F273EB0360&index=13">
     DTrace on Linux
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=m_V7yrrn49Y&index=14&list=PL973D48F273EB0360">
     ZFS Provider
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=s5PpSiPfSNI&index=15&list=PL973D48F273EB0360">
     DTrace on FreeBSD
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=P95LHZ-WOWw&index=16&list=PL973D48F273EB0360">
     Barriers to DTrace Adoption
    </a>
   </li>
  </ul>
 </li>
 <li>
  <p>
   <a href="https://www.joyent.com/about/events/2016/dtrace-conf">
    dtrace.conf 2016
   </a>
  </p>
  <ul>
   <li>
    <a href="https://player.vimeo.com/video/173346406">
     Introduction
    </a>
   </li>
   <li>
    <a href="https://player.vimeo.com/video/173346405">
     (Useful!) DTrace intro
    </a>
   </li>
   <li>
    <a href="https://player.vimeo.com/video/173346404">
     CTF Everywhere!
    </a>
   </li>
   <li>
    <a href="https://player.vimeo.com/video/173346403">
     Distributed DTrace
    </a>
   </li>
   <li>
    <a href="https://player.vimeo.com/video/173346402">
     DTracign Apps
    </a>
   </li>
   <li>
    <a href="https://player.vimeo.com/video/173346401">
     DTrace and JSON: Together at last!
    </a>
   </li>
   <li>
    <a href="https://player.vimeo.com/video/173346400">
     ASSERT() as a DTrace probe (and why I need some help)
    </a>
   </li>
   <li>
    <a href="https://player.vimeo.com/video/173346399">
     Implementing (or not) fds[] in FreeBSD
    </a>
   </li>
   <li>
    <a href="https://player.vimeo.com/video/173346398">
     OpenDTrace
    </a>
   </li>
   <li>
    <a href="https://player.vimeo.com/video/173300658">
     DTrace Performance Improvements with Always-on Instrumentation
    </a>
   </li>
   <li>
    <a href="https://player.vimeo.com/video/173300657">
     D language improvements
    </a>
   </li>
   <li>
    <a href="https://player.vimeo.com/video/173300656">
     D Syntactic Sugar
    </a>
   </li>
   <li>
    <a href="https://player.vimeo.com/video/173300655">
     DTrace and Go
    </a>
   </li>
   <li>
    <a href="https://player.vimeo.com/video/173300654">
     DTrace and Postgres
    </a>
   </li>
   <li>
    <a href="https://player.vimeo.com/video/173300653">
     DTrace in the Zone
    </a>
   </li>
   <li>
    <a href="https://player.vimeo.com/video/173300651">
     DTrace ustack() performance improvements
    </a>
   </li>
   <li>
    <a href="https://player.vimeo.com/video/173300650">
     DTrace Exploitation
    </a>
   </li>
  </ul>
 </li>
</ul>
<h2>
 Software
</h2>
<p>
 List of software with DTrace support.
</p>
<h3>
 Programming languages
</h3>
<h4>
 Erlang
</h4>
<ul>
 <li>
  <a href="http://erlang.org/doc/apps/runtime_tools/DTRACE.html">
   Erlang
  </a>
  - DTrace and Erlang/OTP.
 </li>
</ul>
<h4>
 Lua
</h4>
<ul>
 <li>
  <a href="https://github.com/chrisa/lua-usdt">
   lua-usdt
  </a>
  - Libusdt bindings for Lua.
 </li>
</ul>
<h4>
 Node.js
</h4>
<ul>
 <li>
  <a href="https://github.com/chrisa/node-dtrace-provider">
   node-dtrace-provider
  </a>
  - Native DTrace probes for Node.js apps.
 </li>
</ul>
<h4>
 Perl
</h4>
<ul>
 <li>
  <a href="https://github.com/chrisa/perl-Devel-DTrace-Provider">
   perl-Devel-DTrace-Provider
  </a>
  - Perl wrapper for libusdt.
 </li>
</ul>
<h4>
 PHP
</h4>
<ul>
 <li>
  <a href="https://secure.php.net/manual/en/features.dtrace.dtrace.php">
   PHP
  </a>
  - Using PHP and DTrace.
 </li>
</ul>
<h4>
 Python
</h4>
<ul>
 <li>
  <a href="https://www.jcea.es/artic/python_dtrace.htm">
   Python
  </a>
  - DTrace patch for Python 2.7.x and 3.x.
 </li>
 <li>
  <a href="https://github.com/nshalman/python-usdt">
   python-usdt
  </a>
  - Libusdt bindings for Python.
 </li>
</ul>
<h4>
 Ruby
</h4>
<ul>
 <li>
  <a href="http://ruby-doc.org/core-2.3.1/doc/dtrace_probes_rdoc.html">
   Ruby
  </a>
  - Ruby DTrace probes.
 </li>
 <li>
  <a href="https://github.com/kevinykchan/ruby-usdt">
   ruby-usdt
  </a>
  - Native DTrace probes for ruby apps.
 </li>
</ul>
<h3>
 Databases
</h3>
<ul>
 <li>
  <a href="https://dev.mysql.com/doc/refman/5.7/en/dba-dtrace-mysqld-ref.html">
   MySQL
  </a>
  - MySQL DTrace probes.
 </li>
 <li>
  <a href="https://www.postgresql.org/docs/current/static/dynamic-trace.html">
   PostgreSQL
  </a>
  - PostgreSQL DTrace probes.
 </li>
</ul>
<h3>
 Webservers
</h3>
<ul>
 <li>
  <a href="https://github.com/davepacheco/mod_usdt">
   mod_usdt
  </a>
  - "httpd" DTrace provider.
 </li>
</ul>
<h3>
 Visualization
</h3>
<ul>
 <li>
  <a href="https://github.com/brendangregg/FlameGraph">
   FlameGraph
  </a>
  - Stack trace visualizer.
 </li>
 <li>
  <a href="https://github.com/joyent/node-stackvis">
   node-stackvis
  </a>
  - Stack trace visualizer.
 </li>
</ul>
<h2>
 Tools
</h2>
<ul>
 <li>
  <a href="http://www.brendangregg.com/dtracetoolkit.html">
   DTraceToolkit
  </a>
  - A collection of useful documented DTrace scripts.
 </li>
 <li>
  <a href="https://github.com/brendangregg/dtrace-cloud-tools">
   dtrace-cloud-tools
  </a>
  - DTrace tools written for the SmartOS/SmartDataCenter cloud (illumos-based).
 </li>
 <li>
  <a href="https://github.com/joyent/pgsqlstat">
   pgsql tools
  </a>
  - Report top-level PostgreSQL stats.
 </li>
 <li>
  <a href="https://github.com/davepacheco/portsnoop">
   portsnoop
  </a>
  - Trace event port activity.
 </li>
 <li>
  <a href="https://github.com/richardelling/tools">
   storage tools
  </a>
  - Report NFS, CIFS and iSCSI stats.
 </li>
</ul>
<h2>
 Community
</h2>
<ul>
 <li>
  <a href="http://dtrace.org">
   Community site
  </a>
  - DTrace community site.
 </li>
 <li>
  <a href="http://dtrace.org/blogs/mailing-list/">
   Mailing list
  </a>
  - DTrace community mailing list.
 </li>
 <li>
  <a href="http://chinadtrace.org/">
   China DTrace
  </a>
  - A Chinese DTrace site.
 </li>
</ul>
<h2>
 Contributing
</h2>
<p>
 Contributions are more than welcome! Please see
 <a href="https://github.com/xen0l/awesome-dtrace/blob/master/CONTRIBUTING.md">
  contribution guidelines
 </a>
 first.
</p>
