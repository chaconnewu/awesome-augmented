<h1>
 Awesome Rails Gem
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<p>
 A collection of awesome Ruby Gems for Rails development.
</p>
<p>
 The goal is to help every Rails developer to build an awesome Rails product/service.
</p>
<ul>
 <li>
  <a href="#rails-gem-list">
   Rails Gem List
  </a>
  <ul>
   <li>
    <a href="#user">
     User
    </a>
   </li>
   <li>
    <a href="#active-record">
     Active Record
    </a>
   </li>
   <li>
    <a href="#plugins">
     Plugins
    </a>
   </li>
   <li>
    <a href="#api">
     API
    </a>
   </li>
   <li>
    <a href="#email">
     Email
    </a>
   </li>
   <li>
    <a href="#file-uploading">
     File Uploading
    </a>
   </li>
   <li>
    <a href="#searching">
     Searching
    </a>
   </li>
   <li>
    <a href="#scheduledrecurrence-jobs">
     Scheduled/Recurrence Jobs
    </a>
   </li>
   <li>
    <a href="#view-helper">
     View Helper
    </a>
   </li>
   <li>
    <a href="#environment-variables">
     Environment Variables
    </a>
   </li>
   <li>
    <a href="#admin-panel">
     Admin Panel
    </a>
   </li>
   <li>
    <a href="#logging">
     Logging
    </a>
   </li>
   <li>
    <a href="#debug">
     Debug
    </a>
   </li>
   <li>
    <a href="#coding-style">
     Coding Style
    </a>
   </li>
   <li>
    <a href="#testing">
     Testing
    </a>
   </li>
   <li>
    <a href="#production">
     Production
    </a>
   </li>
   <li>
    <a href="#error-logging">
     Error Logging
    </a>
   </li>
  </ul>
 </li>
</ul>
<h2>
 User
</h2>
<h3>
 Authentication
</h3>
<ul>
 <li>
  <a href="https://github.com/plataformatec/devise/">
   Devise
  </a>
  - Devise is a flexible authentication solution for Rails based on Warden.
 </li>
 <li>
  <a href="https://github.com/nsarno/knock">
   Knock
  </a>
  - Seamless JWT authentication for Rails API.
  <sup>
   &#9733 400, pushed 6 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/thoughtbot/clearance">
   Clearance
  </a>
  - Rails authentication with email & password.
  <sup>
   &#9733 2314, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/lynndylanhurley/devise_token_auth">
   Devise token auth
  </a>
  - Token based authentication for Rails JSON APIs.
  <sup>
   &#9733 1237, pushed 10 days ago
  </sup>
 </li>
</ul>
<h3>
 Authorization
</h3>
<ul>
 <li>
  <a href="https://github.com/elabs/pundit">
   Pundit
  </a>
  - Pundit provides a set of helpers which guide you in leveraging regular Ruby classes and object oriented design patterns to build a simple, robust and scaleable authorization system.
  <sup>
   &#9733 4240, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/CanCanCommunity/cancancan">
   cancancan
  </a>
  - Continuation of CanCan, the authorization Gem for Ruby on Rails.CanCan is an authorization library for Ruby on Rails which restricts what resources a given user is allowed to access. All permissions are defined in a single location (the Ability class) and not duplicated across controllers, views, and database queries.
  <sup>
   &#9733 2870, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/RolifyCommunity/rolify">
   rolify
  </a>
  - Role management library with resource scoping.
  <sup>
   &#9733 1749, pushed 15 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/be9/acl9/">
   acl9
  </a>
  - Acl9 is a role-based authorization system that provides a concise DSL for securing your Rails application.
 </li>
</ul>
<h3>
 Omniauth
</h3>
<ul>
 <li>
  <a href="https://github.com/mkdynamic/omniauth-facebook">
   omniauth-facebook
  </a>
  <sup>
   &#9733 909, pushed 42 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/zquestz/omniauth-google-oauth2">
   omniauth-google-oauth2
  </a>
  <sup>
   &#9733 681, pushed 22 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/beenhero/omniauth-weibo-oauth2">
   omniauth-weibo-oauth2
  </a>
  <sup>
   &#9733 125, pushed 8 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/arunagw/omniauth-twitter">
   omniauth-twitter
  </a>
  <sup>
   &#9733 445, pushed 43 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/intridea/omniauth-github">
   omniauth-github
  </a>
  <sup>
   &#9733 271, pushed 106 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/decioferreira/omniauth-linkedin-oauth2">
   omniauth-linkedin-oauth2
  </a>
  <sup>
   &#9733 60, pushed 168 days ago
  </sup>
 </li>
</ul>
<h2>
 Active Record
</h2>
<ul>
 <li>
  <a href="https://github.com/brainspec/enumerize">
   Enumerize
  </a>
  - Enumerated attributes with I18n and ActiveRecord/Mongoid support. It can be integrated with Simple Form.
  <sup>
   &#9733 1062, pushed 6 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/magnusvk/counter_culture">
   counter_culture
  </a>
  - Turbo-charged counter caches for your Rails app. Huge improvements over the Rails standard counter caches.
  <sup>
   &#9733 612, pushed 9 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/cedric/custom_counter_cache">
   custom
   <em>
    counter
   </em>
   cache
  </a>
  - A simple approach to creating a custom counter cache that can be used across multiple models.
  <sup>
   &#9733 42, pushed 168 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/djreimer/sequenced">
   Sequenced
  </a>
  - Sequenced is a simple gem that generates scoped sequential IDs for ActiveRecord models.
  <sup>
   &#9733 110, pushed 25 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/norman/friendly_id">
   FriendlyId
  </a>
  - FriendlyId is the “Swiss Army bulldozer” of slugging and permalink plugins for ActiveRecord. It allows you to create pretty URL’s and work with human-friendly strings as if they were numeric ids for ActiveRecord models.
  <sup>
   &#9733 4045, pushed 6 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/aasm/aasm">
   AASM
  </a>
  - State machines for Ruby classes (plain Ruby, Rails Active Record, Mongoid).
  <sup>
   &#9733 2344, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/airblade/paper_trail">
   PaperTrail
  </a>
  - PaperTrail lets you track changes to your models' data. It's good for auditing or versioning.
  <sup>
   &#9733 3944, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/rubysherpas/paranoia">
   paranoia
  </a>
  - ActiveRecord plugin allowing you to hide and restore records without actually deleting them.
  <sup>
   &#9733 1481, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/kaize/validates">
   Validates
  </a>
  - Validates provides collection of useful custom validators for Rails applications, including:
  <ul>
   <li>
    EmailValidator
   </li>
   <li>
    UrlValidator
   </li>
   <li>
    SlugValidator
   </li>
   <li>
    MoneyValidator
   </li>
   <li>
    IpValidator
   </li>
   <li>
    AssociationLengthValidator
   </li>
   <li>
    AbsolutePathValidator
   </li>
   <li>
    UriComponentValidator
   </li>
   <li>
    ColorValidator
   </li>
   <li>
    EanValidator (EAN-8 & EAN-13)
   </li>
  </ul>
  <sup>
   &#9733 97, pushed 168 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/globalize/globalize">
   globalize
  </a>
  - Rails I18n de-facto standard library for ActiveRecord model/data translation.
  <sup>
   &#9733 1281, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/moiristo/deep_cloneable">
   deep_cloneable
  </a>
  - This gem gives every ActiveRecord::Base object the possibility to do a deep clone that includes user specified associations.
  <sup>
   &#9733 288, pushed 81 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Timrael/social_shares">
   social_shares
  </a>
  - Check how many times url was shared in social networks.
  <sup>
   &#9733 239, pushed 23 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/chaps-io/public_activity">
   public_activity
  </a>
  - Easy activity tracking for models - similar to Github's Public Activity.
  <sup>
   &#9733 2118, pushed 8 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/salsify/goldiloader">
   goldiloader
  </a>
  - Automatic ActiveRecord eager loading to reduce the number of database queries run by your application.
  <sup>
   &#9733 482, pushed 59 days ago
  </sup>
 </li>
 <li>
  Tagging
  <ul>
   <li>
    <a href="https://github.com/mbleigh/acts-as-taggable-on">
     ActsAsTaggableOn
    </a>
    - A tagging plugin for Rails applications that allows for custom tagging along dynamic contexts.
   </li>
   <li>
    <a href="https://github.com/mceachen/closure_tree">
     closure_tree
    </a>
    - Easily and efficiently make your ActiveRecord models support hierarchies.
    <sup>
     &#9733 832, pushed 8 days ago
    </sup>
   </li>
  </ul>
  <sup>
   &#9733 3650, pushed 12 days ago
  </sup>
 </li>
</ul>
<h2>
 Plugins
</h2>
<ul>
 <li>
  <a href="https://github.com/zdavatz/spreadsheet">
   Spreadsheet
  </a>
  - Library is designed to read and write Spreadsheet Documents.
  <sup>
   &#9733 607, pushed 35 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/ankane/chartkick">
   Chartkick
  </a>
  - Chartkick helps your to create beautiful Javascript charts with one line of Ruby.
  <sup>
   &#9733 3592, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/amatsuda/kaminari">
   kaminari
  </a>
  - A Scope & Engine based, clean, powerful, customizable and sophisticated paginator for Rails 3 and 4.
  <sup>
   &#9733 5736, pushed 13 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/galetahub/ckeditor">
   CKEditor
  </a>
  - CKEditor is a WYSIWYG text editor designed to simplify web content creation. It brings common word processing features directly to your web pages. Enhance your website experience with our community maintained editor.
  <a href="http://ckeditor.com">
   ckeditor.com
  </a>
  <sup>
   &#9733 1511, pushed 34 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jch/html-pipeline">
   HTML::Pipeline
  </a>
  - GitHub HTML processing filters and utilities. This module includes a small framework for defining DOM based content filters and applying them to user provided content.
  <sup>
   &#9733 1640, pushed 7 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/stevenosloan/slack-notifier">
   Slack Notifier
  </a>
  is a simple wrapper to send notifications to
  <a href="https://slack.com/">
   Slack
  </a>
  webhooks.
  <sup>
   &#9733 613, pushed 18 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/voormedia/rails-erd">
   Rails ERD
  </a>
  - Generate Entity-Relationship Diagrams for Rails applications.
  <sup>
   &#9733 1553, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/thoughtbot/parity">
   Parity
  </a>
  - Shell commands for development, staging, and production parity for Heroku apps.
  <sup>
   &#9733 368, pushed 13 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/mattbrictson/airbrussh">
   Airbrussh
  </a>
  - Airbrussh pretties up your SSHKit and Capistrano output
  <sup>
   &#9733 446, pushed 8 days ago
  </sup>
 </li>
</ul>
<h2>
 API
</h2>
<ul>
 <li>
  <a href="https://github.com/ruby-grape/grape">
   Grape
  </a>
  - Microframework to create REST-ful APIs in Ruby.
  <sup>
   &#9733 7240, pushed 1 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/rails-api/active_model_serializers">
   ActiveModel::Serializers
  </a>
  - Serializer brings convention over configuration to your JSON generation.
  <sup>
   &#9733 3473, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/rails/jbuilder">
   Jbuilder
  </a>
  - Jbuilder gives you a simple DSL for declaring JSON structures that beats massaging giant hash structures. This is particularly helpful when the generation process is fraught with conditionals and loops.
  <sup>
   &#9733 2562, pushed 12 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/rest-client/rest-client">
   rest-client
  </a>
  - Simple HTTP and REST client for Ruby, inspired by microframework syntax for specifying actions.
  <sup>
   &#9733 3324, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/plataformatec/has_scope">
   has_scope
  </a>
  - Map incoming controller parameters to named scopes in your resources.
  <sup>
   &#9733 1085, pushed 120 days ago
  </sup>
 </li>
 <li>
  Documentation
  <ul>
   <li>
    <a href="https://github.com/ruby-grape/grape-swagger">
     Grape Swagger
    </a>
    - Autogenerate documentation on Grape API.
   </li>
   <li>
    <a href="https://github.com/swagger-api/swagger-ui">
     Grape Swagger UI
    </a>
    - Display documentation that is generated using Grape Swagger.
    <sup>
     &#9733 4841, pushed 4 days ago
    </sup>
   </li>
   <li>
    <a href="https://apiary.io/">
     apiary
    </a>
    - Work together to quickly design, prototype, document and test APIs.
   </li>
   <li>
    <a href="https://apiblueprint.org">
     apiblueprint
    </a>
    - API Documentation with powerful tooling.
   </li>
  </ul>
  <sup>
   &#9733 638, pushed 2 days ago
  </sup>
 </li>
</ul>
<h2>
 Email
</h2>
<ul>
 <li>
  <a href="https://github.com/ryanb/letter_opener">
   letter_opener
  </a>
  - Preview mail in the browser instead of sending.
  <sup>
   &#9733 2243, pushed 12 days ago
  </sup>
 </li>
</ul>
<h2>
 File Uploading
</h2>
<ul>
 <li>
  <a href="https://github.com/carrierwaveuploader/carrierwave">
   Carrierwave
  </a>
  - Carrierwave is a classier solution for file uploads for Rails, Sinatra and other Ruby web frameworks.
  <ul>
   <li>
    <a href="https://github.com/lardawge/carrierwave_backgrounder">
     carrierwave
     <em>
      backgrounder
     </em>
    </a>
    - Offload CarrierWave's image processing and storage to a background process using Delayed Job, Resque, Sidekiq, Qu, Queue Classic or Girl Friday.
    <sup>
     &#9733 590, pushed 43 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/kirtithorat/carrierwave-crop/">
     CarrierWave Crop
    </a>
    - Carrierwave extension to crop uploaded images using Jcrop plugin with preview.
   </li>
   <li>
    <a href="https://github.com/jtescher/carrierwave-imageoptimizer">
     CarrierWave ImageOptimizer
    </a>
    - This gem allows you to simply optimize CarrierWave images via jpegoptim or optipng using the image
    <sup>
     &#9733 119, pushed 97 days ago
    </sup>
   </li>
  </ul>
  <sup>
   &#9733 6645, pushed 2 days ago
  </sup>
 </li>
</ul>
optimizer gem.
<li>
 <a href="https://github.com/JangoSteve/remotipart">
  remotipart
 </a>
 - Rails jQuery file uploads via standard Rails "remote: true" forms.
 <sup>
  &#9733 849, pushed 12 days ago
 </sup>
</li>
<li>
 <a href="https://github.com/minimagick/minimagick">
  MiniMagick
 </a>
 - MiniMagick is a ruby wrapper for ImageMagick or GraphicsMagick command line.
 <sup>
  &#9733 1748, pushed 39 days ago
 </sup>
</li>
<li>
 <a href="https://github.com/fog/fog">
  fog
 </a>
 - Fog is the Ruby cloud services library, top to bottom.
 <sup>
  &#9733 3829, pushed 8 days ago
 </sup>
</li>
<li>
 <a href="https://github.com/refile/refile">
  refile
 </a>
 - Refile is a modern file upload library for Ruby applications. It is simple, yet powerful.
 <sup>
  &#9733 2154, pushed 14 days ago
 </sup>
</li>
<li>
 <a href="https://github.com/thoughtbot/paperclip">
  Paperclip
 </a>
 - Easy file attachment management for ActiveRecord.
 <sup>
  &#9733 7828, pushed 3 days ago
 </sup>
</li>
<h2>
 Searching
</h2>
<ul>
 <li>
  <a href="https://github.com/activerecord-hackery/ransack">
   ransack
  </a>
  - Ransack enables the creation of both simple and advanced search forms for your Ruby on Rails application.
  <sup>
   &#9733 2693, pushed 6 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/elastic/elasticsearch-rails">
   elasticsearch-rails
  </a>
  - Elasticsearch integrations for ActiveModel/Record and Ruby on Rails.
  <sup>
   &#9733 1565, pushed 11 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/toptal/chewy">
   Chewy
  </a>
  - High-level Elasticsearch Ruby framework based on the official elasticsearch-ruby client.
  <sup>
   &#9733 857, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/averell23/chewy_kiqqer">
   Chewy_Kiqqer
  </a>
  - This is an alternative update/callback mechanism for Chewy. It queues the updates as Sidekiq jobs.
  <sup>
   &#9733 27, pushed 104 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Casecommons/pg_search">
   pg
   <em>
    search
   </em>
  </a>
  - pg
  <sup>
   &#9733 1488, pushed 15 days ago
  </sup>
 </li>
</ul>
search builds ActiveRecord named scopes that take advantage of PostgreSQL's full text search
<li>
 <a href="https://github.com/sunspot/sunspot">
  sunspot
 </a>
 - Sunspot is a Ruby library for expressive, powerful interaction with the Solr search engine. Sunspot is built on top of the RSolr library, which provides a low-level interface for Solr interaction; Sunspot provides a simple, intuitive, expressive DSL backed by powerful features for indexing objects and searching for them.
 <sup>
  &#9733 2536, pushed 4 days ago
 </sup>
</li>
<li>
 <a href="https://github.com/ankane/searchkick">
  searchkick
 </a>
 - Intelligent search made easy with Rails and Elasticsearch.
 <sup>
  &#9733 2745, pushed 10 days ago
 </sup>
</li>
<h2>
 Scheduled/Recurrence Jobs
</h2>
<ul>
 <li>
  <a href="https://github.com/javan/whenever">
   Whenever
  </a>
  - Whenever is a Ruby gem that provides a clear syntax for writing and deploying cron jobs.
  <sup>
   &#9733 6324, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/resque/resque">
   Resque
  </a>
  - Redis-backed Ruby library for creating background jobs, placing them on multiple queues, and processing them later.
  <sup>
   &#9733 7254, pushed 7 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/collectiveidea/delayed_job">
   Delayed Job
  </a>
  - Database based asynchronous priority queue system.
  <sup>
   &#9733 3847, pushed 15 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/mperham/sidekiq">
   Sidekiq
  </a>
  - Simple, efficient background processing for Ruby.
  <ul>
   <li>
    <a href="https://github.com/tobiassvn/sidetiq">
     sidetiq
    </a>
    - Recurring jobs for sidekiq.
    <sup>
     &#9733 1113, pushed 19 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/ondrejbartas/sidekiq-cron">
     sidekiq-cron
    </a>
    - Scheduler / Cron for Sidekiq jobs
    <sup>
     &#9733 312, pushed 8 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/Moove-it/sidekiq-scheduler">
     sidekiq-scheduler
    </a>
    - Lightweight job scheduler extension for Sidekiq
    <sup>
     &#9733 200, pushed 6 days ago
    </sup>
   </li>
  </ul>
  <sup>
   &#9733 6214, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/brandonhilkert/sucker_punch">
   Sucker Punch
  </a>
  - Sucker punch is a single-process Ruby asynchronous processing library.
  <sup>
   &#9733 1827, pushed 8 days ago
  </sup>
 </li>
</ul>
<h2>
 View Helper
</h2>
<ul>
 <li>
  <a href="https://github.com/justinfrench/formtastic">
   formtastic
  </a>
  - Formtastic is a Rails FormBuilder DSL (with some other goodies) to make it far easier to create beautiful, semantically rich, syntactically awesome, readily stylable and wonderfully accessible HTML forms in your Rails applications
  <sup>
   &#9733 4842, pushed 14 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/plataformatec/simple_form">
   Simple Form
  </a>
  - Simple form aims to be as flexible as possible while helping you with powerful components to create your forms. The basic goal of Simple Form is to not touch your way of defining the layout, letting you find the better design for your eyes.
  <sup>
   &#9733 6002, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/ryanb/nested_form">
   Nested Form
  </a>
  - This is a Rails gem for conveniently manage multiple nested models in a single form. It does so in an unobtrusive way through jQuery or Prototype. It can also be integrated with Simple Form.
  <sup>
   &#9733 1677, pushed 94 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/kpumuk/meta-tags">
   meta-tags
  </a>
  - Search Engine Optimization (SEO) plugin for Ruby on Rails applications.
  <sup>
   &#9733 1283, pushed 49 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/comfy/active_link_to">
   active
   <em>
    link
   </em>
   to
  </a>
  - active
  <em>
   link
  </em>
  to adds css 'active' class to your links.
  <sup>
   &#9733 483, pushed 69 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/apotonick/cells">
   cells
  </a>
  - Cells allow you to encapsulate parts of your UI into components into view models. View models, or cells, are simple ruby classes that can render templates.
  <sup>
   &#9733 2560, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/onomojo/i18n_country_select">
   i18n Country Code Select
  </a>
  - I18n Country Code Select Form Helper for Rails 3 & 4.
  <sup>
   &#9733 22, pushed 197 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/cllns/subdivision_select">
   Subdivision Select
  </a>
  - A Rails plugin to populate a state/province select box from country_select.
  <sup>
   &#9733 4, pushed 13 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/nathanvda/cocoon">
   cocoon
  </a>
  - Dynamic nested forms using jQuery made easy
  <sup>
   &#9733 1959, pushed 43 days ago
  </sup>
 </li>
</ul>
<h2>
 Environment Variables
</h2>
<ul>
 <li>
  <a href="https://github.com/railsconfig/config">
   Config
  </a>
  - Multi-environment YAML style configurations that helps easily manage environment specific settings in an easy and usable manner.
  <sup>
   &#9733 1018, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/laserlemon/figaro">
   Figaro
  </a>
  - Figaro is very simple, Heroku-friendly Rails app configuration using ENV and a single YAML file.
  <sup>
   &#9733 2640, pushed 7 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/bkeepers/dotenv">
   dotenv
  </a>
  - Dotenv is a gem that allows you to set your environment variables in .env file, and it will load it in to ENV.
  <sup>
   &#9733 3259, pushed 20 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/mikamai/opsworks-dotenv">
   opsworks-dotenv
  </a>
  - Opsworks-dotenv let you configure the environment for you Rails application using OpsWorks, Chef and Dotenv.
  <sup>
   &#9733 8, pushed 87 days ago
  </sup>
 </li>
</ul>
<h2>
 Admin Panel
</h2>
<ul>
 <li>
  <a href="http://activeadmin.info">
   ActiveAdmin
  </a>
  - ActiveAdmin is a administration framework for Ruby on Rails applications.
  <ul>
   <li>
    <a href="https://github.com/rstgroup/active_skin">
     active_skin
    </a>
    : Flat skin for active admin.
    <sup>
     &#9733 326, pushed 210 days ago
    </sup>
   </li>
  </ul>
 </li>
 <li>
  <a href="https://github.com/sferik/rails_admin">
   RailsAdmin
  </a>
  - RailsAdmin is a Rails engine that provides an easy-to-use interface for managing your data.
  <sup>
   &#9733 5960, pushed 5 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/typus/typus">
   Typus
  </a>
  - Typus is a control panel for Ruby on Rails applications to allow trusted users edit structured content.
  <sup>
   &#9733 1093, pushed 42 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/thoughtbot/administrate">
   administrate
  </a>
  - A Rails engine that helps you put together a super-flexible admin dashboard.
  <sup>
   &#9733 2457, pushed 6 days ago
  </sup>
 </li>
</ul>
<h2>
 Logging
</h2>
<ul>
 <li>
  <a href="https://github.com/charlotte-ruby/impressionist">
   Impressionist
  </a>
  - Impressionist can log page impressions (technically action impressions), but it is not limited to that. You can log impressions multiple times per request. And you can also attach it to a model. The goal of this project is to provide customizable stats that are immediately accessible in your application as opposed to using Google Analytics and pulling data using their API.
  <sup>
   &#9733 860, pushed 91 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/ankane/ahoy">
   Ahoy
  </a>
  - Ahoy provides a solid foundation to track visits and events in Ruby, JavaScript, and native apps.
  <sup>
   &#9733 1484, pushed 40 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/roidrage/lograge">
   Lograge
  </a>
  - An attempt to tame Rails' default policy to log everything.
  <sup>
   &#9733 1612, pushed 2 days ago
  </sup>
 </li>
</ul>
<h2>
 Debug
</h2>
<ul>
 <li>
  <a href="https://github.com/deivid-rodriguez/byebug">
   byebug
  </a>
  - Byebug is a simple to use, feature rich debugger for Ruby 2. It uses the new TracePoint API for execution control and the new Debug Inspector API for call stack navigation, so it doesn't depend on internal core sources.
  <ul>
   <li>
    <a href="https://github.com/deivid-rodriguez/pry-byebug">
     pry-byebug
    </a>
    - Pry navigation commands via byebug.
    <sup>
     &#9733 825, pushed 26 days ago
    </sup>
   </li>
  </ul>
  <sup>
   &#9733 1938, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/rweng/pry-rails">
   pry-rails
  </a>
  - Avoid repeating yourself, use pry-rails instead of copying the initializer to every rails project. This is a small gem which causes rails console to open pry. It therefore depends on pry.
  <sup>
   &#9733 788, pushed 289 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/michaeldv/awesome_print">
   awesome_print
  </a>
  - Awesome Print is a Ruby library that pretty prints Ruby objects in full color exposing their internal structure with proper indentation.
  <sup>
   &#9733 2739, pushed 19 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/rails/web-console">
   web-console
  </a>
  - Web Console is a debugging tool for your Ruby on Rails applications.
  <sup>
   &#9733 932, pushed 50 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/rails/spring">
   spring
  </a>
  - Spring is a Rails application preloader. It speeds up development by keeping your application running in the background so you don't need to boot it every time you run a test, rake task or migration.
  <sup>
   &#9733 2111, pushed 21 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/josevalim/rails-footnotes">
   rails-footnotes
  </a>
  - Rails footnotes displays footnotes in your application for easy debugging, such as sessions, request parameters, cookies, filter chain, routes, queries, etc.
  <sup>
   &#9733 1405, pushed 60 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jugyo/g">
   g
  </a>
  - The Kernel.g that works like Kernel.p by using terminal-notifier or growl.
  <sup>
   &#9733 98, pushed 1007 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/julienXX/terminal-notifier">
   terminal-notifier
  </a>
  - terminal-notifier is a command-line tool to send Mac OS X User Notifications, which are available in Mac OS X 10.8 and higher.
  <sup>
   &#9733 3243, pushed 160 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/ryanb/letter_opener">
   letter_opener
  </a>
  - Preview email in the default browser instead of sending it. This means you do not need to set up email delivery in your development environment, and you no longer need to worry about accidentally sending a test email to someone else's address.
 </li>
 <li>
  <a href="https://github.com/charliesome/better_errors">
   Better Errors
  </a>
  - Better errors replaces the standard Rails error page with a much better and more useful error page.
  <ul>
   <li>
    If you would like to use Better Errors' advanced features (REPL, local/instance variable inspection, pretty stack frame names), you need to add the
    <a href="https://github.com/banister/binding_of_caller">
     binding_
     <em>
      of
     </em>
     _caller
    </a>
    .
    <sup>
     &#9733 462, pushed 105 days ago
    </sup>
   </li>
  </ul>
  <sup>
   &#9733 5735, pushed 18 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/dejan/rails_panel">
   RailsPanel
  </a>
  - RailsPanel is a Chrome extension for Rails development that will end your tailing of development.log.
  <sup>
   &#9733 2603, pushed 22 days ago
  </sup>
 </li>
</ul>
<h2>
 Coding Style
</h2>
<ul>
 <li>
  <a href="https://github.com/bbatsov/rubocop">
   RuboCop
  </a>
  - Rubocop is a Ruby static code analyzer. Out of the box it will enforce many of the guidelines outlined in the community
  <a href="https://github.com/bbatsov/ruby-style-guide">
   Ruby Style Guide
  </a>
  .
  <sup>
   &#9733 6230, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/railsbp/rails_best_practices">
   Rails Best Practice
  </a>
  - Rails best practice is a code metric tool to check the quality of rails codes.
  <sup>
   &#9733 3071, pushed 25 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/metricfu/metric_fu">
   Metric Fu
  </a>
  - A fist full of code metrics
  <sup>
   &#9733 506, pushed 92 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/mmozuras/pronto">
   Pronto
  </a>
  - Quick automated code review of your changes
  <sup>
   &#9733 1071, pushed 2 days ago
  </sup>
 </li>
</ul>
<h2>
 Testing
</h2>
<ul>
 <li>
  <a href="https://github.com/rspec/rspec-rails">
   rspec-rails
  </a>
  - Rspec-rails is a testing framework for Rails 3.x and 4.x.
  <sup>
   &#9733 2793, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jnicklas/capybara">
   Capybara
  </a>
  - Capybara helps you test web applications by simulating how a real user would interact with your app. And drivers:
  <ul>
   <li>
    <a href="https://github.com/thoughtbot/capybara-webkit">
     capybara-webkit
    </a>
    - Capybara-webkit is a capybara driver that uses Webkit via QtWebkit.
    <sup>
     &#9733 1696, pushed 7 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/vertis/selenium-webdriver">
     selenium-webdriver
    </a>
    - Selenium-webdriver provides ruby bindings for WebDriver.
    <sup>
     &#9733 22, pushed 138 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/teampoltergeist/poltergeist">
     poltergeist
    </a>
    - Poltergeist allows you to run your Capybara tests on a headless WebKit browser, provided by PhantomJS.
    <sup>
     &#9733 2097, pushed 14 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/cheezy/page-object">
     page-object
    </a>
    - Page-object is a simple gem that assists in creating flexible page objects for testing browser based applications.
    <sup>
     &#9733 455, pushed 25 days ago
    </sup>
   </li>
  </ul>
  <sup>
   &#9733 6964, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/thoughtbot/factory_girl">
   factory
   <em>
    girl
   </em>
  </a>
  - Factory
  <sup>
   &#9733 4724, pushed 10 days ago
  </sup>
 </li>
</ul>
girl is a fixtures replacement with a straightforward definition syntax, support for multiple build strategies (saved instances, unsaved instances, attribute hashes, and stubbed objects), and support for multiple factories for the same class (user, admin_user, and so on), including factory inheritance.
<li>
 <a href="https://github.com/thoughtbot/factory_girl_rails">
  factory
  <em>
   girl
  </em>
  rails
 </a>
 - Factory
 <em>
  girl
 </em>
 rails provides Rails integration for factory_girl.
 <sup>
  &#9733 1563, pushed 4 days ago
 </sup>
</li>
<li>
 <a href="https://github.com/st0012/factory_factory_girl">
  factory
  <em>
   factory
  </em>
  girl
 </a>
 - FactoryFactoryGirl lets you generate factory files more efficiently with naming rules.
 <sup>
  &#9733 40, pushed 252 days ago
 </sup>
</li>
<li>
 <a href="https://github.com/DatabaseCleaner/database_cleaner">
  Database Cleaner
 </a>
 - Database Cleaner is a set of strategies for cleaning your database in Ruby.Support ActiveRecord, DataMapper, Sequel, MongoMapper, Mongoid, CouchPotato, Ohm and Redis.
 <sup>
  &#9733 1781, pushed 11 days ago
 </sup>
</li>
<li>
 <a href="https://github.com/thoughtbot/shoulda-matchers">
  shoulda-matchers
 </a>
 - Shoulda-matchers provides serveral matchers for testing common Rails functionality.
 <sup>
  &#9733 1642, pushed 13 days ago
 </sup>
</li>
<li>
 <a href="https://github.com/r7kamura/response_code_matchers">
  ResponseCodeMatchers
 </a>
 - ResponseCodeMatchers provides rspec matchers to match http response code.
 <sup>
  &#9733 43, pushed 440 days ago
 </sup>
</li>
<li>
 <a href="https://github.com/colszowka/simplecov">
  SimpleCov
 </a>
 - SimpleCov is a code coverage analysis tool for Ruby.
 <sup>
  &#9733 2593, pushed 12 days ago
 </sup>
</li>
<li>
 <a href="https://github.com/travisjeffery/timecop">
  Timecop
 </a>
 - A gem providing "time travel" and "time freezing" capabilities, making it dead simple to test time-dependent code.
 <sup>
  &#9733 2055, pushed 25 days ago
 </sup>
</li>
<li>
 <a href="https://github.com/vcr/vcr">
  VCR
 </a>
 - Record your test suite's HTTP interactions and replay them during future test runs for fast, deterministic, accurate tests.
 <sup>
  &#9733 2930, pushed 5 days ago
 </sup>
</li>
<h3>
 Security
</h3>
<ul>
 <li>
  <a href="https://github.com/presidentbeef/brakeman">
   brakeman
  </a>
  - Brakeman is a static analysis tool which checks Ruby on Rails applications for security vulnerabilities.
  <sup>
   &#9733 3322, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/rubysec/bundler-audit">
   bundle-audit
  </a>
  - bundler-audit is a patch-level verification tool for Bundler which checks for vulnerable versions of gems and insecure gem sources.
  <sup>
   &#9733 1097, pushed 18 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/twitter/secureheaders">
   Secure Headers
  </a>
  -  Secure Headers will automatically apply several headers that are related to security.
  <sup>
   &#9733 1666, pushed 4 days ago
  </sup>
 </li>
</ul>
<h2>
 Production
</h2>
<ul>
 <li>
  <a href="https://github.com/capistrano/capistrano">
   Capistrano
  </a>
  - Remote multi-server automation tool.
  <sup>
   &#9733 8298, pushed 6 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/ankane/slowpoke">
   Slowpoke
  </a>
  - Rack::Timeout is great. Slowpoke makes it better.
  <sup>
   &#9733 87, pushed 83 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/kickstarter/rack-attack">
   Rack Attack
  </a>
  - Rack middleware to blocking & throttling.
  <sup>
   &#9733 2526, pushed 39 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/plataformatec/responders">
   Responders
  </a>
  - A set of Rails responders to dry up your application.
  <sup>
   &#9733 1371, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/ankane/production_rails">
   production_rails
  </a>
  - Best practices for running Rails in production.
  <sup>
   &#9733 444, pushed 132 days ago
  </sup>
 </li>
</ul>
<h2>
 Error Logging
</h2>
<ul>
 <li>
  <a href="https://github.com/rollbar/rollbar-gem">
   Rollbar
  </a>
  - Exception tracking and logging from Ruby to Rollbar.
  <sup>
   &#9733 163, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/airbrake/airbrake">
   Airbrake
  </a>
  - Notifier gem for integrating apps with Airbrake
  <sup>
   &#9733 697, pushed 11 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/errbit/errbit">
   Errbit
  </a>
  - Open source notifier gem compliant with Airbrake.
  <sup>
   &#9733 3350, pushed 7 days ago
  </sup>
 </li>
</ul>
<h2>
 Asset Pipeline
</h2>
<ul>
 <li>
  <a href="https://github.com/mavenlink/alaska">
   Alaska
  </a>
  - ExecJS runtime with persistent connection to nodejs, speeds up your coffeescript compilation process during development and deployment.
  <sup>
   &#9733 39, pushed 163 days ago
  </sup>
 </li>
</ul>
<h2>
 Contribute
</h2>
<p>
 Contributions welcome! Read the
 <a href="contributing.md">
  contribution guidelines
 </a>
 first.
</p>
