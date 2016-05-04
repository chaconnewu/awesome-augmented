<h1>
 GitHub Cheat Sheet
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<p>
 A collection of cool hidden and not so hidden features of Git and GitHub. This cheat sheet was inspired by
 <a href="https://github.com/holman">
  Zach Holman
 </a>
 's
 <a href="http://confreaks.tv/videos/aloharuby2012-git-and-github-secrets">
  Git and GitHub Secrets
 </a>
 talk at Aloha Ruby Conference 2012 (
 <a href="https://speakerdeck.com/holman/git-and-github-secrets">
  slides
 </a>
 ) and his
 <a href="https://vimeo.com/72955426">
  More Git and GitHub Secrets
 </a>
 talk at WDCNZ 2013 (
 <a href="https://speakerdeck.com/holman/more-git-and-github-secrets">
  slides
 </a>
 ).
</p>
<p>
 <em>
  Shortlink:
  <a href="http://git.io/sheet">
   <code>
    http://git.io/sheet
   </code>
  </a>
 </em>
</p>
<p>
 <em>
  Read this in other languages:
  <a href="README.md">
   English
  </a>
  ,
  <a href="README.ko.md">
   한국어
  </a>
  ,
  <a href="README.ja.md">
   日本語
  </a>
  ,
  <a href="README.zh-cn.md">
   简体中文
  </a>
  ,
  <a href="README.zh-tw.md">
   正體中文
  </a>
  .
 </em>
</p>
<h2>
 Table of Contents
</h2>
<ul>
 <li>
  <a href="#github">
   GitHub
  </a>
  <ul>
   <li>
    <a href="#ignore-whitespace">
     Ignore Whitespace
    </a>
   </li>
   <li>
    <a href="#adjust-tab-space">
     Adjust Tab Space
    </a>
   </li>
   <li>
    <a href="#commit-history-by-author">
     Commit History by Author
    </a>
   </li>
   <li>
    <a href="#cloning-a-repository">
     Cloning a Repository
    </a>
   </li>
   <li>
    <a href="#branch">
     Branch
    </a>
   </li>
   <li>
    <a href="#compare-all-branches-to-another-branch">
     Compare all Branches to Another Branch
    </a>
   </li>
   <li>
    <a href="#comparing-branches">
     Comparing Branches
    </a>
   </li>
   <li>
    <a href="#compare-branches-across-forked-repositories">
     Compare Branches across Forked Repositories
    </a>
   </li>
   <li>
    <a href="#gists">
     Gists
    </a>
   </li>
   <li>
    <a href="#gitio">
     Git.io
    </a>
   </li>
   <li>
    <a href="#keyboard-shortcuts">
     Keyboard Shortcuts
    </a>
   </li>
   <li>
    <a href="#line-highlighting-in-repositories">
     Line Highlighting in Repositories
    </a>
   </li>
   <li>
    <a href="#closing-issues-via-commit-messages">
     Closing Issues via Commit Messages
    </a>
   </li>
   <li>
    <a href="#cross-link-issues">
     Cross-Link Issues
    </a>
   </li>
   <li>
    <a href="#locking-conversations">
     Locking Conversations
    </a>
   </li>
   <li>
    <a href="#ci-status-on-pull-requests">
     CI Status on Pull Requests
    </a>
   </li>
   <li>
    <a href="#filters">
     Filters
    </a>
   </li>
   <li>
    <a href="#syntax-highlighting-in-markdown-files">
     Syntax Highlighting in Markdown Files
    </a>
   </li>
   <li>
    <a href="#emojis">
     Emojis
    </a>
   </li>
   <li>
    <a href="#imagesgifs">
     Images/GIFs
    </a>
   </li>
   <li>
    <a href="#embedding-images-in-github-wiki">
     Embedding Images in GitHub Wiki
    </a>
   </li>
   <li>
    <a href="#quick-quoting">
     Quick Quoting
    </a>
   </li>
   <li>
    <a href="#pasting-clipboard-image-to-comments">
     Pasting Clipboard Image to Comments
    </a>
   </li>
   <li>
    <a href="#quick-licensing">
     Quick Licensing
    </a>
   </li>
   <li>
    <a href="#task-lists">
     Task Lists
    </a>
   </li>
   <li>
    <a href="#task-lists-in-markdown-documents">
     Task Lists in Markdown Documents
    </a>
   </li>
   <li>
    <a href="#relative-links">
     Relative Links
    </a>
   </li>
   <li>
    <a href="#metadata-and-plugin-support-for-github-pages">
     Metadata and Plugin Support for GitHub Pages
    </a>
   </li>
   <li>
    <a href="#viewing-yaml-metadata-in-your-documents">
     Viewing YAML Metadata in your Documents
    </a>
   </li>
   <li>
    <a href="#rendering-tabular-data">
     Rendering Tabular Data
    </a>
   </li>
   <li>
    <a href="#rendering-pdf">
     Rendering PDF
    </a>
   </li>
   <li>
    <a href="#revert-a-pull-request">
     Revert a Pull Request
    </a>
   </li>
   <li>
    <a href="#diffs">
     Diffs
    </a>
   </li>
   <li>
    <a href="#rendered-prose-diffs">
     Rendered Prose Diffs
    </a>
   </li>
   <li>
    <a href="#diffable-maps">
     Diffable Maps
    </a>
   </li>
   <li>
    <a href="#expanding-context-in-diffs">
     Expanding Context in Diffs
    </a>
   </li>
   <li>
    <a href="#diff-or-patch-of-pull-request">
     Diff or Patch of Pull Request
    </a>
   </li>
   <li>
    <a href="#rendering-and-diffing-images">
     Rendering and diffing images
    </a>
   </li>
   <li>
    <a href="#hub">
     Hub
    </a>
   </li>
   <li>
    <a href="#contribution-guidelines">
     Contribution Guidelines
    </a>
   </li>
   <li>
    <a href="#contributing-file">
     CONTRIBUTING file
    </a>
   </li>
   <li>
    <a href="#issue_template-file">
     ISSUE_TEMPLATE file
    </a>
   </li>
   <li>
    <a href="#pull_request_template-file">
     PULL
     <em>
      REQUEST
     </em>
     TEMPLATE file
    </a>
   </li>
   <li>
    <a href="#octicons">
     Octicons
    </a>
   </li>
   <li>
    <a href="#github-student-developer-pack">
     GitHub Student Developer Pack
    </a>
   </li>
   <li>
    <a href="#github-resources">
     GitHub Resources
    </a>
   </li>
   <li>
    <a href="#github-talks">
     GitHub Talks
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#git">
   Git
  </a>
  <ul>
   <li>
    <a href="#remove-all-deleted-files-from-the-working-tree">
     Remove All Deleted Files from the Working Tree
    </a>
   </li>
   <li>
    <a href="#previous-branch">
     Previous Branch
    </a>
   </li>
   <li>
    <a href="#stripspace">
     Stripspace
    </a>
   </li>
   <li>
    <a href="#ssh-keys">
     SSH keys
    </a>
   </li>
   <li>
    <a href="#checking-out-pull-requests">
     Checking out Pull Requests
    </a>
   </li>
   <li>
    <a href="#empty-commits">
     Empty Commits
    </a>
   </li>
   <li>
    <a href="#styled-git-status">
     Styled Git Status
    </a>
   </li>
   <li>
    <a href="#styled-git-log">
     Styled Git Log
    </a>
   </li>
   <li>
    <a href="#git-query">
     Git Query
    </a>
   </li>
   <li>
    <a href="#git-grep">
     Git Grep
    </a>
   </li>
   <li>
    <a href="#merged-branches">
     Merged Branches
    </a>
   </li>
   <li>
    <a href="#fixup-and-autosquash">
     Fixup and Autosquash
    </a>
   </li>
   <li>
    <a href="#web-server-for-browsing-local-repositories">
     Web Server for Browsing Local Repositories
    </a>
   </li>
   <li>
    <a href="#git-configurations">
     Git Configurations
    </a>
   </li>
   <li>
    <a href="#aliases">
     Aliases
    </a>
   </li>
   <li>
    <a href="#auto-correct">
     Auto-Correct
    </a>
   </li>
   <li>
    <a href="#color">
     Color
    </a>
   </li>
   <li>
    <a href="#git-resources">
     Git Resources
    </a>
   </li>
   <li>
    <a href="#git-books">
     Git Books
    </a>
   </li>
   <li>
    <a href="#git-videos">
     Git Videos
    </a>
   </li>
   <li>
    <a href="#git-articles">
     Git Articles
    </a>
   </li>
  </ul>
 </li>
</ul>
<h2>
 GitHub
</h2>
<h3>
 Ignore Whitespace
</h3>
<p>
 Adding
 <code>
  ?w=1
 </code>
 to any diff URL will remove any changes only in whitespace, enabling you to see only that code that has changed.
</p>
<p>
 <img alt="Diff without whitespace" src="https://camo.githubusercontent.com/797184940defadec00393e6559b835358a863eeb/68747470733a2f2f6769746875622d696d616765732e73332e616d617a6f6e6177732e636f6d2f626c6f672f323031312f736563726574732f776869746573706163652e706e67"/>
</p>
<p>
 <a href="https://github.com/blog/967-github-secrets">
  <em>
   Read more about GitHub secrets.
  </em>
 </a>
</p>
<h3>
 Adjust Tab Space
</h3>
<p>
 Adding
 <code>
  ?ts=4
 </code>
 to a diff or file URL will display tab characters as 4 spaces wide instead of the default 8. The number after
 <code>
  ts
 </code>
 can be adjusted to suit your preference. This does not work on Gists, or raw file views, but a
 <a href="https://chrome.google.com/webstore/detail/tab-size-on-github/ofjbgncegkdemndciafljngjbdpfmbkn">
  Chrome
 </a>
 or
 <a href="https://addons.opera.com/en/extensions/details/github-tab-size/">
  Opera extension
 </a>
 can automate this.
</p>
<p>
 Here is a Go source file before adding
 <code>
  ?ts=4
 </code>
 :
</p>
<p>
 <img alt="Before, tab space example" src="http://i.imgur.com/GIT1Fr0.png"/>
</p>
<p>
 ...and this is after adding
 <code>
  ?ts=4
 </code>
 :
</p>
<p>
 <img alt="After, tab space example" src="http://i.imgur.com/70FL4H9.png"/>
</p>
<h3>
 Commit History by Author
</h3>
<p>
 To view all commits on a repo by author add
 <code>
  ?author={user}
 </code>
 to the URL.
</p>
<p>
 <code>
  https://github.com/rails/rails/commits/master?author=dhh
 </code>
</p>
<p>
 <img alt="DHH commit history" src="http://i.imgur.com/S7AE29b.png"/>
</p>
<p>
 <a href="https://help.github.com/articles/differences-between-commit-views/">
  <em>
   Read more about the differences between commits views.
  </em>
 </a>
</p>
<h3>
 Cloning a Repository
</h3>
<p>
 When cloning a repository the
 <code>
  .git
 </code>
 can be left off the end.
</p>
<p>
 <code>
  bash
$ git clone https://github.com/tiimgreen/github-cheat-sheet
 </code>
</p>
<p>
 <a href="http://git-scm.com/docs/git-clone">
  <em>
   Read more about the Git
   <code>
    clone
   </code>
   command.
  </em>
 </a>
</p>
<h3>
 Branch
</h3>
<h4>
 Compare all Branches to Another Branch
</h4>
<p>
 If you go to the repo's
 <a href="https://github.com/tiimgreen/github-cheat-sheet/branches">
  Branches
 </a>
 page, next to the Commits button:
</p>
<p>
 <code>
  https://github.com/{user}/{repo}/branches
 </code>
</p>
<p>
 ... you would see a list of all branches which are not merged into the main branch.
</p>
<p>
 From here you can access the compare page or delete a branch with a click of a button.
</p>
<p>
 <img alt="Compare branches not merged into master in rails/rails repo - https://github.com/rails/rails/branches" src="http://i.imgur.com/0FEe30z.png"/>
</p>
<h4>
 Comparing Branches
</h4>
<p>
 To use GitHub to compare branches, change the URL to look like this:
</p>
<p>
 <code>
  https://github.com/{user}/{repo}/compare/{range}
 </code>
</p>
<p>
 Where
 <code>
  {range} = master...4-1-stable
 </code>
</p>
<p>
 For example:
</p>
<p>
 <code>
  https://github.com/rails/rails/compare/master...4-1-stable
 </code>
</p>
<p>
 <img alt="Rails branch compare example" src="http://i.imgur.com/tIRCOsK.png"/>
</p>
<p>
 <code>
  {range}
 </code>
 can be changed to things like:
</p>
<p>
 <code>
  https://github.com/rails/rails/compare/master@{1.day.ago}...master
https://github.com/rails/rails/compare/master@{2014-10-04}...master
 </code>
</p>
<p>
 <em>
  Dates are in the format
  <code>
   YYYY-MM-DD
  </code>
 </em>
</p>
<p>
 <img alt="Another compare example" src="http://i.imgur.com/5dtzESz.png"/>
</p>
<p>
 Branches can also be compared in
 <code>
  diff
 </code>
 and
 <code>
  patch
 </code>
 views:
</p>
<p>
 <code>
  https://github.com/rails/rails/compare/master...4-1-stable.diff
https://github.com/rails/rails/compare/master...4-1-stable.patch
 </code>
</p>
<p>
 <a href="https://help.github.com/articles/comparing-commits-across-time/">
  <em>
   Read more about comparing commits across time.
  </em>
 </a>
</p>
<h4>
 Compare Branches across Forked Repositories
</h4>
<p>
 To use GitHub to compare branches across forked repositories, change the URL to look like this:
</p>
<p>
 <code>
  https://github.com/{user}/{repo}/compare/{foreign-user}:{branch}...{own-branch}
 </code>
</p>
<p>
 For example:
</p>
<p>
 <code>
  https://github.com/rails/rails/compare/byroot:master...master
 </code>
</p>
<p>
 <img alt="Forked branch compare" src="http://i.imgur.com/Q1W6qcB.png"/>
</p>
<h3>
 Gists
</h3>
<p>
 <a href="https://gist.github.com/">
  Gists
 </a>
 are an easy way to work with small bits of code without creating a fully fledged repository.
</p>
<p>
 <img alt="Gist" src="http://i.imgur.com/VkKI1LC.png?1"/>
</p>
<p>
 Add
 <code>
  .pibb
 </code>
 to the end of any Gist URL (
 <a href="https://gist.github.com/tiimgreen/10545817.pibb">
  like this
 </a>
 ) in order to get the
 <em>
  HTML only
 </em>
 version suitable for embedding in any other site.
</p>
<p>
 Gists can be treated as a repository so they can be cloned like any other:
</p>
<p>
 <code>
  bash
$ git clone https://gist.github.com/tiimgreen/10545817
 </code>
</p>
<p>
 <img alt="Gists" src="http://i.imgur.com/BcFzabp.png"/>
</p>
<p>
 This means you also can modify and push updates to Gists:
</p>
<p>
 <code>
  bash
$ git commit
$ git push
Username for 'https://gist.github.com':
Password for 'https://tiimgreen@gist.github.com':
 </code>
</p>
<p>
 However, Gists do not support directories. All files need to be added to the repository root.
 <a href="https://help.github.com/articles/creating-gists/">
  <em>
   Read more about creating Gists.
  </em>
 </a>
</p>
<h3>
 Git.io
</h3>
<p>
 <a href="http://git.io">
  Git.io
 </a>
 is a simple URL shortener for GitHub.
</p>
<p>
 <img alt="Git.io" src="http://i.imgur.com/6JUfbcG.png?1"/>
</p>
<p>
 You can also use it via pure HTTP using Curl:
</p>
<p>
 ```bash
$ curl -i http://git.io -F "url=https://github.com/..."
HTTP/1.1 201 Created
Location: http://git.io/abc123
</p>
<p>
 $ curl -i http://git.io/abc123
HTTP/1.1 302 Found
Location: https://github.com/...
```
</p>
<p>
 <a href="https://github.com/blog/985-git-io-github-url-shortener">
  <em>
   Read more about Git.io.
  </em>
 </a>
</p>
<h3>
 Keyboard Shortcuts
</h3>
<p>
 When on a repository page, keyboard shortcuts allow you to navigate easily.
</p>
<ul>
 <li>
  Pressing
  <code>
   t
  </code>
  will bring up a file explorer.
 </li>
 <li>
  Pressing
  <code>
   w
  </code>
  will bring up the branch selector.
 </li>
 <li>
  Pressing
  <code>
   s
  </code>
  will focus the search field for the current repository. Pressing Backspace to delete the “This repository” pill changes the field to search all of GitHub.
 </li>
 <li>
  Pressing
  <code>
   l
  </code>
  will edit labels on existing Issues.
 </li>
 <li>
  Pressing
  <code>
   y
  </code>
  <strong>
   when looking at a file
  </strong>
  (e.g.
  <code>
   https://github.com/tiimgreen/github-cheat-sheet/blob/master/README.md
  </code>
  ) will change your URL to one which, in effect, freezes the page you are looking at. If this code changes, you will still be able to see what you saw at that current time.
 </li>
</ul>
<p>
 To see all of the shortcuts for the current page press
 <code>
  ?
 </code>
 :
</p>
<p>
 <img alt="Keyboard shortcuts" src="http://i.imgur.com/y5ZfNEm.png"/>
</p>
<p>
 <a href="https://help.github.com/articles/search-syntax/">
  Read more about search syntax you can use.
 </a>
</p>
<h3>
 Line Highlighting in Repositories
</h3>
<p>
 Either adding
 <code>
  #L52
 </code>
 to the end of a code file URL or simply clicking the line number will highlight that line number.
</p>
<p>
 It also works with ranges, e.g.
 <code>
  #L53-L60
 </code>
 , to select ranges, hold
 <code>
  shift
 </code>
 and click two lines:
</p>
<p>
 <code>
  https://github.com/rails/rails/blob/master/activemodel/lib/active_model.rb#L53-L60
 </code>
</p>
<p>
 <img alt="Line Highlighting" src="http://i.imgur.com/8AhjrCz.png"/>
</p>
<h3>
 Closing Issues via Commit Messages
</h3>
<p>
 If a particular commit fixes an issue, any of the keywords
 <code>
  fix/fixes/fixed
 </code>
 ,
 <code>
  close/closes/closed
 </code>
 or
 <code>
  resolve/resolves/resolved
 </code>
 , followed by the issue number, will close the issue once it is committed to the master branch.
</p>
<p>
 <code>
  bash
$ git commit -m "Fix screwup, fixes #12"
 </code>
</p>
<p>
 This closes the issue and references the closing commit.
</p>
<p>
 <img alt="Closing Repo" src="http://i.imgur.com/Uh1gZdx.png"/>
</p>
<p>
 <a href="https://help.github.com/articles/closing-issues-via-commit-messages/">
  <em>
   Read more about closing Issues via commit messages.
  </em>
 </a>
</p>
<h3>
 Cross-Link Issues
</h3>
<p>
 If you want to link to another issue in the same repository, simply type hash
 <code>
  #
 </code>
 then the issue number, and it will be auto-linked.
</p>
<p>
 To link to an issue in another repository,
 <code>
  {user}/{repo}#ISSUE_NUMBER
 </code>
 e.g.
 <code>
  tiimgreen/toc#12
 </code>
 .
</p>
<p>
 <img alt="Cross-Link Issues" src="https://camo.githubusercontent.com/447e39ab8d96b553cadc8d31799100190df230a8/68747470733a2f2f6769746875622d696d616765732e73332e616d617a6f6e6177732e636f6d2f626c6f672f323031312f736563726574732f7265666572656e6365732e706e67"/>
</p>
<h3>
 Locking Conversations
</h3>
<p>
 Pull Requests and Issues can now be locked by owners or collaborators of the repo.
</p>
<p>
 <img alt="Lock conversation" src="https://cloud.githubusercontent.com/assets/2723/3221693/bf54dd44-f00d-11e3-8eb6-bb51e825bc2c.png"/>
</p>
<p>
 This means that users who are not collaborators on the project will no longer be able to comment.
</p>
<p>
 <img alt="Comments locked" src="https://cloud.githubusercontent.com/assets/2723/3221775/d6e513b0-f00e-11e3-9721-2131cb37c906.png"/>
</p>
<p>
 <a href="https://github.com/blog/1847-locking-conversations">
  <em>
   Read more about locking conversations.
  </em>
 </a>
</p>
<h3>
 CI Status on Pull Requests
</h3>
<p>
 If set up correctly, every time you receive a Pull Request,
 <a href="https://travis-ci.org/">
  Travis CI
 </a>
 will build that Pull Request just like it would every time you make a new commit. Read more about how to
 <a href="http://docs.travis-ci.com/user/getting-started/">
  get started with Travis CI
 </a>
 .
</p>
<p>
 <a href="https://github.com/octokit/octokit.rb/pull/452">
  <img alt="Travis CI status" src="https://cloud.githubusercontent.com/assets/1687642/2700187/3a88838c-c410-11e3-9a46-e65e2a0458cd.png"/>
 </a>
</p>
<p>
 <a href="https://github.com/blog/1227-commit-status-api">
  <em>
   Read more about the commit status API.
  </em>
 </a>
</p>
<h3>
 Filters
</h3>
<p>
 Both issues and pull requests allow filtering in the user interface.
</p>
<p>
 For the Rails repo: https://github.com/rails/rails/issues, the following filter is built by selecting the label "activerecord":
</p>
<p>
 <code>
  is:issue label:activerecord
 </code>
</p>
<p>
 But, you can also find all issues that are NOT labeled activerecord:
</p>
<p>
 <code>
  is:issue -label:activerecord
 </code>
</p>
<p>
 Additionally, this also works for pull requests:
</p>
<p>
 <code>
  is:pr -label:activerecord
 </code>
</p>
<p>
 Github has tabs for displaying open or closed issues and pull requests but you
can also see merged pull requests.  Just put the following in the filter:
</p>
<p>
 <code>
  is:merged
 </code>
</p>
<p>
 <a href="https://help.github.com/articles/searching-issues/">
  <em>
   Read more about searching issues.
  </em>
 </a>
</p>
<p>
 Finally, github now allows you to filter by the Status API's status.
</p>
<p>
 Pull requests with only successful statuses:
</p>
<p>
 <code>
  status:success
 </code>
</p>
<p>
 <a href="https://github.com/blog/2014-filter-pull-requests-by-status">
  <em>
   Read more about searching on the Status API.
  </em>
 </a>
</p>
<h3>
 Syntax Highlighting in Markdown Files
</h3>
<p>
 For example, to syntax highlight Ruby code in your Markdown files write:
</p>
<pre><code>```ruby
require 'tabbit'
table = Tabbit.new('Name', 'Email')
table.add_row('Tim Green', 'tiimgreen@gmail.com')
puts table.to_s
```
</code></pre>
<p>
 This will produce:
</p>
<p>
 <code>
  ruby
require 'tabbit'
table = Tabbit.new('Name', 'Email')
table.add_row('Tim Green', 'tiimgreen@gmail.com')
puts table.to_s
 </code>
</p>
<p>
 GitHub uses
 <a href="https://github.com/github/linguist">
  Linguist
 </a>
 to perform language detection and syntax highlighting. You can find out which keywords are valid by perusing the
 <a href="https://github.com/github/linguist/blob/master/lib/linguist/languages.yml">
  languages YAML file
 </a>
 .
</p>
<p>
 <a href="https://help.github.com/articles/github-flavored-markdown/">
  <em>
   Read more about GitHub Flavored Markdown.
  </em>
 </a>
</p>
<h3>
 Emojis
</h3>
<p>
 Emojis can be added to Pull Requests, Issues, commit messages, repository descriptions, etc. using
 <code>
  :name_of_emoji:
 </code>
 .
</p>
<p>
 The full list of supported Emojis on GitHub can be found at
 <a href="http://www.emoji-cheat-sheet.com/">
  emoji-cheat-sheet.com
 </a>
 or
 <a href="https://github.com/scotch-io/All-Github-Emoji-Icons">
  scotch-io/All-Github-Emoji-Icons
 </a>
 .
A handy emoji search engine can be found at
 <a href="http://emoji.muan.co/">
  emoji.muan.co
 </a>
 .
</p>
<p>
 The top 5 used Emojis on GitHub are:
</p>
<ol>
 <li>
  <code>
   :shipit:
  </code>
 </li>
 <li>
  <code>
   :sparkles:
  </code>
 </li>
 <li>
  <code>
   :-1:
  </code>
 </li>
 <li>
  <code>
   :+1:
  </code>
 </li>
 <li>
  <code>
   :clap:
  </code>
 </li>
</ol>
<h3>
 Images/GIFs
</h3>
<p>
 Images and GIFs can be added to comments, READMEs etc.:
</p>
<p>
 <code>
  ![Alt Text](http://www.sheawong.com/wp-content/uploads/2013/08/keephatin.gif)
 </code>
</p>
<p>
 Raw images from the repo can be used by calling them directly.:
</p>
<p>
 <code>
  ![Alt Text](https://github.com/{user}/{repo}/raw/master/path/to/image.gif)
 </code>
</p>
<p>
 <img alt="Peter don't care" src="http://www.sheawong.com/wp-content/uploads/2013/08/keephatin.gif"/>
</p>
<p>
 All images are cached on GitHub, so if your host goes down, the image will remain available.
</p>
<h4>
 Embedding Images in GitHub Wiki
</h4>
<p>
 There are multiple ways of embedding images in Wiki pages. There's the standard Markdown syntax (shown above). But there's also a syntax that allows things like specifying the height or width of the image:
</p>
<p>
 <code>
  markdown
[[ http://www.sheawong.com/wp-content/uploads/2013/08/keephatin.gif | height = 100px ]]
 </code>
</p>
<p>
 Which produces:
</p>
<p>
 <img alt="Just a screenshot" src="http://i.imgur.com/J5bMf7S.png"/>
</p>
<h3>
 Quick Quoting
</h3>
<p>
 When on a comment thread and you want to quote something someone previously said, highlight the text and press
 <code>
  r
 </code>
 , this will copy it into your text box in the block-quote format.
</p>
<p>
 <img alt="Quick Quote" src="https://f.cloud.github.com/assets/296432/124483/b0fa6204-6ef0-11e2-83c3-256c37fa7abc.gif"/>
</p>
<p>
 <a href="https://github.com/blog/1399-quick-quotes">
  <em>
   Read more about quick quoting.
  </em>
 </a>
</p>
<h3>
 Pasting Clipboard Image to Comments
</h3>
<p>
 <em>
  (Works on Chrome browsers only)
 </em>
</p>
<p>
 After taking a screenshot and adding it to the clipboard (mac:
 <code>
  cmd-ctrl-shift-4
 </code>
 ), you can simply paste (
 <code>
  cmd-v / ctrl-v
 </code>
 ) the image into the comment section and it will be auto-uploaded to github.
</p>
<p>
 <img alt="Pasting Clipboard Image to Comments" src="https://cloud.githubusercontent.com/assets/39191/5794265/39c9b65a-9f1b-11e4-9bc7-04e41f59ea5f.png"/>
</p>
<p>
 <a href="https://help.github.com/articles/issue-attachments/">
  <em>
   Read more about issue attachments.
  </em>
 </a>
</p>
<h3>
 Quick Licensing
</h3>
<p>
 When creating a repository, GitHub gives you the option of adding in a pre-made license:
</p>
<p>
 <img alt="License" src="http://i.imgur.com/Chqj4Fg.png"/>
</p>
<p>
 You can also add them to existing repositories by creating a new file through the web interface. When the name
 <code>
  LICENSE
 </code>
 is typed in you will get an option to use a template:
</p>
<p>
 <img alt="License" src="http://i.imgur.com/fTjQict.png"/>
</p>
<p>
 Also works for
 <code>
  .gitignore
 </code>
 .
</p>
<p>
 <a href="https://help.github.com/articles/open-source-licensing/">
  <em>
   Read more about open source licensing.
  </em>
 </a>
</p>
<h3>
 Task Lists
</h3>
<p>
 In Issues and Pull requests check boxes can be added with the following syntax (notice the space):
</p>
<p>
 <code>
  - [ ] Be awesome
- [ ] Prepare dinner
  - [ ] Research recipe
  - [ ] Buy ingredients
  - [ ] Cook recipe
- [ ] Sleep
 </code>
</p>
<p>
 <img alt="Task List" src="http://i.imgur.com/jJBXhsY.png"/>
</p>
<p>
 When they are clicked, they will be updated in the pure Markdown:
</p>
<p>
 <code>
  - [x] Be awesome
- [ ] Prepare dinner
  - [x] Research recipe
  - [x] Buy ingredients
  - [ ] Cook recipe
- [ ] Sleep
 </code>
</p>
<p>
 <a href="https://help.github.com/articles/writing-on-github/#task-lists">
  <em>
   Read more about task lists.
  </em>
 </a>
</p>
<h4>
 Task Lists in Markdown Documents
</h4>
<p>
 In full Markdown documents
 <strong>
  read-only
 </strong>
 checklists can now be added using the following syntax:
</p>
<p>
 <code>
  - [ ] Mercury
- [x] Venus
- [x] Earth
  - [x] Moon
- [x] Mars
  - [ ] Deimos
  - [ ] Phobos
 </code>
</p>
<ul>
 <li>
  [ ] Mercury
 </li>
 <li>
  [x] Venus
 </li>
 <li>
  [x] Earth
  <ul>
   <li>
    [x] Moon
   </li>
  </ul>
 </li>
 <li>
  [x] Mars
  <ul>
   <li>
    [ ] Deimos
   </li>
   <li>
    [ ] Phobos
   </li>
  </ul>
 </li>
</ul>
<p>
 <a href="https://github.com/blog/1825-task-lists-in-all-markdown-documents">
  <em>
   Read more about task lists in markdown documents.
  </em>
 </a>
</p>
<h3>
 Relative Links
</h3>
<p>
 Relative links are recommended in your Markdown files when linking to internal content.
</p>
<p>
 <code>
  markdown
[Link to a header](#awesome-section)
[Link to a file](docs/readme)
 </code>
</p>
<p>
 Absolute links have to be updated whenever the URL changes (e.g. repository renamed, username changed, project forked). Using relative links makes your documentation easily stand on its own.
</p>
<p>
 <a href="https://help.github.com/articles/relative-links-in-readmes/">
  <em>
   Read more about relative links.
  </em>
 </a>
</p>
<h3>
 Metadata and Plugin Support for GitHub Pages
</h3>
<p>
 Within Jekyll pages and posts, repository information is available within the
 <code>
  site.github
 </code>
 namespace, and can be displayed, for example, using
 <code>
  {{ site.github.project_title }}
 </code>
 .
</p>
<p>
 The Jemoji and jekyll-mentions plugins enable
 <a href="#emojis">
  emoji
 </a>
 and
 <a href="https://github.com/blog/821">
  @mentions
 </a>
 in your Jekyll posts and pages to work just like you'd expect when interacting with a repository on GitHub.com.
</p>
<p>
 <a href="https://github.com/blog/1797-repository-metadata-and-plugin-support-for-github-pages">
  <em>
   Read more about repository metadata and plugin support for GitHub Pages.
  </em>
 </a>
</p>
<h3>
 Viewing YAML Metadata in your Documents
</h3>
<p>
 Many blogging websites, like
 <a href="http://jekyllrb.com/">
  Jekyll
 </a>
 with
 <a href="https://pages.github.com">
  GitHub Pages
 </a>
 , depend on some YAML-formatted metadata at the beginning of your post. GitHub will render this metadata as a horizontal table, for easier reading
</p>
<p>
 <img alt="YAML metadata" src="https://camo.githubusercontent.com/47245aa16728e242f74a9a324ce0d24c0b916075/68747470733a2f2f662e636c6f75642e6769746875622e636f6d2f6173736574732f36343035302f313232383236372f65303439643063362d323761302d313165332d396464382d6131636432323539393334342e706e67"/>
</p>
<p>
 <a href="https://github.com/blog/1647-viewing-yaml-metadata-in-your-documents">
  <em>
   Read more about viewing YAML metadata in your documents.
  </em>
 </a>
</p>
<h3>
 Rendering Tabular Data
</h3>
<p>
 GitHub supports rendering tabular data in the form of
 <code>
  .csv
 </code>
 (comma-separated) and
 <code>
  .tsv
 </code>
 (tab-separated) files.
</p>
<p>
 <img alt="Tabular data" src="https://camo.githubusercontent.com/1b6dd0157ffb45d9939abf14233a0cb13b3b4dfe/68747470733a2f2f662e636c6f75642e6769746875622e636f6d2f6173736574732f3238323735392f3937363436322f33323038336463652d303638642d313165332d393262322d3566323863313061353035392e706e67"/>
</p>
<p>
 <a href="https://github.com/blog/1601-see-your-csvs">
  <em>
   Read more about rendering tabular data.
  </em>
 </a>
</p>
<h3>
 Rendering PDF
</h3>
<p>
 GitHub supports rendering PDF:
</p>
<p>
 <img alt="PDF" src="https://cloud.githubusercontent.com/assets/1000669/7492902/f8493160-f42e-11e4-8cea-1cb4f02757e7.png"/>
</p>
<p>
 <a href="https://github.com/blog/1974-pdf-viewing">
  <em>
   Read more about rendering PDF.
  </em>
 </a>
</p>
<h3>
 Revert a Pull Request
</h3>
<p>
 After a pull request is merged, you may find it does not help anything or it was a bad decision to merge the pull request.
</p>
<p>
 You can revert it by clicking the
 <strong>
  Revert
 </strong>
 button on the right side of a commit in the pull request page to create a pull request with reverted changes to this specific pull request.
</p>
<p>
 <img alt="Revert button" src="https://camo.githubusercontent.com/0d3350caf2bb1cba53123ffeafc00ca702b1b164/68747470733a2f2f6769746875622d696d616765732e73332e616d617a6f6e6177732e636f6d2f68656c702f70756c6c5f72657175657374732f7265766572742d70756c6c2d726571756573742d6c696e6b2e706e67"/>
</p>
<p>
 <a href="https://github.com/blog/1857-introducing-the-revert-button">
  <em>
   Read more about reverting pull requests
  </em>
 </a>
</p>
<h3>
 Diffs
</h3>
<h4>
 Rendered Prose Diffs
</h4>
<p>
 Commits and pull requests, including rendered documents supported by GitHub (e.g. Markdown), feature
 <em>
  source
 </em>
 and
 <em>
  rendered
 </em>
 views.
</p>
<p>
 <img alt="Source / Rendered view" src="https://github-images.s3.amazonaws.com/help/repository/rendered_prose_diff.png"/>
</p>
<p>
 Click the "rendered" button to see the changes as they'll appear in the rendered document. Rendered prose view is handy when you're adding, removing, and editing text:
</p>
<p>
 <img alt="Rendered Prose Diffs" src="https://f.cloud.github.com/assets/17715/2003056/3997edb4-862b-11e3-90be-5e9586edecd7.png"/>
</p>
<p>
 <a href="https://github.com/blog/1784-rendered-prose-diffs">
  <em>
   Read more about rendered prose diffs.
  </em>
 </a>
</p>
<h4>
 Diffable Maps
</h4>
<p>
 Any time you view a commit or pull request on GitHub that includes geodata, GitHub will render a visual representation of what was changed.
</p>
<p>
 <a href="https://github.com/benbalter/congressional-districts/commit/2233c76ca5bb059582d796f053775d8859198ec5">
  <img alt="Diffable Maps" src="https://f.cloud.github.com/assets/282759/2090660/63f2e45a-8e97-11e3-9d8b-d4c8078b004e.gif"/>
 </a>
</p>
<p>
 <a href="https://github.com/blog/1772-diffable-more-customizable-maps">
  <em>
   Read more about diffable maps.
  </em>
 </a>
</p>
<h4>
 Expanding Context in Diffs
</h4>
<p>
 Using the
 <em>
  unfold
 </em>
 button in the gutter of a diff, you can reveal additional lines of context with a click. You can keep clicking
 <em>
  unfold
 </em>
 until you've revealed the whole file, and the feature is available anywhere GitHub renders diffs.
</p>
<p>
 <img alt="Expanding Context in Diffs" src="https://f.cloud.github.com/assets/22635/1610539/863c1f64-5584-11e3-82bf-151b406a272f.gif"/>
</p>
<p>
 <a href="https://github.com/blog/1705-expanding-context-in-diffs">
  <em>
   Read more about expanding context in diffs.
  </em>
 </a>
</p>
<h4>
 Diff or Patch of Pull Request
</h4>
<p>
 You can get the diff of a Pull Request by adding a
 <code>
  .diff
 </code>
 or
 <code>
  .patch
 </code>
 extension to the end of the URL. For example:
</p>
<p>
 <code>
  https://github.com/tiimgreen/github-cheat-sheet/pull/15
https://github.com/tiimgreen/github-cheat-sheet/pull/15.diff
https://github.com/tiimgreen/github-cheat-sheet/pull/15.patch
 </code>
</p>
<p>
 The
 <code>
  .diff
 </code>
 extension would give you this in plain text:
</p>
<p>
 ```
diff --git a/README.md b/README.md
index 88fcf69..8614873 100644
--- a/README.md
+++ b/README.md
@@ -28,6 +28,7 @@ All the hidden and not hidden features of Git and GitHub. This cheat sheet was i
 -
 <a href="#merged-branches">
  Merged Branches
 </a>
 -
 <a href="#quick-licensing">
  Quick Licensing
 </a>
 -
 <a href="#todo-lists">
  TODO Lists
 </a>
 +-
 <a href="#relative-links">
  Relative Links
 </a>
 -
 <a href="#gitconfig-recommendations">
  .gitconfig Recommendations
 </a>
 -
 <a href="#aliases">
  Aliases
 </a>
 -
 <a href="#auto-correct">
  Auto-correct
 </a>
 @@ -381,6 +382,19 @@ When they are clicked, they will be updated in the pure Markdown:
 - [ ] Sleep
</p>
<p>
 (...)
```
</p>
<h4>
 Rendering and diffing images
</h4>
<p>
 GitHub can display several common image formats, including PNG, JPG, GIF, and PSD. In addition, there are several ways to compare differences between versions of those image formats.
</p>
<p>
 <a href="https://github.com/blog/1845-psd-viewing-diffing">
  <img alt="Diffable PSD" src="https://cloud.githubusercontent.com/assets/2546/3165594/55f2798a-eb56-11e3-92e7-b79ad791a697.gif"/>
 </a>
</p>
<p>
 <a href="https://help.github.com/articles/rendering-and-diffing-images/">
  <em>
   Read more about rendering and diffing images.
  </em>
 </a>
</p>
<h3>
 Hub
</h3>
<p>
 <a href="https://github.com/github/hub">
  Hub
 </a>
 is a command line Git wrapper that gives you extra features and commands that make working with GitHub easier.
</p>
<p>
 This allows you to do things like:
</p>
<p>
 <code>
  bash
$ hub clone tiimgreen/toc
 </code>
</p>
<p>
 <a href="https://github.com/github/hub#commands">
  <em>
   Check out some more cool commands Hub has to offer.
  </em>
 </a>
</p>
<h3>
 Contribution Guidelines
</h3>
<p>
 GitHub supports adding 3 different files which help users contribute to your project.
These files can either be placed in the root of your repository or a
 <code>
  .github
 </code>
 directory under the root.
</p>
<h4>
 CONTRIBUTING File
</h4>
<p>
 Adding a
 <code>
  CONTRIBUTING
 </code>
 or
 <code>
  CONTRIBUTING.md
 </code>
 file to either the root of your repository or a
 <code>
  .github
 </code>
 directory will add a link to your file when a contributor creates an Issue or opens a Pull Request.
</p>
<p>
 <img alt="Contributing Guidelines" src="https://camo.githubusercontent.com/71995d6b0e620a9ef1ded00a04498241c69dd1bf/68747470733a2f2f6769746875622d696d616765732e73332e616d617a6f6e6177732e636f6d2f736b697463682f6973737565732d32303132303931332d3136323533392e6a7067"/>
</p>
<p>
 <a href="https://github.com/blog/1184-contributing-guidelines">
  <em>
   Read more about contributing guidelines.
  </em>
 </a>
</p>
<h4>
 ISSUE_TEMPLATE file
</h4>
<p>
 You can define a template for all new issues opened in your project. The content of this file will pre-populate the new issue box when users create new issues. Add an
 <code>
  ISSUE_TEMPLATE
 </code>
 or
 <code>
  ISSUE_TEMPLATE.md
 </code>
 file to either the root of your repository or a
 <code>
  .github
 </code>
 directory.
</p>
<p>
 <a href="https://github.com/blog/2111-issue-and-pull-request-templates">
  <em>
   Read more about issue templates.
  </em>
 </a>
</p>
<p>
 <a href="https://www.talater.com/open-source-templates/">
  Issue template file generator
 </a>
</p>
<p>
 <img alt="GitHub Issue template" src="https://cloud.githubusercontent.com/assets/25792/13120859/733479fe-d564-11e5-8a1f-a03f95072f7a.png"/>
</p>
<h4>
 PULL
 <em>
  REQUEST
 </em>
 TEMPLATE file
</h4>
<p>
 You can define a template for all new pull requests opened in your project. The content of this file will pre-populate the text area when users create pull requests. Add a
 <code>
  PULL_REQUEST_TEMPLATE
 </code>
 or
 <code>
  PULL_REQUEST_TEMPLATE.md
 </code>
 file to either the root of your repository or a
 <code>
  .github
 </code>
 directory.
</p>
<p>
 <a href="https://github.com/blog/2111-issue-and-pull-request-templates">
  <em>
   Read more about pull request templates.
  </em>
 </a>
</p>
<p>
 <a href="https://www.talater.com/open-source-templates/">
  Pull request template file generator
 </a>
</p>
<h3>
 Octicons
</h3>
<p>
 GitHubs icons (Octicons) have now been open sourced.
</p>
<p>
 <img alt="Octicons" src="https://og.github.com/octicons/octicons@1200x630.png"/>
</p>
<p>
 <a href="https://octicons.github.com">
  <em>
   Read more about GitHub's Octicons
  </em>
 </a>
</p>
<h3>
 GitHub Student Developer Pack
</h3>
<p>
 If you are a student you will be eligible for the GitHub Student Developer Pack. This gives you free credit, free trials and early access to software that will help you when developing.
</p>
<p>
 <img alt="GitHub Student Developer Pack" src="http://i.imgur.com/9ru3K43.png"/>
</p>
<p>
 <a href="https://education.github.com/pack">
  <em>
   Read more about GitHub's Student Developer Pack
  </em>
 </a>
</p>
<h3>
 GitHub Resources
</h3>
<p>
 | Title | Link |
| ----- | ---- |
| GitHub Explore | https://github.com/explore |
| GitHub Blog | https://github.com/blog |
| GitHub Help | https://help.github.com/ |
| GitHub Training | https://training.github.com/ |
| GitHub Developer | https://developer.github.com/ |
| Github Education (Free Micro Account and other stuff for students) | https://education.github.com/ |
</p>
<h4>
 GitHub Talks
</h4>
<p>
 | Title | Link |
| ----- | ---- |
| How GitHub Uses GitHub to Build GitHub | https://www.youtube.com/watch?v=qyz3jkOBbQY |
| Introduction to Git with Scott Chacon of GitHub | https://www.youtube.com/watch?v=ZDR433b0HJY |
| How GitHub No Longer Works | https://www.youtube.com/watch?v=gXD1ITW7iZI |
| Git and GitHub Secrets | https://www.youtube.com/watch?v=Foz9yvMkvlA |
| More Git and GitHub Secrets | https://www.youtube.com/watch?v=p50xsL-iVgU |
</p>
<h2>
 Git
</h2>
<h3>
 Remove All Deleted Files from the Working Tree
</h3>
<p>
 When you delete a lot of files using
 <code>
  /bin/rm
 </code>
 you can use the following command to remove them from the working tree and from the index, eliminating the need to remove each one individually:
</p>
<p>
 <code>
  bash
$ git rm $(git ls-files -d)
 </code>
</p>
<p>
 For example:
</p>
<p>
 ```bash
$ git status
On branch master
Changes not staged for commit:
    deleted:    a
    deleted:    c
</p>
<p>
 $ git rm $(git ls-files -d)
rm 'a'
rm 'c'
</p>
<p>
 $ git status
On branch master
Changes to be committed:
    deleted:    a
    deleted:    c
```
</p>
<h3>
 Previous Branch
</h3>
<p>
 To move to the previous branch in Git:
</p>
<p>
 ```bash
$ git checkout -
</p>
<h1>
 Switched to branch 'master'
</h1>
<p>
 $ git checkout -
</p>
<h1>
 Switched to branch 'next'
</h1>
<p>
 $ git checkout -
</p>
<h1>
 Switched to branch 'master'
</h1>
<p>
 ```
</p>
<p>
 <a href="http://git-scm.com/book/en/Git-Branching-Basic-Branching-and-Merging">
  <em>
   Read more about Git branching.
  </em>
 </a>
</p>
<h3>
 Stripspace
</h3>
<p>
 Git Stripspace:
</p>
<ul>
 <li>
  Strips trailing whitespace
 </li>
 <li>
  Collapses newlines
 </li>
 <li>
  Adds newline to end of file
 </li>
</ul>
<p>
 A file must be passed when calling the command, e.g.:
 <code>
  bash
$ git stripspace < README.md
 </code>
</p>
<p>
 <a href="http://git-scm.com/docs/git-stripspace">
  <em>
   Read more about the Git
   <code>
    stripspace
   </code>
   command.
  </em>
 </a>
</p>
<h3>
 SSH keys
</h3>
<p>
 You can get a list of public ssh keys in plain text format by visiting:
</p>
<p>
 <code>
  https://github.com/{user}.keys
 </code>
</p>
<p>
 e.g.
 <a href="https://github.com/tiimgreen.keys">
  https://github.com/tiimgreen.keys
 </a>
</p>
<p>
 <a href="https://changelog.com/github-exposes-public-ssh-keys-for-its-users/">
  <em>
   Read more about accessing public ssh keys.
  </em>
 </a>
</p>
<h3>
 Checking out Pull Requests
</h3>
<p>
 Pull Requests are special branches on the GitHub repository which can be retrieved locally in several ways:
</p>
<p>
 Retrieve a specific Pull Request and store it temporarily in
 <code>
  FETCH_HEAD
 </code>
 for quickly
 <code>
  diff
 </code>
 ing or
 <code>
  merge
 </code>
 ing:
</p>
<p>
 <code>
  bash
$ git fetch origin refs/pull/[PR-Number]/head
 </code>
</p>
<p>
 Acquire all Pull Request branches as local remote branches by refspec:
</p>
<p>
 <code>
  bash
$ git fetch origin '+refs/pull/*/head:refs/remotes/origin/pr/*'
 </code>
</p>
<p>
 Or setup the remote to fetch Pull Requests automatically by adding these corresponding lines in your repository's
 <code>
  .git/config
 </code>
 :
</p>
<p>
 <code>
  [remote "origin"]
    fetch = +refs/heads/*:refs/remotes/origin/*
    url = git@github.com:tiimgreen/github-cheat-sheet.git
 </code>
</p>
<p>
 <code>
  [remote "origin"]
    fetch = +refs/heads/*:refs/remotes/origin/*
    url = git@github.com:tiimgreen/github-cheat-sheet.git
    fetch = +refs/pull/*/head:refs/remotes/origin/pr/*
 </code>
</p>
<p>
 For Fork-based Pull Request contributions, it's useful to
 <code>
  checkout
 </code>
 a remote branch representing the Pull Request and create a local branch from it:
</p>
<p>
 <code>
  bash
$ git checkout pr/42 pr-42
 </code>
</p>
<p>
 Or should you work on more repositories, you can globally configure fetching pull requests in the global git config instead.
</p>
<p>
 <code>
  bash
git config --global --add remote.origin.fetch "+refs/pull/*/head:refs/remotes/origin/pr/*"
 </code>
</p>
<p>
 This way, you can use the following short commands in all your repositories:
</p>
<p>
 <code>
  bash
git fetch origin
 </code>
</p>
<p>
 <code>
  bash
git checkout pr/42
 </code>
</p>
<p>
 <a href="https://help.github.com/articles/checking-out-pull-requests-locally/">
  <em>
   Read more about checking out pull requests locally.
  </em>
 </a>
</p>
<h3>
 Empty Commits
</h3>
<p>
 Commits can be pushed with no code changes by adding
 <code>
  --allow-empty
 </code>
 :
</p>
<p>
 <code>
  bash
$ git commit -m "Big-ass commit" --allow-empty
 </code>
</p>
<p>
 Some use-cases for this (that make sense), include:
</p>
<ul>
 <li>
  Annotating the start of a new bulk of work or a new feature.
 </li>
 <li>
  Documenting when you make changes to the project that aren't code related.
 </li>
 <li>
  Communicating with people using your repository.
 </li>
 <li>
  The first commit of a repository:
  <code>
   git commit -m "Initial commit" --allow-empty
  </code>
  .
 </li>
</ul>
<h3>
 Styled Git Status
</h3>
<p>
 Running:
</p>
<p>
 <code>
  bash
$ git status
 </code>
</p>
<p>
 Produces:
</p>
<p>
 <img alt="git status" src="http://i.imgur.com/qjPyvXb.png"/>
</p>
<p>
 By adding
 <code>
  -sb
 </code>
 :
</p>
<p>
 <code>
  bash
$ git status -sb
 </code>
</p>
<p>
 This is produced:
</p>
<p>
 <img alt="git status -sb" src="http://i.imgur.com/K0OY3nm.png"/>
</p>
<p>
 <a href="http://git-scm.com/docs/git-status">
  <em>
   Read more about the Git
   <code>
    status
   </code>
   command.
  </em>
 </a>
</p>
<h3>
 Styled Git Log
</h3>
<p>
 Running:
</p>
<p>
 <code>
  bash
$ git log --all --graph --pretty=format:'%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative
 </code>
</p>
<p>
 Produces:
</p>
<p>
 <img alt="git log --all --graph --pretty=format:'%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative" src="http://i.imgur.com/58eOtkW.png"/>
</p>
<p>
 Credit to
 <a href="http://stackoverflow.com/users/88355/palesz">
  Palesz
 </a>
</p>
<p>
 <em>
  This can be aliased using the instructions found
  <a href="https://github.com/tiimgreen/github-cheat-sheet#aliases">
   here
  </a>
  .
 </em>
</p>
<p>
 <a href="http://git-scm.com/docs/git-log">
  <em>
   Read more about the Git
   <code>
    log
   </code>
   command.
  </em>
 </a>
</p>
<h3>
 Git Query
</h3>
<p>
 A Git query allows you to search all your previous commit messages and find the most recent one matching the query.
</p>
<p>
 <code>
  bash
$ git show :/query
 </code>
</p>
<p>
 Where
 <code>
  query
 </code>
 (case-sensitive) is the term you want to search, this then finds the last one and gives details on the lines that were changed.
</p>
<p>
 <code>
  bash
$ git show :/typo
 </code>
 <img alt="git show :/query" src="http://i.imgur.com/icaGiNt.png"/>
</p>
<p>
 <em>
  Press
  <code>
   q
  </code>
  to quit.
 </em>
</p>
<h3>
 Git Grep
</h3>
<p>
 Git Grep will return a list of lines matching a pattern.
</p>
<p>
 Running:
 <code>
  bash
$ git grep aliases
 </code>
 will show all the files containing the string
 <em>
  aliases
 </em>
 .
</p>
<p>
 <img alt="git grep aliases" src="http://i.imgur.com/DL2zpQ9.png"/>
</p>
<p>
 <em>
  Press
  <code>
   q
  </code>
  to quit.
 </em>
</p>
<p>
 You can also use multiple flags for more advanced search. For example:
</p>
<ul>
 <li>
  <code>
   -e
  </code>
  The next parameter is the pattern (e.g. regex)
 </li>
 <li>
  <code>
   --and
  </code>
  ,
  <code>
   --or
  </code>
  and
  <code>
   --not
  </code>
  Combine multiple patterns.
 </li>
</ul>
<p>
 Use it like this:
 <code>
  bash
 $ git grep -e pattern --and -e anotherpattern
 </code>
</p>
<p>
 <a href="http://git-scm.com/docs/git-grep">
  <em>
   Read more about the Git
   <code>
    grep
   </code>
   command.
  </em>
 </a>
</p>
<h3>
 Merged Branches
</h3>
<p>
 Running:
</p>
<p>
 <code>
  bash
$ git branch --merged
 </code>
</p>
<p>
 Will give you a list of all branches that have been merged into your current branch.
</p>
<p>
 Conversely:
</p>
<p>
 <code>
  bash
$ git branch --no-merged
 </code>
</p>
<p>
 Will give you a list of branches that have not been merged into your current branch.
</p>
<p>
 <a href="http://git-scm.com/docs/git-branch">
  <em>
   Read more about the Git
   <code>
    branch
   </code>
   command.
  </em>
 </a>
</p>
<h3>
 Fixup and Autosquash
</h3>
<p>
 If there is something wrong with a previous commit (can be one or more from HEAD), for example
 <code>
  abcde
 </code>
 , run the following command after you've amended the problem:
 <code>
  bash
$ git commit --fixup=abcde
$ git rebase abcde^ --autosquash -i
 </code>
 <a href="http://git-scm.com/docs/git-commit">
  <em>
   Read more about the Git
   <code>
    commit
   </code>
   command.
  </em>
 </a>
 <a href="http://git-scm.com/docs/git-rebase">
  <em>
   Read more about the Git
   <code>
    rebase
   </code>
   command.
  </em>
 </a>
</p>
<h3>
 Web Server for Browsing Local Repositories
</h3>
<p>
 Use the Git
 <code>
  instaweb
 </code>
 command to instantly browse your working repository in
 <code>
  gitweb
 </code>
 . This command is a simple script to set up
 <code>
  gitweb
 </code>
 and a web server for browsing the local repository.
</p>
<p>
 <code>
  bash
$ git instaweb
 </code>
</p>
<p>
 Opens:
</p>
<p>
 <img alt="Git instaweb" src="http://i.imgur.com/Dxekmqc.png"/>
</p>
<p>
 <a href="http://git-scm.com/docs/git-instaweb">
  <em>
   Read more about the Git
   <code>
    instaweb
   </code>
   command.
  </em>
 </a>
</p>
<h3>
 Git Configurations
</h3>
<p>
 Your
 <code>
  .gitconfig
 </code>
 file contains all your Git configurations.
</p>
<h4>
 Aliases
</h4>
<p>
 Aliases are helpers that let you define your own git calls. For example you could set
 <code>
  git a
 </code>
 to run
 <code>
  git add --all
 </code>
 .
</p>
<p>
 To add an alias, either navigate to
 <code>
  ~/.gitconfig
 </code>
 and fill it out in the following format:
</p>
<p>
 <code>
  [alias]
  co = checkout
  cm = commit
  p = push
  # Show verbose output about tags, branches or remotes
  tags = tag -l
  branches = branch -a
  remotes = remote -v
 </code>
</p>
<p>
 ...or type in the command-line:
</p>
<p>
 <code>
  bash
$ git config --global alias.new_alias git_function
 </code>
</p>
<p>
 For example:
</p>
<p>
 <code>
  bash
$ git config --global alias.cm commit
 </code>
</p>
<p>
 For an alias with multiple functions use quotes:
</p>
<p>
 <code>
  bash
$ git config --global alias.ac 'add -A . && commit'
 </code>
</p>
<p>
 Some useful aliases include:
</p>
<p>
 | Alias | Command | What to Type |
| --- | --- | --- |
|
 <code>
  git cm
 </code>
 |
 <code>
  git commit
 </code>
 |
 <code>
  git config --global alias.cm commit
 </code>
 |
|
 <code>
  git co
 </code>
 |
 <code>
  git checkout
 </code>
 |
 <code>
  git config --global alias.co checkout
 </code>
 |
|
 <code>
  git ac
 </code>
 |
 <code>
  git add . -A
 </code>
 <code>
  git commit
 </code>
 |
 <code>
  git config --global alias.ac '!git add -A && git commit'
 </code>
 |
|
 <code>
  git st
 </code>
 |
 <code>
  git status -sb
 </code>
 |
 <code>
  git config --global alias.st 'status -sb'
 </code>
 |
|
 <code>
  git tags
 </code>
 |
 <code>
  git tag -l
 </code>
 |
 <code>
  git config --global alias.tags 'tag -l'
 </code>
 |
|
 <code>
  git branches
 </code>
 |
 <code>
  git branch -a
 </code>
 |
 <code>
  git config --global alias.branches 'branch -a'
 </code>
 |
|
 <code>
  git cleanup
 </code>
 |
 <code>
  git branch --merged | grep -v '*' | xargs git branch -d
 </code>
 |
 <code>
  git config --global alias.cleanup "!git branch --merged | grep -v '*' | xargs git branch -d"
 </code>
 |
|
 <code>
  git remotes
 </code>
 |
 <code>
  git remote -v
 </code>
 |
 <code>
  git config --global alias.remotes 'remote -v'
 </code>
 |
|
 <code>
  git lg
 </code>
 |
 <code>
  git log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --
 </code>
 |
 <code>
  git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --"
 </code>
 |
</p>
<p>
 <em>
  Some Aliases are taken from
  <a href="https://github.com/mathiasbynens">
   @mathiasbynens
  </a>
  dotfiles: https://github.com/mathiasbynens/dotfiles/blob/master/.gitconfig
 </em>
</p>
<h4>
 Auto-Correct
</h4>
<p>
 If you type
 <code>
  git comit
 </code>
 you will get this:
</p>
<p>
 ```bash
$ git comit -m "Message"
</p>
<h1>
 git: 'comit' is not a git command. See 'git --help'.
</h1>
<h1>
 Did you mean this?
</h1>
<h1>
 commit
</h1>
<p>
 ```
</p>
<p>
 To call
 <code>
  commit
 </code>
 when
 <code>
  comit
 </code>
 is typed, just enable auto-correct:
</p>
<p>
 <code>
  bash
$ git config --global help.autocorrect 1
 </code>
</p>
<p>
 So now you will get this:
</p>
<p>
 ```bash
$ git comit -m "Message"
</p>
<h1>
 WARNING: You called a Git command named 'comit', which does not exist.
</h1>
<h1>
 Continuing under the assumption that you meant 'commit'
</h1>
<h1>
 in 0.1 seconds automatically...
</h1>
<p>
 ```
</p>
<h4>
 Color
</h4>
<p>
 To add more color to your Git output:
</p>
<p>
 <code>
  bash
$ git config --global color.ui 1
 </code>
</p>
<p>
 <a href="http://git-scm.com/docs/git-config">
  <em>
   Read more about the Git
   <code>
    config
   </code>
   command.
  </em>
 </a>
</p>
<h3>
 Git Resources
</h3>
<p>
 | Title | Link |
| ----- | ---- |
| Official Git Site | http://git-scm.com/ |
| Official Git Video Tutorials | http://git-scm.com/videos |
| Code School Try Git | http://try.github.com/ |
| Introductory Reference & Tutorial for Git | http://gitref.org/ |
| Official Git Tutorial | http://git-scm.com/docs/gittutorial |
| Everyday Git | http://git-scm.com/docs/everyday |
| Git Immersion | http://gitimmersion.com/ |
| Ry's Git Tutorial | http://rypress.com/tutorials/git/index |
| Git for Computer Scientists | http://eagain.net/articles/git-for-computer-scientists/ |
| Git Magic | http://www-cs-students.stanford.edu/~blynn/gitmagic/ |
| GitHub Training Kit | https://training.github.com/kit/ |
| Git Visualization Playground | http://onlywei.github.io/explain-git-with-d3/#freeplay |
| Learn Git Branching | http://pcottle.github.io/learnGitBranching/ |
| A collection of useful .gitignore templates | https://github.com/github/gitignore |
</p>
<h4>
 Git Books
</h4>
<p>
 | Title | Link |
| ----- | ---- |
| Pragmatic Version Control Using Git | https://pragprog.com/titles/tsgit/pragmatic-version-control-using-git |
| Pro Git | http://git-scm.com/book |
| Git Internals PluralSight | https://github.com/pluralsight/git-internals-pdf |
| Git in the Trenches | http://cbx33.github.io/gitt/ |
| Version Control with Git | http://www.amazon.com/Version-Control-Git-collaborative-development/dp/1449316387 |
| Pragmatic Guide to Git | https://pragprog.com/titles/pg_git/pragmatic-guide-to-git |
| Git: Version Control for Everyone | https://www.packtpub.com/application-development/git-version-control-everyone |
</p>
<h4>
 Git Videos
</h4>
<p>
 | Title | Link |
| ----- | ---- |
| Linus Torvalds on Git | https://www.youtube.com/watch?v=4XpnKHJAok8 |
| Introduction to Git with Scott Chacon | https://www.youtube.com/watch?v=ZDR433b0HJY |
| Git From the Bits Up | https://www.youtube.com/watch?v=MYP56QJpDr4 |
| Graphs, Hashes, and Compression, Oh My! | https://www.youtube.com/watch?v=ig5E8CcdM9g |
| GitHub Training & Guides | https://www.youtube.com/watch?list=PLg7s6cbtAD15G8lNyoaYDuKZSKyJrgwB-&v=FyfwLX4HAxM |
</p>
<h4>
 Git Articles
</h4>
<p>
 | Title | Link |
| ----- | ---- |
| GitHub Flow  | http://scottchacon.com/2011/08/31/github-flow.html |
</p>
