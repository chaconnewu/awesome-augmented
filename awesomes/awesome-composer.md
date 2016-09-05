<h2>
 Awesome Composer
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
 <a href="https://travis-ci.org/jakoch/awesome-composer">
  <img alt="Build Status" src="https://api.travis-ci.org/jakoch/awesome-composer.svg?branch=master"/>
 </a>
 <a href="">
  <img alt="license" src="https://img.shields.io/github/license/jakoch/awesome-composer.svg?maxAge=2592000"/>
 </a>
</h2>
<p>
 <a href="https://getcomposer.org/">
  <img align="right" src="https://raw.githubusercontent.com/jakoch/awesome-composer/master/logo-composer-transparent.png" width="150"/>
 </a>
</p>
<blockquote>
 <p>
  A curated list of resources for Composer, Packagist, Satis, Plugins, Scripts, Videos, Tutorials.
 </p>
</blockquote>
<p>
 You might also like
 <a href="https://github.com/ziadoz/awesome-php">
  awesome-php
 </a>
 .
</p>
<p>
 <em>
  Please read the
  <a href="contributing.md">
   contribution guidelines
  </a>
  before contributing.
 </em>
</p>
<h2>
 Composer
</h2>
<ul>
 <li>
  <a href="https://getcomposer.org/">
   Official Website
  </a>
 </li>
 <li>
  <a href="https://github.com/composer/composer/issues">
   Issues
  </a>
 </li>
 <li>
  <a href="https://github.com/composer/composer">
   Github
  </a>
 </li>
 <li>
  <a href="https://getcomposer.org/doc/00-intro.md">
   Getting Started Guide and Installation Instructions
  </a>
 </li>
 <li>
  <a href="https://getcomposer.org/doc/">
   Documentation
  </a>
 </li>
 <li>
  <a href="https://getcomposer.org/apidoc/master/index.html">
   API Documentation
  </a>
 </li>
 <li>
  <a href="https://packagist.org/">
   Find Packages on Packagist
  </a>
 </li>
 <li>
  <a href="http://composer.json.jolicode.com/">
   CheatSheet
  </a>
  - Overview of CLI commands and
  <code>
   composer.json
  </code>
  schema.
 </li>
 <li>
  <a href="https://github.com/composer/installers">
   Composer Installers
  </a>
  - Composer installers for multiple frameworks.
  <sup>
   &#9733 541, pushed 134 days ago
  </sup>
 </li>
</ul>
<h3>
 Support
</h3>
<h4>
 Stack Overflow
</h4>
<ul>
 <li>
  You might use the following tags:
  <code>
   composer-php
  </code>
  ,
  <code>
   packagist
  </code>
  ,
  <code>
   satis
  </code>
  +
  <code>
   php
  </code>
  .
 </li>
 <li>
  <a href="http://stackoverflow.com/questions/ask?tags=composer-php+php">
   Ask a new question
  </a>
 </li>
 <li>
  <a href="http://stackoverflow.com/questions/tagged/composer-php">
   Find questions tagged
   <code>
    composer-php
   </code>
  </a>
 </li>
</ul>
<h4>
 IRC
</h4>
<ul>
 <li>
  IRC channels are on
  <code>
   irc.freenode.org
  </code>
  :
  <a href="https://webchat.freenode.net/?channels=composer">
   #composer
  </a>
  for users and
  <a href="https://webchat.freenode.net/?channels=composer-dev">
   #composer-dev
  </a>
  for development.
 </li>
</ul>
<h2>
 Plugins
</h2>
<ul>
 <li>
  <a href="https://getcomposer.org/doc/articles/plugins.md">
   Documentation for Plugins
  </a>
  - This offical documentation is good starting point, when writing a Composer plugin.
 </li>
 <li>
  <a href="https://github.com/fxpio/composer-asset-plugin">
   Composer-Asset-Plugin
  </a>
  - A npm/Bower Dependencies Manager for Composer.
 </li>
 <li>
  <a href="https://github.com/naderman/composer-aws">
   Composer-AWS
  </a>
  - The plugin loads repository data and downloads packages from Amazon S3 (with authentication support for private repositories).
 </li>
 <li>
  <a href="https://github.com/bamarni/composition">
   Composer-Composition
  </a>
  - Provides an API, for checking your environment at runtime.
  <sup>
   &#9733 93, pushed 171 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/nfreear/composer-suggest">
   Composer-Suggest
  </a>
  - Enables you to install a custom group of suggested packages, based on keyword patterns.
 </li>
 <li>
  <a href="https://github.com/deprecat/climb">
   Climb
  </a>
  - Climb is a "Composer version manager tool" inspired by
  <code>
   npm-check-updates
  </code>
  . It shows the outdates package version and indicates "upgrades" to latest versions.
 </li>
 <li>
  <a href="https://github.com/Soullivaneuh/composer-versions-check">
   Composer-Versions-Check
  </a>
  - Shows outdated packages from last major versions after using the update command (showing "Latest is vX.Y.Z").
 </li>
 <li>
  <a href="https://github.com/pyrech/composer-changelogs">
   Composer-Changelogs
  </a>
  - Provides a summary of the updates with links to changelog/releasenote/tag. The output is ready to be pasted into the commit message when updating the composer.lock file.
 </li>
 <li>
  <a href="https://github.com/wikimedia/composer-merge-plugin">
   Composer-Merge-Plugin
  </a>
  - Merges multiple
  <code>
   composer.json
  </code>
  files at Composer runtime.
  <sup>
   &#9733 120, pushed 134 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/beberlei/composer-monorepo-plugin">
   Composer-MonoRepo-Plugin
  </a>
  - The plugin adds support for managing dependencies for multiple packages in a single repository.
 </li>
 <li>
  <a href="https://github.com/netresearch/composer-patches-plugin">
   Composer-Patches-Plugin
  </a>
  - Enables you to provide patches for any package from any package. When the dependency is fetched, the patch is applied on top.
 </li>
 <li>
  <a href="https://github.com/barryvdh/composer-cleanup-plugin">
   Composer-Cleanup-Plugin
  </a>
  - Removes tests & documentation folders from the vendor dir.
 </li>
 <li>
  <a href="https://github.com/dg/composer-cleaner">
   Composer-Cleaner
  </a>
  - The tool removes unnecessary files and directories from the vendor directory.
 </li>
 <li>
  <a href="https://github.com/Letudiant/composer-shared-package-plugin">
   Composer-Shared-Package-Plugin
  </a>
  - Allows you to share your selected packages between your projects by creating symlinks.
 </li>
 <li>
  <a href="https://github.com/dg/composer-symlinker">
   Composer-Symlinker
  </a>
  - Enables you to load some packages from different directories (instead of loading them from /vendor).
 </li>
 <li>
  <a href="https://github.com/hirak/prestissimo">
   Prestissimo
  </a>
  - A parallel downloader using
  <code>
   phpext_curl
  </code>
  .
  <sup>
   &#9733 1698, pushed 129 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jakoch/composer-fastfetch">
   Composer-FastFetch
  </a>
  - Parallel Downloader using external download tools: Aria2.
 </li>
 <li>
  <a href="https://github.com/ngyuki/composer-curl-plugin">
   Composer-Curl-Plugin
  </a>
  - The plugin use phpext_curl for downloading packages.
 </li>
 <li>
  <a href="https://github.com/mnsami/composer-custom-directory-installer">
   Composer-Custom-Directory-Installer
  </a>
  - A composer plugin, to install different types of composer packages in custom directories outside the default composer installation path (which is in the vendor folder).
 </li>
 <li>
  <a href="https://packagist.org/packages/jms/composer-deps-analyzer">
   Composer-Dependency-Analyzer
  </a>
  - Allows you to build a dependency graph for an installed composer project.
 </li>
 <li>
  <a href="https://github.com/Ocramius/PackageVersions">
   PackageVersions
  </a>
  - Provides a very quick and easy access to installed composer dependency versions.
 </li>
 <li>
  <a href="https://github.com/mindplay-dk/composer-locator">
   Composer Locator
  </a>
  - Provides a means of locating the installation path for a given Composer package name.
 </li>
 <li>
  <a href="https://github.com/ThaDafinser/PackageInfo">
   PackageInfo
  </a>
  - Check if a package is installed and retrieve all package informations like version, tag release date, description, ...
 </li>
</ul>
<h2>
 Tools
</h2>
<ul>
 <li>
  <a href="https://semver.mwl.be">
   Composer SemVer Checker
  </a>
  - Enables you identify constraint to version resolution issues, by doing a semantic version check for Packagist hosted packages.
 </li>
 <li>
  <a href="https://github.com/igorw/composer-yaml">
   Composer-Yaml
  </a>
  - This tool converts composer.yml to composer.json.
 </li>
 <li>
  <a href="https://github.com/franzliedke/studio">
   Studio
  </a>
  - A workbench for developing Composer packages. Its an alternative to editing dependencies in the vendor folder or using
  <a href="https://getcomposer.org/doc/05-repositories.md#path">
   PathRepositories
  </a>
  to load a local clone of your dependency into your project.
 </li>
 <li>
  <a href="https://github.com/OctoLinker/browser-extension">
   OctoLinker Browser Extension
  </a>
  - Enables you to navigate Composer/NPM dependencies on Github.
 </li>
</ul>
<h2>
 Scripts
</h2>
<ul>
 <li>
  <a href="https://github.com/neronmoon/scriptsdev">
   ScriptsDev
  </a>
  - Enables you to use a
  <code>
   scripts-dev
  </code>
  section, which triggers scripts only in dev mode.
 </li>
 <li>
  <a href="https://github.com/Incenteev/ParameterHandler">
   ParameterHandler
  </a>
  - Allows you to manage your ignored parameters when running a composer install or update.
 </li>
 <li>
  <a href="https://github.com/jakoch/phantomjs-installer">
   PhantomJS-Installer
  </a>
  - A Composer Package which installs the PhantomJS binary (Linux, Windows, Mac) into /bin of your project.
 </li>
</ul>
<h2>
 Tutorials
</h2>
<ul>
 <li>
  <a href="https://scotch.io/tutorials/a-beginners-guide-to-composer">
   A beginners guide to Composer
  </a>
 </li>
 <li>
  <a href="https://www.dev-metal.com/composer-tutorial/">
   A short & simple Composer tutorial
  </a>
 </li>
 <li>
  <a href="http://code.tutsplus.com/tutorials/easy-package-management-with-composer--net-25530">
   Easy package management with Composer
  </a>
 </li>
 <li>
  <a href="https://www.sitepoint.com/php-dependency-management-with-composer/">
   PHP Dependency Management with Composer
  </a>
 </li>
 <li>
  <a href="https://daylerees.com/composer-primer/">
   Composer Primer
  </a>
 </li>
 <li>
  <a href="http://alanstorm.com/php_composer_magento_tutorial">
   PHP Composer Magento Tutorial by Alan Storm
  </a>
 </li>
</ul>
<h2>
 Slides
</h2>
<ul>
 <li>
  Slides by Nils Aderman
  <ul>
   <li>
    <a href="http://www.naderman.de/slippy/src/?file=2015-02-03-Composer-Update.html">
     Composer Update
    </a>
   </li>
   <li>
    <a href="http://www.naderman.de/slippy/src/?file=2015-02-01-Dependency-Management-with-Composer-PHP-Reinvented.html">
     Dependency Management with Composer PHP Reinvented
    </a>
   </li>
   <li>
    <a href="http://www.naderman.de/slippy/src/?file=2014-04-13-PHP-Reinvented.html">
     PHP Reinvented - How Composer helped shape the new way of writing PHP
    </a>
   </li>
  </ul>
 </li>
 <li>
  Slides by Jordi Boggiano
  <ul>
   <li>
    <a href="http://slides.seld.be/?file=2015-07-25+Composer+Best+Practices.html">
     Composer Best Practices
    </a>
   </li>
   <li>
    <a href="http://slides.seld.be/?file=2015-06-30+Introduction+to+Composer.html">
     Introduction to Composer
    </a>
   </li>
   <li>
    <a href="http://slides.seld.be/?file=2013-10-05+In-Depth+with+Composer.html">
     In Depth with Composer
    </a>
   </li>
   <li>
    <a href="http://slides.seld.be/?file=2013-10-04+Dependency+Management+with+Composer.html">
     Dependency Management with Composer
    </a>
   </li>
  </ul>
 </li>
</ul>
<h2>
 Books
</h2>
<ul>
 <li>
  <a href="https://www.packtpub.com/books/content/creating-and-using-composer-packages">
   Creating and Using Composer Packages
  </a>
 </li>
</ul>
<h2>
 Blogs
</h2>
<ul>
 <li>
  <a href="https://seld.be/">
   Jordi Boggiano (seldaek)
  </a>
 </li>
 <li>
  <a href="http://naderman.de/">
   Nils Adermann (naderman)
  </a>
 </li>
 <li>
  <a href="http://blog.nelm.io/2011/12/composer-part-1-what-why/">
   Composer: Part 1 - What & Why
  </a>
 </li>
 <li>
  <a href="http://blog.nelm.io/2011/12/composer-part-2-impact/">
   Composer: Part 2 - Impact
  </a>
 </li>
 <li>
  <a href="https://igor.io/2013/02/07/composer-stability-flags.html">
   Composer Stability Flags
  </a>
 </li>
 <li>
  <a href="https://igor.io/2013/01/07/composer-versioning.html">
   Composer Versioning
  </a>
 </li>
</ul>
<h2>
 Videos
</h2>
<ul>
 <li>
  <a href="https://www.youtube.com/watch?v=uNlYpSTiAcA">
   Composer Best Practices — Jordi Boggiano @ php[tek] 2015
  </a>
 </li>
 <li>
  <a href="https://knpuniversity.com/screencast/composer">
   Wonderful World of Composer
  </a>
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=Ejr4Xqs9V2I">
   PHP Composer Quickstart
  </a>
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=C2jfLM-Egvg">
   How Composer helped shape the new way of writing PHP - Nils Adermann @ Drupal Camp Frankfurt
  </a>
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=P4Qnp90TG0g">
   Composer Package Management - Nils Adermann @ T3CON12DE
  </a>
 </li>
</ul>
<h2>
 Packagist
</h2>
<ul>
 <li>
  <a href="https://github.com/hirak/packagist-crawler">
   Packagist-Crawler
  </a>
  - Script to mirror Packagist metadata.
 </li>
</ul>
<h3>
 Packagist Mirrors
</h3>
<ul>
 <li>
  Europe
  <ul>
   <li>
    France https://packagist.org/ - 87.98.253.214 (ovh.net).
   </li>
  </ul>
 </li>
 <li>
  Asia
  <ul>
   <li>
    Japan http://packagist.jp/ - 104.28.30.100 (CloudFlare, San Fransico, USA).
   </li>
   <li>
    China http://packagist.cn/ - 123.56.107.40 (Aliyun Computing; Alibaba, Hangzhou, China). (Abandoned)
   </li>
   <li>
    China http://www.phpcomposer.com/
   </li>
  </ul>
 </li>
 <li>
  USA
  <ul>
   <li>
    Give http://packagist.jp/ a try.
   </li>
  </ul>
 </li>
</ul>
<h2>
 Satis
</h2>
<ul>
 <li>
  <a href="https://github.com/wemakecustom/gitlab-composer">
   Gitlab-Composer
  </a>
  - This is a branch/tag indexer for Gitlab repositories.
 </li>
 <li>
  <a href="https://github.com/ludofleury/satisfy">
   Satisfy
  </a>
  - Satis composer repository manager with a Web UI.
 </li>
 <li>
  <a href="https://github.com/realshadow/satis-control-panel">
   Satis Control Panel
  </a>
  - A simple web UI for managing your Satis Repository with optional CI integration.
 </li>
 <li>
  <a href="https://github.com/benschw/satis-go">
   Satis Go
  </a>
  - A web server for managing Satis configuration and hosting the generated Composer repository.
 </li>
</ul>
<h2>
 Proxies
</h2>
<ul>
 <li>
  <a href="https://toranproxy.com/">
   ToranProxy
  </a>
  - ToranProxy acts as a proxy server for Packagist and GitHub.
 </li>
</ul>
<hr/>
<h2>
 License
</h2>
<p>
 <a href="https://creativecommons.org/publicdomain/zero/1.0/">
  <img alt="CC0" src="https://licensebuttons.net/p/zero/1.0/88x31.png"/>
 </a>
</p>
<p>
 To the extent possible under law,
 <a href="https://github.com/jakoch">
  Jens A. Koch
 </a>
 has waived all copyright and related or neighboring rights to this work.
</p>
