<h1>
 Awesome Fortran
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<p>
 A curated list of awesome Fortran frameworks, libraries and software. Inspired by
 <a href="https://github.com/Wolg/awesome-swift">
  awesome-swift
 </a>
 by @Wolg.
</p>
<ul>
 <li>
  <a href="#awesome-fortran">
   Awesome Fortran
  </a>
  <ul>
   <li>
    <a href="#graphics-libraries">
     Graphics Libraries
    </a>
   </li>
   <li>
    <a href="#math-libs">
     Math libs
    </a>
   </li>
   <li>
    <a href="#json-manipulation">
     JSON Manipulation
    </a>
   </li>
   <li>
    <a href="#xml-manipulation">
     XML Manipulation
    </a>
   </li>
   <li>
    <a href="#date-and-time-manipulation">
     Date and time manipulation
    </a>
   </li>
   <li>
    <a href="#testing">
     Testing
    </a>
   </li>
   <li>
    <a href="#encoding-decoding">
     Encoding-Decoding
    </a>
   </li>
   <li>
    <a href="#portability-enabling">
     Portability enabling
    </a>
   </li>
   <li>
    <a href="#command-line-parsing">
     Command-Line parsing
    </a>
   </li>
   <li>
    <a href="#compiling-and-building">
     Compiling and building
    </a>
   </li>
   <li>
    <a href="#preprocessor">
     Preprocessor
    </a>
   </li>
   <li>
    <a href="#automatic-documentation">
     Automatic documentation
    </a>
   </li>
   <li>
    <a href="#computational-fluid-dynamics">
     Computational Fluid Dynamics
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#resources">
   Resources
  </a>
  <ul>
   <li>
    <a href="#fortran-websites">
     Fortran Websites
    </a>
   </li>
   <li>
    <a href="#fortran-videos">
     Fortran Videos
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#other-awesome-lists">
   Other Awesome Lists
  </a>
 </li>
 <li>
  <a href="#contributing">
   Contributing
  </a>
 </li>
</ul>
<h2>
 Graphics Libraries
</h2>
<p>
 <em>
  Libraries for graphing, graphics, and GUIs
 </em>
</p>
<ul>
 <li>
  <a href="http://www.mps.mpg.de/dislin/">
   DISLIN
  </a>
  - a high-level graphing and user-interface library.
 </li>
 <li>
  <a href="http://math.nist.gov/f90gl/">
   f90gl
  </a>
  - public domain implementation of the official NIST Fortran 90 bindings for OpenGL.
 </li>
 <li>
  <a href="http://www-stone.ch.cam.ac.uk/pub/f03gl/index.xhtml">
   F03GL
  </a>
  - a Fortran 2003 interface to the OpenGL library, along with the GLU and GLUT toolkits.
 </li>
 <li>
  <a href="https://github.com/jerryd/gtk-fortran/wiki">
   gtk-fortran
  </a>
  - a cross-platform library to build Graphical User Interfaces (GUI) using
  <a href="http://www.gtk.org/">
   GTK+
  </a>
  .  Very useful when combined with the
  <a href="https://glade.gnome.org/">
   Glade
  </a>
  RAD tool.
 </li>
 <li>
  <a href="http://www.astro.caltech.edu/~tjp/pgplot/">
   PGPLOT
  </a>
  - cross-platform scientific graphing library.
 </li>
 <li>
  <a href="https://github.com/szaghi/Lib_VTK_IO">
   Lib
   <em>
    VTK
   </em>
   IO
  </a>
  - Pure Fortran (2003+) library to write and read data conforming the VTK standard.
  <sup>
   14 GitHub links in total 56 links, ★ 19, pushed 33 days ago
  </sup>
  <sup>
   &#9733 19, pushed 33 days ago
  </sup>
 </li>
</ul>
<h2>
 Math Libs
</h2>
<p>
 <em>
  Libraries for calculating and other mathematical operations.
 </em>
</p>
<ul>
 <li>
  <a href="http://www.netlib.org/blas/">
   BLAS
  </a>
  - application programming interface standard for publishing libraries to perform basic linear algebra operations such as vector and matrix multiplication.
 </li>
 <li>
  <a href="http://cernlib.web.cern.ch/cernlib/">
   CERNLIB
  </a>
  - The CERN Program Library is a large collection of general purpose libraries and modules maintained and offered in both source and object code form on the CERN central computers
 </li>
 <li>
  <a href="http://www.netlib.org/eispack/">
   EISPACK
  </a>
  - a software library for numerical computation of eigenvalues and eigenvectors of matrices, written in FORTRAN
 </li>
 <li>
  <a href="http://www.lrz.de/services/software/mathematik/gsl/fortran/index.html">
   FGSL
  </a>
  - portable, object-based Fortran interface to the
  <a href="http://www.lrz.de/services/software/mathematik/gsl/">
   GNU scientific library
  </a>
 </li>
 <li>
  <a href="http://www.roguewave.com/products-services/imsl-numerical-libraries/fortran-libraries">
   IMSL
  </a>
  - The IMSL Fortran Numerical Library is the standard for high performance computing commercial mathematics and statistics libraries
 </li>
 <li>
  <a href="http://www.ssisc.org/lis/index.en.html#download">
   Lis
  </a>
  - a Library of Iterative Solvers for Linear Systems
 </li>
 <li>
  <a href="http://www.nag.co.uk/numeric/fl/FLdescription.asp">
   NAG Fortran Library
  </a>
  - Produced by experts for use in a variety of applications, the NAG Fortran Library has a global reputation for its excellence and, with hundreds of fully documented and tested routines, is the largest collection of mathematical and statistical algorithms available
 </li>
 <li>
  <a href="https://github.com/Unidata/netcdf-fortran">
   netCDF
  </a>
  - a set of software libraries and self-describing, machine-independent data formats that support the creation, access, and sharing of array-oriented scientific data.
  <sup>
   14 GitHub links in total 56 links, ★ 37, pushed 4 days ago
  </sup>
  <sup>
   &#9733 37, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/xianyi/OpenBLAS">
   OpenBLAS
  </a>
  - one of the fastest open source BLAS libraries available.  Almost as fast as Intel MKL.
  <sup>
   14 GitHub links in total 56 links, ★ 896, pushed 4 days ago
  </sup>
  <sup>
   &#9733 896, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="http://paw.web.cern.ch/paw/">
   PAW
  </a>
  - conceived as an instrument to assist physicists in the analysis and presentation of their data
 </li>
</ul>
<h2>
 JSON Manipulation
</h2>
<p>
 <em>
  Libraries for JSON data manipulating with Fortran language.
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/josephalevin/fson">
   FSON
  </a>
  - Fortran 95 JSON Parser.
  <sup>
   14 GitHub links in total 56 links, ★ 27, pushed 27 days ago
  </sup>
  <sup>
   &#9733 27, pushed 27 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jacobwilliams/json-fortran">
   json-fortran
  </a>
  - A Fortran 2008 JSON API.
  <sup>
   14 GitHub links in total 56 links, ★ 40, pushed 1 days ago
  </sup>
  <sup>
   &#9733 40, pushed 1 days ago
  </sup>
 </li>
</ul>
<h2>
 XML Manipulation
</h2>
<p>
 <em>
  Libraries for XML data manipulating with Fortran language.
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/andreww/fox">
   fox
  </a>
  - Fortran XML library
  <sup>
   14 GitHub links in total 56 links, ★ 27, pushed 126 days ago
  </sup>
  <sup>
   &#9733 27, pushed 126 days ago
  </sup>
 </li>
 <li>
  <a href="http://sourceforge.net/projects/xml-fortran/">
   xml-fortran
  </a>
  - an all-Fortran solution for reading and writing XML files.
 </li>
</ul>
<h2>
 Date and time manipulation
</h2>
<p>
 <em>
  Libraries for date and time manipulation with Fortran language.
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/milancurcic/datetime-fortran">
   datetime-fortran
  </a>
  - A Fortran 2003 date and time manipulation library, modeled after Python's datetime library.
  <sup>
   14 GitHub links in total 56 links, ★ 24, pushed 12 days ago
  </sup>
  <sup>
   &#9733 24, pushed 12 days ago
  </sup>
 </li>
</ul>
<h2>
 Testing
</h2>
<p>
 <em>
  Libraries for testing codebases and generating test data.
 </em>
</p>
<ul>
 <li>
  <a href="http://sourceforge.net/projects/fortranxunit/">
   FRUIT
  </a>
  - FORTRAN Unit Test Framework, written in FORTRAN 95
 </li>
 <li>
  <a href="http://flibs.sourceforge.net/ftnunit.html">
   Ftunit
  </a>
  - Fortran unit testing framework by Arjen Markus
 </li>
 <li>
  <a href="http://sourceforge.net/projects/pfunit/">
   pFUnit
  </a>
  - Unit testing framework for Fortran with MPI extensions by developers from NASA and NGC TASC.  Uses parallel codes and object-oriented design.
 </li>
</ul>
<h2>
 Encoding-Decoding
</h2>
<p>
 <em>
  Libraries for encoding and decoding data with Fortran language.
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/szaghi/BeFoR64">
   BeFoR64
  </a>
  - Base64 encoding/decoding library for FoRtran poor men. A KISS library for base64 encoding/decoding for modern (2003+) Fortran projects.
  <sup>
   14 GitHub links in total 56 links, ★ 8, pushed 34 days ago
  </sup>
  <sup>
   &#9733 8, pushed 34 days ago
  </sup>
 </li>
</ul>
<h2>
 Portability enabling
</h2>
<p>
 <em>
  Libraries for enabling codes portability.
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/szaghi/IR_Precision">
   IR_Precision
  </a>
  - Pure Fortran (2003+) library for ensuring codes portability.
 </li>
</ul>
<h2>
 Command-Line parsing
</h2>
<p>
 <em>
  Libraries for parsing command-line and building user interfaces.
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/szaghi/FLAP">
   FLAP
  </a>
  - Fortran command Line Arguments Parser for poor men. A KISS library for building easily nice Command Line Interfaces (CLI) for modern (2003+) Fortran projects.
  <sup>
   14 GitHub links in total 56 links, ★ 17, pushed 25 days ago
  </sup>
  <sup>
   &#9733 17, pushed 25 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/cngilbreth/optionsf90">
   options.f90
  </a>
  - Options & input processing for modern Fortran.
  <sup>
   14 GitHub links in total 56 links, ★ 3, pushed 408 days ago
  </sup>
  <sup>
   &#9733 3, pushed 408 days ago
  </sup>
 </li>
</ul>
<h2>
 Compiling and building
</h2>
<p>
 <em>
  Libraries for compiling and building Fortran projects.
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/szaghi/FoBiS">
   FoBiS
  </a>
  - Fortran Building System for poor men. A KISS tool for automatic building modern Fortran projects.
  <sup>
   14 GitHub links in total 56 links, ★ 32, pushed 53 days ago
  </sup>
  <sup>
   &#9733 32, pushed 53 days ago
  </sup>
 </li>
</ul>
<h2>
 Preprocessor
</h2>
<p>
 <em>
  Libraries for conditional-compilation, macros for code simplification, and inclusion of additional source files, templating systems.
 </em>
</p>
<ul>
 <li>
  <a href="http://blockit.sourceforge.net/">
   Blockit/PyF95++
  </a>
  - A fairly simple Python framework used to block parse your code (or any text file) into nested blocks. The BlockIt framework has already been used to create a templating capability for the Fortran 95/2003 language along with some language extensions.
 </li>
 <li>
  <a href="https://github.com/szaghi/PreForM">
   PreForM
  </a>
  - Preprocessor for Fortran poor Men.
  <sup>
   14 GitHub links in total 56 links, ★ 9, pushed 350 days ago
  </sup>
  <sup>
   &#9733 9, pushed 350 days ago
  </sup>
 </li>
</ul>
<h2>
 Automatic documentation
</h2>
<p>
 <em>
  Libraries for building documentation.
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/cmacmackin/ford">
   FORD
  </a>
  - An automatic documentation generator for modern Fortran programs.
  <sup>
   14 GitHub links in total 56 links, ★ 49, pushed 6 days ago
  </sup>
  <sup>
   &#9733 49, pushed 6 days ago
  </sup>
 </li>
</ul>
<h2>
 Computational Fluid Dynamics
</h2>
<p>
 <em>
  Libraries for CFD computations
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/szaghi/OFF/tree/testing">
   OFF
  </a>
  - Open source Finite volume Fluid dynamics code.
 </li>
</ul>
<h1>
 Resources
</h1>
<p>
 Various resources, such as books, websites and articles, for improving your Fortran development skills and knowledge.
</p>
<h2>
 Fortran Websites
</h2>
<ul>
 <li>
  <a href="http://www.fortran.com/">
   The Fortran Company
  </a>
  - A home page of FORTRAN programming language.
 </li>
 <li>
  <a href="https://fortrandev.wordpress.com/">
   Fortran Dev
  </a>
  - Fortran development blog.
 </li>
 <li>
  <a href="http://fortranwiki.org/fortran/show/HomePage">
   Fortran WIKI
  </a>
  - An open venue for discussing all aspects of the Fortran programming language and scientific computing.
 </li>
</ul>
<h2>
 Fortran Videos
</h2>
<ul>
 <li>
  <a href="https://www.youtube.com/watch?v=qUy8M10uZRU">
   GNU FORTRAN Lesson 1
  </a>
  - Videos about the Fortran programming language.
 </li>
</ul>
<h1>
 Other Awesome Lists
</h1>
<p>
 Other amazingly awesome lists can be found in the
 <a href="https://github.com/bayandin/awesome-awesomeness">
  awesome-awesomeness
 </a>
 list.
</p>
<h1>
 Contributing
</h1>
<p>
 Your contributions are always welcome! Please submit a pull request or create an issue to add a new framework, library or software to the list. Do not submit a project, which hasn't been updated in the past 6 months or is not awesome.
</p>
