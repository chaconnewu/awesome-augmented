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
  <sup>
   &#9733 16, pushed 27 days ago
  </sup>
  - Dotted output.
 </li>
 <li>
  <a href="https://github.com/scottcorgan/tap-spec">
   tap-spec
  </a>
  <sup>
   &#9733 138, pushed 90 days ago
  </sup>
  - Mocha-like spec reporter.
 </li>
 <li>
  <a href="https://github.com/calvinmetcalf/tap-nyan">
   tap-nyan
  </a>
  <sup>
   &#9733 55, pushed 48 days ago
  </sup>
  - Nyan cat.
 </li>
 <li>
  <a href="https://github.com/gummesson/tap-min">
   tap-min
  </a>
  <sup>
   &#9733 17, pushed 87 days ago
  </sup>
  - Minimal output.
 </li>
 <li>
  <a href="https://github.com/namuol/tap-difflet">
   tap-difflet
  </a>
  <sup>
   &#9733 23, pushed 47 days ago
  </sup>
  - Minimal output with diffing.
 </li>
 <li>
  <a href="https://github.com/axross/tap-diff">
   tap-diff
  </a>
  <sup>
   &#9733 30, pushed 62 days ago
  </sup>
  - Human-friendly output with diffing.
 </li>
 <li>
  <a href="https://github.com/joeybaker/tap-simple">
   tap-simple
  </a>
  <sup>
   &#9733 6, pushed 369 days ago
  </sup>
  - Simple output.
 </li>
 <li>
  <a href="https://github.com/substack/faucet">
   faucet
  </a>
  <sup>
   &#9733 363, pushed 806 days ago
  </sup>
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
  <sup>
   &#9733 6, pushed 123 days ago
  </sup>
  - Summarized output.
 </li>
 <li>
  <a href="https://github.com/clux/tap-pessimist">
   tap-pessimist
  </a>
  <sup>
   &#9733 7, pushed 208 days ago
  </sup>
  - Only shows failed tests.
 </li>
 <li>
  <a href="https://github.com/toolness/tap-prettify">
   tap-prettify
  </a>
  <sup>
   &#9733 24, pushed 961 days ago
  </sup>
  - Nice readable output with diffing.
 </li>
 <li>
  <a href="https://github.com/substack/tap-colorize">
   tap-colorize
  </a>
  <sup>
   &#9733 22, pushed 357 days ago
  </sup>
  - Colorize the output while preserving machine-readability.
 </li>
 <li>
  <a href="https://github.com/juliangruber/tap-bail">
   tap-bail
  </a>
  <sup>
   &#9733 11, pushed 800 days ago
  </sup>
  - Bail out when the first test fails.
 </li>
 <li>
  <a href="https://github.com/axross/tap-notify">
   tap-notify
  </a>
  <sup>
   &#9733 22, pushed 62 days ago
  </sup>
  - Notifier for OS X, Linux and Windows.
 </li>
 <li>
  <a href="https://github.com/gummesson/tap-json">
   tap-json
  </a>
  <sup>
   &#9733 10, pushed 5 days ago
  </sup>
  - JSON output.
 </li>
 <li>
  <a href="https://github.com/aghassemi/tap-xunit">
   tap-xunit
  </a>
  <sup>
   &#9733 8, pushed 7 days ago
  </sup>
  - xUnit output.
 </li>
 <li>
  <a href="https://github.com/smockle/tap-teamcity">
   tap-teamcity
  </a>
  <sup>
   &#9733 1, pushed 69 days ago
  </sup>
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
  <sup>
   &#9733 4490, pushed 2 days ago
  </sup>
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
  <sup>
   &#9733 2290, pushed 24 days ago
  </sup>
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
  <sup>
   &#9733 71, pushed 12 days ago
  </sup>
  - TAP output for QUnit.
 </li>
 <li>
  <a href="https://github.com/larrymyers/jasmine-reporters">
   jasmine-reporters
  </a>
  <sup>
   &#9733 324, pushed 32 days ago
  </sup>
  - TAP output for Jasmine.
 </li>
 <li>
  <a href="https://github.com/fumiakiy/karma-tap-reporter">
   karma-tap-reporter
  </a>
  <sup>
   &#9733 7, pushed 151 days ago
  </sup>
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
  <sup>
   &#9733 193, pushed 12 days ago
  </sup>
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
  <sup>
   &#9733 12, pushed 27 days ago
  </sup>
  - TAP parser.
 </li>
 <li>
  <a href="https://github.com/isaacs/yamlish">
   yamlish
  </a>
  <sup>
   &#9733 15, pushed 349 days ago
  </sup>
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
  <sup>
   &#9733 23, pushed 322 days ago
  </sup>
  - Prettify TAP in the browser console.
 </li>
 <li>
  <a href="https://github.com/anko/tap-merge">
   tap-merge
  </a>
  <sup>
   &#9733 3, pushed 107 days ago
  </sup>
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
  <sup>
   &#9733 32, pushed 34 days ago
  </sup>
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
  <sup>
   &#9733 78, pushed 18 days ago
  </sup>
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
