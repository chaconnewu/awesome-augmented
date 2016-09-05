<h1>
 Awesome Pyramid
</h1>
<p>
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
 <a href="https://webchat.freenode.net/?channels=pyramid">
  <img alt="IRC
Freenode" src="https://img.shields.io/badge/irc-freenode-blue.svg"/>
 </a>
</p>
<p>
 A curated list of awesome Pyramid apps, projects and resources. Inspired by and
based on
 <a href="https://github.com/vinta/awesome-python/">
  awesome-python
 </a>
 .
</p>
<ul>
 <li>
  <a href="#awesome-pyramid">
   Awesome Pyramid
  </a>
  <ul>
   <li>
    <a href="#admin-interface">
     Admin Interface
    </a>
   </li>
   <li>
    <a href="#asset-management">
     Asset Management
    </a>
   </li>
   <li>
    <a href="#async">
     Async
    </a>
   </li>
   <li>
    <a href="#authentication">
     Authentication
    </a>
   </li>
   <li>
    <a href="#authorization">
     Authorization
    </a>
   </li>
   <li>
    <a href="#caching--session">
     Caching & Session
    </a>
   </li>
   <li>
    <a href="#debugging">
     Debugging
    </a>
   </li>
   <li>
    <a href="#email">
     Email
    </a>
   </li>
   <li>
    <a href="#forms">
     Forms
    </a>
   </li>
   <li>
    <a href="#media-management">
     Media-Management
    </a>
   </li>
   <li>
    <a href="#restful-api">
     RESTful API
    </a>
   </li>
   <li>
    <a href="#search">
     Search
    </a>
   </li>
   <li>
    <a href="#security">
     Security
    </a>
   </li>
   <li>
    <a href="#services">
     Services
    </a>
   </li>
   <li>
    <a href="#settings">
     Settings
    </a>
   </li>
   <li>
    <a href="#storage">
     Storage
    </a>
   </li>
   <li>
    <a href="#task-queue">
     Task Queue
    </a>
   </li>
   <li>
    <a href="#testing">
     Testing
    </a>
   </li>
   <li>
    <a href="#translations">
     Translations
    </a>
   </li>
   <li>
    <a href="#web-frontend-integration">
     Web frontend integration
    </a>
   </li>
   <li>
    <a href="#workflows">
     Workflows
    </a>
   </li>
   <li>
    <a href="#other">
     Other
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#projects">
   Projects
  </a>
  <ul>
   <li>
    <a href="#framework">
     Framework
    </a>
   </li>
   <li>
    <a href="#cms">
     CMS
    </a>
   </li>
   <li>
    <a href="#e-commerce">
     e-Commerce
    </a>
   </li>
   <li>
    <a href="#project-management">
     Project Management
    </a>
   </li>
   <li>
    <a href="#other">
     Other
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
    <a href="#books">
     Books
    </a>
   </li>
   <li>
    <a href="#websites">
     Websites
    </a>
   </li>
   <li>
    <a href="#conferences">
     Conferences
    </a>
   </li>
   <li>
    <a href="#videos">
     Videos
    </a>
   </li>
   <li>
    <a href="#who-uses-it">
     Who uses it?
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
 Admin interface
</h2>
<p>
 <em>
  Packages that extend the Admin interface, adding or improving features.
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/FormAlchemy/pyramid_formalchemy">
   pyramid_formalchemy
  </a>
  -
provides a CRUD interface for pyramid based on FormAlchemy.
  <sup>
   &#9733 51, pushed 1232 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/sacrud/pyramid_sacrud">
   pyramid
   <em>
    sacrud
   </em>
  </a>
  -    Pyramid CRUD interface.
Provides an administration web interface for Pyramid.
Unlike classic CRUD, pyramid
  <sup>
   &#9733 33, pushed 171 days ago
  </sup>
 </li>
</ul>
sacrud allows overrides and flexibility to
customize your interface, similar to django.contrib.admin but uses a
different backend to provide resources.
<a href="http://pyramid-sacrud.readthedocs.io/pages/contribute/architecture.html">
 New Architecture
</a>
built on the resources and mechanism traversal, allows to use it in various cases.
<ul>
 <li>
  <a href="https://github.com/sacrud/ps_alchemy">
   ps
   <em>
    alchemy
   </em>
  </a>
  - extension for pyramid
  <sup>
   &#9733 3, pushed 131 days ago
  </sup>
 </li>
</ul>
sacrud
which provides SQLAlchemy models.
<li>
 <a href="https://github.com/sacrud/ps_tree">
  ps
  <em>
   tree
  </em>
 </a>
 - extension for
 <a href="https://github.com/sacrud/pyramid_sacrud">
  pyramid
 </a>
 <sup>
  &#9733 0, pushed 423 days ago
 </sup>
</li>
sacrud
which displays
a list of records as tree. This works fine with models from
<a href="https://github.com/uralbash/sqlalchemy_mptt">
 sqlalchemy_mptt
</a>
.
<li>
 <a href="https://websauna.org/docs/">
  Websauna
 </a>
 - a full stack application framework for Pyramid
</li>
<h2>
 Asset Management
</h2>
<p>
 <em>
  Packages that help manage the static assets of a project.
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/sontek/pyramid_webassets">
   pyramid_webassets
  </a>
  - Pyramid
extension for working with the webassets library.
  <sup>
   &#9733 60, pushed 460 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/mrijken/pyramid_bowerstatic">
   pyramid_bowerstatic
  </a>
  -
integration of Bowerstatic in Pyramid
  <sup>
   &#9733 12, pushed 606 days ago
  </sup>
 </li>
</ul>
<h2>
 Async
</h2>
<ul>
 <li>
  <a href="https://github.com/housleyjk/aiopyramid">
   aiopyramid
  </a>
  - Run pyramid using
asyncio.
  <sup>
   &#9733 44, pushed 199 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/abourget/gevent-socketio">
   gevent-socketio
  </a>
  -
gevent-socketio is a Python implementation of the Socket.IO protocol,
developed originally for Node.js by LearnBoost and then ported to other
languages.
  <sup>
   &#9733 1021, pushed 133 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/boothead/stargate">
   Stargate
  </a>
  - Stargate is a package for
adding WebSockets support to pyramid applications using the excellent
eventlet library for long running connections.
  <sup>
   &#9733 35, pushed 1501 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/AppEnlight/channelstream">
   channelstream
  </a>
  - websocket communication server (gevent).
 </li>
</ul>
<h2>
 Authentication
</h2>
<p>
 <em>
  Packages that improve or extend the authentication methods of Pyramid.
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/Pylons/pyramid_ldap">
   pyramid_ldap
  </a>
  - an LDAP
authentication policy for Pyramid.
  <sup>
   &#9733 8, pushed 1146 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Pylons/pyramid_who">
   pyramid_who
  </a>
  - Authentication policy
for pyramid using repoze.who 2.0 API.
  <sup>
   &#9733 10, pushed 1616 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/bbangert/velruse">
   velruse
  </a>
  - Simplifying third-party
authentication for web applications. it supports most of auth
  <a href="https://github.com/bbangert/velruse/tree/master/velruse/providers">
   providers
  </a>
  .
  <sup>
   &#9733 244, pushed 397 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/madjar/pyramid_persona">
   pyramid_persona
  </a>
  - Pyramid plugin
to use
  <a href="https://login.persona.org/">
   persona
  </a>
  for authentication.
  <sup>
   &#9733 24, pushed 360 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/thruflo/pyramid_simpleauth">
   pyramid_simpleauth
  </a>
  - session
based authentication and role based security for Pyramid application
  <sup>
   &#9733 25, pushed 132 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/omab/python-social-auth">
   Python Social Auth
  </a>
  - Social
authentication/registration mechanism with support for a large number of
  <a href="https://github.com/omab/python-social-auth#auth-providers">
   providers
  </a>
  .
  <sup>
   &#9733 2237, pushed 129 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/peterhudec/authomatic">
   Authomatic
  </a>
  -  Simple yet powerful
authorization / authentication client library for Python web applications.
  <sup>
   &#9733 671, pushed 131 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/cd34/apex">
   apex
  </a>
  - Toolkit for Pyramid, a Pylons Project,
to add Authentication and Authorization using Velruse (OAuth) and/or a local
database, CSRF, ReCaptcha, Sessions, Flash messages and I18N.
  <sup>
   &#9733 88, pushed 659 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/usingnamespace/pyramid_authsanity">
   pyramid_authsanity
  </a>
  -
That will make it simpler to have a secure authentication policy with an easy
to use backend.
  <sup>
   &#9733 5, pushed 142 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/wichert/pyramid_jwt">
   pyramid_jwt
  </a>
  - This package
implements an authentication policy for Pyramid that using [JSON Web Tokens].
This standard ([RFC 7519]) is often used to secure backens APIs. The
excellent [PyJWT] library is used for the JWT encoding / decoding logic.
  <sup>
   &#9733 6, pushed 162 days ago
  </sup>
 </li>
</ul>
<h2>
 Authorization
</h2>
<p>
 <em>
  Packages related to authorization infrastructure and permissions.
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/ergo/ziggurat_foundations">
   ziggurat_foundations
  </a>
  -
Framework agnostic set of sqlalchemy classes that make building applications
that require permissions an easy task.
  <sup>
   &#9733 26, pushed 131 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/mozilla-services/pyramid_multiauth">
   pyramid_multiauth
  </a>
  -
An authentication policy for Pyramid that proxies to a stack of other
authentication policies.
  <sup>
   &#9733 29, pushed 207 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/wichert/pyramid_authstack">
   pyramid_authstack
  </a>
  -  Use
multiple authentication policies with Pyramid.
  <sup>
   &#9733 7, pushed 1121 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Pylons/horus">
   horus
  </a>
  - User registration and login system
for the Pyramid Web Framework.
  <sup>
   &#9733 12, pushed 852 days ago
  </sup>
 </li>
</ul>
<h2>
 Caching & Session
</h2>
<p>
 <em>
  Packages that help with caching and session.
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/Pylons/pyramid_beaker">
   pyramid_beaker
  </a>
  - A Beaker session
factory backend for Pyramid, also cache configurator.
  <ul>
   <li>
    <a href="http://techspot.zzzeek.org/2012/04/19/using-beaker-for-caching-why-you-ll-want-to-switch-to-dogpile.cache/">
     Why You'll Want to Switch to
dogpile.cache
    </a>
   </li>
  </ul>
  <sup>
   &#9733 49, pushed 429 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/ericrasmussen/pyramid_redis_sessions">
   pyramid
   <em>
    redis
   </em>
   sessions
  </a>
  -
Pyramid web framework session factory backed by Redis.
  <sup>
   &#9733 36, pushed 294 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/moriyoshi/pyramid_dogpile_cache">
   pyramid
   <em>
    dogpile
   </em>
   cache
  </a>
  -
dogpile.cache configuration package for Pyramid
  <sup>
   &#9733 3, pushed 716 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/joulez/pyramid_sessions">
   pyramid_sessions
  </a>
  - Multiple
session support for the Pyramid Web Framework
  <sup>
   &#9733 0, pushed 605 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Pylons/pyramid_nacl_session">
   pyramid
   <em>
    nacl
   </em>
   session
  </a>
  -
defines an encrypting, pickle-based cookie serializer, using
  <a href="http://pynacl.readthedocs.io/en/latest/secret/">
   PyNaCl
  </a>
  to generate the
symmetric encryption for the cookie state.
  <sup>
   &#9733 5, pushed 202 days ago
  </sup>
 </li>
</ul>
<h2>
 Debugging
</h2>
<p>
 <em>
  Packages that help hunt down bugs.
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/Pylons/pyramid_debugtoolbar">
   pyramid_debugtoolbar
  </a>
  -
provides a debug toolbar useful while you're developing your Pyramid
application.
  <sup>
   &#9733 77, pushed 135 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Pylons/pyramid_exclog">
   pyramid_exclog
  </a>
  - a package which
logs exceptions from Pyramid applications.
  <sup>
   &#9733 20, pushed 152 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jvanasco/pyramid_debugtoolbar_dogpile">
   pyramid
   <em>
    debugtoolbar
   </em>
   dogpile
  </a>
  -
dogpile caching support for pyramid_debugtoolbar
  <sup>
   &#9733 1, pushed 296 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Pylons/pyramid_ipython">
   pyramid_ipython
  </a>
  - IPython
bindings for Pyramid's pshell
  <sup>
   &#9733 0, pushed 320 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Pylons/pyramid_bpython">
   pyramid_bpython
  </a>
  - bpython
bindings for Pyramid's pshell
  <sup>
   &#9733 0, pushed 320 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/disko/pyramid_pycallgraph">
   pyramid_pycallgraph
  </a>
  - Pyramid tween to generate a callgraph image for every request
  <sup>
   &#9733 0, pushed 259 days ago
  </sup>
 </li>
</ul>
<h2>
 Email
</h2>
<p>
 <em>
  Packages that help manage email sending.
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/Pylons/pyramid_mailer">
   pyramid_mailer
  </a>
  - A package for
sending email from your Pyramid application.
  <sup>
   &#9733 41, pushed 364 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/domenkozar/pyramid_marrowmailer">
   pyramid_marrowmailer
  </a>
  -
Pyramid integration package for marrow.mailer, formerly known as TurboMail
  <sup>
   &#9733 4, pushed 613 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/evannook/pyramid_mailgun">
   pyramid_mailgun
  </a>
  -
Pyramid integration package for marrow.mailer, formerly known as TurboMail
  <sup>
   &#9733 0, pushed 221 days ago
  </sup>
 </li>
</ul>
<h2>
 Forms
</h2>
<p>
 <em>
  Packages that extend the functionality of forms or add new types of forms.
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/Pylons/deform">
   deform
  </a>
  - is a Python HTML form generation
library.
  <sup>
   &#9733 170, pushed 143 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Pylons/colander">
   colander
  </a>
  - A
serialization/deserialization/validation library for strings, mappings and
lists.
  <sup>
   &#9733 239, pushed 135 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/wtforms/wtforms">
   WTForms
  </a>
  - is a flexible forms
validation and rendering library for python web development.
  <sup>
   &#9733 507, pushed 134 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/stefanofontanelli/ColanderAlchemy">
   ColanderAlchemy
  </a>
  -
helps you to auto-generate Colander schemas that are based on SQLAlchemy
mapped classes.
  <sup>
   &#9733 53, pushed 248 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/marshmallow-code/marshmallow">
   marshmallow
  </a>
  - A
lightweight library for converting complex objects to and from simple Python
datatypes (i.e. (de)serialization and validation).
  <sup>
   &#9733 1082, pushed 129 days ago
  </sup>
 </li>
</ul>
<h2>
 Media-Management
</h2>
<ul>
 <li>
  <a href="https://github.com/uralbash/pyramid_elfinder">
   pyramid_elfinder
  </a>
  - This is
conector for elfinder file manager, written for pyramid framework.
  <sup>
   &#9733 0, pushed 419 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/danjac/pyramid_storage">
   pyramid_storage
  </a>
  - This is a package for handling file uploads in your Pyramid framework application.
  <sup>
   &#9733 8, pushed 200 days ago
  </sup>
 </li>
</ul>
<h2>
 RESTful API
</h2>
<p>
 <em>
  Packages for developing RESTful APIs.
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/mozilla-services/cornice">
   cornice
  </a>
  - provides helpers to
build & document REST-ish Web Services with Pyramid, with decent default
behaviors. It takes care of following the HTTP specification in an automated
way where possible.
  <sup>
   &#9733 274, pushed 130 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/wichert/rest_toolkit">
   rest
   <em>
    toolkit
   </em>
  </a>
  - is a Python package
which provides a very convenient way to build REST servers. It is build on
top of Pyramid, but you do not need to know much about Pyramid to use
rest
  <sup>
   &#9733 27, pushed 145 days ago
  </sup>
 </li>
</ul>
toolkit.
<li>
 <a href="https://github.com/hadrien/pyramid_royal">
  pyramid_royal
 </a>
 - Royal is a
pyramid extension which eases writing RESTful web applications.
 <sup>
  &#9733 22, pushed 290 days ago
 </sup>
</li>
<li>
 <a href="https://github.com/mozilla-services/cliquet">
  cliquet
 </a>
 - Cliquet is a toolkit
to ease the implementation of HTTP microservices, such as data-driven REST
APIs.
 <sup>
  &#9733 68, pushed 126 days ago
 </sup>
</li>
<li>
 <a href="https://github.com/sloria/webargs">
  webargs
 </a>
 - A friendly library for parsing
HTTP request arguments, with built-in support for popular web frameworks.
 <sup>
  &#9733 312, pushed 126 days ago
 </sup>
</li>
<li>
 <a href="https://github.com/ramses-tech/ramses">
  ramses
 </a>
 - Generate a RESTful API using
RAML. It uses Nefertari which provides ElasticSearch-powered views.
 <sup>
  &#9733 219, pushed 157 days ago
 </sup>
</li>
<li>
 <a href="https://github.com/ramses-tech/nefertari">
  nefertari
 </a>
 -  Nefertari is a REST
API framework sitting on top of Pyramid and ElasticSearch
 <sup>
  &#9733 38, pushed 127 days ago
 </sup>
</li>
<li>
 <a href="https://github.com/striglia/pyramid_swagger">
  pyramid_swagger
 </a>
 - Convenient
tools for using Swagger to define and validate your interfaces in a Pyramid webapp.
 <sup>
  &#9733 33, pushed 132 days ago
 </sup>
</li>
<h2>
 Search
</h2>
<p>
 <em>
  Packages that provide search capabilities to projects.
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/Pylons/hypatia">
   hypatia
  </a>
  - A Python indexing and
searching system.
  <sup>
   &#9733 21, pushed 154 days ago
  </sup>
 </li>
</ul>
<h2>
 Security
</h2>
<p>
 <em>
  Packages that improve the security of a project.
 </em>
</p>
<h2>
 Services
</h2>
<ul>
 <li>
  <a href="https://github.com/websauna/pyramid_sms">
   pyramid_sms
  </a>
  -
SMS services for Pyramid web framework.
  <sup>
   &#9733 2, pushed 129 days ago
  </sup>
 </li>
</ul>
<h2>
 Settings
</h2>
<p>
 <em>
  Packages that help manage the configurability of projects.
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/Pylons/pyramid_zcml">
   pyramid_zcml
  </a>
  - Zope Configuration
Markup Language configuration support for Pyramid.
  <sup>
   &#9733 3, pushed 176 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/mmerickel/pyramid_services">
   pyramid_services
  </a>
  - defines a
pattern and helper methods for accessing a pluggable service layer from
within your Pyramid apps.
  <sup>
   &#9733 39, pushed 214 days ago
  </sup>
 </li>
</ul>
<h2>
 Storage
</h2>
<p>
 <em>
  Packages that extend the functionality of the existing storage backend or
provide new storage backends.
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/Pylons/pyramid_tm">
   pyramid_tm
  </a>
  - Centralized transaction
management for Pyramid applications (without middleware).
  <sup>
   &#9733 24, pushed 132 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/zopefoundation/zope.sqlalchemy">
   zope.sqlalchemy
  </a>
  -
Integration of SQLAlchemy with transaction management.
  <ul>
   <li>
    <a href="https://metaclassical.com/what-the-zope-transaction-manager-means-to-me-and-you/">
     What the Zope Transaction Manager Means To Me (and
you)
    </a>
   </li>
  </ul>
  <sup>
   &#9733 17, pushed 133 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/wichert/pyramid_sqlalchemy">
   pyramid_sqlalchemy
  </a>
  -
provides some basic glue to facilitate using SQLAlchemy with Pyramid.
  <sup>
   &#9733 21, pushed 130 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Pylons/pyramid_zodbconn">
   pyramid_zodbconn
  </a>
  - ZODB
Database connection management for Pyramid.
  <sup>
   &#9733 4, pushed 256 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/marioidival/pyramid_mongoengine">
   pyramid_mongoengine
  </a>
  -
pyramid-mongoengine package based on flask-mongoengine
  <sup>
   &#9733 8, pushed 397 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/niallo/pyramid_mongodb">
   pyramid_mongodb
  </a>
  - 
Basic Pyramid Scaffold to easily use MongoDB for persistence with the Pyramid Web framework
  <sup>
   &#9733 39, pushed 996 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/pyexcel/pyramid-excel">
   pyramid-excel
  </a>
  - pyramid-excel is based on
  <a href="https://github.com/pyexcel/pyexcel">
   pyexcel
  </a>
  and makes it easy to consume/produce information stored in excel files over HTTP protocol as well as on file system. This library can turn the excel data into a list of lists, a list of records(dictionaries), dictionaries of lists. And vice versa. Hence it lets you focus on data in Pyramid based web development, instead of file formats.
 </li>
</ul>
<h2>
 Task Queue
</h2>
<p>
 <em>
  Packages that make working with task/background queues easier.
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/sontek/pyramid_celery">
   pyramid_celery
  </a>
  - Pyramid
configuration with celery integration. Allows you to use pyramid .ini files
to configure celery and have your pyramid configuration inside celery tasks.
  <sup>
   &#9733 71, pushed 280 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/wichert/pyramid_rq">
   pyramid_rq
  </a>
  - Support using the rq
queueing system with pyramid. The easiest way to monitor and use
  <a href="http://python-rq.org">
   RQ
  </a>
  in your Pyramid projects.
  <sup>
   &#9733 8, pushed 535 days ago
  </sup>
 </li>
</ul>
<h2>
 Templates
</h2>
<ul>
 <li>
  <a href="https://github.com/Pylons/pyramid_mako">
   pyramid_mako
  </a>
  - Mako templating
system bindings for the Pyramid web framework.
  <sup>
   &#9733 15, pushed 512 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Pylons/pyramid_chameleon">
   pyramid_chameleon
  </a>
  - Chameleon
template compiler for pyramid.
  <sup>
   &#9733 7, pushed 147 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Pylons/pyramid_jinja2">
   pyramid_jinja2
  </a>
  - Jinja2
templating system bindings for the Pyramid web framework.
  <sup>
   &#9733 63, pushed 226 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/ztane/Tonnikala">
   Tonnikala
  </a>
  - Python templating engine
with Pyramid integration
  <sup>
   &#9733 0, pushed 411 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/nandoflorestan/kajiki">
   Kajiki
  </a>
  - provides fast well-formed XML templates, with
  <a href="https://github.com/nandoflorestan/kajiki/blob/master/kajiki/integration/pyramid.py">
   Pyramid integration
  </a>
 </li>
</ul>
<h2>
 Testing
</h2>
<p>
 <em>
  Packages that help test code or generate test data.
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/Pylons/webtest">
   webtest
  </a>
  - Wraps any WSGI application and
makes it easy to send test requests to that application, without starting up
an HTTP server.
  <sup>
   &#9733 150, pushed 146 days ago
  </sup>
 </li>
</ul>
<h2>
 Translations
</h2>
<p>
 <em>
  Packages help with the task of translating projects.
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/wichert/lingua">
   lingua
  </a>
  - Lingua is a package with tools
to extract translatable texts from your code, and to check existing
translations. It replaces the use of the xgettext command from gettext, or
pybabel from Babel.
  <sup>
   &#9733 36, pushed 150 days ago
  </sup>
 </li>
</ul>
<h2>
 Web frontend integration
</h2>
<h2>
 Workflows
</h2>
<p>
 <em>
  Packages that do process, procedure and/or business tasks management.
 </em>
</p>
<h2>
 Other
</h2>
<ul>
 <li>
  <a href="https://github.com/Pylons/pyramid_layout">
   pyramid_layout
  </a>
  - Pyramid add-on
for managing UI layouts.
  <sup>
   &#9733 17, pushed 136 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Pylons/pyramid_skins">
   pyramid_skins
  </a>
  - This package
provides a simple framework to integrate code with templates and resources.
  <sup>
   &#9733 0, pushed 713 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Pylons/waitress">
   waitress
  </a>
  - Waitress is meant to be a
production-quality pure-Python WSGI server with very acceptable performance.
It has no dependencies except ones which live in the Python standard library.
  <sup>
   &#9733 254, pushed 142 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Pylons/pyramid_handlers">
   pyramid_handlers
  </a>
  - analogue of
Pylons-style “controllers” for Pyramid.
  <sup>
   &#9733 9, pushed 1338 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Pylons/pyramid_rpc">
   pyramid
   <em>
    rpc
   </em>
  </a>
  - RPC service add-on for
Pyramid, supports XML-RPC in a more extensible manner than pyramid
  <sup>
   &#9733 20, pushed 145 days ago
  </sup>
 </li>
</ul>
xmlrpc
with support for JSON-RPC and AMF.
<li>
 <a href="https://github.com/SurveyMonkey/pyramid_autodoc">
  pyramid_autodoc
 </a>
 - Sphinx
extension for documenting your Pyramid APIs.
 <sup>
  &#9733 6, pushed 130 days ago
 </sup>
</li>
<li>
 <a href="https://github.com/uralbash/pyramid_pages">
  pyramid_pages
 </a>
 - Provides a
collections of tree pages to your Pyramid application. This is very similar
to django.contrib.flatpages but with a tree structure and traversal algorithm
in URL dispath.
 <sup>
  &#9733 7, pushed 126 days ago
 </sup>
</li>
<li>
 <a href="https://github.com/Pylons/paginate">
  paginate
 </a>
 - Python pagination module.
 <sup>
  &#9733 20, pushed 135 days ago
 </sup>
</li>
<li>
 <a href="https://github.com/lxneng/pyramid_tablib">
  pyramid_tablib
 </a>
 - tablib renderer
(xlsx, xls, csv) for pyramid
 <sup>
  &#9733 6, pushed 543 days ago
 </sup>
</li>
<li>
 <a href="https://github.com/sontek/tomb_routes">
  tomb_routes
 </a>
 - Simple utility library
around pyramid routing
 <sup>
  &#9733 1, pushed 439 days ago
 </sup>
</li>
<li>
 <a href="https://github.com/jenner/pyramid_extdirect">
  pyramid_extdirect
 </a>
 - This pyramid plugin provides a router for the ExtDirect Sencha API included in ExtJS. ExtDirect allows to run server-side callbacks directly through JavaScript without the extra AJAX boilerplate.
 <sup>
  &#9733 11, pushed 155 days ago
 </sup>
</li>
<h1>
 Projects
</h1>
<p>
 <em>
  Outstanding Pyramid projects.
 </em>
</p>
<h2>
 Framework
</h2>
<ul>
 <li>
  <a href="http://www.ringo-framework.org/">
   Ringo
  </a>
  - Ringo is a Python based high level
web application framework build on top of Pyramid. The framework can be used
to build form based management or administration software.
 </li>
</ul>
<h2>
 CMS
</h2>
<ul>
 <li>
  <a href="https://github.com/nive/nive_cms">
   nive_cms
  </a>
  - Nive is professional out the
box content management system for mobile and desktop websites based on python
and the webframework pyramid. Please refer to the website cms.nive.co for
detailed information.
  <sup>
   &#9733 11, pushed 178 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Pylons/substanced">
   substanced
  </a>
  - An application server
built upon the Pyramid web framework. It provides a user interface for
managing content as well as libraries and utilities which make it easy to
create applications.
  <sup>
   &#9733 115, pushed 144 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Kotti/Kotti">
   Kotti
  </a>
  - A user-friendly, light-weight and
extensible web content management system. Based on Pyramid and SQLAlchemy.
  <sup>
   &#9733 292, pushed 138 days ago
  </sup>
 </li>
 <li>
  <a href="https://karlproject.readthedocs.io/en/latest/">
   KARL
  </a>
  - A moderately-sized
application (roughly 80K lines of Python code) built on top of Pyramid. It is
an open source web
system for collaboration, organizational intranets, and knowledge management.
It provides facilities for wikis, calendars, manuals, searching, tagging,
commenting, and file uploads. See the KARL site for download and installation
details.
 </li>
</ul>
<h2>
 e-Commerce
</h2>
<h2>
 Other
</h2>
<ul>
 <li>
  <a href="https://github.com/Pylons/cluegun">
   cluegun
  </a>
  - A simple pastebin application
based on Rocky Burt’s ClueBin. It demonstrates form processing, security, and
the use of ZODB within a Pyramid application.
  <sup>
   &#9733 20, pushed 1663 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Pylons/shootout">
   shootout
  </a>
  - An example “idea
competition” application by Carlos de la Guardia and Lukasz Fidosz. It
demonstrates URL dispatch, simple authentication, integration with SQLAlchemy
and pyramid_simpleform.
  <sup>
   &#9733 94, pushed 1067 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Pylons/virginia">
   virginia
  </a>
  - A very simple dynamic
file rendering application. It is willing to render structured text
documents, HTML documents, and images from a filesystem directory. It’s also
a good example of traversal. An earlier version of this application runs the
repoze.org website.
  <sup>
   &#9733 19, pushed 1663 days ago
  </sup>
 </li>
 <li>
  <a href="http://docs.pylonsproject.org/projects/akhet/en/latest/">
   Akhet
  </a>
  -     A
Pyramid library and demo application with a Pylons-like feel. Its most known
for its former application scaffold, which helped users transition from
  Pylons and those preferring a more Pylons-like API. The scaffold has been
  retired but the demo plays a similar role.
 </li>
 <li>
  <a href="http://khufuproject.github.io/">
   Khufu Project
  </a>
  - Khufu is an application
scaffolding for Pyramid that provides an environment to work with Jinja2 and
SQLAlchemy.
 </li>
 <li>
  <a href="https://github.com/ptahproject/ptah">
   Ptah
  </a>
  - Ptah is a fast, fun, open
source high-level Python web development environment.
  <sup>
   &#9733 73, pushed 449 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/pypa/warehouse">
   warehouse
  </a>
  - Warehouse is a next
generation Python Package Repository designed to replace the legacy code base
that currently powers PyPI.
  <sup>
   &#9733 522, pushed 125 days ago
  </sup>
 </li>
 <li>
  <a href="http://www.travelcrm.org.ua/">
   travelcrm
  </a>
  - TravelCRM is effective free and open source application for the automation of customer relationships for travel agencies at all levels, from small to large networks.
 </li>
</ul>
<h2>
 Project Management
</h2>
<h1>
 Resources
</h1>
<p>
 Where to discover new Pyramid apps and projects.
</p>
<h2>
 Books
</h2>
<ul>
 <li>
  <a href="http://www.oreilly.com/web-platform/free/python-web-frameworks.csp">
   Python Web Frameworks
  </a>
  - Dive into details on the top
six Python frameworks—Django, Flask, Tornado, Bottle, Pyramid, and CherryPy.
 </li>
</ul>
<h2>
 Websites
</h2>
<ul>
 <li>
  <a href="https://trypyramid.com/">
   Try Pyramid
  </a>
  - The Start Small, Finish Big,
Stay Finished Framework. Official website.
 </li>
</ul>
<h2>
 Conferences
</h2>
<ul>
 <li>
  <a href="https://2016.ploneconf.org/">
   PloneConf 2016
  </a>
  - Boston Plone Digital Experience Conference (17~23 Oct. 2016)
 </li>
</ul>
<h2>
 Videos
</h2>
<ul>
 <li>
  <p>
   <a href="http://shop.oreilly.com/product/0636920041900.do">
    Web Applications with Python and the Pyramid
Framework
   </a>
   -
In this Web Applications with Python and the Pyramid Framework training
course, expert author Paul Everitt will teach you about the features needed
for Python web development, as well as Pyramid's unique features. This
course is designed for users that already have a basic knowledge of Python.
  </p>
  <p>
   You will start by learning about single file web apps, templating, and
multiple routes and views. From there, Paul will teach you about MyApp
Python package, views and routes, and templating and static assets. This
video tutorial also covers forms, databases, and sessions, authentication
and authorization, and JSON. Finally, you will learn about extensibility,
including custom configuration settings, extending and overriding, and
custom view predicates.
  </p>
  <p>
   Once you have completed this computer based training course, you will have
gained a basic understanding of the features needed for Python web
development and the features unique to Pyramid.
  </p>
 </li>
</ul>
<h2>
 Who uses it?
</h2>
<ul>
 <li>
  <a href="https://trypyramid.com/community-powered-by-pyramid.html">
   Projects, Websites, Companies and Organizations that use
Pyramid
  </a>
  - add your project to the list
 </li>
</ul>
<h1>
 Contributing
</h1>
<p>
 Just fork and send a pull request with your awesome Pyramid apps, projects or
resources.
</p>
<h2>
 License
</h2>
<p>
 <a href="https://creativecommons.org/publicdomain/zero/1.0/">
  <img alt="CC0" src="https://licensebuttons.net/p/zero/1.0/88x31.png"/>
 </a>
</p>
<p>
 To the extent possible under law, @uralbash has waived all copyright and related
or neighboring rights to this work.
</p>
