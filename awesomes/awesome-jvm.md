<h1>
 Awesome JVM
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<p>
 A curated list of awesome JVM low level and performance related stuff.
</p>
<ul>
 <li>
  <a href="#awesome-jvm">
   Awesome JVM
  </a>
  <ul>
   <li>
    <a href="#bytecode">
     Bytecode
    </a>
   </li>
   <li>
    <a href="#garbage-collectors">
     Garbage collectors
    </a>
   </li>
   <li>
    <a href="#load-tools">
     Load tools
    </a>
   </li>
   <li>
    <a href="#languages">
     Languages
    </a>
   </li>
   <li>
    <a href="#memory-and-concurrency">
     Memory and Concurrency
    </a>
   </li>
   <li>
    <a href="#metaprogramming">
     Metaprogramming
    </a>
   </li>
   <li>
    <a href="#native">
     Native
    </a>
   </li>
   <li>
    <a href="#network">
     Network
    </a>
   </li>
   <li>
    <a href="#nix-tools">
     Nix tools
    </a>
   </li>
   <li>
    <a href="#profilers">
     Profilers
    </a>
   </li>
   <li>
    <a href="#runtimes">
     Runtimes
    </a>
   </li>
   <li>
    <a href="#virtual-machines">
     Virtual Machines
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
    <a href="#communities">
     Communities
    </a>
   </li>
   <li>
    <a href="#documentation">
     Documentation
    </a>
   </li>
   <li>
    <a href="#media">
     Media
    </a>
   </li>
   <li>
    <a href="#people">
     People
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#contributing">
   Contributing
  </a>
 </li>
</ul>
<h2>
 Bytecode
</h2>
<p>
 <em>
  Tools for bytecode manipulation and analysis.
 </em>
</p>
<ul>
 <li>
  <a href="https://wiki.openjdk.java.net/display/CodeTools/asmtools">
   asmtools
  </a>
  - Used to develop tools for the production of Java .class files.
 </li>
 <li>
  <a href="http://bytebuddy.net">
   Byte Buddy
  </a>
  - Code generation library creating Java classes at runtime without the help of a compiler.
 </li>
 <li>
  <a href="https://github.com/qmx/jitescript">
   Jitescript
  </a>
  - Bytecode generation library similar to BiteScript.
  <sup>
   69 GitHub links in total 132 links, ★ 127, pushed 312 days ago
  </sup>
  <sup>
   &#9733 127, pushed 312 days ago
  </sup>
 </li>
</ul>
<h2>
 Garbage collectors
</h2>
<p>
 <em>
  Garbage collectors for the JVM.
 </em>
</p>
<ul>
 <li>
  <a href="http://www.azulsystems.com/sites/default/files//images/wp_pgc_zing_v5.pdf">
   Azul Pauseless Garbage Collection
  </a>
  - Providing continuous, pauseless operation for Java applications.
 </li>
 <li>
  <a href="http://www.oracle.com/technetwork/java/javase/tech/g1-intro-jsp-135488.html">
   G1
  </a>
  - The Garbage-First Garbage Collector.
 </li>
 <li>
  <a href="http://openjdk.java.net/jeps/189">
   Shenandoah
  </a>
  - Ultra-Low-Pause-Time Garbage Collector.
 </li>
</ul>
<h2>
 Load tools
</h2>
<p>
 <em>
  Tools that generate load and measure the system accurately without coordinated omission
 </em>
</p>
<ul>
 <li>
  <a href="http://gatling.io">
   Gatling
  </a>
  - Asynchronous non-blocking scenario driven load testing tool for testing HTTP servers.
 </li>
 <li>
  <a href="https://github.com/giltene/wrk2">
   wrk2
  </a>
  - A constant throughput, correct latency recording variant of wrk.
  <sup>
   69 GitHub links in total 132 links, ★ 526, pushed 132 days ago
  </sup>
  <sup>
   &#9733 526, pushed 132 days ago
  </sup>
 </li>
</ul>
<h2>
 Languages
</h2>
<p>
 <em>
  Languages running on the JVM.
 </em>
 *
 <a href="http://ceylon-lang.org/">
  Ceylon
 </a>
 - Object-oriented, strong and static programming language with an emphasis on immutability, created by Red Hat.
*
 <a href="http://clojure.org/">
  Clojure
 </a>
 - Dialect of Lisp created by Rich Hickey. Dynamically typed with emphasis on functional programming.
*
 <a href="http://www.erjang.org">
  Erjang
 </a>
 - A JVM-based Erlang VM.
*
 <a href="https://github.com/Frege/frege">
  Frege
 </a>
 - Pure functional programming language in the spirit of Haskell.
*
 <a href="http://golo-lang.org/">
  Golo
 </a>
 - A simple dynamic language that makes extensive usage of
 <code>
  invokedynamic
 </code>
 .
*
 <a href="http://www.groovy-lang.org/">
  Groovy
 </a>
 - Optionally typed and dynamic language, with static-typing and static compilation capabilities.
*
 <a href="http://www.oracle.com/technetwork/java/javase/overview/index.html">
  Java
 </a>
 - General-purpose, concurrent, strongly typed, class-based object-oriented language.
*
 <a href="http://jruby.org">
  JRuby
 </a>
 - Implementation of the Ruby language on the JVM.
*
 <a href="http://j-php.net">
  JPHP
 </a>
 - PHP on the Java VM.
*
 <a href="http://www.jython.org">
  Jython
 </a>
 - Python for the Java Platform.
*
 <a href="http://www.gnu.org/software/kawa/">
  Kawa
 </a>
 - Extension of the Scheme language, which is in the Lisp family of programming languages.
*
 <a href="http://kotlinlang.org/">
  Kotlin
 </a>
 - Statically typed programming language for the JVM, Android and the browser.
*
 <a href="http://www.luaj.org/luaj/3.0/README.html">
  LuaJ
 </a>
 - Java-centric implementation of lua vm built to leverage standard Java features.
*
 <a href="http://openjdk.java.net/projects/nashorn/">
  Nashorn
 </a>
 - Lightweight high-performance JavaScript runtime in Java with a native JVM.
*
 <a href="http://nodyn.io/">
  Nodyn
 </a>
 - Node.js compatible framework, running on the JVM powered by the DynJS Javascript runtime.
*
 <a href="http://www.ocamljava.org/">
  OCaml-Java
 </a>
 - Supports OCaml language v4. Generates plain Java bytecode and have seamless integration with Java.
*
 <a href="http://www.renjin.org/">
  Renjin
 </a>
 - JVM-based interpreter for the R language for the statistical analysis
*
 <a href="http://www.scala-lang.org/">
  Scala
 </a>
 - Strong and static programming language that combine object-oriented and functional programming ideas.
*
 <a href="http://www.eclipse.org/xtend/">
  Xtend
 </a>
 - Flexible and expressive dialect of Java, which compiles into Java 5 source code.
</p>
<h2>
 Memory and concurrency
</h2>
<p>
 <em>
  Tools and data structures for efficient memory layout and concurrent access.
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/real-logic/Agrona">
   Agrona
  </a>
  - Library of data structures and utility methods that are a common need when building high-performance applications.
  <sup>
   69 GitHub links in total 132 links, ★ 400, pushed 3 days ago
  </sup>
  <sup>
   &#9733 400, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="http://arrow.apache.org/">
   Apache Arrow
  </a>
  - A high-performance cross-system data layer for columnar in-memory analytics.
 </li>
 <li>
  <a href="https://github.com/lemire/bloofi">
   bloofi
  </a>
  - Java implementation of multidimensional Bloom filters
  <sup>
   69 GitHub links in total 132 links, ★ 38, pushed 56 days ago
  </sup>
  <sup>
   &#9733 38, pushed 56 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/ben-manes/caffeine">
   caffeine
  </a>
  - A high performance caching library for Java 8.
  <sup>
   69 GitHub links in total 132 links, ★ 1295, pushed 3 days ago
  </sup>
  <sup>
   &#9733 1295, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/OpenHFT/Chronicle-Bytes">
   Chronicle-Bytes
  </a>
  - Low level memory access wrappers.
  <sup>
   69 GitHub links in total 132 links, ★ 45, pushed 2 days ago
  </sup>
  <sup>
   &#9733 45, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/krukow/clj-ds">
   clj-ds
  </a>
  - Clojure's data structures modified for use outside of Clojure.
  <sup>
   69 GitHub links in total 132 links, ★ 179, pushed 922 days ago
  </sup>
  <sup>
   &#9733 179, pushed 922 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/romix/java-concurrent-hash-trie-map">
   java-concurrent-hash-trie-map
  </a>
  - Java port of a concurrent trie hash map implementation from Scala collections.
  <sup>
   69 GitHub links in total 132 links, ★ 82, pushed 60 days ago
  </sup>
  <sup>
   &#9733 82, pushed 60 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/boundary/fasttuple">
   fasttuple
  </a>
  - Collections that are laid out adjacently in both on- and off-heap memory.
  <sup>
   69 GitHub links in total 132 links, ★ 121, pushed 717 days ago
  </sup>
  <sup>
   &#9733 121, pushed 717 days ago
  </sup>
 </li>
 <li>
  <a href="http://google.github.io/flatbuffers/">
   FlatBuffers
  </a>
  - Efficient cross platform serialization library for C++, C#, Go, Java, JavaScript, PHP, and Python.
 </li>
 <li>
  <a href="https://github.com/goldmansachs/gs-collections">
   gs-collections
  </a>
  - Goldman Sachs collections framework.
  <sup>
   69 GitHub links in total 132 links, ★ 1518, pushed 50 days ago
  </sup>
  <sup>
   &#9733 1518, pushed 50 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/boundary/high-scale-lib">
   high-scale-lib
  </a>
  - Cliff Click's High Scale Library.
  <sup>
   69 GitHub links in total 132 links, ★ 250, pushed 402 days ago
  </sup>
  <sup>
   &#9733 250, pushed 402 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/carrotsearch/hppc">
   hppc
  </a>
  - High Performance Primitive Collections.
  <sup>
   69 GitHub links in total 132 links, ★ 263, pushed 110 days ago
  </sup>
  <sup>
   &#9733 263, pushed 110 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.javaslang.io/">
   javaslang
  </a>
  - Functional Library for Java 8+.
 </li>
 <li>
  <a href="http://jctools.github.io/JCTools/">
   JCTools
  </a>
  - Concurrent data structures currently missing from the JDK.
 </li>
 <li>
  <a href="https://github.com/OpenHFT/Koloboke">
   Koloboke
  </a>
  - Java Collections til the last breadcrumb of memory and performance.
  <sup>
   69 GitHub links in total 132 links, ★ 466, pushed 9 days ago
  </sup>
  <sup>
   &#9733 466, pushed 9 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/bryanduxbury/lightweight_trie">
   lightweight_trie
  </a>
  - A very memory-efficient trie (radix tree) implementation.
  <sup>
   69 GitHub links in total 132 links, ★ 30, pushed 1408 days ago
  </sup>
  <sup>
   &#9733 30, pushed 1408 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/cowtowncoder/low-gc-membuffers">
   low-gc-membuffers
  </a>
  - In-memory circular buffers that use direct ByteBuffers to minimize GC overhead.
  <sup>
   69 GitHub links in total 132 links, ★ 110, pushed 545 days ago
  </sup>
  <sup>
   &#9733 110, pushed 545 days ago
  </sup>
 </li>
 <li>
  <a href="http://netty.io/wiki/using-as-a-generic-library.html#wiki-h2-1">
   netty-buffers
  </a>
  - Memory buffer pool implementation similar to jemalloc.
 </li>
 <li>
  <a href="http://objectlayout.org">
   ObjectLayout
  </a>
  - A layout-optimized Java data structure package.
 </li>
 <li>
  <a href="https://github.com/snazy/ohc">
   ohc
  </a>
  - Java large off heap cache developed for Apache Cassandra 3.0.
  <sup>
   69 GitHub links in total 132 links, ★ 91, pushed 21 days ago
  </sup>
  <sup>
   &#9733 91, pushed 21 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/square/okio">
   okio
  </a>
  - Modern Java IO library that do clever things to save CPU and memory.
  <sup>
   69 GitHub links in total 132 links, ★ 2228, pushed 1 days ago
  </sup>
  <sup>
   &#9733 2228, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/giltene/PauselessHashMap">
   PauselessHashMap
  </a>
  - A java.util.HashMap compatible map that won't stall puts or gets when resizing.
  <sup>
   69 GitHub links in total 132 links, ★ 106, pushed 688 days ago
  </sup>
  <sup>
   &#9733 106, pushed 688 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/hrldcpr/pcollections">
   pcollections
  </a>
  - A Persistent Java Collections Library.
  <sup>
   69 GitHub links in total 132 links, ★ 203, pushed 19 days ago
  </sup>
  <sup>
   &#9733 203, pushed 19 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.paralleluniverse.co/quasar/">
   Quasar
  </a>
  - Lightweight threads and actors for the JVM.
 </li>
 <li>
  <a href="http://www.reactive-streams.org/">
   Reactive Streams
  </a>
  - Standard for asynchronous stream processing with non-blocking back pressure.
 </li>
 <li>
  <a href="https://github.com/RoaringBitmap/RoaringBitmap">
   RoaringBitmap
  </a>
  - A better compressed bitset in Java.
  <sup>
   69 GitHub links in total 132 links, ★ 355, pushed 4 days ago
  </sup>
  <sup>
   &#9733 355, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="http://projectreactor.io/">
   Reactor
  </a>
  - Reactive data applications on the JVM for Java, Groovy, Clojure and other.
 </li>
 <li>
  <a href="https://github.com/ReactiveX/RxJava">
   RxJava
  </a>
  - Library for composing asynchronous and event-based programs using observable sequences.
  <sup>
   69 GitHub links in total 132 links, ★ 13390, pushed 1 days ago
  </sup>
  <sup>
   &#9733 13390, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/OpenHFT/SmoothieMap">
   SmoothieMap
  </a>
  - java.util.Map impl with worst put latencies more than 100 times smaller than java.util.HashMap.
  <sup>
   69 GitHub links in total 132 links, ★ 90, pushed 15 days ago
  </sup>
  <sup>
   &#9733 90, pushed 15 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/real-logic/simple-binary-encoding">
   Simple Binary Encoding
  </a>
  - High Performance Message Codec.
  <sup>
   69 GitHub links in total 132 links, ★ 806, pushed 8 days ago
  </sup>
  <sup>
   &#9733 806, pushed 8 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/chrisvest/stormpot">
   stormpot
  </a>
  - A fast object pool for the JVM.
  <sup>
   69 GitHub links in total 132 links, ★ 83, pushed 8 days ago
  </sup>
  <sup>
   &#9733 83, pushed 8 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/addthis/stream-lib">
   stream-lib
  </a>
  - A Java library for summarizing data in streams for which it is infeasible to store all events.
  <sup>
   69 GitHub links in total 132 links, ★ 1341, pushed 4 days ago
  </sup>
  <sup>
   &#9733 1341, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/cognitect-labs/transducers-java">
   transducers-java
  </a>
  - Composable algorithmic transformations independent from the context of their input and output sources.
  <sup>
   69 GitHub links in total 132 links, ★ 88, pushed 307 days ago
  </sup>
  <sup>
   &#9733 88, pushed 307 days ago
  </sup>
 </li>
</ul>
<h2>
 Metaprogramming
</h2>
<p>
 <em>
  Parsers, interpreters, compilers and source generation targeted for the JVM.
 </em>
</p>
<ul>
 <li>
  <a href="http://www.antlr.org/">
   Antlr
  </a>
  - Parser generator for reading, processing, executing, or translating structured text or binary files.
 </li>
 <li>
  <a href="http://calcite.apache.org/docs/">
   Apache Calcite
  </a>
  - Dynamic data management framework and SQL parser plugin.
 </li>
 <li>
  <a href="https://github.com/google/compile-testing">
   compile-testing
  </a>
  - Testing tools for javac and annotation processors.
  <sup>
   69 GitHub links in total 132 links, ★ 256, pushed 42 days ago
  </sup>
  <sup>
   &#9733 256, pushed 42 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/derive4j/derive4j">
   derive4j
  </a>
  - Algebraic data types constructors, pattern-matching, morphisms, optics and typeclasses.
  <sup>
   69 GitHub links in total 132 links, ★ 110, pushed 75 days ago
  </sup>
  <sup>
   &#9733 110, pushed 75 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/google/error-prone">
   error-prone
  </a>
  - Catch common Java mistakes as compile-time errors.
  <sup>
   69 GitHub links in total 132 links, ★ 917, pushed 5 days ago
  </sup>
  <sup>
   &#9733 917, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="http://openjdk.java.net/projects/graal/">
   Graal
  </a>
  - New experimental just-in-time compiler for Java that is integrated with the HotSpot virtual machine.
 </li>
 <li>
  <a href="https://javacc.java.net/">
   javacc
  </a>
  - Parser generator for use with Java.
 </li>
 <li>
  <a href="https://github.com/javaparser/javaparser">
   javaparser
  </a>
  - Java 1.8 Parser and Abstract Syntax Tree for Java.
  <sup>
   69 GitHub links in total 132 links, ★ 541, pushed 0 days ago
  </sup>
  <sup>
   &#9733 541, pushed 0 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/square/javapoet">
   JavaPoet
  </a>
  - A Java API for generating .java source files.
  <sup>
   69 GitHub links in total 132 links, ★ 1905, pushed 6 days ago
  </sup>
  <sup>
   &#9733 1905, pushed 6 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jparsec/jparsec">
   jparsec
  </a>
  - Builds mini parsers in pure Java a la Haskell Parsec.
  <sup>
   69 GitHub links in total 132 links, ★ 103, pushed 229 days ago
  </sup>
  <sup>
   &#9733 103, pushed 229 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.jsweet.org/">
   JSweet
  </a>
  - A transpiler from Java to TypeScript/JavaScript.
 </li>
 <li>
  <a href="https://www.jetbrains.com/mps/">
   MPS
  </a>
  - Design and build extensible DSLs and editors.
 </li>
 <li>
  <a href="https://github.com/sirthias/parboiled">
   parboiled
  </a>
  - Parsing of arbitrary input text based on parsing expression grammars.
  <sup>
   69 GitHub links in total 132 links, ★ 886, pushed 8 days ago
  </sup>
  <sup>
   &#9733 886, pushed 8 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/graalvm/sulong">
   Sulong
  </a>
  - LLVM IR interpreter written in Java using Truffle and Graal.
  <sup>
   69 GitHub links in total 132 links, ★ 117, pushed 2 days ago
  </sup>
  <sup>
   &#9733 117, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/graalvm/truffle">
   Truffle
  </a>
  - Framework for implementing languages as simple interpreters.
  <sup>
   69 GitHub links in total 132 links, ★ 52, pushed 8 days ago
  </sup>
  <sup>
   &#9733 52, pushed 8 days ago
  </sup>
 </li>
 <li>
  <a href="https://eclipse.org/Xtext/">
   Xtext
  </a>
  - Framework for development of programming languages and DSLs.
 </li>
</ul>
<h2>
 Native
</h2>
<p>
 <em>
  Interconnecting JVM and native code
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/fusesource/hawtjni">
   hawtjni
  </a>
  - A JNI code generator based on the JNI generator used in Eclipse SWT.
  <sup>
   69 GitHub links in total 132 links, ★ 50, pushed 7 days ago
  </sup>
  <sup>
   &#9733 50, pushed 7 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/eclipsesource/j2v8">
   j2v8
  </a>
  - Java API for Google's V8 JavaScript engine.
  <sup>
   69 GitHub links in total 132 links, ★ 259, pushed 14 days ago
  </sup>
  <sup>
   &#9733 259, pushed 14 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/bytedeco/javacpp">
   JavaCPP
  </a>
  - JavaCPP provides efficient access to native C++ inside Java.
  <sup>
   69 GitHub links in total 132 links, ★ 1511, pushed 3 days ago
  </sup>
  <sup>
   &#9733 1511, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jnr/jnr-ffi">
   jnr-ffi
  </a>
  - Load native libraries without writing JNI code by hand.
  <sup>
   69 GitHub links in total 132 links, ★ 260, pushed 50 days ago
  </sup>
  <sup>
   &#9733 260, pushed 50 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/dvx/jssembly">
   jssembly
  </a>
  - Execution of native assembly from Java.
  <sup>
   69 GitHub links in total 132 links, ★ 91, pushed 75 days ago
  </sup>
  <sup>
   &#9733 91, pushed 75 days ago
  </sup>
 </li>
 <li>
  <a href="http://openjdk.java.net/projects/panama/">
   Project Panama
  </a>
  - Enriching the connections between the JVM and APIs used by C programmers.
 </li>
</ul>
<h2>
 Network
</h2>
<p>
 <em>
  Tools for network packet capture, monitoring, testing and resiliency.
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/tylertreat/comcast">
   comcast
  </a>
  - Simulating shitty network connections.
  <sup>
   69 GitHub links in total 132 links, ★ 4212, pushed 48 days ago
  </sup>
  <sup>
   &#9733 4212, pushed 48 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/buger/gor">
   gor
  </a>
  - HTTP traffic replay in real-time.
  <sup>
   69 GitHub links in total 132 links, ★ 5039, pushed 3 days ago
  </sup>
  <sup>
   &#9733 5039, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/LatencyUtils/jRT">
   jRT
  </a>
  - Measures response time of a java application to socket-based requests.
  <sup>
   69 GitHub links in total 132 links, ★ 14, pushed 316 days ago
  </sup>
  <sup>
   &#9733 14, pushed 316 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/k3po/k3po">
   K3PO
  </a>
  - Create arbitrary network traffic and behavior to certify whether a network endpoint behaves correctly.
  <sup>
   69 GitHub links in total 132 links, ★ 21, pushed 13 days ago
  </sup>
  <sup>
   &#9733 21, pushed 13 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/mefellows/muxy">
   muxy
  </a>
  - Simulating real-world distributed system failures.
  <sup>
   69 GitHub links in total 132 links, ★ 521, pushed 99 days ago
  </sup>
  <sup>
   &#9733 521, pushed 99 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Netflix/SimianArmy">
   SimianArmy
  </a>
  - Resiliency tool that helps ensure that your applications can tolerate random instance failures.
  <sup>
   69 GitHub links in total 132 links, ★ 3979, pushed 34 days ago
  </sup>
  <sup>
   &#9733 3979, pushed 34 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/kaitoy/pcap4j">
   pcap4j
  </a>
  - Java library for capturing, crafting, and sending packets using libpcap.
  <sup>
   69 GitHub links in total 132 links, ★ 171, pushed 2 days ago
  </sup>
  <sup>
   &#9733 171, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/rafael-santiago/pig">
   pig
  </a>
  - A Linux packet crafting tool.
  <sup>
   69 GitHub links in total 132 links, ★ 236, pushed 2 days ago
  </sup>
  <sup>
   &#9733 236, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.tcpdump.org/">
   tcpdump
  </a>
  - Packet analyzer for network traffic capture.
 </li>
 <li>
  <a href="https://github.com/simsong/tcpflow">
   tcpflow
  </a>
  - Captures TCP connections flows in a way that is convenient for protocol analysis and debugging.
  <sup>
   69 GitHub links in total 132 links, ★ 516, pushed 98 days ago
  </sup>
  <sup>
   &#9733 516, pushed 98 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/appneta/tcpreplay">
   tcpreplay
  </a>
  - Pcap editing and replay tools.
  <sup>
   69 GitHub links in total 132 links, ★ 137, pushed 113 days ago
  </sup>
  <sup>
   &#9733 137, pushed 113 days ago
  </sup>
 </li>
</ul>
<h2>
 Nix tools
</h2>
<p>
 <em>
  Useful *nix tools when profiling the JVM and interaction with the host environment
 </em>
 *
 <a href="http://www.atoptool.nl/">
  atoptool
 </a>
 - Logging of system and process activity for long-term analysis, highlighting overloaded system.
*
 <a href="http://www.brendangregg.com/flamegraphs.html">
  Flame Graphs
 </a>
 - Visualization of profiled software, allowing the most frequent code-paths to be identified quickly and accurately.
*
 <a href="http://docs.oracle.com/javase/8/docs/technotes/tools/unix/javap.html">
  javap
 </a>
 - Disassembles class files into code that reflects the java bytecode.
*
 <a href="http://docs.oracle.com/javase/8/docs/technotes/tools/unix/jhat.html">
  jhat
 </a>
 - Java Heap Analysis Tool
*
 <a href="http://docs.oracle.com/javase/8/docs/technotes/tools/unix/jinfo.html">
  jinfo
 </a>
 - Prints configuration information for a given process.
*
 <a href="http://docs.oracle.com/javase/8/docs/technotes/tools/unix/jstack.html">
  jstack
 </a>
 - Prints stack traces of threads for a given Java process.
*
 <a href="https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jstat.html">
  jstat
 </a>
 - Monitors GC and compiler statistics in the JVM.
*
 <a href="http://linux.die.net/man/7/hwloc">
  hwloc
 </a>
 - Reports the structure of the processor, number of cores, hyperthreads and cache size.
*
 <a href="https://github.com/RRZE-HPC/likwid">
  likwid
 </a>
 - Read hardware performance counters on Intel and AMD processors.
*
 <a href="http://linux.die.net/man/8/numactl">
  numactl
 </a>
 - Control NUMA policy for processes or shared memory.
*
 <a href="http://oprofile.sourceforge.net/news/">
  oprofile
 </a>
 - System-wide hardware performance monitoring with easy-to-use interface at low overhead.
*
 <a href="https://perf.wiki.kernel.org/index.php/Main_Page">
  perf
 </a>
 - Linux profiling with performance counters.
*
 <a href="https://github.com/brendangregg/perf-tools">
  perf-tools
 </a>
 - Performance analysis tools based on Linux perf_events (aka perf) and ftrace.
*
 <a href="http://sebastien.godard.pagesperso-orange.fr">
  sysstat
 </a>
 - Performance monitoring tools for Linux.
*
 <a href="http://linuxcommand.org/man_pages/taskset1.html">
  taskset
 </a>
 - Retrieve or set a processes’s CPU affinity.
</p>
<h2>
 Profilers
</h2>
<p>
 <em>
  Tools that provide profiling and tracing information to aid program optimization
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/google/allocation-instrumenter">
   allocation-instrumenter
  </a>
  - Java agent that rewrites bytecode to instrument allocation sites.
  <sup>
   69 GitHub links in total 132 links, ★ 54, pushed 380 days ago
  </sup>
  <sup>
   &#9733 54, pushed 380 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Devexperts/aprof">
   aprof
  </a>
  - Java memory allocation profiler.
  <sup>
   69 GitHub links in total 132 links, ★ 71, pushed 103 days ago
  </sup>
  <sup>
   &#9733 71, pushed 103 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jbachorik/btrace">
   BTrace
  </a>
  - a safe, dynamic tracing tool for the Java platform.
 </li>
 <li>
  <a href="http://chrononsystems.com">
   Chronon
  </a>
  - Record your entire java program. Replay on any machine.
 </li>
 <li>
  <a href="https://github.com/chewiebug/GCViewer">
   GCViewer
  </a>
  - GCViewer is a tool that visualizes verbose GC output.
  <sup>
   69 GitHub links in total 132 links, ★ 1292, pushed 14 days ago
  </sup>
  <sup>
   &#9733 1292, pushed 14 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jClarity/hawkshaw">
   hawkshaw
  </a>
  - Tools for tracking down memory / JVM problems & generating predictable-as-possible VM behaviour.
  <sup>
   69 GitHub links in total 132 links, ★ 33, pushed 153 days ago
  </sup>
  <sup>
   &#9733 33, pushed 153 days ago
  </sup>
 </li>
 <li>
  <a href="http://hdrhistogram.github.io/HdrHistogram/">
   HdrHistogram
  </a>
  - A Histogram that supports recording and analyzing sampled data value counts.
 </li>
 <li>
  <a href="https://bitbucket.org/marshallpierce/hdrhistogram-metrics-reservoir">
   hdrhistogram-metrics-reservoir
  </a>
  - A Metrics Reservoir implementation backed by HdrHistogram.
 </li>
 <li>
  <a href="https://github.com/mariusae/heapster">
   heapster
  </a>
  - Production heap profiling for the JVM.
  <sup>
   69 GitHub links in total 132 links, ★ 295, pushed 22 days ago
  </sup>
  <sup>
   &#9733 295, pushed 22 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/RichardWarburton/honest-profiler">
   honest-profiler
  </a>
  - Sampling JVM profiler without the safepoint sample bias.
  <sup>
   69 GitHub links in total 132 links, ★ 380, pushed 7 days ago
  </sup>
  <sup>
   &#9733 380, pushed 7 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jbellis/jamm">
   jamm
  </a>
  - Measure actual object memory use including JVM overhead.
  <sup>
   69 GitHub links in total 132 links, ★ 306, pushed 401 days ago
  </sup>
  <sup>
   &#9733 306, pushed 401 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.oracle.com/technetwork/java/javaseproducts/mission-control/java-mission-control-1998576.html">
   Java Mission Control
  </a>
  - Continuously collect low level and detailed runtime information enabling after-the-fact incident analysis.
 </li>
 <li>
  <a href="https://github.com/dweiss/java-sizeof">
   java-sizeof
  </a>
  - Memory consumption estimator for Java.
  <sup>
   69 GitHub links in total 132 links, ★ 78, pushed 27 days ago
  </sup>
  <sup>
   &#9733 78, pushed 27 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/AdoptOpenJDK/jitwatch">
   jitwatch
  </a>
  - Log analyser / visualiser for Java HotSpot JIT compiler.
  <sup>
   69 GitHub links in total 132 links, ★ 746, pushed 1 days ago
  </sup>
  <sup>
   &#9733 746, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.azul.com/jhiccup/">
   jHiccup
  </a>
  - jHiccup is an open source tool designed to measure the pauses and stalls associated with an application’s underlying Java runtime platform.
 </li>
 <li>
  <a href="http://openjdk.java.net/projects/code-tools/jmh/">
   jmh
  </a>
  - Micro benchmarks written in Java and other languages targetting the JVM.
 </li>
 <li>
  <a href="http://openjdk.java.net/projects/code-tools/jol/">
   JOL
  </a>
  - Analyze actual object layout schemes, footprint, and references in JVMs.
 </li>
 <li>
  <a href="https://www.ej-technologies.com/products/jprofiler/overview.html">
   JProfiler
  </a>
  - Helps resolve performance bottlenecks, pin down memory leaks and understand threading issues.
 </li>
 <li>
  <a href="https://docs.oracle.com/javase/8/docs/technotes/guides/jvmti/">
   JVMTI
  </a>
  - Provide a native API to inspect the state and to control the execution of applications running in the JVM.
 </li>
 <li>
  <a href="https://github.com/patric-r/jvmtop">
   jvmtop
  </a>
  - Lightweight console application to monitor running jvms on a machine in top-like manner.
  <sup>
   69 GitHub links in total 132 links, ★ 193, pushed 105 days ago
  </sup>
  <sup>
   &#9733 193, pushed 105 days ago
  </sup>
 </li>
 <li>
  <a href="https://eclipse.org/mat/">
   MAT
  </a>
  - Java heap analyzer that help find memory leaks and reduce memory consumption.
 </li>
 <li>
  <a href="https://github.com/square/leakcanary">
   leakcanary
  </a>
  - A memory leak detection library for Android and Java.
  <sup>
   69 GitHub links in total 132 links, ★ 8691, pushed 11 days ago
  </sup>
  <sup>
   &#9733 8691, pushed 11 days ago
  </sup>
 </li>
 <li>
  <a href="http://metrics.dropwizard.io/">
   metrics
  </a>
  - Measure the behavior of critical components in production environment.
 </li>
 <li>
  <a href="http://www.peternier.com/projects/overseer/overseer.php">
   Overseer
  </a>
  - Low-Level Hardware Monitoring and Management for Java.
 </li>
 <li>
  <a href="https://github.com/jrudolph/perf-map-agent">
   perf-map-agent
  </a>
  - Generate method mappings to use with the linux
  <code>
   perf
  </code>
  tool.
  <sup>
   69 GitHub links in total 132 links, ★ 258, pushed 4 days ago
  </sup>
  <sup>
   &#9733 258, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/coderplay/perfj">
   perfj
  </a>
  - Linux perf for java programs.
  <sup>
   69 GitHub links in total 132 links, ★ 233, pushed 211 days ago
  </sup>
  <sup>
   &#9733 233, pushed 211 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Cue/polarbear">
   polarbear
  </a>
  - A tool to help diagnose OutOfMemoryError conditions.
  <sup>
   69 GitHub links in total 132 links, ★ 17, pushed 1296 days ago
  </sup>
  <sup>
   &#9733 17, pushed 1296 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/riemann/riemann-jvm-profiler">
   Riemann JVM Profiler
  </a>
  - JVM agent which sends function-level profiler telemetry to a Riemann server for analysis, visualization, and storage.
  <sup>
   69 GitHub links in total 132 links, ★ 245, pushed 495 days ago
  </sup>
  <sup>
   &#9733 245, pushed 495 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/etsy/statsd-jvm-profiler">
   statsd-jvm-profiler
  </a>
  - JVM agent profiler that sends profiling data to StatsD.
  <sup>
   69 GitHub links in total 132 links, ★ 177, pushed 39 days ago
  </sup>
  <sup>
   &#9733 177, pushed 39 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/aragozin/jvm-tools">
   Swiss Java Knife
  </a>
  - Small set of tools for JVM troublshooting, monitoring and profiling.
  <sup>
   69 GitHub links in total 132 links, ★ 570, pushed 37 days ago
  </sup>
  <sup>
   &#9733 570, pushed 37 days ago
  </sup>
 </li>
 <li>
  <a href="https://www.takipi.com/">
   Takipi
  </a>
  - Tells you when and why code breaks in production.
 </li>
 <li>
  <a href="https://www.yourkit.com/">
   YourKit
  </a>
  - Fully featured, easy to use, low overhead profiler.
 </li>
 <li>
  <a href="https://github.com/openzipkin/zipkin">
   Zipkin
  </a>
  - A distributed tracing system gather timing data for disparate services developed by Twitter.
  <sup>
   69 GitHub links in total 132 links, ★ 3459, pushed 2 days ago
  </sup>
  <sup>
   &#9733 3459, pushed 2 days ago
  </sup>
 </li>
</ul>
<h2>
 Runtimes
</h2>
<p>
 <em>
  Tools for managing jvm runtime processes
 </em>
 *
 <a href="http://www.crashub.org/">
  CRaSH
 </a>
 - The shell for the Java Platform.
*
 <a href="https://github.com/ninjudd/drip">
  Drip
 </a>
 - Fast JVM launching without the hassle of persistent JVMs.
*
 <a href="https://github.com/HotswapProjects/HotswapAgent">
  HotswapAgent
 </a>
 - Redefine classes at runtime and skip the redeploy process.
*
 <a href="https://github.com/airlift/jvmkill">
  jvmkill
 </a>
 - Agent that forcibly terminates the JVM when it is unable to allocate memory or create a thread.
*
 <a href="http://martiansoftware.com/nailgun/">
  Nailgun
 </a>
 - Nailgun is a client, protocol, and server for running Java programs from the command line without incurring the JVM startup overhead.
</p>
<h2>
 Virtual Machines
</h2>
<p>
 <em>
  Virtual machines that implement the JVM specification or parts of it.
 </em>
 *
 <a href="https://github.com/ReadyTalk/avian">
  Avian
 </a>
 - Lightweight highly portable JVM with an option for AOT compilation.
*
 <a href="https://source.android.com/devices/tech/dalvik/">
  Dalvik
 </a>
 - Android runtime (ART) is the managed runtime used by applications and some system services on Android.
*
 <a href="http://dcevm.github.io">
  DCEVM
 </a>
 - Modification of Java HotSwap VM with unlimited support for reloading classes at runtime.
*
 <a href="http://openjdk.java.net/groups/hotspot/">
  HotSpot
 </a>
 - HotSpot virtual machine maintained and distributed by Oracle Corporation.
*
 <a href="http://www.ibm.com/developerworks/java/jdk/">
  IBM J9
 </a>
 - JVM developed by IBM.
*
 <a href="https://github.com/google/j2objc">
  J2ObjC
 </a>
 - Translator from Java source to Objective-C code. Keeps shared code between iOS native apps and Android native apps. 
*
 <a href="https://github.com/zxh0/jvm.go">
  jvm.go
 </a>
 - A JVM written in Go.
*
 <a href="https://github.com/codenameone/CodenameOne/tree/master/vm">
  ParparVM
 </a>
 - An Open Source Java bytecode to C translator for iOS native development. Designed as a part of the
 <a href="https://www.codenameone.com/">
  Codename One
 </a>
 WORA for mobile project.
*
 <a href="https://robovm.com/">
  RoboVM
 </a>
 - Create native iOS and Android apps in Java.
*
 <a href="https://www.azul.com/products/zing/">
  Zing
 </a>
 - The only JVM that eliminates Java garbage collection pauses for large heap sizes.
*
 <a href="https://www.azul.com/products/zulu/">
  Zulu
 </a>
 - The only certified multi-platform build of OpenJDK: Free, 100% open source Java.
</p>
<h1>
 Resources
</h1>
<h2>
 Documentation
</h2>
<p>
 <em>
  Documentation related to JVM
 </em>
 *
 <a href="https://groups.google.com/forum/#!msg/mechanical-sympathy/icNZJejUHfE/BfDekfBEs_sJ">
  Coordinated Omission problem
 </a>
 - Discussion on Mechanical Sympathy.
*
 <a href="http://mechanical-sympathy.blogspot.se/2011/07/false-sharing.html">
  False sharing
 </a>
 - Threads impact the performance of each other while modifying independent variables sharing the same cache line. Martin Thompson.
*
 <a href="https://docs.oracle.com/javase/specs/jvms/se8/jvms8.pdf">
  The JVM specification
 </a>
 - The Java Virtual
Machine Specification Java SE 8 Edition.
*
 <a href="http://www.cs.umd.edu/~pugh/java/memoryModel/">
  The Java Memory Model
 </a>
 - Starting point for discussions of and information concerning the Java Memory Model.
*
 <a href="http://gee.cs.oswego.edu/dl/jmm/cookbook.html">
  The JSR-133 Cookbook for Compiler Writers
 </a>
 - Unofficial guide to implementing the new Java Memory Model (JMM) specified by JSR-133.
*
 <a href="http://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/">
  Garbage Collection Tuning Guide
 </a>
 - HotSpot Virtual Machine Garbage Collection Tuning Guide.
*
 <a href="http://psy-lob-saw.blogspot.se/2014/03/where-is-my-safepoint.html">
  Safepoints
 </a>
 - Where is my safepoint? Nitsan Wakart.
 <br/>
 *
 <a href="https://www.informatica.com/downloads/1568_high_perf_messaging_wp/Topics-in-High-Performance-Messaging.htm">
  Topics in High-Performance Messaging
 </a>
 - Design decisions, experience and constraints explained in high performance messaging systems.
*
 <a href="http://www.infoq.com/articles/top-10-performance-mistakes">
  Top 10 Performance Mistakes
 </a>
 - Digest of the top 10 performance related mistakes Martin Thompson has seen in production.
</p>
<h2>
 Communities
</h2>
<p>
 <em>
  Active discussions.
 </em>
</p>
<ul>
 <li>
  <a href="http://altair.cs.oswego.edu/mailman/listinfo/concurrency-interest">
   concurrency-interest
  </a>
  - Discussion list for JSR-166.
 </li>
 <li>
  <a href="http://mail.openjdk.java.net/mailman/listinfo/hotspot-compiler-dev">
   hotspot-compiler-dev
  </a>
  - Technical discussion about the development of the HotSpot bytecode compilers.
 </li>
 <li>
  <a href="http://mail.openjdk.java.net/mailman/listinfo/hotspot-dev">
   hotspot-dev
  </a>
  - HotSpot development mailing list.
 </li>
 <li>
  <a href="http://mail.openjdk.java.net/mailman/listinfo/hotspot-gc-dev">
   hotspot-gc-dev
  </a>
  - Technical discussion about the development of the HotSpot garbage collectors.
 </li>
 <li>
  <a href="https://groups.google.com/forum/#!forum/mechanical-sympathy">
   mechanical-sympathy
  </a>
  - Discussing how to code sympathetically to and measure the underlying stack/platform so good performance can be extracted.
 </li>
 <li>
  <a href="http://vmmeetup.github.io/2015/">
   Virtual Machine Meetup
  </a>
  - Venue for discussing the latest research and developments in the area of managed language execution.
 </li>
</ul>
<h2>
 Media
</h2>
<p>
 <em>
  Videos, podcasts and other media related to JVMs
 </em>
 *
 <a href="http://www.infoq.com/presentations/java-vs-c-performance">
  Java vs. C Performance
 </a>
 - Cliff Click.
*
 <a href="https://www.youtube.com/watch?v=_6vJyciXkwo">
  Java Profiling from the Ground Up
 </a>
 - Nitsan Wakart.
*
 <a href="https://www.youtube.com/watch?v=3g9R-RVIkOE">
  The Illusion of Execution
 </a>
 - Nitsan Wakart.
*
 <a href="https://www.youtube.com/watch?v=MC1EKLQ2Wmg">
  Mythbusting Modern Hardware to Gain 'Mechanical Sympathy'
 </a>
 - Martin Thompson.
*
 <a href="https://www.youtube.com/watch?v=fDGWWpHlzvw">
  Designing for Performance
 </a>
 - Martin Thompson.
*
 <a href="https://www.youtube.com/watch?v=lJ8ydIuPFeU">
  How NOT to Measure Latency
 </a>
 - Gil Tene.
*
 <a href="http://openjdk.java.net/projects/mlvm/jvmlangsummit/">
  JVM Language Summit 2015
 </a>
 - JVM Language Summit 2015.
*
 <a href="https://www.youtube.com/watch?v=vzzABBxo44g">
  Bits of advice for VM writers
 </a>
 - Cliff Click.
*
 <a href="https://www.youtube.com/watch?v=_e5hujoTkgY">
  Understanding Java garbage collection ...
 </a>
 - Gil Tene.
*
 <a href="https://www.youtube.com/watch?v=bZuPTCaciLU">
  Faster Object Arrays
 </a>
 - Gil Tene at GOTO Conferences.
*
 <a href="https://www.youtube.com/watch?v=TxqsKzxyySo">
  Java Memory Model Pragmatics
 </a>
 - Aleksey Shipilev.
</p>
<h2>
 People
</h2>
<p>
 <em>
  People that influence JVM development and/or the community around it
 </em>
 *
 <a href="http://shipilev.net/">
  Aleksey Shipilëv
 </a>
 - Developing Oracle/Open JDK/Hotspot and other Java-related technologies.
*
 <a href="https://twitter.com/BrianGoetz">
  Brian Goetz
 </a>
 - Java Language Architect at Oracle.
*
 <a href="https://twitter.com/benjchristensen">
  Ben Christensen
 </a>
 - Facebook, Netflix, Apple engineering.
*
 <a href="https://twitter.com/headius">
  Charles Nutter
 </a>
 - JRuby guy.
*
 <a href="http://www.cliffc.org/blog/">
  Cliff Click
 </a>
 - Creator of the HotSpot Server Compiler.
*
 <a href="https://blogs.oracle.com/dave/">
  Dave Dice
 </a>
 - Senior research scientist in the Scalable Synchronization Research Group within Oracle.
*
 <a href="http://akarnokd.blogspot.se/">
  Dávid Karnok
 </a>
 - RxJava committer that blogs about advanced RxJava.
*
 <a href="http://g.oswego.edu/">
  Doug Lea
 </a>
 - Author of the Java memory model.
*
 <a href="https://twitter.com/giltene">
  Gil Tene
 </a>
 - Azul Systems.
*
 <a href="https://blogs.oracle.com/jrose/">
  John Rose
 </a>
 - HotSpot developer.
*
 <a href="https://twitter.com/jboner">
  Jonas Bonér
 </a>
 - Founder & CTO of Lightbend.
*
 <a href="https://twitter.com/lagergren">
  Marcus Lagergren
 </a>
 - Java language team alumnus.
*
 <a href="https://twitter.com/mreinhold">
  Mark Reinhold
 </a>
 - Chief Architect, Java Platform Group, Oracle.
*
 <a href="http://mechanical-sympathy.blogspot.se/">
  Martin Thompson
 </a>
 - Pasty faced performance gangster.
*
 <a href="https://twitter.com/karianna">
  Martijn Verburg
 </a>
 - Java Champion.
*
 <a href="http://psy-lob-saw.blogspot.se/2014/03/where-is-my-safepoint.html">
  Nitsan Wakart
 </a>
 - Azul Systems.
*
 <a href="https://twitter.com/normanmaurer">
  Norman Maurer
 </a>
 - Netty developer.
*
 <a href="https://twitter.com/extempore2">
  Paul Phillips
 </a>
 - Forever undisputed SLOC Scala compiler dev.
*
 <a href="https://twitter.com/PeterLawrey">
  Peter Lawrey
 </a>
 - Innovative developer of high performance Java systems for competitive advantage.
*
 <a href="https://twitter.com/RichardWarburto">
  Richard Warburton
 </a>
 - Developer, Speaker, Author.
*
 <a href="https://twitter.com/toddlmontgomery">
  Todd L. Montgomery
 </a>
 - Ex-CTO, Ex-NASA researcher, network geek, messaging middleware designer.
*
 <a href="https://twitter.com/smaldini">
  Stéphane Maldini
 </a>
 - Project Reactor Lead @Pivotal.
*
 <a href="https://twitter.com/stuartmarks">
  Stuart Marks
 </a>
 - Doctor Deprecator. Java/JDK/OpenJDK developer 
*
 <a href="https://twitter.com/viktorklang">
  Viktor Klang
 </a>
 - Deputy CTO at Typesafe Inc.
</p>
<h1>
 Contributing
</h1>
<p>
 Contributions are very welcome!
</p>
<p>
 Please have a look at
 <a href="https://github.com/deephacks/awesome-jvm/blob/master/contributing.md">
  contributing.md
 </a>
 for guidelines.
</p>
