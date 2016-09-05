<h1>
 Awesome FP JS
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<p>
 This is a curated list of awesome
 <a href="https://en.wikipedia.org/wiki/Functional_programming">
  functional programming
 </a>
 code and learning resources for JavaScript. As a multi-paradigm programming language, JavaScript can be written in many styles. With these resources we want to help you to make better use of JavaScript’s support for writing programs in a
 <em>
  functional
 </em>
 way.
</p>
<p>
 Functional programming is a
 <a href="https://wiki.haskell.org/Functional_programming">
  style of programming
 </a>
 which models computations as the evaluation of expressions. Contrast this  with imperative programming where programs are composed of statements which change global state when executed. Functional programming typically avoids using mutable state and favors
 <em>
  side-effect free
 </em>
 functions and
 <em>
  immutable
 </em>
 data instead. This encourages writing composable and declarative programs that are easy to reason about.
</p>
<h5>
 Table of Contents
</h5>
<ul>
 <li>
  <a href="#libraries">
   Libraries
  </a>
  <ul>
   <li>
    <a href="#data-structures">
     Data Structures
    </a>
   </li>
   <li>
    <a href="#algebraic-data-types">
     Algebraic Data Types
    </a>
   </li>
   <li>
    <a href="#lenses">
     Lenses
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#functional-languages-that-compile-to-javascript">
   Functional Languages that Compile to JavaScript
  </a>
 </li>
 <li>
  <a href="#resources">
   Resources
  </a>
  <ul>
   <li>
    <a href="#books">
     Books
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
    <a href="#examples-and-exercises">
     Examples and Exercises
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#community">
   Community
  </a>
 </li>
 <li>
  <a href="#contribution">
   Contribution
  </a>
 </li>
</ul>
<h2>
 Libraries
</h2>
<ul>
 <li>
  <a href="https://github.com/ramda/ramda">
   Ramda
  </a>
  – A practical functional library for JavaScript that is designed specifically for a functional programming style. A style that makes it easy to create functional pipelines and never mutates user data.
 </li>
 <li>
  <a href="http://folktalejs.org/">
   Folktale
  </a>
  – Folktale is a suite of libraries for generic functional programming that allows you to write elegant modular applications with fewer bugs and more reuse.
 </li>
 <li>
  <a href="https://github.com/lodash/lodash/wiki/FP-Guide">
   lodash/fp
  </a>
  – An instance of
  <a href="https://github.com/lodash/lodash">
   Lodash
  </a>
  with its methods wrapped to produce immutable, auto-curried, iteratee-first, data-last methods.
 </li>
 <li>
  <a href="http://functionaljs.com">
   functional.js
  </a>
  – A lightweight functional JavaScript library that facilitates currying and point-free / tacit programming.
 </li>
 <li>
  <a href="https://github.com/tjmehta/101">
   101
  </a>
  – A modern and modular JavaScript utility library made to work well with vanilla JavaScript methods.
 </li>
 <li>
  <a href="https://github.com/algesten/fnuc">
   fnuc
  </a>
  – A functional library for CoffeeScript (and JavaScript) to facilitate functional composition and higher order functions.
 </li>
 <li>
  <a href="https://github.com/cullophid/barely-functional">
   barely-functional
  </a>
  – A tiny (2.7kb) functional programming library using native ES5/6 operations.
 </li>
 <li>
  <a href="http://gkz.github.io/prelude-ls/">
   prelude.ls
  </a>
  – A functionally oriented utility library somewhat based off of Haskell's Prelude module.
 </li>
 <li>
  <a href="http://allong.es/">
   allong.es
  </a>
  – A collection of functions to facilitate writing JavaScript with functions as first-class values, designed to complement libraries like Underscore, not compete with them.
 </li>
 <li>
  <a href="https://github.com/1-liners/1-liners">
   1-liners
  </a>
  – Functional tools that couldn’t be simpler. A dead simple functional utility belt, hand-crafted with love and attention.
 </li>
 <li>
  <a href="https://github.com/thunklife/fn-curry">
   fn-curry
  </a>
  – A simple function to curry a function.
 </li>
 <li>
  <a href="https://github.com/thisables/curry">
   curry
  </a>
  – Curry your functions using function bind syntax.
 </li>
 <li>
  <a href="https://github.com/stoeffel/compose-function">
   compose-function
  </a>
  – Compose a new function from smaller functions.
  <sup>
   &#9733 14, pushed 336 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/paldepind/functionize">
   functionize
  </a>
  – A collection of functions which aid in making non-functional libraries functional.
 </li>
 <li>
  <a href="https://github.com/loop-recur/lambdajs">
   lambdajs
  </a>
  – The full ECMAScript API done a functional way.
 </li>
 <li>
  <a href="https://github.com/fp-dom/">
   fp-dom
  </a>
  – Making the DOM functional.
 </li>
 <li>
  <a href="https://github.com/algesten/trifl">
   trifl
  </a>
  – A functional user interface library with unidirectional dataflow and a virtual dom.
 </li>
 <li>
  <a href="https://github.com/bramstein/funcy">
   funcy
  </a>
  – An experiment in adding functional pattern matching to JavaScript.
  <em>
   Experimental
  </em>
  :triangular
  <em>
   flag
  </em>
  on_post:
 </li>
 <li>
  <a href="https://github.com/cullophid/date-fp">
   date-fp
  </a>
  – A functional utility library for working with JavaScript dates. All functions in date-fp are pure, autocurried and will not mutate the date objects they are applied to.
 </li>
 <li>
  <a href="https://github.com/js-joda/js-joda">
   js-joda
  </a>
  – An immutable date and time library that provides a simple, domain-driven and clean API based on the ISO8601 calendar.
 </li>
 <li>
  <a href="https://github.com/AutoSponge/_part_">
   _part_
  </a>
  – A micro library that encourages functional programming by making native methods available as partially applied functions.
 </li>
 <li>
  <a href="https://github.com/robotlolita/claire">
   claire
  </a>
  – A property-based testing library for clearly specifying code invariants and behaviour.
 </li>
</ul>
<h3>
 Data Structures
</h3>
<p>
 Write performant functional code by using the right data structures for the task.
</p>
<ul>
 <li>
  <a href="https://github.com/facebook/immutable-js">
   Immutable.js
  </a>
  – Immutable persistent data collections.
  <sup>
   &#9733 12697, pushed 130 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/swannodette/mori">
   Mori
  </a>
  – ClojureScript’s persistent data structures and supporting API from the comfort of vanilla JavaScript.
  <sup>
   &#9733 2073, pushed 190 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/qiao/immutable-sequence.js">
   immutable-sequence.js
  </a>
  –  High performance implementation of Immutable Sequence in JavaScript, based on
  <a href="https://github.com/qiao/fingertree.js">
   Finger Trees
  </a>
  .
 </li>
 <li>
  <a href="http://guigrpa.github.io/timm/">
   Timm
  </a>
  – Immutability helpers with fast reads and acceptable writes.
 </li>
 <li>
  <a href="https://github.com/dtao/lazy.js">
   Lazy.js
  </a>
  – A utility library with a lazy engine under the hood that strives to do as little work as possible while being as flexible as possible.
  <sup>
   &#9733 3662, pushed 135 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/ds300/derivablejs">
   DerivableJS
  </a>
  – Functional Reactive State for JavaScript and TypeScript. DerivableJS enables you to make elegant declarative statements about how your bits of state are related.
 </li>
 <li>
  <a href="https://github.com/benji6/imlazy">
   imlazy
  </a>
  – Library for creating and manipulating lazy iterables using the ES2015 iteration protocols.
 </li>
</ul>
<h3>
 Algebraic Data Types
</h3>
<p>
 Use the laws of math instead of always reinventing your own thing. Algebraic!
</p>
<ul>
 <li>
  <a href="https://github.com/fantasyland/fantasy-land">
   Fantasy Land
  </a>
  – Not a library, but a specification of the Monad laws for libraries to follow.
  <sup>
   &#9733 1574, pushed 141 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/rpominov/static-land">
   Static Land
  </a>
  – Specification similar to Fantasy Land but based on static methods rather than instance methods.
 </li>
 <li>
  <a href="https://github.com/DrBoolean/immutable-ext">
   immutable-ext
  </a>
  – FantasyLand extensions for
  <a href="https://github.com/facebook/immutable-js">
   Immutable.js
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/puffnfresh/daggy">
   daggy
  </a>
  – Library for creating tagged constructors.
 </li>
 <li>
  <a href="https://github.com/plaid/sanctuary">
   Sanctuary
  </a>
  – Sanctuary makes it possible to write safe code without null checks.
 </li>
 <li>
  <a href="https://github.com/ramda/ramda-fantasy">
   ramda-fantasy
  </a>
  – Fantasy-Land compatible types for easy integration with Ramda.js.
 </li>
 <li>
  <a href="http://cwmyers.github.io/monet.js/">
   monet.js
  </a>
  – A library that assists functional programming by providing a rich set of Monads and other useful functions.
 </li>
 <li>
  <a href="https://github.com/paldepind/union-type">
   union-type
  </a>
  – A small JavaScript library for defining and using union types.
 </li>
 <li>
  <a href="https://github.com/DrBoolean/freeky">
   freeky
  </a>
  – A collection of Free monads.
 </li>
 <li>
  <a href="https://github.com/Avaq/Fluture">
   Fluture
  </a>
  – A Future library with included control utilities, high performance and great error messages.
 </li>
 <li>
  <a href="https://github.com/fantasyland/fantasy-combinators">
   fantasy-combinators
  </a>
  – Common combinators.
 </li>
 <li>
  <a href="https://github.com/fantasyland/fantasy-birds">
   fantasy-birds
  </a>
  – Port of the Haskell package Data.Aviary.Birds. Everything for your combinatory needs.
 </li>
</ul>
<h3>
 Lenses
</h3>
<ul>
 <li>
  <a href="https://github.com/DrBoolean/lenses">
   lenses
  </a>
  – Composable
  <a href="https://github.com/ekmett/lens">
   kmett
  </a>
  style lenses.
 </li>
 <li>
  <a href="https://github.com/flunc/optics">
   optics
  </a>
  – Profunctor optics (Lens, Prism, iso).
 </li>
 <li>
  <a href="https://github.com/ramda/ramda-lens">
   ramda-lens
  </a>
  – :ram: :mag_right: Lens library built on Ramda.
 </li>
 <li>
  <a href="https://github.com/fantasyland/fantasy-lenses">
   fantasy-lenses
  </a>
  – Composable, immutable getters and setters. (Profunctor lenses WIP)
 </li>
 <li>
  <a href="https://github.com/5outh/nanoscope">
   nanoscope
  </a>
  – Lenses with dotty support.
 </li>
 <li>
  <a href="https://github.com/calmm-js/partial.lenses">
   partial.lenses
  </a>
  – Ramda compatible partial lenses. View, insert and update optional data.
 </li>
</ul>
<h2>
 Functional Languages that Compile to JavaScript
</h2>
<ul>
 <li>
  <a href="https://github.com/clojure/clojurescript">
   ClojureScript
  </a>
  – Compiles
  <a href="http://clojure.org/">
   Clojure
  </a>
  , a hosted Lisp with immutable persistent data structures, to JavaScript.
 </li>
 <li>
  <a href="http://elm-lang.org/">
   Elm
  </a>
  – A type-safe functional programming language for declaratively creating web browser-based graphical user interfaces. Implemented in Haskell.
 </li>
 <li>
  <a href="http://www.purescript.org/">
   PureScript
  </a>
  – A small strongly typed programming language that compiles to JavaScript.
 </li>
 <li>
  <a href="http://www.idris-lang.org/">
   Idris
  </a>
  – A general purpose pure functional programming language with dependent types.
 </li>
 <li>
  <a href="https://github.com/ghcjs/ghcjs">
   GHCJS
  </a>
  –
  <a href="https://www.haskell.org/">
   Haskell
  </a>
  to JavaScript compiler, based on GHC.
 </li>
 <li>
  <a href="https://github.com/bryanjos/elixirscript">
   ElixirScript
  </a>
  – Compiles a subset of
  <a href="http://elixir-lang.org/">
   Elixir
  </a>
  , a dynamic, functional language designed for building scalable and maintainable applications, to JavaScript.
  <sup>
   &#9733 487, pushed 128 days ago
  </sup>
 </li>
 <li>
  <a href="http://ocsigen.org/js_of_ocaml/">
   Js_of_ocaml
  </a>
  – Compiles
  <a href="http://ocaml.org/">
   OCaml
  </a>
  bytecode to JavaScript, making it possible to run OCaml programs in the browser.
 </li>
 <li>
  <a href="https://bloomberg.github.io/bucklescript/">
   BuckleScript
  </a>
  – JavaScript backend for
  <a href="https://ocaml.org/">
   the OCaml compiler
  </a>
  .
 </li>
 <li>
  <a href="http://facebook.github.io/reason/">
   Reason
  </a>
  – Reason is a new interface to OCaml, a highly expressive dialect of the ML language featuring type inference and static type checking.
 </li>
 <li>
  <a href="http://www.scala-js.org/">
   Scala.js
  </a>
  – Compiles
  <a href="http://www.scala-lang.org/">
   Scala
  </a>
  to JavaScript.
 </li>
 <li>
  <a href="http://gkz.github.io/LiveScript/">
   LiveScript
  </a>
  – LiveScript has a straightforward mapping to JavaScript and allows you to write expressive code devoid of repetitive boilerplate.
 </li>
</ul>
<h2>
 Resources
</h2>
<h3>
 Books
</h3>
<ul>
 <li>
  <a href="https://github.com/MostlyAdequate/mostly-adequate-guide">
   Professor Frisby’s Mostly Adequate Guide to Functional Programming
  </a>
  – This is a book on the functional paradigm in general using the world’s most popular functional programming language: JavaScript. It’s a practical introduction that builds up intuition through real-world examples. Strongly recommended. By
  <a href="https://twitter.com/drboolean">
   Brian Lonsdorf
  </a>
  (2016)
 </li>
 <li>
  <a href="https://github.com/getify/functional-light-js">
   Functional-Light JavaScript
  </a>
  – This book explores the core principles of functional programming (FP) that can be applied to JavaScript. But what makes this book different is that it approaches these principles without all the heavy terminology.
 </li>
 <li>
  <a href="https://leanpub.com/javascriptallongesix">
   JavaScript Allongé
  </a>
  , the “Six” edition. Starts with as little as possible about functions – but no less! – and builds up towards powerful combinators and decorators. A foundational book. By
  <a href="https://github.com/raganwald">
   Reginald  Braithwaite
  </a>
  (2016)
 </li>
 <li>
  <a href="https://www.manning.com/books/functional-programming-in-javascript">
   Functional Programming in JavaScript
  </a>
  teaches JavaScript developers functional techniques that will improve extensibility, modularity, reusability, testability, and performance. Through concrete examples and jargon-free explanations, this book teaches you how to apply functional programming to real-life development tasks. By Luis Atencio (2016)
 </li>
 <li>
  <a href="http://eloquentjavascript.net/">
   Eloquent JavaScript
  </a>
  . A modern introduction to programming using JavaScript. By Marijn Haverbeke (2014)
 </li>
 <li>
  <a href="http://shop.oreilly.com/product/0636920028857.do">
   Functional JavaScript
  </a>
  teaches how to create code that’s beautiful, safe, and simple to understand and test by using JavaScript’s functional programming support. By
  <a href="https://github.com/fogus">
   Michael Fogus
  </a>
  (2013)
 </li>
</ul>
<h3>
 Articles
</h3>
<ul>
 <li>
  <a href="https://medium.com/@collardeau/intro-to-functional-programming-concepts-in-javascript-b0650773139c">
   FP Concepts in JavaScript
  </a>
  – An introduction to Functional Programming Concepts in JavaScript. Uses the Ramda library to teach the concepts of composition, pointfree style, and functors through the simplest of examples.
 </li>
 <li>
  <a href="http://stephen-young.me.uk/2013/01/20/functional-programming-with-javascript.html">
   Functional programming with JavaScript
  </a>
  – Another introduction to Functional Programming in JavaScript with a focus on three key themes: computation as the application of functions, statelessness, avoiding side effects.
 </li>
 <li>
  <a href="http://jrsinclair.com/articles/2016/gentle-introduction-to-functional-javascript-intro/">
   A gentle introduction to functional JavaScript
  </a>
  – A four-part series introduction functional programming in JavaScript that gets you up to speed what all the hype about functional programming is all about.
 </li>
 <li>
  <a href="https://hughfdjackson.com/javascript/why-curry-helps/">
   Why Curry Helps
  </a>
  – A short overview of how to write reusable and declarative code using currying.
 </li>
 <li>
  <a href="http://fr.umio.us/favoring-curry/">
   Favoring Curry
  </a>
  - Practical applications of currying using Ramda.
 </li>
 <li>
  <a href="http://blog.jenkster.com/2016/06/functional-mumbo-jumbo-adts.html">
   Functional Mumbo Jumbo – ADTs
  </a>
  – A beginner-friendly introduction to Algebraic Data Types.
 </li>
 <li>
  <a href="https://medium.com/@yelouafi/javascript-and-type-thinking-735edddc388d">
   JavaScript and Type Thinking
  </a>
  – Learn to reason about your JavaScript code with
  <em>
   type thinking
  </em>
  . Algebraic Data Types are introduced as a conceptual basis to reason about program entities.
 </li>
 <li>
  <a href="https://codewords.recurse.com/issues/four/lazy-composable-and-modular-javascript">
   Lazy, composable, and modular JavaScript
  </a>
  – Use four new featurs of ES6 – iterables, generators, fat arrows, and for-of – in conjunction with higher-order functions, function composition, and lazy evaluation, to write cleaner and more modular JavaScript.
 </li>
 <li>
  <a href="http://fr.umio.us/why-ramda/">
   Why Ramda
  </a>
  – To those not used to functional programming, Ramda seems to serve no purpose whatsoever. However, it does offer a different style of coding, a style that’s taken for granted in purely functional programming languages: Ramda makes it simple for you to build complex logic through functional composition.
 </li>
 <li>
  <a href="https://curiosity-driven.org/monads-in-javascript">
   Monads in JavaScript
  </a>
  – An introduction to the Monad design pattern in JavaScript.
 </li>
 <li>
  <a href="http://robotlolita.me/2013/12/08/a-monad-in-practicality-first-class-failures.html">
   A Monad in Practicality: First-Class Failures
  </a>
  – A walk through some practical use cases for specific monadic structures in JavaScript: use the
  <code>
   Maybe
  </code>
  monad to handle simple failure cases and model more complex scenarios with the
  <code>
   Either
  </code>
  monad or the
  <code>
   Validation
  </code>
  applicative functor.
 </li>
 <li>
  <a href="https://glebbahmutov.com/blog/tags/functional/">
   Functional programming
  </a>
  – Many articles on various aspects of functional programming in JavaScript by Gleb Bahmutov.
 </li>
 <li>
  <a href="https://github.com/hemanth/functional-programming-jargon">
   Functional Programming Jargon
  </a>
  – Jargon from the functional programming world explained in JavaScript.
 </li>
 <li>
  <a href="http://blog.benoitvallon.com/data-structures-in-javascript/data-structures-in-javascript/">
   Data Structures in JavaScript
  </a>
  – A series of blog posts that reimplements various data structures in JavaScript to better understand their benefits and downsides.
 </li>
</ul>
<h3>
 Videos
</h3>
<ul>
 <li>
  <a href="https://www.youtube.com/watch?v=h_tkIpwbsxY&list=PLK_hdtAJ4KqX0JOs_KMAmUNTNMRYhWEaC">
   Classroom Coding with Prof. Frisby
  </a>
  – A series that builds a “practical” web application with React and functional programming in JavaScript.
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=m3svKOdZijA">
   Hey Underscore, You're Doing It Wrong!
  </a>
  – Underscore.js claims to be a functional programming library, but is it really?
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=AvgwKjTPMmM">
   Functional programming patterns for the non-mathematician
  </a>
  – Learn about practical use cases for functors, applicatives, and monads.
 </li>
 <li>
  <a href="https://vimeo.com/49384334">
   Pure JavaScript
  </a>
  – Christian Johansen will show you how you can significantly up your game by leaving loops behind and embracing functions as the primary unit of abstraction.
 </li>
</ul>
<h3>
 Examples and Exercises
</h3>
<ul>
 <li>
  <a href="https://github.com/loop-recur/FPJS-Class">
   FPJS-Class
  </a>
  – Functional Programming learned through JavaScript.
 </li>
 <li>
  <a href="https://github.com/timoxley/functional-javascript-workshop">
   functional-javascript-workshop
  </a>
  – The goal of this workshop is to create realistic problems that can be solved using terse, vanilla, idiomatic JavaScript to teach fundamental functional programming features of JavaScript.
  <sup>
   &#9733 1017, pushed 170 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/paldepind/functional-frontend-architecture">
   functional-frontend-architecture
  </a>
  – A functional frontend framework. Based on Ramda + union-type-js + Flyd + Snabbdom
 </li>
 <li>
  <a href="https://github.com/sharkdp/cube-composer">
   cube-composer
  </a>
  – A puzzle game inspired by functional programming.
  <sup>
   &#9733 279, pushed 216 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jaysoo/example-fp-youtube-search">
   FP Youtube Search
  </a>
  – YouTube search app with ReactJS, Redux, and FP concepts
 </li>
 <li>
  <a href="https://frontendmasters.com/courses/functional-javascript/">
   Hardcore Functional Programming in JavaScript
  </a>
  – Learn to apply techniques from the forefront of computer science research to solve practical problems in Javascript. Discover functional programming and see it demonstrated step-by-step with how to build an example web app using abstract interfaces like Monads, Functors, Monoids and Applicatives. (
  <em>
   commercial
  </em>
  )
 </li>
</ul>
<h2>
 Community
</h2>
<h3>
 Related Lists
</h3>
<ul>
 <li>
  <a href="https://github.com/stoeffel/awesome-frp-js">
   Awesome FRP JS
  </a>
  – A curated list of awesome (functional) reactive programming stuff in JavaScript.
 </li>
 <li>
  <a href="https://github.com/lucasviola/awesome-functional-programming">
   lucasviola/Awesome Functional Programming
  </a>
  – Awesome resources on functional programming theory and learning materials.
  <sup>
   &#9733 115, pushed 188 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/xgrommx/awesome-functional-programming">
   xgrommx/Awesome Functional Programming
  </a>
  – A ton of articles on functional programming, as well as a huge list of functional libraries for many programming languages.
  <sup>
   &#9733 422, pushed 128 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/busypeoples/functional-programming-javascript">
   Functional Programming Resources In JavaScript
  </a>
  <sup>
   &#9733 139, pushed 225 days ago
  </sup>
 </li>
</ul>
<h3>
 Talk
</h3>
<ul>
 <li>
  <a href="https://functionalprogramming.slack.com/">
   Functional Programming Slack channel
  </a>
  – Community with a friendly channel for JavaScript as well as many other channels about functional programming in general.
 </li>
</ul>
<h2>
 Contribution
</h2>
<p>
 :star: Suggestions and PRs are welcome! :star:
</p>
<p>
 Please read the
 <a href="./contributing.md">
  contribution guidelines
 </a>
 to get started.
</p>
<h2>
 License
</h2>
<p>
 <a href="http://creativecommons.org/publicdomain/zero/1.0/">
  <img alt="CC0" src="http://i.creativecommons.org/p/zero/1.0/88x31.png"/>
 </a>
</p>
<p>
 To the extent possible under law,
 <a href="http://stoeffel.github.io/">
  Christoph Hermann
 </a>
 has waived all copyright and related or neighboring rights to this work.
</p>
