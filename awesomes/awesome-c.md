<h1>
 awesome-c
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<p>
 A curated list of C good stuff. This list contains
 <em>
  only
 </em>
 <a href="https://en.wikipedia.org/wiki/Free_software">
  free software
 </a>
 for code, and sellers who aren't evil for physical resources.
</p>
<p>
 This is released under the GNU Free Documentation License - its text is provided in the LICENSE file.
</p>
<p>
 This list was previously maintained by
 <a href="https://github.com/kozross">
  @kozross
 </a>
 . He decided to switch the list to a
 <a href="https://notabug.org/koz.ross/awesome-c">
  new platform
 </a>
 , so I've decided to fork it so we could keep it on GitHub.
</p>
<p>
 Your contributions are highly welcome.
</p>
<p>
 For more awesome lists, see
 <a href="https://github.com/sindresorhus/awesome">
  awesome
 </a>
 .
</p>
<h1>
 Contents
</h1>
<h2>
 Contents
</h2>
<ul>
 <li>
  <a href="#build-systems">
   Build Systems
  </a>
 </li>
 <li>
  <a href="#compilers">
   Compilers
  </a>
 </li>
 <li>
  <a href="#crypto">
   Crypto
  </a>
 </li>
 <li>
  <a href="#database">
   Database
  </a>
 </li>
 <li>
  <a href="#deep-learning">
   Deep Learning
  </a>
 </li>
 <li>
  <a href="#documentation-generation">
   Documentation Generation
  </a>
 </li>
 <li>
  <a href="#editors">
   Editors
  </a>
 </li>
 <li>
  <a href="#environments">
   Environments
  </a>
 </li>
 <li>
  <a href="#frameworks">
   Frameworks
  </a>
 </li>
 <li>
  <a href="#game-programming">
   Game Programming
  </a>
  <ul>
   <li>
    <a href="#engines">
     Engines
    </a>
   </li>
   <li>
    <a href="#resources">
     Resources
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#generic-programming">
   Generic Programming
  </a>
 </li>
 <li>
  <a href="#graphics">
   Graphics
  </a>
 </li>
 <li>
  <a href="#graphical-user-interface">
   Graphical User Interface
  </a>
 </li>
 <li>
  <a href="#image-processing">
   Image Processing
  </a>
 </li>
 <li>
  <a href="#json">
   JSON
  </a>
 </li>
 <li>
  <a href="#learning-reference-and-tutorials">
   Learning, Reference and Tutorials
  </a>
  <ul>
   <li>
    <a href="#online">
     Online
    </a>
    <ul>
     <li>
      <a href="#reference">
       Reference
      </a>
     </li>
     <li>
      <a href="#beginner">
       Beginner
      </a>
     </li>
     <li>
      <a href="#intermediate">
       Intermediate
      </a>
     </li>
     <li>
      <a href="#advanced">
       Advanced
      </a>
     </li>
     <li>
      <a href="#self-study-courses">
       Self-study courses
      </a>
     </li>
    </ul>
   </li>
   <li>
    <a href="#physical">
     Physical
    </a>
    <ul>
     <li>
      <a href="#reference-1">
       Reference
      </a>
     </li>
     <li>
      <a href="#beginner-1">
       Beginner
      </a>
     </li>
     <li>
      <a href="#intermediate-1">
       Intermediate
      </a>
     </li>
     <li>
      <a href="#advanced-1">
       Advanced
      </a>
     </li>
    </ul>
   </li>
  </ul>
 </li>
 <li>
  <a href="#multimedia">
   Multimedia
  </a>
 </li>
 <li>
  <a href="#networking-and-internet">
   Networking and Internet
  </a>
  <ul>
   <li>
    <a href="#web-frameworks">
     Web Frameworks
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#numerical">
   Numerical
  </a>
 </li>
 <li>
  <a href="#parallel-programming">
   Parallel Programming
  </a>
 </li>
 <li>
  <a href="#regex">
   Regex
  </a>
 </li>
 <li>
  <a href="#serialization">
   Serialization
  </a>
 </li>
 <li>
  <a href="#source-code-collections">
   Source Code Collections
  </a>
 </li>
 <li>
  <a href="#standard-libraries">
   Standard Libraries
  </a>
 </li>
 <li>
  <a href="#string-manipulation">
   String Manipulation
  </a>
 </li>
 <li>
  <a href="#testing">
   Testing
  </a>
 </li>
 <li>
  <a href="#text-editor-extensions">
   Text Editor Extensions
  </a>
  <ul>
   <li>
    <a href="#emacs">
     Emacs
    </a>
   </li>
   <li>
    <a href="#vim">
     Vim
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#tools">
   Tools
  </a>
 </li>
 <li>
  <a href="#utilities">
   Utilities
  </a>
 </li>
 <li>
  <a href="#xml">
   XML
  </a>
 </li>
</ul>
<h2>
 Build Systems
</h2>
<p>
 These are tools to automate the building and testing of projects in C.
</p>
<ul>
 <li>
  <a href="http://nethack4.org/projects/aimake/">
   aimake
  </a>
  - A build tool designed to avoid complex configurations.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later.
 </li>
 <li>
  <a href="https://www.gnu.org/software/autoconf/">
   Autoconf
  </a>
  - An extensible package of M4 macros that produce shell scripts to automatically configure software source code packages. Part of the Autotools.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later.
 </li>
 <li>
  <a href="https://www.gnu.org/software/automake/automake.html">
   Automake
  </a>
  - A tool for automatically generating
  <code>
   Makefile.in
  </code>
  files compliant with the GNU Coding Standards. Requires the use of Autoconf. Part of the Autotools.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later.
 </li>
 <li>
  <a href="https://www.perforce.com/resources/documentation/jam">
   Jam
  </a>
  - A build system, designed to be easier than make. Understands C build rules implicitly.
  <a href="https://en.wikipedia.org/wiki/Perforce_Jam#License">
   Jam License
  </a>
  .
 </li>
 <li>
  <a href="https://gnu.org/software/libtool/">
   Libtool
  </a>
  - A generic library support script. Part of the Autotools.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later.
 </li>
 <li>
  <a href="http://mesonbuild.com/">
   Meson
  </a>
  - An extremely fast, user-friendly build system. Based on Ninja.
  <a href="http://directory.fsf.org/wiki/License:Apache2.0">
   Apache2.0
  </a>
  .
 </li>
</ul>
<h2>
 Compilers
</h2>
<ul>
 <li>
  <a href="http://clang.llvm.org/">
   Clang
  </a>
  - A C compiler for LLVM. Supports C11.
  <a href="http://directory.fsf.org/wiki/License:IllinoisNCSA">
   NCSA
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/AbsInt/CompCert">
   CompCert
  </a>
  <span>
   &#9733 181, pushed 6 days ago
  </span>
  - A fully-verified C compiler. Supports almost all of C89.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  or later.
 </li>
 <li>
  <a href="https://gcc.gnu.org/">
   GCC
  </a>
  - Provides a C compiler as part of its compiler set. Supports C11 and OpenMP.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later.
 </li>
 <li>
  <a href="http://pcc.ludd.ltu.se/">
   PCC
  </a>
  - A venerable C compiler. Supports C99.
  <a href="http://pcc.ludd.ltu.se/licenses/">
   Various licenses
  </a>
  , all free.
 </li>
 <li>
  <a href="http://bellard.org/tcc/">
   TCC
  </a>
  - Tiny C Compiler; a small, fast C compiler. Supports C99 (except complex types).
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   GNU LGPL2.1
  </a>
  only.
 </li>
</ul>
<h2>
 Crypto
</h2>
<ul>
 <li>
  <a href="http://www.gnutls.org/">
   GnuTLS
  </a>
  - A secure communication library, implementing SSL, TLS and DTLS.
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   GNU LGPL2.1
  </a>
  or later.
 </li>
 <li>
  <a href="https://www.gnu.org/software/libgcrypt/">
   libgcrypt
  </a>
  - A general-purpose cryptography library, with a range of available ciphers.
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   GNU LGPL2.1
  </a>
  or later (code),
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  or later (manual and tools).
 </li>
 <li>
  <a href="https://www.openssl.org/">
   OpenSSL
  </a>
  - Implementation of the SSL and TLS protocols, and also includes a cryptography library.
  <a href="https://www.openssl.org/source/license.html">
   Dual Licensed under the OpenSSL License and the SSLeay License
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/jedisct1/libsodium">
   libsodium
  </a>
  <span>
   &#9733 2814, pushed 3 days ago
  </span>
  - A modern and easy-to-use crypto library.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/libtom/libtomcrypt">
   libtomcrypt
  </a>
  <span>
   &#9733 352, pushed 19 days ago
  </span>
  - A fairly comprehensive, modular and portable cryptographic toolkit. Public domain.
 </li>
 <li>
  <a href="https://tls.mbed.org/">
   mbed TLS
  </a>
  - Another crypto implementation for C.
  <a href="http://directory.fsf.org/wiki/License:Apache2.0">
   Apache2.0
  </a>
  .
 </li>
</ul>
<h2>
 Database
</h2>
<p>
 This lists databases and data stores with C APIs.
</p>
<ul>
 <li>
  <a href="http://www.oracle.com/us/products/database/berkeley-db/overview/index.html">
   BerkeleyDB
  </a>
  - A library for a high-performance embedded database for key-value data.
  <a href="https://gnu.org/licenses/agpl.html">
   GNU AGPLv3
  </a>
  only.
 </li>
 <li>
  <a href="https://github.com/redis/hiredis">
   Hiredis
  </a>
  <span>
   &#9733 1907, pushed 13 days ago
  </span>
  - A minimalistic client library for Redis.
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  .
 </li>
 <li>
  <a href="http://symas.com/mdb/">
   LMDB
  </a>
  - An ultra-fast, ultra-compact key-value embedded data store.
  <a href="http://directory.fsf.org/wiki/License:OpenLDAPv2.7">
   newOpenLDAP
  </a>
  .
 </li>
 <li>
  <a href="https://mariadb.com/">
   MariaDB
  </a>
  - A robust, scalable and reliable SQL server, designed to be a drop-in replacement for MySQL.
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/mongodb/mongo-c-driver">
   mongo-c-driver
  </a>
  <span>
   &#9733 224, pushed 5 days ago
  </span>
  - A high-performance client library for
  <a href="https://www.mongodb.org/">
   MongoDB
  </a>
  .
  <a href="http://directory.fsf.org/wiki/License:Apache2.0">
   Apache2.0
  </a>
  .
 </li>
 <li>
  <a href="http://www.postgresql.org/">
   PostgreSQL
  </a>
  - A powerful object-relational database system.
  <a href="https://opensource.org/licenses/postgresql">
   PostgreSQL licence
  </a>
  .
 </li>
 <li>
  <a href="https://www.gnu.org/software/recutils/">
   recutils
  </a>
  - A set of tools and a C library for accessing human-editable, plaintext database files called recfiles.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later.
 </li>
 <li>
  <a href="http://redis.io/">
   Redis
  </a>
  - An advanced key-value store.
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/pmwkaa/sophia">
   sophia
  </a>
  <span>
   &#9733 1265, pushed 5 days ago
  </span>
  - A modern, embeddable key-value database.
  <a href="http://directory.fsf.org/wiki?title=License:FreeBSD">
   FreeBSD
  </a>
  .
 </li>
 <li>
  <a href="http://www.sqlite.org/">
   SQLite
  </a>
  - A self-contained, serverless, zero-configuration, transactional SQL database engine with a C interface. Public domain.
 </li>
 <li>
  <a href="https://unqlite.org/">
   UnQLite
  </a>
  - A self-contained, serverless, zero-configuration, transactional NoSQL engine with a C interface.
  <a href="http://directory.fsf.org/wiki?title=License:FreeBSD">
   FreeBSD
  </a>
  .
 </li>
</ul>
<h2>
 Deep Learning
</h2>
<ul>
 <li>
  <a href="http://pjreddie.com/darknet/">
   Darknet
  </a>
  - An open source neural network framework written in C and CUDA. It is fast, easy to install, and supports CPU and GPU computation.
 </li>
</ul>
<h2>
 Documentation Generation
</h2>
<ul>
 <li>
  <a href="http://www.gedanken.org.uk/software/cxref/">
   Cxref
  </a>
  - Generates documentation of C programs in either LaTeX, HTML, RTF or SGML.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="https://hplgit.github.io/doconce/doc/web/index.html">
   DocOnce
  </a>
  - A modestly-tagged markup language that can be used to generate a range of formats.
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  .
 </li>
 <li>
  <a href="http://www.stack.nl/~dimitri/doxygen/index.html">
   Doxygen
  </a>
  - The de-facto standard tool for generating C documentation from annotated sources. Can generate a large range of formats.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="http://www.gtk.org/gtk-doc/">
   GTK-Doc
  </a>
  - A tool for generating C documentation from annotated sources. Has support for the Autotools.
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   GNU GPL2.1
  </a>
  only (code),
  <a href="https://www.gnu.org/licenses/old-licenses/fdl-1.1.html">
   GNU FDL1.1
  </a>
  only.
 </li>
</ul>
<h2>
 Editors
</h2>
<p>
 These are specifically fancier, IDE-type editors. If you want a programmer's text editor, look elsewhere. Besides, whatever choice you make most likely supports C anyway.
</p>
<ul>
 <li>
  <a href="http://anjuta.org/">
   Anjuta DevStudio
  </a>
  - The GNOME IDE.
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   GNU GPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="http://www.codeblocks.org/">
   Code::Blocks
  </a>
  - An extensible, configurable IDE supporting C.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  only.
 </li>
 <li>
  <a href="http://www.codelite.org/">
   CodeLite
  </a>
  - A cross-platform IDE.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="http://www.eclipse.org/ide/">
   Eclipse
  </a>
  - An IDE written in Java.
  <a href="http://directory.fsf.org/wiki/License:EPLv1.0">
   EPL
  </a>
  .
 </li>
 <li>
  <a href="http://www.geany.org/">
   Geany
  </a>
  - A very small and fast IDE.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  or later.
 </li>
 <li>
  <a href="https://www.kdevelop.org/">
   KDevelop
  </a>
  - The KDE IDE.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="https://www.qt.io/ide/">
   Qt Creator
  </a>
  - A cross-platform IDE written with C++ and Qt, part of the Qt SDK. Supports Clang Code Model.
  <a href="https://github.com/qtproject/qt-creator/blob/master/LICENSE.GPL3-EXCEPT">
   GNU GPL3 with Qt exception
  </a>
  only.
 </li>
</ul>
<h2>
 Environments
</h2>
<p>
 This is a list of technologies designed to bring Windows into the 21st century with respect to support for C.
</p>
<ul>
 <li>
  <a href="https://cygwin.com/">
   Cygwin
  </a>
  - Designed to emulate a POSIX-compatible environment extensively under Windows.
  <a href="https://cygwin.com/licensing.html">
   Various licenses, all free
  </a>
  .
 </li>
 <li>
  <a href="http://mingw-w64.yaxm.org/doku.php/start">
   MinGW-w64
  </a>
  - A minimalist environment for C development on Windows with 64 bit support.
  <a href="http://mingw.org/license">
   Various licenses, all free
  </a>
  .
 </li>
</ul>
<h2>
 Frameworks
</h2>
<p>
 This section has big libraries that provide data structures and other stuff you expect of a 'modern' standard library.
</p>
<ul>
 <li>
  <a href="http://apr.apache.org/">
   APR
  </a>
  - Apache Portable Runtime; another library of cross-platform utility functions.
  <a href="http://directory.fsf.org/wiki/License:Apache2.0">
   Apache2.0
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/fragglet/c-algorithms">
   C Algorithms
  </a>
  <span>
   &#9733 508, pushed 17 days ago
  </span>
  - A collection of common algorithms and data structures for C.
  <a href="http://directory.fsf.org/wiki/License:ISC">
   ISC
  </a>
  .
 </li>
 <li>
  <a href="http://www.eso.org/sci/software/cpl/">
   CPL
  </a>
  - The Common Pipeline Library; a set of libraries designed to be a comprehensive, efficient and robust software toolkit.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="https://www.enlightenment.org?p=about%252Fefl">
   EFL
  </a>
  - A large collection of useful data structures and functions. Various licenses, all free.
 </li>
 <li>
  <a href="https://wiki.gnome.org/Projects/GLib">
   GLib
  </a>
  - A library of utility functions and structures, designed to be portable, efficient and powerful.
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   GNU LGPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="https://developer.gnome.org/gio/">
   GIO
  </a>
  - A modern and easy-to-use VFS API.
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   GNU LGPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="https://developer.gnome.org/gobject/stable/">
   GObject
  </a>
  - An object-oriented system and object model for C.
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   GNU LGPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="https://github.com/keybuk/libnih">
   libnih
  </a>
  <span>
   &#9733 26, pushed 876 days ago
  </span>
  - A lightweight library of C functions and structures.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="http://www.koanlogic.com/libu/">
   libU
  </a>
  - A small library of basic utilities, including memory allocation, string manipulation and logging.
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  .
 </li>
 <li>
  <a href="http://www.mission-base.com/peter/source/">
   PBL
  </a>
  - A large library of utilities, featuring data structures, among other things.
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   GNU LGPL2.1
  </a>
  or later (library),
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  or later (test code).
 </li>
 <li>
  <a href="https://github.com/wolkykim/qlibc">
   qlibc
  </a>
  <span>
   &#9733 181, pushed 138 days ago
  </span>
  - A simple and powerful C library, designed as a replacement for GLib while focusing on being small and light.
  <a href="https://github.com/wolkykim/qlibc/blob/master/LICENSE">
   qLib license
  </a>
  (similar to
  <a href="http://directory.fsf.org/wiki?title=License:FreeBSD">
   FreeBSD
  </a>
  ).
 </li>
 <li>
  <a href="https://github.com/nothings/stb">
   stb
  </a>
  <span>
   &#9733 3498, pushed 4 days ago
  </span>
  - A range of single-file libraries for C. Public domain.
 </li>
</ul>
<h2>
 Game Programming
</h2>
<h3>
 Engines
</h3>
<p>
 These are provided as examples of C game programming code.
</p>
<ul>
 <li>
  <a href="https://github.com/orangeduck/Corange">
   Corange
  </a>
  <span>
   &#9733 436, pushed 3 days ago
  </span>
  - A game engine in pure C.
  <a href="http://directory.fsf.org/wiki?title=License:FreeBSD">
   FreeBSD
  </a>
  .
 </li>
 <li>
  <a href="https://icculus.org/twilight/darkplaces/">
   Darkplaces
  </a>
  - A modified version of the Quake2 engine.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="https://github.com/ioquake/ioq3">
   ioquake3
  </a>
  <span>
   &#9733 509, pushed 17 days ago
  </span>
  - The Quake3 engine, freed at last.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="https://bitbucket.org/orx/orx">
   Orx
  </a>
  - A portable, lightweight, plugin-based, data-driven, 2D-oriented game engine.
  <a href="http://directory.fsf.org/wiki/License:Zlib">
   zlib
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/id-Software/Quake">
   Quake
  </a>
  <span>
   &#9733 1167, pushed 1554 days ago
  </span>
  - The Quake engine.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="https://github.com/id-Software/Quake-2">
   Quake2
  </a>
  <span>
   &#9733 601, pushed 1554 days ago
  </span>
  - The Quake2 engine.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="https://github.com/zturtleman/spearmint">
   Spearmint
  </a>
  <span>
   &#9733 49, pushed 7 days ago
  </span>
  - An engine designed for FPS games.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later.
 </li>
</ul>
<h3>
 Resources
</h3>
<p>
 These are libraries of all sorts that are useful for game programming.
</p>
<ul>
 <li>
  <a href="http://liballeg.org">
   Allegro
  </a>
  - A cross-platform, video game development and multimedia library.
  <a href="http://directory.fsf.org/wiki/License:Zlib">
   zlib
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/slembcke/Chipmunk2D">
   Chipmunk2D
  </a>
  <span>
   &#9733 807, pushed 35 days ago
  </span>
  - A fast and lightweight 2D game physics library.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="http://www.sfml-dev.org/download/csfml/">
   CSFML
  </a>
  - A binding for
  <a href="http://www.sfml-dev.org/index.php">
   SFML
  </a>
  in C.
  <a href="http://directory.fsf.org/wiki/License:Zlib">
   zlib
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/dcnieho/FreeGLUT">
   FreeGLUT
  </a>
  <span>
   &#9733 118, pushed 72 days ago
  </span>
  - An alternative to the OpenGL Utility Toolkit. Allows the creation and management of windows with OpenGL contexts.
  <a href="http://directory.fsf.org/wiki/License:X11">
   X11
  </a>
  .
 </li>
 <li>
  <a href="http://www.glfw.org/">
   GLFW
  </a>
  - A multi-platform library for creating windows with OpenGL contexts.
  <a href="http://directory.fsf.org/wiki/License:Zlib">
   zlib
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/timonwong/libao">
   libao
  </a>
  <span>
   &#9733 3, pushed 1045 days ago
  </span>
  - A cross-platform audio library with a wide variety of outputs.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  or later.
 </li>
 <li>
  <a href="https://github.com/libretro/RetroArch">
   RetroArch
  </a>
  <span>
   &#9733 1082, pushed 1 days ago
  </span>
  - The reference frontend for
  <a href="http://www.libretro.com/">
   libretro
  </a>
  .
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  only.
 </li>
 <li>
  <a href="https://www.libsdl.org/">
   SDL
  </a>
  - A cross-platform library designed to provide low-level access to audio, keyboard, mouse, joystick and graphics hardware via OpenGL.
  <a href="http://directory.fsf.org/wiki/License:Zlib">
   zlib
  </a>
  .
 </li>
 <li>
  <a href="https://www.libsdl.org/">
   SDL2
  </a>
  - A a cross-platform development library designed to provide low level access to audio, keyboard, mouse, joystick, and graphics hardware via OpenGL. This is the most current version.
  <a href="http://directory.fsf.org/wiki/License:Zlib">
   zlib
  </a>
 </li>
</ul>
<h2>
 Generic Programming
</h2>
<ul>
 <li>
  <a href="https://github.com/attractivechaos/klib">
   klib
  </a>
  <span>
   &#9733 1364, pushed 72 days ago
  </span>
  - Small and lightweight implementations of common algorithms and data structures.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
</ul>
<h2>
 Graphics
</h2>
<ul>
 <li>
  <a href="http://cairographics.org/">
   Cairo
  </a>
  - A 2D graphics library.
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   GNU LGPL2.1
  </a>
  only or
  <a href="https://directory.fsf.org/wiki/License:MPLv1.1">
   MPLv1.1
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/rib/cogl-web/wiki">
   Cogl
  </a>
  - A GPU graphics and utilities API.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  (dependent on
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  and possibly
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   LGPLv2.1
  </a>
  only libs).
 </li>
 <li>
  <a href="https://blogs.gnome.org/clutter/get-it/">
   Clutter
  </a>
  - A UI library based on OpenGL.
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   GNU LGPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="https://github.com/prideout/heman">
   heman
  </a>
  <span>
   &#9733 259, pushed 161 days ago
  </span>
  - A tiny library of image utilities dealing with height maps, normal maps, distance fields and the like.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/cacalabs/libcaca">
   libcaca
  </a>
  <span>
   &#9733 51, pushed 36 days ago
  </span>
  - An ASCII renderer for terminal-based interfaces.
  <a href="http://www.wtfpl.net/txt/copying/">
   WTFPLv2
  </a>
  .
 </li>
 <li>
  <a href="https://pngquant.org/lib/">
   libimagequant
  </a>
  - Small, portable library for high-quality conversion of RGBA images to 8-bit indexed colour images.
  <a href="http://directory.fsf.org/wiki?title=License:FreeBSD">
   FreeBSD
  </a>
  .
 </li>
 <li>
  <a href="http://libjpeg-turbo.virtualgl.org/">
   libjpeg-turbo
  </a>
  - A faster library for reading and writing JPEG files.
  <a href="http://www.libjpeg-turbo.org/About/License">
   Various licences
  </a>
  .
 </li>
 <li>
  <a href="http://www.libpng.org">
   libpng
  </a>
  - The official PNG reference library.
  <a href="http://www.libpng.org/pub/png/src/libpng-LICENSE.txt">
   libpng license
  </a>
  .
 </li>
 <li>
  <a href="https://gnu.org/software/libxmi/">
   libxmi
  </a>
  - A function library for rasterizing 2D vector graphics.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later.
 </li>
 <li>
  <a href="https://github.com/mozilla/mozjpeg">
   mozjpeg
  </a>
  <span>
   &#9733 1949, pushed 37 days ago
  </span>
  - An improved JPEG encoder.
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  .
 </li>
 <li>
  <a href="https://www.opengl.org/">
   OpenGL
  </a>
  - The industry standard for high-performance graphics, with a native C binding.
  <a href="http://www.sgi.com/tech/opengl/?/license.html">
   Various licenses
  </a>
  .
 </li>
</ul>
<h2>
 Graphical User Interface
</h2>
<p>
 These are specifically
 <a href="https://en.wikipedia.org/wiki/Widget_toolkit">
  widget toolkits
 </a>
 .
</p>
<ul>
 <li>
  <a href="http://www.gtk.org/">
   GTK+
  </a>
  - A cross-platform widget toolkit.
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   GNU LGPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="http://webserver2.tecgraf.puc-rio.br/iup/">
   IUP
  </a>
  - Another cross-platform widget toolkit.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="http://www.tcl.tk/">
   Tk
  </a>
  - A basic widget toolkit. Part of Tcl/Tk.
  <a href="http://www.tcl.tk/software/tcltk/license.html">
   Tcl/Tk License
  </a>
  .
 </li>
 <li>
  <a href="http://xforms-toolkit.org/">
   XForms Toolkit
  </a>
  - A widget toolkit designed for the XWindow system.
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   GNU LGPL2.1
  </a>
  only.
 </li>
</ul>
<h2>
 Image Processing
</h2>
<ul>
 <li>
  <a href="http://libccv.org">
   libccv
  </a>
  - A Modern Computer Vision Library.
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  .
 </li>
</ul>
<h2>
 JSON
</h2>
<ul>
 <li>
  <a href="http://www.digip.org/jansson/">
   Jansson
  </a>
  - A C library for encoding, decoding and manipulating JSON.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="http://zserge.com/jsmn.html">
   jsmn
  </a>
  - A minimalistic JSON parser.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/json-c/json-c/wiki">
   json-c
  </a>
  - A library for working with JSON.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/netmail-open/wjelement/">
   WJElement
  </a>
  - Advanced JSON manipulation library, with support for JSON Schema. LGPL, any version.
 </li>
 <li>
  <a href="https://lloyd.github.io/yajl/">
   YAJL
  </a>
  - A fast C JSON streaming parser library.
  <a href="http://directory.fsf.org/wiki/License:ISC">
   ISC
  </a>
 </li>
</ul>
<h2>
 Learning, Reference and Tutorials
</h2>
<p>
 This is a list of resources for learning C programming in general, or something useful relating to C programming.
</p>
<h3>
 Online
</h3>
<h4>
 Reference
</h4>
<ul>
 <li>
  <a href="https://www.securecoding.cert.org/confluence/display/c/SEI+CERT+C+Coding+Standard">
   SEI CERT C Coding Standard
  </a>
 </li>
 <li>
  <a href="http://c-faq.com/">
   C FAQ - comp.lang.c Frequently Asked Questions
  </a>
 </li>
 <li>
  <a href="http://www.etalabs.net/compare_libcs.html">
   Comparison of C/POSIX standard library implementations for GNU/Linux
  </a>
 </li>
 <li>
  <a href="http://www.open-std.org/JTC1/SC22/WG14/">
   Draft C11 standard
  </a>
 </li>
 <li>
  <a href="https://www.gnu.org/software/gnu-c-manual/">
   GNU C Reference Manual
  </a>
 </li>
 <li>
  <a href="http://kamalatta.ddnss.de/otherdocs/pikestyle.html">
   Robert Pike's notes on programming in C
  </a>
 </li>
</ul>
<h4>
 Beginner
</h4>
<ul>
 <li>
  <a href="http://home.netcom.com/~tjensen/ptr/pointers.htm">
   A tutorial on pointers
  </a>
 </li>
 <li>
  <a href="http://nethack4.org/blog/building-c.html">
   Building C Projects
  </a>
 </li>
 <li>
  <a href="https://en.wikibooks.org/wiki/C_Programming">
   C Programming Wikibook
  </a>
 </li>
 <li>
  <a href="https://gist.github.com/eatonphil/21b3d6569f24ad164365">
   Introduction to 'fun' C
  </a>
 </li>
 <li>
  <a href="https://www.recurse.com/blog/5-learning-c-with-gdb">
   Learning C with GDB
  </a>
 </li>
 <li>
  <a href="https://computing.llnl.gov/tutorials/pthreads/">
   POSIX Threads Programming tutorial
  </a>
  (a little dated, but most of it is still valid and useful)
 </li>
 <li>
  <a href="http://www.crasseux.com/books/ctut.pdf">
   The GNU C Programming Tutorial
  </a>
  (online PDF)
 </li>
 <li>
  <a href="http://blog.pkh.me/p/20-templating-in-c.html">
   Templating in C
  </a>
 </li>
</ul>
<h4>
 Intermediate
</h4>
<ul>
 <li>
  <a href="https://blogs.oracle.com/ksplice/entry/8_gdb_tricks_you_should">
   8 gdb tricks you should know
  </a>
 </li>
 <li>
  <a href="http://blog.noctua-software.com/c-tricks.html">
   10 C99 tricks
  </a>
 </li>
 <li>
  <a href="http://jvns.ca/blog/2014/12/14/fun-with-threads/">
   Diving into concurrency: trying out mutexes and atomics
  </a>
 </li>
 <li>
  <a href="https://www.youtube.com/playlist?list=PLLX-Q6B8xqZ8n8bwjGdzBJ25X2utwnoEG">
   Introduction to OpenMP
  </a>
  (video)
 </li>
 <li>
  <a href="https://computing.llnl.gov/tutorials/openMP/">
   OpenMP tutorial
  </a>
  (for the OpenMP3 standard)
 </li>
 <li>
  <a href="http://www.tedunangst.com/flak/post/memcpy-vs-memmove">
   memcpy vs memmove
  </a>
 </li>
 <li>
  <a href="https://computing.llnl.gov/tutorials/mpi/">
   MPI tutorial
  </a>
 </li>
 <li>
  <a href="http://proprogramming.org/some-unknown-features-or-tricks-in-c-language/">
   Some unknown features or tricks in C language
  </a>
 </li>
 <li>
  <a href="http://www.catb.org/esr/structure-packing/">
   The lost art of C structure packing
  </a>
 </li>
 <li>
  <a href="http://marek.vavrusa.com/c/memory/2015/02/20/memory/">
   What a C programmer should know about memory
  </a>
 </li>
 <li>
  <a href="http://blog.llvm.org/2011/05/what-every-c-programmer-should-know.html">
   What every C programmer should know about undefined behaviour
  </a>
 </li>
</ul>
<h4>
 Advanced
</h4>
<ul>
 <li>
  <a href="http://250bpm.com/blog:56">
   Advanced metaprogramming in C
  </a>
 </li>
 <li>
  <a href="http://danluu.com/malloc-tutorial/">
   A quick tutorial on implementing and debugging malloc, free, calloc, and realloc
  </a>
 </li>
 <li>
  <a href="https://graphics.stanford.edu/~seander/bithacks.html">
   Bit twiddling hacks
  </a>
 </li>
 <li>
  <a href="http://kukuruku.co/hub/programming/i-do-not-know-c">
   I do not know C
  </a>
 </li>
 <li>
  <a href="https://snai.pe/c/c-smart-pointers/">
   Implementing smart pointers for the C programming language
  </a>
 </li>
 <li>
  <a href="http://www.greenend.org.uk/rjk/tech/inline.html">
   Inline functions in C
  </a>
 </li>
 <li>
  <a href="http://www.chiark.greenend.org.uk/~sgtatham/mp/">
   Metaprogramming custom control structures in C
  </a>
 </li>
 <li>
  <a href="http://www.samnip.ps/thought/macro-storage-for-inverse-comma">
   Solving the temporary storage problem of C macros
  </a>
 </li>
 <li>
  <a href="https://docs.google.com/presentation/d/1h49gY3TSiayLMXYmRMaAEMl05FaJ-Z6jDOWOz3EsqqQ/edit?pli=1#slide=id.gaf50702c_0153">
   Some dark corners of C
  </a>
 </li>
 <li>
  <a href="http://www.codeproject.com/Articles/6154/Writing-Efficient-C-and-C-Code-Optimization">
   Writing efficient C and C code optimization
  </a>
 </li>
</ul>
<h4>
 Self-study courses
</h4>
<ul>
 <li>
  <a href="http://cppinstitute.com/study-resources">
   C Programming Language Certified Associate preparation course
  </a>
 </li>
</ul>
<h3>
 Physical
</h3>
<h4>
 Reference
</h4>
<ul>
 <li>
  <a href="http://careferencemanual.com/">
   C: A Reference Manual 5E
  </a>
  - A full reference book for C99.
 </li>
 <li>
  <a href="http://shop.oreilly.com/product/9780596004361.do">
   C Pocket Reference
  </a>
  - A concise reference book for C99.
 </li>
 <li>
  <a href="https://en.wikipedia.org/wiki/The_C_Programming_Language">
   The C Programming Language 2E
  </a>
  - The original book on C, by its creators.
 </li>
</ul>
<h4>
 Beginner
</h4>
<ul>
 <li>
  <a href="https://www.pearsonhighered.com/program/Prata-C-Primer-Plus-6th-Edition/PGM4399.html">
   C Primer Plus 6E
  </a>
  - A complete tutorial on programming in C11.
 </li>
 <li>
  <a href="http://knking.com/books/c2/index.html">
   C Programming: A Modern Approach
  </a>
  - An excellent book to learn the basics from C from.
 </li>
 <li>
  <a href="http://shop.oreilly.com/product/0636920015482.do">
   Head First C
  </a>
  - A 'head-first' style book for learning C.
 </li>
</ul>
<h4>
 Intermediate
</h4>
<ul>
 <li>
  <a href="http://shop.oreilly.com/product/0636920033677.do">
   21st Century C
  </a>
  - A very good
  <em>
   second
  </em>
  programming book on C.
 </li>
 <li>
  <a href="http://shop.oreilly.com/product/0636920028000.do">
   Understanding and Using C Pointers
  </a>
  - An in-depth resource on pointers in C.
 </li>
 <li>
  <a href="http://shop.oreilly.com/product/0636920026136.do">
   ZeroMQ
  </a>
  - A book for using ZeroMQ with C.
 </li>
</ul>
<h4>
 Advanced
</h4>
<ul>
 <li>
  <a href="http://dl.acm.org/citation.cfm?id=179241">
   Expert C Programming: Deep C Secrets
  </a>
  - An interesting, in-depth and
  <em>
   entertaining
  </em>
  look at the innards of C.
 </li>
</ul>
<h2>
 Multimedia
</h2>
<ul>
 <li>
  <a href="https://www.ffmpeg.org/">
   FFMPEG
  </a>
  - A complete, cross-platform solution to record, convert and stream audio and video.
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   GNU LGPL2.1
  </a>
  or later, with some parts under
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  or later.
 </li>
 <li>
  <a href="https://gstreamer.freedesktop.org/">
   GStreamer
  </a>
  - A framework for audio and visual media.
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   GNU LGPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="http://lodev.org/lodepng/">
   lodepng
  </a>
  - A simple PNG image decoder and encoder, requiring no other dependencies.
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  .
 </li>
</ul>
<h2>
 Networking and Internet
</h2>
<ul>
 <li>
  <a href="http://lionet.info/asn1c/compiler.html">
   asnlc
  </a>
  - A compiler of ASN.1 specifications into C source code.
  <a href="http://directory.fsf.org/wiki?title=License:FreeBSD">
   FreeBSD
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/zeromq/czmq">
   czmq
  </a>
  <span>
   &#9733 466, pushed 4 days ago
  </span>
  - A high-level binding for ZeroMQ.
  <a href="https://www.gnu.org/licenses/license-list.html#MPL-2.0">
   MPL2.0
  </a>
 </li>
 <li>
  <a href="https://gnu.org/software/adns/">
   GNU adns
  </a>
  - An advanced, easy-to-use, asynch-capable DNS client library and utilities.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later.
 </li>
 <li>
  <a href="https://gnu.org/software/gsasl/">
   GNU SASL
  </a>
  - An implementation of the Simple Authentication and Security Layer and a few common SASL mechanism.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later.
 </li>
 <li>
  <a href="http://www.gnutls.org/">
   GnuTLS
  </a>
  - A secure communication library, implementing SSL, TLS and DTLS.
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   GNU LGPL2.1
  </a>
  or later.
 </li>
 <li>
  <a href="https://github.com/google/gumbo-parser">
   gumbo-parser
  </a>
  <span>
   &#9733 3650, pushed 152 days ago
  </span>
  - An HTML5 parsing library in C99.
  <a href="http://directory.fsf.org/wiki/License:Apache2.0">
   Apache2.0
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/nodejs/http-parser">
   http-parser
  </a>
  <span>
   &#9733 2639, pushed 8 days ago
  </span>
  - An HTTP request/response parser.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="http://www.nlnetlabs.nl/projects/ldns/index.html">
   ldns
  </a>
  - A library to simplify DNS programming.
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  .
 </li>
 <li>
  <a href="https://curl.haxx.se/libcurl/">
   libcurl
  </a>
  - A client-side URL transfer library, supporting a wide range of formats.
  <a href="https://curl.haxx.se/docs/copyright.html">
   curl license
  </a>
 </li>
 <li>
  <a href="https://github.com/dinhviethoa/libetpan">
   LibEtPan
  </a>
  <span>
   &#9733 381, pushed 2 days ago
  </span>
  - A mail library providing an efficient network for IMAP, SMTP, POP and NNTP.
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  .
 </li>
 <li>
  <a href="http://software.schmorp.de/pkg/libev.html">
   libev
  </a>
  - Yet another event loop.
  <a href="http://directory.fsf.org/wiki?title=License:FreeBSD">
   FreeBSD
  </a>
  .
 </li>
 <li>
  <a href="http://libevent.org/">
   libevent
  </a>
  - An event loop replacement for network servers.
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  .
 </li>
 <li>
  <a href="https://gnu.org/software/gss/">
   libgss
  </a>
  - Generic Security Service.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later.
 </li>
 <li>
  <a href="http://www.hughes.com.au/products/libhttpd/">
   libhttpd
  </a>
  - A library to add basic web server capabilities to an application or embedded device.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL2
  </a>
  only.
 </li>
 <li>
  <a href="https://gnu.org/software/libidn/">
   libidn
  </a>
  - An implementation of the Stringprep, Punycode and IDNA specifications.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later.
 </li>
 <li>
  <a href="https://gnu.org/software/libmicrohttpd/">
   libmicrohttpd
  </a>
  - A small C library that makes it easy to run an HTTP server as part of another application.
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   GNU LGPL2.1
  </a>
  or later.
 </li>
 <li>
  <a href="https://wiki.gnome.org/action/show/Projects/libsoup?action=show&redirect=LibSoup">
   libsoup
  </a>
  - A GNOME HTTP client/server library. Uses GObject.
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   GNU LGPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="https://github.com/lpereira/lwan">
   lwan
  </a>
  <span>
   &#9733 3389, pushed 1 days ago
  </span>
  - An experimental, scalable, high-performance HTTP server.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="https://github.com/cesanta/mongoose">
   mongoose
  </a>
  <span>
   &#9733 2638, pushed 4 days ago
  </span>
  - Embedded web server for C.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="https://github.com/nanomsg/nanomsg">
   nanomsg
  </a>
  <span>
   &#9733 2742, pushed 2 days ago
  </span>
  - A C-based implementation of ZeroMQ.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/davidmoreno/onion">
   onion
  </a>
  <span>
   &#9733 1013, pushed 1 days ago
  </span>
  - HTTP server library, designed to be easy to use.
  <a href="http://directory.fsf.org/wiki/License:Apache2.0">
   Apache2.0
  </a>
  .
 </li>
 <li>
  <a href="https://www.openssl.org/">
   OpenSSL
  </a>
  - Implementation of the SSL and TLS protocols, and also includes a cryptography library.
  <a href="https://www.openssl.org/source/license.html">
   Dual Licensed under the OpenSSL License and the SSLeay License
  </a>
 </li>
 <li>
  <a href="https://gnu.org/software/osip/">
   oSip
  </a>
  - A SIP implementation in C without additional dependencies.
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   GNU LGPLv2.1
  </a>
  or later.
 </li>
 <li>
  <a href="https://github.com/rafael-santiago/pig">
   pig
  </a>
  <span>
   &#9733 236, pushed 2 days ago
  </span>
  - A Linux packet crafting tool.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GPL2
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/awslabs/s2n">
   s2n
  </a>
  <span>
   &#9733 2275, pushed 13 days ago
  </span>
  - A C99 implementation of the TLS/SSL protocols, designed to be simple, fast and with security as a priority.
  <a href="http://directory.fsf.org/wiki/License:Apache2.0">
   Apache2.0
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/silentbicycle/socket99">
   socket99
  </a>
  <span>
   &#9733 71, pushed 196 days ago
  </span>
  - A C99 wrapper for the BSD sockets API.
  <a href="http://directory.fsf.org/wiki/License:ISC">
   ISC
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/irungentoo/toxcore">
   Tox
  </a>
  <span>
   &#9733 7849, pushed 1 days ago
  </span>
  - A communication platform, designed to be a Skype-killer.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  only.
 </li>
 <li>
  <a href="https://github.com/sinemetu1/twitc">
   twitc
  </a>
  <span>
   &#9733 17, pushed 466 days ago
  </span>
  - A mini C library for interacting with the Twitter OAuth API.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
</ul>
<h3>
 Web Frameworks
</h3>
<ul>
 <li>
  <a href="https://github.com/balde/balde">
   balde
  </a>
  <span>
   &#9733 42, pushed 135 days ago
  </span>
  - A microframework for C based on GLib.
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   GNU LGPLv2.1
  </a>
  only.
 </li>
</ul>
<h2>
 Numerical
</h2>
<ul>
 <li>
  <a href="https://github.com/b-k/apophenia">
   apophenia
  </a>
  <span>
   &#9733 90, pushed 7 days ago
  </span>
  - A library for statistical and scientific computing.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="http://math-atlas.sourceforge.net/">
   ATLAS
  </a>
  - Automatically Tuned Linear Algebra Software.
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  .
 </li>
 <li>
  <a href="http://www.netlib.org/blas/">
   BLAS
  </a>
  - Basic Linear Algebra Subprograms; a set of routines that provide vector and matrix operations.
  <a href="http://www.netlib.org/blas/#_licensing">
   BLAS license
  </a>
 </li>
 <li>
  <a href="http://www.feynarts.de/cuba/">
   Cuba
  </a>
  - A library for multidimensional numerical integration.
  <a href="http://www.gnu.org/licenses/lgpl.html">
   GNU LGPLv3
  </a>
  only.
 </li>
 <li>
  <a href="http://www.fftw.org/">
   FFTW
  </a>
  - The Fastest Fourier Transform in the West; a highly-optimized fast Fourier transform routine.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  or later.
 </li>
 <li>
  <a href="http://flintlib.org/">
   FLINT
  </a>
  - Fast Library for Number Theory; a library supporting arithmetic with numbers, polynomials, power series and matrices, among others.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  or later.
 </li>
 <li>
  <a href="https://gnu.org/software/glpk/">
   GLPK
  </a>
  - GNU Linear Programming Kit; a package designed for solving large-scale linear programming, mixed integer programming and other related problems.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later.
 </li>
 <li>
  <a href="https://gmplib.org/">
   GMP
  </a>
  - GNU Multple Precision Arithmetic Library; a library for arbitrary-precision arithmetic. Dual-licensed
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  only and
  <a href="http://www.gnu.org/licenses/lgpl.html">
   GNU LGPLv3
  </a>
  only.
 </li>
 <li>
  <a href="http://www.multiprecision.org/index.php?prog=mpc&page=home">
   GNU MPC
  </a>
  - A library for complex number arithmetic.
  <a href="http://www.gnu.org/licenses/lgpl.html">
   GNU LGPL3
  </a>
  or later.
 </li>
 <li>
  <a href="http://mpfr.loria.fr/index.html">
   GNU MPFR
  </a>
  - A library for arbitrary-precision floating-point arithmetic.
  <a href="http://www.gnu.org/licenses/lgpl.html">
   GNU LGPL3
  </a>
  or later (most recent versions),
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   GNU LGPL2.1
  </a>
  or later (until version 2.4.x).
 </li>
 <li>
  <a href="https://gnu.org/software/mpria/">
   GNU MPRIA
  </a>
  - A portable mathematics library for multi-precision rational interval arithmetic.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later.
 </li>
 <li>
  <a href="http://www.gnu.org/software/gsl/">
   GSL
  </a>
  - The GNU Scientific Library; a sophisticated numerical library.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  only.
 </li>
 <li>
  <a href="https://sourceforge.net/projects/kissfft/">
   KISS FFT
  </a>
  - A very simple fast Fourier transform library.
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  .
 </li>
 <li>
  <a href="http://www.netlib.org/lapack/lapacke.html">
   LAPACKE
  </a>
  - A C interface to
  <a href="http://www.netlib.org/lapack/">
   LAPACK
  </a>
  .
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  .
 </li>
 <li>
  <a href="http://pari.math.u-bordeaux.fr/">
   PARI/GP
  </a>
  - A computer algebra system for number theory; includes a compiler to C.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  or later.
 </li>
 <li>
  <a href="http://www.mcs.anl.gov/petsc/">
   PETSc
  </a>
  - A suite of data structures and routines for scalable parallel solution of scientific applications modelled by partial differential equations.
  <a href="http://directory.fsf.org/wiki?title=License:FreeBSD">
   FreeBSD
  </a>
  .
 </li>
 <li>
  <a href="http://slepc.upv.es/">
   SLEPc
  </a>
  - A software library for the solution of large, sparse eigenvalue problems on parallel computers.
  <a href="http://www.gnu.org/licenses/lgpl.html">
   GNU LGPL3
  </a>
  only.
 </li>
 <li>
  <a href="http://www.yeppp.info/">
   Yeppp!
  </a>
  - Very fast, SIMD-optimized mathematical library.
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  .
 </li>
</ul>
<h2>
 Parallel Programming
</h2>
<ul>
 <li>
  <a href="http://repo.hu/projects/cchan/">
   cchan
  </a>
  - A small library for channel constructs for inter-thread communication. Public domain.
 </li>
 <li>
  <a href="https://github.com/concurrencykit/ck">
   ck
  </a>
  <span>
   &#9733 887, pushed 46 days ago
  </span>
  - Concurrency primitives, safe memory reclamation mechanisms and non-blocking data structures.
  <a href="http://directory.fsf.org/wiki?title=License:FreeBSD">
   FreeBSD
  </a>
  .
 </li>
 <li>
  <a href="http://libmill.org/">
   mill
  </a>
  - Go-style concurrency in C.
  <a href="https://directory.fsf.org/wiki/License:X11">
   X11
  </a>
  .
 </li>
 <li>
  <a href="http://www.mpich.org/">
   MPICH
  </a>
  - Another implementation of MPI.
  <a href="http://git.mpich.org/mpich.git/blob_plain/6aab201f58d71fc97f2c044d250389ba86ac1e3c:/COPYRIGHT">
   MPICH licence
  </a>
  .
 </li>
 <li>
  <a href="http://openmp.org/wp/about-openmp/">
   OpenMP
  </a>
  - A set of C pragmas designed to allow for easy parallelization of code. Standard (licensing not applicable).
 </li>
 <li>
  <a href="https://github.com/open-mpi/ompi">
   OpenMPI
  </a>
  <span>
   &#9733 171, pushed 1 days ago
  </span>
  - A message passing interface implementation.
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  .
 </li>
 <li>
  <a href="http://www.mcs.anl.gov/petsc/">
   PETSc
  </a>
  - A suite of data structures and routines for scalable parallel solution of scientific applications modelled by partial differential equations.
  <a href="http://directory.fsf.org/wiki?title=License:FreeBSD">
   FreeBSD
  </a>
  .
 </li>
 <li>
  <a href="https://gnu.org/software/pth/">
   pth
  </a>
  - A portable implementation for non-preemptive priority-based scheduling for multiple threads of execution.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later.
 </li>
 <li>
  <a href="https://en.wikipedia.org/wiki/POSIX_Threads">
   pthreads
  </a>
  - The POSIX thread library. Standard (no license applicable).
 </li>
 <li>
  <a href="http://slepc.upv.es/">
   SLEPc
  </a>
  - A software library for the solution of large, sparse eigenvalue problems on parallel computers.
  <a href="http://www.gnu.org/licenses/lgpl.html">
   GNU LGPL3
  </a>
  only.
 </li>
 <li>
  <a href="https://tinycthread.github.io/">
   TinyCThread
  </a>
  - A portable, small implementation of the C11 threads API.
  <a href="http://directory.fsf.org/wiki/License:Zlib">
   zlib
  </a>
  .
 </li>
</ul>
<h2>
 Regex
</h2>
<blockquote>
 <p>
  "Some people, when confronted with a problem, think 'I know, I'll use regular expressions'. Now they have two problems." - Jamie Zawinski.
 </p>
</blockquote>
<ul>
 <li>
  <a href="http://www.pcre.org/">
   PCRE
  </a>
  - An implementation of regexes identical to that of Perl 5.
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/cesanta/slre">
   SLRE
  </a>
  <span>
   &#9733 269, pushed 40 days ago
  </span>
  - Super Light Regular Expression library; a very small implementation of a subset of Perl regex syntax.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="https://github.com/laurikari/tre/">
   TRE
  </a>
  - A POSIX-compliant, feature-full regex library.
  <a href="http://directory.fsf.org/wiki?title=License:FreeBSD">
   FreeBSD
  </a>
  .
 </li>
</ul>
<h2>
 Serialization
</h2>
<ul>
 <li>
  <a href="https://github.com/jmckaskill/c-capnproto">
   c-capnproto
  </a>
  <span>
   &#9733 51, pushed 6 days ago
  </span>
  - An implementation of the Cap'n Proto serialization protocol.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/camgunz/cmp">
   cmp
  </a>
  <span>
   &#9733 102, pushed 21 days ago
  </span>
  - An implementation of the
  <a href="http://msgpack.org/">
   MessagePack
  </a>
  serialization protocol.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="http://avro.apache.org/docs/current/api/c/index.html#_introduction_to_avro_c">
   libavro
  </a>
  - A C implementation of the Avro data serialization system.
  <a href="http://directory.fsf.org/wiki/License:Apache2.0">
   Apache2.0
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/ludocode/mpack">
   mpack
  </a>
  <span>
   &#9733 34, pushed 2 days ago
  </span>
  - Another implementation of the
  <a href="http://msgpack.org/">
   MessagePack
  </a>
  serialization protocol.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/protobuf-c/protobuf-c">
   protobuf-c
  </a>
  <span>
   &#9733 461, pushed 1 days ago
  </span>
  - An implementation of Google Protocol Buffer in C.
  <a href="http://directory.fsf.org/wiki?title=License:FreeBSD">
   FreeBSD
  </a>
  .
 </li>
 <li>
  <a href="https://en.wikipedia.org/wiki/External_Data_Representation">
   xdr
  </a>
  - External Data Representation; a standard for data serialization. Standard (no license applicable).
 </li>
</ul>
<h2>
 Source Code Collections
</h2>
<p>
 This contains collections of small source code. If you want something big and integrated, check the Frameworks section.
</p>
<ul>
 <li>
  <a href="http://ccodearchive.net/">
   CCAN
  </a>
  - Modelled after Perl's CPAN, this is a big collection of C code that does stuff. The full list is
  <a href="http://ccodearchive.net/list.html">
   here
  </a>
  . Various licenses (all free software).
 </li>
 <li>
  <a href="https://github.com/clibs/clib">
   clib
  </a>
  <span>
   &#9733 2051, pushed 29 days ago
  </span>
  - Something of a package manager for C. Comes with a
  <a href="https://github.com/clibs/clib/wiki/Packages">
   bunch of libraries of its own
  </a>
  .
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="https://www.gnu.org/software/gnulib/">
   gnulib
  </a>
  - A collection of common GNU code. Various licenses, all free.
 </li>
 <li>
  <a href="http://www.fefe.de/djb/">
   libdjb
  </a>
  - A collection of libraries doing various things. (Apparently) public domain.
 </li>
</ul>
<h2>
 Standard Libraries
</h2>
<p>
 This contains standard C libraries.
</p>
<ul>
 <li>
  <a href="https://github.com/android/platform_bionic">
   Bionic
  </a>
  <span>
   &#9733 252, pushed 1 days ago
  </span>
  - Google's C standard library, developed for Android.
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  .
 </li>
 <li>
  <a href="http://www.fefe.de/dietlibc/">
   dietlibc
  </a>
  - A C standard library designed for the smallest possible binaries.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="http://www.gnu.org/software/libc/">
   glibc
  </a>
  - The GNU C Library; an implementation of the C standard library.
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   GNU LGPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="http://www.musl-libc.org/">
   musl
  </a>
  - A standard C library, compatible with POSIX 2008 and C11. Designed for static linking.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
</ul>
<h2>
 String Manipulation
</h2>
<ul>
 <li>
  <a href="http://bstring.sourceforge.net/">
   bstrlib
  </a>
  - The Better String Library. Dual-licensed under
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  or
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="http://site.icu-project.org/">
   ICU
  </a>
  - International Components for Unicode; a library for Unicode support.
  <a href="http://source.icu-project.org/repos/icu/icu/trunk/license.html">
   ICU license
  </a>
  .
 </li>
 <li>
  <a href="https://gnu.org/software/libunistring/">
   libunistring
  </a>
  - A library for manipulating Unicode strings in C.
  <a href="http://www.gnu.org/licenses/lgpl.html">
   GNU LGPL3
  </a>
  only.
 </li>
 <li>
  <a href="https://gnu.org/software/libiconv/">
   libgiconv
  </a>
  - A text conversion library.
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   GNU LGPL2.1
  </a>
  only (library),
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  only (
  <em>
   iconv
  </em>
  program).
 </li>
 <li>
  <a href="https://github.com/antirez/sds">
   SDS
  </a>
  <span>
   &#9733 1563, pushed 45 days ago
  </span>
  - Simple Dynamic Strings; a library for handling C strings in a simpler way, but one that is compatible with normal C string functions. Available via
  <a href="https://github.com/clibs/clib">
   clib
  </a>
  .
  <a href="http://directory.fsf.org/wiki?title=License:FreeBSD">
   FreeBSD
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/Ed-von-Schleck/shoco">
   shoco
  </a>
  <span>
   &#9733 104, pushed 58 days ago
  </span>
  - A compressor for small text strings.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/antirez/smaz">
   smaz
  </a>
  <span>
   &#9733 446, pushed 94 days ago
  </span>
  - An efficient string compression library.
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  .
 </li>
</ul>
<h2>
 Testing
</h2>
<ul>
 <li>
  <a href="https://github.com/Tuplanolla/cheat">
   CHEAT
  </a>
  <span>
   &#9733 120, pushed 372 days ago
  </span>
  - A very simple unit testing framework.
  <a href="http://directory.fsf.org/wiki?title=License:FreeBSD">
   FreeBSD
  </a>
  .
 </li>
 <li>
  <a href="http://check.sourceforge.net/">
   Check
  </a>
  - A unit testing framework for C.
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   GNU LGPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="https://github.com/ThrowTheSwitch/CMock">
   CMock
  </a>
  <span>
   &#9733 84, pushed 12 days ago
  </span>
  - A mock/stub generator for C.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="https://cmocka.org/">
   cmocka
  </a>
  - A unit testing framework with support for mock objects.
  <a href="http://directory.fsf.org/wiki/License:Apache2.0">
   Apache2.0
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/Snaipe/Criterion">
   Criterion
  </a>
  <span>
   &#9733 277, pushed 6 days ago
  </span>
  - A KISS, non-intrusive C test framework.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="http://cunit.sourceforge.net/">
   CUnit
  </a>
  - Another unit testing framework for C.
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   GNU LGPL2.0
  </a>
  only.
 </li>
 <li>
  <a href="https://github.com/rafael-santiago/cutest">
   Cutest
  </a>
  <span>
   &#9733 14, pushed 210 days ago
  </span>
  - Library for unit testing with memory leak detection (Linux, freeBSD and Windows).
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GPL2
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/siu/minunit">
   minunit
  </a>
  <span>
   &#9733 101, pushed 9 days ago
  </span>
  - Minimal unit testing framework for C.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/ThrowTheSwitch/Unity">
   Unity
  </a>
  <span>
   &#9733 340, pushed 5 days ago
  </span>
  - A simple unit testing framework for C.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
</ul>
<h2>
 Text Editor Extensions
</h2>
<p>
 While practically any decent programmer's text editor supports C, there are some extensions that make it more pleasant. This is categorized by editor.
</p>
<h3>
 Emacs
</h3>
<ul>
 <li>
  <a href="http://cedet.sourceforge.net/">
   CEDET
  </a>
  - Collection of Emacs Development Environment Tools; designed to provide IDE-like features to Emacs. Built-in.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later.
 </li>
 <li>
  <a href="https://github.com/flycheck/flycheck">
   Flycheck
  </a>
  <span>
   &#9733 989, pushed 3 days ago
  </span>
  - Modern syntax checking. For C, it can use either GCC or Clang as a back-end.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later.
 </li>
 <li>
  <a href="https://github.com/capitaomorte/yasnippet">
   Yasnippet
  </a>
  <span>
   &#9733 1223, pushed 1 days ago
  </span>
  - A template system, with C templates for common code snippets.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later.
 </li>
</ul>
<h3>
 Vim
</h3>
<ul>
 <li>
  <a href="https://github.com/scrooloose/syntastic">
   Syntastic
  </a>
  <span>
   &#9733 6546, pushed 1 days ago
  </span>
  - Syntax checking and linting.
  <a href="https://github.com/scrooloose/syntastic/blob/master/LICENCE">
   Do What The Fuck You Want To license
  </a>
  .
 </li>
 <li>
  <a href="http://valloric.github.io/YouCompleteMe/">
   YouCompleteMe
  </a>
  - A code completion engine for Vim.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  only.
 </li>
</ul>
<h2>
 Tools
</h2>
<p>
 This is a list of useful programs to help you write and debug C code which are
 <em>
  not
 </em>
 editors, libraries or compilers.
</p>
<ul>
 <li>
  <a href="http://astyle.sourceforge.net/">
   Artistic Style
  </a>
  - A fast and small automatic source code formatter that supports C.
  <a href="http://www.gnu.org/licenses/lgpl.html">
   GNU LGPL3
  </a>
  only.
 </li>
 <li>
  <a href="https://github.com/google/sanitizers">
   address-sanitizer
  </a>
  <span>
   &#9733 547, pushed 20 days ago
  </span>
  - A fast memory error detector.
  <a href="http://directory.fsf.org/wiki/License:Apache2.0">
   Apache2.0
  </a>
  .
 </li>
 <li>
  <a href="https://biicode.github.io/biicode/">
   biicode
  </a>
  - A modern dependency manager for C.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/ryanmjacobs/c">
   c
  </a>
  <span>
   &#9733 1345, pushed 85 days ago
  </span>
  - Compile and execute C "scripts" in one go on the command line. Also has shebang support.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/RhysU/c99sh">
   c99sh
  </a>
  <span>
   &#9733 28, pushed 226 days ago
  </span>
  - Run C files using hash-bang.
  <a href="http://directory.fsf.org/wiki?title=License:FreeBSD">
   FreeBSD
  </a>
  .
 </li>
 <li>
  <a href="http://www.cprover.org/cbmc/">
   CBMC
  </a>
  - C Bounded Model Checker; a tool for verification of array bounds, pointer safety and user-specified assertions.
  <a href="https://directory.fsf.org/wiki/License:BSD_4Clause">
   Original BSD
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/mpv-player/mpv">
   cdecl
  </a>
  <span>
   &#9733 3378, pushed 2 days ago
  </span>
  - An online service to translate C declarations into English and vice versa. Public domain.
 </li>
 <li>
  <a href="https://www.flourish.org/cinclude2dot/">
   cinclude2dot
  </a>
  - Graphs include dependencies in a C project using Graphviz. Any GNU GPL version (due to underspecification in the file).
 </li>
 <li>
  <a href="https://www.gnu.org/software/complexity/">
   Complexity
  </a>
  - A tool for measuring the complexity of C source code.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later.
 </li>
 <li>
  <a href="https://www.gnu.org/software/ddd/ddd.html">
   DDD
  </a>
  - A graphical front-end for a range of command-line debuggers.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later.
 </li>
 <li>
  <a href="http://www.gnu.org/software/gdb/">
   GDB
  </a>
  - The GNU Project debugger; a debugger for C.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later.
 </li>
 <li>
  <a href="https://glade.gnome.org/">
   Glade
  </a>
  - A RAD tool to enable quick development of GTK+ GUIs.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="http://gmsl.sourceforge.net/">
   GMSL
  </a>
  - GNU Make Standard Library; a collection of additional functionality for GNU Make.
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  .
 </li>
 <li>
  <a href="https://www.gnu.org/software/global/">
   GNU Global
  </a>
  - A source code tagging tool which works with C.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  only.
 </li>
 <li>
  <a href="http://www.gnu.org/software/binutils/">
   gprof
  </a>
  - A performance analysis tool. Part of GNU binutils.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later.
 </li>
 <li>
  <a href="http://www.andre-simon.de/index.php">
   Highlight
  </a>
  - Converts source code to formatted text with nice highlighting.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  only.
 </li>
 <li>
  <a href="https://github.com/include-what-you-use/include-what-you-use">
   include-what-you-use
  </a>
  <span>
   &#9733 428, pushed 2 days ago
  </span>
  - Helps find unecessary inclusions and make suggestions for fixing them. Based on LLVM/Clang (and only works with it).
  <a href="http://directory.fsf.org/wiki/License:IllinoisNCSA">
   NCSA
  </a>
  .
 </li>
 <li>
  <a href="https://www.gnu.org/software/indent/">
   indent
  </a>
  - Formats C source code automatically to make it easier to read. Also converts from one style of source to another.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPLv3
  </a>
  or later.
 </li>
 <li>
  <a href="https://www.gnu.org/software/make/">
   Make
  </a>
  - A tool which controls the generation of executables and other non-source files of a program.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later (link to the GNU implementation).
 </li>
 <li>
  <a href="https://github.com/andlabs/qo">
   qo
  </a>
  <span>
   &#9733 229, pushed 160 days ago
  </span>
  - A build system that works without a separate config file.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="http://rr-project.org/">
   rr
  </a>
  - A debugger that records non-deterministic executions to allow for deterministic debugging.
  <a href="http://directory.fsf.org/wiki?title=License:FreeBSD">
   FreeBSD
  </a>
  .
 </li>
 <li>
  <a href="http://gittup.org/tup/index.html">
   tup
  </a>
  - A very fast, file-based, cross-platform build system.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="http://dotat.at/prog/unifdef/">
   unifdef
  </a>
  - Removes #ifdef and #if directives with their delimited text without touching any other part of the file.
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  and
  <a href="http://directory.fsf.org/wiki?title=License:FreeBSD">
   FreeBSD
  </a>
  .
 </li>
 <li>
  <a href="http://www.valgrind.org/">
   Valgrind
  </a>
  - A range of dynamic analysis tools, including a leak checker.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  only.
 </li>
</ul>
<h2>
 Utilities
</h2>
<p>
 This is a 'catch-all' category for anything that doesn't fit well anywhere else.
</p>
<ul>
 <li>
  <a href="https://github.com/jeremyevans/ape_tag_libs/tree/master/c">
   ApeTagLibs
  </a>
  - A C library for working with APEv2 tags.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="http://sourceware.org/binutils/docs/bfd/">
   bfd
  </a>
  - A library for manipulating binary object files. Part of GNU binutils.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later.
 </li>
 <li>
  <a href="https://github.com/liuliu/ccv">
   ccv
  </a>
  <span>
   &#9733 5192, pushed 1 days ago
  </span>
  - C-based/Cached/Core Computer Vision library; modern computer vision.
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  .
 </li>
 <li>
  <a href="https://fakenmc.github.io/cf4ocl/">
   cf4ocl
  </a>
  - The C Framework for OpenCL; a cross-platform object-oriented framework for developing and benchmarking
  <a href="https://www.khronos.org/opencl/">
   OpenCL
  </a>
  projects.
  <a href="http://www.gnu.org/licenses/lgpl.html">
   GNU LGPL3
  </a>
  only (library),
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  (other code).
 </li>
 <li>
  <a href="https://github.com/jgm/CommonMark">
   CommonMark
  </a>
  <span>
   &#9733 3053, pushed 28 days ago
  </span>
  - A C implementation of the CommonMark spec.
  <a href="https://github.com/jgm/CommonMark/blob/master/LICENSE">
   Variety of licenses, all free
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/ThrowTheSwitch/CException">
   CException
  </a>
  <span>
   &#9733 33, pushed 13 days ago
  </span>
  - A C implementation of exceptions.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/docopt/docopt.c">
   docopt.c
  </a>
  <span>
   &#9733 191, pushed 9 days ago
  </span>
  - A C implementation of a command-line option parser.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="http://www.dyncall.org/">
   dyncall
  </a>
  - Another foreign function interface library.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="http://leenissen.dk/fann/wp/">
   FANN
  </a>
  - Fast Artifical Neural Network library; an implementation of neural networks.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="http://pp.ipd.kit.edu/firm/Index">
   Firm
  </a>
  - A C library that provides a graph-based intermediate representation, optimizations and assembly code generation suitable for use in compilers. Comes with an example C front-end under the same license.
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   GNU LGPLv2.1
  </a>
  only.
 </li>
 <li>
  <a href="https://sourceforge.net/projects/gjrand/">
   gjrand
  </a>
  - A library of random-number generation routines.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  or
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPLv3
  </a>
  (user's choice).
 </li>
 <li>
  <a href="https://gnu.org/software/freeipmi/index.html">
   GNU FreeIPMI
  </a>
  - An in-band and out-of-band IPMI implementation.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  only.
 </li>
 <li>
  <a href="https://www.gnu.org/software/gperf/">
   GNU gperf
  </a>
  - A perfect hash function generator, given a list of strings. Outputs C code.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later.
 </li>
 <li>
  <a href="https://gnu.org/software/libffcall/">
   GNU Libffcall
  </a>
  - A collection of libraries for building foreign function interfaces.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later.
 </li>
 <li>
  <a href="https://github.com/gperftools/gperftools">
   gperftools
  </a>
  <span>
   &#9733 668, pushed 18 days ago
  </span>
  - A collection of utilities for measuring and improving performance.
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/abiggerhammer/hammer">
   hammer
  </a>
  <span>
   &#9733 140, pushed 68 days ago
  </span>
  - Parser combinators for binary formats.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="http://www.hboehm.info/gc/">
   Hans Boehm GC
  </a>
  - Garbage collection for C? Don't mind if I do! Various licenses, all free.
 </li>
 <li>
  <a href="https://github.com/adamierymenko/huffandpuff">
   huffandpuff
  </a>
  <span>
   &#9733 32, pushed 1054 days ago
  </span>
  - A minimal Huffman encoder and decoder. Public domain.
 </li>
 <li>
  <a href="https://github.com/ndevilla/iniparser">
   iniparser
  </a>
  <span>
   &#9733 203, pushed 6 days ago
  </span>
  - A parser for .ini files.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="http://www.canonware.com/jemalloc/">
   jemalloc
  </a>
  - A malloc implementation that emphasizes avoidance of fragmentation and scalable concurrency support.
  <a href="http://directory.fsf.org/wiki?title=License:FreeBSD">
   FreeBSD
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/watmough/jwHash">
   jwHash
  </a>
  <span>
   &#9733 184, pushed 349 days ago
  </span>
  - A fast hashtable implementation.
  <a href="http://directory.fsf.org/wiki/License:Apache2.0">
   Apache2.0
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/jtsiomb/kdtree">
   kdtree
  </a>
  <span>
   &#9733 58, pushed 167 days ago
  </span>
  - A simple library for working with KD-trees.
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  .
 </li>
 <li>
  <a href="http://kitsune-dsu.com/">
   Kitsune
  </a>
  - An efficient, general-purpose framework for dynamic software updating.
  <a href="http://www.gnu.org/licenses/lgpl.html">
   GNU LGPL3
  </a>
  or later.
 </li>
 <li>
  <a href="http://adtinfo.org/libavl.html/index.html">
   libavl
  </a>
  - A library containing a range of self-balancing binary trees.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later.
 </li>
 <li>
  <a href="https://github.com/mongodb/libbson">
   libbson
  </a>
  <span>
   &#9733 188, pushed 7 days ago
  </span>
  - A BSON utility library.
  <a href="http://directory.fsf.org/wiki/License:Apache2.0">
   Apache2.0
  </a>
  .
 </li>
 <li>
  <a href="http://libcello.org/">
   libCello
  </a>
  - A library introducing higher-level programming to C.
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  .
 </li>
 <li>
  <a href="http://libcox.net/">
   libcox
  </a>
  - A library which permits cross-platform system calls and standard utilities across different operating systems.
  <a href="http://directory.fsf.org/wiki?title=License:FreeBSD">
   FreeBSD
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/libffi/libffi">
   libffi
  </a>
  <span>
   &#9733 516, pushed 2 days ago
  </span>
  - A portable foreign-function interface library.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="https://libgit2.github.com/">
   libgit2
  </a>
  - Pure C implementation of Git.
  <a href="https://github.com/libgit2/libgit2/blob/master/COPYING">
   GNU GPL2 only, with a linking exception
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/libimobiledevice/libimobiledevice">
   libimobiledevice
  </a>
  <span>
   &#9733 926, pushed 4 days ago
  </span>
  - A cross-platform protocol library to communicate with iThings.
  <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">
   GNU LGPLv2.1
  </a>
  or later (library),
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  or later (tools).
 </li>
 <li>
  <a href="https://github.com/mpv-player/mpv">
   libmpv
  </a>
  <span>
   &#9733 3378, pushed 2 days ago
  </span>
  - A music-playing library. Compile with
  <code>
   ./waf configure --disable-cplayer --enable-libmpv-shared
  </code>
  to not have the music player.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  or later.
 </li>
 <li>
  <a href="https://github.com/nfc-tools/libnfc">
   libnfc
  </a>
  <span>
   &#9733 108, pushed 5 days ago
  </span>
  - A platform-independent Near-Field Communication library.
  <a href="http://www.gnu.org/licenses/lgpl.html">
   GNU LGPL3
  </a>
  only.
 </li>
 <li>
  <a href="http://facebook.github.io/libphenom/index.html">
   libPhenom
  </a>
  - An eventing framework for building high-scalability and high-performance systems.
  <a href="http://directory.fsf.org/wiki/License:Apache2.0">
   Apache2.0
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/andrewrk/libsoundio">
   libsoundio
  </a>
  <span>
   &#9733 404, pushed 2 days ago
  </span>
  - A library for cross-platform, real-time audio input and output. Has a range of back-ends.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/vstakhov/libucl">
   libucl
  </a>
  <span>
   &#9733 628, pushed 5 days ago
  </span>
  - A universal configuration library parser.
  <a href="http://directory.fsf.org/wiki?title=License:FreeBSD">
   FreeBSD
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/libuv/libuv">
   libuv
  </a>
  <span>
   &#9733 3793, pushed 4 days ago
  </span>
  - Cross-platform asynchronous I/O.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="http://www.pyyaml.org/wiki/LibYAML">
   libYAML
  </a>
  - A YAML 1.1 parser and emitter.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="http://www.oberhumer.com/opensource/lzo/">
   lzo
  </a>
  - A very fast data compression library.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/orangeduck/mpc">
   mpc
  </a>
  <span>
   &#9733 907, pushed 14 days ago
  </span>
  - A parser combinator library.
  <a href="http://directory.fsf.org/wiki?title=License:FreeBSD">
   FreeBSD
  </a>
  .
 </li>
 <li>
  <a href="https://gnu.org/software/ncurses/">
   ncurses
  </a>
  - Coloured terminal UI library.
  <a href="http://www.gnu.org/licenses/gpl.html">
   GNU GPL3
  </a>
  or later.
 </li>
 <li>
  <a href="https://github.com/riolet/WAFer">
   nope.c
  </a>
  <span>
   &#9733 497, pushed 114 days ago
  </span>
  - A C-language-based, ultra-light software platform for scalable server-side and networking applications (think node.js for C programmers).
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="https://github.com/cloudwu/pbc">
   pbc
  </a>
  <span>
   &#9733 697, pushed 41 days ago
  </span>
  - A protocol buffers library.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/alanxz/rabbitmq-c">
   rabbitmq-c
  </a>
  <span>
   &#9733 487, pushed 11 days ago
  </span>
  - A client library for
  <a href="http://www.rabbitmq.com/">
   RabbitMQ
  </a>
  .
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="http://www.colm.net/open-source/ragel/">
   Ragel
  </a>
  - A DSL for state machines that compiles to C.
  <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">
   GNU GPL2.1
  </a>
  only.
 </li>
 <li>
  <a href="http://troydhanson.github.io/uthash/">
   uthash
  </a>
  - A hash table implementation, allowing existing structures to be stored in a hash table easily.
  <a href="http://troydhanson.github.io/uthash/license.html">
   1-clause BSD
  </a>
 </li>
 <li>
  <a href="https://github.com/eatonphil/Viola">
   Viola
  </a>
  <span>
   &#9733 32, pushed 474 days ago
  </span>
  - A simplification of libCello.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/madler/zlib">
   zlib
  </a>
  <span>
   &#9733 545, pushed 23 days ago
  </span>
  - A massively-spiffy yet delicately-unobtrusive compression library.
  <a href="http://directory.fsf.org/wiki/License:BSD_3Clause">
   3-clause BSD
  </a>
  .
 </li>
</ul>
<h2>
 XML
</h2>
<blockquote>
 <p>
  "XML is crap. Really. There are no excuses. XML is nasty to parse for humans, and it's a disaster to parse even for computers. There's just no reason for that horrible crap to exist." - Linus Torvalds
 </p>
</blockquote>
<ul>
 <li>
  <a href="http://www.libexpat.org/">
   Expat
  </a>
  - A stream-oriented XML parser.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="http://xmlsoft.org/">
   libxml2
  </a>
  - A standards-compliant, portable XML parser.
  <a href="http://directory.fsf.org/wiki/License:Expat">
   Expat
  </a>
  .
 </li>
 <li>
  <a href="http://www.msweet.org/projects.php?Z3">
   mini-xml
  </a>
  - A small XML reading and writing library. No dependencies aside from C standard library.
  <a href="http://svn.msweet.org/mxml/trunk/COPYING">
   GNU LGPL2.1 with static linking exception
  </a>
  .
 </li>
</ul>
