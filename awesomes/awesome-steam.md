<h1>
 Awesome Steam
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<blockquote>
 <p>
  A curated list of
  <a href="#packages">
   packages
  </a>
  and
  <a href="#resources">
   resources
  </a>
  regarding
  <a href="http://store.steampowered.com/">
   Steam
  </a>
  development.
 </p>
</blockquote>
<p>
 <em>
  Please read the
  <a href="CONTRIBUTING.md">
   contribution guidelines
  </a>
  before contributing.
 </em>
</p>
<p>
 The purpose of this document is to provide a quick overview over existing packages (libraries, modules etc.) and resources available regarding Steam client automation and WebAPI usage. Whenever you need to start a new project, have a look at the list of packages and see if there is anything useful for your use case. If you need technical details or tutorials, check out the resources section.
</p>
<h2>
 Table of Contents
</h2>
<ul>
 <li>
  <p>
   <a href="#packages">
    Packages
   </a>
  </p>
  <ul>
   <li>
    <a href="#c">
     C#
    </a>
   </li>
   <li>
    <a href="#nodejs">
     Node.js
    </a>
   </li>
   <li>
    <a href="#php">
     PHP
    </a>
   </li>
   <li>
    <a href="#go">
     Go
    </a>
   </li>
   <li>
    <a href="#python">
     Python
    </a>
   </li>
   <li>
    <a href="#c-1">
     C++
    </a>
   </li>
   <li>
    <a href="#java">
     Java
    </a>
   </li>
   <li>
    <a href="#objective-c">
     Objective-C
    </a>
   </li>
  </ul>
 </li>
 <li>
  <p>
   <a href="#resources">
    Resources
   </a>
  </p>
  <ul>
   <li>
    <a href="#general-1">
     General
    </a>
   </li>
   <li>
    <a href="#tutorials">
     Tutorials
    </a>
   </li>
   <li>
    <a href="#posts">
     Posts
    </a>
   </li>
   <li>
    <a href="#standalone-tools">
     Standalone Tools
    </a>
   </li>
   <li>
    <a href="#discussion-boards">
     Discussion Boards
    </a>
   </li>
  </ul>
 </li>
</ul>
<h2>
 Packages
</h2>
<blockquote>
 <p>
  💡 Many of these package repositories provide helpful READMEs and wiki pages, which explain the usage and/or provide examples. Do not forget to check them out when using particular package.
 </p>
</blockquote>
<h3>
 C#
</h3>
<ul>
 <li>
  <a href="https://github.com/SteamRE/SteamKit">
   SteamKit2
  </a>
  - .NET library designed to interoperate with Valve's Steam network.
 </li>
 <li>
  <a href="https://github.com/geel9/SteamAuth">
   SteamAuth
  </a>
  - A C# library that provides vital Steam Mobile Authenticator functionality.
 </li>
 <li>
  <a href="https://github.com/Jessecar96/SteamBot">
   SteamBot
  </a>
  - Automated bot software for interacting with steam trade.
 </li>
 <li>
  <a href="https://github.com/waylaidwanderer/SteamTradeOffersBot">
   SteamTradeOffersBot
  </a>
  - SteamBot fork which focuses on trade offers.
 </li>
</ul>
<h3>
 Node.js
</h3>
<h4>
 General
</h4>
<ul>
 <li>
  <a href="https://github.com/seishun/node-steam">
   steam
  </a>
  - Interface directly with Steam servers from Node.js.
 </li>
 <li>
  <a href="https://github.com/DoctorMcKay/node-steam-client">
   steam-client
  </a>
  - API-compatible fork of node-steam's SteamClient.
 </li>
 <li>
  <a href="https://github.com/DoctorMcKay/node-steam-user">
   steam-user
  </a>
  - Feature-rich easy-to-use Steam client.
 </li>
 <li>
  <a href="https://github.com/scholtzm/vapor">
   vapor
  </a>
  - Lightweight Steam client framework.
 </li>
 <li>
  <a href="https://github.com/dragonbanshee/node-steam-parentbot">
   steam-parentbot
  </a>
  - Simple base class for a Steam bot.
 </li>
</ul>
<h4>
 WebAPI
</h4>
<ul>
 <li>
  <a href="https://github.com/DoctorMcKay/node-steam-webapi">
   steam-webapi
  </a>
  - Complete WebAPI wrapper with support for extra HTTP headers sent by Steam.
 </li>
</ul>
<h4>
 Trading
</h4>
<ul>
 <li>
  <a href="https://github.com/seishun/node-steam-trade">
   steam-trade
  </a>
  - Node.js wrapper around Steam live trading.
 </li>
 <li>
  <a href="https://github.com/Alex7Kom/node-steam-tradeoffers">
   steam-tradeoffers
  </a>
  - Steam Trade Offers for Node.js.
 </li>
 <li>
  <a href="https://github.com/DoctorMcKay/node-steam-tradeoffer-manager">
   steam-tradeoffer-manager
  </a>
  - Simple and sane Steam trade offer management.
 </li>
</ul>
<h4>
 Game Interaction
</h4>
<ul>
 <li>
  <a href="https://github.com/DoctorMcKay/node-tf2">
   tf2
  </a>
  - Interact directly with TF2 game coordinator.
 </li>
 <li>
  <a href="https://github.com/joshuaferrara/node-csgo">
   csgo
  </a>
  - Interact directly with CS:GO game coordinator.
 </li>
 <li>
  <a href="https://github.com/RJacksonm1/node-dota2">
   dota2
  </a>
  - Interact directly with Dota 2 game coordinator.
 </li>
</ul>
<h4>
 Community & Store Automation
</h4>
<ul>
 <li>
  <a href="https://github.com/DoctorMcKay/node-steamcommunity">
   steamcommunity
  </a>
  - Interact with steamcommunity.com. Also allows to confirm trade offers.
 </li>
 <li>
  <a href="https://github.com/DoctorMcKay/node-steamstore">
   steamstore
  </a>
  - Interact with store.steampowered.com.
 </li>
 <li>
  <a href="https://github.com/Alex7Kom/node-steam-weblogon">
   steam-weblogon
  </a>
  - Retrieve SteamCommunity cookies if you are running Steam network client.
 </li>
 <li>
  <a href="https://github.com/Alex7Kom/node-steam-web-api-key">
   steam-web-api-key
  </a>
  - Automatically registers and retrieves Steam API key.
 </li>
 <li>
  <a href="https://github.com/Alex7Kom/node-steam-parental">
   steam-parental
  </a>
  - Disable parental lock.
 </li>
</ul>
<h4>
 Authentication
</h4>
<ul>
 <li>
  <a href="https://github.com/cpancake/steam-login">
   steam-login
  </a>
  - Simple Connect / Express Steam authentication library.
 </li>
 <li>
  <a href="https://github.com/liamcurry/passport-steam">
   passport-steam
  </a>
  - Steam (OpenID) authentication strategy for Passport and Node.js.
 </li>
 <li>
  <a href="https://github.com/scholtzm/meteor-accounts-steam">
   meteor-accounts-steam
  </a>
  - Steam OpenID integration for Meteor Accounts.
 </li>
</ul>
<h4>
 Misc
</h4>
<ul>
 <li>
  <a href="https://github.com/seishun/node-steam-resources">
   steam-resources
  </a>
  - Steam's enums, protobufs and structs.
 </li>
 <li>
  <a href="https://github.com/seishun/node-steam-crypto">
   steam-crypto
  </a>
  - Node.js implementation of Steam crypto.
 </li>
 <li>
  <a href="https://github.com/scholtzm/node-steam-groups">
   steam-groups
  </a>
  - Custom node-steam handler which provides group functions.
 </li>
 <li>
  <a href="https://github.com/DoctorMcKay/node-steamid">
   steamid
  </a>
  - SteamID usage and conversion made easy.
 </li>
 <li>
  <a href="https://github.com/DoctorMcKay/node-steam-totp">
   steam-totp
  </a>
  - Easily generate 2FA codes used by Steam.
 </li>
 <li>
  <a href="https://github.com/Steam-Chat-Bot/node-steam-chat-bot">
   steam-chat-bot
  </a>
  - Simplified interface for a steam chat bot.
 </li>
 <li>
  <a href="https://github.com/RJacksonm1/node-vdf">
   vdf
  </a>
  - vdf to object and vice versa.
 </li>
 <li>
  <a href="https://github.com/scholtzm/node-steamrep">
   steamrep
  </a>
  - Check user's SteamRep reputation.
 </li>
 <li>
  <a href="https://github.com/scholtzm/node-reptf">
   reptf
  </a>
  - Check user's rep.tf reputation.
 </li>
</ul>
<h3>
 PHP
</h3>
<ul>
 <li>
  <a href="https://github.com/waylaidwanderer/PHP-SteamCommunity">
   SteamCommunity
  </a>
  - A PHP library for interacting with the Steam Community website.
 </li>
 <li>
  <a href="https://github.com/SmItH197/SteamAuthentication">
   SteamAuthentication
  </a>
  - Steam OpenID authentication with PHP.
 </li>
 <li>
  <a href="https://github.com/BlackCetha/SteamAuthOOP">
   SteamAuthOOP
  </a>
  - An object-oriented alternative to SteamAuthentication.
 </li>
 <li>
  <a href="https://github.com/DaMitchell/steam-api-php">
   steam-api-php
  </a>
  - A PHP wrapper for the Steam API.
 </li>
</ul>
<h3>
 Go
</h3>
<ul>
 <li>
  <a href="https://github.com/Philipp15b/go-steam">
   steam
  </a>
  - Steam's protocol in Go.
 </li>
 <li>
  <a href="https://github.com/YellowOrWhite/go-steam-mobileauth">
   steam-mobileauth
  </a>
  - Port of SteamAuth in Go.
 </li>
</ul>
<h3>
 Python
</h3>
<ul>
 <li>
  <a href="https://github.com/ValvePython/steam">
   steam
  </a>
  - Module for various interactions with Steam.
 </li>
 <li>
  <a href="https://bitbucket.org/AzuiSleet/pysteamkit">
   PySteamKit
  </a>
  - Python port of SteamKit.
 </li>
 <li>
  <a href="https://github.com/Lagg/steamodd">
   steamodd
  </a>
  - Steam tools library.
 </li>
 <li>
  <a href="https://github.com/bukson/steampy">
   steampy
  </a>
  - Fully automated Steam trade offers library with SteamGuard support.
 </li>
</ul>
<h3>
 C++
</h3>
<ul>
 <li>
  <a href="https://github.com/seishun/SteamPP">
   SteamPP
  </a>
  - C++ library to interoperate with Steam servers.
 </li>
</ul>
<h3>
 Java
</h3>
<ul>
 <li>
  <a href="https://github.com/Top-Cat/SteamKit-Java">
   SteamKit-Java
  </a>
  - Java port of SteamKit.
 </li>
</ul>
<h3>
 Objective-C
</h3>
<ul>
 <li>
  <a href="https://github.com/michaelchum/SteamAuth">
   SteamAuth
  </a>
  - An iOS wrapper around Steam's OpenID login.
 </li>
</ul>
<h2>
 Resources
</h2>
<h3>
 General
</h3>
<ul>
 <li>
  <a href="https://developer.valvesoftware.com/wiki/Steam_Web_API">
   Steam WebAPI @ ValveSoftware
  </a>
 </li>
 <li>
  <a href="https://wiki.teamfortress.com/wiki/WebAPI">
   Steam WebAPI @ TF2 Wiki
  </a>
 </li>
 <li>
  <a href="https://lab.xpaw.me/steam_api_documentation.html">
   Steam WebAPI Documentation by xpaw
  </a>
 </li>
 <li>
  <a href="http://steamcommunity.com/dev">
   Steam as OpenID Provider
  </a>
 </li>
 <li>
  <a href="http://steamcommunity.com/dev/apikey">
   Steam API Key Registration
  </a>
 </li>
 <li>
  <a href="https://steamerrors.com/">
   Steam Error Codes
  </a>
  - List of
  <code>
   EResult
  </code>
  codes with possible explanations.
 </li>
</ul>
<h3>
 Tutorials
</h3>
<ul>
 <li>
  <a href="https://firepowered.org/developer/create-a-steam-trade-bot-with-nodejs-iojs-updated-for-node-steam-v1-0/">
   Creating a Steam Trade Bot with Node.js
  </a>
 </li>
 <li>
  <a href="https://github.com/charredgrass/nodejs-bot-guide">
   Charred's node.js Guide to Steam Bots
  </a>
 </li>
 <li>
  <a href="http://forums.backpack.tf/index.php?/topic/45995-guide-how-to-get-your-shared-secret-from-ios-device-steam-mobile/">
   Retrieving 2FA Keys from iOS Device
  </a>
 </li>
 <li>
  <a href="http://forums.backpack.tf/index.php?/topic/20204-backpacktf-automatic-help-thread/page-65#entry491155">
   Retrieving 2FA Keys from Android Device
  </a>
 </li>
</ul>
<h3>
 Posts
</h3>
<ul>
 <li>
  <a href="https://dev.doctormckay.com/topic/332-identifying-steam-items/">
   Item IDs Explained
  </a>
 </li>
 <li>
  <a href="https://www.reddit.com/r/SteamBot/comments/3udhkd/everything_related_to_escrow/">
   Everything Related to Escrow
  </a>
 </li>
 <li>
  <a href="https://www.reddit.com/r/SteamBot/comments/3cv6k7/problem_downloading_an_avatar_using/">
   Understanding Avatar Hash
  </a>
 </li>
</ul>
<h3>
 Standalone Tools
</h3>
<ul>
 <li>
  <a href="https://github.com/SteamRE/SteamKit/tree/master/Resources/NetHook2">
   NetHook2
  </a>
  - Intercept Steam client's network messages.
 </li>
 <li>
  <a href="https://github.com/SteamRE/SteamKit/tree/master/Resources/NetHookAnalyzer2">
   NetHook2 Analyzer
  </a>
  - Inspect messages dumped by NetHook2.
 </li>
 <li>
  <a href="http://scholtzm.github.io/steam-auth-web-util/">
   steam-auth-web-util
  </a>
  - Generate 2FA codes directly in your web browser.
 </li>
 <li>
  <a href="https://github.com/Jessecar96/SteamDesktopAuthenticator">
   SteamDesktopAuthenticator
  </a>
  - Desktop implementation of Steam's mobile authenticator app.
 </li>
</ul>
<h3>
 Discussion Boards
</h3>
<ul>
 <li>
  <a href="https://www.reddit.com/r/SteamBot">
   /r/SteamBot
  </a>
 </li>
 <li>
  <a href="https://discord.gg/0i5X3oDHJbDUsiGC">
   /r/SteamBot Discord
  </a>
 </li>
 <li>
  <a href="https://www.reddit.com/r/nodesteam">
   /r/nodesteam
  </a>
 </li>
 <li>
  <a href="https://dev.doctormckay.com/">
   DoctorMcKay's Dev Forum
  </a>
 </li>
 <li>
  <a href="https://github.com/steam-forward/node-steam-forum">
   node-steam-forum
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
 To the extent possible under law, the author and contributors of this text have waived all copyright and related or neighboring rights to this work.
</p>
