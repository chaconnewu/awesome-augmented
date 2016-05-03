<h1>
 Awesome FOSS apps
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<blockquote>
 <p>
  A curated list of awesome production grade free and open source software organized by category.
 </p>
</blockquote>
<p>
 This list is for developers who are looking for non-trivial quality applications they can analyze and learn from.
</p>
<p>
 <em>
  Inspired by Sindre Sorhus's
  <a href="https://github.com/sindresorhus/awesome">
   awesome
  </a>
  .
 </em>
</p>
<h2>
 TOC
</h2>
<ul>
 <li>
  <a href="#web-apps-frontend-only">
   Webapps (frontend only)
  </a>
 </li>
 <li>
  <a href="#web-apps-fullstack">
   Webapps (fullstack)
  </a>
 </li>
 <li>
  <a href="#desktop-apps">
   Desktop Apps
  </a>
 </li>
 <li>
  <a href="#mobile-apps">
   Mobile Apps
  </a>
 </li>
 <li>
  <a href="#games">
   Games
  </a>
 </li>
</ul>
<p>
 <br/>
</p>
<h2>
 ### Web Apps (frontend only)
</h2>
<h5>
 <a href="https://github.com/circleci/frontend">
  CircleCI
 </a>
</h5>
<ul>
 <li>
  clojurescript, om, react
 </li>
 <li>
  Eclipse Public License
 </li>
</ul>
<blockquote>
 <p>
  CircleCI provides a continuous integration and deployment platform. The frontend is an impressive example of a large application built with the immutable data structures of clojurescript. The frontend integrates with pusher, intercom, d3, and google analytics and has a great example of navigation routing and communication via real-time events, websockets, and backend API servers. Its test suite is not that extensive but does provide a good example of how to test clojurescript/om apps using karma.
 </p>
</blockquote>
<h5>
 <a href="https://github.com/guardian/frontend">
  The Guardian
 </a>
</h5>
<ul>
 <li>
  play2, scala, node
 </li>
 <li>
  Apache 2.0 License
 </li>
</ul>
<blockquote>
 <p>
  The guardian is a news site with subscriptions, sign in, search, an admin interface and a series of middleman scala apps that handle communication between the static frontends and backend APIs. Its very fast and has a comprehensive test suite plus great examples of how to optimize large traditional websites for speed.
 </p>
</blockquote>
<p>
 <br/>
</p>
<h2>
 ### Web Apps (fullstack)
</h2>
<h5>
 <a href="https://github.com/TryGhost/Ghost">
  Ghost
 </a>
</h5>
<ul>
 <li>
  node, express, ember
 </li>
 <li>
  MIT License
 </li>
</ul>
<blockquote>
 <p>
  Ghost provides a simple publishing platform for bloggers. The code contains an emberjs client and node server backend that handle authorization, role management, tagging, blog posting, data persistence, and most things you'd expect from a quality blogging platform. The only thing that Ghost doesn't handle is i18n. It also contains a comprehensive test suite with both integration and unit tests that hit the whole ember/node stack.
 </p>
</blockquote>
<h5>
 <a href="https://github.com/gitlabhq/gitlabhq">
  Gitlab
 </a>
</h5>
<ul>
 <li>
  ruby, rails, coffescript, redis, sidekiq,
 </li>
 <li>
  MIT License
 </li>
</ul>
<blockquote>
 <p>
  Gitlab is a code collaboration tool. It is used by more than 100,000 organizations. It has just about everything you could imagine in a webapp, user management, user roles, OAuth, i18n, many modules designed for integrating with third-parties, deep git integration, and an extensive asynchronous task system using Sidekiq. It has an exemplary test suite using cucumber and rspec.
 </p>
</blockquote>
<h5>
 <a href="https://github.com/discourse/discourse">
  Discourse
 </a>
</h5>
<ul>
 <li>
  ruby, rails, ember
 </li>
 <li>
  GPLv2 License
 </li>
</ul>
<blockquote>
 <p>
  Discourse is a discussion platform or a modern take on the web forum. It has a very modular system built on top of rails and contains great examples of how to build an interactive frontend in ember within a rails application. It has an admin interface, signup/sign-in with Oauth for Google, Facebook, Twitter, Yahoo, and Github. It has extensive i18n, real time notifications, a plugin ecosystem, is SEO optimized, and is designed for tablet and mobile devices.
 </p>
</blockquote>
<h5>
 <a href="https://github.com/reddit">
  Reddit
 </a>
</h5>
<ul>
 <li>
  python, pylons, node, react, rabbitmq, postgresql
 </li>
 <li>
  Common Public Attribution License Version 1.0
 </li>
</ul>
<blockquote>
 <p>
  Reddit is a news platform for what's new and popular on the web. It is built in python and integrates with a lot of third party services: rabbitmq, memcached, cassandra, solr, and postgresql to name a few. The code provides a good example of a large pylons project and shines when it comes to the code that integrates with many other services.
 </p>
</blockquote>
<h5>
 <a href="https://github.com/taigaio">
  Taiga
 </a>
</h5>
<ul>
 <li>
  python3, django, coffeescript, angular
 </li>
 <li>
  GNU Affero License
 </li>
</ul>
<blockquote>
 <p>
  Taiga is a project management tool. It is an incredible example of a modular architecture. Its interface is clean, very well-designed, responsive, and fast, and the modern backend code written in python3 is a great example of a well written django app. It also has an extensive test suite with both integration and unit tests using pytest.
 </p>
</blockquote>
<h5>
 <a href="https://github.com/travis-ci">
  Travis CI
 </a>
</h5>
<ul>
 <li>
  ruby, rails, sinatra, rabbitmq, ember
 </li>
 <li>
  MIT License
 </li>
</ul>
<blockquote>
 <p>
  Travis CI is a continutous integration and deployment system. What's great about Travis is its modular architecture, every component of this large distributed system is split up by its main function. From worker management, rails backend, emberjs frontend to yaml configuration parser, each is split up into there own repositories.
 </p>
</blockquote>
<p>
 <br/>
</p>
<h2>
 ### Desktop Apps
</h2>
<h5>
 <a href="http://www.blender.org/download/">
  Blender
 </a>
</h5>
<ul>
 <li>
  c, c++, python
 </li>
 <li>
  GPLv2 License
 </li>
</ul>
<blockquote>
 <p>
  Blender is 3D Graphic Software that can visually compete with Maya and 3DS Max. The end product is an amazing example of a cross-platform 3D Tooling piece of software. It is a very mature project having been in development since 1994. It has an embedded python scripting engine, a game logic engine and is loaded with implementations of 3d manipulation, rendering, and compositing algorithms.
 </p>
</blockquote>
<h5>
 <a href="https://github.com/atom/atom">
  Atom
 </a>
</h5>
<ul>
 <li>
  coffeescript, electron, node
 </li>
 <li>
  MIT License
 </li>
</ul>
<blockquote>
 <p>
  Atom is a hackable text editor. Its built on top of electron and is a good example of integrating libchromium, nodejs, and web technologies into a cross-platform runnable binary. It also contains an exemplary test suite for electron apps.
 </p>
</blockquote>
<p>
 <br/>
</p>
<h2>
 ### Mobile Apps
</h2>
<p>
 <em>
  still searching
 </em>
</p>
<p>
 <br/>
</p>
<h2>
 ### Games
</h2>
<h5>
 <a href="https://github.com/0ad/0ad">
  0ad
 </a>
</h5>
<ul>
 <li>
  c++, python
 </li>
 <li>
  GPLv2 License
 </li>
</ul>
<blockquote>
 <p>
  0 A.D is a cross-platform real-time strategy game of ancient warfare. Every aspect of the game's implementation is modern and impressive - from the AI to the graphics. It also has an embedded SpiderMonkey scripting engine, which is a great example for adding js scriptability to an existing cpp project.
 </p>
</blockquote>
<h5>
 <a href="https://github.com/hedgewars/hw">
  Hedgewars
 </a>
</h5>
<ul>
 <li>
  c, c++, pascal, haskell
 </li>
 <li>
  GPLv2 License
 </li>
</ul>
<blockquote>
 <p>
  Hedgewars is a 2D turn-based strategy game like worms but with hedgehogs. Its graphics, animation, and gameplay can compete with worms on every level. The game server is an impressive real-world example of Haskell and the frontend provides a clean interface between QT and the backend game.
 </p>
</blockquote>
<h5>
 <a href="https://github.com/wesnoth/wesnoth">
  Wesnoth
 </a>
</h5>
<ul>
 <li>
  c, c++, lua
 </li>
 <li>
  GPLv2 License
 </li>
</ul>
<blockquote>
 <p>
  The Battle for Wesnoth is a turn-based tactical strategy game with a high fantasy theme. It features single player and online multiplayer combat. Its GUI and gameplay graphics are impressive as well as its multi-platform support (it even builds on NaCL). It has clean, well-coded examples of pretty much everything a game developer would want to know, from a an embedded lua scripting engine, to a dialog and GUI system, to a c++ test suite and cross-platform builds.
 </p>
</blockquote>
<h2>
 License
</h2>
<p>
 <a href="http://creativecommons.org/publicdomain/zero/1.0/">
  <img alt="CC0" src="http://i.creativecommons.org/p/zero/1.0/88x31.png"/>
 </a>
</p>
<p>
 To the extent possible under law, John Faucett has waived all copyright and related or neighboring rights to this work.
</p>
