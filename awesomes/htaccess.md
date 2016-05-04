<h1>
 .htaccess Snippets
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<p>
 A collection of useful .htaccess snippets, all in one place.
</p>
<p>
 <strong>
  Disclaimer
 </strong>
 : While dropping the snippet into an
 <code>
  .htaccess
 </code>
 file is most of the time sufficient, there are cases when certain modifications might be required. Use at your own risk.
</p>
<p>
 <strong>
  IMPORTANT
 </strong>
 : Apache 2.4 introduces a few breaking changes, most notably in access control configuration. For more information, check the
 <a href="https://httpd.apache.org/docs/2.4/upgrading.html">
  upgrading document
 </a>
 as well as
 <a href="https://github.com/phanan/htaccess/issues/2">
  this issue
 </a>
 .
</p>
<h2>
 Credits
</h2>
<p>
 What we are doing here is mostly collecting useful snippets from all over the interwebs (for example, a good chunk is from
 <a href="https://github.com/h5bp/server-configs-apache">
  Apache Server Configs
 </a>
 ) into one place. While we’ve been trying to credit where due, things might be missing. If you believe anything here is your work and credits should be given, let us know, or just send a PR.
</p>
<h2>
 Table of Contents
</h2>
<ul>
 <li>
  <a href="#rewrite-and-redirection">
   Rewrite and Redirection
  </a>
  <ul>
   <li>
    <a href="#force-www">
     Force www
    </a>
   </li>
   <li>
    <a href="#force-www-in-a-generic-way">
     Force www in a Generic Way
    </a>
   </li>
   <li>
    <a href="#force-non-www">
     Force non-www
    </a>
   </li>
   <li>
    <a href="#force-non-www-in-a-generic-way">
     Force non-www in a Generic Way
    </a>
   </li>
   <li>
    <a href="#force-https">
     Force HTTPS
    </a>
   </li>
   <li>
    <a href="#force-https-behind-a-proxy">
     Force HTTPS Behind a Proxy
    </a>
   </li>
   <li>
    <a href="#force-trailing-slash">
     Force Trailing Slash
    </a>
   </li>
   <li>
    <a href="#remove-trailing-slash">
     Remove Trailing Slash
    </a>
   </li>
   <li>
    <a href="#redirect-a-single-page">
     Redirect a Single Page
    </a>
   </li>
   <li>
    <a href="#redirect-using-redirectmatch">
     Redirect Using RedirectMatch
    </a>
   </li>
   <li>
    <a href="#alias-a-single-directory">
     Alias a Single Directory
    </a>
   </li>
   <li>
    <a href="#alias-paths-to-script">
     Alias Paths to Script
    </a>
   </li>
   <li>
    <a href="#redirect-an-entire-site">
     Redirect an Entire Site
    </a>
   </li>
   <li>
    <a href="#alias-clean-urls">
     Alias "Clean" URLs
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#security">
   Security
  </a>
  <ul>
   <li>
    <a href="#deny-all-access">
     Deny All Access
    </a>
   </li>
   <li>
    <a href="#deny-all-access-except-yours">
     Deny All Access Except Yours
    </a>
   </li>
   <li>
    <a href="#allow-all-access-except-spammers">
     Allow All Access Except Spammers'
    </a>
   </li>
   <li>
    <a href="#deny-access-to-hidden-files-and-directories">
     Deny Access to Hidden Files and Directories
    </a>
   </li>
   <li>
    <a href="#deny-access-to-backup-and-source-files">
     Deny Access to Backup and Source Files
    </a>
   </li>
   <li>
    <a href="#disable-directory-browsing">
     Disable Directory Browsing
    </a>
   </li>
   <li>
    <a href="#disable-image-hotlinking">
     Disable Image Hotlinking
    </a>
   </li>
   <li>
    <a href="#disable-image-hotlinking-for-specific-domains">
     Disable Image Hotlinking for Specific Domains
    </a>
   </li>
   <li>
    <a href="#password-protect-a-directory">
     Password Protect a Directory
    </a>
   </li>
   <li>
    <a href="#password-protect-a-file-or-several-files">
     Password Protect a File or Several Files
    </a>
   </li>
   <li>
    <a href="#block-visitors-by-referrer">
     Block Visitors by Referrer
    </a>
   </li>
   <li>
    <a href="#prevent-framing-the-site">
     Prevent Framing the Site
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#performance">
   Performance
  </a>
  <ul>
   <li>
    <a href="#compress-text-files">
     Compress Text Files
    </a>
   </li>
   <li>
    <a href="#set-expires-headers">
     Set Expires Headers
    </a>
   </li>
   <li>
    <a href="#turn-etags-off">
     Turn eTags Off
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#miscellaneous">
   Miscellaneous
  </a>
  <ul>
   <li>
    <a href="#set-php-variables">
     Set PHP Variables
    </a>
   </li>
   <li>
    <a href="#custom-error-pages">
     Custom Error Pages
    </a>
   </li>
   <li>
    <a href="#force-downloading">
     Force Downloading
    </a>
   </li>
   <li>
    <a href="#prevent-downloading">
     Prevent Downloading
    </a>
   </li>
   <li>
    <a href="#allow-cross-domain-fonts">
     Allow Cross-Domain Fonts
    </a>
   </li>
   <li>
    <a href="#auto-utf-8-encode">
     Auto UTF-8 Encode
    </a>
   </li>
   <li>
    <a href="#switch-to-another-php-version">
     Switch to Another PHP Version
    </a>
   </li>
   <li>
    <a href="#disable-internet-explorer-compatibility-view">
     Disable Internet Explorer Compatibility View
    </a>
   </li>
   <li>
    <a href="#serve-webp-images">
     Serve WebP Images
    </a>
   </li>
  </ul>
 </li>
</ul>
<h2>
 Rewrite and Redirection
</h2>
<p>
 Note: It is assumed that you have
 <code>
  mod_rewrite
 </code>
 installed and enabled.
</p>
<h3>
 Force www
</h3>
<p>
 <code>
  apacheconf
RewriteEngine on
RewriteCond %{HTTP_HOST} ^example\.com [NC]
RewriteRule ^(.*)$ http://www.example.com/$1 [L,R=301,NC]
 </code>
</p>
<h3>
 Force www in a Generic Way
</h3>
<p>
 <code>
  apacheconf
RewriteCond %{HTTP_HOST} !^$
RewriteCond %{HTTP_HOST} !^www\. [NC]
RewriteCond %{HTTPS}s ^on(s)|
RewriteRule ^ http%1://www.%{HTTP_HOST}%{REQUEST_URI} [R=301,L]
 </code>
 This works for
 <em>
  any
 </em>
 domain.
 <a href="https://stackoverflow.com/questions/4916222/htaccess-how-to-force-www-in-a-generic-way">
  Source
 </a>
</p>
<h3>
 Force non-www
</h3>
<p>
 It’s
 <a href="http://www.sitepoint.com/domain-www-or-no-www/">
  still
 </a>
 <a href="https://devcenter.heroku.com/articles/apex-domains">
  open
 </a>
 <a href="http://yes-www.org/">
  for
 </a>
 <a href="http://no-www.org/">
  debate
 </a>
 whether www or non-www is the way to go, so if you happen to be a fan of bare domains, here you go:
 <code>
  apacheconf
RewriteEngine on
RewriteCond %{HTTP_HOST} ^www\.example\.com [NC]
RewriteRule ^(.*)$ http://example.com/$1 [L,R=301]
 </code>
</p>
<h3>
 Force non-www in a Generic Way
</h3>
<p>
 <code>
  apacheconf
RewriteEngine on
RewriteCond %{HTTP_HOST} ^www\.
RewriteCond %{HTTPS}s ^on(s)|off
RewriteCond http%1://%{HTTP_HOST} ^(https?://)(www\.)?(.+)$
RewriteRule ^ %1%3%{REQUEST_URI} [R=301,L]
 </code>
</p>
<h3>
 Force HTTPS
</h3>
<p>
 ``` apacheconf
RewriteEngine on
RewriteCond %{HTTPS} !on
RewriteRule (.*) https://%{HTTP
 <em>
  HOST}%{REQUEST
 </em>
 URI}
</p>
<h1>
 Note: It’s also recommended to enable HTTP Strict Transport Security (HSTS)
</h1>
<h1>
 on your HTTPS website to help prevent man-in-the-middle attacks.
</h1>
<h1>
 See https://developer.mozilla.org/en-US/docs/Web/Security/HTTP
 <em>
  strict
 </em>
 transport_security
</h1>
<p>
 <ifmodule mod_headers.c="">
  Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
 </ifmodule>
 ```
</p>
<h3>
 Force HTTPS Behind a Proxy
</h3>
<p>
 Useful if you have a proxy in front of your server performing TLS termination.
 <code>
  apacheconf
RewriteCond %{HTTP:X-Forwarded-Proto} !https
RewriteRule (.*) https://%{HTTP_HOST}%{REQUEST_URI}
 </code>
</p>
<h3>
 Force Trailing Slash
</h3>
<p>
 <code>
  apacheconf
RewriteCond %{REQUEST_URI} /+[^\.]+$
RewriteRule ^(.+[^/])$ %{REQUEST_URI}/ [R=301,L]
 </code>
</p>
<h3>
 Remove Trailing Slash
</h3>
<p>
 This snippet will redirect paths ending in slashes to their non-slash-terminated counterparts (except for actual directories), e.g.
 <code>
  http://www.example.com/blog/
 </code>
 to
 <code>
  http://www.example.com/blog
 </code>
 . This is important for SEO, since it’s
 <a href="http://overit.com/blog/canonical-urls">
  recommended
 </a>
 to have a canonical URL for every page.
 <code>
  apacheconf
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_URI} (.+)/$
RewriteRule ^ %1 [R=301,L]
 </code>
 <a href="https://stackoverflow.com/questions/21417263/htaccess-add-remove-trailing-slash-from-url#27264788">
  Source
 </a>
</p>
<h3>
 Redirect a Single Page
</h3>
<p>
 <code>
  apacheconf
Redirect 301 /oldpage.html http://www.example.com/newpage.html
Redirect 301 /oldpage2.html http://www.example.com/folder/
 </code>
 <a href="http://css-tricks.com/snippets/htaccess/301-redirects/">
  Source
 </a>
</p>
<h3>
 Redirect Using RedirectMatch
</h3>
<p>
 <code>
  apacheconf
RedirectMatch 301 /subdirectory(.*) http://www.newsite.com/newfolder/$1
RedirectMatch 301 ^/(.*).htm$ /$1.html
RedirectMatch 301 ^/200([0-9])/([^01])(.*)$ /$2$3
RedirectMatch 301 ^/category/(.*)$ /$1
RedirectMatch 301 ^/(.*)/htaccesselite-ultimate-htaccess-article.html(.*) /htaccess/htaccess.html
RedirectMatch 301 ^/(.*).html/1/(.*) /$1.html$2
RedirectMatch 301 ^/manual/(.*)$ http://www.php.net/manual/$1
RedirectMatch 301 ^/dreamweaver/(.*)$ /tools/$1
RedirectMatch 301 ^/z/(.*)$ http://static.askapache.com/$1
 </code>
 <a href="http://www.askapache.com/htaccess/301-redirect-with-mod_rewrite-or-redirectmatch.html#301_Redirects_RedirectMatch">
  Source
 </a>
</p>
<h3>
 Alias a Single Directory
</h3>
<p>
 <code>
  apacheconf
RewriteEngine On
RewriteRule ^source-directory/(.*) /target-directory/$1 [R=301,L]
 </code>
</p>
<h3>
 Alias Paths To Script
</h3>
<p>
 <code>
  apacheconf
FallbackResource /index.fcgi
 </code>
 This example has an
 <code>
  index.fcgi
 </code>
 file in some directory, and any requests within that directory that fail to resolve a filename/directory will be sent to the
 <code>
  index.fcgi
 </code>
 script. It’s good if you want
 <code>
  baz.foo/some/cool/path
 </code>
 to be handled by
 <code>
  baz.foo/index.fcgi
 </code>
 (which also supports requests to
 <code>
  baz.foo
 </code>
 ) while maintaining
 <code>
  baz.foo/css/style.css
 </code>
 and the like. Get access to the original path from the PATH_INFO environment variable, as exposed to your scripting environment.
</p>
<p>
 <code>
  apacheconf
RewriteEngine On
RewriteRule ^$ index.fcgi/ [QSA,L]
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ index.fcgi/$1 [QSA,L]
 </code>
 This is a less efficient version of the FallbackResource directive (because using
 <code>
  mod_rewrite
 </code>
 is more complex than just handling the
 <code>
  FallbackResource
 </code>
 directive), but it’s also more flexible.
</p>
<h3>
 Redirect an Entire Site
</h3>
<p>
 <code>
  apacheconf
Redirect 301 / http://newsite.com/
 </code>
 This way does it with links intact. That is
 <code>
  www.oldsite.com/some/crazy/link.html
 </code>
 will become
 <code>
  www.newsite.com/some/crazy/link.html
 </code>
 . This is extremely helpful when you are just “moving” a site to a new domain.
 <a href="http://css-tricks.com/snippets/htaccess/301-redirects/">
  Source
 </a>
</p>
<h3>
 Alias “Clean” URLs
</h3>
<p>
 This snippet lets you use “clean” URLs -- those without a PHP extension, e.g.
 <code>
  example.com/users
 </code>
 instead of
 <code>
  example.com/users.php
 </code>
 .
 <code>
  apacheconf
RewriteEngine On
RewriteCond %{SCRIPT_FILENAME} !-d
RewriteRule ^([^.]+)$ $1.php [NC,L]
 </code>
 <a href="http://www.abeautifulsite.net/access-pages-without-the-php-extension-using-htaccess/">
  Source
 </a>
</p>
<h2>
 Security
</h2>
<h3>
 Deny All Access
</h3>
<p>
 ``` apacheconf
</p>
<h2>
 Apache 2.2
</h2>
<p>
 Deny from all
</p>
<h2>
 Apache 2.4
</h2>
<h1>
 Require all denied
</h1>
<p>
 ```
</p>
<p>
 But wait, this will lock you out from your content as well! Thus introducing...
</p>
<h3>
 Deny All Access Except Yours
</h3>
<p>
 ``` apacheconf
</p>
<h2>
 Apache 2.2
</h2>
<p>
 Order deny,allow
Deny from all
Allow from xxx.xxx.xxx.xxx
</p>
<h2>
 Apache 2.4
</h2>
<h1>
 Require all denied
</h1>
<h1>
 Require ip xxx.xxx.xxx.xxx
</h1>
<p>
 ``
 <code>
 </code>
 xxx.xxx.xxx.xxx
 <code>
  is your IP. If you replace the last three digits with
 </code>
 0/12` for example, this will specify a range of IPs within the same network, thus saving you the trouble to list all allowed IPs separately.
 <a href="http://speckyboy.com/2013/01/08/useful-htaccess-snippets-and-hacks/">
  Source
 </a>
</p>
<p>
 Now of course there's a reversed version:
</p>
<h3>
 Allow All Access Except Spammers'
</h3>
<p>
 ``` apacheconf
</p>
<h2>
 Apache 2.2
</h2>
<p>
 Order deny,allow
Deny from xxx.xxx.xxx.xxx
Deny from xxx.xxx.xxx.xxy
</p>
<h2>
 Apache 2.4
</h2>
<h1>
 Require all granted
</h1>
<h1>
 Require not ip xxx.xxx.xxx.xxx
</h1>
<h1>
 Require not ip xxx.xxx.xxx.xxy
</h1>
<p>
 ```
</p>
<h3>
 Deny Access to Hidden Files and Directories
</h3>
<p>
 Hidden files and directories (those whose names start with a dot
 <code>
  .
 </code>
 ) should most, if not all, of the time be secured. For example:
 <code>
  .htaccess
 </code>
 ,
 <code>
  .htpasswd
 </code>
 ,
 <code>
  .git
 </code>
 ,
 <code>
  .hg
 </code>
 ...
 <code>
  apacheconf
RewriteCond %{SCRIPT_FILENAME} -d [OR]
RewriteCond %{SCRIPT_FILENAME} -f
RewriteRule "(^|/)\." - [F]
 </code>
</p>
<p>
 Alternatively, you can just raise a “Not Found” error, giving the attacker no clue:
 <code>
  apacheconf
RedirectMatch 404 /\..*$
 </code>
</p>
<h3>
 Deny Access to Backup and Source Files
</h3>
<p>
 These files may be left by some text/HTML editors (like Vi/Vim) and pose a great security danger if exposed to public.
``` apacheconf
 <filesmatch "(\.(bak|config|dist|fla|inc|ini|log|psd|sh|sql|swp)|~)$"="">
  ## Apache 2.2
    Order allow,deny
    Deny from all
    Satisfy All
 </filesmatch>
</p>
<pre><code>## Apache 2.4
# Require all denied
</code></pre>
<p>
</p>
<p>
 ```
 <a href="https://github.com/h5bp/server-configs-apache">
  Source
 </a>
</p>
<h3>
 Disable Directory Browsing
</h3>
<p>
 <code>
  apacheconf
Options All -Indexes
 </code>
</p>
<h3>
 Disable Image Hotlinking
</h3>
<p>
 ``` apacheconf
RewriteEngine on
</p>
<h1>
 Remove the following line if you want to block blank referrer too
</h1>
<p>
 RewriteCond %{HTTP_REFERER} !^$
</p>
<p>
 RewriteCond %{HTTP_REFERER} !^https?://(.+.)?example.com [NC]
RewriteRule .(jpe?g|png|gif|bmp)$ - [NC,F,L]
</p>
<h1>
 If you want to display a “blocked” banner in place of the hotlinked image,
</h1>
<h1>
 replace the above rule with:
</h1>
<h1>
 RewriteRule .(jpe?g|png|gif|bmp) http://example.com/blocked.png [R,L]
</h1>
<p>
 ```
</p>
<h3>
 Disable Image Hotlinking for Specific Domains
</h3>
<p>
 Sometimes you want to disable image hotlinking from some bad guys only.
``` apacheconf
RewriteEngine on
RewriteCond %{HTTP
 <em>
  REFERER} ^https?://(.+.)?badsite.com [NC,OR]
RewriteCond %{HTTP
 </em>
 REFERER} ^https?://(.+.)?badsite2.com [NC,OR]
RewriteRule .(jpe?g|png|gif|bmp)$ - [NC,F,L]
</p>
<h1>
 If you want to display a “blocked” banner in place of the hotlinked image,
</h1>
<h1>
 replace the above rule with:
</h1>
<h1>
 RewriteRule .(jpe?g|png|gif|bmp) http://example.com/blocked.png [R,L]
</h1>
<p>
 ```
</p>
<h3>
 Password Protect a Directory
</h3>
<p>
 First you need to create a
 <code>
  .htpasswd
 </code>
 file somewhere in the system:
 <code>
  bash
htpasswd -c /home/fellowship/.htpasswd boromir
 </code>
</p>
<p>
 Then you can use it for authentication:
 <code>
  apacheconf
AuthType Basic
AuthName "One does not simply"
AuthUserFile /home/fellowship/.htpasswd
Require valid-user
 </code>
</p>
<h3>
 Password Protect a File or Several Files
</h3>
<p>
 ``` apacheconf
AuthName "One still does not simply"
AuthType Basic
AuthUserFile /home/fellowship/.htpasswd
</p>
<p>
 <files "one-ring.o"="">
  Require valid-user
 </files>
</p>
<p>
 <filesmatch <="" ^((one|two|three)-rings?\.o)$&gt;="" filesmatch="" require="" valid-user="">
  ```
 </filesmatch>
</p>
<h3>
 Block Visitors by Referrer
</h3>
<p>
 This denies access for all users who are coming from (referred by) a specific domain.
 <a href="http://www.htaccess-guide.com/deny-visitors-by-referrer/">
  Source
 </a>
 ``` apacheconf
RewriteEngine on
</p>
<h1>
 Options +FollowSymlinks
</h1>
<p>
 RewriteCond %{HTTP
 <em>
  REFERER} somedomain.com [NC,OR]
RewriteCond %{HTTP
 </em>
 REFERER} anotherdomain.com
RewriteRule .* - [F]
```
</p>
<h3>
 Prevent Framing the Site
</h3>
<p>
 This prevents the website to be framed (i.e. put into an
 <code>
  iframe
 </code>
 tag), when still allows framing for a specific URI.
 <code>
  apacheconf
SetEnvIf Request_URI "/starry-night" allow_framing=true
Header set X-Frame-Options SAMEORIGIN env=!allow_framing
 </code>
</p>
<h2>
 Performance
</h2>
<h3>
 Compress Text Files
</h3>
<p>
 ``` apacheconf
 <ifmodule mod_deflate.c="">
 </ifmodule>
</p>
<pre><code># Force compression for mangled headers.
# https://developer.yahoo.com/blogs/ydn/pushing-beyond-gzipping-25601.html
<ifmodule mod_setenvif.c="">
    <ifmodule mod_headers.c="">
        SetEnvIfNoCase ^(Accept-EncodXng|X-cept-Encoding|X{15}|~{15}|-{15})$ ^((gzip|deflate)\s*,?\s*)+|[X~-]{4,13}$ HAVE_Accept-Encoding
        RequestHeader append Accept-Encoding "gzip,deflate" env=HAVE_Accept-Encoding
    </ifmodule>
</ifmodule>

# Compress all output labeled with one of the following MIME-types
# (for Apache versions below 2.3.7, you don't need to enable `mod_filter`
#  and can remove the `<ifmodule mod_filter.c="">` and `</ifmodule>` lines
#  as `AddOutputFilterByType` is still in the core directives).
<ifmodule mod_filter.c="">
    AddOutputFilterByType DEFLATE application/atom+xml \
                                  application/javascript \
                                  application/json \
                                  application/rss+xml \
                                  application/vnd.ms-fontobject \
                                  application/x-font-ttf \
                                  application/x-web-app-manifest+json \
                                  application/xhtml+xml \
                                  application/xml \
                                  font/opentype \
                                  image/svg+xml \
                                  image/x-icon \
                                  text/css \
                                  text/html \
                                  text/plain \
                                  text/x-component \
                                  text/xml
</ifmodule>
</code></pre>
<p>
</p>
<p>
 ```
 <a href="https://github.com/h5bp/server-configs-apache">
  Source
 </a>
</p>
<h3>
 Set Expires Headers
</h3>
<p>
 <em>
  Expires headers
 </em>
 tell the browser whether they should request a specific file from the server or just grab it from the cache. It is advisable to set static content's expires headers to something far in the future.
</p>
<p>
 If you don’t control versioning with filename-based cache busting, consider lowering the cache time for resources like CSS and JS to something like 1 week.
 <a href="https://github.com/h5bp/server-configs-apache">
  Source
 </a>
 ``` apacheconf
 <ifmodule mod_expires.c="">
  ExpiresActive on
    ExpiresDefault                                      "access plus 1 month"
 </ifmodule>
</p>
<p>
 # CSS
    ExpiresByType text/css                              "access plus 1 year"
</p>
<p>
 # Data interchange
    ExpiresByType application/json                      "access plus 0 seconds"
    ExpiresByType application/xml                       "access plus 0 seconds"
    ExpiresByType text/xml                              "access plus 0 seconds"
</p>
<p>
 # Favicon (cannot be renamed!)
    ExpiresByType image/x-icon                          "access plus 1 week"
</p>
<p>
 # HTML components (HTCs)
    ExpiresByType text/x-component                      "access plus 1 month"
</p>
<p>
 # HTML
    ExpiresByType text/html                             "access plus 0 seconds"
</p>
<p>
 # JavaScript
    ExpiresByType application/javascript                "access plus 1 year"
</p>
<p>
 # Manifest files
    ExpiresByType application/x-web-app-manifest+json   "access plus 0 seconds"
    ExpiresByType text/cache-manifest                   "access plus 0 seconds"
</p>
<p>
 # Media
    ExpiresByType audio/ogg                             "access plus 1 month"
    ExpiresByType image/gif                             "access plus 1 month"
    ExpiresByType image/jpeg                            "access plus 1 month"
    ExpiresByType image/png                             "access plus 1 month"
    ExpiresByType video/mp4                             "access plus 1 month"
    ExpiresByType video/ogg                             "access plus 1 month"
    ExpiresByType video/webm                            "access plus 1 month"
</p>
<p>
 # Web feeds
    ExpiresByType application/atom+xml                  "access plus 1 hour"
    ExpiresByType application/rss+xml                   "access plus 1 hour"
</p>
<p>
 # Web fonts
    ExpiresByType application/font-woff2                "access plus 1 month"
    ExpiresByType application/font-woff                 "access plus 1 month"
    ExpiresByType application/vnd.ms-fontobject         "access plus 1 month"
    ExpiresByType application/x-font-ttf                "access plus 1 month"
    ExpiresByType font/opentype                         "access plus 1 month"
    ExpiresByType image/svg+xml                         "access plus 1 month"
</p>
<p>
 ```
</p>
<h3>
 Turn eTags Off
</h3>
<p>
 By removing the
 <code>
  ETag
 </code>
 header, you disable caches and browsers from being able to validate files, so they are forced to rely on your
 <code>
  Cache-Control
 </code>
 and
 <code>
  Expires
 </code>
 header.
 <a href="http://www.askapache.com/htaccess/apache-speed-etags.html">
  Source
 </a>
 <code>
  apacheconf
  <ifmodule mod_headers.c="">
   Header unset ETag
  </ifmodule>
  FileETag None
 </code>
</p>
<h2>
 Miscellaneous
</h2>
<h3>
 Set PHP Variables
</h3>
<p>
 ``` apacheconf
php_value
 <key>
  <val>
  </val>
 </key>
</p>
<h1>
 For example:
</h1>
<p>
 php
 <em>
  value upload
 </em>
 max
 <em>
  filesize 50M
php
 </em>
 value max
 <em>
  execution
 </em>
 time 240
```
</p>
<h3>
 Custom Error Pages
</h3>
<p>
 <code>
  apacheconf
ErrorDocument 500 "Houston, we have a problem."
ErrorDocument 401 http://error.example.com/mordor.html
ErrorDocument 404 /errors/halflife3.html
 </code>
</p>
<h3>
 Force Downloading
</h3>
<p>
 Sometimes you want to force the browser to download some content instead of displaying it.
 <code>
  apacheconf
  <files *.md="">
   ForceType application/octet-stream
    Header set Content-Disposition attachment
  </files>
 </code>
</p>
<p>
 Now there is a yang to this yin:
</p>
<h3>
 Prevent Downloading
</h3>
<p>
 Sometimes you want to force the browser to display some content instead of downloading it.
 <code>
  apacheconf
  <filesmatch "\.(tex|log|aux)$"="">
   Header set Content-Type text/plain
  </filesmatch>
 </code>
</p>
<h3>
 Allow Cross-Domain Fonts
</h3>
<p>
 CDN-served webfonts might not work in Firefox or IE due to
 <a href="https://en.wikipedia.org/wiki/Cross-origin_resource_sharing">
  CORS
 </a>
 . This snippet solves the problem.
 <code>
  apacheconf
  <ifmodule mod_headers.c="">
   <filesmatch "\.(eot|otf|ttc|ttf|woff|woff2)$"="">
    Header set Access-Control-Allow-Origin "*"
   </filesmatch>
  </ifmodule>
 </code>
 <a href="https://github.com/h5bp/server-configs-apache/issues/32">
  Source
 </a>
</p>
<h3>
 Auto UTF-8 Encode
</h3>
<p>
 Your text content should always be UTF-8 encoded, no?
``` apacheconf
</p>
<h1>
 Use UTF-8 encoding for anything served text/plain or text/html
</h1>
<p>
 AddDefaultCharset utf-8
</p>
<h1>
 Force UTF-8 for a number of file formats
</h1>
<p>
 AddCharset utf-8 .atom .css .js .json .rss .vtt .xml
```
 <a href="https://github.com/h5bp/server-configs-apache">
  Source
 </a>
</p>
<h3>
 Switch to Another PHP Version
</h3>
<p>
 If you’re on a shared host, chances are there are more than one version of PHP installed, and sometimes you want a specific version for your website. The following snippet should switch the PHP version for you.
</p>
<p>
 ``` apacheconf
AddHandler application/x-httpd-php56 .php
</p>
<h1>
 Alternatively, you can use AddType
</h1>
<p>
 AddType application/x-httpd-php56 .php
```
</p>
<h3>
 Disable Internet Explorer Compatibility View
</h3>
<p>
 Compatibility View in IE may affect how some websites are displayed. The following snippet should force IE to use the Edge Rendering Engine and disable the Compatibility View.
</p>
<p>
 <code>
  apacheconf
  <ifmodule mod_headers.c="">
   BrowserMatch MSIE is-msie
    Header set X-UA-Compatible IE=edge env=is-msie
  </ifmodule>
 </code>
</p>
<h3>
 Serve WebP Images
</h3>
<p>
 If
 <a href="https://developers.google.com/speed/webp/?csw=1">
  WebP images
 </a>
 are supported and an image with a .webp extension and the same name is found at the same place as the jpg/png image that is going to be served, then the WebP image is served instead.
</p>
<p>
 <code>
  apacheconf
RewriteEngine On
RewriteCond %{HTTP_ACCEPT} image/webp
RewriteCond %{DOCUMENT_ROOT}/$1.webp -f
RewriteRule (.+)\.(jpe?g|png)$ $1.webp [T=image/webp,E=accept:1]
 </code>
 <a href="https://github.com/vincentorback/WebP-images-with-htaccess">
  Source
 </a>
</p>
