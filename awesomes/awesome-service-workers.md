<h1>
 Awesome Service Workers
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<p>
 A curated collection of service worker resources.
</p>
<blockquote>
 <p>
  A service worker is an event-driven worker registered against an origin and a path. It takes the form of a JavaScript file that can control the web page/site it is associated with, intercepting and modifying navigation and resource requests, and caching resources in a very granular fashion to give you complete control over how your app behaves in certain situations (the most obvious one being when the network is not available.)
 </p>
 <p>
  --
  <cite>
   <a href="https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API">
    Mozilla Developer Network - Service Worker API
   </a>
  </cite>
 </p>
</blockquote>
<p>
 <a href="http://makeapullrequest.com">
  <img alt="PRs Welcome" src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square"/>
 </a>
</p>
<p>
 If you want to contribute, please read the
 <a href="contributing.md">
  contribution guidelines
 </a>
 .
</p>
<h2>
 Contents
</h2>
<ul>
 <li>
  <a href="#must-reads">
   Must Reads
  </a>
 </li>
 <li>
  <a href="#learning-resources">
   Learning Resources
  </a>
 </li>
 <li>
  <a href="#reference">
   Reference
  </a>
 </li>
 <li>
  <a href="#browser-support">
   Browser Support
  </a>
 </li>
 <li>
  <a href="#libraries-and-tools">
   Libraries and Tools
  </a>
 </li>
 <li>
  <a href="#videos">
   Videos
  </a>
 </li>
 <li>
  <a href="#case-studies">
   Case Studies
  </a>
 </li>
 <li>
  <a href="#related-technologies">
   Related Technologies
  </a>
 </li>
</ul>
<h2>
 Must Reads
</h2>
<ul>
 <li>
  <a href="http://alistapart.com/article/offline-first">
   Designing Offline-First Web Apps
  </a>
  - A fascinating look at design and UX considerations for dealing with various states of connectivity.
 </li>
 <li>
  <a href="http://www.html5rocks.com/en/tutorials/service-worker/introduction/">
   Introduction to Service Worker
  </a>
  - A graceful introduction to service workers.
 </li>
 <li>
  <a href="https://www.udacity.com/course/offline-web-applications--ud899">
   Offline Web Applications Using IndexedDB & Service Worker
  </a>
  - This free Udacity course is a must if you're planning to dive deep into service workers.
 </li>
 <li>
  <a href="https://github.com/slightlyoff/ServiceWorker/blob/master/explainer.md">
   Service Workers Explained
  </a>
  - Service workers explained by
  <a href="https://github.com/slightlyoff">
   Alex Russell
  </a>
  .
 </li>
</ul>
<h2>
 Learning Resources
</h2>
<ul>
 <li>
  <a href="https://dev.opera.com/articles/offline-with-upup-service-workers/">
   Building Offline Sites with ServiceWorkers and UpUp
  </a>
  - A general introduction to service workers and using UpUp to provide offline functionality in minutes.
 </li>
 <li>
  <a href="http://www.html5rocks.com/en/tutorials/service-worker/introduction/">
   Introduction to Service Worker
  </a>
 </li>
 <li>
  <a href="https://github.com/delapuente/service-workers-101">
   Service Workers 101
  </a>
  - An infographic summarizing the most important parts of service workers API.
 </li>
 <li>
  <a href="https://serviceworke.rs/">
   ServiceWorker Cookbook by Mozilla
  </a>
  - A collection of recipes for different use cases.
 </li>
 <li>
  <a href="https://remysharp.com/2016/03/22/the-copy--paste-guide-to-your-first-service-worker">
   The copy & paste guide to your first Service Worker
  </a>
  - Shortest available introduction, by
  <a href="https://github.com/remy">
   Remy Sharp
  </a>
  .
 </li>
 <li>
  <a href="https://jakearchibald.com/2014/offline-cookbook/">
   The offline cookbook
  </a>
  - The bible of service worker Patterns by Jake Archibald.
 </li>
</ul>
<h2>
 Reference
</h2>
<ul>
 <li>
  <a href="https://wicg.github.io/BackgroundSync/spec/">
   Background Sync Spec
  </a>
  - The WIP spec for Background Sync.
 </li>
 <li>
  <a href="https://www.w3.org/TR/service-workers/">
   Service Workers - W3C Specification
  </a>
  - The official service workers spec.
 </li>
</ul>
<h2>
 Browser Support
</h2>
<ul>
 <li>
  <a href="http://caniuse.com/#feat=serviceworkers">
   Can I Use - Service Workers
  </a>
  - Up-to-date browser support table of ServiceWorker API.
 </li>
 <li>
  <a href="https://jakearchibald.github.io/isserviceworkerready/">
   Jake Archibald - Is Service Worker ready?
  </a>
  - Current status of ServiceWorker support in different browsers.
 </li>
</ul>
<h2>
 Libraries and Tools
</h2>
<ul>
 <li>
  <a href="http://upup.rocks/">
   UpUp
  </a>
  - A popular service worker library providing complete offline functionality for your site in 1 line of code.
 </li>
 <li>
  <a href="https://github.com/GoogleChrome/sw-toolbox/">
   sw-toolbox
  </a>
  - A collection of simple helpers to simplify implementing common runtime caching patterns.
 </li>
 <li>
  <a href="https://brucelawson.github.io/manifest/">
   Manifest Generator
  </a>
  - Generate a web app manifest, required for push notifications and installable web apps.
 </li>
 <li>
  <a href="https://github.com/GoogleChrome/sw-precache/">
   sw-precache
  </a>
  - Generates a service worker to cache your local App Shell resources.
 </li>
 <li>
  <a href="https://github.com/GoogleChrome/sw-helpers/tree/master/projects/sw-appcache-behavior">
   sw-appcache-behavior
  </a>
  - A service worker implementation of the behavior defined in a page's App Cache manifest.
 </li>
 <li>
  <a href="https://github.com/GoogleChrome/sw-helpers/tree/master/projects/sw-offline-google-analytics">
   sw-offline-google-analytics
  </a>
  - A service worker helper library to retry offline Google Analytics requests when a connection is available.
 </li>
</ul>
<h2>
 Videos
</h2>
<ul>
 <li>
  <a href="https://youtu.be/cmGr0RszHc8">
   Instant Loading: Building offline-first Progressive Web Apps - Google I/O 2016
  </a>
  - A quick dive into the most common technologies and techniques for building progressive web apps.
 </li>
 <li>
  <a href="https://www.udacity.com/course/offline-web-applications--ud899">
   Offline Web Applications Using IndexedDB & Service Worker
  </a>
  - This free Udacity course is a must if you're planning to dive deep into service workers.
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=jCKZDTtUA2A">
   Instant Loading with Service Workers (Chrome Dev Summit 2015)
  </a>
  - Explains how to structure your web app to optimize load time for initial and return visitors, and cover helpful service worker libraries that minimize the amount of boilerplate code you'll have to write.
 </li>
</ul>
<h2>
 Case Studies
</h2>
<ul>
 <li>
  <a href="https://developers.google.com/web/showcase/case-study/service-workers-iowa">
   Service Workers in Production
  </a>
  - A case-study about how Google I/O 2015 web app was built.
 </li>
 <li>
  <a href="https://developers.google.com/web/showcase/2016/service-worker-perf">
   Measuring the Real-world Performance Impact of Service Workers
  </a>
  - One of the most significant benefits of service workers (from a performance perspective, at least) is their ability to proactively control the caching of assets. A web application that can cache all of its necessary resources should load substantially faster for returning visitors. But what do these gains actually look like to real users? And how do you even measure this?
 </li>
</ul>
<h2>
 Related Technologies
</h2>
<ul>
 <li>
  <a href="https://github.com/TalAter/awesome-progressive-web-apps#installable-web-apps">
   App Install Banners
  </a>
 </li>
 <li>
  <a href="https://github.com/TalAter/awesome-progressive-web-apps#background-sync">
   Background Sync
  </a>
 </li>
 <li>
  <a href="https://github.com/TalAter/awesome-progressive-web-apps#cachestorage-api">
   CacheStorage API
  </a>
 </li>
 <li>
  <a href="https://github.com/TalAter/awesome-progressive-web-apps#indexeddb">
   IndexedDB
  </a>
 </li>
 <li>
  <a href="https://github.com/TalAter/awesome-progressive-web-apps#push-notifications">
   Push Notifications
  </a>
 </li>
</ul>
