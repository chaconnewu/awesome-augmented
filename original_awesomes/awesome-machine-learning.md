<h1>
 Awesome Machine Learning
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<p>
 A curated list of awesome machine learning frameworks, libraries and software (by language). Inspired by awesome-php.
</p>
<p>
 If you want to contribute to this list (please do), send me a pull request or contact me
 <a href="https://twitter.com/josephmisiti">
  @josephmisiti
 </a>
 Also, when you noticed that listed repository should be deprecated.
</p>
<ul>
 <li>
  Repository's owner explicitly say that "this library is not maintained".
 </li>
 <li>
  Not committed for long time (2~3 years).
 </li>
</ul>
<p>
 For a list of free machine learning books available for download, go
 <a href="https://github.com/josephmisiti/awesome-machine-learning/blob/master/books.md">
  here
 </a>
 .
</p>
<h2>
 Table of Contents
</h2>
<!-- MarkdownTOC depth=4 -->
<ul>
 <li>
  <a href="#c">
   C
  </a>
  <ul>
   <li>
    <a href="#c-general-purpose">
     General-Purpose Machine Learning
    </a>
   </li>
   <li>
    <a href="#c-cv">
     Computer Vision
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#cpp">
   C++
  </a>
  <ul>
   <li>
    <a href="#cpp-cv">
     Computer Vision
    </a>
   </li>
   <li>
    <a href="#cpp-general-purpose">
     General-Purpose Machine Learning
    </a>
   </li>
   <li>
    <a href="#cpp-nlp">
     Natural Language Processing
    </a>
   </li>
   <li>
    <a href="#cpp-sequence">
     Sequence Analysis
    </a>
   </li>
   <li>
    <a href="#cpp-gestures">
     Gesture Recognition
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#common-lisp">
   Common Lisp
  </a>
  <ul>
   <li>
    <a href="#common-lisp-general-purpose">
     General-Purpose Machine Learning
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#clojure">
   Clojure
  </a>
  <ul>
   <li>
    <a href="#clojure-nlp">
     Natural Language Processing
    </a>
   </li>
   <li>
    <a href="#clojure-general-purpose">
     General-Purpose Machine Learning
    </a>
   </li>
   <li>
    <a href="#clojure-data-analysis">
     Data Analysis / Data Visualization
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#erlang">
   Erlang
  </a>
  <ul>
   <li>
    <a href="#erlang-general-purpose">
     General-Purpose Machine Learning
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#go">
   Go
  </a>
  <ul>
   <li>
    <a href="#go-nlp">
     Natural Language Processing
    </a>
   </li>
   <li>
    <a href="#go-general-purpose">
     General-Purpose Machine Learning
    </a>
   </li>
   <li>
    <a href="#go-data-analysis">
     Data Analysis / Data Visualization
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#haskell">
   Haskell
  </a>
  <ul>
   <li>
    <a href="#haskell-general-purpose">
     General-Purpose Machine Learning
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#java">
   Java
  </a>
  <ul>
   <li>
    <a href="#java-nlp">
     Natural Language Processing
    </a>
   </li>
   <li>
    <a href="#java-general-purpose">
     General-Purpose Machine Learning
    </a>
   </li>
   <li>
    <a href="#java-data-analysis">
     Data Analysis / Data Visualization
    </a>
   </li>
   <li>
    <a href="#java-deep-learning">
     Deep Learning
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#javascript">
   Javascript
  </a>
  <ul>
   <li>
    <a href="#javascript-nlp">
     Natural Language Processing
    </a>
   </li>
   <li>
    <a href="#javascript-data-analysis">
     Data Analysis / Data Visualization
    </a>
   </li>
   <li>
    <a href="#javascript-general-purpose">
     General-Purpose Machine Learning
    </a>
   </li>
   <li>
    <a href="#javascript-misc">
     Misc
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#julia">
   Julia
  </a>
  <ul>
   <li>
    <a href="#julia-general-purpose">
     General-Purpose Machine Learning
    </a>
   </li>
   <li>
    <a href="#julia-nlp">
     Natural Language Processing
    </a>
   </li>
   <li>
    <a href="#julia-data-analysis">
     Data Analysis / Data Visualization
    </a>
   </li>
   <li>
    <a href="#julia-misc">
     Misc Stuff / Presentations
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#lua">
   Lua
  </a>
  <ul>
   <li>
    <a href="#lua-general-purpose">
     General-Purpose Machine Learning
    </a>
   </li>
   <li>
    <a href="#lua-demos">
     Demos and Scripts
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#matlab">
   Matlab
  </a>
  <ul>
   <li>
    <a href="#matlab-cv">
     Computer Vision
    </a>
   </li>
   <li>
    <a href="#matlab-nlp">
     Natural Language Processing
    </a>
   </li>
   <li>
    <a href="#matlab-general-purpose">
     General-Purpose Machine Learning
    </a>
   </li>
   <li>
    <a href="#matlab-data-analysis">
     Data Analysis / Data Visualization
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#net">
   .NET
  </a>
  <ul>
   <li>
    <a href="#net-cv">
     Computer Vision
    </a>
   </li>
   <li>
    <a href="#net-nlp">
     Natural Language Processing
    </a>
   </li>
   <li>
    <a href="#net-general-purpose">
     General-Purpose Machine Learning
    </a>
   </li>
   <li>
    <a href="#net-data-analysis">
     Data Analysis / Data Visualization
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#objectivec">
   Objective C
  </a>
  <ul>
   <li>
    <a href="#objectivec-general-purpose">
     General-Purpose Machine Learning
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#ocaml">
   OCaml
  </a>
  <ul>
   <li>
    <a href="#ocaml-general-purpose">
     General-Purpose Machine Learning
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#php">
   PHP
  </a>
  <ul>
   <li>
    <a href="#php-nlp">
     Natural Language Processing
    </a>
   </li>
   <li>
    <a href="#php-general-purpose">
     General-Purpose Machine Learning
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#python">
   Python
  </a>
  <ul>
   <li>
    <a href="#python-cv">
     Computer Vision
    </a>
   </li>
   <li>
    <a href="#python-nlp">
     Natural Language Processing
    </a>
   </li>
   <li>
    <a href="#python-general-purpose">
     General-Purpose Machine Learning
    </a>
   </li>
   <li>
    <a href="#python-data-analysis">
     Data Analysis / Data Visualization
    </a>
   </li>
   <li>
    <a href="#python-misc">
     Misc Scripts / iPython Notebooks / Codebases
    </a>
   </li>
   <li>
    <a href="#python-kaggle">
     Kaggle Competition Source Code
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#ruby">
   Ruby
  </a>
  <ul>
   <li>
    <a href="#ruby-nlp">
     Natural Language Processing
    </a>
   </li>
   <li>
    <a href="#ruby-general-purpose">
     General-Purpose Machine Learning
    </a>
   </li>
   <li>
    <a href="#ruby-data-analysis">
     Data Analysis / Data Visualization
    </a>
   </li>
   <li>
    <a href="#ruby-misc">
     Misc
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#rust">
   Rust
  </a>
  <ul>
   <li>
    <a href="#rust-general-purpose">
     General-Purpose Machine Learning
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#r">
   R
  </a>
  <ul>
   <li>
    <a href="#r-general-purpose">
     General-Purpose Machine Learning
    </a>
   </li>
   <li>
    <a href="#r-data-analysis">
     Data Analysis / Data Visualization
    </a>
   </li>
  </ul>
 </li>
 <li>
  [SAS] (#sas)
  <ul>
   <li>
    [General-Purpose Machine Learning] (#sas-general-purpose)
   </li>
   <li>
    [Data Analysis / Data Visualization] (#sas-data-analysis)
   </li>
   <li>
    [High Performance Machine Learning (MPP)] (#sas-mpp)
   </li>
   <li>
    [Natural Language Processing] (#sas-nlp)
   </li>
   <li>
    [Demos and Scripts] (#sas-demos)
   </li>
  </ul>
 </li>
 <li>
  <a href="#scala">
   Scala
  </a>
  <ul>
   <li>
    <a href="#scala-nlp">
     Natural Language Processing
    </a>
   </li>
   <li>
    <a href="#scala-data-analysis">
     Data Analysis / Data Visualization
    </a>
   </li>
   <li>
    <a href="#scala-general-purpose">
     General-Purpose Machine Learning
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#swift">
   Swift
  </a>
  <ul>
   <li>
    <a href="#swift-general-purpose">
     General-Purpose Machine Learning
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#credits">
   Credits
  </a>
 </li>
</ul>
<!-- /MarkdownTOC -->
<p>
 <a name="c">
 </a>
</p>
<h2>
 C
</h2>
<p>
 <a name="c-general-purpose">
 </a>
</p>
<h4>
 General-Purpose Machine Learning
</h4>
<ul>
 <li>
  <a href="https://github.com/GHamrouni/Recommender">
   Recommender
  </a>
  - A C library for product recommendations/suggestions using collaborative filtering (CF).
  <sup>
   377 GitHub links in total 753 links, &#9733 82, pushed 1069 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/pjreddie/darknet">
   Darknet
  </a>
  - Darknet is an open source neural network framework written in C and CUDA. It is fast, easy to install, and supports CPU and GPU computation.
  <sup>
   377 GitHub links in total 753 links, &#9733 752, pushed 26 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="c-cv">
 </a>
</p>
<h4>
 Computer Vision
</h4>
<ul>
 <li>
  <a href="https://github.com/liuliu/ccv">
   CCV
  </a>
  - C-based/Cached/Core Computer Vision Library, A Modern Computer Vision Library
  <sup>
   377 GitHub links in total 753 links, &#9733 5192, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.vlfeat.org/">
   VLFeat
  </a>
  - VLFeat is an open and portable library of computer vision algorithms, which has Matlab toolbox
 </li>
</ul>
<h3>
 Speech Recognition
</h3>
<ul>
 <li>
  <a href="http://htk.eng.cam.ac.uk/">
   HTK
  </a>
  -The Hidden Markov Model Toolkit (HTK) is a portable toolkit for building and manipulating hidden Markov models.
 </li>
</ul>
<p>
 <a name="cpp">
 </a>
</p>
<h2>
 C++
</h2>
<p>
 <a name="cpp-cv">
 </a>
</p>
<h4>
 Computer Vision
</h4>
<ul>
 <li>
  <a href="http://opencv.org">
   OpenCV
  </a>
  - OpenCV has C++, C, Python, Java and MATLAB interfaces and supports Windows, Linux, Android and Mac OS.
 </li>
 <li>
  <a href="http://dlib.net/imaging.html">
   DLib
  </a>
  - DLib has C++ and Python interfaces for face detection and training general object detectors.
 </li>
 <li>
  <a href="http://eblearn.sourceforge.net/">
   EBLearn
  </a>
  - Eblearn is an object-oriented C++ library that implements various machine learning models
 </li>
 <li>
  <a href="https://github.com/ukoethe/vigra">
   VIGRA
  </a>
  - VIGRA is a generic cross-platform C++ computer vision and machine learning library for volumes of arbitrary dimensionality with Python bindings.
  <sup>
   377 GitHub links in total 753 links, &#9733 189, pushed 2 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="cpp-general-purpose">
 </a>
</p>
<h4>
 General-Purpose Machine Learning
</h4>
<ul>
 <li>
  <a href="http://www.mlpack.org/">
   mlpack
  </a>
  - A scalable C++ machine learning library
 </li>
 <li>
  <a href="http://dlib.net/ml.html">
   DLib
  </a>
  - A suite of ML tools designed to be easy to imbed in other applications
 </li>
 <li>
  <a href="https://code.google.com/p/encog-cpp/">
   encog-cpp
  </a>
 </li>
 <li>
  <a href="http://image.diku.dk/shark/sphinx_pages/build/html/index.html">
   shark
  </a>
 </li>
 <li>
  <a href="https://github.com/JohnLangford/vowpal_wabbit/wiki">
   Vowpal Wabbit (VW)
  </a>
  - A fast out-of-core learning system.
 </li>
 <li>
  <a href="https://code.google.com/p/sofia-ml/">
   sofia-ml
  </a>
  - Suite of fast incremental algorithms.
 </li>
 <li>
  <a href="https://github.com/shogun-toolbox/shogun">
   Shogun
  </a>
  - The Shogun Machine Learning Toolbox
  <sup>
   377 GitHub links in total 753 links, &#9733 1048, pushed 7 days ago
  </sup>
 </li>
 <li>
  <a href="http://caffe.berkeleyvision.org">
   Caffe
  </a>
  - A deep learning framework developed with cleanliness, readability, and speed in mind. [DEEP LEARNING]
 </li>
 <li>
  <a href="https://github.com/antinucleon/cxxnet">
   CXXNET
  </a>
  - Yet another deep learning framework with less than 1000 lines core code [DEEP LEARNING]
  <sup>
   377 GitHub links in total 753 links, &#9733 23, pushed 202 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/dmlc/xgboost">
   XGBoost
  </a>
  - A parallelized optimized general purpose gradient boosting library.
  <sup>
   377 GitHub links in total 753 links, &#9733 3203, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://code.google.com/p/cuda-convnet/">
   CUDA
  </a>
  - This is a fast C++/CUDA implementation of convolutional [DEEP LEARNING]
 </li>
 <li>
  <a href="http://mc-stan.org/">
   Stan
  </a>
  - A probabilistic programming language implementing full Bayesian statistical inference with Hamiltonian Monte Carlo sampling
 </li>
 <li>
  <a href="https://github.com/jkomiyama/banditlib">
   BanditLib
  </a>
  - A simple Multi-armed Bandit library.
  <sup>
   377 GitHub links in total 753 links, &#9733 24, pushed 312 days ago
  </sup>
 </li>
 <li>
  <a href="http://ilk.uvt.nl/timbl/">
   Timbl
  </a>
  - A software package/C++ library implementing several memory-based learning algorithms, among which IB1-IG, an implementation of k-nearest neighbor classification, and IGTree, a decision-tree approximation of IB1-IG. Commonly used for NLP.
 </li>
 <li>
  <a href="http://www.dmtk.io/">
   Disrtibuted Machine learning Tool Kit (DMTK)
  </a>
  - A distributed machine learning (parameter server) framework by Microsoft. Enables training models on large data sets across multiple machines. Current tools bundled with it include: LightLDA and Distributed (Multisense) Word Embedding.
 </li>
 <li>
  <a href="http://igraph.org/c/">
   igraph
  </a>
  - General purpose graph library
 </li>
 <li>
  <a href="https://github.com/baidu-research/warp-ctc">
   Warp-CTC
  </a>
  - A fast parallel implementation of Connectionist Temporal Classification (CTC), on both CPU and GPU.
  <sup>
   377 GitHub links in total 753 links, &#9733 2234, pushed 102 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Microsoft/CNTK">
   CNTK
  </a>
  - The Computational Network Toolkit (CNTK) by Microsoft Research, is a unified deep-learning toolkit that describes neural networks as a series of computational steps via a directed graph.
  <sup>
   377 GitHub links in total 753 links, &#9733 5304, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/beniz/deepdetect">
   DeepDetect
  </a>
  - A machine learning API and server written in C++11. It makes state of the art machine learning easy to work with and integrate into existing applications.
  <sup>
   377 GitHub links in total 753 links, &#9733 548, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/FidoProject/Fido">
   Fido
  </a>
  - A highly-modular C++ machine learning library for embedded electronics and robotics.
  <sup>
   377 GitHub links in total 753 links, &#9733 15, pushed 1 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="cpp-nlp">
 </a>
</p>
<h4>
 Natural Language Processing
</h4>
<ul>
 <li>
  <a href="https://github.com/mit-nlp/MITIE">
   MIT Information Extraction Toolkit
  </a>
  - C, C++, and Python tools for named entity recognition and relation extraction
  <sup>
   377 GitHub links in total 753 links, &#9733 898, pushed 28 days ago
  </sup>
 </li>
 <li>
  <a href="https://taku910.github.io/crfpp/">
   CRF++
  </a>
  - Open source implementation of Conditional Random Fields (CRFs) for segmenting/labeling sequential data & other Natural Language Processing tasks.
 </li>
 <li>
  <a href="http://www.chokkan.org/software/crfsuite/">
   CRFsuite
  </a>
  - CRFsuite is an implementation of Conditional Random Fields (CRFs) for labeling sequential data.
 </li>
 <li>
  <a href="https://github.com/BLLIP/bllip-parser">
   BLLIP Parser
  </a>
  - BLLIP Natural Language Parser (also known as the Charniak-Johnson parser)
  <sup>
   377 GitHub links in total 753 links, &#9733 104, pushed 80 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/proycon/colibri-core">
   colibri-core
  </a>
  - C++ library, command line tools, and Python binding for extracting and working with basic linguistic constructions such as n-grams and skipgrams in a quick and memory-efficient way.
  <sup>
   377 GitHub links in total 753 links, &#9733 40, pushed 8 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/proycon/ucto">
   ucto
  </a>
  - Unicode-aware regular-expression based tokenizer for various languages. Tool and C++ library. Supports FoLiA format.
 </li>
 <li>
  <a href="https://github.com/proycon/libfolia">
   libfolia
  </a>
  - C++ library for the
  <a href="http://proycon.github.io/folia/">
   FoLiA format
  </a>
 </li>
 <li>
  <a href="https://github.com/proycon/frog">
   frog
  </a>
  - Memory-based NLP suite developed for Dutch: PoS tagger, lemmatiser, dependency parser, NER, shallow parser, morphological analyzer.
 </li>
 <li>
  <a href="https://github.com/meta-toolkit/meta">
   MeTA
  </a>
  -
  <a href="https://meta-toolkit.org/">
   MeTA : ModErn Text Analysis
  </a>
  is a C++ Data Sciences Toolkit that facilitates mining big text data.
  <sup>
   377 GitHub links in total 753 links, &#9733 227, pushed 11 days ago
  </sup>
 </li>
</ul>
<h4>
 Speech Recognition
</h4>
<ul>
 <li>
  <a href="http://kaldi.sourceforge.net/">
   Kaldi
  </a>
  - Kaldi is a toolkit for speech recognition written in C++ and licensed under the Apache License v2.0. Kaldi is intended for use by speech recognition researchers.
 </li>
</ul>
<p>
 <a name="cpp-sequence">
 </a>
</p>
<h4>
 Sequence Analysis
</h4>
<ul>
 <li>
  <a href="https://github.com/ayoshiaki/tops">
   ToPS
  </a>
  - This is an objected-oriented framework that facilitates the integration of probabilistic models for sequences over a user defined alphabet.
  <sup>
   377 GitHub links in total 753 links, &#9733 13, pushed 272 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="cpp-gestures">
 </a>
</p>
<h4>
 Gesture Detection
</h4>
<ul>
 <li>
  <a href="https://github.com/nickgillian/grt">
   grt
  </a>
  - The Gesture Recognition Toolkit (GRT) is a cross-platform, open-source, C++ machine learning library designed for real-time gesture recognition.
  <sup>
   377 GitHub links in total 753 links, &#9733 196, pushed 10 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="common-lisp">
 </a>
</p>
<h2>
 Common Lisp
</h2>
<p>
 <a name="common-lisp-general-purpose">
 </a>
</p>
<h4>
 General-Purpose Machine Learning
</h4>
<ul>
 <li>
  <a href="https://github.com/melisgl/mgl/">
   mgl
  </a>
  - Neural networks  (boltzmann machines, feed-forward and recurrent nets), Gaussian Processes
 </li>
 <li>
  <a href="https://github.com/melisgl/mgl-gpr/">
   mgl-gpr
  </a>
  - Evolutionary algorithms
 </li>
 <li>
  <a href="https://github.com/melisgl/cl-libsvm/">
   cl-libsvm
  </a>
  - Wrapper for the libsvm support vector machine library
 </li>
</ul>
<p>
 <a name="clojure">
 </a>
</p>
<h2>
 Clojure
</h2>
<p>
 <a name="clojure-nlp">
 </a>
</p>
<h4>
 Natural Language Processing
</h4>
<ul>
 <li>
  <a href="https://github.com/dakrone/clojure-opennlp">
   Clojure-openNLP
  </a>
  - Natural Language Processing in Clojure (opennlp)
  <sup>
   377 GitHub links in total 753 links, &#9733 551, pushed 8 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/r0man/inflections-clj">
   Infections-clj
  </a>
  - Rails-like inflection library for Clojure and ClojureScript
  <sup>
   377 GitHub links in total 753 links, &#9733 119, pushed 48 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="clojure-general-purpose">
 </a>
</p>
<h4>
 General-Purpose Machine Learning
</h4>
<ul>
 <li>
  <a href="https://github.com/ptaoussanis/touchstone">
   Touchstone
  </a>
  - Clojure A/B testing library
  <sup>
   377 GitHub links in total 753 links, &#9733 97, pushed 53 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/lspector/Clojush">
   Clojush
  </a>
  -  The Push programming language and the PushGP genetic programming system implemented in Clojure
  <sup>
   377 GitHub links in total 753 links, &#9733 170, pushed 10 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/aria42/infer">
   Infer
  </a>
  - Inference and machine learning in clojure
  <sup>
   377 GitHub links in total 753 links, &#9733 147, pushed 126 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/antoniogarrote/clj-ml">
   Clj-ML
  </a>
  - A machine learning library for Clojure built on top of Weka and friends
  <sup>
   377 GitHub links in total 753 links, &#9733 108, pushed 71 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jimpil/enclog">
   Encog
  </a>
  - Clojure wrapper for Encog (v3) (Machine-Learning framework that specializes in neural-nets)
  <sup>
   377 GitHub links in total 753 links, &#9733 118, pushed 745 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/vollmerm/fungp">
   Fungp
  </a>
  - A genetic programming library for Clojure
  <sup>
   377 GitHub links in total 753 links, &#9733 77, pushed 715 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/clojurewerkz/statistiker">
   Statistiker
  </a>
  - Basic Machine Learning algorithms in Clojure.
  <sup>
   377 GitHub links in total 753 links, &#9733 42, pushed 302 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/nupic-community/clortex">
   clortex
  </a>
  - General Machine Learning library using Numenta’s Cortical Learning Algorithm
  <sup>
   377 GitHub links in total 753 links, &#9733 151, pushed 153 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/nupic-community/comportex">
   comportex
  </a>
  - Functionally composable Machine Learning library using Numenta’s Cortical Learning Algorithm
  <sup>
   377 GitHub links in total 753 links, &#9733 92, pushed 2 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="clojure-data-analysis">
 </a>
</p>
<h4>
 Data Analysis / Data Visualization
</h4>
<ul>
 <li>
  <a href="http://incanter.org/">
   Incanter
  </a>
  - Incanter is a Clojure-based, R-like platform for statistical computing and graphics.
 </li>
 <li>
  <a href="https://github.com/Netflix/PigPen">
   PigPen
  </a>
  - Map-Reduce for Clojure.
  <sup>
   377 GitHub links in total 753 links, &#9733 419, pushed 8 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/clojurewerkz/envision">
   Envision
  </a>
  - Clojure Data Visualisation library, based on Statistiker and D3
  <sup>
   377 GitHub links in total 753 links, &#9733 45, pushed 443 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="erlang">
 </a>
</p>
<h2>
 Erlang
</h2>
<p>
 <a name="erlang-general-purpose">
 </a>
</p>
<h4>
 General-Purpose Machine Learning
</h4>
<ul>
 <li>
  <a href="https://github.com/discoproject/disco/">
   Disco
  </a>
  - Map Reduce in Erlang
 </li>
</ul>
<p>
 <a name="go">
 </a>
</p>
<h2>
 Go
</h2>
<p>
 <a name="go-nlp">
 </a>
</p>
<h4>
 Natural Language Processing
</h4>
<ul>
 <li>
  <a href="https://github.com/reiver/go-porterstemmer">
   go-porterstemmer
  </a>
  - A native Go clean room implementation of the Porter Stemming algorithm.
  <sup>
   377 GitHub links in total 753 links, &#9733 98, pushed 21 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Rookii/paicehusk">
   paicehusk
  </a>
  - Golang implementation of the Paice/Husk Stemming Algorithm.
  <sup>
   377 GitHub links in total 753 links, &#9733 13, pushed 869 days ago
  </sup>
 </li>
 <li>
  <a href="https://bitbucket.org/tebeka/snowball">
   snowball
  </a>
  - Snowball Stemmer for Go.
 </li>
 <li>
  <a href="https://github.com/Lazin/go-ngram">
   go-ngram
  </a>
  - In-memory n-gram index with compression.
  <sup>
   377 GitHub links in total 753 links, &#9733 55, pushed 43 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="go-general-purpose">
 </a>
</p>
<h4>
 General-Purpose Machine Learning
</h4>
<ul>
 <li>
  <a href="https://github.com/sjwhitworth/golearn">
   Go Learn
  </a>
  - Machine Learning for Go
  <sup>
   377 GitHub links in total 753 links, &#9733 2746, pushed 0 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/daviddengcn/go-pr">
   go-pr
  </a>
  - Pattern recognition package in Go lang.
  <sup>
   377 GitHub links in total 753 links, &#9733 36, pushed 1060 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/alonsovidales/go_ml">
   go-ml
  </a>
  - Linear / Logistic regression, Neural Networks, Collaborative Filtering and Gaussian Multivariate Distribution
  <sup>
   377 GitHub links in total 753 links, &#9733 82, pushed 468 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jbrukh/bayesian">
   bayesian
  </a>
  - Naive Bayesian Classification for Golang.
  <sup>
   377 GitHub links in total 753 links, &#9733 305, pushed 38 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/thoj/go-galib">
   go-galib
  </a>
  - Genetic Algorithms library written in Go / golang
  <sup>
   377 GitHub links in total 753 links, &#9733 120, pushed 127 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/ryanbressler/CloudForest">
   Cloudforest
  </a>
  - Ensembles of decision trees in go/golang.
  <sup>
   377 GitHub links in total 753 links, &#9733 348, pushed 64 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/goml/gobrain">
   gobrain
  </a>
  - Neural Networks written in go
  <sup>
   377 GitHub links in total 753 links, &#9733 85, pushed 261 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/fxsjy/gonn">
   GoNN
  </a>
  - GoNN is an implementation of Neural Network in Go Language, which includes BPNN, RBF, PCN
  <sup>
   377 GitHub links in total 753 links, &#9733 181, pushed 95 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/dmlc/mxnet">
   MXNet
  </a>
  - Lightweight, Portable, Flexible Distributed/Mobile Deep Learning with Dynamic, Mutation-aware Dataflow Dep Scheduler; for Python, R, Julia, Go, Javascript and more.
  <sup>
   377 GitHub links in total 753 links, &#9733 3543, pushed 2 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="go-data-analysis">
 </a>
</p>
<h4>
 Data Analysis / Data Visualization
</h4>
<ul>
 <li>
  <a href="https://github.com/StepLg/go-graph">
   go-graph
  </a>
  - Graph library for Go/golang language.
  <sup>
   377 GitHub links in total 753 links, &#9733 59, pushed 178 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.svgopen.org/2011/papers/34-SVGo_a_Go_Library_for_SVG_generation/">
   SVGo
  </a>
  - The Go Language library for SVG generation
 </li>
 <li>
  <a href="https://github.com/fxsjy/RF.go">
   RF
  </a>
  - Random forests implementation in Go
  <sup>
   377 GitHub links in total 753 links, &#9733 57, pushed 663 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="haskell">
 </a>
</p>
<h2>
 Haskell
</h2>
<p>
 <a name="haskell-general-purpose">
 </a>
</p>
<h4>
 General-Purpose Machine Learning
</h4>
<ul>
 <li>
  <a href="https://github.com/ajtulloch/haskell-ml">
   haskell-ml
  </a>
  - Haskell implementations of various ML algorithms.
  <sup>
   377 GitHub links in total 753 links, &#9733 26, pushed 705 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/mikeizbicki/HLearn">
   HLearn
  </a>
  - a suite of libraries for interpreting machine learning models according to their algebraic structure.
  <sup>
   377 GitHub links in total 753 links, &#9733 921, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="https://wiki.haskell.org/HNN">
   hnn
  </a>
  - Haskell Neural Network library.
 </li>
 <li>
  <a href="https://github.com/ajtulloch/hopfield-networks">
   hopfield-networks
  </a>
  - Hopfield Networks for unsupervised learning in Haskell.
  <sup>
   377 GitHub links in total 753 links, &#9733 9, pushed 751 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/ajtulloch/dnngraph">
   caffegraph
  </a>
  - A DSL for deep neural networks
  <sup>
   377 GitHub links in total 753 links, &#9733 468, pushed 148 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jbarrow/LambdaNet">
   LambdaNet
  </a>
  - Configurable Neural Networks in Haskell
  <sup>
   377 GitHub links in total 753 links, &#9733 268, pushed 39 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="java">
 </a>
</p>
<h2>
 Java
</h2>
<p>
 <a name="java-nlp">
 </a>
</p>
<h4>
 Natural Language Processing
</h4>
<ul>
 <li>
  <a href="http://www.cortical.io/">
   Cortical.io
  </a>
  - Retina: an API performing complex NLP operations (disambiguation, classification, streaming text filtering, etc...) as quickly and intuitively as the brain.
 </li>
 <li>
  <a href="http://nlp.stanford.edu/software/corenlp.shtml">
   CoreNLP
  </a>
  - Stanford CoreNLP provides a set of natural language analysis tools which can take raw English language text input and give the base forms of words
 </li>
 <li>
  <a href="http://nlp.stanford.edu/software/lex-parser.shtml">
   Stanford Parser
  </a>
  - A natural language parser is a program that works out the grammatical structure of sentences
 </li>
 <li>
  <a href="http://nlp.stanford.edu/software/tagger.shtml">
   Stanford POS Tagger
  </a>
  - A Part-Of-Speech Tagger (POS Tagger
 </li>
 <li>
  <a href="http://nlp.stanford.edu/software/CRF-NER.shtml">
   Stanford Name Entity Recognizer
  </a>
  - Stanford NER is a Java implementation of a Named Entity Recognizer.
 </li>
 <li>
  <a href="http://nlp.stanford.edu/software/segmenter.shtml">
   Stanford Word Segmenter
  </a>
  - Tokenization of raw text is a standard pre-processing step for many NLP tasks.
 </li>
 <li>
  <a href="http://nlp.stanford.edu/software/tregex.shtml">
   Tregex, Tsurgeon and Semgrex
  </a>
  - Tregex is a utility for matching patterns in trees, based on tree relationships and regular expression matches on nodes (the name is short for "tree regular expressions").
 </li>
 <li>
  <a href="http://nlp.stanford.edu/software/phrasal/">
   Stanford Phrasal: A Phrase-Based Translation System
  </a>
 </li>
 <li>
  <a href="http://nlp.stanford.edu/software/tokenizer.shtml">
   Stanford English Tokenizer
  </a>
  - Stanford Phrasal is a state-of-the-art statistical phrase-based machine translation system, written in Java.
 </li>
 <li>
  <a href="http://nlp.stanford.edu/software/tokensregex.shtml">
   Stanford Tokens Regex
  </a>
  - A tokenizer divides text into a sequence of tokens, which roughly correspond to "words"
 </li>
 <li>
  <a href="http://nlp.stanford.edu/software/sutime.shtml">
   Stanford Temporal Tagger
  </a>
  - SUTime is a library for recognizing and normalizing time expressions.
 </li>
 <li>
  <a href="http://nlp.stanford.edu/software/patternslearning.shtml">
   Stanford SPIED
  </a>
  - Learning entities from unlabeled text starting with seed sets using patterns in an iterative fashion
 </li>
 <li>
  <a href="http://nlp.stanford.edu/software/tmt/tmt-0.4/">
   Stanford Topic Modeling Toolbox
  </a>
  - Topic modeling tools to social scientists and others who wish to perform analysis on datasets
 </li>
 <li>
  <a href="https://github.com/twitter/twitter-text-java">
   Twitter Text Java
  </a>
  - A Java implementation of Twitter's text processing library
  <sup>
   377 GitHub links in total 753 links, &#9733 374, pushed 507 days ago
  </sup>
 </li>
 <li>
  <a href="http://mallet.cs.umass.edu/">
   MALLET
  </a>
  - A Java-based package for statistical natural language processing, document classification, clustering, topic modeling, information extraction, and other machine learning applications to text.
 </li>
 <li>
  <a href="https://opennlp.apache.org/">
   OpenNLP
  </a>
  - a machine learning based toolkit for the processing of natural language text.
 </li>
 <li>
  <a href="http://alias-i.com/lingpipe/index.html">
   LingPipe
  </a>
  - A tool kit for processing text using computational linguistics.
 </li>
 <li>
  <a href="https://code.google.com/p/cleartk/">
   ClearTK
  </a>
  - ClearTK provides a framework for developing statistical natural language processing (NLP) components in Java and is built on top of Apache UIMA.
 </li>
 <li>
  <a href="http://ctakes.apache.org/">
   Apache cTAKES
  </a>
  - Apache clinical Text Analysis and Knowledge Extraction System (cTAKES) is an open-source natural language processing system for information extraction from electronic medical record clinical free-text.
 </li>
 <li>
  <a href="http://www.clearnlp.com">
   ClearNLP
  </a>
  - The ClearNLP project provides software and resources for natural language processing. The project started at the Center for Computational Language and EducAtion Research, and is currently developed by the Center for Language and Information Research at Emory University. This project is under the Apache 2 license.
 </li>
</ul>
<p>
 <a name="java-general-purpose">
 </a>
</p>
<h4>
 General-Purpose Machine Learning
</h4>
<ul>
 <li>
  <a href="https://github.com/airbnb/aerosolve">
   aerosolve
  </a>
  - A machine learning library by Airbnb designed from the ground up to be human friendly.
  <sup>
   377 GitHub links in total 753 links, &#9733 2955, pushed 0 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/datumbox/datumbox-framework">
   Datumbox
  </a>
  - Machine Learning framework for rapid development of Machine Learning and Statistical applications
  <sup>
   377 GitHub links in total 753 links, &#9733 685, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="http://elki.dbs.ifi.lmu.de/">
   ELKI
  </a>
  - Java toolkit for data mining. (unsupervised: clustering, outlier detection etc.)
 </li>
 <li>
  <a href="https://github.com/encog/encog-java-core">
   Encog
  </a>
  - An advanced neural network and machine learning framework. Encog contains classes to create a wide variety of networks, as well as support classes to normalize and process data for these neural networks. Encog trains using multithreaded resilient propagation. Encog can also make use of a GPU to further speed processing time. A GUI based workbench is also provided to help model and train neural networks.
  <sup>
   377 GitHub links in total 753 links, &#9733 489, pushed 12 days ago
  </sup>
 </li>
 <li>
  <a href="www.ra.cs.uni-tuebingen.de/software/eva2/">
   EvA2
  </a>
  - Evolutionary Algorithms Framework with Genetic Algorithm, Differential Evolution, Particle Swarm Optimization, Evolution Strategies, Covariance Matrix Adaptation Evolution Strategy, and more
 </li>
 <li>
  <a href="https://ci.apache.org/projects/flink/flink-docs-master/apis/batch/libs/ml/index.html">
   FlinkML in Apache Flink
  </a>
  - Distributed machine learning library in Flink
 </li>
 <li>
  <a href="https://github.com/h2oai/h2o-3">
   H2O
  </a>
  - ML engine that supports distributed learning on Hadoop, Spark or your laptop via APIs in R, Python, Scala, REST/JSON.
  <sup>
   377 GitHub links in total 753 links, &#9733 1021, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/numenta/htm.java">
   htm.java
  </a>
  - General Machine Learning library using Numenta’s Cortical Learning Algorithm
  <sup>
   377 GitHub links in total 753 links, &#9733 152, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/deeplearning4j/deeplearning4j">
   java-deeplearning
  </a>
  - Distributed Deep Learning Platform for Java, Clojure,Scala
  <sup>
   377 GitHub links in total 753 links, &#9733 2626, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="http://java-ml.sourceforge.net/">
   JAVA-ML
  </a>
  - A general ML library with a common interface for all algorithms in Java
 </li>
 <li>
  <a href="https://code.google.com/p/java-statistical-analysis-tool/">
   JSAT
  </a>
  - Numerous Machine Learning algorithms for classification, regression, and  clustering.
 </li>
 <li>
  <a href="https://github.com/apache/mahout">
   Mahout
  </a>
  - Distributed machine learning
  <sup>
   377 GitHub links in total 753 links, &#9733 791, pushed 0 days ago
  </sup>
 </li>
 <li>
  <a href="http://meka.sourceforge.net/">
   Meka
  </a>
  - An open source implementation of methods for multi-label classification and evaluation (extension to Weka).
 </li>
 <li>
  <a href="http://spark.apache.org/docs/latest/mllib-guide.html">
   MLlib in Apache Spark
  </a>
  - Distributed machine learning library in Spark
 </li>
 <li>
  <a href="http://neuroph.sourceforge.net/">
   Neuroph
  </a>
  - Neuroph is lightweight Java neural network framework
 </li>
 <li>
  <a href="https://github.com/oryxproject/oryx">
   ORYX
  </a>
  - Lambda Architecture Framework using Apache Spark and Apache Kafka with a specialization for real-time large-scale machine learning.
  <sup>
   377 GitHub links in total 753 links, &#9733 777, pushed 9 days ago
  </sup>
 </li>
 <li>
  <a href="https://samoa.incubator.apache.org/">
   Samoa
  </a>
  SAMOA is a framework that includes distributed machine learning for data streams with an interface to plug-in different stream processing platforms.
 </li>
 <li>
  <a href="http://sourceforge.net/p/lemur/wiki/RankLib/">
   RankLib
  </a>
  - RankLib is a library of learning to rank algorithms
 </li>
 <li>
  <a href="https://github.com/padreati/rapaio">
   rapaio
  </a>
  - statistics, data mining and machine learning toolbox in Java
  <sup>
   377 GitHub links in total 753 links, &#9733 15, pushed 14 days ago
  </sup>
 </li>
 <li>
  <a href="http://rapid-i.com/wiki/index.php?title=Integrating_RapidMiner_into_your_application">
   RapidMiner
  </a>
  - RapidMiner integration into Java code
 </li>
 <li>
  <a href="http://nlp.stanford.edu/software/classifier.shtml">
   Stanford Classifier
  </a>
  - A classifier is a machine learning tool that will take data items and place them into one of k classes.
 </li>
 <li>
  <a href="https://github.com/haifengl/smile">
   SmileMiner
  </a>
  - Statistical Machine Intelligence & Learning Engine
  <sup>
   377 GitHub links in total 753 links, &#9733 2512, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/apache/incubator-systemml">
   SystemML
  </a>
  - flexible, scalable machine learning (ML) language.
  <sup>
   377 GitHub links in total 753 links, &#9733 267, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/WalnutiQ/WalnutiQ">
   WalnutiQ
  </a>
  - object oriented model of the human brain
 </li>
 <li>
  <a href="http://www.cs.waikato.ac.nz/ml/weka/">
   Weka
  </a>
  - Weka is a collection of machine learning algorithms for data mining tasks
 </li>
</ul>
<h4>
 Speech Recognition
</h4>
<ul>
 <li>
  <a href="http://cmusphinx.sourceforge.net/">
   CMU Sphinx
  </a>
  - Open Source Toolkit For Speech Recognition purely based on Java speech recognition library.
 </li>
</ul>
<p>
 <a name="java-data-analysis">
 </a>
</p>
<h4>
 Data Analysis / Data Visualization
</h4>
<ul>
 <li>
  <a href="http://flink.apache.org/">
   Flink
  </a>
  - Open source platform for distributed stream and batch data processing.
 </li>
 <li>
  <a href="https://github.com/apache/hadoop-mapreduce">
   Hadoop
  </a>
  - Hadoop/HDFS
  <sup>
   377 GitHub links in total 753 links, &#9733 21, pushed 339 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/apache/spark">
   Spark
  </a>
  - Spark is a fast and general engine for large-scale data processing.
  <sup>
   377 GitHub links in total 753 links, &#9733 8374, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="http://storm.apache.org/">
   Storm
  </a>
  - Storm is a distributed realtime computation system.
 </li>
 <li>
  <a href="https://github.com/cloudera/impala">
   Impala
  </a>
  - Real-time Query for Hadoop
  <sup>
   377 GitHub links in total 753 links, &#9733 1560, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="http://jwork.org/dmelt/">
   DataMelt
  </a>
  - Mathematics software for numeric computation, statistics, symbolic calculations, data analysis and data visualization.
 </li>
 <li>
  <a href="http://www.ee.ucl.ac.uk/~mflanaga/java/">
   Dr. Michael Thomas Flanagan's Java Scientific Library
  </a>
 </li>
</ul>
<p>
 <a name="java-deep-learning">
 </a>
</p>
<h4>
 Deep Learning
</h4>
<ul>
 <li>
  <a href="https://github.com/deeplearning4j/deeplearning4j">
   Deeplearning4j
  </a>
  - Scalable deep learning for industry with parallel GPUs
  <sup>
   377 GitHub links in total 753 links, &#9733 2626, pushed 2 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="javascript">
 </a>
</p>
<h2>
 Javascript
</h2>
<p>
 <a name="javascript-nlp">
 </a>
</p>
<h4>
 Natural Language Processing
</h4>
<ul>
 <li>
  <a href="https://github.com/twitter/twitter-text">
   Twitter-text
  </a>
  - A JavaScript implementation of Twitter's text processing library
  <sup>
   377 GitHub links in total 753 links, &#9733 1134, pushed 42 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/nicktesla/nlpjs">
   NLP.js
  </a>
  - NLP utilities in javascript and coffeescript
  <sup>
   377 GitHub links in total 753 links, &#9733 28, pushed 885 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/NaturalNode/natural">
   natural
  </a>
  - General natural language facilities for node
  <sup>
   377 GitHub links in total 753 links, &#9733 4656, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/loadfive/Knwl.js">
   Knwl.js
  </a>
  - A Natural Language Processor in JS
  <sup>
   377 GitHub links in total 753 links, &#9733 5076, pushed 27 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/wooorm/retext">
   Retext
  </a>
  - Extensible system for analyzing and manipulating natural language
  <sup>
   377 GitHub links in total 753 links, &#9733 830, pushed 49 days ago
  </sup>
 </li>
 <li>
  <a href="https://www.mashape.com/japerk/text-processing/support">
   TextProcessing
  </a>
  - Sentiment analysis, stemming and lemmatization, part-of-speech tagging and chunking, phrase extraction and named entity recognition.
 </li>
 <li>
  <a href="https://github.com/spencermountain/nlp_compromise">
   NLP Compromise
  </a>
  - Natural Language processing in the browser
 </li>
</ul>
<p>
 <a name="javascript-data-analysis">
 </a>
</p>
<h4>
 Data Analysis / Data Visualization
</h4>
<ul>
 <li>
  <a href="http://d3js.org/">
   D3.js
  </a>
 </li>
 <li>
  <a href="http://www.highcharts.com/">
   High Charts
  </a>
 </li>
 <li>
  <a href="http://nvd3.org/">
   NVD3.js
  </a>
 </li>
 <li>
  <a href="http://dc-js.github.io/dc.js/">
   dc.js
  </a>
 </li>
 <li>
  <a href="http://www.chartjs.org/">
   chartjs
  </a>
 </li>
 <li>
  <a href="http://dimplejs.org/">
   dimple
  </a>
 </li>
 <li>
  <a href="http://www.amcharts.com/">
   amCharts
  </a>
 </li>
 <li>
  <a href="https://github.com/NathanEpstein/D3xter">
   D3xter
  </a>
  - Straight forward plotting built on D3
  <sup>
   377 GitHub links in total 753 links, &#9733 340, pushed 48 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/rigtorp/statkit">
   statkit
  </a>
  - Statistics kit for JavaScript
  <sup>
   377 GitHub links in total 753 links, &#9733 26, pushed 517 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/nathanepstein/datakit">
   datakit
  </a>
  - A lightweight framework for data analysis in JavaScript
  <sup>
   377 GitHub links in total 753 links, &#9733 272, pushed 204 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jasondavies/science.js/">
   science.js
  </a>
  - Scientific and statistical computing in JavaScript.
 </li>
 <li>
  <a href="https://github.com/NathanEpstein/Z3d">
   Z3d
  </a>
  - Easily make interactive 3d plots built on Three.js
  <sup>
   377 GitHub links in total 753 links, &#9733 80, pushed 481 days ago
  </sup>
 </li>
 <li>
  <a href="http://sigmajs.org/">
   Sigma.js
  </a>
  - JavaScript library dedicated to graph drawing.
 </li>
 <li>
  <a href="http://c3js.org/">
   C3.js
  </a>
  - customizable library based on D3.js for easy chart drawing.
 </li>
 <li>
  <a href="http://www.zingchart.com/">
   ZingChart
  </a>
  - library written on Vanilla JS for big data visualization.
 </li>
 <li>
  <a href="http://www.cheminfo.org/">
   cheminfo
  </a>
  - Platform for data visualization and analysis, using the
  <a href="https://github.com/npellet/visualizer">
   visualizer
  </a>
  project.
 </li>
</ul>
<p>
 <a name="javascript-general-purpose">
 </a>
</p>
<h4>
 General-Purpose Machine Learning
</h4>
<ul>
 <li>
  <a href="http://cs.stanford.edu/people/karpathy/convnetjs/">
   Convnet.js
  </a>
  - ConvNetJS is a Javascript library for training Deep Learning models[DEEP LEARNING]
 </li>
 <li>
  <a href="http://harthur.github.io/clusterfck/">
   Clusterfck
  </a>
  - Agglomerative hierarchical clustering implemented in Javascript for Node.js and the browser
 </li>
 <li>
  <a href="https://github.com/emilbayes/clustering.js">
   Clustering.js
  </a>
  - Clustering algorithms implemented in Javascript for Node.js and the browser
  <sup>
   377 GitHub links in total 753 links, &#9733 20, pushed 655 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/serendipious/nodejs-decision-tree-id3">
   Decision Trees
  </a>
  - NodeJS Implementation of Decision Tree using ID3 Algorithm
  <sup>
   377 GitHub links in total 753 links, &#9733 84, pushed 134 days ago
  </sup>
 </li>
 <li>
  <a href="http://code.google.com/p/figue/">
   figue
  </a>
  - K-means, fuzzy c-means and agglomerative clustering
 </li>
 <li>
  <a href="https://github.com/rlidwka/node-fann">
   Node-fann
  </a>
  - FANN (Fast Artificial Neural Network Library) bindings for Node.js
  <sup>
   377 GitHub links in total 753 links, &#9733 136, pushed 155 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/emilbayes/kMeans.js">
   Kmeans.js
  </a>
  - Simple Javascript implementation of the k-means algorithm, for node.js and the browser
  <sup>
   377 GitHub links in total 753 links, &#9733 24, pushed 1008 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/primaryobjects/lda">
   LDA.js
  </a>
  - LDA topic modeling for node.js
  <sup>
   377 GitHub links in total 753 links, &#9733 96, pushed 82 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/yandongliu/learningjs">
   Learning.js
  </a>
  - Javascript implementation of logistic regression/c4.5 decision tree
  <sup>
   377 GitHub links in total 753 links, &#9733 27, pushed 720 days ago
  </sup>
 </li>
 <li>
  <a href="http://joonku.com/project/machine_learning">
   Machine Learning
  </a>
  - Machine learning library for Node.js
 </li>
 <li>
  <a href="https://github.com/mil-tokyo">
   mil-tokyo
  </a>
  - List of several machine learning libraries
 </li>
 <li>
  <a href="https://github.com/nicolaspanel/node-svm">
   Node-SVM
  </a>
  - Support Vector Machine for nodejs
  <sup>
   377 GitHub links in total 753 links, &#9733 159, pushed 79 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/harthur/brain">
   Brain
  </a>
  - Neural networks in JavaScript
  <strong>
   [Deprecated]
  </strong>
  <sup>
   377 GitHub links in total 753 links, &#9733 6952, pushed 186 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/omphalos/bayesian-bandit.js">
   Bayesian-Bandit
  </a>
  - Bayesian bandit implementation for Node and the browser.
  <sup>
   377 GitHub links in total 753 links, &#9733 28, pushed 988 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/cazala/synaptic">
   Synaptic
  </a>
  - Architecture-free neural network library for node.js and the browser
  <sup>
   377 GitHub links in total 753 links, &#9733 2155, pushed 39 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/NathanEpstein/kNear">
   kNear
  </a>
  - JavaScript implementation of the k nearest neighbors algorithm for supervised learning
  <sup>
   377 GitHub links in total 753 links, &#9733 25, pushed 524 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/totemstech/neuraln">
   NeuralN
  </a>
  - C++ Neural Network library for Node.js. It has advantage on large dataset and multi-threaded training.
  <sup>
   377 GitHub links in total 753 links, &#9733 257, pushed 309 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/itamarwe/kalman">
   kalman
  </a>
  - Kalman filter for Javascript.
  <sup>
   377 GitHub links in total 753 links, &#9733 70, pushed 241 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/dambalah/shaman">
   shaman
  </a>
  - node.js library with support for both simple and multiple linear regression.
 </li>
 <li>
  <a href="https://github.com/mljs/ml">
   ml.js
  </a>
  - Machine learning and numerical analysis tools for Node.js and the Browser!
  <sup>
   377 GitHub links in total 753 links, &#9733 18, pushed 19 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/NathanEpstein/Pavlov.js">
   Pavlov.js
  </a>
  - Reinforcement learning using Markov Decision Processes
  <sup>
   377 GitHub links in total 753 links, &#9733 436, pushed 124 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/dmlc/mxnet">
   MXNet
  </a>
  - Lightweight, Portable, Flexible Distributed/Mobile Deep Learning with Dynamic, Mutation-aware Dataflow Dep Scheduler; for Python, R, Julia, Go, Javascript and more.
 </li>
</ul>
<p>
 <a name="javascript-misc">
 </a>
</p>
<h4>
 Misc
</h4>
<ul>
 <li>
  <a href="https://github.com/jcoglan/sylvester">
   sylvester
  </a>
  - Vector and Matrix math for JavaScript.
  <sup>
   377 GitHub links in total 753 links, &#9733 820, pushed 344 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/simple-statistics/simple-statistics">
   simple-statistics
  </a>
  - A JavaScript implementation of descriptive, regression, and inference statistics. Implemented in literate JavaScript with no dependencies, designed to work in all modern browsers (including IE) as well as in node.js.
  <sup>
   377 GitHub links in total 753 links, &#9733 1038, pushed 26 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Tom-Alexander/regression-js">
   regression-js
  </a>
  - A javascript library containing a collection of least squares fitting methods for finding a trend in a set of data.
  <sup>
   377 GitHub links in total 753 links, &#9733 198, pushed 152 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/flurry/Lyric">
   Lyric
  </a>
  - Linear Regression library.
  <sup>
   377 GitHub links in total 753 links, &#9733 39, pushed 951 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/mwgg/GreatCircle">
   GreatCircle
  </a>
  - Library for calculating great circle distance.
  <sup>
   377 GitHub links in total 753 links, &#9733 39, pushed 83 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="julia">
 </a>
</p>
<h2>
 Julia
</h2>
<p>
 <a name="julia-general-purpose">
 </a>
</p>
<h4>
 General-Purpose Machine Learning
</h4>
<ul>
 <li>
  <a href="https://github.com/benhamner/MachineLearning.jl">
   MachineLearning
  </a>
  - Julia Machine Learning library
  <sup>
   377 GitHub links in total 753 links, &#9733 60, pushed 233 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/JuliaStats/MLBase.jl">
   MLBase
  </a>
  - A set of functions to support the development of machine learning algorithms
  <sup>
   377 GitHub links in total 753 links, &#9733 68, pushed 193 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/JuliaStats/PGM.jl">
   PGM
  </a>
  - A Julia framework for probabilistic graphical models.
  <sup>
   377 GitHub links in total 753 links, &#9733 30, pushed 773 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/trthatcher/DiscriminantAnalysis.jl">
   DA
  </a>
  - Julia package for Regularized Discriminant Analysis
  <sup>
   377 GitHub links in total 753 links, &#9733 4, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/lindahua/Regression.jl">
   Regression
  </a>
  - Algorithms for regression analysis (e.g. linear regression and logistic regression)
  <sup>
   377 GitHub links in total 753 links, &#9733 31, pushed 190 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/dcjones/Loess.jl">
   Local Regression
  </a>
  - Local regression, so smooooth!
  <sup>
   377 GitHub links in total 753 links, &#9733 8, pushed 29 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/nutsiepully/NaiveBayes.jl">
   Naive Bayes
  </a>
  - Simple Naive Bayes implementation in Julia
  <sup>
   377 GitHub links in total 753 links, &#9733 3, pushed 1065 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/dmbates/MixedModels.jl">
   Mixed Models
  </a>
  - A Julia package for fitting (statistical) mixed-effects models
  <sup>
   377 GitHub links in total 753 links, &#9733 58, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/fredo-dedup/SimpleMCMC.jl">
   Simple MCMC
  </a>
  - basic mcmc sampler implemented in Julia
  <sup>
   377 GitHub links in total 753 links, &#9733 10, pushed 1037 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/JuliaStats/Distance.jl">
   Distance
  </a>
  - Julia module for Distance evaluation
  <sup>
   377 GitHub links in total 753 links, &#9733 25, pushed 413 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/bensadeghi/DecisionTree.jl">
   Decision Tree
  </a>
  - Decision Tree Classifier and Regressor
  <sup>
   377 GitHub links in total 753 links, &#9733 60, pushed 6 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/compressed/BackpropNeuralNet.jl">
   Neural
  </a>
  - A neural network in Julia
  <sup>
   377 GitHub links in total 753 links, &#9733 26, pushed 92 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/doobwa/MCMC.jl">
   MCMC
  </a>
  - MCMC tools for Julia
  <sup>
   377 GitHub links in total 753 links, &#9733 19, pushed 1113 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/brian-j-smith/Mamba.jl">
   Mamba
  </a>
  - Markov chain Monte Carlo (MCMC) for Bayesian analysis in Julia
  <sup>
   377 GitHub links in total 753 links, &#9733 76, pushed 56 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/JuliaStats/GLM.jl">
   GLM
  </a>
  - Generalized linear models in Julia
  <sup>
   377 GitHub links in total 753 links, &#9733 107, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/lendle/OnlineLearning.jl">
   Online Learning
  </a>
  <sup>
   377 GitHub links in total 753 links, &#9733 10, pushed 511 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/simonster/GLMNet.jl">
   GLMNet
  </a>
  - Julia wrapper for fitting Lasso/ElasticNet GLM models using glmnet
  <sup>
   377 GitHub links in total 753 links, &#9733 28, pushed 204 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/JuliaStats/Clustering.jl">
   Clustering
  </a>
  - Basic functions for clustering data: k-means, dp-means, etc.
  <sup>
   377 GitHub links in total 753 links, &#9733 56, pushed 64 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/JuliaStats/SVM.jl">
   SVM
  </a>
  - SVM's for Julia
  <sup>
   377 GitHub links in total 753 links, &#9733 25, pushed 221 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/JuliaStats/KernelDensity.jl">
   Kernal Density
  </a>
  - Kernel density estimators for julia
  <sup>
   377 GitHub links in total 753 links, &#9733 17, pushed 125 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/JuliaStats/DimensionalityReduction.jl">
   Dimensionality Reduction
  </a>
  - Methods for dimensionality reduction
  <sup>
   377 GitHub links in total 753 links, &#9733 20, pushed 598 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/JuliaStats/NMF.jl">
   NMF
  </a>
  - A Julia package for non-negative matrix factorization
  <sup>
   377 GitHub links in total 753 links, &#9733 24, pushed 87 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/EricChiang/ANN.jl">
   ANN
  </a>
  - Julia artificial neural networks
  <sup>
   377 GitHub links in total 753 links, &#9733 48, pushed 491 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/pluskid/Mocha.jl">
   Mocha
  </a>
  - Deep Learning framework for Julia inspired by Caffe
  <sup>
   377 GitHub links in total 753 links, &#9733 675, pushed 20 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/dmlc/XGBoost.jl">
   XGBoost
  </a>
  - eXtreme Gradient Boosting Package in Julia
  <sup>
   377 GitHub links in total 753 links, &#9733 48, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/wildart/ManifoldLearning.jl">
   ManifoldLearning
  </a>
  - A Julia package for manifold learning and nonlinear dimensionality reduction
  <sup>
   377 GitHub links in total 753 links, &#9733 13, pushed 168 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/dmlc/mxnet">
   MXNet
  </a>
  - Lightweight, Portable, Flexible Distributed/Mobile Deep Learning with Dynamic, Mutation-aware Dataflow Dep Scheduler; for Python, R, Julia, Go, Javascript and more.
 </li>
 <li>
  <a href="https://github.com/hshindo/Merlin.jl">
   Merlin
  </a>
  - Flexible Deep Learning Framework in Julia
  <sup>
   377 GitHub links in total 753 links, &#9733 15, pushed 5 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="julia-nlp">
 </a>
</p>
<h4>
 Natural Language Processing
</h4>
<ul>
 <li>
  <a href="https://github.com/slycoder/TopicModels.jl">
   Topic Models
  </a>
  - TopicModels for Julia
  <sup>
   377 GitHub links in total 753 links, &#9733 22, pushed 18 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/johnmyleswhite/TextAnalysis.jl">
   Text Analysis
  </a>
  - Julia package for text analysis
  <sup>
   377 GitHub links in total 753 links, &#9733 87, pushed 193 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="julia-data-analysis">
 </a>
</p>
<h4>
 Data Analysis / Data Visualization
</h4>
<ul>
 <li>
  <a href="https://github.com/IainNZ/GraphLayout.jl">
   Graph Layout
  </a>
  - Graph layout algorithms in pure Julia
  <sup>
   377 GitHub links in total 753 links, &#9733 35, pushed 45 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/JuliaStats/DataFramesMeta.jl">
   Data Frames Meta
  </a>
  - Metaprogramming tools for DataFrames
  <sup>
   377 GitHub links in total 753 links, &#9733 54, pushed 28 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/nfoti/JuliaData">
   Julia Data
  </a>
  - library for working with tabular data in Julia
  <sup>
   377 GitHub links in total 753 links, &#9733 4, pushed 972 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/WizardMac/DataRead.jl">
   Data Read
  </a>
  - Read files from Stata, SAS, and SPSS
  <sup>
   377 GitHub links in total 753 links, &#9733 32, pushed 200 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/JuliaStats/HypothesisTests.jl">
   Hypothesis Tests
  </a>
  - Hypothesis tests for Julia
  <sup>
   377 GitHub links in total 753 links, &#9733 28, pushed 14 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/dcjones/Gadfly.jl">
   Gadfly
  </a>
  - Crafty statistical graphics for Julia.
  <sup>
   377 GitHub links in total 753 links, &#9733 872, pushed 6 days ago
  </sup>
 </li>
 <li>
  <p>
   <a href="https://github.com/JuliaStats/Stats.jl">
    Stats
   </a>
   - Statistical tests for Julia
  </p>
  <sup>
   377 GitHub links in total 753 links, &#9733 4, pushed 753 days ago
  </sup>
 </li>
 <li>
  <p>
   <a href="https://github.com/johnmyleswhite/RDatasets.jl">
    RDataSets
   </a>
   - Julia package for loading many of the data sets available in R
  </p>
  <sup>
   377 GitHub links in total 753 links, &#9733 43, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/JuliaStats/DataFrames.jl">
   DataFrames
  </a>
  - library for working with tabular data in Julia
  <sup>
   377 GitHub links in total 753 links, &#9733 272, pushed 0 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/JuliaStats/Distributions.jl">
   Distributions
  </a>
  - A Julia package for probability distributions and associated functions.
  <sup>
   377 GitHub links in total 753 links, &#9733 174, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/JuliaStats/DataArrays.jl">
   Data Arrays
  </a>
  - Data structures that allow missing values
  <sup>
   377 GitHub links in total 753 links, &#9733 28, pushed 69 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/JuliaStats/TimeSeries.jl">
   Time Series
  </a>
  - Time series toolkit for Julia
  <sup>
   377 GitHub links in total 753 links, &#9733 50, pushed 49 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/lindahua/Sampling.jl">
   Sampling
  </a>
  - Basic sampling algorithms for Julia
  <sup>
   377 GitHub links in total 753 links, &#9733 0, pushed 684 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="julia-misc">
 </a>
</p>
<h4>
 Misc Stuff / Presentations
</h4>
<ul>
 <li>
  <a href="https://github.com/JuliaDSP/DSP.jl">
   DSP
  </a>
  - Digital Signal Processing (filtering, periodograms, spectrograms, window functions).
  <sup>
   377 GitHub links in total 753 links, &#9733 47, pushed 93 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/JuliaCon/presentations">
   JuliaCon Presentations
  </a>
  - Presentations for JuliaCon
  <sup>
   377 GitHub links in total 753 links, &#9733 64, pushed 57 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/davidavdav/SignalProcessing.jl">
   SignalProcessing
  </a>
  - Signal Processing tools for Julia
  <sup>
   377 GitHub links in total 753 links, &#9733 2, pushed 570 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/timholy/Images.jl">
   Images
  </a>
  - An image library for Julia
  <sup>
   377 GitHub links in total 753 links, &#9733 100, pushed 7 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="lua">
 </a>
</p>
<h2>
 Lua
</h2>
<p>
 <a name="lua-general-purpose">
 </a>
</p>
<h4>
 General-Purpose Machine Learning
</h4>
<ul>
 <li>
  <a href="http://torch.ch/">
   Torch7
  </a>
  <ul>
   <li>
    <a href="http://jucor.github.io/torch-cephes">
     cephes
    </a>
    - Cephes mathematical functions library, wrapped for Torch. Provides and wraps the 180+ special mathematical functions from the Cephes mathematical library, developed by Stephen L. Moshier. It is used, among many other places, at the heart of SciPy.
   </li>
   <li>
    <a href="https://github.com/twitter/torch-autograd">
     autograd
    </a>
    - Autograd automatically differentiates native Torch code. Inspired by the original Python version.
    <sup>
     377 GitHub links in total 753 links, &#9733 362, pushed 2 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/torch/graph">
     graph
    </a>
    - Graph package for Torch
    <sup>
     377 GitHub links in total 753 links, &#9733 23, pushed 18 days ago
    </sup>
   </li>
   <li>
    <a href="http://jucor.github.io/torch-randomkit/">
     randomkit
    </a>
    - Numpy's randomkit, wrapped for Torch
   </li>
   <li>
    <a href="http://soumith.ch/torch-signal/signal/">
     signal
    </a>
    - A signal processing toolbox for Torch-7. FFT, DCT, Hilbert, cepstrums, stft
   </li>
   <li>
    <a href="https://github.com/torch/nn">
     nn
    </a>
    - Neural Network package for Torch
    <sup>
     377 GitHub links in total 753 links, &#9733 528, pushed 2 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/torch/nngraph">
     nngraph
    </a>
    - This package provides graphical computation for nn library in Torch7.
    <sup>
     377 GitHub links in total 753 links, &#9733 128, pushed 5 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/clementfarabet/lua---nnx">
     nnx
    </a>
    - A completely unstable and experimental package that extends Torch's builtin nn library
    <sup>
     377 GitHub links in total 753 links, &#9733 65, pushed 5 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/Element-Research/rnn">
     rnn
    </a>
    - A Recurrent Neural Network library that extends Torch's nn. RNNs, LSTMs, GRUs, BRNNs, BLSTMs, etc.
    <sup>
     377 GitHub links in total 753 links, &#9733 452, pushed 2 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/Element-Research/dpnn">
     dpnn
    </a>
    - Many useful features that aren't part of the main nn package.
    <sup>
     377 GitHub links in total 753 links, &#9733 105, pushed 14 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/nicholas-leonard/dp">
     dp
    </a>
    - A deep learning library designed for streamlining research and development using the Torch7 distribution. It emphasizes flexibility through the elegant use of object-oriented design patterns.
    <sup>
     377 GitHub links in total 753 links, &#9733 280, pushed 6 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/torch/optim">
     optim
    </a>
    - An optimization library for Torch. SGD, Adagrad, Conjugate-Gradient, LBFGS, RProp and more.
    <sup>
     377 GitHub links in total 753 links, &#9733 100, pushed 7 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/koraykv/unsup">
     unsup
    </a>
    - A package for unsupervised learning in Torch. Provides modules that are compatible with nn (LinearPsd, ConvPsd, AutoEncoder, ...), and self-contained algorithms (k-means, PCA).
    <sup>
     377 GitHub links in total 753 links, &#9733 65, pushed 88 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/clementfarabet/manifold">
     manifold
    </a>
    - A package to manipulate manifolds
    <sup>
     377 GitHub links in total 753 links, &#9733 60, pushed 175 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/koraykv/torch-svm">
     svm
    </a>
    - Torch-SVM library
    <sup>
     377 GitHub links in total 753 links, &#9733 24, pushed 20 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/clementfarabet/lbfgs">
     lbfgs
    </a>
    - FFI Wrapper for liblbfgs
    <sup>
     377 GitHub links in total 753 links, &#9733 2, pushed 1152 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/clementfarabet/vowpal_wabbit">
     vowpalwabbit
    </a>
    - An old vowpalwabbit interface to torch.
    <sup>
     377 GitHub links in total 753 links, &#9733 1, pushed 1455 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/clementfarabet/lua---opengm">
     OpenGM
    </a>
    - OpenGM is a C++ library for graphical modeling, and inference. The Lua bindings provide a simple way of describing graphs, from Lua, and then optimizing them with OpenGM.
    <sup>
     377 GitHub links in total 753 links, &#9733 5, pushed 1523 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/MichaelMathieu/lua---spaghetti">
     sphagetti
    </a>
    - Spaghetti (sparse linear) module for torch7 by @MichaelMathieu
    <sup>
     377 GitHub links in total 753 links, &#9733 0, pushed 1002 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/ocallaco/LuaSHkit">
     LuaSHKit
    </a>
    - A lua wrapper around the Locality sensitive hashing library SHKit
    <sup>
     377 GitHub links in total 753 links, &#9733 1, pushed 713 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/rlowrance/kernel-smoothers">
     kernel smoothing
    </a>
    - KNN, kernel-weighted average, local linear regression smoothers
    <sup>
     377 GitHub links in total 753 links, &#9733 2, pushed 1285 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/torch/cutorch">
     cutorch
    </a>
    - Torch CUDA Implementation
    <sup>
     377 GitHub links in total 753 links, &#9733 128, pushed 2 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/torch/cunn">
     cunn
    </a>
    - Torch CUDA Neural Network Implementation
    <sup>
     377 GitHub links in total 753 links, &#9733 95, pushed 2 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/clementfarabet/lua---imgraph">
     imgraph
    </a>
    - An image/graph library for Torch. This package provides routines to construct graphs on images, segment them, build trees out of them, and convert them back to images.
    <sup>
     377 GitHub links in total 753 links, &#9733 11, pushed 335 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/clementfarabet/videograph">
     videograph
    </a>
    - A video/graph library for Torch. This package provides routines to construct graphs on videos, segment them, build trees out of them, and convert them back to videos.
    <sup>
     377 GitHub links in total 753 links, &#9733 6, pushed 1034 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/marcoscoffier/torch-saliency">
     saliency
    </a>
    - code and tools around integral images. A library for finding interest points based on fast integral histograms.
    <sup>
     377 GitHub links in total 753 links, &#9733 3, pushed 872 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/marcoscoffier/lua---stitch">
     stitch
    </a>
    - allows us to use hugin to stitch images and apply same stitching to a video sequence
    <sup>
     377 GitHub links in total 753 links, &#9733 1, pushed 1458 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/marcoscoffier/lua---sfm">
     sfm
    </a>
    - A bundle adjustment/structure from motion package
    <sup>
     377 GitHub links in total 753 links, &#9733 2, pushed 1539 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/koraykv/fex">
     fex
    </a>
    - A package for feature extraction in Torch. Provides SIFT and dSIFT modules.
    <sup>
     377 GitHub links in total 753 links, &#9733 5, pushed 823 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/sermanet/OverFeat">
     OverFeat
    </a>
    - A state-of-the-art generic dense feature extractor
    <sup>
     377 GitHub links in total 753 links, &#9733 399, pushed 630 days ago
    </sup>
   </li>
  </ul>
 </li>
 <li>
  <a href="http://numlua.luaforge.net/">
   Numeric Lua
  </a>
 </li>
 <li>
  <a href="http://labix.org/lunatic-python">
   Lunatic Python
  </a>
 </li>
 <li>
  <a href="http://www.scilua.org/">
   SciLua
  </a>
 </li>
 <li>
  <a href="https://bitbucket.org/lucashnegri/lna">
   Lua - Numerical Algorithms
  </a>
 </li>
 <li>
  <a href="http://zrake.webfactional.com/projects/lunum">
   Lunum
  </a>
 </li>
</ul>
<p>
 <a name="lua-demos">
 </a>
</p>
<h4>
 Demos and Scripts
</h4>
<ul>
 <li>
  <a href="https://github.com/e-lab/torch7-demos">
   Core torch7 demos repository
  </a>
  .
  <ul>
   <li>
    linear-regression, logistic-regression
   </li>
   <li>
    face detector (training and detection as separate demos)
   </li>
   <li>
    mst-based-segmenter
   </li>
   <li>
    train-a-digit-classifier
   </li>
   <li>
    train-autoencoder
   </li>
   <li>
    optical flow demo
   </li>
   <li>
    train-on-housenumbers
   </li>
   <li>
    train-on-cifar
   </li>
   <li>
    tracking with deep nets
   </li>
   <li>
    kinect demo
   </li>
   <li>
    filter-bank visualization
   </li>
   <li>
    saliency-networks
   </li>
  </ul>
  <sup>
   377 GitHub links in total 753 links, &#9733 25, pushed 325 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/soumith/galaxyzoo">
   Training a Convnet for the Galaxy-Zoo Kaggle challenge(CUDA demo)
  </a>
  <sup>
   377 GitHub links in total 753 links, &#9733 31, pushed 549 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/mbhenaff/MusicTagging">
   Music Tagging
  </a>
  - Music Tagging scripts for torch7
  <sup>
   377 GitHub links in total 753 links, &#9733 7, pushed 776 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/rosejn/torch-datasets">
   torch-datasets
  </a>
  - Scripts to load several popular datasets including:
  <ul>
   <li>
    BSR 500
   </li>
   <li>
    CIFAR-10
   </li>
   <li>
    COIL
   </li>
   <li>
    Street View House Numbers
   </li>
   <li>
    MNIST
   </li>
   <li>
    NORB
   </li>
  </ul>
  <sup>
   377 GitHub links in total 753 links, &#9733 28, pushed 783 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/fidlej/aledataset">
   Atari2600
  </a>
  - Scripts to generate a dataset with static frames from the Arcade Learning Environment
  <sup>
   377 GitHub links in total 753 links, &#9733 15, pushed 725 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="matlab">
 </a>
</p>
<h2>
 Matlab
</h2>
<p>
 <a name="matlab-cv">
 </a>
</p>
<h4>
 Computer Vision
</h4>
<ul>
 <li>
  <a href="http://www.ifp.illinois.edu/~minhdo/software/contourlet_toolbox.tar">
   Contourlets
  </a>
  - MATLAB source code that implements the contourlet transform and its utility functions.
 </li>
 <li>
  <a href="http://www.shearlab.org/index_software.html">
   Shearlets
  </a>
  - MATLAB code for shearlet transform
 </li>
 <li>
  <a href="http://www.curvelet.org/software.html">
   Curvelets
  </a>
  - The Curvelet transform is a higher dimensional generalization of the Wavelet transform designed to represent images at different scales and different angles.
 </li>
 <li>
  <a href="http://www.cmap.polytechnique.fr/~peyre/download/">
   Bandlets
  </a>
  - MATLAB code for bandlet transform
 </li>
 <li>
  <a href="http://kyamagu.github.io/mexopencv/">
   mexopencv
  </a>
  - Collection and a development kit of MATLAB mex functions for OpenCV library
 </li>
</ul>
<p>
 <a name="matlab-nlp">
 </a>
</p>
<h4>
 Natural Language Processing
</h4>
<ul>
 <li>
  <a href="https://amplab.cs.berkeley.edu/2012/05/05/an-nlp-library-for-matlab/">
   NLP
  </a>
  - An NLP library for Matlab
 </li>
</ul>
<p>
 <a name="matlab-general-purpose">
 </a>
</p>
<h4>
 General-Purpose Machine Learning
</h4>
<ul>
 <li>
  <a href="http://www.cs.toronto.edu/~hinton/MatlabForSciencePaper.html">
   Training a deep autoencoder or a classifier
on MNIST digits
  </a>
  - Training a deep autoencoder or a classifier
on MNIST digits[DEEP LEARNING]
 </li>
 <li>
  <a href="http://www.socher.org/index.php/Main/Convolutional-RecursiveDeepLearningFor3DObjectClassification">
   Convolutional-Recursive Deep Learning for 3D Object Classification
  </a>
  - Convolutional-Recursive Deep Learning for 3D Object Classification[DEEP LEARNING]
 </li>
 <li>
  <a href="http://homepage.tudelft.nl/19j49/t-SNE.html">
   t-Distributed Stochastic Neighbor Embedding
  </a>
  - t-Distributed Stochastic Neighbor Embedding (t-SNE) is a (prize-winning) technique for dimensionality reduction that is particularly well suited for the visualization of high-dimensional datasets.
 </li>
 <li>
  <a href="http://people.kyb.tuebingen.mpg.de/spider/">
   Spider
  </a>
  - The spider is intended to be a complete object orientated environment for machine learning in Matlab.
 </li>
 <li>
  <a href="http://www.csie.ntu.edu.tw/~cjlin/libsvm/#matlab">
   LibSVM
  </a>
  - A Library for Support Vector Machines
 </li>
 <li>
  <a href="http://www.csie.ntu.edu.tw/~cjlin/liblinear/#download">
   LibLinear
  </a>
  - A Library for Large Linear Classification
 </li>
 <li>
  <a href="https://github.com/josephmisiti/machine-learning-module">
   Machine Learning Module
  </a>
  - Class on machine w/ PDF,lectures,code
  <sup>
   377 GitHub links in total 753 links, &#9733 258, pushed 1832 days ago
  </sup>
 </li>
 <li>
  <a href="http://caffe.berkeleyvision.org">
   Caffe
  </a>
  - A deep learning framework developed with cleanliness, readability, and speed in mind.
 </li>
 <li>
  <a href="https://github.com/newfolder/PRT">
   Pattern Recognition Toolbox
  </a>
  - A complete object-oriented environment for machine learning in Matlab.
 </li>
 <li>
  <a href="https://github.com/PRML/PRMLT">
   Pattern Recognition and Machine Learning
  </a>
  - This package contains the matlab implementation of the algorithms described in the book Pattern Recognition and Machine Learning by C. Bishop.
  <sup>
   377 GitHub links in total 753 links, &#9733 423, pushed 7 days ago
  </sup>
 </li>
 <li>
  <a href="http://docs.optunity.net">
   Optunity
  </a>
  - A library dedicated to automated hyperparameter optimization with a simple, lightweight API to facilitate drop-in replacement of grid search. Optunity is written in Python but interfaces seamlessly with MATLAB.
 </li>
</ul>
<p>
 <a name="matlab-data-analysis">
 </a>
</p>
<h4>
 Data Analysis / Data Visualization
</h4>
<ul>
 <li>
  <a href="https://www.cs.purdue.edu/homes/dgleich/packages/matlab_bgl/">
   matlab_gbl
  </a>
  - MatlabBGL is a Matlab package for working with graphs.
 </li>
 <li>
  <a href="http://www.mathworks.com/matlabcentral/fileexchange/24134-gaimc---graph-algorithms-in-matlab-code">
   gamic
  </a>
  - Efficient pure-Matlab implementations of graph algorithms to complement MatlabBGL's mex functions.
 </li>
</ul>
<p>
 <a name="net">
 </a>
</p>
<h2>
 .NET
</h2>
<p>
 <a name="net-cv">
 </a>
</p>
<h4>
 Computer Vision
</h4>
<ul>
 <li>
  <a href="https://code.google.com/p/opencvdotnet/">
   OpenCVDotNet
  </a>
  - A wrapper for the OpenCV project to be used with .NET applications.
 </li>
 <li>
  <a href="http://www.emgu.com/wiki/index.php/Main_Page">
   Emgu CV
  </a>
  - Cross platform wrapper of OpenCV which can be compiled in Mono to e run on Windows, Linus, Mac OS X, iOS, and Android.
 </li>
 <li>
  <a href="http://www.aforgenet.com/framework/">
   AForge.NET
  </a>
  - Open source C# framework for developers and researchers in the fields of Computer Vision and Artificial Intelligence. Development has now shifted to GitHub.
 </li>
 <li>
  <a href="http://accord-framework.net">
   Accord.NET
  </a>
  - Together with AForge.NET, this library can provide image processing and computer vision algorithms to Windows, Windows RT and Windows Phone. Some components are also available for Java and Android.
 </li>
</ul>
<p>
 <a name="net-nlp">
 </a>
</p>
<h4>
 Natural Language Processing
</h4>
<ul>
 <li>
  <a href="https://github.com/sergey-tihon/Stanford.NLP.NET/">
   Stanford.NLP for .NET
  </a>
  - A full port of Stanford NLP packages to .NET and also available precompiled as a NuGet package.
 </li>
</ul>
<p>
 <a name="net-general-purpose">
 </a>
</p>
<h4>
 General-Purpose Machine Learning
</h4>
<ul>
 <li>
  <a href="http://accord-framework.net/">
   Accord-Framework
  </a>
  -The Accord.NET Framework is a complete framework for building machine learning, computer vision, computer audition, signal processing and statistical applications.
 </li>
 <li>
  <a href="http://www.nuget.org/packages/Accord.MachineLearning/">
   Accord.MachineLearning
  </a>
  - Support Vector Machines, Decision Trees, Naive Bayesian models, K-means, Gaussian Mixture models and general algorithms such as Ransac, Cross-validation and Grid-Search for machine-learning applications. This package is part of the Accord.NET Framework.
 </li>
 <li>
  <a href="http://diffsharp.github.io/DiffSharp/">
   DiffSharp
  </a>
  - An automatic differentiation (AD) library providing exact and efficient derivatives (gradients, Hessians, Jacobians, directional derivatives, and matrix-free Hessian- and Jacobian-vector products) for machine learning and optimization applications. Operations can be nested to any level, meaning that you can compute exact higher-order derivatives and differentiate functions that are internally making use of differentiation, for applications such as hyperparameter optimization.
 </li>
 <li>
  <a href="https://github.com/fsprojects/Vulpes">
   Vulpes
  </a>
  - Deep belief and deep learning implementation written in F# and leverages CUDA GPU execution with Alea.cuBase.
  <sup>
   377 GitHub links in total 753 links, &#9733 87, pushed 29 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.nuget.org/packages/encog-dotnet-core/">
   Encog
  </a>
  -  An advanced neural network and machine learning framework. Encog contains classes to create a wide variety of networks, as well as support classes to normalize and process data for these neural networks. Encog trains using multithreaded resilient propagation. Encog can also make use of a GPU to further speed processing time. A GUI based workbench is also provided to help model and train neural networks.
 </li>
 <li>
  <a href="http://bragisoft.com/">
   Neural Network Designer
  </a>
  - DBMS management system and designer for neural networks. The designer application is developed using WPF, and is a user interface which allows you to design your neural network, query the network, create and configure chat bots that are capable of asking questions and learning from your feed back.  The chat bots can even scrape the internet for information to return in their output as well as to use for learning.
 </li>
</ul>
<p>
 <a name="net-data-analysis">
 </a>
</p>
<h4>
 Data Analysis / Data Visualization
</h4>
<ul>
 <li>
  <a href="http://www.nuget.org/packages/numl/">
   numl
  </a>
  - numl is a machine learning library intended to ease the use of using standard modeling techniques for both prediction and clustering.
 </li>
 <li>
  <a href="http://www.nuget.org/packages/MathNet.Numerics/">
   Math.NET Numerics
  </a>
  - Numerical foundation of the Math.NET project, aiming to provide methods and algorithms for numerical computations in science, engineering and every day use. Supports .Net 4.0, .Net 3.5 and Mono on Windows, Linux and Mac; Silverlight 5, WindowsPhone/SL 8, WindowsPhone 8.1 and Windows 8 with PCL Portable Profiles 47 and 344; Android/iOS with Xamarin.
 </li>
 <li>
  <a href="http://research.microsoft.com/en-us/projects/sho/">
   Sho
  </a>
  - Sho is an interactive environment for data analysis and scientific computing that lets you seamlessly connect scripts (in IronPython) with compiled code (in .NET) to enable fast and flexible prototyping. The environment includes powerful and efficient libraries for linear algebra as well as data visualization that can be used from any .NET language, as well as a feature-rich interactive shell for rapid development.
 </li>
</ul>
<p>
 <a name="objectivec">
 </a>
</p>
<h2>
 Objective C
</h2>
<p>
 <a name="objectivec-general-purpose">
 </a>
</p>
<h3>
 General-Purpose Machine Learning
</h3>
<ul>
 <li>
  <a href="https://github.com/yconst/YCML">
   YCML
  </a>
  - A Machine Learning framework for Objective-C and Swift (OS X / iOS).
  <sup>
   377 GitHub links in total 753 links, &#9733 41, pushed 12 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/nikolaypavlov/MLPNeuralNet">
   MLPNeuralNet
  </a>
  - Fast multilayer perceptron neural network library for iOS and Mac OS X. MLPNeuralNet predicts new examples by trained neural network. It is built on top of the Apple's Accelerate Framework, using vectorized operations and hardware acceleration if available.
  <sup>
   377 GitHub links in total 753 links, &#9733 807, pushed 225 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/gianlucabertani/MAChineLearning">
   MAChineLearning
  </a>
  - An Objective-C multilayer perceptron library, with full support for training through backpropagation. Implemented using vDSP and vecLib, it's 20 times faster than its Java equivalent. Includes sample code for use from Swift.
  <sup>
   377 GitHub links in total 753 links, &#9733 11, pushed 366 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Kalvar/ios-BPN-NeuralNetwork">
   BPN-NeuralNetwork
  </a>
  - It implemented 3 layers neural network ( Input Layer, Hidden Layer and Output Layer ) and it named Back Propagation Neural Network (BPN). This network can be used in products recommendation, user behavior analysis, data mining and data analysis.
  <sup>
   377 GitHub links in total 753 links, &#9733 22, pushed 170 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Kalvar/ios-Multi-Perceptron-NeuralNetwork">
   Multi-Perceptron-NeuralNetwork
  </a>
  - it implemented multi-perceptrons neural network (ニューラルネットワーク) based on Back Propagation Neural Network (BPN) and designed unlimited-hidden-layers.
  <sup>
   377 GitHub links in total 753 links, &#9733 10, pushed 131 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Kalvar/ios-KRHebbian-Algorithm">
   KRHebbian-Algorithm
  </a>
  - It is a non-supervisor and self-learning algorithm (adjust the weights) in neural network of Machine Learning.
  <sup>
   377 GitHub links in total 753 links, &#9733 10, pushed 177 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Kalvar/ios-KRKmeans-Algorithm">
   KRKmeans-Algorithm
  </a>
  - It implemented K-Means the clustering and classification algorithm. It could be used in data mining and image compression.
  <sup>
   377 GitHub links in total 753 links, &#9733 11, pushed 97 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Kalvar/ios-KRFuzzyCMeans-Algorithm">
   KRFuzzyCMeans-Algorithm
  </a>
  - It implemented Fuzzy C-Means (FCM) the fuzzy clustering / classification algorithm on Machine Learning. It could be used in data mining and image compression.
  <sup>
   377 GitHub links in total 753 links, &#9733 8, pushed 97 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="ocaml">
 </a>
</p>
<h2>
 OCaml
</h2>
<p>
 <a name="ocaml-general-purpose">
 </a>
</p>
<h3>
 General-Purpose Machine Learning
</h3>
<ul>
 <li>
  <a href="https://github.com/hammerlab/oml/">
   Oml
  </a>
  - A general statistics and machine learning library.
 </li>
 <li>
  <a href="http://mmottl.github.io/gpr">
   GPR
  </a>
  - Efficient Gaussian Process Regression in OCaml.
 </li>
 <li>
  <a href="http://libra.cs.uoregon.edu">
   Libra-Tk
  </a>
  - Algorithms for learning and inference with discrete probabilistic models.
 </li>
</ul>
<p>
 <a name="php">
 </a>
</p>
<h2>
 PHP
</h2>
<p>
 <a name="php-nlp">
 </a>
</p>
<h3>
 Natural Language Processing
</h3>
<ul>
 <li>
  <a href="https://github.com/fukuball/jieba-php">
   jieba-php
  </a>
  - Chinese Words Segmentation Utilities.
  <sup>
   377 GitHub links in total 753 links, &#9733 135, pushed 47 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="php-general-purpose">
 </a>
</p>
<h3>
 General-Purpose Machine Learning
</h3>
<ul>
 <li>
  <a href="https://github.com/denissimon/prediction-builder">
   PredictionBuilder
  </a>
  - A library for machine learning that builds predictions using a linear regression.
  <sup>
   377 GitHub links in total 753 links, &#9733 35, pushed 7 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="python">
 </a>
</p>
<h2>
 Python
</h2>
<p>
 <a name="python-cv">
 </a>
</p>
<h4>
 Computer Vision
</h4>
<ul>
 <li>
  <a href="https://github.com/scikit-image/scikit-image">
   Scikit-Image
  </a>
  - A collection of algorithms for image processing in Python.
  <sup>
   377 GitHub links in total 753 links, &#9733 1070, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="http://simplecv.org/">
   SimpleCV
  </a>
  - An open source computer vision framework that gives access to several high-powered computer vision libraries, such as OpenCV. Written on Python and runs on Mac, Windows, and Ubuntu Linux.
 </li>
 <li>
  <a href="https://github.com/ukoethe/vigra">
   Vigranumpy
  </a>
  - Python bindings for the VIGRA C++ computer vision library.
  <sup>
   377 GitHub links in total 753 links, &#9733 189, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://cmusatyalab.github.io/openface/">
   OpenFace
  </a>
  - Free and open source face recognition with deep neural networks.
 </li>
</ul>
<p>
 <a name="python-nlp">
 </a>
</p>
<h4>
 Natural Language Processing
</h4>
<ul>
 <li>
  <a href="http://www.nltk.org/">
   NLTK
  </a>
  - A leading platform for building Python programs to work with human language data.
 </li>
 <li>
  <a href="http://www.clips.ua.ac.be/pattern">
   Pattern
  </a>
  - A web mining module for the Python programming language. It has tools for natural language processing, machine learning, among others.
 </li>
 <li>
  <a href="https://github.com/machinalis/quepy">
   Quepy
  </a>
  - A python framework to transform natural language questions to queries in a database query language
  <sup>
   377 GitHub links in total 753 links, &#9733 572, pushed 48 days ago
  </sup>
 </li>
 <li>
  <a href="http://textblob.readthedocs.org/">
   TextBlob
  </a>
  - Providing a consistent API for diving into common natural language processing (NLP) tasks. Stands on the giant shoulders of NLTK and Pattern, and plays nicely with both.
 </li>
 <li>
  <a href="https://github.com/machinalis/yalign">
   YAlign
  </a>
  - A sentence aligner, a friendly tool for extracting parallel sentences from comparable corpora.
  <sup>
   377 GitHub links in total 753 links, &#9733 46, pushed 263 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/fxsjy/jieba#jieba-1">
   jieba
  </a>
  - Chinese Words Segmentation Utilities.
 </li>
 <li>
  <a href="https://github.com/isnowfy/snownlp">
   SnowNLP
  </a>
  - A library for processing Chinese text.
  <sup>
   377 GitHub links in total 753 links, &#9733 1294, pushed 216 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/prodicus/spammy">
   spammy
  </a>
  - A library for email Spam filtering built on top of nltk
  <sup>
   377 GitHub links in total 753 links, &#9733 34, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/victorlin/loso">
   loso
  </a>
  - Another Chinese segmentation library.
  <sup>
   377 GitHub links in total 753 links, &#9733 56, pushed 1845 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/duanhongyi/genius">
   genius
  </a>
  - A Chinese segment base on Conditional Random Field.
  <sup>
   377 GitHub links in total 753 links, &#9733 95, pushed 554 days ago
  </sup>
 </li>
 <li>
  <a href="http://konlpy.org">
   KoNLPy
  </a>
  - A Python package for Korean natural language processing.
 </li>
 <li>
  <a href="https://github.com/pprett/nut">
   nut
  </a>
  - Natural language Understanding Toolkit
  <sup>
   377 GitHub links in total 753 links, &#9733 75, pushed 727 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/columbia-applied-data-science/rosetta">
   Rosetta
  </a>
  - Text processing tools and wrappers (e.g. Vowpal Wabbit)
  <sup>
   377 GitHub links in total 753 links, &#9733 145, pushed 126 days ago
  </sup>
 </li>
 <li>
  <a href="https://pypi.python.org/pypi/bllipparser/">
   BLLIP Parser
  </a>
  - Python bindings for the BLLIP Natural Language Parser (also known as the Charniak-Johnson parser)
 </li>
 <li>
  <a href="https://github.com/proycon/pynlpl">
   PyNLPl
  </a>
  - Python Natural Language Processing Library. General purpose NLP library for Python. Also contains some specific modules for parsing common NLP formats, most notably for
  <a href="http://proycon.github.io/folia/">
   FoLiA
  </a>
  , but also ARPA language models, Moses phrasetables, GIZA++ alignments.
  <sup>
   377 GitHub links in total 753 links, &#9733 182, pushed 12 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/proycon/python-ucto">
   python-ucto
  </a>
  - Python binding to ucto (a unicode-aware rule-based tokenizer for various languages)
  <sup>
   377 GitHub links in total 753 links, &#9733 9, pushed 54 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/proycon/python-frog">
   python-frog
  </a>
  - Python binding to Frog, an NLP suite for Dutch. (pos tagging, lemmatisation, dependency parsing, NER)
  <sup>
   377 GitHub links in total 753 links, &#9733 7, pushed 41 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/EducationalTestingService/python-zpar">
   python-zpar
  </a>
  - Python bindings for
  <a href="https://github.com/frcchang/zpar">
   ZPar
  </a>
  , a statistical part-of-speech-tagger, constiuency parser, and dependency parser for English.
  <sup>
   377 GitHub links in total 753 links, &#9733 24, pushed 292 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/proycon/colibri-core">
   colibri-core
  </a>
  - Python binding to C++ library for extracting and working with with basic linguistic constructions such as n-grams and skipgrams in a quick and memory-efficient way.
 </li>
 <li>
  <a href="https://github.com/honnibal/spaCy/">
   spaCy
  </a>
  - Industrial strength NLP with Python and Cython.
 </li>
 <li>
  <a href="https://github.com/dmcc/PyStanfordDependencies">
   PyStanfordDependencies
  </a>
  - Python interface for converting Penn Treebank trees to Stanford Dependencies.
  <sup>
   377 GitHub links in total 753 links, &#9733 22, pushed 80 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="python-general-purpose">
 </a>
</p>
<h4>
 General-Purpose Machine Learning
</h4>
<ul>
 <li>
  <a href="https://github.com/jeff1evesque/machine-learning">
   machine learning
  </a>
  - automated build consisting of a
  <a href="https://github.com/jeff1evesque/machine-learning#web-interface">
   web-interface
  </a>
  , and set of
  <a href="https://github.com/jeff1evesque/machine-learning#programmatic-interface">
   programmatic-interface
  </a>
  API, for support vector machines.  Corresponding dataset(s) are stored into a SQL database, then generated model(s) used for prediction(s), are stored into a NoSQL datastore.
  <sup>
   377 GitHub links in total 753 links, &#9733 37, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/dmlc/xgboost">
   XGBoost
  </a>
  - Python bindings for eXtreme Gradient Boosting (Tree) Library
 </li>
 <li>
  <a href="https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers">
   Bayesian Methods for Hackers
  </a>
  - Book/iPython notebooks on Probabilistic Programming in Python
  <sup>
   377 GitHub links in total 753 links, &#9733 9693, pushed 6 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/machinalis/featureforge">
   Featureforge
  </a>
  A set of tools for creating and testing machine learning features, with a scikit-learn compatible API
  <sup>
   377 GitHub links in total 753 links, &#9733 203, pushed 17 days ago
  </sup>
 </li>
 <li>
  <a href="http://spark.apache.org/docs/latest/mllib-guide.html">
   MLlib in Apache Spark
  </a>
  - Distributed machine learning library in Spark
 </li>
 <li>
  <a href="http://scikit-learn.org/">
   scikit-learn
  </a>
  - A Python module for machine learning built on top of SciPy.
 </li>
 <li>
  <a href="https://github.com/all-umass/metric-learn">
   metric-learn
  </a>
  - A Python module for metric learning.
  <sup>
   377 GitHub links in total 753 links, &#9733 172, pushed 178 days ago
  </sup>
 </li>
 <li>
  <a href="http://github.com/simpleai-team/simpleai">
   SimpleAI
  </a>
  Python implementation of many of the artificial intelligence algorithms described on the book "Artificial Intelligence, a Modern Approach". It focuses on providing an easy to use, well documented and tested library.
 </li>
 <li>
  <a href="http://www.astroml.org/">
   astroML
  </a>
  - Machine Learning and Data Mining for Astronomy.
 </li>
 <li>
  <a href="http://graphlab.com/products/create/docs/">
   graphlab-create
  </a>
  - A library with various machine learning models (regression, clustering, recommender systems, graph analytics, etc.) implemented on top of a disk-backed DataFrame.
 </li>
 <li>
  <a href="https://bigml.com">
   BigML
  </a>
  - A library that contacts external servers.
 </li>
 <li>
  <a href="https://github.com/clips/pattern">
   pattern
  </a>
  - Web mining module for Python.
  <sup>
   377 GitHub links in total 753 links, &#9733 4390, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/numenta/nupic">
   NuPIC
  </a>
  - Numenta Platform for Intelligent Computing.
  <sup>
   377 GitHub links in total 753 links, &#9733 4079, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/lisa-lab/pylearn2">
   Pylearn2
  </a>
  - A Machine Learning library based on
  <a href="https://github.com/Theano/Theano">
   Theano
  </a>
  .
  <sup>
   377 GitHub links in total 753 links, &#9733 2065, pushed 30 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/fchollet/keras">
   keras
  </a>
  - Modular neural network library based on
  <a href="https://github.com/Theano/Theano">
   Theano
  </a>
  .
  <sup>
   377 GitHub links in total 753 links, &#9733 5863, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/hannes-brt/hebel">
   hebel
  </a>
  - GPU-Accelerated Deep Learning Library in Python.
  <sup>
   377 GitHub links in total 753 links, &#9733 1137, pushed 264 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/pfnet/chainer">
   Chainer
  </a>
  - Flexible neural network framework
  <sup>
   377 GitHub links in total 753 links, &#9733 1354, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/piskvorky/gensim">
   gensim
  </a>
  - Topic Modelling for Humans.
  <sup>
   377 GitHub links in total 753 links, &#9733 2482, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/ContinuumIO/topik">
   topik
  </a>
  - Topic modelling toolkit
  <sup>
   377 GitHub links in total 753 links, &#9733 53, pushed 7 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/pybrain/pybrain">
   PyBrain
  </a>
  - Another Python Machine Learning Library.
  <sup>
   377 GitHub links in total 753 links, &#9733 1775, pushed 53 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/IDSIA/brainstorm">
   Brainstorm
  </a>
  - Fast, flexible and fun neural networks. This is the successor of PyBrain.
  <sup>
   377 GitHub links in total 753 links, &#9733 1090, pushed 10 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/muricoca/crab">
   Crab
  </a>
  - A ﬂexible, fast recommender engine.
  <sup>
   377 GitHub links in total 753 links, &#9733 667, pushed 1524 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/ocelma/python-recsys">
   python-recsys
  </a>
  - A Python library for implementing a Recommender System.
  <sup>
   377 GitHub links in total 753 links, &#9733 561, pushed 139 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/AllenDowney/ThinkBayes">
   thinking bayes
  </a>
  - Book on Bayesian Analysis
  <sup>
   377 GitHub links in total 753 links, &#9733 421, pushed 49 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/echen/restricted-boltzmann-machines">
   Restricted Boltzmann Machines
  </a>
  -Restricted Boltzmann Machines in Python. [DEEP LEARNING]
  <sup>
   377 GitHub links in total 753 links, &#9733 394, pushed 178 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/pprett/bolt">
   Bolt
  </a>
  - Bolt Online Learning Toolbox
  <sup>
   377 GitHub links in total 753 links, &#9733 66, pushed 1672 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/patvarilly/CoverTree">
   CoverTree
  </a>
  - Python implementation of cover trees, near-drop-in replacement for scipy.spatial.kdtree
  <sup>
   377 GitHub links in total 753 links, &#9733 14, pushed 1512 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/nilearn/nilearn">
   nilearn
  </a>
  - Machine learning for NeuroImaging in Python
  <sup>
   377 GitHub links in total 753 links, &#9733 166, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/shogun-toolbox/shogun">
   Shogun
  </a>
  - The Shogun Machine Learning Toolbox
 </li>
 <li>
  <a href="https://github.com/perone/Pyevolve">
   Pyevolve
  </a>
  - Genetic algorithm framework.
  <sup>
   377 GitHub links in total 753 links, &#9733 200, pushed 182 days ago
  </sup>
 </li>
 <li>
  <a href="http://caffe.berkeleyvision.org">
   Caffe
  </a>
  - A deep learning framework developed with cleanliness, readability, and speed in mind.
 </li>
 <li>
  <a href="https://github.com/breze-no-salt/breze">
   breze
  </a>
  - Theano based library for deep and recurrent neural networks
  <sup>
   377 GitHub links in total 753 links, &#9733 73, pushed 20 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/mattjj/pyhsmm">
   pyhsmm
  </a>
  - library for approximate unsupervised inference in Bayesian Hidden Markov Models (HMMs) and explicit-duration Hidden semi-Markov Models (HSMMs), focusing on the Bayesian Nonparametric extensions, the HDP-HMM and HDP-HSMM, mostly with weak-limit approximations.
  <sup>
   377 GitHub links in total 753 links, &#9733 216, pushed 32 days ago
  </sup>
 </li>
 <li>
  <a href="https://pythonhosted.org/mrjob/">
   mrjob
  </a>
  - A library to let Python program run on Hadoop.
 </li>
 <li>
  <a href="https://github.com/EducationalTestingService/skll">
   SKLL
  </a>
  - A wrapper around scikit-learn that makes it simpler to conduct experiments.
  <sup>
   377 GitHub links in total 753 links, &#9733 334, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/zueve/neurolab">
   neurolab
  </a>
  - https://github.com/zueve/neurolab
  <sup>
   377 GitHub links in total 753 links, &#9733 64, pushed 88 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/JasperSnoek/spearmint">
   Spearmint
  </a>
  - Spearmint is a package to perform Bayesian optimization according to the algorithms outlined in the paper: Practical Bayesian Optimization of Machine Learning Algorithms. Jasper Snoek, Hugo Larochelle and Ryan P. Adams. Advances in Neural Information Processing Systems, 2012.
  <sup>
   377 GitHub links in total 753 links, &#9733 648, pushed 81 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/abhik/pebl/">
   Pebl
  </a>
  - Python Environment for Bayesian Learning
 </li>
 <li>
  <a href="https://github.com/Theano/Theano/">
   Theano
  </a>
  - Optimizing GPU-meta-programming code generating array oriented optimizing math compiler in Python
 </li>
 <li>
  <a href="https://github.com/tensorflow/tensorflow/">
   TensorFlow
  </a>
  - Open source software library for numerical computation using data flow graphs
 </li>
 <li>
  <a href="https://github.com/jmschrei/yahmm/">
   yahmm
  </a>
  - Hidden Markov Models for Python, implemented in Cython for speed and efficiency.
 </li>
 <li>
  <a href="https://github.com/proycon/python-timbl">
   python-timbl
  </a>
  - A Python extension module wrapping the full TiMBL C++ programming interface. Timbl is an elaborate k-Nearest Neighbours machine learning toolkit.
  <sup>
   377 GitHub links in total 753 links, &#9733 5, pushed 51 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/deap/deap">
   deap
  </a>
  - Evolutionary algorithm framework.
  <sup>
   377 GitHub links in total 753 links, &#9733 549, pushed 20 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/andersbll/deeppy">
   pydeep
  </a>
  - Deep Learning In Python
  <sup>
   377 GitHub links in total 753 links, &#9733 875, pushed 27 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/rasbt/mlxtend">
   mlxtend
  </a>
  - A library consisting of useful tools for data science and machine learning tasks.
  <sup>
   377 GitHub links in total 753 links, &#9733 405, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/NervanaSystems/neon">
   neon
  </a>
  - Nervana's
  <a href="https://github.com/soumith/convnet-benchmarks">
   high-performance
  </a>
  Python-based Deep Learning framework [DEEP LEARNING]
  <sup>
   377 GitHub links in total 753 links, &#9733 1808, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="http://docs.optunity.net">
   Optunity
  </a>
  - A library dedicated to automated hyperparameter optimization with a simple, lightweight API to facilitate drop-in replacement of grid search.
 </li>
 <li>
  <a href="https://github.com/mnielsen/neural-networks-and-deep-learning">
   Neural Networks and Deep Learning
  </a>
  - Code samples for my book "Neural Networks and Deep Learning" [DEEP LEARNING]
  <sup>
   377 GitHub links in total 753 links, &#9733 1909, pushed 162 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/spotify/annoy">
   Annoy
  </a>
  - Approximate nearest neighbours implementation
  <sup>
   377 GitHub links in total 753 links, &#9733 1131, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/google/skflow">
   skflow
  </a>
  - Simplified interface for TensorFlow, mimicking Scikit Learn.
 </li>
 <li>
  <a href="https://github.com/rhiever/tpot">
   TPOT
  </a>
  - Tool that automatically creates and optimizes machine learning pipelines using genetic programming. Consider it your personal data science assistant, automating a tedious part of machine learning.
  <sup>
   377 GitHub links in total 753 links, &#9733 691, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/pgmpy/pgmpy">
   pgmpy
  </a>
  A python library for working with Probabilistic Graphical Models.
  <sup>
   377 GitHub links in total 753 links, &#9733 220, pushed 9 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/NVIDIA/DIGITS">
   DIGITS
  </a>
  - The Deep Learning GPU Training System (DIGITS) is a web application for training deep learning models.
  <sup>
   377 GitHub links in total 753 links, &#9733 1076, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="http://orange.biolab.si/">
   Orange
  </a>
  - Open source data visualization and data analysis for novices and experts.
 </li>
 <li>
  <a href="https://github.com/dmlc/mxnet">
   MXNet
  </a>
  - Lightweight, Portable, Flexible Distributed/Mobile Deep Learning with Dynamic, Mutation-aware Dataflow Dep Scheduler; for Python, R, Julia, Go, Javascript and more.
 </li>
 <li>
  <a href="https://github.com/luispedro/milk">
   milk
  </a>
  - Machine learning toolkit focused on supervised classification.
  <sup>
   377 GitHub links in total 753 links, &#9733 501, pushed 358 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/tflearn/tflearn">
   TFLearn
  </a>
  - Deep learning library featuring a higher-level API for TensorFlow.
  <sup>
   377 GitHub links in total 753 links, &#9733 2550, pushed 4 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="python-data-analysis">
 </a>
</p>
<h4>
 Data Analysis / Data Visualization
</h4>
<ul>
 <li>
  <a href="http://www.scipy.org/">
   SciPy
  </a>
  - A Python-based ecosystem of open-source software for mathematics, science, and engineering.
 </li>
 <li>
  <a href="http://www.numpy.org/">
   NumPy
  </a>
  - A fundamental package for scientific computing with Python.
 </li>
 <li>
  <a href="http://numba.pydata.org/">
   Numba
  </a>
  - Python JIT (just in time) complier to LLVM aimed at scientific Python by the developers of Cython and NumPy.
 </li>
 <li>
  <a href="https://networkx.github.io/">
   NetworkX
  </a>
  - A high-productivity software for complex networks.
 </li>
 <li>
  <a href="http://igraph.org/python/">
   igraph
  </a>
  - binding to igraph library - General purpose graph library
 </li>
 <li>
  <a href="http://pandas.pydata.org/">
   Pandas
  </a>
  - A library providing high-performance, easy-to-use data structures and data analysis tools.
 </li>
 <li>
  <a href="https://github.com/avelino/mining">
   Open Mining
  </a>
  - Business Intelligence (BI) in Python (Pandas web interface)
 </li>
 <li>
  <a href="https://github.com/pymc-devs/pymc">
   PyMC
  </a>
  - Markov Chain Monte Carlo sampling toolkit.
  <sup>
   377 GitHub links in total 753 links, &#9733 289, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/quantopian/zipline">
   zipline
  </a>
  - A Pythonic algorithmic trading library.
  <sup>
   377 GitHub links in total 753 links, &#9733 3154, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://pydy.org/">
   PyDy
  </a>
  - Short for Python Dynamics, used to assist with workflow in the modeling of dynamic motion based around NumPy, SciPy, IPython, and matplotlib.
 </li>
 <li>
  <a href="https://github.com/sympy/sympy">
   SymPy
  </a>
  - A Python library for symbolic mathematics.
  <sup>
   377 GitHub links in total 753 links, &#9733 2825, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/statsmodels/statsmodels">
   statsmodels
  </a>
  - Statistical modeling and econometrics in Python.
  <sup>
   377 GitHub links in total 753 links, &#9733 1418, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.astropy.org/">
   astropy
  </a>
  - A community Python library for Astronomy.
 </li>
 <li>
  <a href="http://matplotlib.org/">
   matplotlib
  </a>
  - A Python 2D plotting library.
 </li>
 <li>
  <a href="https://github.com/bokeh/bokeh">
   bokeh
  </a>
  - Interactive Web Plotting for Python.
  <sup>
   377 GitHub links in total 753 links, &#9733 4131, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://plot.ly/python/">
   plotly
  </a>
  - Collaborative web plotting for Python and matplotlib.
 </li>
 <li>
  <a href="https://github.com/wrobstory/vincent">
   vincent
  </a>
  - A Python to Vega translator.
  <sup>
   377 GitHub links in total 753 links, &#9733 1843, pushed 102 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/mikedewar/d3py">
   d3py
  </a>
  - A plotting library for Python, based on
  <a href="http://d3js.org/">
   D3.js
  </a>
  .
  <sup>
   377 GitHub links in total 753 links, &#9733 1105, pushed 211 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/yhat/ggplot">
   ggplot
  </a>
  - Same API as ggplot2 for R.
  <sup>
   377 GitHub links in total 753 links, &#9733 2487, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/sinhrks/ggfortify">
   ggfortify
  </a>
  - Unified interface to ggplot2 popular R packages.
  <sup>
   377 GitHub links in total 753 links, &#9733 180, pushed 10 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/kartograph/kartograph.py">
   Kartograph.py
  </a>
  - Rendering beautiful SVG maps in Python.
  <sup>
   377 GitHub links in total 753 links, &#9733 858, pushed 292 days ago
  </sup>
 </li>
 <li>
  <a href="http://pygal.org/">
   pygal
  </a>
  - A Python SVG Charts Creator.
 </li>
 <li>
  <a href="https://github.com/pyqtgraph/pyqtgraph">
   PyQtGraph
  </a>
  - A pure-python graphics and GUI library built on PyQt4 / PySide and NumPy.
  <sup>
   377 GitHub links in total 753 links, &#9733 401, pushed 8 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/twitter/pycascading">
   pycascading
  </a>
  <sup>
   377 GitHub links in total 753 links, &#9733 213, pushed 867 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/AirSage/Petrel">
   Petrel
  </a>
  - Tools for writing, submitting, debugging, and monitoring Storm topologies in pure Python.
  <sup>
   377 GitHub links in total 753 links, &#9733 227, pushed 14 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/blaze/blaze">
   Blaze
  </a>
  - NumPy and Pandas interface to Big Data.
  <sup>
   377 GitHub links in total 753 links, &#9733 1445, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/dfm/emcee">
   emcee
  </a>
  - The Python ensemble sampling toolkit for affine-invariant MCMC.
  <sup>
   377 GitHub links in total 753 links, &#9733 527, pushed 9 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.windml.org">
   windML
  </a>
  - A Python Framework for Wind Energy Analysis and Prediction
 </li>
 <li>
  <a href="https://github.com/vispy/vispy">
   vispy
  </a>
  - GPU-based high-performance interactive OpenGL 2D/3D data visualization library
  <sup>
   377 GitHub links in total 753 links, &#9733 1007, pushed 32 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/numenta/nupic.cerebro2">
   cerebro2
  </a>
  A web-based visualization and debugging platform for NuPIC.
  <sup>
   377 GitHub links in total 753 links, &#9733 13, pushed 259 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/nupic-community/nupic.studio">
   NuPIC Studio
  </a>
  An all-in-one NuPIC Hierarchical Temporal Memory visualization and debugging super-tool!
  <sup>
   377 GitHub links in total 753 links, &#9733 59, pushed 165 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/sparklingpandas/sparklingpandas">
   SparklingPandas
  </a>
  Pandas on PySpark (POPS)
  <sup>
   377 GitHub links in total 753 links, &#9733 248, pushed 218 days ago
  </sup>
 </li>
 <li>
  <a href="http://stanford.edu/~mwaskom/software/seaborn/">
   Seaborn
  </a>
  - A python visualization library based on matplotlib
 </li>
 <li>
  <a href="https://github.com/bloomberg/bqplot">
   bqplot
  </a>
  - An API for plotting in Jupyter (IPython)
  <sup>
   377 GitHub links in total 753 links, &#9733 838, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/rewonc/pastalog">
   pastalog
  </a>
  - Simple, realtime visualization of neural network training performance.
  <sup>
   377 GitHub links in total 753 links, &#9733 249, pushed 21 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/airbnb/caravel">
   caravel
  </a>
  - A data exploration platform designed to be visual, intuitive, and interactive.
  <sup>
   377 GitHub links in total 753 links, &#9733 5894, pushed 2 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="python-misc">
 </a>
</p>
<h4>
 Misc Scripts / iPython Notebooks / Codebases
</h4>
<ul>
 <li>
  <a href="https://github.com/jaredmichaelsmith/BioPy">
   BioPy
  </a>
  - Biologically-Inspired and Machine Learning Algorithms in Python.
  <sup>
   377 GitHub links in total 753 links, &#9733 7, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/rasbt/pattern_classification">
   pattern_classification
  </a>
  <sup>
   377 GitHub links in total 753 links, &#9733 1661, pushed 58 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Wavelets/ThinkStats2">
   thinking stats 2
  </a>
  <sup>
   377 GitHub links in total 753 links, &#9733 5, pushed 659 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/hyperopt/hyperopt-sklearn">
   hyperopt
  </a>
  <sup>
   377 GitHub links in total 753 links, &#9733 115, pushed 6 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/numenta/nupic">
   numpic
  </a>
  <sup>
   377 GitHub links in total 753 links, &#9733 4079, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/dib-lab/2012-paper-diginorm">
   2012-paper-diginorm
  </a>
  <sup>
   377 GitHub links in total 753 links, &#9733 7, pushed 348 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks">
   A gallery of interesting IPython notebooks
  </a>
 </li>
 <li>
  <a href="https://github.com/ogrisel/notebooks">
   ipython-notebooks
  </a>
  <sup>
   377 GitHub links in total 753 links, &#9733 293, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/donnemartin/data-science-ipython-notebooks">
   data-science-ipython-notebooks
  </a>
  - Continually updated Data Science Python Notebooks: Spark, Hadoop MapReduce, HDFS, AWS, Kaggle, scikit-learn, matplotlib, pandas, NumPy, SciPy, and various command lines.
  <sup>
   377 GitHub links in total 753 links, &#9733 5541, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/CamDavidsonPilon/decision-weights">
   decision-weights
  </a>
  <sup>
   377 GitHub links in total 753 links, &#9733 19, pushed 428 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Wavelets/sarah-palin-lda">
   Sarah Palin LDA
  </a>
  - Topic Modeling the Sarah Palin emails.
  <sup>
   377 GitHub links in total 753 links, &#9733 8, pushed 1760 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Wavelets/diffusion-segmentation">
   Diffusion Segmentation
  </a>
  - A collection of image segmentation algorithms based on diffusion methods
  <sup>
   377 GitHub links in total 753 links, &#9733 2, pushed 2077 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Wavelets/scipy-tutorials">
   Scipy Tutorials
  </a>
  - SciPy tutorials. This is outdated, check out scipy-lecture-notes
  <sup>
   377 GitHub links in total 753 links, &#9733 1, pushed 2176 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/marcelcaraciolo/crab">
   Crab
  </a>
  - A recommendation engine library for Python
  <sup>
   377 GitHub links in total 753 links, &#9733 71, pushed 1705 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/maxsklar/BayesPy">
   BayesPy
  </a>
  - Bayesian Inference Tools in Python
  <sup>
   377 GitHub links in total 753 links, &#9733 35, pushed 55 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/GaelVaroquaux/scikit-learn-tutorial">
   scikit-learn tutorials
  </a>
  - Series of notebooks for learning scikit-learn
  <sup>
   377 GitHub links in total 753 links, &#9733 55, pushed 1610 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/madhusudancs/sentiment-analyzer">
   sentiment-analyzer
  </a>
  - Tweets Sentiment Analyzer
  <sup>
   377 GitHub links in total 753 links, &#9733 26, pushed 1495 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/kevincobain2000/sentiment_classifier">
   sentiment_classifier
  </a>
  - Sentiment classifier using word sense disambiguation.
  <sup>
   377 GitHub links in total 753 links, &#9733 60, pushed 39 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/fabianp/group_lasso">
   group-lasso
  </a>
  - Some experiments with the coordinate descent algorithm used in the (Sparse) Group Lasso model
  <sup>
   377 GitHub links in total 753 links, &#9733 6, pushed 1287 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/kevincobain2000/jProcessing">
   jProcessing
  </a>
  - Kanji / Hiragana / Katakana to Romaji Converter. Edict Dictionary & parallel sentences Search. Sentence Similarity between two JP Sentences. Sentiment Analysis of Japanese Text. Run Cabocha(ISO--8859-1 configured) in Python.
  <sup>
   377 GitHub links in total 753 links, &#9733 34, pushed 146 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/mne-tools/mne-python-notebooks">
   mne-python-notebooks
  </a>
  - IPython notebooks for EEG/MEG data processing using mne-python
  <sup>
   377 GitHub links in total 753 links, &#9733 2, pushed 23 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jvns/pandas-cookbook">
   pandas cookbook
  </a>
  - Recipes for using Python's pandas library
  <sup>
   377 GitHub links in total 753 links, &#9733 1510, pushed 9 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/BRML/climin">
   climin
  </a>
  - Optimization library focused on machine learning, pythonic implementations of gradient descent, LBFGS, rmsprop, adadelta and others
  <sup>
   377 GitHub links in total 753 links, &#9733 100, pushed 69 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/AllenDowney/DataScience">
   Allen Downey’s Data Science Course
  </a>
  - Code for Data Science at Olin College, Spring 2014.
  <sup>
   377 GitHub links in total 753 links, &#9733 19, pushed 740 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/AllenDowney/ThinkBayes">
   Allen Downey’s Think Bayes Code
  </a>
  - Code repository for Think Bayes.
  <sup>
   377 GitHub links in total 753 links, &#9733 421, pushed 49 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/AllenDowney/ThinkComplexity">
   Allen Downey’s Think Complexity Code
  </a>
  - Code for Allen Downey's book Think Complexity.
  <sup>
   377 GitHub links in total 753 links, &#9733 46, pushed 285 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/AllenDowney/ThinkOS">
   Allen Downey’s Think OS Code
  </a>
  - Text and supporting code for Think OS: A Brief Introduction to Operating Systems.
  <sup>
   377 GitHub links in total 753 links, &#9733 120, pushed 71 days ago
  </sup>
 </li>
 <li>
  <a href="http://fbkarsdorp.github.io/python-course/">
   Python Programming for the Humanities
  </a>
  - Course for Python programming for the Humanities, assuming no prior knowledge. Heavy focus on text processing / NLP.
 </li>
 <li>
  <a href="https://github.com/mwgg/GreatCircle">
   GreatCircle
  </a>
  - Library for calculating great circle distance.
 </li>
 <li>
  <a href="http://docs.optunity.net/notebooks/index.html">
   Optunity examples
  </a>
  - Examples demonstrating how to use Optunity in synergy with machine learning libraries.
 </li>
 <li>
  <a href="https://github.com/hangtwenty/dive-into-machine-learning">
   Dive into Machine Learning  with Python Jupyter notebook and scikit-learn
  </a>
  - "I learned Python by hacking first, and getting serious
  <em>
   later.
  </em>
  I wanted to do this with Machine Learning. If this is your style, join me in getting a bit ahead of yourself."
  <sup>
   377 GitHub links in total 753 links, &#9733 5160, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/ericjang/tdb">
   TDB
  </a>
  - TensorDebugger (TDB) is a visual debugger for deep learning. It features interactive, node-by-node debugging and visualization for TensorFlow.
  <sup>
   377 GitHub links in total 753 links, &#9733 773, pushed 62 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="python-kaggle">
 </a>
</p>
<h4>
 Kaggle Competition Source Code
</h4>
<ul>
 <li>
  <a href="https://github.com/hammer/wikichallenge">
   wiki challenge
  </a>
  - An implementation of Dell Zhang's solution to Wikipedia's Participation Challenge on Kaggle
  <sup>
   377 GitHub links in total 753 links, &#9733 5, pushed 1623 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/amueller/kaggle_insults">
   kaggle insults
  </a>
  - Kaggle Submission for "Detecting Insults in Social Commentary"
  <sup>
   377 GitHub links in total 753 links, &#9733 96, pushed 218 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/MLWave/kaggle_acquire-valued-shoppers-challenge">
   kaggle_acquire-valued-shoppers-challenge
  </a>
  - Code for the Kaggle acquire valued shoppers challenge
  <sup>
   377 GitHub links in total 753 links, &#9733 37, pushed 747 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/zygmuntz/kaggle-cifar">
   kaggle-cifar
  </a>
  - Code for the CIFAR-10 competition at Kaggle, uses cuda-convnet
  <sup>
   377 GitHub links in total 753 links, &#9733 34, pushed 682 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/zygmuntz/kaggle-blackbox">
   kaggle-blackbox
  </a>
  - Deep learning made easy
  <sup>
   377 GitHub links in total 753 links, &#9733 110, pushed 682 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/zygmuntz/kaggle-accelerometer">
   kaggle-accelerometer
  </a>
  - Code for Accelerometer Biometric Competition at Kaggle
  <sup>
   377 GitHub links in total 753 links, &#9733 7, pushed 682 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/zygmuntz/kaggle-advertised-salaries">
   kaggle-advertised-salaries
  </a>
  - Predicting job salaries from ads - a Kaggle competition
  <sup>
   377 GitHub links in total 753 links, &#9733 44, pushed 682 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/zygmuntz/kaggle-amazon">
   kaggle amazon
  </a>
  - Amazon access control challenge
  <sup>
   377 GitHub links in total 753 links, &#9733 15, pushed 682 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/zygmuntz/kaggle-bestbuy_big">
   kaggle-bestbuy_big
  </a>
  - Code for the Best Buy competition at Kaggle
  <sup>
   377 GitHub links in total 753 links, &#9733 2, pushed 682 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/zygmuntz/kaggle-bestbuy_small">
   kaggle-bestbuy_small
  </a>
  <sup>
   377 GitHub links in total 753 links, &#9733 2, pushed 682 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/kastnerkyle/kaggle-dogs-vs-cats">
   Kaggle Dogs vs. Cats
  </a>
  - Code for Kaggle Dogs vs. Cats competition
  <sup>
   377 GitHub links in total 753 links, &#9733 48, pushed 822 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/benanne/kaggle-galaxies">
   Kaggle Galaxy Challenge
  </a>
  - Winning solution for the Galaxy Challenge on Kaggle
  <sup>
   377 GitHub links in total 753 links, &#9733 313, pushed 629 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/zygmuntz/kaggle-gender">
   Kaggle Gender
  </a>
  - A Kaggle competition: discriminate gender based on handwriting
  <sup>
   377 GitHub links in total 753 links, &#9733 4, pushed 682 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/zygmuntz/kaggle-merck">
   Kaggle Merck
  </a>
  - Merck challenge at Kaggle
  <sup>
   377 GitHub links in total 753 links, &#9733 3, pushed 682 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/zygmuntz/kaggle-stackoverflow">
   Kaggle Stackoverflow
  </a>
  - Predicting closed questions on Stack Overflow
  <sup>
   377 GitHub links in total 753 links, &#9733 29, pushed 682 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/MLWave/kaggle_acquire-valued-shoppers-challenge">
   kaggle_acquire-valued-shoppers-challenge
  </a>
  - Code for the Kaggle acquire valued shoppers challenge
 </li>
 <li>
  <a href="https://github.com/zygmuntz/wine-quality">
   wine-quality
  </a>
  - Predicting wine quality
  <sup>
   377 GitHub links in total 753 links, &#9733 5, pushed 243 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="ruby">
 </a>
</p>
<h2>
 Ruby
</h2>
<p>
 <a name="ruby-nlp">
 </a>
</p>
<h4>
 Natural Language Processing
</h4>
<ul>
 <li>
  <a href="https://github.com/louismullie/treat">
   Treat
  </a>
  -  Text REtrieval and Annotation Toolkit, definitely the most comprehensive toolkit I’ve encountered so far for Ruby
  <sup>
   377 GitHub links in total 753 links, &#9733 1154, pushed 60 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.deveiate.org/projects/Linguistics/">
   Ruby Linguistics
  </a>
  -  Linguistics is a framework for building linguistic utilities for Ruby objects in any language. It includes a generic language-independent front end, a module for mapping language codes into language names, and a module which contains various English-language utilities.
 </li>
 <li>
  <a href="https://github.com/aurelian/ruby-stemmer">
   Stemmer
  </a>
  - Expose libstemmer_c to Ruby
  <sup>
   377 GitHub links in total 753 links, &#9733 202, pushed 85 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.deveiate.org/projects/Ruby-WordNet/">
   Ruby Wordnet
  </a>
  - This library is a Ruby interface to WordNet
 </li>
 <li>
  <a href="http://sourceforge.net/projects/raspell/">
   Raspel
  </a>
  - raspell is an interface binding for ruby
 </li>
 <li>
  <a href="https://github.com/ealdent/uea-stemmer">
   UEA Stemmer
  </a>
  - Ruby port of UEALite Stemmer - a conservative stemmer for search and indexing
  <sup>
   377 GitHub links in total 753 links, &#9733 38, pushed 251 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/twitter/twitter-text-rb">
   Twitter-text-rb
  </a>
  - A library that does auto linking and extraction of usernames, lists and hashtags in tweets
  <sup>
   377 GitHub links in total 753 links, &#9733 634, pushed 507 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="ruby-general-purpose">
 </a>
</p>
<h4>
 General-Purpose Machine Learning
</h4>
<ul>
 <li>
  <a href="https://github.com/tsycho/ruby-machine-learning">
   Ruby Machine Learning
  </a>
  - Some Machine Learning algorithms, implemented in Ruby
  <sup>
   377 GitHub links in total 753 links, &#9733 23, pushed 1575 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/mizoR/machine-learning-ruby">
   Machine Learning Ruby
  </a>
  <sup>
   377 GitHub links in total 753 links, &#9733 12, pushed 1335 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/vasinov/jruby_mahout">
   jRuby Mahout
  </a>
  - JRuby Mahout is a gem that unleashes the power of Apache Mahout in the world of JRuby.
  <sup>
   377 GitHub links in total 753 links, &#9733 161, pushed 226 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/cardmagic/classifier">
   CardMagic-Classifier
  </a>
  - A general classifier module to allow Bayesian and other types of classifications.
  <sup>
   377 GitHub links in total 753 links, &#9733 566, pushed 847 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/febeling/rb-libsvm">
   rb-libsvm
  </a>
  - Ruby language bindings for LIBSVM which is a Library for Support Vector Machines
  <sup>
   377 GitHub links in total 753 links, &#9733 210, pushed 227 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="ruby-data-analysis">
 </a>
</p>
<h4>
 Data Analysis / Data Visualization
</h4>
<ul>
 <li>
  <a href="https://github.com/alexgutteridge/rsruby">
   rsruby
  </a>
  - Ruby - R bridge
  <sup>
   377 GitHub links in total 753 links, &#9733 295, pushed 1616 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/chrislo/data_visualisation_ruby">
   data-visualization-ruby
  </a>
  - Source code and supporting content for my Ruby Manor presentation on Data Visualisation with Ruby
  <sup>
   377 GitHub links in total 753 links, &#9733 67, pushed 2324 days ago
  </sup>
 </li>
 <li>
  <a href="https://www.ruby-toolbox.com/projects/ruby-plot">
   ruby-plot
  </a>
  - gnuplot wrapper for ruby, especially for plotting roc curves into svg files
 </li>
 <li>
  <a href="https://github.com/zuhao/plotrb">
   plot-rb
  </a>
  - A plotting library in Ruby built on top of Vega and D3.
  <sup>
   377 GitHub links in total 753 links, &#9733 33, pushed 953 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.rubyinside.com/scruffy-a-beautiful-graphing-toolkit-for-ruby-194.html">
   scruffy
  </a>
  - A beautiful graphing toolkit for Ruby
 </li>
 <li>
  <a href="http://sciruby.com/">
   SciRuby
  </a>
 </li>
 <li>
  <a href="https://github.com/glean/glean">
   Glean
  </a>
  - A data management tool for humans
  <sup>
   377 GitHub links in total 753 links, &#9733 113, pushed 664 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/bioruby/bioruby">
   Bioruby
  </a>
  <sup>
   377 GitHub links in total 753 links, &#9733 288, pushed 43 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/nkallen/arel">
   Arel
  </a>
  <sup>
   377 GitHub links in total 753 links, &#9733 239, pushed 2539 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="ruby-misc">
 </a>
</p>
<h4>
 Misc
</h4>
<ul>
 <li>
  <a href="https://github.com/infochimps-labs/big_data_for_chimps">
   Big Data For Chimps
  </a>
  <sup>
   377 GitHub links in total 753 links, &#9733 149, pushed 323 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/kevincobain2000/listof">
   Listof
  </a>
  - Community based data collection, packed in gem. Get list of pretty much anything (stop words, countries, non words) in txt, json or hash.
  <a href="http://listof.herokuapp.com/">
   Demo/Search for a list
  </a>
  <sup>
   377 GitHub links in total 753 links, &#9733 8, pushed 50 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="rust">
 </a>
</p>
<h2>
 Rust
</h2>
<p>
 <a name="rust-general-purpose">
 </a>
</p>
<h4>
 General-Purpose Machine Learning
</h4>
<ul>
 <li>
  <a href="https://github.com/tedsta/deeplearn-rs">
   deeplearn-rs
  </a>
  - deeplearn-rs provides simple networks that use matrix multiplication, addition, and ReLU under the MIT license.
  <sup>
   377 GitHub links in total 753 links, &#9733 84, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/maciejkula/rustlearn">
   rustlearn
  </a>
  - a machine learning framework featuring logistic regression, support vector machines, decision trees and random forests.
  <sup>
   377 GitHub links in total 753 links, &#9733 142, pushed 63 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/AtheMathmo/rusty-machine">
   rusty-machine
  </a>
  - a pure-rust machine learning library.
  <sup>
   377 GitHub links in total 753 links, &#9733 129, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/autumnai/leaf">
   leaf
  </a>
  - open source framework for machine intelligence, sharing concepts from TensorFlow and Caffe.  Available under the MIT license.
  <sup>
   377 GitHub links in total 753 links, &#9733 4007, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jackm321/RustNN">
   RustNN
  </a>
  - RustNN is a feedforward neural network library.
  <sup>
   377 GitHub links in total 753 links, &#9733 243, pushed 227 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="r">
 </a>
</p>
<h2>
 R
</h2>
<p>
 <a name="r-general-purpose">
 </a>
</p>
<h4>
 General-Purpose Machine Learning
</h4>
<ul>
 <li>
  <a href="http://cran.r-project.org/web/packages/ahaz/index.html">
   ahaz
  </a>
  - ahaz: Regularization for semiparametric additive hazards regression
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/arules/index.html">
   arules
  </a>
  - arules: Mining Association Rules and Frequent Itemsets
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/bigrf/index.html">
   bigrf
  </a>
  - bigrf: Big Random Forests: Classification and Regression Forests for Large Data Sets
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/bigRR/index.html">
   bigRR
  </a>
  - bigRR: Generalized Ridge Regression (with special advantage for p >> n cases)
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/bmrm/index.html">
   bmrm
  </a>
  - bmrm: Bundle Methods for Regularized Risk Minimization Package
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/Boruta/index.html">
   Boruta
  </a>
  - Boruta: A wrapper algorithm for all-relevant feature selection
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/bst/index.html">
   bst
  </a>
  - bst: Gradient Boosting
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/C50/index.html">
   C50
  </a>
  - C50: C5.0 Decision Trees and Rule-Based Models
 </li>
 <li>
  <a href="http://caret.r-forge.r-project.org/">
   caret
  </a>
  - Classification and Regression Training: Unified interface to ~150 ML algorithms in R.
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/caretEnsemble/index.html">
   caretEnsemble
  </a>
  - caretEnsemble: Framework for fitting multiple caret models as well as creating ensembles of such models.
 </li>
 <li>
  <a href="https://github.com/jbrownlee/CleverAlgorithmsMachineLearning">
   Clever Algorithms For Machine Learning
  </a>
  <sup>
   377 GitHub links in total 753 links, &#9733 176, pushed 1115 days ago
  </sup>
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/CORElearn/index.html">
   CORElearn
  </a>
  - CORElearn: Classification, regression, feature evaluation and ordinal evaluation
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/CoxBoost/index.html">
   CoxBoost
  </a>
  - CoxBoost: Cox models by likelihood based boosting for a single survival endpoint or competing risks
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/Cubist/index.html">
   Cubist
  </a>
  - Cubist: Rule- and Instance-Based Regression Modeling
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/e1071/index.html">
   e1071
  </a>
  - e1071: Misc Functions of the Department of Statistics (e1071), TU Wien
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/earth/index.html">
   earth
  </a>
  - earth: Multivariate Adaptive Regression Spline Models
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/elasticnet/index.html">
   elasticnet
  </a>
  - elasticnet: Elastic-Net for Sparse Estimation and Sparse PCA
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/ElemStatLearn/index.html">
   ElemStatLearn
  </a>
  - ElemStatLearn: Data sets, functions and examples from the book: "The Elements of Statistical Learning, Data Mining, Inference, and Prediction" by Trevor Hastie, Robert Tibshirani and Jerome Friedman Prediction" by Trevor Hastie, Robert Tibshirani and Jerome Friedman
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/evtree/index.html">
   evtree
  </a>
  - evtree: Evolutionary Learning of Globally Optimal Trees
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/fpc/index.html">
   fpc
  </a>
  - fpc: Flexible procedures for clustering
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/frbs/index.html">
   frbs
  </a>
  - frbs: Fuzzy Rule-based Systems for Classification and Regression Tasks
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/GAMBoost/index.html">
   GAMBoost
  </a>
  - GAMBoost: Generalized linear and additive models by likelihood based boosting
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/gamboostLSS/index.html">
   gamboostLSS
  </a>
  - gamboostLSS: Boosting Methods for GAMLSS
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/gbm/index.html">
   gbm
  </a>
  - gbm: Generalized Boosted Regression Models
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/glmnet/index.html">
   glmnet
  </a>
  - glmnet: Lasso and elastic-net regularized generalized linear models
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/glmpath/index.html">
   glmpath
  </a>
  - glmpath: L1 Regularization Path for Generalized Linear Models and Cox Proportional Hazards Model
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/GMMBoost/index.html">
   GMMBoost
  </a>
  - GMMBoost: Likelihood-based Boosting for Generalized mixed models
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/grplasso/index.html">
   grplasso
  </a>
  - grplasso: Fitting user specified models with Group Lasso penalty
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/grpreg/index.html">
   grpreg
  </a>
  - grpreg: Regularization paths for regression models with grouped covariates
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/h2o/index.html">
   h2o
  </a>
  - A framework for fast, parallel, and distributed machine learning algorithms at scale -- Deeplearning, Random forests, GBM, KMeans, PCA, GLM
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/hda/index.html">
   hda
  </a>
  - hda: Heteroscedastic Discriminant Analysis
 </li>
 <li>
  <a href="http://www-bcf.usc.edu/~gareth/ISL/">
   Introduction to Statistical Learning
  </a>
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/ipred/index.html">
   ipred
  </a>
  - ipred: Improved Predictors
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/kernlab/index.html">
   kernlab
  </a>
  - kernlab: Kernel-based Machine Learning Lab
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/klaR/index.html">
   klaR
  </a>
  - klaR: Classification and visualization
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/lars/index.html">
   lars
  </a>
  - lars: Least Angle Regression, Lasso and Forward Stagewise
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/lasso2/index.html">
   lasso2
  </a>
  - lasso2: L1 constrained estimation aka ‘lasso’
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/LiblineaR/index.html">
   LiblineaR
  </a>
  - LiblineaR: Linear Predictive Models Based On The Liblinear C/C++ Library
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/LogicReg/index.html">
   LogicReg
  </a>
  - LogicReg: Logic Regression
 </li>
 <li>
  <a href="https://github.com/johnmyleswhite/ML_for_Hackers">
   Machine Learning For Hackers
  </a>
  <sup>
   377 GitHub links in total 753 links, &#9733 2309, pushed 56 days ago
  </sup>
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/maptree/index.html">
   maptree
  </a>
  - maptree: Mapping, pruning, and graphing tree models
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/mboost/index.html">
   mboost
  </a>
  - mboost: Model-Based Boosting
 </li>
 <li>
  <a href="https://www.kaggle.com/forums/f/15/kaggle-forum/t/3661/medley-a-new-r-package-for-blending-regression-models/21278">
   medley
  </a>
  - medley: Blending regression models, using a greedy stepwise approach
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/mlr/index.html">
   mlr
  </a>
  - mlr: Machine Learning in R
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/mvpart/index.html">
   mvpart
  </a>
  - mvpart: Multivariate partitioning
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/ncvreg/index.html">
   ncvreg
  </a>
  - ncvreg: Regularization paths for SCAD- and MCP-penalized regression models
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/nnet/index.html">
   nnet
  </a>
  - nnet: Feed-forward Neural Networks and Multinomial Log-Linear Models
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/oblique.tree/index.html">
   oblique.tree
  </a>
  - oblique.tree: Oblique Trees for Classification Data
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/pamr/index.html">
   pamr
  </a>
  - pamr: Pam: prediction analysis for microarrays
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/party/index.html">
   party
  </a>
  - party: A Laboratory for Recursive Partytioning
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/partykit/index.html">
   partykit
  </a>
  - partykit: A Toolkit for Recursive Partytioning
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/penalized/index.html">
   penalized
  </a>
  - penalized: L1 (lasso and fused lasso) and L2 (ridge) penalized estimation in GLMs and in the Cox model
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/penalizedLDA/index.html">
   penalizedLDA
  </a>
  - penalizedLDA: Penalized classification using Fisher's linear discriminant
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/penalizedSVM/index.html">
   penalizedSVM
  </a>
  - penalizedSVM: Feature Selection SVM using penalty functions
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/quantregForest/index.html">
   quantregForest
  </a>
  - quantregForest: Quantile Regression Forests
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/randomForest/index.html">
   randomForest
  </a>
  - randomForest: Breiman and Cutler's random forests for classification and regression
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/randomForestSRC/index.html">
   randomForestSRC
  </a>
  - randomForestSRC: Random Forests for Survival, Regression and Classification (RF-SRC)
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/rattle/index.html">
   rattle
  </a>
  - rattle: Graphical user interface for data mining in R
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/rda/index.html">
   rda
  </a>
  - rda: Shrunken Centroids Regularized Discriminant Analysis
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/rdetools/index.html">
   rdetools
  </a>
  - rdetools: Relevant Dimension Estimation (RDE) in Feature Spaces
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/REEMtree/index.html">
   REEMtree
  </a>
  - REEMtree: Regression Trees with Random Effects for Longitudinal (Panel) Data
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/relaxo/index.html">
   relaxo
  </a>
  - relaxo: Relaxed Lasso
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/rgenoud/index.html">
   rgenoud
  </a>
  - rgenoud: R version of GENetic Optimization Using Derivatives
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/rgp/index.html">
   rgp
  </a>
  - rgp: R genetic programming framework
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/Rmalschains/index.html">
   Rmalschains
  </a>
  - Rmalschains: Continuous Optimization using Memetic Algorithms with Local Search Chains (MA-LS-Chains) in R
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/rminer/index.html">
   rminer
  </a>
  - rminer: Simpler use of data mining methods (e.g. NN and SVM) in classification and regression
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/ROCR/index.html">
   ROCR
  </a>
  - ROCR: Visualizing the performance of scoring classifiers
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/RoughSets/index.html">
   RoughSets
  </a>
  - RoughSets: Data Analysis Using Rough Set and Fuzzy Rough Set Theories
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/rpart/index.html">
   rpart
  </a>
  - rpart: Recursive Partitioning and Regression Trees
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/RPMM/index.html">
   RPMM
  </a>
  - RPMM: Recursively Partitioned Mixture Model
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/RSNNS/index.html">
   RSNNS
  </a>
  - RSNNS: Neural Networks in R using the Stuttgart Neural Network Simulator (SNNS)
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/RWeka/index.html">
   RWeka
  </a>
  - RWeka: R/Weka interface
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/RXshrink/index.html">
   RXshrink
  </a>
  - RXshrink: Maximum Likelihood Shrinkage via Generalized Ridge or Least Angle Regression
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/sda/index.html">
   sda
  </a>
  - sda: Shrinkage Discriminant Analysis and CAT Score Variable Selection
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/SDDA/index.html">
   SDDA
  </a>
  - SDDA: Stepwise Diagonal Discriminant Analysis
 </li>
 <li>
  <a href="https://github.com/ecpolley/SuperLearner">
   SuperLearner
  </a>
  and
  <a href="http://cran.r-project.org/web/packages/subsemble/index.html">
   subsemble
  </a>
  - Multi-algorithm ensemble learning packages.
  <sup>
   377 GitHub links in total 753 links, &#9733 55, pushed 22 days ago
  </sup>
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/svmpath/index.html">
   svmpath
  </a>
  - svmpath: svmpath: the SVM Path algorithm
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/tgp/index.html">
   tgp
  </a>
  - tgp: Bayesian treed Gaussian process models
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/tree/index.html">
   tree
  </a>
  - tree: Classification and regression trees
 </li>
 <li>
  <a href="http://cran.r-project.org/web/packages/varSelRF/index.html">
   varSelRF
  </a>
  - varSelRF: Variable selection using random forests
 </li>
 <li>
  <a href="https://github.com/tqchen/xgboost/tree/master/R-package">
   XGBoost.R
  </a>
  - R binding for eXtreme Gradient Boosting (Tree) Library
 </li>
 <li>
  <a href="http://docs.optunity.net">
   Optunity
  </a>
  - A library dedicated to automated hyperparameter optimization with a simple, lightweight API to facilitate drop-in replacement of grid search. Optunity is written in Python but interfaces seamlessly to R.
 </li>
 <li>
  <a href="http://igraph.org/r/">
   igraph
  </a>
  - binding to igraph library - General purpose graph library
 </li>
 <li>
  <a href="https://github.com/dmlc/mxnet">
   MXNet
  </a>
  - Lightweight, Portable, Flexible Distributed/Mobile Deep Learning with Dynamic, Mutation-aware Dataflow Dep Scheduler; for Python, R, Julia, Go, Javascript and more.
 </li>
</ul>
<p>
 <a name="r-data-analysis">
 </a>
</p>
<h4>
 Data Analysis / Data Visualization
</h4>
<ul>
 <li>
  <a href="http://ggplot2.org/">
   ggplot2
  </a>
  - A data visualization package based on the grammar of graphics.
 </li>
</ul>
<p>
 <a name="sas">
 </a>
</p>
<h2>
 SAS
</h2>
<p>
 <a name="sas-general-purpose">
 </a>
</p>
<h4>
 General-Purpose Machine Learning
</h4>
<ul>
 <li>
  <a href="http://www.sas.com/en_us/software/analytics/enterprise-miner.html">
   Enterprise Miner
  </a>
  - Data mining and machine learning that creates deployable models using a GUI or code.
 </li>
 <li>
  <a href="http://www.sas.com/en_us/software/analytics/factory-miner.html">
   Factory Miner
  </a>
  - Automatically creates deployable machine learning models across numerous market or customer segments using a GUI.
 </li>
</ul>
<p>
 <a name="sas-data-analysis">
 </a>
</p>
<h4>
 Data Analysis / Data Visualization
</h4>
<ul>
 <li>
  <a href="http://www.sas.com/en_us/software/analytics/stat.html">
   SAS/STAT
  </a>
  - For conducting advanced statistical analysis.
 </li>
 <li>
  <a href="http://www.sas.com/en_us/software/university-edition.html">
   University Edition
  </a>
  - FREE! Includes all SAS packages necessary for data analysis and visualization, and includes online SAS courses.
 </li>
</ul>
<p>
 <a name="sas-mpp">
 </a>
</p>
<h4>
 High Performance Machine Learning
</h4>
<ul>
 <li>
  <a href="http://www.sas.com/en_us/software/analytics/high-performance-data-mining.html">
   High Performance Data Mining
  </a>
  - Data mining and machine learning that creates deployable models using a GUI or code in an MPP environment, including Hadoop.
 </li>
 <li>
  <a href="http://www.sas.com/en_us/software/analytics/high-performance-text-mining.html">
   High Performance Text Mining
  </a>
  - Text mining using a GUI or code in an MPP environment, including Hadoop.
 </li>
</ul>
<p>
 <a name="sas-nlp">
 </a>
</p>
<h4>
 Natural Language Processing
</h4>
<ul>
 <li>
  <a href="http://www.sas.com/en_us/software/analytics/contextual-analysis.html">
   Contextual Analysis
  </a>
  - Add structure to unstructured text using a GUI.
 </li>
 <li>
  <a href="http://www.sas.com/en_us/software/analytics/sentiment-analysis.html">
   Sentiment Analysis
  </a>
  - Extract sentiment from text using a GUI.
 </li>
 <li>
  <a href="http://www.sas.com/en_us/software/analytics/text-miner.html">
   Text Miner
  </a>
  - Text mining using a GUI or code.
 </li>
</ul>
<p>
 <a name="sas-demos">
 </a>
</p>
<h4>
 Demos and Scripts
</h4>
<ul>
 <li>
  <a href="https://github.com/sassoftware/enlighten-apply/tree/master/ML_tables">
   ML_Tables
  </a>
  - Concise cheat sheets containing machine learning best practices.
 </li>
 <li>
  <a href="https://github.com/sassoftware/enlighten-apply">
   enlighten-apply
  </a>
  - Example code and materials that illustrate applications of SAS machine learning techniques.
  <sup>
   377 GitHub links in total 753 links, &#9733 37, pushed 6 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/sassoftware/enlighten-integration">
   enlighten-integration
  </a>
  - Example code and materials that illustrate techniques for integrating SAS with other analytics technologies in Java, PMML, Python and R.
  <sup>
   377 GitHub links in total 753 links, &#9733 23, pushed 11 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/sassoftware/enlighten-deep">
   enlighten-deep
  </a>
  - Example code and materials that illustrate using neural networks with several hidden layers in SAS.
  <sup>
   377 GitHub links in total 753 links, &#9733 5, pushed 170 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/sassoftware/dm-flow">
   dm-flow
  </a>
  - Library of SAS Enterprise Miner process flow diagrams to help you learn by example about specific data mining topics.
  <sup>
   377 GitHub links in total 753 links, &#9733 9, pushed 19 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="scala">
 </a>
</p>
<h2>
 Scala
</h2>
<p>
 <a name="scala-nlp">
 </a>
</p>
<h4>
 Natural Language Processing
</h4>
<ul>
 <li>
  <a href="http://www.scalanlp.org/">
   ScalaNLP
  </a>
  - ScalaNLP is a suite of machine learning and numerical computing libraries.
 </li>
 <li>
  <a href="https://github.com/scalanlp/breeze">
   Breeze
  </a>
  - Breeze is a numerical processing library for Scala.
  <sup>
   377 GitHub links in total 753 links, &#9733 1500, pushed 8 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/scalanlp/chalk">
   Chalk
  </a>
  - Chalk is a natural language processing library.
  <sup>
   377 GitHub links in total 753 links, &#9733 200, pushed 565 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/factorie/factorie">
   FACTORIE
  </a>
  - FACTORIE is a toolkit for deployable probabilistic modeling, implemented as a software library in Scala. It provides its users with a succinct language for creating relational factor graphs, estimating parameters and performing inference.
  <sup>
   377 GitHub links in total 753 links, &#9733 403, pushed 5 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="scala-data-analysis">
 </a>
</p>
<h4>
 Data Analysis / Data Visualization
</h4>
<ul>
 <li>
  <a href="http://spark.apache.org/docs/latest/mllib-guide.html">
   MLlib in Apache Spark
  </a>
  - Distributed machine learning library in Spark
 </li>
 <li>
  <a href="https://github.com/twitter/scalding">
   Scalding
  </a>
  - A Scala API for Cascading
  <sup>
   377 GitHub links in total 753 links, &#9733 2496, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/twitter/summingbird">
   Summing Bird
  </a>
  - Streaming MapReduce with Scalding and Storm
  <sup>
   377 GitHub links in total 753 links, &#9733 1706, pushed 87 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/twitter/algebird">
   Algebird
  </a>
  - Abstract Algebra for Scala
  <sup>
   377 GitHub links in total 753 links, &#9733 1215, pushed 6 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/xerial/xerial">
   xerial
  </a>
  - Data management utilities for Scala
  <sup>
   377 GitHub links in total 753 links, &#9733 14, pushed 54 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/avibryant/simmer">
   simmer
  </a>
  - Reduce your data. A unix filter for algebird-powered aggregation.
  <sup>
   377 GitHub links in total 753 links, &#9733 123, pushed 1076 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/PredictionIO/PredictionIO">
   PredictionIO
  </a>
  - PredictionIO, a machine learning server for software developers and data engineers.
  <sup>
   377 GitHub links in total 753 links, &#9733 9075, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/BIDData/BIDMat">
   BIDMat
  </a>
  - CPU and GPU-accelerated matrix library intended to support large-scale exploratory data analysis.
  <sup>
   377 GitHub links in total 753 links, &#9733 190, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.wolfe.ml/">
   Wolfe
  </a>
  Declarative Machine Learning
 </li>
 <li>
  <a href="http://flink.apache.org/">
   Flink
  </a>
  - Open source platform for distributed stream and batch data processing.
 </li>
 <li>
  <a href="http://spark-notebook.io">
   Spark Notebook
  </a>
  - Interactive and Reactive Data Science using Scala and Spark.
 </li>
</ul>
<p>
 <a name="scala-general-purpose">
 </a>
</p>
<h4>
 General-Purpose Machine Learning
</h4>
<ul>
 <li>
  <a href="https://github.com/etsy/Conjecture">
   Conjecture
  </a>
  - Scalable Machine Learning in Scalding
  <sup>
   377 GitHub links in total 753 links, &#9733 307, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/stripe/brushfire">
   brushfire
  </a>
  - Distributed decision tree ensemble learning in Scala
  <sup>
   377 GitHub links in total 753 links, &#9733 298, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/tresata/ganitha">
   ganitha
  </a>
  - scalding powered machine learning
  <sup>
   377 GitHub links in total 753 links, &#9733 110, pushed 532 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/bigdatagenomics/adam">
   adam
  </a>
  - A genomics processing engine and specialized file format built using Apache Avro, Apache Spark and Parquet. Apache 2 licensed.
  <sup>
   377 GitHub links in total 753 links, &#9733 424, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/bioscala/bioscala">
   bioscala
  </a>
  - Bioinformatics for the Scala programming language
  <sup>
   377 GitHub links in total 753 links, &#9733 68, pushed 31 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/BIDData/BIDMach">
   BIDMach
  </a>
  - CPU and GPU-accelerated Machine Learning Library.
  <sup>
   377 GitHub links in total 753 links, &#9733 569, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/p2t2/figaro">
   Figaro
  </a>
  - a Scala library for constructing probabilistic models.
  <sup>
   377 GitHub links in total 753 links, &#9733 310, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/h2oai/sparkling-water">
   H2O Sparkling Water
  </a>
  - H2O and Spark interoperability.
  <sup>
   377 GitHub links in total 753 links, &#9733 292, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="https://ci.apache.org/projects/flink/flink-docs-master/apis/batch/libs/ml/index.html">
   FlinkML in Apache Flink
  </a>
  - Distributed machine learning library in Flink
 </li>
 <li>
  <a href="https://github.com/mandar2812/DynaML">
   DynaML
  </a>
  - Scala Library/REPL for Machine Learning Research
  <sup>
   377 GitHub links in total 753 links, &#9733 33, pushed 3 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="swift">
 </a>
</p>
<h2>
 Swift
</h2>
<p>
 <a name="swift-general-purpose">
 </a>
</p>
<h4>
 General-Purpose Machine Learning
</h4>
<ul>
 <li>
  <a href="https://github.com/collinhundley/Swift-AI">
   Swift AI
  </a>
  - Highly optimized artificial intelligence and machine learning library written in Swift.
  <sup>
   377 GitHub links in total 753 links, &#9733 2758, pushed 10 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/aleph7/BrainCore">
   BrainCore
  </a>
  - The iOS and OS X neural network framework
  <sup>
   377 GitHub links in total 753 links, &#9733 47, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/scottsievert/swix">
   swix
  </a>
  - A bare bones library that
includes a general matrix language and wraps some OpenCV for iOS development.
 </li>
 <li>
  <a href="http://deeplearningkit.org/">
   DeepLearningKit
  </a>
  an Open Source Deep Learning Framework for Apple’s iOS, OS X and tvOS.
It currently allows using deep convolutional neural network models trained in Caffe on Apple operating systems.
 </li>
 <li>
  <a href="https://github.com/KevinCoble/AIToolbox">
   AIToolbox
  </a>
  - A toolbox framework of AI modules written in Swift:  Graphs/Trees, Linear Regression, Support Vector Machines, Neural Networks, PCA, KMeans, Genetic Algorithms, MDP, Mixture of Gaussians.
  <sup>
   377 GitHub links in total 753 links, &#9733 318, pushed 3 days ago
  </sup>
 </li>
</ul>
<p>
 <a name="credits">
 </a>
</p>
<h2>
 Credits
</h2>
<ul>
 <li>
  Some of the python libraries were cut-and-pasted from
  <a href="https://github.com/vinta/awesome-python">
   vinta
  </a>
  <sup>
   377 GitHub links in total 753 links, &#9733 20412, pushed 3 days ago
  </sup>
 </li>
 <li>
  The few go reference I found where pulled from
  <a href="https://code.google.com/p/go-wiki/wiki/Projects#Machine_Learning">
   this page
  </a>
 </li>
</ul>
