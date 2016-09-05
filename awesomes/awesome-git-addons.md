<h1>
 Awesome git addons
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<p>
 A curated list of addons that extends git cli.
</p>
<p>
 <code>
  $ git bla
Something awesome happens!
 </code>
</p>
<blockquote>
 <p>
  <em>
   “You don’t have to know everything. You simply need to know where to find it when necessary.” (John Brunner)
  </em>
 </p>
</blockquote>
<p>
 Inspired by the
 <a href="https://github.com/sindresorhus/awesome">
  awesome
 </a>
 list thing.
</p>
<p>
 <strong>
  Note
 </strong>
 : Some of the commands may not work out of the box. You might need to run a post install script to add aliases or add them manually.
</p>
<h2>
 Table of Contents
</h2>
<ul>
 <li>
  <a href="#git-extras">
   Git Extras
  </a>
 </li>
 <li>
  <a href="#gitflow-avh-edition">
   Git Flow
  </a>
 </li>
 <li>
  <a href="#git-up">
   Git Up
  </a>
 </li>
 <li>
  <a href="#hub">
   Hub
  </a>
 </li>
 <li>
  <a href="#git-deploy">
   Git Deploy
  </a>
 </li>
 <li>
  <a href="#git-cal">
   Git Cal
  </a>
 </li>
 <li>
  <a href="#git-hooks">
   Git Hooks
  </a>
 </li>
 <li>
  <a href="#git-imerge">
   Git Imerge
  </a>
 </li>
 <li>
  <a href="#git-lfs">
   Git Large File Storage
  </a>
 </li>
 <li>
  <a href="#git-now">
   Git Now
  </a>
 </li>
 <li>
  <a href="#git-plus">
   Git Plus
  </a>
 </li>
 <li>
  <a href="#git-test">
   Git Test
  </a>
 </li>
 <li>
  <a href="#legit">
   Legit
  </a>
 </li>
 <li>
  <a href="#git-when-merged">
   Git When Merged
  </a>
 </li>
 <li>
  <a href="#git-playback">
   Git Playback
  </a>
 </li>
 <li>
  <a href="#git-branch-status">
   Git Branch Status
  </a>
 </li>
 <li>
  <a href="#git-open">
   Git Open
  </a>
 </li>
 <li>
  <a href="#git-my">
   Git My
  </a>
 </li>
 <li>
  <a href="#git-ink">
   Git Ink
  </a>
 </li>
 <li>
  <a href="#recursive-blame">
   Recursive Blame
  </a>
 </li>
 <li>
  <a href="#git-fire">
   Git Fire
  </a>
 </li>
 <li>
  <a href="#git-town">
   Git Town
  </a>
 </li>
 <li>
  <a href="#git-blame-someone-else">
   Git blame-someone-else
  </a>
 </li>
 <li>
  <a href="#diff-so-fancy">
   Diff So Fancy
  </a>
 </li>
 <li>
  <a href="#git-stats">
   Git Stats
  </a>
 </li>
 <li>
  <a href="#git-secret">
   Git Secret
  </a>
 </li>
 <li>
  <a href="#apply-pr">
   apply-pr
  </a>
 </li>
 <li>
  <a href="#git-fixup">
   git-fixup
  </a>
 </li>
 <li>
  <a href="#git-recent">
   git-recent
  </a>
 </li>
 <li>
  <a href="#git-fiddle">
   git-fiddle
  </a>
 </li>
</ul>
<h2>
 <a href="https://github.com/tj/git-extras">
  git-extras
 </a>
</h2>
<h3>
 squash
</h3>
<p>
 <code>
  $ git squash fixed-cursor-styling "Fixed cursor styling"
$ git squash 95b7c52
$ git squash HEAD~3
 </code>
</p>
<h3>
 summary
</h3>
<p>
 ```
$ git summary
</p>
<p>
 project  : git
 repo age : 10 years
 active   : 11868 days
 commits  : 40530
 files    : 2825
 authors  :
 15401  Junio C Hamano                  38.0%
  1844  Jeff King                       4.5%
```
</p>
<h3>
 line-summary
</h3>
<p>
 ```
$ git line-summary
</p>
<p>
 project  : gulp
 lines    : 3900
 authors  :
 1040 Contra                    26.7%
  828 Sindre Sorhus             21.2%
```
</p>
<h3>
 effort
</h3>
<p>
 ```
$ git effort
</p>
<p>
 file                                          commits    active days
</p>
<p>
 .gitattributes............................... 3          3
  .gitignore................................... 265        226
  .mailmap..................................... 47         40
```
</p>
<h3>
 authors
</h3>
<p>
 <code>
  $ git authors
Contra <contra@maricopa.edu>
Eric Schoffstall <contra@wearefractal.com>
Sindre Sorhus <sindresorhus@gmail.com>
 </code>
</p>
<h3>
 changelog
</h3>
<p>
 ```
$ git changelog
</p>
<h2>
 3.9.0
</h2>
<ul>
 <li>
  add babel support
 </li>
 <li>
  add transpiler fallback support
 </li>
 <li>
  add support for some renamed transpilers (livescript, etc)
 </li>
 <li>
  add JSCS
 </li>
 <li>
  update dependecies (liftoff, interpret)
 </li>
 <li>
  documentation tweaks
 </li>
</ul>
<h2>
 3.8.11
</h2>
<ul>
 <li>
  fix node 0.12/iojs problems
 </li>
 <li>
  add node 0.12 and iojs to travis
 </li>
 <li>
  update dependencies (liftoff, v8flags)
 </li>
 <li>
  documentation tweaks
```
 </li>
</ul>
<h3>
 commits-since
</h3>
<p>
 <code>
  $ git commits-since yesterday
... changes since yesterday
TJ Holowaychuk - Fixed readme
 </code>
</p>
<h3>
 count
</h3>
<p>
 <code>
  $ git count
total 855
 </code>
</p>
<h3>
 create-branch
</h3>
<p>
 <code>
  $ git create-branch development
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/tj/git-extras.git
 * [new branch]      HEAD -> development
Branch development set up to track remote branch development from origin.
Switched to a new branch 'development'
 </code>
</p>
<h3>
 delete-branch
</h3>
<p>
 <code>
  $ git delete-branch integration
Deleted branch integration (was bfb8522).
Deleted remote-tracking branch remote/integration (was bfb8522).
To git@github.com:remote/gulp.git
 - [deleted]         integration
 </code>
</p>
<h3>
 delete-submodule
</h3>
<p>
 <code>
  $ git delete-submodule lib/foo
 </code>
</p>
<h3>
 delete-tag
</h3>
<p>
 <code>
  $ git delete-tag v0.1.1
Deleted tag 'v0.1.1' (was 9fde751)
To https://github.com/tj/git-extras.git
 - [deleted]         v0.1.1
 </code>
</p>
<h3>
 delete-merged-branches
</h3>
<p>
 <code>
  $ git delete-merged-branches
Deleted feature/themes (was c029ab3).
Deleted feature/live_preview (was a81b002).
Deleted feature/dashboard (was 923befa).
 </code>
</p>
<h3>
 fresh-branch
</h3>
<p>
 <code>
  $ git fresh-branch docs
Removing .DS_Store
Removing .editorconfig
Removing .gitignore
 </code>
</p>
<h3>
 guilt
</h3>
<p>
 <code>
  $ git guilt `git log --until="3 weeks ago" --format="%H" -n 1` HEAD
Paul Schreiber                +++++++++++++++++++++++++++++++++++++++++++++(349)
spacewander                   +++++++++++++++++++++++++++++++++++++++++++++(113)
Mark Eissler                  ++++++++++++++++++++++++++
 </code>
</p>
<h3>
 merge-into
</h3>
<p>
 <code>
  $ git merge-into master
Switched to branch 'master'
Your branch is up-to-date with 'origin/master'.
Updating 9fde751..e62edfa
Fast-forward
 234 | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 234
Switched to branch 'development'
 </code>
</p>
<h3>
 graft
</h3>
<p>
 <code>
  $ git graft development
Your branch is up-to-date with 'origin/master'.
Merge made by the 'recursive' strategy.
 package.json | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
Deleted branch development (was 64b3563).
 </code>
</p>
<h3>
 alias
</h3>
<p>
 <code>
  $ git alias last "cat-file commit HEAD"
$ git alias
last = cat-file commit HEAD
 </code>
</p>
<h3>
 ignore
</h3>
<p>
 <code>
  $ git ignore build "*.o" "*.log"
... added 'build'
... added '*.o'
... added '*.log'
 </code>
</p>
<h3>
 info
</h3>
<p>
 ```
$ git info
</p>
<pre><code>## Remote URLs:

origin              git@github.com:sampleAuthor/git-extras.git (fetch)
origin              git@github.com:sampleAuthor/git-extras.git (push)

## Remote Branches:

origin/HEAD -> origin/master
origin/myBranch

## Local Branches:

myBranch
* master

## Most Recent Commit:

commit e3952df2c172c6f3eb533d8d0b1a6c77250769a7
Author: Sample Author <sampleAuthor@gmail.com>

Added git-info command.

Type 'git log' for more commits, or 'git show <commit id>' for full commit details.

## Configuration (.git/config):

color.diff=auto
color.status=auto
</code></pre>
<p>
 ```
</p>
<h3>
 fork
</h3>
<p>
 <code>
  $ git fork LearnBoost/expect.js
 </code>
</p>
<h3>
 release
</h3>
<p>
 <code>
  $ git release 0.1.0
... releasing 0.1.0
On branch development
Your branch is up-to-date with 'origin/development'.
nothing to commit, working directory clean
Total 0 (delta 0), reused 0 (delta 0)
To https://github.com/tj/git-extras.git
   9fde751..e62edfa  master -> master
Counting objects: 1, done.
Writing objects: 100% (1/1), 166 bytes | 0 bytes/s, done.
Total 1 (delta 0), reused 0 (delta 0)
To https://github.com/tj/git-extras.git
 * [new tag]         0.1.0 -> 0.1.0
... complete
 </code>
</p>
<h3>
 contrib
</h3>
<p>
 <code>
  $ git contrib visionmedia
visionmedia (18):
  Export STATUS_CODES
  Replaced several Array.prototype.slice.call() calls with Array.prototype.unshift.call()
  Moved help msg to node-repl
 </code>
</p>
<h3>
 repl
</h3>
<p>
 ```
$ git repl
</p>
<p>
 git> ls-files
History.md
Makefile
```
</p>
<h3>
 undo
</h3>
<p>
 <code>
  $ git undo
Unstaged changes after reset:
M   package.json
M   readme.md
 </code>
</p>
<h3>
 gh-pages
</h3>
<p>
 <code>
  $ git gh-pages
 </code>
</p>
<h3>
 scp
</h3>
<p>
 <code>
  $ git scp staging HEAD
 </code>
</p>
<h3>
 setup
</h3>
<p>
 <code>
  $ git setup
Initialized empty Git repository in /GitHub/test/gulp/.git/
[master (root-commit) 9469797] Initial commit
 69 files changed, 3900 insertions(+)
 create mode 100644 .editorconfig
 create mode 100644 .gitignore
 create mode 100644 .jscsrc
 </code>
</p>
<h3>
 touch
</h3>
<p>
 <code>
  $ git touch index.js
 </code>
</p>
<h3>
 obliterate
</h3>
<p>
 <code>
  $ git obliterate secrets.json
Rewrite 2357a4334051a6d1733037406ab7538255030d0b (1/981)rm 'secrets.json'
Rewrite b5f62b2746c23150917d346bd0c50c467f01eb03 (2/981)rm 'secrets.json'
Rewrite 3cd94f3395c2701848f6ff626a0a4f883d8a8433 (3/981)rm 'secrets.json'
 </code>
</p>
<h3>
 feature|refactor|bug|chore
</h3>
<p>
 <code>
  $ git feature dependencies
$ git feature finish dependencies
Already up-to-date.
Deleted branch feature/dependencies (was f0fc4c7).
Deleted remote-tracking branch origin/feature/dependencies (was f0fc4c7).
To git@github.com:stevemao/gulp.git
 - [deleted]         feature/dependencies
 </code>
</p>
<h3>
 local-commits
</h3>
<p>
 ```
$ git local-commits
commit 5f00a3c1bb71876ebdca059fac96b7185dea5467
Merge: 7ad3ef9 841af4e
Author: Blaine Bublitz
 <a href="mailto:blaine@iceddev.com">
  blaine@iceddev.com
 </a>
 Date:   Thu Aug 20 11:35:15 2015 -0700
</p>
<pre><code>Merge pull request #1211 from JimiHFord/patch-1

Update guidelines.md
</code></pre>
<p>
 commit 841af4ee7aaf55b505354d0e86d7fb876d745e26
Author: Jimi Ford
 <a href="mailto:JimiHFord@users.noreply.github.com">
  JimiHFord@users.noreply.github.com
 </a>
 Date:   Thu Aug 20 11:55:38 2015 -0400
</p>
<pre><code>Update guidelines.md

fixed typo
</code></pre>
<p>
 ```
</p>
<h3>
 archive-file
</h3>
<p>
 <code>
  $ git archive-file
Building archive on branch "master"
Saved to "gulp.v3.9.0-36-g47cb6b0.zip" ( 60K)
 </code>
</p>
<h3>
 missing
</h3>
<p>
 ```
$ git missing master
< d14b8f0 only on current checked out branch
</p>
<blockquote>
 <p>
  97ef387 only on master
  ```
 </p>
</blockquote>
<h3>
 lock
</h3>
<p>
 <code>
  $ git lock config/database.yml
 </code>
</p>
<h3>
 locked
</h3>
<p>
 <code>
  $ git locked
config/database.yml
 </code>
</p>
<h3>
 unlock
</h3>
<p>
 <code>
  $ git unlock config/database.yml
 </code>
</p>
<h3>
 reset-file
</h3>
<p>
 <code>
  $ git reset-file README.md HEAD^
Reset 'README.md' to HEAD^
 </code>
</p>
<h3>
 pr
</h3>
<p>
 <code>
  $ git pr 226
From https://github.com/tj/git-extras
 * [new ref]       refs/pulls/226/head -> pr/226
Switched to branch 'pr/226'
 </code>
</p>
<h3>
 root
</h3>
<p>
 <code>
  $ git root
/GitHub/git
 </code>
</p>
<h3>
 delta
</h3>
<p>
 <code>
  $ git delta
README.md
 </code>
</p>
<h3>
 merge-repo
</h3>
<p>
 <code>
  $ git merge-repo git@github.com:tj/git-extras.git master .
git fetch git@github.com:tj/git-extras.git master
warning: no common commits
remote: Counting objects: 3507, done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 3507 (delta 1), reused 0 (delta 0), pack-reused 3502
Receiving objects: 100% (3507/3507), 821.12 KiB | 286.00 KiB/s, done.
Resolving deltas: 100% (1986/1986), done.
From github.com:tj/git-extras
 * branch            master     -> FETCH_HEAD
Added dir 'git-merge-repo.E95m0gj'
No local changes to save
 </code>
</p>
<h3>
 psykorebase
</h3>
<p>
 <code>
  $ git psykorebase master
$ git psykorebase --continue
$ git psykorebase master feature
 </code>
</p>
<h2>
 <a href="https://github.com/petervanderdoes/gitflow-avh">
  gitflow (AVH Edition)
 </a>
</h2>
<h3>
 flow init
</h3>
<p>
 ```
$ git flow init
</p>
<p>
 Which branch should be used for bringing forth production releases?
   - changelog
   - master
Branch name for production releases: [master]
</p>
<p>
 Which branch should be used for integration of the "next release"?
   - changelog
Branch name for "next release" development: [master]
Production and integration branches should differ.
```
</p>
<h3>
 flow feature
</h3>
<p>
 ```
$ git flow feature
$ git flow feature start awesome-feature
$ git flow feature finish awesome-feature
$ git flow feature delete awesome-feature
</p>
<p>
 $ git flow feature publish awesome-feature
$ git flow feature pull remote awesome-feature
```
</p>
<h3>
 flow release
</h3>
<p>
 <code>
  $ git flow release
$ git flow release start awesome-release
$ git flow release finish awesome-release
$ git flow release delete awesome-release
 </code>
</p>
<h3>
 flow hotfix
</h3>
<p>
 <code>
  $ git flow hotfix
$ git flow hotfix start awesome-release
$ git flow hotfix finish awesome-release
$ git flow hotfix delete awesome-release
 </code>
</p>
<h3>
 flow support
</h3>
<p>
 <code>
  $ git flow support
 </code>
</p>
<h2>
 <a href="https://github.com/aanand/git-up">
  git-up
 </a>
</h2>
<p>
 <code>
  $ git up
Fetching origin
4.0       fast-forwarding...
changelog ahead of upstream
master    fast-forwarding...
returning to 4.0
 </code>
</p>
<h2>
 <a href="https://github.com/github/hub">
  hub
 </a>
</h2>
<h3>
 clone
</h3>
<p>
 ```
$ git clone schacon/ticgit
</p>
<blockquote>
 <p>
  git clone git://github.com/schacon/ticgit.git
 </p>
</blockquote>
<p>
 $ git clone -p schacon/ticgit
</p>
<blockquote>
 <p>
  git clone git@github.com:schacon/ticgit.git
 </p>
</blockquote>
<p>
 $ git clone resque
</p>
<blockquote>
 <p>
  git clone git@github.com/YOUR_USER/resque.git
  ```
 </p>
</blockquote>
<h3>
 remote add
</h3>
<p>
 ```
$ git remote add rtomayko
</p>
<blockquote>
 <p>
  git remote add rtomayko git://github.com/rtomayko/CURRENT_REPO.git
 </p>
</blockquote>
<p>
 $ git remote add -p rtomayko
</p>
<blockquote>
 <p>
  git remote add rtomayko git@github.com:rtomayko/CURRENT_REPO.git
 </p>
</blockquote>
<p>
 $ git remote add origin
</p>
<blockquote>
 <p>
  git remote add origin git://github.com/YOUR
  <em>
   USER/CURRENT
  </em>
  REPO.git
  ```
 </p>
</blockquote>
<h3>
 fetch
</h3>
<p>
 ```
$ git fetch mislav
</p>
<blockquote>
 <p>
  git remote add mislav git://github.com/mislav/REPO.git
  git fetch mislav
 </p>
</blockquote>
<p>
 $ git fetch mislav,xoebus
</p>
<blockquote>
 <p>
  git remote add mislav ...
  git remote add xoebus ...
  git fetch --multiple mislav xoebus
  ```
 </p>
</blockquote>
<h3>
 cherry-pick
</h3>
<p>
 ```
$ git cherry-pick https://github.com/mislav/REPO/commit/SHA
</p>
<blockquote>
 <p>
  git remote add -f --no-tags mislav git://github.com/mislav/REPO.git
  git cherry-pick SHA
 </p>
</blockquote>
<p>
 $ git cherry-pick mislav@SHA
</p>
<blockquote>
 <p>
  git remote add -f --no-tags mislav git://github.com/mislav/CURRENT_REPO.git
  git cherry-pick SHA
 </p>
</blockquote>
<p>
 $ git cherry-pick mislav@SHA
</p>
<blockquote>
 <p>
  git fetch mislav
  git cherry-pick SHA
  ```
 </p>
</blockquote>
<h3>
 am
</h3>
<p>
 ```
$ git am https://github.com/github/hub/pull/55
[ downloads patch via API ]
</p>
<blockquote>
 <p>
  git am /tmp/55.patch
 </p>
</blockquote>
<p>
 $ git am --ignore-whitespace https://github.com/davidbalbert/hub/commit/fdb9921
[ downloads patch via API ]
</p>
<blockquote>
 <p>
  git am --ignore-whitespace /tmp/fdb9921.patch
  ```
 </p>
</blockquote>
<h3>
 apply
</h3>
<p>
 ```
$ git apply https://gist.github.com/8da7fb575debd88c54cf
[ downloads patch via API ]
</p>
<blockquote>
 <p>
  git apply /tmp/gist-8da7fb575debd88c54cf.txt
  ```
 </p>
</blockquote>
<h3>
 fork
</h3>
<p>
 ```
$ git fork
[ repo forked on GitHub ]
</p>
<blockquote>
 <p>
  git remote add -f YOUR
  <em>
   USER git@github.com:YOUR
  </em>
  USER/CURRENT_REPO.git
  ```
 </p>
</blockquote>
<h3>
 pull-request
</h3>
<p>
 <code>
  $ git pull-request
[ opens text editor to edit title & body for the request ]
[ opened pull request on GitHub for "YOUR_USER:feature" ]
 </code>
</p>
<h3>
 checkout
</h3>
<p>
 ```
$ git checkout https://github.com/github/hub/pull/73
</p>
<blockquote>
 <p>
  git remote add -f --no-tags -t feature mislav git://github.com/mislav/hub.git
  git checkout --track -B mislav-feature mislav/feature
  ```
 </p>
</blockquote>
<h3>
 merge
</h3>
<p>
 ```
$ git merge https://github.com/github/hub/pull/73
</p>
<blockquote>
 <p>
  git fetch git://github.com/mislav/hub.git +refs/heads/feature:refs/remotes/mislav/feature
  git merge mislav/feature --no-ff -m 'Merge pull request #73 from mislav/feature...'
  ```
 </p>
</blockquote>
<h3>
 create
</h3>
<p>
 ```
$ git create
[ repo created on GitHub ]
</p>
<blockquote>
 <p>
  git remote add origin git@github.com:YOUR
  <em>
   USER/CURRENT
  </em>
  REPO.git
  ```
 </p>
</blockquote>
<h3>
 init
</h3>
<p>
 ```
$ git init -g
</p>
<blockquote>
 <p>
  git init
  git remote add origin git@github.com:YOUR_USER/REPO.git
  ```
 </p>
</blockquote>
<h3>
 push
</h3>
<p>
 ```
$ git push origin,staging,qa bert_timeout
</p>
<blockquote>
 <p>
  git push origin bert
  <em>
   timeout
  git push staging bert
  </em>
  timeout
  git push qa bert_timeout
  ```
 </p>
</blockquote>
<h3>
 browse
</h3>
<p>
 ```
$ git browse
</p>
<blockquote>
 <p>
  open https://github.com/YOUR
  <em>
   USER/CURRENT
  </em>
  REPO
  ```
 </p>
</blockquote>
<h3>
 compare
</h3>
<p>
 ```
$ git compare refactor
</p>
<blockquote>
 <p>
  open https://github.com/CURRENT_REPO/compare/refactor
  ```
 </p>
</blockquote>
<h3>
 submodule
</h3>
<p>
 ```
$ git submodule add wycats/bundler vendor/bundler
</p>
<blockquote>
 <p>
  git submodule add git://github.com/wycats/bundler.git vendor/bundler
  ```
 </p>
</blockquote>
<h3>
 ci-status
</h3>
<p>
 <code>
  $ git ci-status
success
 </code>
</p>
<h2>
 <a href="https://github.com/mislav/git-deploy">
  git-deploy
 </a>
</h2>
<p>
 <code>
  $ git remote add production "user@example.com:/apps/mynewapp"
$ git deploy setup -r "production"
$ git deploy init
$ git push production master
 </code>
</p>
<h2>
 <a href="https://github.com/k4rthik/git-cal">
  git-cal
 </a>
</h2>
<p>
 <img alt="68747470733a2f2f7261772e6769746875622e636f6d2f6b34727468696b2f6769742d63616c2f6d61737465722f73637265656e73686f74732f696d67322e706e67" src="https://cloud.githubusercontent.com/assets/6316590/12465623/17d828ea-c023-11e5-8077-2e9a284defd6.png"/>
</p>
<h2>
 <a href="https://github.com/icefox/git-hooks">
  git-hooks
 </a>
</h2>
<p>
 ```
$ git hooks --install
$ git hooks
Git hooks ARE installed in this repository.
</p>
<h2>
 Listing User, Project, and Global hooks:
</h2>
<p>
 /Users/stevemao/.git_hooks:
</p>
<p>
 /GitHub/git-hooks/git_hooks:
commit-msg/signed-off-by    - Checks commit message for presence of Signed-off-by line.
pre-commit/bsd  - Check for the BSD license.
</p>
<p>
 /GitHub/git-hooks/.githooks:
```
</p>
<h2>
 <a href="https://github.com/mhagger/git-imerge">
  git-imerge
 </a>
</h2>
<h3>
 imerge start
</h3>
<p>
 <code>
  $ git imerge start --name=next --goal=merge --first-parent 4.0
Attempting automerge of 1-1...success.
Attempting automerge of 1-29...success.
Attempting automerge of 1-44...success.
Attempting automerge of 1-51...success.
 </code>
</p>
<h3>
 imerge merge
</h3>
<p>
 <code>
  $ git imerge merge 4.0
Attempting automerge of 1-1...success.
Attempting automerge of 1-6...success.
Attempting automerge of 1-9...success.
Attempting automerge of 1-10...success.
 </code>
</p>
<h3>
 imerge rebase
</h3>
<p>
 <code>
  $ git imerge rebase 4.0
The following commits on the to-be-merged branch are merge commits:
    8e4931ae15971a14897cf347ac50b7d7fe125ac4
    d7c772142ce663a20210db73d9ad17cc8d59e0d6
    856df83c77b33029d2ddfb8eecd08efedeadc027
 </code>
</p>
<h3>
 imerge continue
</h3>
<p>
 <code>
  $ git add --all
$ git commit
[imerge/next e442618] imerge 'next': manual merge 10-26
$ git imerge continue
Merge has been recorded for merge 10-26.
Attempting automerge of 10-27...success.
Attempting automerge of 10-42...failure.
Attempting automerge of 10-34...failure.
Attempting automerge of 10-30...success.
Recording autofilled block MergeState('next', tip1='master', tip2='4.0', goal='merge')[18:20,34:58].
Merge is complete!
 </code>
</p>
<h3>
 imerge finish
</h3>
<p>
 <code>
  $ git imerge finish
Previous HEAD position was fcbe161... imerge 'next': automatic merge 19-57
Switched to branch 'next'
[next 23362e6] Merge 4.0 into master (using imerge)
 Date: Wed Sep 2 10:59:56 2015 +1000
 </code>
</p>
<h3>
 imerge diagram
</h3>
<p>
 ```
$ git imerge diagram
</p>
<hr/>
<p>
 <em>
  ????????.?????????|
*????????.?????????|
*????????.?????????|
*????????...-------+
*????????.
 </em>
 |#???????
```
</p>
<h3>
 imerge list
</h3>
<p>
 <code>
  $ git imerge list
* next
 </code>
</p>
<h3>
 imerge init
</h3>
<p>
 <code>
  $ git imerge init --name=next --goal=merge --first-parent 4.0
 </code>
</p>
<h3>
 imerge record
</h3>
<p>
 <code>
  $ git imerge record
Merge has been recorded for merge 10-26.
Attempting automerge of 10-27...success.
Attempting automerge of 10-42...failure.
Attempting automerge of 10-34...failure.
 </code>
</p>
<h3>
 imerge autofill
</h3>
<p>
 <code>
  $ git imerge autofill
Attempting automerge of 1-1...success.
Attempting automerge of 1-29...success.
Attempting automerge of 1-44...success.
 </code>
</p>
<h3>
 imerge simplify
</h3>
<p>
 <code>
  $ git imerge simplify
Previous HEAD position was 4d19598... imerge 'next': automatic merge 20-57
Switched to branch 'next'
[next 6c308aa] Merge 4.0 into master (using imerge)
 Date: Wed Sep 2 13:37:31 2015 +1000
 </code>
</p>
<h3>
 imerge remove
</h3>
<p>
 <code>
  $ git imerge remove
 </code>
</p>
<h3>
 imerge reparent
</h3>
<p>
 <code>
  $ git imerge reparent
67ebc0e6517ac791de6699453b71d2c7fd81ffcd
 </code>
</p>
<h2>
 <a href="https://github.com/github/git-lfs">
  git-lfs
 </a>
</h2>
<p>
 ```
$ git lfs track "*.mp3"
Tracking *.mp3
</p>
<p>
 $ git lfs track "*.zip"
Tracking *.zip
</p>
<p>
 $ git lfs track
Listing tracked paths
    *.mp3 (.gitattributes)
    *.zip (.gitattributes)
</p>
<p>
 $ git lfs untrack "*.zip"
Untracking *.zip
</p>
<p>
 $ git lfs track
Listing tracked paths
    *.mp3 (.gitattributes)
```
</p>
<h2>
 <a href="https://github.com/iwata/git-now">
  git-now
 </a>
</h2>
<p>
 ```
$ git now
[master 1bd9ce8] [from now] 2015/08/27 10:39:10
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git log
commit 1bd9ce878a76140f7db95afd9cfd4d7befbc7243
Author: Steve Mao
 <a href="mailto:maochenyan@gmail.com">
  maochenyan@gmail.com
 </a>
 Date:   Thu Aug 27 10:39:10 2015 +1000
</p>
<pre><code>[from now] 2015/08/27 10:39:10

diff --git a/package.json b/package.json
index 8768569..540523a 100644
--- a/package.json
+++ b/package.json
@@ -1,7 +1,7 @@
 {
   "name": "gulp",
   "description": "The streaming build system",
-  "version": "3.9.0",
+  "version": "3.10.0",
   "homepage": "http://gulpjs.com",
   "repository": "gulpjs/gulp",
   "author": "Fractal <contact@wearefractal.com> (http://wearefractal.com/)",
</code></pre>
<p>
 ```
</p>
<h2>
 <a href="https://github.com/tkrajina/git-plus">
  git-plus
 </a>
</h2>
<h3>
 multi
</h3>
<p>
 ```
</p>
<h2>
 $ git multi
</h2>
<h2>
 Executing git status -s
</h2>
<p>
 chalk:
     M package.json
</p>
<p>
 gulp:
     D index.js
```
</p>
<h3>
 relation
</h3>
<p>
 ```
$ git relation origin/4.0
HEAD and origin/4.0 DIVERGED, common point is 657213a52d5e9c19b85df6a42f76341a98c08ae8
</p>
<p>
 Commits from 657213a52d5e9c19b85df6a42f76341a98c08ae8 to HEAD:
Error retrieving log 657213a52d5e9c19b85df6a42f76341a98c08ae8..HEAD
```
</p>
<h3>
 old-branches
</h3>
<p>
 <code>
  $ git old-branches -d 10
Branch 4.0 is older than 10 days (139.86)!
 </code>
</p>
<h3>
 recent
</h3>
<p>
 <code>
  $ git recent
      3.64 days: master
     11.63 days: dev
 </code>
</p>
<h2>
 <a href="https://github.com/spotify/git-test">
  git-test
 </a>
</h2>
<p>
 <code>
  $ git test -v
4.0 ^origin/4.0 ^origin/master will test        2 commits
iter commit  tree    result
0000 57af4b0 f5ef0d8 pass (cached)
0001 10ed389 434370f pass
 </code>
</p>
<h2>
 <a href="https://github.com/kennethreitz/legit">
  legit
 </a>
</h2>
<h3>
 branches
</h3>
<p>
 <code>
  $ git branches
   4.0                        (published)
   development                (unpublished)
   everything-is-not-awesome  (published)
*  master                     (published)
   old-master                 (published)
 </code>
</p>
<h3>
 sync
</h3>
<p>
 <code>
  $ git sync
Pulling commits from the server.
First, rewinding head to replay your work on top of it...
Fast-forwarded 4.0 to origin/4.0.
Pushing commits to the server.
 </code>
</p>
<h3>
 resync
</h3>
<p>
 <code>
  $ git resync
Switching to master.
Your branch is ahead of 'origin/master' by 10 commits.
  (use "git push" to publish your local commits)
Pulling commits from the server.
Already up-to-date.
Switching to master.
Your branch is ahead of 'origin/master' by 10 commits.
  (use "git push" to publish your local commits)
Grafting commits from master.
Already up-to-date.
Pulling commits from the server.
Already up-to-date.
Pushing commits to the server.
 </code>
</p>
<h3>
 switch
</h3>
<p>
 ```
$ git switch master
Saving local changes.
Saved working directory and index state On developement: Legit: stashing before switching branches.
HEAD is now at f0fc4c7 Merge branch 'development'
Switching to master.
Your branch is up-to-date with 'origin/master'.
Restoring local changes.
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
  (use "git add
 <file>
  ..." to update what will be committed)
  (use "git checkout --
  <file>
   ..." to discard changes in working directory)
  </file>
 </file>
</p>
<pre><code>modified:   package.json
</code></pre>
<p>
 no changes added to commit (use "git add" and/or "git commit -a")
Dropped stash@{0} (86f5dc9066ff9f69c01c77e2f5a55643ad19f8f2)
```
</p>
<h3>
 sprout
</h3>
<p>
 <code>
  $ git sprout development
Branching master to development.
 </code>
</p>
<h3>
 harvest
</h3>
<p>
 <code>
  $ git harvest development
Grafting commits from development.
Updating e4f08f4..64b3563
Fast-forward
 package.json | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
Restoring local changes.
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)
nothing to commit, working directory clean
Dropped stash@{0} (7c28b7f5eaf09dd72ec6e1ea440cbd1611e36c7f)
 </code>
</p>
<h3>
 graft
</h3>
<p>
 <code>
  $ git graft development
Switching to master.
Your branch is ahead of 'origin/master' by 2 commits.
  (use "git push" to publish your local commits)
Grafting development into master.
Merge made by the 'recursive' strategy.
 feature | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 feature
Deleted branch development (was 6a022ba).
 </code>
</p>
<h3>
 publish
</h3>
<p>
 <code>
  $ git publish
   4.0                        (published)
   changelog                  (published)
   everything-is-not-awesome  (published)
*  master                     (unpublished)
Branch None not found, using current branch master
Publishing master.
Branch master set up to track remote branch master from origin.
 </code>
</p>
<h3>
 unpublish
</h3>
<p>
 <code>
  $ git unpublish master
Unpublishing master.
 </code>
</p>
<h2>
 <a href="https://github.com/mhagger/git-when-merged">
  git-when-merged
 </a>
</h2>
<p>
 <code>
  $ git when-merged a2c9e695ecf3600f21fa731e705fd1a0503632d9
refs/heads/master                      5a2ec1b1a6633f830bd4a2b1daab578c062e6975
$ git when-merged HEAD
refs/heads/master                      Commit is directly on this branch.
 </code>
</p>
<h2>
 <a href="https://github.com/jianli/git-playback">
  git-playback
 </a>
</h2>
<p>
 <code>
  $ git playback README.md
 </code>
</p>
<p>
 <img alt="" src="https://camo.githubusercontent.com/9abe1d2de474dbc0d1ad4f48acf9e954ff0d0b30/68747470733a2f2f7261772e6769746875622e636f6d2f6a69616e6c692f6769742d706c61796261636b2f6d61737465722f616e696d6174696f6e2e676966"/>
</p>
<h2>
 <a href="https://github.com/alexdavid/git-branch-status">
  git-branch-status
 </a>
</h2>
<p>
 <code>
  $ git branch-status
 4.0       [57 ahead and 38 behind master]    [up to date with origin/4.0]
 master    [current branch]                   [1 ahead of origin/master]
 </code>
</p>
<h2>
 <a href="https://github.com/paulirish/git-open">
  git-open
 </a>
</h2>
<p>
 ```
$ git open
</p>
<blockquote>
 <p>
  open https://github.com/REMOTE
  <em>
   ORIGIN
  </em>
  USER/CURRENT
  <em>
   REPO/tree/CURRENT
  </em>
  BRANCH
 </p>
</blockquote>
<p>
 $ git open upstream
</p>
<blockquote>
 <p>
  open https://github.com/REMOTE
  <em>
   UPSTREAM
  </em>
  USER/CURRENT
  <em>
   REPO/tree/CURRENT
  </em>
  BRANCH
 </p>
</blockquote>
<p>
 $ git open upstream master
</p>
<blockquote>
 <p>
  open https://github.com/REMOTE
  <em>
   UPSTREAM
  </em>
  USER/CURRENT_REPO/tree/master
  ```
 </p>
</blockquote>
<h2>
 <a href="https://github.com/davidosomething/git-my">
  git-my
 </a>
</h2>
<p>
 ```
$ git my
</p>
<p>
 +------------------------------------------------------------------------------+
| your name's remote branches in git@repo:repopath/reponame.git                |
+------------------------------------------------------------------------------+
</p>
<p>
 local copy?  in master?  branch name
  ................[merged]. EC-242
  .....[local]....[merged]. commonjs-lazyload
  .....[local]............. enqueue-gpt
  ......................... defunct-ios-app-nag
  .....[local]............. factor-bundles
```
</p>
<h2>
 <a href="https://github.com/davidosomething/git-ink">
  git-ink
 </a>
</h2>
<p>
 ```
$ git ink
</p>
<p>
 • enqueue-gpt ........................................... 2015-08-31
• factor-bundles ........................................ 2015-10-14
    - Pull out more modules into node
 <em>
  modules
    - Works but does not provide any gains
• hbsfy ................................................. 2015-10-21
✓ master ................................................ 2015-10-22
• nda-ads4 .............................................. 2015-10-22
• remove-equalize
 </em>
 content
 <em>
  height ........................ 2015-10-21
• remove-exorcise ....................................... 2015-10-21
    - Need to DRY up exorcise function
    - Does not map properly when uglified
    - Need to undo postCSS mapping changes
• rm-convert
 </em>
 dates-order ................................ 2015-10-22
• sass-lint ............................................. 2015-10-14
    - module does not work
```
</p>
<h2>
 <a href="https://github.com/scottgonzalez/recursive-blame">
  recursive-blame
 </a>
</h2>
<p>
 ```
$ git recursive-blame version package.json
</p>
<p>
 Commit: 247479d017f138c26be27c64a0ce27f5f21fc0af
Author: Jeff Cross
 <a href="mailto:middlefloor@gmail.com">
  middlefloor@gmail.com
 </a>
 Date:   Tue Oct 13 15:58:13 2015 -0700 (7 weeks ago)
Path:   package.json
Match:  1 of 1
</p>
<pre><code>chore(release): bump angular version to alpha.42
</code></pre>
<p>
 1) {
2)   "name": "angular",
3)   "version": "2.0.0-alpha.42",
4)   "branchPattern": "2.0.*",
5)   "description": "Angular 2 - a web framework for modern web apps",
6)   "homepage": "https://github.com/angular/angular",
7)   "bugs": "https://github.com/angular/angular/issues",
</p>
<p>
 Next action [r,n,p,c,d,q,?]? r
</p>
<p>
 Commit: bb9d299b3860f6d579192828451ccd7ace70e1d8
Author: Igor Minar
 <a href="mailto:igor@angularjs.org">
  igor@angularjs.org
 </a>
 Date:   Tue Oct 13 12:28:03 2015 -0700 (7 weeks ago)
Path:   package.json
Match:  1 of 1
</p>
<pre><code>chore(release): bump angular version to alpha.41
</code></pre>
<p>
 1) {
2)   "name": "angular",
3)   "version": "2.0.0-alpha.41",
4)   "branchPattern": "2.0.*",
5)   "description": "Angular 2 - a web framework for modern web apps",
6)   "homepage": "https://github.com/angular/angular",
7)   "bugs": "https://github.com/angular/angular/issues",
```
</p>
<h2>
 <a href="https://github.com/qw3rtman/git-fire">
  git-fire
 </a>
</h2>
<p>
 ```
$ git fire
Switched to a new branch 'fire-master-maochenyan@gmail.com-1451379915'
On branch fire-master-maochenyan@gmail.com-1451379915
nothing to commit, working directory clean
Counting objects: 2, done.
Writing objects: 100% (2/2), 168 bytes | 0 bytes/s, done.
Total 2 (delta 0), reused 0 (delta 0)
To git@bitbucket.org:maochenyan/fire.git
 * [new branch]      fire-master-maochenyan@gmail.com-1451379915 -> fire-master-maochenyan@gmail.com-1451379915
Branch fire-master-maochenyan@gmail.com-1451379915 set up to track remote branch fire-master-maochenyan@gmail.com-1451379915 from origin.
</p>
<p>
 Leave building!
```
</p>
<h2>
 <a href="https://github.com/Originate/git-town">
  git-town
 </a>
</h2>
<p>
 TBD
</p>
<h2>
 <a href="https://github.com/jayphelps/git-blame-someone-else">
  git-blame-someone-else
 </a>
</h2>
<p>
 <code>
  $ git blame-someone-else 'Steve Mao <maochenyan@gmail.com>' 2efb4e3a061a2e8aaa58033e9c13c3e0e5fcde4b
Steve Mao  is now the author of 2efb4e3. You're officially an asshole.
 </code>
</p>
<h2>
 <a href="https://github.com/so-fancy/diff-so-fancy">
  diff-so-fancy
 </a>
</h2>
<p>
 <code>
  $ git dsf
 </code>
</p>
<p>
 <img alt="diff-so-fancy" src="https://cloud.githubusercontent.com/assets/39191/13622719/7cc7c54c-e555-11e5-86c4-7045d91af041.png"/>
</p>
<h2>
 <a href="https://github.com/IonicaBizau/git-stats">
  git-stats
 </a>
</h2>
<p>
 <img alt="" src="http://i.imgur.com/PpM0i3v.png"/>
</p>
<h2>
 <a href="https://github.com/sobolevn/git-secret">
  git-secret
 </a>
</h2>
<h3>
 git secret init
</h3>
<p>
 <code>
  $ git secret init
'.gitsecret/' created.
 </code>
</p>
<h3>
 git secret tell
</h3>
<p>
 <code>
  $ git secret tell my@email.com
done. my@email.com added as a person who knows the secret.
cleaning up...
 </code>
</p>
<h3>
 git secret add
</h3>
<p>
 <code>
  $ git secret add hideme.txt 
1 items added.
 </code>
</p>
<h3>
 git secret list
</h3>
<p>
 <code>
  $ git secret list
hideme.txt
 </code>
</p>
<h3>
 git secret hide
</h3>
<p>
 <code>
  $ git secret hide
done. all 1 files are hidden.
 </code>
</p>
<h3>
 git secret reveal
</h3>
<p>
 ```
$ git secret reveal
</p>
<p>
 You need a passphrase to unlock the secret key for
user: "Test User
 <a href="mailto:my@email.com">
  my@email.com
 </a>
 "
2048-bit RSA key, ID #######, created 2015-01-01 (main key ID #######)
</p>
<p>
 gpg: gpg-agent is not available in this session
File `hideme.txt' exists. Overwrite? (y/N) y
done. all 1 files are revealed.
```
</p>
<h2>
 <a href="https://github.com/petkaantonov/apply-pr">
  apply-pr
 </a>
</h2>
<p>
 TBD
</p>
<h2>
 <a href="https://github.com/keis/git-fixup">
  git-fixup
 </a>
</h2>
<p>
 <code>
  $ git diff --cached -U0
diff --git a/README.md b/README.md
index 0c700d1..7a57cef 100644
--- a/README.md
+++ b/README.md
@@ -1330 +1330 @@ $ git secret hide
-done. all 1 files are hidden.
+done. all 3 files are hidden.
$ git fixup 6d623f6525dd94b4aaea6f6ae2e7a59edc39bdb8
24aa3d9c10cc02fe813dc83d1ac792cc2e7d705d [F] add screenshot of git-stats <maochenyan@gmail.com>
6d623f6525dd94b4aaea6f6ae2e7a59edc39bdb8 [L] changed gif with text <mail@sobolevn.me>
 </code>
</p>
<h2>
 <a href="https://github.com/paulirish/git-recent">
  git-recent
 </a>
</h2>
<p>
 <code>
  $ git recent
 </code>
</p>
<p>
 <img alt="git-recent screenshot" src="https://cloud.githubusercontent.com/assets/39191/17446638/039d4cee-5aff-11e6-9e11-4294f0020513.png"/>
</p>
<h2>
 <a href="https://github.com/felixSchl/git-fiddle">
  git-fiddle
 </a>
</h2>
<p>
 ```
$ git fiddle -h
git-fiddle
</p>
<p>
 Edit commit meta information during an
 <em>
  interactive
 </em>
 rebase.
</p>
<p>
 <code>
  git-fiddle(1)' is a lightweight wrapper around
 </code>
 git-rebase(1)' that
annotates each commit with it's
 <em>
  author
 </em>
 date, the author name, as well
as the commit message. Changes to any of these will then be applied
using an 'exec' script during the git-rebase sequence.
</p>
<p>
 Usage:
  $SCRIPT [--[no-]-fiddle-messages] [args...]
</p>
<p>
 Options:
  --[no-]fiddle-messages Do not edit commit messages. Useful for quick edits
                         to author or date. This value can also be set using
 <code>
  git config fiddle.messages
 </code>
 .
  [args...]              These arguments are passed verbatim to git-rebase.
```
</p>
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
 <a href="https://github.com/stevemao">
  Steve Mao
 </a>
 has waived all copyright and related or neighboring rights to this work.
</p>
