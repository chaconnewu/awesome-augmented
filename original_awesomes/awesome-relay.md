<h1>
 Awesome Relay
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<p>
 Awesome resources for
 <a href="https://github.com/facebook/relay">
  Relay
 </a>
 , based on the
 <a href="https://github.com/sindresorhus/awesome/">
  Awesome
 </a>
 project
</p>
<h1>
 Table of Contents
</h1>
<ul>
 <li>
  <a href="#learning-resources">
   Learning Resources
  </a>
  <ul>
   <li>
    <a href="#documentation">
     Documentation
    </a>
   </li>
   <li>
    <a href="#faqs">
     FAQs
    </a>
   </li>
   <li>
    <a href="#tutorials">
     Tutorials
    </a>
   </li>
   <li>
    <a href="#overviews">
     Overviews
    </a>
   </li>
   <li>
    <a href="#example-implementations">
     Example Implementations
    </a>
   </li>
   <li>
    <a href="#lists-of-lists">
     Lists of Lists
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#ecosystem">
   Ecosystem
  </a>
  <ul>
   <li>
    <a href="#libraries--packages">
     Libraries & Packages
    </a>
   </li>
   <li>
    <a href="#tooling">
     Tooling
    </a>
   </li>
   <li>
    <a href="#starter-kits">
     Starter Kits
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#relay-specific-server-support">
   Relay-Specific Server Support
  </a>
  <ul>
   <li>
    <a href="#go">
     Go
    </a>
   </li>
   <li>
    <a href="#javascript">
     JavaScript
    </a>
   </li>
   <li>
    <a href="#python">
     Python
    </a>
   </li>
   <li>
    <a href="#ruby">
     Ruby
    </a>
   </li>
   <li>
    <a href="#rails">
     Rails
    </a>
   </li>
   <li>
    <a href="#scala">
     Scala
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#testing">
   Testing
  </a>
 </li>
</ul>
<h1>
 Learning Resources
</h1>
<h2>
 Documentation
</h2>
<ul>
 <li>
  <a href="https://facebook.github.io/relay/docs/getting-started.html#content">
   Official Docs
  </a>
  - Official Relay documentation.
 </li>
</ul>
<h2>
 FAQs
</h2>
<ul>
 <li>
  <a href="https://gist.github.com/wincent/598fa75e22bdfa44cf47">
   Unofficial Relay FAQ
  </a>
  - Common questions answered! Relay resources are scarce at the moment, so this is very helpful if you get stuck.
 </li>
</ul>
<h2>
 Tutorials
</h2>
<ul>
 <li>
  <a href="https://auth0.com/blog/2015/10/06/getting-started-with-relay/">
   Getting Started with Relay
  </a>
  - One of the few detailed walk throughs of hand-on Relay.
 </li>
 <li>
  <a href="https://medium.com/@clayallsopp/relay-101-building-a-hacker-news-client-bb8b2bdc76e6#.1i64q1pf9">
   Relay 101: Building A Hacker News Client
  </a>
  - A complete workable example.
  <ul>
   <li>
    <a href="https://medium.com/@clayallsopp/relay-102-mutations-d8b471a4730e#.i9vuv3vxl">
     Relay 102: Mutations
    </a>
    - A follow up to "Relay 101" concentrating on mutations.
   </li>
  </ul>
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=sP3n-nht0Xo">
   Facebook Relay talk - Lunch and Learn session
  </a>
  - Walkthrough of building a simple app, and demonstration of
  <a href="https://github.com/graphql/graphiql">
   GraphiQL
  </a>
  .
 </li>
 <li>
  <a href="http://blog.pathgather.com/blog/a-beginners-guide-to-relay-mutations">
   A Beginner's Guide to Relay Mutations
  </a>
  - Mutations in depth.
 </li>
</ul>
<h2>
 Overviews
</h2>
<ul>
 <li>
  <a href="http://www.sitepoint.com/react-data-fetching-with-relay/">
   React Data Fetching with Relay
  </a>
  - Clear conceptual overview of Relay's moving parts and magic.
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=IrgHurBjQbg">
   Joseph Savona - Relay: An Application Framework For React
  </a>
  - Conceptual overview of Relay from the Facebook team.
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=X6YbAKiLCLU">
   F8 2015 - React Native & Relay: Bringing Modern Web Techniques to Mobile
  </a>
  - Overview of Relay, some about the philosophy.
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=dvWTxy1eY6s">
   Relay - Daniel Dembach - Hamburg React.js Meetup
  </a>
  - A good general overview of Relay, some discussion of alternatives. Common questions are covered in Q&A at the end.
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=sP3n-nht0Xo">
   Facebook Relay talk - Lunch and Learn session
  </a>
  - Walkthrough of building a simple app, and demonstration of
  <a href="https://github.com/graphql/graphiql">
   GraphiQL
  </a>
  .
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=Cfna8gwt9h8">
   React with Relay and GraphQL with Andrew Smith
  </a>
  - High level overview of Relay and GraphQL, with some useful discussion from the audience. Some discussion of other front-end frameworks, as well.
 </li>
 <li>
  <a href="http://sgwilym.github.io/relay-visual-learners/">
   Relay for Visual Learners
  </a>
  - Very clear set of diagrams laying out how the different parts of Relay relate to each other.
 </li>
 <li>
  <a href="http://www.slideshare.net/BrooklynZelenka/relay-seamless-syncing-for-react-vanjs">
   Relay: Seamless Syncing For React
  </a>
  - An overview of what Relay is, and some discussion of experience using it in production.
 </li>
 <li>
  Cartoon Intro to Facebook's Relay - An overview of how Relay works, complete with illustrations.
  <ul>
   <li>
    <a href="https://code-cartoons.com/a-cartoon-intro-to-facebook-s-relay-part-1-3ec1a127bca5">
     Part 1: Saying what data you need with GraphQL
    </a>
   </li>
   <li>
    <a href="https://code-cartoons.com/a-cartoon-intro-to-facebook-s-relay-part-2-d4a2435aee59">
     Part 2: Fetching data from the server
    </a>
   </li>
   <li>
    <a href="https://code-cartoons.com/a-cartoon-intro-to-facebook-s-relay-part-3-9d8fcf8db670">
     Part 3: Syncing changes back up to the server
    </a>
   </li>
   <li>
    <a href="https://code-cartoons.com/a-cartoon-intro-to-facebook-s-relay-part-4-aef7d819a8ed">
     Part 4: How it all fits together
    </a>
   </li>
  </ul>
 </li>
</ul>
<h2>
 Example Implementations
</h2>
<ul>
 <li>
  <a href="https://github.com/taion/relay-todomvc">
   Relay TODO MVC
  </a>
  - The classic TODO example app, written with Relay.
  <sup>
   27 GitHub links in total 80 links, &#9733 73, pushed 12 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/transedward/relay-chat">
   <code>
    relay-chat
   </code>
  </a>
  - Relay with routing and pagination.
  <sup>
   27 GitHub links in total 80 links, &#9733 71, pushed 141 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/chentsulin/koa-graphql-relay-example">
   <code>
    koa-graphql-relay-example
   </code>
  </a>
  - "TODO" app with
  <a href="https://github.com/chentsulin/koa-graphql">
   <code>
    koa-graphql
   </code>
  </a>
  and
  <code>
   relay
  </code>
  .
  <sup>
   27 GitHub links in total 80 links, &#9733 24, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/sogko/todomvc-relay-go">
   <code>
    todomvc-relay-go
   </code>
  </a>
  - Relay TodoMVC app, driven by a Golang GraphQL backend.
  <sup>
   27 GitHub links in total 80 links, &#9733 15, pushed 166 days ago
  </sup>
 </li>
</ul>
<h2>
 Lists of Lists
</h2>
<ul>
 <li>
  <a href="https://quip.com/oLxzA1gTsJsE">
   Relay and GraphQL Introduction Materials
  </a>
 </li>
</ul>
<h1>
 Ecosystem
</h1>
<h2>
 Libraries & Packages
</h2>
<ul>
 <li>
  <a href="https://github.com/graphql/graphql-relay-js">
   <code>
    graphql-relay-js
   </code>
  </a>
  - Simplifies creating a JS GraphQL server for
  <code>
   react-relay
  </code>
  .
  <sup>
   27 GitHub links in total 80 links, &#9733 460, pushed 8 days ago
  </sup>
 </li>
 <li>
  <a href="https://www.npmjs.com/package/babel-relay-plugin">
   Babel Relay Plugin
  </a>
  - Use Relay the latest ES6+ syntax.
 </li>
 <li>
  <a href="https://github.com/relay-tools/react-router-relay">
   <code>
    react-router-relay
   </code>
  </a>
  -
  <code>
   react-router
  </code>
  bindings for Relay. Greatly simplifies many local state UI uses cases.
  <ul>
   <li>
    <a href="https://medium.com/@cpojer/relay-and-routing-36b5439bad9#.h91614i65">
     Relay and Routing
    </a>
    - A well-articulated walk through of
    <code>
     react-router-relay
    </code>
    , and the problems that it solves.
   </li>
   <li>
    <a href="https://www.npmjs.com/package/relay-nested-routes">
     <code>
      relay-nested-routes
     </code>
    </a>
    - Generate nested routes that reflect nested data. Helpful for managing deep data.
   </li>
   <li>
    <a href="https://github.com/denvned/isomorphic-relay-router">
     <code>
      isomorphic-relay-router
     </code>
    </a>
    - Server side rendering support for
    <code>
     react-router-relay
    </code>
    .
    <sup>
     27 GitHub links in total 80 links, &#9733 64, pushed 2 days ago
    </sup>
   </li>
  </ul>
  <sup>
   27 GitHub links in total 80 links, &#9733 356, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/4Catalyzer/relay-decorators">
   <code>
    relay-decorator
   </code>
  </a>
  - Simply syntax for Relay containers with ES7 decorators (
  <code>
   @
  </code>
  syntax)
  <sup>
   27 GitHub links in total 80 links, &#9733 2, pushed 62 days ago
  </sup>
 </li>
 <li>
  <a href="https://www.npmjs.com/package/recompose-relay">
   <code>
    recompose-relay
   </code>
  </a>
  - Ease composition of Relay containers by currying and providing the component after the container.
 </li>
 <li>
  <a href="https://github.com/relay-tools/relay-local-schema">
   <code>
    relay-local-schema
   </code>
  </a>
  - Use a local schema; no need for a remote GraphQL server.
  <sup>
   27 GitHub links in total 80 links, &#9733 91, pushed 21 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/lenaten/react-native-relay">
   <code>
    react-native-relay
   </code>
  </a>
  - Use Relay with React Native.
  <ul>
   <li>
    May be supported
    <a href="https://github.com/facebook/relay/issues/26">
     out of the box
    </a>
    in the future.
   </li>
  </ul>
  <sup>
   27 GitHub links in total 80 links, &#9733 56, pushed 40 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/acdlite/relay-sink">
   <code>
    relay-sink
   </code>
  </a>
  - Use Relay to fetch and store data outside of a React component.
  <sup>
   27 GitHub links in total 80 links, &#9733 107, pushed 148 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/guymers/babel-plugin-flow-relay-query">
   <code>
    babel-plugin-flow-relay-query
   </code>
  </a>
  - Convert
  <a href="http://flowtype.org">
   Flow
  </a>
  types into Relay fragments.
  <sup>
   27 GitHub links in total 80 links, &#9733 10, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/MattMcFarland/sequelize-relay">
   <code>
    sequelize-relay
   </code>
  </a>
  - Make Relay compatible with
  <a href="https://github.com/sequelize/sequelize">
   <code>
    sequelize
   </code>
  </a>
  .
  <sup>
   27 GitHub links in total 80 links, &#9733 41, pushed 99 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/mikberg/relay-mongodb-connection">
   <code>
    relay-mongodb-connection
   </code>
  </a>
  - Create Relay connections from MongoDB cursors.
  <sup>
   27 GitHub links in total 80 links, &#9733 4, pushed 169 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/eyston/relay-composite-network-layer">
   <code>
    relay-composite-network-layer
   </code>
  </a>
  - Compose your Relay Network Layer of many different Network Layers each with their own schema.
  <sup>
   27 GitHub links in total 80 links, &#9733 28, pushed 127 days ago
  </sup>
 </li>
</ul>
<h2>
 Tooling
</h2>
<ul>
 <li>
  <a href="https://github.com/graphql/graphiql">
   GraphiQL
  </a>
  - A library to introspect GraphQL, test queries and mutations.
  <ul>
   <li>
    <a href="https://github.com/skevy/graphiql-app">
     GraphiQL App
    </a>
    - A standalone app for viewing GraphQL, introspection docs, and testing queries/mutations. Invaluable for debugging your Relay app.
    <sup>
     27 GitHub links in total 80 links, &#9733 186, pushed 76 days ago
    </sup>
   </li>
  </ul>
  <sup>
   27 GitHub links in total 80 links, &#9733 1295, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/relay-tools/relay-local-schema">
   <code>
    relay-local-schema
   </code>
  </a>
  - Use a local schema; no need for a remote GraphQL server.
 </li>
 <li>
  <a href="https://www.npmjs.com/package/babel-relay-plugin">
   Babel Relay Plugin
  </a>
  - Use Relay the latest ES6+ syntax.
 </li>
</ul>
<h2>
 Starter Kits
</h2>
<ul>
 <li>
  <a href="https://github.com/fortruce/relay-skeleton">
   Relay Skeleton
  </a>
  - Relay project skeleton.
  <sup>
   27 GitHub links in total 80 links, &#9733 94, pushed 71 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/relayjs/relay-starter-kit">
   Relay Starter Kit
  </a>
  - An app that it already set up with a basic setup. Just clone and tweak to suit your needs!
  <sup>
   27 GitHub links in total 80 links, &#9733 667, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/mhart/simple-relay-starter">
   Simple Relay Starter
  </a>
  - A Browserify version of the
  <a href="https://github.com/relayjs/relay-starter-kit">
   Relay Starter Kit
  </a>
  .
  <sup>
   27 GitHub links in total 80 links, &#9733 86, pushed 27 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/codefoundries/isomorphic-material-relay-starter-kit">
   Isomorphic Material Relay Starter Kit
  </a>
  - Isomorphic Relay starter kit with examples. Uses Material-UI, Webpack, hot reload, Helmet, JWT. Utilizes Facebook Data Loader for persistence into in-memory structures and Cassandra.
  <sup>
   27 GitHub links in total 80 links, &#9733 169, pushed 12 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/nethsix/relay-on-rails">
   Relay on Rails Starter Kit
  </a>
  - A barebones starter kit for Relay application on Rails server. Just clone and tweak!
  <sup>
   27 GitHub links in total 80 links, &#9733 19, pushed 186 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/lvarayut/relay-fullstack">
   Relay Fullstack
  </a>
  - Relay Starter Kit integrated with Relay, Express, Webpack, Babel, Material Design Lite, and PostCSS.
  <sup>
   27 GitHub links in total 80 links, &#9733 333, pushed 2 days ago
  </sup>
 </li>
</ul>
<h1>
 Relay-Specific Server Support
</h1>
<h2>
 Go
</h2>
<ul>
 <li>
  <a href="https://github.com/graphql-go/relay">
   Go Relay
  </a>
  - A Go/Golang library to help construct a graphql-go server supporting react-relay.
  <sup>
   27 GitHub links in total 80 links, &#9733 63, pushed 55 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/sogko/todomvc-relay-go">
   <code>
    todomvc-relay-go
   </code>
  </a>
  - React/Relay TodoMVC app, driven by a Golang GraphQL backend.
 </li>
</ul>
<h2>
 JavaScipt
</h2>
<ul>
 <li>
  <a href="https://github.com/graphql/graphql-relay-js">
   <code>
    graphql-relay-js
   </code>
  </a>
  - Simplifies creating a JS GraphQL server for
  <code>
   react-relay
  </code>
  .
 </li>
</ul>
<h2>
 Python
</h2>
<ul>
 <li>
  <a href="https://github.com/graphql-python/graphql-relay-py">
   <code>
    graphql-relay-py
   </code>
  </a>
  - A library to help construct a
  <code>
   graphql-py
  </code>
  server supporting
  <code>
   react-relay
  </code>
  .
  <sup>
   27 GitHub links in total 80 links, &#9733 61, pushed 195 days ago
  </sup>
 </li>
</ul>
<h2>
 Ruby
</h2>
<ul>
 <li>
  <a href="https://github.com/rmosolgo/graphql-relay-ruby">
   <code>
    graphql-relay-ruby
   </code>
  </a>
  - Relay helpers for GraphQL & Ruby.
  <sup>
   27 GitHub links in total 80 links, &#9733 77, pushed 4 days ago
  </sup>
 </li>
</ul>
<h3>
 Rails
</h3>
<ul>
 <li>
  <a href="https://medium.com/@gauravtiwari/graphql-and-relay-on-rails-first-relay-powered-react-component-cb3f9ee95eca#.c88zcoftn">
   GraphQL and Relay on Rails — First relay powered react component
  </a>
  - Full walk through of a simple Relay setup, including clonable code.
 </li>
 <li>
  <a href="https://medium.com/@khor/relay-facebook-on-rails-8b4af2057152#.5hjih9wms">
   Relay/GraphQL On Rails
  </a>
  - A brief example of Relay with Rails, complete with several diagrams to aid in comprehension.
 </li>
 <li>
  <a href="https://github.com/nethsix/relay-on-rails">
   Relay on Rails Starter Kit
  </a>
  - A barebones starter kit for Relay application on Rails server. Just clone and tweak!
 </li>
</ul>
<h2>
 Scala
</h2>
<ul>
 <li>
  <a href="https://github.com/sangria-graphql/sangria-relay">
   <code>
    sangria-relay
   </code>
  </a>
  - Relay support for
  <a href="http://sangria-graphql.org">
   Sangria
  </a>
  .
  <sup>
   27 GitHub links in total 80 links, &#9733 30, pushed 2 days ago
  </sup>
 </li>
</ul>
<h1>
 Testing
</h1>
<ul>
 <li>
  <a href="https://medium.com/@mikaelberg/writing-simple-unit-tests-with-relay-707f19e90129">
   Writing Simple Unit Tests with Relay
  </a>
  - An early first look at testing Relay.
 </li>
</ul>
