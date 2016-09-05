<h1>
 Awesome static analysis
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<blockquote>
 <p>
  Static program analysis is the analysis of computer software that is performed without actually executing programs (analysis performed on executing programs is known as dynamic analysis). — Definition by
  <a href="https://en.wikipedia.org/wiki/Static_program_analysis">
   Wikipedia
  </a>
 </p>
</blockquote>
<p>
 This is a collection of static analysis tools and code quality checkers for all programming languages.
 <br/>
 Explanation: [OSS] stands for Open-Source-Software, [PROPRIETARY] stands for proprietary software.
 <br/>
 <strong>
  Pull requests are very welcome!
 </strong>
</p>
<h2>
 Table of Contents
</h2>
<ul>
 <li>
  <a href="#cc">
   C/C++
  </a>
 </li>
 <li>
  <a href="#c">
   C#
  </a>
 </li>
 <li>
  <a href="#containers">
   Containers
  </a>
 </li>
 <li>
  <a href="#elixir">
   Elixir
  </a>
 </li>
 <li>
  <a href="#go">
   Go
  </a>
 </li>
 <li>
  <a href="#groovy">
   Groovy
  </a>
 </li>
 <li>
  <a href="#haskell">
   Haskell
  </a>
 </li>
 <li>
  <a href="#haxe">
   Haxe
  </a>
 </li>
 <li>
  <a href="#html">
   Html
  </a>
 </li>
 <li>
  <a href="#java">
   Java
  </a>
 </li>
 <li>
  <a href="#javascript">
   JavaScript
  </a>
 </li>
 <li>
  <a href="#lua">
   Lua
  </a>
 </li>
 <li>
  <a href="#python">
   Python
  </a>
 </li>
 <li>
  <a href="#php">
   PHP
  </a>
 </li>
 <li>
  <a href="#r">
   R
  </a>
 </li>
 <li>
  <a href="#ruby">
   Ruby
  </a>
 </li>
 <li>
  <a href="#rust">
   Rust
  </a>
 </li>
 <li>
  <a href="#scala">
   Scala
  </a>
 </li>
 <li>
  <a href="#shell">
   Shell
  </a>
 </li>
 <li>
  <a href="#swift">
   Swift
  </a>
 </li>
 <li>
  <a href="#meta">
   Meta
  </a>
 </li>
 <li>
  <a href="#multiple-languages">
   Multiple Languages
  </a>
 </li>
 <li>
  <a href="#web-services">
   Web-Services
  </a>
 </li>
</ul>
<h2>
 C/C++
</h2>
<ul>
 <li>
  <a href="https://github.com/MetricsGrimoire/CMetrics">
   CMetrics
  </a>
  [OSS] - Measures size and complexity for C files
  <sup>
   &#9733 10, pushed 531 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/dspinellis/cqmetrics">
   cqmetrics
  </a>
  [OSS] - quality metrics for C code
 </li>
 <li>
  <a href="http://clang.llvm.org/extra/clang-tidy/">
   clang-tidy
  </a>
  [OSS] - clang static analyser
 </li>
 <li>
  <a href="https://github.com/danmar/cppcheck">
   cppcheck
  </a>
  [OSS] - static analysis of C/C++ code
  <sup>
   &#9733 913, pushed 127 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.dwheeler.com/flawfinder/">
   flawfinder
  </a>
  [OSS] - finds possible security weaknesses
 </li>
 <li>
  <a href="http://oclint.org/">
   oclint
  </a>
  [OSS] - static analysis of C/C++ code
 </li>
 <li>
  <a href="http://www.splint.org/">
   splint
  </a>
  [OSS] - static analysis of C/C++ code
 </li>
 <li>
  <a href="https://github.com/TrustInSoft/tis-interpreter">
   tis-interpreter
  </a>
  [OSS] - An interpreter for finding subtle bugs in programs written in standard C
 </li>
 <li>
  <a href="https://bitbucket.org/verateam/vera/wiki/Introduction">
   vera++
  </a>
  [OSS] - Vera++ is a programmable tool for verification, analysis and transformation of C++ source code.
 </li>
</ul>
<h2>
 C#
</h2>
<ul>
 <li>
  <a href="https://carc.codeplex.com/">
   Code Analysis Rule Collection
  </a>
  [OSS] - Contains a set of diagnostics, code fixes and refactorings built on the Microsoft .NET Compiler Platform "Roslyn".
 </li>
 <li>
  <a href="https://github.com/code-cracker/code-cracker">
   code-cracker
  </a>
  [OSS] - An analyzer library for C# and VB that uses Roslyn to produce refactorings, code analysis, and other niceties.
  <sup>
   &#9733 560, pushed 138 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/DustinCampbell/CSharpEssentials">
   CSharpEssentials
  </a>
  [OSS] - C# Essentials is a collection of Roslyn diagnostic analyzers, code fixes and refactorings that make it easy to work with C# 6 language features.
  <sup>
   &#9733 115, pushed 306 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.designite-tools.com">
   Designite
  </a>
  [PROPRIETARY] - Designite is a software design quality assessment tool. It supports detection of implementation and design smells, computation of various code quality metrics, and trend analysis.
 </li>
 <li>
  <a href="http://www.mono-project.com/docs/tools+libraries/tools/gendarme/">
   Gendarme
  </a>
  [OSS] - Gendarme inspects programs and libraries that contain code in ECMA CIL format (Mono and .NET) and looks for common problems with the code, problems that compiler do not typically check or have not historically checked.
 </li>
 <li>
  <a href="https://github.com/DotNetAnalyzers">
   .NET Analyzers
  </a>
  [OSS] - An organization for the development of analyzers (diagnostics, code fixes, and refactorings) using the .NET Compiler Platform.
 </li>
 <li>
  <a href="https://github.com/SonarSource/sonarlint-vs">
   SonarLint for Visual Studio
  </a>
  [OSS] - SonarLint is a Visual Studio 2015 extension that provides on-the-fly feedback to developers on new bugs and quality issues injected into .NET code.
 </li>
 <li>
  <a href="http://vsrefactoringessentials.com/">
   Refactoring Essentials
  </a>
  [OSS] - The premier free Visual Studio 2015 extension for C# and VB.NET refactorings, including code best practice analyzers to improve your projects.
 </li>
 <li>
  <a href="https://www.jetbrains.com/resharper/">
   ReSharper
  </a>
  [PROPRIETARY] - Extends Visual Studio with on-the-fly code inspections for C#, VB.NET, ASP.NET, JavaScript, TypeScript and other technologies.
 </li>
 <li>
  <a href="https://github.com/Vannevelj/VSDiagnostics">
   VSDiagnostics
  </a>
  [OSS] - A collection of static analyzers based on Roslyn that integrate with VS.
 </li>
 <li>
  <a href="https://github.com/Wintellect/Wintellect.Analyzers">
   Wintellect.Analyzers
  </a>
  [OSS] - .NET Compiler Platform ("Roslyn") diagnostic analyzers and code fixes written by Wintellect.
  <sup>
   &#9733 54, pushed 189 days ago
  </sup>
 </li>
</ul>
<h2>
 Containers
</h2>
<ul>
 <li>
  <a href="https://github.com/coreos/clair">
   clair
  </a>
  [OSS] - Vulnerability Static Analysis for Containers
  <sup>
   &#9733 1105, pushed 130 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/banyanops/collector">
   collector
  </a>
  [OSS] - Run arbitrary scripts inside containers, and gather useful information
 </li>
 <li>
  <a href="https://github.com/lukasmartinelli/hadolint">
   Haskell Dockerfile Linter
  </a>
  [OSS] - A smarter Dockerfile linter that helps you build best practice Docker images
  <sup>
   &#9733 377, pushed 154 days ago
  </sup>
 </li>
</ul>
<h2>
 Elixir
</h2>
<ul>
 <li>
  <a href="https://github.com/rrrene/credo">
   credo
  </a>
  [OSS] -  A static code analysis tool with a focus on code consistency and teaching.
  <sup>
   &#9733 652, pushed 131 days ago
  </sup>
 </li>
</ul>
<h2>
 Go
</h2>
<ul>
 <li>
  <a href="https://github.com/nickng/dingo-hunter">
   dingo-hunter
  </a>
  [OSS] - Static analyser for finding Deadlocks in Go
 </li>
 <li>
  <a href="https://github.com/lafolle/flen">
   flen
  </a>
  [OSS] - Get info on length of functions in a Go package
 </li>
 <li>
  <a href="https://golang.org/pkg/go/ast/">
   go/ast
  </a>
  [OSS] - Package ast declares the types used to represent syntax trees for Go packages.
 </li>
 <li>
  <a href="https://github.com/fzipp/gocyclo">
   gocyclo
  </a>
  [OSS] - Calculate cyclomatic complexities of functions in Go source code
  <sup>
   &#9733 184, pushed 254 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/alecthomas/gometalinter">
   Go Meta Linter
  </a>
  [OSS] - Concurrently run Go lint tools and normalise their output
  <sup>
   &#9733 887, pushed 131 days ago
  </sup>
 </li>
 <li>
  <a href="https://godoc.org/golang.org/x/tools/cmd/vet">
   go vet
  </a>
  [OSS] - Examines Go source code and reports suspicious constructs
 </li>
 <li>
  <a href="https://github.com/gordonklaus/ineffassign">
   ineffassign
  </a>
  - Detect ineffectual assignments in Go code
  <sup>
   &#9733 34, pushed 155 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/stripe/safesql">
   safesql
  </a>
  [OSS] - Static analysis tool for Golang that protects against SQL injections
  <sup>
   &#9733 203, pushed 185 days ago
  </sup>
 </li>
</ul>
<h2>
 Groovy
</h2>
<ul>
 <li>
  <a href="https://github.com/CodeNarc/CodeNarc">
   CodeNarc
  </a>
  [OSS] - a static analysis tool for Groovy source code, enabling monitoring and enforcement of many coding standards and best practices
  <sup>
   &#9733 87, pushed 152 days ago
  </sup>
 </li>
</ul>
<h2>
 Haskell
</h2>
<ul>
 <li>
  <a href="https://github.com/ndmitchell/hlint">
   HLint
  </a>
  [OSS] - HLint is a tool for suggesting possible improvements to Haskell code.
  <sup>
   &#9733 293, pushed 159 days ago
  </sup>
 </li>
</ul>
<h2>
 Haxe
</h2>
<ul>
 <li>
  <a href="https://github.com/HaxeCheckstyle/haxe-checkstyle">
   Haxe Checkstyle
  </a>
  [OSS] - A static analysis tool to help developers write Haxe code that adheres to a coding standard.
  <sup>
   &#9733 44, pushed 129 days ago
  </sup>
 </li>
</ul>
<h2>
 HTML
</h2>
<ul>
 <li>
  <a href="https://github.com/yaniswang/HTMLHint">
   HTMLHint
  </a>
  [OSS] - A Static Code Analysis Tool for HTML
  <sup>
   &#9733 1120, pushed 126 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/philipwalton/html-inspector">
   HTML Inspector
  </a>
  [OSS] - HTML Inspector is a code quality tool to help you and your team write better markup.
  <sup>
   &#9733 2161, pushed 137 days ago
  </sup>
 </li>
</ul>
<h2>
 Java
</h2>
<ul>
 <li>
  <a href="https://github.com/checkstyle/checkstyle">
   checkstyle
  </a>
  [OSS] - checking Java source code for adherence to a Code Standard or set of validation rules (best practices)
  <sup>
   &#9733 1037, pushed 125 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.spinellis.gr/sw/ckjm/">
   ckjm
  </a>
  [OSS] - calculates Chidamber and Kemerer object-oriented metrics by processing the bytecode of compiled Java files
 </li>
 <li>
  <a href="https://github.com/google/error-prone">
   Error-prone
  </a>
  [OSS] - Catch common Java mistakes as compile-time errors·
  <sup>
   &#9733 917, pushed 130 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/mebigfatguy/fb-contrib">
   fb-contrib
  </a>
  [OSS] - A plugin for FindBugs with additional bug detectors
  <sup>
   &#9733 25, pushed 126 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/findbugsproject/findbugs">
   Findbugs
  </a>
  [OSS] - FindBugs is a program to find bugs in Java programs. It looks for patterns are likely to be errors.
  <sup>
   &#9733 148, pushed 149 days ago
  </sup>
 </li>
 <li>
  <a href="https://find-sec-bugs.github.io/">
   find-sec-bugs
  </a>
  [OSS] - IDE/Sonarcube plugin for security audits of Java web applications.
 </li>
 <li>
  <a href="https://pmd.github.io/">
   PMD
  </a>
  [OSS] - A Java source code analyzer
 </li>
</ul>
<h2>
 JavaScript
</h2>
<ul>
 <li>
  <a href="https://github.com/codecombat/aether">
   aether
  </a>
  [OSS] - Lint, analyze, normalize, transform, sandbox, run, step through, and visualize user JavaScript, in node or the browser.
  <sup>
   &#9733 124, pushed 132 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/google/closure-linter">
   ClosureLinter
  </a>
  [OSS] - ensures that all of your project's JavaScript code follows the guidelines in the Google JavaScript Style Guide. It can also automatically fix many common errors
  <sup>
   &#9733 70, pushed 270 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jared-stilwell/complexity-report">
   complexity-report
  </a>
  [OSS] - Software complexity analysis for JavaScript projects
  <sup>
   &#9733 61, pushed 135 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jared-stilwell/escomplex">
   escomplex
  </a>
  [OSS] - Software complexity analysis of JavaScript-family abstract syntax trees.
  <sup>
   &#9733 66, pushed 128 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/eslint/eslint">
   eslint
  </a>
  [OSS] - A fully pluggable tool for identifying and reporting on patterns in JavaScript
  <sup>
   &#9733 4784, pushed 126 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jquery/esprima">
   Esprima
  </a>
  [OSS] - ECMAScript parsing infrastructure for multipurpose analysis
  <sup>
   &#9733 3097, pushed 133 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jden/quality">
   quality
  </a>
  [OSS] - zero configuration code and module linting
  <sup>
   &#9733 4, pushed 452 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jshint/jshint">
   jshint
  </a>
  [OSS] - detect errors and potential problems in JavaScript code and enforce your team's coding conventions
  <sup>
   &#9733 6289, pushed 134 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/douglascrockford/JSLint">
   JSLint
  </a>
  [PROPRIETARY] - The JavaScript Code Quality Tool
  <sup>
   &#9733 2667, pushed 134 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/es-analysis/plato">
   plato
  </a>
  [OSS] - Visualize JavaScript source complexity
  <sup>
   &#9733 3492, pushed 133 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/calmh/yardstick">
   yardstick
  </a>
  [OSS] - Javascript code metrics
  <sup>
   &#9733 18, pushed 1486 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/sindresorhus/xo">
   XO
  </a>
  [OSS] - Enforce strict code style. Never discuss code style on a pull request again!
  <sup>
   &#9733 1158, pushed 128 days ago
  </sup>
 </li>
</ul>
<h2>
 Lua
</h2>
<ul>
 <li>
  <a href="https://github.com/mpeterv/luacheck">
   luacheck
  </a>
  [OSS] -  A tool for linting and static analysis of Lua code.
  <sup>
   &#9733 265, pushed 140 days ago
  </sup>
 </li>
</ul>
<h2>
 Python
</h2>
<ul>
 <li>
  <a href="https://pypi.python.org/pypi/flake8">
   flake8
  </a>
  [OSS] - the modular source code checker: pep8, pyflakes and co
 </li>
 <li>
  <a href="http://jedi.jedidjah.ch/en/latest/">
   jedi
  </a>
  [OSS] - autocompletion/static analysis library for Python
 </li>
 <li>
  <a href="https://github.com/lyft/linty_fresh">
   Linty fresh
  </a>
  [OSS] - Surface lint errors during code review
  <sup>
   &#9733 87, pushed 136 days ago
  </sup>
 </li>
 <li>
  <a href="http://mypy-lang.org/">
   mypy
  </a>
  [OSS] - an experimental optional static type checker for Python that aims to combine the benefits of dynamic (or "duck") typing and static typing
 </li>
 <li>
  <a href="https://github.com/landscapeio/prospector">
   prospector
  </a>
  [OSS] - output information about errors, potential problems, convention violations and complexity in Python code
 </li>
 <li>
  <a href="https://github.com/pyflakes/pyflakes/">
   pyflakes
  </a>
  [OSS] - A simple program which checks Python source files for errors.
 </li>
 <li>
  <a href="https://github.com/PyCQA/pylint">
   pylint
  </a>
  [OSS] -  Looks for programming errors, helps enforcing a coding standard and sniffs for some code smells
  <sup>
   &#9733 167, pushed 127 days ago
  </sup>
 </li>
</ul>
<h2>
 PHP
</h2>
<ul>
 <li>
  <a href="https://github.com/Halleck45/DesignPatternDetector">
   DesignPatternDetector
  </a>
  [OSS] - detection of design patterns in PHP code
  <sup>
   &#9733 40, pushed 266 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/sensiolabs-de/deptrac">
   deptrac
  </a>
  [OSS] - Enforce rules for dependencies between software layers.
  <sup>
   &#9733 92, pushed 127 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/exakat/exakat">
   exakat
  </a>
  [OSS] - An automated code reviewing engine for PHP
  <sup>
   &#9733 9, pushed 128 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/phpro/grumphp">
   GrumPHP
  </a>
  [OSS] - checks code on every commit
  <sup>
   &#9733 957, pushed 126 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/etsy/phan">
   phan
  </a>
  [OSS] - a modern static analyzer from etsy
  <sup>
   &#9733 926, pushed 130 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/sstalle/php7cc">
   php7cc
  </a>
  [OSS] - PHP 7 Compatibility Checker
  <sup>
   &#9733 588, pushed 141 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Alexia/php7mar">
   php7mar
  </a>
  [OSS] - assist developers in porting their code quickly to PHP 7
  <sup>
   &#9733 333, pushed 129 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/sebastianbergmann/phpcpd">
   phpcpd
  </a>
  [OSS] - Copy/Paste Detector (CPD) for PHP code.
  <sup>
   &#9733 992, pushed 141 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/squizlabs/PHP_CodeSniffer">
   PHP_CodeSniffer
  </a>
  [OSS] - detects violations of a defined set of coding standards
  <sup>
   &#9733 2270, pushed 130 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/sebastianbergmann/phpdcd">
   phpdcd
  </a>
  [OSS] - Dead Code Detector (DCD) for PHP code.
  <sup>
   &#9733 270, pushed 329 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/mamuz/PhpDependencyAnalysis">
   PhpDependencyAnalysis
  </a>
  [OSS] - builds a dependency graph for a project
  <sup>
   &#9733 173, pushed 192 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/ovr/phpsa">
   phpsa
  </a>
  [OSS] - Static analysis tool for PHP.
  <sup>
   &#9733 172, pushed 134 days ago
  </sup>
 </li>
 <li>
  <a href="http://phpmd.org/">
   PHPMD
  </a>
  [OSS] - finds possible bugs in your code
 </li>
 <li>
  <a href="https://github.com/Halleck45/PhpMetrics">
   PhpMetrics
  </a>
  [OSS] - calculates code complexity metrics
 </li>
 <li>
  <a href="https://github.com/QafooLabs/php-refactoring-browser">
   PHP Refactoring Browser
  </a>
  [OSS] - Refactoring helper
  <sup>
   &#9733 494, pushed 510 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Andrewsville/PHP-Token-Reflection">
   PHP-Token-Reflection
  </a>
  [OSS] - Library emulating the PHP internal reflection
  <sup>
   &#9733 180, pushed 262 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/nikic/PHP-Parser">
   PHP-Parser
  </a>
  [OSS] - A PHP parser written in PHP
  <sup>
   &#9733 2252, pushed 138 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/ripsscanner/rips">
   RIPS
  </a>
  [OSS] -  A static source code analyser for vulnerabilities in PHP scripts
  <sup>
   &#9733 100, pushed 462 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/ircmaxell/Tuli">
   Tuli
  </a>
  [OSS] - A static analysis engine
  <sup>
   &#9733 154, pushed 318 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/asm89/twig-lint">
   twig-lint
  </a>
  [OSS] - twig-lint is a lint tool for your twig files.
  <sup>
   &#9733 43, pushed 278 days ago
  </sup>
 </li>
</ul>
<h2>
 R
</h2>
<ul>
 <li>
  <a href="https://github.com/jimhester/lintr">
   lintr
  </a>
  [PROPRIETARY] - Static Code Analysis for R
  <sup>
   &#9733 165, pushed 143 days ago
  </sup>
 </li>
</ul>
<h2>
 Ruby
</h2>
<ul>
 <li>
  <a href="https://github.com/presidentbeef/brakeman">
   brakeman
  </a>
  [OSS] - A static analysis security vulnerability scanner for Ruby on Rails applications
  <sup>
   &#9733 3322, pushed 126 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/square/cane">
   cane
  </a>
  [OSS] - Code quality threshold checking as part of your build
  <sup>
   &#9733 1286, pushed 175 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/thesp0nge/dawnscanner">
   dawnscanner
  </a>
  [OSS] - a static analysis security scanner for ruby written web applications. It supports Sinatra, Padrino and Ruby on Rails frameworks.
  <sup>
   &#9733 299, pushed 187 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/seattlerb/flay">
   flay
  </a>
  [OSS] - Flay analyzes code for structural similarities.
  <sup>
   &#9733 400, pushed 126 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/seattlerb/flog">
   flog
  </a>
  [OSS] - Flog reports the most tortured code in an easy to read pain
report. The higher the score, the more pain the code is in.
  <sup>
   &#9733 451, pushed 269 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/michaeledgar/laser">
   laser
  </a>
  [OSS] - Static analysis and style linter for Ruby code.
  <sup>
   &#9733 395, pushed 1821 days ago
  </sup>
 </li>
 <li>
  <a href="http://trismegiste.github.io/Mondrian/">
   Mondrian
  </a>
  [OSS] - a set of static analysis and refactoring tools for more abstraction
 </li>
 <li>
  <a href="https://github.com/codegram/pelusa">
   pelusa
  </a>
  [OSS] -  Static analysis Lint-type tool to improve your OO Ruby code
  <sup>
   &#9733 449, pushed 607 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/apiology/quality">
   quality
  </a>
  [OSS] -  Runs quality checks on your code using community tools, and makes sure your numbers don't get any worse over time.
  <sup>
   &#9733 106, pushed 149 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/troessner/reek">
   reek
  </a>
  [OSS] - Code smell detector for Ruby
  <sup>
   &#9733 1884, pushed 129 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/bbatsov/rubocop">
   rubocop
  </a>
  [OSS] - A Ruby static code analyzer, based on the community Ruby style guide.
  <sup>
   &#9733 6230, pushed 126 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/whitesmith/rubycritic">
   rubycritic
  </a>
  [OSS] - A Ruby code quality reporter
  <sup>
   &#9733 1326, pushed 138 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/YorickPeterse/ruby-lint">
   ruby-lint
  </a>
  [OSS] - Static code analysis for Ruby
  <sup>
   &#9733 675, pushed 132 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/makaroni4/sandi_meter">
   SandyMeter
  </a>
  [OSS] - Static analysis tool for checking Ruby code for Sandi Metz' rules.
  <sup>
   &#9733 623, pushed 262 days ago
  </sup>
 </li>
</ul>
<h2>
 Rust
</h2>
<ul>
 <li>
  <a href="https://github.com/Manishearth/rust-clippy">
   clippy
  </a>
  [OSS] - a code linter to catch common mistakes and improve your Rust code
  <sup>
   &#9733 619, pushed 127 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/AtomLinter/linter-rust">
   linter-rust
  </a>
  [OSS] -  Linting your Rust-files in Atom, using rustc and cargo
 </li>
</ul>
<h2>
 Scala
</h2>
<ul>
 <li>
  <a href="https://github.com/HairyFotr/linter">
   linter
  </a>
  [OSS] - Linter is a Scala static analysis compiler plugin which adds compile-time checks for various possible bugs, inefficiencies, and style problems.
  <sup>
   &#9733 152, pushed 127 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/scalastyle/scalastyle/wiki">
   ScalaStyle
  </a>
  [OSS] - Scalastyle examines your Scala code and indicates potential problems with it.
 </li>
 <li>
  <a href="https://github.com/sksamuel/scapegoat">
   scapegoat
  </a>
  [OSS] - Scala compiler plugin for static code analysis
  <sup>
   &#9733 135, pushed 182 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/puffnfresh/wartremover">
   WartRemover
  </a>
  [OSS] - a flexible Scala code linting tool.
  <sup>
   &#9733 472, pushed 141 days ago
  </sup>
 </li>
</ul>
<h2>
 Shell
</h2>
<ul>
 <li>
  <a href="https://github.com/koalaman/shellcheck">
   shellcheck
  </a>
  [OSS] - ShellCheck, a static analysis tool that gives warnings and suggestions for bash/sh shell scripts
  <sup>
   &#9733 3767, pushed 128 days ago
  </sup>
 </li>
</ul>
<h2>
 Swift
</h2>
<ul>
 <li>
  <a href="https://github.com/realm/SwiftLint">
   SwiftLint
  </a>
  [OSS] - A tool to enforce Swift style and conventions
  <sup>
   &#9733 3811, pushed 129 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/sleekbyte/tailor">
   Tailor
  </a>
  [OSS] - A static analysis and lint tool for source code written in Apple's Swift programming language.
  <sup>
   &#9733 651, pushed 126 days ago
  </sup>
 </li>
</ul>
<h1>
 Meta
</h1>
<h2>
 Multiple languages
</h2>
<ul>
 <li>
  <a href="https://github.com/groupon/codeburner">
   codeburner
  </a>
  [OSS] - Provides a unified interface to sort and act on the issues it finds
 </li>
 <li>
  <a href="http://www.coverity.com/products/coverity-save/">
   Coverity Save
  </a>
  [PROPRIETARY] - Static analysis for  C/C++, Java and C#
 </li>
 <li>
  <a href="https://github.com/justinabrahms/imhotep">
   imhotep
  </a>
  [OSS] - Comment on commits coming into your repository and check for syntactic errors and general lint warnings.
 </li>
 <li>
  <a href="https://github.com/facebook/infer">
   Infer
  </a>
  [OSS] -  A static analyzer for Java, C and Objective-C
  <sup>
   &#9733 5107, pushed 129 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/oclint/oclint">
   oclint
  </a>
  [OSS] - A static source code analysis tool to improve quality and reduce defects for C, C++ and Objective-C
  <sup>
   &#9733 1293, pushed 137 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/facebook/pfff">
   pfff
  </a>
  [OSS] - Facebook's tools for code analysis, visualizations, or style-preserving source transformation for many languages
  <sup>
   &#9733 1653, pushed 161 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.viva64.com/en/pvs-studio/">
   PVS-Studio
  </a>
  [PROPRIETARY] - static analysis of C/C++ and C# code
 </li>
 <li>
  <a href="https://github.com/google/shipshape">
   shipshape
  </a>
  [OSS] - Static program analysis platform that allows custom analyzers to plug in through a common interface
  <sup>
   &#9733 118, pushed 133 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/StanfordPL/stoke-release">
   STOKE
  </a>
  [OSS] - a programming-language agnosti stochastic optimizer for the x86_64 instruction set. It uses random search to explore the extremely high-dimensional space of all possible program transformations
  <sup>
   &#9733 353, pushed 210 days ago
  </sup>
 </li>
 <li>
  <a href="https://developer.apple.com/xcode/">
   XCode
  </a>
  [PROPRIETARY/OSS] - XCode provides a pretty decend UI for
  <a href="http://clang-analyzer.llvm.org/xcode.html">
   Clang's
  </a>
  static code analyzer (C/C++, Obj-C)
 </li>
</ul>
<h2>
 Web-Services
</h2>
<ul>
 <li>
  <a href="https://www.codacy.com/">
   Codacy
  </a>
  [PROPRIETARY] - Code Analysis to ship Better Code, Faster.
 </li>
 <li>
  <a href="https://codeclimate.com/">
   Code Climate
  </a>
  [PROPRIETARY] - The open and extensible static analysis platform, for everyone.
 </li>
 <li>
  <a href="http://www.conqat.org/">
   ConQAT
  </a>
  [OSS] - a toolkit for rapid development and execution of software quality analyses.
 </li>
 <li>
  <a href="http://www.functor.se/products/prevent/">
   Functor Prevent
  </a>
  [PROPRIETARY] - Static code analysis for C code.
 </li>
 <li>
  <a href="https://www.kiuwan.com/">
   kiuwan
  </a>
  [PROPRIETARY] - Software Analytics in the Cloud supporting more than 22 programming languages.
 </li>
 <li>
  <a href="https://landscape.io/">
   Landscape
  </a>
  [PROPRIETARY] - Static code analysis for Python
 </li>
 <li>
  <a href="https://nitpick-ci.com">
   Nitpick CI
  </a>
  [PROPRIETARY] - Automated PHP code review
 </li>
 <li>
  <a href="https://nodesecurity.io/">
   Node Security Platform
  </a>
  [PROPRIETARY] - Continuous Security monitoring for your node apps (free for Open Source Projects)
 </li>
 <li>
  <a href="https://www.quantifiedcode.com/">
   QuantifiedCode
  </a>
  [PROPRIETARY] - Automated code review & repair
 </li>
 <li>
  <a href="https://scrutinizer-ci.com/">
   Scrutinizer
  </a>
  [PROPRIETARY] - A proprietery code quality checker that can be integrated with GitHub
 </li>
 <li>
  <a href="https://insight.sensiolabs.com/">
   SensioLabs Insight
  </a>
  [PROPRIETARY] - Detect security risks, find bugs and provide actionable metrics for PHP projects
 </li>
 <li>
  <a href="https://snyk.io/">
   Snyk
  </a>
  [PROPRIETARY] - Vulnerability scanner for dependencies of node.js apps (free for Open Source Projects)
 </li>
 <li>
  <a href="http://www.teamscale.com/">
   Teamscale
  </a>
  [PROPRIETARY] - analyze, monitor, and improve the quality of your code.
 </li>
</ul>
<h2>
 License
</h2>
<p>
 <a href="https://creativecommons.org/publicdomain/zero/1.0/">
  <img alt="CC0" src="https://i.creativecommons.org/p/zero/1.0/88x31.png"/>
 </a>
</p>
<p>
 To the extent possible under law,
 <a href="http://matthias-endler.de">
  Matthias Endler
 </a>
 has waived all copyright and related or neighboring rights to this work.
</p>
