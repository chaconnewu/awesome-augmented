<p>
 <a href="https://promisesaplus.com/">
  <img align="right" alt="Promises/A+ logo" src="https://promisesaplus.com/assets/logo-small.png"/>
 </a>
</p>
<h1>
 Awesome Promises
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<blockquote>
 <p>
  A curated list of useful resources for JavaScript Promises
 </p>
</blockquote>
<p>
 Inspired by the
 <a href="https://github.com/sindresorhus/awesome">
  awesome
 </a>
 list thing. Not to be confused with other awesome promises like "I promise you a million dollars" or "I promise you'll stay fit and never have to go to the gym again".
</p>
<p>
 <strong>
  Table of Contents
 </strong>
</p>
<ul>
 <li>
  <a href="#resources-blogs-and-books">
   Resources, Blogs, and Books
  </a>
 </li>
 <li>
  <a href="#promisesa-implementations-es6es2015-compatible">
   Promises/A+ Implementations (ES6/ES2015 compatible)
  </a>
  <ul>
   <li>
    <a href="#strict-implementations">
     Strict Implementations
    </a>
   </li>
   <li>
    <a href="#implementations-with-extras">
     Implementations with extras
    </a>
   </li>
   <li>
    <a href="#fallbacks">
     Fallbacks
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#convenience-utilities">
   Convenience Utilities
  </a>
 </li>
</ul>
<h2>
 Resources, Blogs, and Books
</h2>
<h3>
 For beginners
</h3>
<ul>
 <li>
  <a href="https://github.com/mattdesl/promise-cookbook">
   Promise Cookbook
  </a>
  - The why, what, and how. "A brief introduction [...] primarily aimed at frontend developers".
  <sup>
   &#9733 810, pushed 166 days ago
  </sup>
 </li>
 <li>
  <a href="http://exploringjs.com/es6/ch_promises.html">
   Promises for Asynchronous Programming
  </a>
  - Chapter from
  <a href="http://exploringjs.com/">
   Exploring ES6
  </a>
 </li>
 <li>
  <a href="https://github.com/getify/You-Dont-Know-JS/blob/master/async%20&%20performance/ch3.md">
   You Don't Know JS: Promises
  </a>
  - Chapter from
  <a href="https://github.com/getify/You-Dont-Know-JS/tree/master/async%20%26%20performance">
   You Don't Know JS: Async & Performance
  </a>
 </li>
 <li>
  <a href="http://www.html5rocks.com/en/tutorials/es6/promises/">
   JavaScript Promises: There and back again
  </a>
  - Basics of JavaScript's native promise implementation.
 </li>
 <li>
  <a href="http://shop.oreilly.com/product/0636920032151.do">
   JavaScript with Promises
  </a>
  - from O'Reilly. Short and to-the-point. Uses native and bluebird.
 </li>
 <li>
  <a href="https://github.com/stevekane/promise-it-wont-hurt">
   Promise it won't hurt
  </a>
  - An interactive
  <a href="http://nodeschool.io/">
   nodeschool
  </a>
  workshop
  <sup>
   &#9733 161, pushed 23 days ago
  </sup>
 </li>
 <li>
  <a href="http://es6katas.org/">
   ES6 Kata Promises
  </a>
  - Promises Katas :
  <a href="http://tddbin.com/#?kata=es6/language/promise/basics">
   Basics
  </a>
 </li>
 <li>
  <a href="https://ponyfoo.com/articles/es6-promises-in-depth">
   ES6 Promises in Depth
  </a>
 </li>
</ul>
<h3>
 Deep Dive
</h3>
<ul>
 <li>
  <a href="https://blog.domenic.me/youre-missing-the-point-of-promises/">
   You're Missing the Point of Promises
  </a>
  - Promises are much more than callback aggregation, and that jQuery's implementation (prior to 3.0) isn't enough.
 </li>
 <li>
  <a href="https://pouchdb.com/2015/05/18/we-have-a-problem-with-promises.html">
   We have a problem with promises
  </a>
  - "Many of us are using promises without really understanding them."
 </li>
 <li>
  <a href="https://github.com/petkaantonov/bluebird/wiki/Promise-anti-patterns">
   Promise anti-patterns
  </a>
  - Common misuses and how to avoid them.
 </li>
 <li>
  <a href="http://taoofcode.net/promise-anti-patterns/">
   Promise anti-patterns (2)
  </a>
  - Another set of promises anti-patterns
 </li>
 <li>
  <a href="https://sdgluck.github.io/2015/08/24/promise-ponderings-patterns-apologies/">
   Promise Ponderings, (Anti-)Patterns, and Apologies
  </a>
  - Promise behaviour demonstrated and explained by common questions and their answers.
 </li>
 <li>
  <a href="http://www.mattgreer.org/articles/promises-in-wicked-detail/">
   Javascript Promises...In Wicked Detail
  </a>
  - Recreate the promise implementation
 </li>
 <li>
  <a href="https://www.w3.org/2001/tag/doc/promises-guide">
   Writing Promise-Using Specifications
  </a>
  - "This document gives guidance on how to write specifications that create, accept, or manipulate promises"
 </li>
</ul>
<h3>
 References
</h3>
<ul>
 <li>
  <a href="https://promisesaplus.com/">
   Promises/A+ specification
  </a>
 </li>
 <li>
  <a href="http://caniuse.com/#feat=promises">
   caniuse promises
  </a>
 </li>
 <li>
  <a href="https://github.com/domenic/promises-unwrapping/blob/master/docs/states-and-fates.md">
   Fates and States
  </a>
  - Quick definitions of possible states.
 </li>
 <li>
  <a href="https://bevacqua.github.io/promisees/">
   Promisees
  </a>
  - Promise visualization playground for the adventurous.
 </li>
</ul>
<h2>
 Promises/A+ Implementations (ES6/ES2015 compatible)
</h2>
<h3>
 Strict Implementations
</h3>
<p>
 These implement no more or less than the es6 spec. They make great polyfills and are exceptionally compatible with native promises.
</p>
<ul>
 <li>
  <a href="https://github.com/floatdrop/pinkie">
   pinkie
  </a>
  - Ponyfill. Node-oriented, but
  <a href="https://github.com/substack/node-browserify">
   browserifyable
  </a>
  .
  <em>
   Extremely
  </em>
  small implementation.
  <sup>
   &#9733 97, pushed 92 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/getify/native-promise-only">
   native-promise-only
  </a>
  - Polyfill. Browser and node-compatible.
  <sup>
   &#9733 454, pushed 39 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/stefanpenner/es6-promise">
   es6-promise
  </a>
  - Opt-in polyfill. A strict-spec subset of rsvp.js.
  <sup>
   &#9733 2999, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/calvinmetcalf/lie">
   lie
  </a>
  - Small, browserifyable with an opt-in polyfill.
  <sup>
   &#9733 428, pushed 3 days ago
  </sup>
 </li>
</ul>
<h3>
 Implementations with extras
</h3>
<p>
 All of these provide more features than the language yet remain compatible. Node + Browsers for all.
</p>
<ul>
 <li>
  <a href="https://github.com/petkaantonov/bluebird">
   bluebird
  </a>
  - Fully featured, extremely performant. Long stack traces & generator/coroutine support.
  <sup>
   &#9733 10820, pushed 6 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/tildeio/rsvp.js/">
   rsvp.js
  </a>
  - Lightweight with a few extras. Compatible down to IE6!
 </li>
 <li>
  <a href="https://github.com/kriskowal/q">
   Q
  </a>
  - One of the original implementations. Long stack traces and other goodies.
  <sup>
   &#9733 11547, pushed 20 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/then/promise">
   then/promise
  </a>
  - Small with
  <code>
   nodeify
  </code>
  ,
  <code>
   denodify
  </code>
  and
  <code>
   done()
  </code>
  additions.
  <sup>
   &#9733 1116, pushed 54 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/cujojs/when">
   when.js
  </a>
  - Packed with control flow, functional, and utility methods.
  <sup>
   &#9733 2925, pushed 5 days ago
  </sup>
 </li>
</ul>
<h3>
 Fallbacks
</h3>
<ul>
 <li>
  <a href="https://www.npmjs.com/package/native-or-bluebird">
   native-or-bluebird
  </a>
  - Helps transition to completely native.
 </li>
 <li>
  <a href="https://github.com/floatdrop/pinkie-promise">
   pinkie-promise
  </a>
  - Use native, or fall back to
  <code>
   pinkie
  </code>
  . Great for node library authors.
  <sup>
   &#9733 69, pushed 23 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/kevinbeaty/any-promise">
   any-promise
  </a>
  - Loads the first available implementation. Safe for browserify.
  <sup>
   &#9733 50, pushed 1 days ago
  </sup>
 </li>
</ul>
<h2>
 Convenience Utilities
</h2>
<p>
 Native and strictly spec-compliant promises are awesome for compatibility, future-proofness, library authors, and browsers. However, libraries like bluebird patch goodies onto the
 <code>
  Promise
 </code>
 constructor and prototype. Solution? tiny modules of course!
</p>
<ul>
 <li>
  <a href="https://github.com/sindresorhus/pify">
   pify
  </a>
  - Promisify ("denodify") a callback-style function.
  <sup>
   &#9733 162, pushed 16 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/yoshuawuyts/promise-each">
   promise-each
  </a>
  - Standalone
  <code>
   bluebird.each
  </code>
  . Execute one after the other sequentially.
  <sup>
   &#9733 10, pushed 211 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/yoshuawuyts/promise-filter">
   promise-filter
  </a>
  - Standalone
  <code>
   bluebird.filter
  </code>
  . Filter an array to a promise.
  <sup>
   &#9733 6, pushed 298 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/blakeembrey/promise-finally">
   promise-finally
  </a>
  - Standalone bluebird
  <code>
   finally()
  </code>
  . Execute a handler unconditionally after others have been handled.
  <sup>
   &#9733 2, pushed 91 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/yoshuawuyts/promise-map">
   promise-map
  </a>
  - Standalone
  <code>
   bluebird.map
  </code>
  . Map an array to a promise.
  <sup>
   &#9733 7, pushed 298 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/wbinnssmith/promise-method">
   promise-method
  </a>
  - Standalone
  <code>
   bluebird.method
  </code>
  . Turn a synchronously-returning method into a promise-returning one.
  <sup>
   &#9733 1, pushed 227 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/exponentjs/promise-props">
   promise-props
  </a>
  - Standalone implementation of bluebird's
  <code>
   bluebird.props
  </code>
  or rsvp's
  <code>
   RSVP.hash
  </code>
  <sup>
   &#9733 3, pushed 338 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/yoshuawuyts/promise-reduce">
   promise-reduce
  </a>
  - Standalone
  <code>
   bluebird.reduce
  </code>
  . Reduce an array to a promise.
  <sup>
   &#9733 6, pushed 287 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/yoshuawuyts/promise-some">
   promise-some
  </a>
  - Standalone
  <code>
   bluebird.some
  </code>
  . Check if an element passes the predicate, return a promise.
  <sup>
   &#9733 4, pushed 298 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/wbinnssmith/promise-try">
   promise-try
  </a>
  - Standalone
  <code>
   bluebird.try
  </code>
  . Execute a synchronously-returning function and return a promise.
  <sup>
   &#9733 2, pushed 227 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/then/is-promise">
   is-promise
  </a>
  - Determine if something looks like a Promise.
  <sup>
   &#9733 22, pushed 132 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/then/sprom">
   sprom
  </a>
  - Resolve when a stream ends. Optional buffering (be careful with this!)
  <sup>
   &#9733 10, pushed 132 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/mozilla/task.js">
   task.js
  </a>
  - Write async functions in a blocking style using promises and generators. Like
  <code>
   bluebird.coroutine
  </code>
  .
  <sup>
   &#9733 1492, pushed 887 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/tj/co">
   co
  </a>
  - Like
  <code>
   task.js
  </code>
  and
  <code>
   bluebird.coroutine
  </code>
  , but supports thunks too.
  <sup>
   &#9733 5252, pushed 6 days ago
  </sup>
 </li>
 <li>
  <a href="https://www.npmjs.com/package/lie-fs">
   lie-fs
  </a>
  - Promise wrappers for Node's FS API.
 </li>
 <li>
  <a href="https://github.com/sindresorhus/immediate-promise">
   immediate-promise
  </a>
  - Returns a promise resolved in the next event loop - think
  <code>
   setImmediate()
  </code>
  .
  <sup>
   &#9733 37, pushed 26 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/sindresorhus/delay">
   delay
  </a>
  - Delay a promise a specified amount of time.
  <sup>
   &#9733 82, pushed 124 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/sindresorhus/promise-whilst">
   promise-whilst
  </a>
  - Calls a function repeatedly if and while a condition returns true and then resolves the promise.
  <sup>
   &#9733 15, pushed 26 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/sindresorhus/loud-rejection">
   loud-rejection
  </a>
  - Make unhandled promise rejections fail loudly instead of the default silent fail.
  <sup>
   &#9733 89, pushed 25 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/busterc/promise-until">
   promise-until
  </a>
  - Calls a function repeatedly if a condition returns false and until the condition returns true and then resolves the promise.
  <sup>
   &#9733 0, pushed 160 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/busterc/promise-do-until">
   promise-do-until
  </a>
  - Calls a function repeatedly until a condition returns true and then resolves the promise.
  <sup>
   &#9733 0, pushed 160 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/busterc/promise-do-whilst">
   promise-do-whilst
  </a>
  - Calls a function repeatedly while a condition returns true and then resolves the promise.
  <sup>
   &#9733 0, pushed 160 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/samccone/promise-semaphore">
   promise-semaphore
  </a>
  - Push a set of work to be done in a configurable serial fashion
  <sup>
   &#9733 22, pushed 72 days ago
  </sup>
 </li>
</ul>
<h2>
 License
</h2>
<p>
 Licensed under the
 <a href="https://creativecommons.org/publicdomain/zero/1.0/">
  Creative Commons CC0 License
 </a>
 .
</p>
