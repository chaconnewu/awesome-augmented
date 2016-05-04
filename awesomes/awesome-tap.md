<h1>
 Awesome TAP
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
 <a href="https://testanything.org">
  <img align="right" src="https://testanything.org/images/tap.png" width="67"/>
 </a>
</h1>
<blockquote>
 <p>
  Useful resources for the
  <a href="https://testanything.org">
   Test Anything Protocol
  </a>
  <br/>
  A simple text-based interface between testing modules in a test harness
 </p>
</blockquote>
<p>
 <em>
  The list is very JavaScript focused right now. That's just because I'm only familiar with TAP stuff in the JS world. Contributions welcome for any language.
 </em>
</p>
<h2>
 Reporters
</h2>
<h3>
 JavaScript
</h3>
<ul>
 <li>
  <a href="https://github.com/scottcorgan/tap-dot">
   tap-dot
  </a>
  <span>
   &#9733 16, pushed 27 days ago
  </span>
  - Dotted output.
 </li>
 <li>
  <a href="https://github.com/scottcorgan/tap-spec">
   tap-spec
  </a>
  <span>
   &#9733 138, pushed 90 days ago
  </span>
  - Mocha-like spec reporter.
 </li>
 <li>
  <a href="https://github.com/calvinmetcalf/tap-nyan">
   tap-nyan
  </a>
  <span>
   &#9733 55, pushed 48 days ago
  </span>
  - Nyan cat.
 </li>
 <li>
  <a href="https://github.com/gummesson/tap-min">
   tap-min
  </a>
  <span>
   &#9733 17, pushed 87 days ago
  </span>
  - Minimal output.
 </li>
 <li>
  <a href="https://github.com/namuol/tap-difflet">
   tap-difflet
  </a>
  <span>
   &#9733 23, pushed 47 days ago
  </span>
  - Minimal output with diffing.
 </li>
 <li>
  <a href="https://github.com/axross/tap-diff">
   tap-diff
  </a>
  <span>
   &#9733 30, pushed 62 days ago
  </span>
  - Human-friendly output with diffing.
 </li>
 <li>
  <a href="https://github.com/joeybaker/tap-simple">
   tap-simple
  </a>
  <span>
   &#9733 6, pushed 369 days ago
  </span>
  - Simple output.
 </li>
 <li>
  <a href="https://github.com/substack/faucet">
   faucet
  </a>
  <span>
   &#9733 363, pushed 806 days ago
  </span>
  - Human-readable summarizer.
 </li>
 <li>
  <a href="https://github.com/isaacs/tap-mocha-reporter">
   tap-mocha-reporter
  </a>
  - Use any of the
  <a href="https://github.com/isaacs/tap-mocha-reporter/tree/master/lib/reporters">
   Mocha reporters
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/zoubin/tap-summary">
   tap-summary
  </a>
  <span>
   &#9733 6, pushed 122 days ago
  </span>
  - Summarized output.
 </li>
 <li>
  <a href="https://github.com/clux/tap-pessimist">
   tap-pessimist
  </a>
  <span>
   &#9733 7, pushed 208 days ago
  </span>
  - Only shows failed tests.
 </li>
 <li>
  <a href="https://github.com/toolness/tap-prettify">
   tap-prettify
  </a>
  <span>
   &#9733 24, pushed 961 days ago
  </span>
  - Nice readable output with diffing.
 </li>
 <li>
  <a href="https://github.com/substack/tap-colorize">
   tap-colorize
  </a>
  <span>
   &#9733 22, pushed 357 days ago
  </span>
  - Colorize the output while preserving machine-readability.
 </li>
 <li>
  <a href="https://github.com/juliangruber/tap-bail">
   tap-bail
  </a>
  <span>
   &#9733 11, pushed 800 days ago
  </span>
  - Bail out when the first test fails.
 </li>
 <li>
  <a href="https://github.com/axross/tap-notify">
   tap-notify
  </a>
  <span>
   &#9733 22, pushed 62 days ago
  </span>
  - Notifier for OS X, Linux and Windows.
 </li>
 <li>
  <a href="https://github.com/gummesson/tap-json">
   tap-json
  </a>
  <span>
   &#9733 10, pushed 5 days ago
  </span>
  - JSON output.
 </li>
 <li>
  <a href="https://github.com/aghassemi/tap-xunit">
   tap-xunit
  </a>
  <span>
   &#9733 8, pushed 7 days ago
  </span>
  - xUnit output.
 </li>
 <li>
  <a href="https://github.com/smockle/tap-teamcity">
   tap-teamcity
  </a>
  <span>
   &#9733 1, pushed 69 days ago
  </span>
  - Output for TeamCity.
 </li>
</ul>
<h2>
 Producers
</h2>
<p>
 Things that produce TAP output.
</p>
<h3>
 JavaScript
</h3>
<ul>
 <li>
  <a href="https://github.com/sindresorhus/ava">
   AVA
  </a>
  <span>
   &#9733 4490, pushed 2 days ago
  </span>
  - Futuristic test runner.
  <code>
   $ ava --tap
  </code>
 </li>
 <li>
  <a href="https://github.com/isaacs/node-tap">
   tap
  </a>
  - TAP test framework for Node.js.
 </li>
 <li>
  <a href="https://github.com/substack/tape">
   tape
  </a>
  <span>
   &#9733 2290, pushed 24 days ago
  </span>
  - TAP-producing test harness for Node.js and browsers.
 </li>
 <li>
  <a href="http://eslint.org/docs/user-guide/formatters/#tap">
   ESLint
  </a>
  - Pluggable JavaScript linter.
  <code>
   $ eslint --format=tap
  </code>
 </li>
 <li>
  <a href="https://mochajs.org">
   Mocha
  </a>
  - Feature-rich test framework for Node.js and browsers.
  <code>
   $ mocha reporter=tap
  </code>
 </li>
 <li>
  <a href="https://github.com/twada/qunit-tap">
   qunit-tap
  </a>
  <span>
   &#9733 71, pushed 12 days ago
  </span>
  - TAP output for QUnit.
 </li>
 <li>
  <a href="https://github.com/larrymyers/jasmine-reporters">
   jasmine-reporters
  </a>
  <span>
   &#9733 324, pushed 32 days ago
  </span>
  - TAP output for Jasmine.
 </li>
 <li>
  <a href="https://github.com/fumiakiy/karma-tap-reporter">
   karma-tap-reporter
  </a>
  <span>
   &#9733 7, pushed 151 days ago
  </span>
  - TAP output for Karma.
 </li>
</ul>
<h2>
 Fish
</h2>
<ul>
 <li>
  <a href="https://github.com/fisherman/fishtape">
   Fishtape
  </a>
  <span>
   &#9733 193, pushed 12 days ago
  </span>
  - TAP producer and test harness for fish.
 </li>
</ul>
<p>
 <a href="https://testanything.org/producers.html">
  More...
 </a>
</p>
<h2>
 Consumers
</h2>
<p>
 Things that consume TAP output.
</p>
<h3>
 JavaScript
</h3>
<ul>
 <li>
  <a href="https://github.com/substack/tap-parser">
   tap-parser
  </a>
  - TAP parser.
 </li>
 <li>
  <a href="https://github.com/scottcorgan/tap-out">
   tap-out
  </a>
  <span>
   &#9733 12, pushed 27 days ago
  </span>
  - TAP parser.
 </li>
 <li>
  <a href="https://github.com/isaacs/yamlish">
   yamlish
  </a>
  <span>
   &#9733 15, pushed 348 days ago
  </span>
  - YAML-block parser.
 </li>
</ul>
<p>
 <a href="https://testanything.org/consumers.html">
  More...
 </a>
</p>
<h2>
 Tools
</h2>
<h3>
 JavaScript
</h3>
<ul>
 <li>
  <a href="https://github.com/Jam3/tap-dev-tool">
   tap-dev-tool
  </a>
  <span>
   &#9733 23, pushed 322 days ago
  </span>
  - Prettify TAP in the browser console.
 </li>
 <li>
  <a href="https://github.com/anko/tap-merge">
   tap-merge
  </a>
  <span>
   &#9733 3, pushed 106 days ago
  </span>
  - Merge multiple TAP streams.
 </li>
</ul>
<h3>
 Python
</h3>
<ul>
 <li>
  <a href="https://github.com/mblayman/tappy">
   tappy
  </a>
  <span>
   &#9733 32, pushed 34 days ago
  </span>
  - Tools for working with TAP.
 </li>
</ul>
<h2>
 Articles
</h2>
<ul>
 <li>
  <a href="http://www.effectiveperlprogramming.com/2011/05/understand-the-test-anything-protocol/">
   Understand the Test Anything Protocol
  </a>
 </li>
</ul>
<h2>
 Tutorials
</h2>
<ul>
 <li>
  <a href="https://github.com/finnp/test-anything">
   test-anything
  </a>
  <span>
   &#9733 78, pushed 18 days ago
  </span>
  - Learn to test anything with TAP through an interactive workshop.
 </li>
</ul>
<h2>
 Documentation
</h2>
<ul>
 <li>
  <a href="https://testanything.org/tap-version-13-specification.html">
   Specification
  </a>
 </li>
 <li>
  <a href="https://en.wikipedia.org/wiki/Test_Anything_Protocol">
   Wikipedia article
  </a>
 </li>
</ul>
<h2>
 Community
</h2>
<ul>
 <li>
  <a href="https://github.com/TestAnything/Specification/issues">
   Discuss
  </a>
 </li>
 <li>
  <a href="https://www.reddit.com/r/testanythingprotocol">
   Reddit
  </a>
 </li>
 <li>
  <a href="http://stackoverflow.com/questions/tagged/tap">
   StackOverflow
  </a>
 </li>
</ul>
<h2>
 License
</h2>
<p>
 <a href="https://creativecommons.org/publicdomain/zero/1.0/">
  <img alt="CC0" src="http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg"/>
 </a>
</p>
<p>
 To the extent possible under law,
 <a href="http://sindresorhus.com">
  Sindre Sorhus
 </a>
 has waived all copyright and related or neighboring rights to this work.
</p>
