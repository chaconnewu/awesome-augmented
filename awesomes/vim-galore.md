<p>
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="vim-galore" src="https://cdn.rawgit.com/mhinz/vim-galore/master/media/badge-awesome.svg"/>
 </a>
 <a href="https://raw.githubusercontent.com/mhinz/vim-galore/master/LICENSE">
  <img alt="LICENSE" src="https://img.shields.io/badge/license-MIT-lightgrey.svg"/>
 </a>
 <a href="https://travis-ci.org/mhinz/vim-galore">
  <img alt="Build Status" src="https://travis-ci.org/mhinz/vim-galore.svg?branch=master"/>
 </a>
</p>
<p>
 <img alt="vim-galore" src="https://raw.githubusercontent.com/mhinz/vim-galore/master/media/vim-galore.png"/>
</p>
<hr/>
<p>
 Want me to write about a certain topic? Create an
 <a href="https://github.com/mhinz/vim-galore/issues">
  issue
 </a>
 for it! ∴ My
 <a href="https://github.com/mhinz/dotfiles/blob/master/vim/vimrc">
  vimrc
 </a>
 . ∴
 <a href="https://twitter.com/_mhinz_">
  Me on
Twitter
 </a>
 .
</p>
<hr/>
<h4>
 <a href="#intro-1">
  Intro
 </a>
</h4>
<ul>
 <li>
  <a href="#what-is-vim">
   What is Vim?
  </a>
 </li>
 <li>
  <a href="#the-vim-philosophy">
   The Vim Philosophy
  </a>
 </li>
 <li>
  <a href="#first-steps">
   First steps
  </a>
 </li>
 <li>
  <a href="#minimal-vimrc">
   Minimal vimrc
  </a>
 </li>
 <li>
  <a href="#what-kind-of-vim-am-i-running">
   What kind of Vim am I running?
  </a>
 </li>
 <li>
  <a href="#cheatsheets">
   Cheatsheets
  </a>
 </li>
</ul>
<h4>
 <a href="#basics-1">
  Basics
 </a>
</h4>
<ul>
 <li>
  <a href="#buffers-windows-tabs">
   Buffers, windows, tabs?
  </a>
 </li>
 <li>
  <a href="#active-loaded-listed-named-buffers">
   Active, loaded, listed, named buffers?
  </a>
 </li>
 <li>
  <a href="#argument-list">
   Argument list?
  </a>
 </li>
 <li>
  <a href="#mappings">
   Mappings?
  </a>
 </li>
 <li>
  <a href="#mapleader">
   Mapleader?
  </a>
 </li>
 <li>
  <a href="#registers">
   Registers?
  </a>
 </li>
 <li>
  <a href="#ranges">
   Ranges?
  </a>
 </li>
 <li>
  <a href="#marks">
   Marks?
  </a>
 </li>
 <li>
  <a href="#completion">
   Completion?
  </a>
 </li>
 <li>
  <a href="#motions-operators-text-objects">
   Motions? Operators? Text objects?
  </a>
 </li>
 <li>
  <a href="#autocmds">
   Autocmds?
  </a>
 </li>
 <li>
  <a href="#changelist-jumplist">
   Changelist? Jumplist?
  </a>
 </li>
 <li>
  <a href="#undo-tree">
   Undo tree?
  </a>
 </li>
 <li>
  <a href="#quickfix-and-location-lists">
   Quickfix and location lists?
  </a>
 </li>
 <li>
  <a href="#macros">
   Macros?
  </a>
 </li>
 <li>
  <a href="#colorschemes">
   Colorschemes?
  </a>
 </li>
 <li>
  <a href="#folding">
   Folding?
  </a>
 </li>
 <li>
  <a href="#sessions">
   Sessions?
  </a>
 </li>
 <li>
  <a href="#locality">
   Locality?
  </a>
 </li>
</ul>
<h4>
 <a href="#usage-1">
  Usage
 </a>
</h4>
<ul>
 <li>
  <a href="#getting-help-offline">
   Getting help offline
  </a>
 </li>
 <li>
  <a href="#getting-help-offline-alternative">
   Getting help offline (alternative)
  </a>
 </li>
 <li>
  <a href="#getting-help-online">
   Getting help online
  </a>
 </li>
 <li>
  <a href="#clipboard">
   Clipboard
  </a>
  <ul>
   <li>
    <a href="#clipboard-usage-windows-osx">
     Clipboard usage (Windows, OSX)
    </a>
   </li>
   <li>
    <a href="#clipboard-usage-linux-bsd-">
     Clipboard usage (Linux, BSD, ...)
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#restore-cursor-position-when-opening-file">
   Restore cursor position when opening file
  </a>
 </li>
 <li>
  <a href="#handling-backup-swap-undo-and-viminfo-files">
   Handling backup, swap, undo, and viminfo files
  </a>
 </li>
 <li>
  <a href="#editing-remote-files">
   Editing remote files
  </a>
 </li>
 <li>
  <a href="#managing-plugins">
   Managing plugins
  </a>
 </li>
 <li>
  <a href="#block-insert">
   Block insert
  </a>
 </li>
 <li>
  <a href="#running-external-programs-and-using-filters">
   Running external programs and using filters
  </a>
 </li>
 <li>
  <a href="#cscope">
   Cscope
  </a>
 </li>
 <li>
  <a href="#matchit">
   MatchIt
  </a>
 </li>
</ul>
<h4>
 <a href="#tips-1">
  Tips
 </a>
</h4>
<ul>
 <li>
  <a href="#saner-behavior-of-n-and-n">
   Saner behavior of n and N
  </a>
 </li>
 <li>
  <a href="#saner-command-line-history">
   Saner command-line history
  </a>
 </li>
 <li>
  <a href="#saner-ctrl-l">
   Saner CTRL-L
  </a>
 </li>
 <li>
  <a href="#disable-audible-and-visual-bells">
   Disable audible and visual bells
  </a>
 </li>
 <li>
  <a href="#quickly-move-current-line">
   Quickly move current line
  </a>
 </li>
 <li>
  <a href="#quickly-add-empty-lines">
   Quickly add empty lines
  </a>
 </li>
 <li>
  <a href="#quickly-edit-your-macros">
   Quickly edit your macros
  </a>
 </li>
 <li>
  <a href="#quickly-jump-to-header-or-source-file">
   Quickly jump to header or source file
  </a>
 </li>
 <li>
  <a href="#quickly-change-font-size-in-gui">
   Quickly change font size in GUI
  </a>
 </li>
 <li>
  <a href="#change-cursor-style-dependent-on-mode">
   Change cursor style dependent on mode
  </a>
 </li>
 <li>
  <a href="#dont-lose-selection-when-shifting-sidewards">
   Don't lose selection when shifting sidewards
  </a>
 </li>
 <li>
  <a href="#reload-a-file-on-saving">
   Reload a file on saving
  </a>
 </li>
 <li>
  <a href="#smarter-cursorline">
   Smarter cursorline
  </a>
 </li>
 <li>
  <a href="#faster-keyword-completion">
   Faster keyword completion
  </a>
 </li>
</ul>
<h4>
 <a href="#commands-1">
  Commands
 </a>
</h4>
<ul>
 <li>
  <a href="#global">
   :global
  </a>
  - Execute a command on all matching lines.
 </li>
 <li>
  <a href="#normal-and-execute">
   :normal and :execute
  </a>
  - The scripting dream team.
 </li>
 <li>
  <a href="#redir">
   :redir
  </a>
  - Redirect messages.
 </li>
</ul>
<h4>
 <a href="#debugging-1">
  Debugging
 </a>
</h4>
<ul>
 <li>
  <a href="#general-tips">
   General tips
  </a>
 </li>
 <li>
  <a href="#profiling-startup-time">
   Profiling startup time
  </a>
 </li>
 <li>
  <a href="#profiling-at-runtime">
   Profiling at runtime
  </a>
 </li>
 <li>
  <a href="#verbosity">
   Verbosity
  </a>
 </li>
 <li>
  <a href="#debugging-vim-scripts">
   Debugging Vim scripts
  </a>
 </li>
 <li>
  <a href="#debugging-syntax-files">
   Debugging syntax files
  </a>
 </li>
</ul>
<h4>
 <a href="#miscellaneous-1">
  Miscellaneous
 </a>
</h4>
<ul>
 <li>
  <a href="#additional-resources">
   Additional resources
  </a>
 </li>
 <li>
  <a href="#vim-distributions">
   Vim distributions
  </a>
 </li>
 <li>
  <a href="#standard-plugins">
   Standard plugins
  </a>
 </li>
 <li>
  <a href="#map-capslock-to-control">
   Map CapsLock to Control
  </a>
 </li>
 <li>
  <a href="#easter-eggs">
   Easter eggs
  </a>
 </li>
 <li>
  <a href="#why-hjkl-for-navigation">
   Why hjkl for navigation?
  </a>
 </li>
</ul>
<h4>
 <a href="#quirks-1">
  Quirks
 </a>
</h4>
<ul>
 <li>
  <a href="#editing-small-files-is-slow">
   Editing small files is slow
  </a>
 </li>
 <li>
  <a href="#editing-huge-files-is-slow">
   Editing huge files is slow
  </a>
 </li>
 <li>
  <a href="#newline-used-for-nul">
   Newline used for NUL
  </a>
 </li>
 <li>
  <a href="#bracketed-paste-or-why-do-i-have-to-set-paste-all-the-time">
   Bracketed paste (or why do I have to set 'paste' all the time?)
  </a>
 </li>
 <li>
  <a href="#delays-when-using-escape-key-in-terminal">
   Delays when using escape key in terminal
  </a>
 </li>
</ul>
<h4>
 <a href="#list-of-colorschemes-1">
  List of colorschemes
 </a>
</h4>
<h4>
 <a href="content/plugins.md">
  List of plugins
 </a>
</h4>
<h4>
 <a href="content/neovim.md">
  Neovim
 </a>
</h4>
<hr/>
<h2>
 Intro
</h2>
<h4>
 What is Vim?
</h4>
<p>
 <a href="http://www.vim.org">
  Vim
 </a>
 is a text editor with a long line of ancestors that
goes back to
 <a href="https://en.wikipedia.org/wiki/QED_(text_editor)">
  qed
 </a>
 .
 <a href="https://en.wikipedia.org/wiki/Bram_Moolenaar">
  Bram
Moolenaar
 </a>
 released it in 1991.
</p>
<p>
 The project is hosted online at
 <a href="http://www.vim.org/index.php">
  vim.org
 </a>
 .
</p>
<p>
 Getting Vim: Use your favourite package manager or visit the
 <a href="http://www.vim.org/download.php">
  download
page
 </a>
 from vim.org.
</p>
<p>
 Discussions and user questions are best done on the
 <a href="https://groups.google.com/forum/#!forum/vim_use">
  vim_use
 </a>
 mailing list or using
IRC (
 <a href="https://freenode.net">
  Freenode
 </a>
 ) in the
 <code>
  #vim
 </code>
 channel.
</p>
<p>
 Development happens on
 <a href="https://github.com/vim/vim">
  Github
 </a>
 , discussions on the
 <a href="https://groups.google.com/forum/#!forum/vim_dev">
  vim_dev
 </a>
 mailing list.
</p>
<p>
 Read
 <a href="http://www.viemu.com/a-why-vi-vim.html">
  Why, oh WHY, do those #?@! nutheads use
vi?
 </a>
 to see common misconceptions about
Vim explained.
</p>
<h4>
 The Vim Philosophy
</h4>
<p>
 Vim adheres to the modal editing philosophy. This means that it provides
multiple modes and the meaning of keys changes according to the mode. You
navigate files in
 <em>
  normal mode
 </em>
 , you insert text in
 <em>
  insert mode
 </em>
 , you select
lines in
 <em>
  visual mode
 </em>
 , you access commands in
 <em>
  command-line mode
 </em>
 and so on.
This might sound complicated at first, but has a huge advantage: you don't have
to break your fingers by holding several keys at once, most of the time you
simply press them one after the other. The more common the task, the fewer keys
are needed.
</p>
<p>
 A related concept that works well with modal editing are operators and motions.
 <em>
  Operators
 </em>
 start a certain action, e.g. changing, removing, or selecting text.
Afterwards you specify the region of text you want to act on using a
 <em>
  motion
 </em>
 .
To change everything between parentheses, use
 <code>
  ci(
 </code>
 (read
 <em>
  change inner
parentheses
 </em>
 ). To remove an entire paragraph of text, use
 <code>
  dap
 </code>
 (read
 <em>
  delete
around paragraph
 </em>
 ).
</p>
<p>
 If you see advanced Vim users working, you'll notice that they speak the
 <em>
  language of Vim
 </em>
 as well as pianists handle their instruments. Complex
operations are done using only a few key presses. They don't even think about it
anymore as
 <a href="https://en.wikipedia.org/wiki/Muscle_memory">
  muscle memory
 </a>
 took
over already. This reduces
 <a href="https://en.wikipedia.org/wiki/Cognitive_load">
  cognitive
load
 </a>
 and helps focusing on the
actual task.
</p>
<h4>
 First steps
</h4>
<p>
 Vim comes bundled with an interactive tutorial that teaches the most basic
things you need to know about. You can start it from the shell:
</p>
<p>
 <code>
  $ vimtutor
 </code>
</p>
<p>
 Don't be put off by how boring it looks like and work through the exercises. The
editors or IDEs you used before were most probably all non-modal, so working by
switching modes will seem awkward at first, but the more you use Vim, the more
it becomes
 <a href="https://en.wikipedia.org/wiki/Muscle_memory">
  muscle memory
 </a>
 .
</p>
<p>
 Vim was bolted on
 <a href="https://en.wikipedia.org/wiki/Stevie_(text_editor)">
  Stevie
 </a>
 , a
 <a href="https://en.wikipedia.org/wiki/Vi">
  vi
 </a>
 clone, and supports two operating modes:
"compatible" and "nocompatible". Using Vim in compatible mode means using vi
defaults for all options, opposed to Vim defaults. As long as you didn't create
a user vimrc yet or started Vim with
 <code>
  vim -N
 </code>
 , compatible mode is assumed! Don't
use Vim in compatible mode. Just don't.
</p>
<p>
 Next steps:
</p>
<ol>
 <li>
  Create your own
  <a href="#minimal-vimrc">
   vimrc
  </a>
  .
 </li>
 <li>
  Have some
  <a href="#cheatsheets">
   cheatsheets
  </a>
  ready for the first weeks.
 </li>
 <li>
  Read through the
  <a href="#basics-1">
   basics
  </a>
  section to learn what is even possible.
 </li>
 <li>
  Learn on demand! You never finish learning Vim. If you encounter any
problems, just look for it on the internet. Your problem was solved already.
Vim comes with great documentation and knowing how to navigate it is a must:
  <a href="#getting-help-offline">
   Getting help offline
  </a>
  .
 </li>
 <li>
  Have a look at the
  <a href="#additional-resources">
   additional resources
  </a>
  .
 </li>
</ol>
<p>
 One last advice: Please learn how to use Vim properly before starting to add all
kinds of hyped
 <a href="#managing-plugins">
  plugins
 </a>
 that only implement features that
Vim already supports natively.
</p>
<h4>
 Minimal vimrc
</h4>
<p>
 The user vimrc can be put into
 <code>
  ~/.vimrc
 </code>
 or for the sake of better separation
into
 <code>
  ~/.vim/vimrc
 </code>
 . The latter makes it easy to put the entire configuration
under version control and upload it to, let's say Github.
</p>
<p>
 You find many "minimal vimrcs" all over the net, and maybe my version isn't as
minimal as it should be, but it provides a good set of sane settings that I deem
to be useful for starting out.
</p>
<p>
 Eventually you have to read up on all the mentioned settings anyway and decide
for yourself. :-)
</p>
<p>
 So here it is:
 <a href="content/minimal-vimrc.vim">
  minimal-vimrc
 </a>
</p>
<p>
 In case you're interested, here's
 <a href="https://github.com/mhinz/dotfiles/blob/master/vim/vimrc">
  my
vimrc
 </a>
 .
</p>
<p>
 <strong>
  TIP
 </strong>
 : Most plugin authors maintain several plugins and also publish their
vimrc on Github (often in a repository called "vim-config" or "dotfiles"), so
whenever you find a plugin you like, look up its maintainer's Github page and
look through the repositories.
</p>
<h4>
 What kind of Vim am I running?
</h4>
<p>
 Looking at
 <code>
  :version
 </code>
 will give you all the information you need to know about
how the currently running Vim binary was compiled.
</p>
<p>
 The first line tells you when the binary was compiled and the version, e.g. 7.4.
One of the next lines states
 <code>
  Included patches: 1-1051
 </code>
 , which is the patch
level. Thus your exact Vim version is 7.4.1051.
</p>
<p>
 Another line states something like
 <code>
  Tiny version without GUI
 </code>
 or
 <code>
  Huge version
with GUI
 </code>
 . The obvious information from that is whether your Vim includes GUI
support, e.g. for starting
 <code>
  gvim
 </code>
 from the shell or running
 <code>
  :gui
 </code>
 from Vim
within a terminal emulator. The other important information is the
 <code>
  Tiny
 </code>
 and
 <code>
  Huge
 </code>
 . Vim distinguishes between feature sets called
 <code>
  tiny
 </code>
 ,
 <code>
  small
 </code>
 ,
 <code>
  normal
 </code>
 ,
 <code>
  big
 </code>
 , and
 <code>
  huge
 </code>
 , all enabling different subsets of features.
</p>
<p>
 The majority of
 <code>
  :version
 </code>
 output is consumed by the feature list itself.
 <code>
  +clipboard
 </code>
 means the clipboard feature was compiled in,
 <code>
  -clipboard
 </code>
 means it
wasn't compiled in.
</p>
<p>
 A few Vim features need to be compiled in for them to work. E.g. for
 <code>
  :prof
 </code>
 to
work, you need a Vim with a huge feature set, because that set enables the
 <code>
  +profile
 </code>
 feature.
</p>
<p>
 If that's not the case and you installed Vim from a package manager, make sure
to install a package called
 <code>
  vim-x
 </code>
 ,
 <code>
  vim-x11
 </code>
 ,
 <code>
  vim-gtk
 </code>
 ,
 <code>
  vim-gnome
 </code>
 or
similar, since these packages usually come with the huge feature set.
</p>
<p>
 You can also test for the version or features programmatically:
</p>
<p>
 <code>
  vim
" Do something if running at least Vim 7.4.42 with +profile enabled.
if (v:version > 704 || v:version == 704 && has('patch42')) && has('profile')
  " do stuff
endif
 </code>
</p>
<p>
 Related help:
</p>
<p>
 <code>
  :h :version
:h feature-list
:h +feature-list
:h has-patch
 </code>
</p>
<h4>
 Cheatsheets
</h4>
<p>
 To avoid copyright issues, I'll just link external URLs:
</p>
<ul>
 <li>
  http://people.csail.mit.edu/vgod/vim/vim-cheat-sheet-en.png
 </li>
 <li>
  https://cdn.shopify.com/s/files/1/0165/4168/files/preview.png
 </li>
 <li>
  http://www.nathael.org/Data/vi-vim-cheat-sheet.svg
 </li>
 <li>
  http://michael.peopleofhonoronly.com/vim/vim
  <em>
   cheat
  </em>
  sheet
  <em>
   for
  </em>
  programmers_screen.png
 </li>
 <li>
  http://www.rosipov.com/images/posts/vim-movement-commands-cheatsheet.png
 </li>
</ul>
<h2>
 Basics
</h2>
<h4>
 Buffers, windows, tabs?
</h4>
<p>
 Vim is a text editor. Every time text is shown, the text is part of a
 <strong>
  buffer
 </strong>
 . Each file will be opened in its own buffer. Plugins show stuff in
their own buffers etc.
</p>
<p>
 Buffers have many attributes, e.g. whether the text it contains is modifiable,
or whether it is associated with a file and thus needs to be synchronized to
disk on saving.
</p>
<p>
 <strong>
  Windows
 </strong>
 are viewports
 <em>
  onto
 </em>
 buffers. If you want to view several files at
the same time or even different locations of the same file, you use windows.
</p>
<p>
 And please, please don't call them
 <em>
  splits
 </em>
 . You can split a window in two, but
that doesn't make them
 <em>
  splits
 </em>
 .
</p>
<p>
 Windows can be split vertically or horizontally and the heights and widths of
existing windows can be altered, too. Therefore you can use whatever window
layout you prefer.
</p>
<p>
 A
 <strong>
  tab page
 </strong>
 (or just tab) is a collection of windows. Thus, if you want to
use multiple window layouts, use tabs.
</p>
<p>
 Putting it in a nutshell, if you start Vim without arguments, you'll have one
tab page that holds one window that shows one buffer.
</p>
<p>
 By the way, the buffer list is global and you can access any buffer from any
tab.
</p>
<h4>
 Active, loaded, listed, named buffers?
</h4>
<p>
 Run Vim like this
 <code>
  vim file1
 </code>
 . The file's content will be loaded into a buffer.
You have a
 <strong>
  loaded buffer
 </strong>
 now. The content of the buffer is only synchronized
to disk (written back to the file) if you save it within Vim.
</p>
<p>
 Since the buffer is also shown in a window, it's also an
 <strong>
  active buffer
 </strong>
 . Now
if you load another file via
 <code>
  :e file2
 </code>
 ,
 <code>
  file1
 </code>
 will become a
 <strong>
  hidden buffer
 </strong>
 and
 <code>
  file2
 </code>
 the active one.
</p>
<p>
 Both buffers are also
 <strong>
  listed
 </strong>
 , thus they will get listed in the output of
 <code>
  :ls
 </code>
 . Plugin buffers or help buffers are often marked as unlisted, since
they're not regular files you usually edit with a text editor. Listed and
unlisted buffers can be shown via
 <code>
  :ls!
 </code>
 .
</p>
<p>
 <strong>
  Unnamed buffers
 </strong>
 , also often used by plugins, are buffers that don't have an
associated filename. E.g.
 <code>
  :enew
 </code>
 will create an unnamed scratch buffer. Add
some text and write it to disk via
 <code>
  :w /tmp/foo
 </code>
 , and it will become a named
buffer.
</p>
<h4>
 Argument list?
</h4>
<p>
 The
 <a href="#buffers-windows-tabs">
  global buffer list
 </a>
 is a Vim thing. Before that, in
vi, there only used to be the argument list, which is also available in Vim.
</p>
<p>
 Every filename given to Vim on the shell command-line, is remembered in the
argument list. There can be multiple argument lists: by default all arguments
are put into the global argument list, but you can use
 <code>
  :arglocal
 </code>
 to create a
new argument list that is local to the window.
</p>
<p>
 List the current arguments with
 <code>
  :args
 </code>
 . Switch between files from the argument
list with
 <code>
  :next
 </code>
 ,
 <code>
  :previous
 </code>
 ,
 <code>
  :first
 </code>
 ,
 <code>
  :last
 </code>
 and friends. Alter it with
 <code>
  :argadd
 </code>
 ,
 <code>
  :argdelete
 </code>
 or
 <code>
  :args
 </code>
 with a list of files.
</p>
<p>
 If you should prefer using the buffer or argument list for working with files is
a matter of taste. My impression is that most people use the buffer list
exclusively.
</p>
<p>
 Nevertheless there is one huge use case for the argument list: batch processing
via
 <code>
  :argdo
 </code>
 ! A simple refactoring example:
</p>
<p>
 <code>
  vim
:args **/*.[ch]
:argdo %s/foo/bar/ge | update
 </code>
</p>
<p>
 This replaces all occurrences of "foo" by "bar" in all C source and header files
from the current directory and below.
</p>
<p>
 Related help:
 <code>
  :h argument-list
 </code>
</p>
<h4>
 Mappings?
</h4>
<p>
 You can define your own mappings with the
 <code>
  :map
 </code>
 family of commands. Each
command of that family defines a mapping for a certain set of modes. Technically
Vim comes with a whopping 12 modes, 6 of them can be mapped. Additionally, some
commands act on multiple modes at once.
</p>
<p>
 | Recursive | Non-recursive | Unmap     | Modes                            |
|-----------|---------------|-----------|----------------------------------|
|
 <code>
  :map
 </code>
 |
 <code>
  :noremap
 </code>
 |
 <code>
  :unmap
 </code>
 | normal, visual, operator-pending |
|
 <code>
  :nmap
 </code>
 |
 <code>
  :nnoremap
 </code>
 |
 <code>
  :nunmap
 </code>
 | normal                           |
|
 <code>
  :xmap
 </code>
 |
 <code>
  :xnoremap
 </code>
 |
 <code>
  :xunmap
 </code>
 | visual                           |
|
 <code>
  :cmap
 </code>
 |
 <code>
  :cnoremap
 </code>
 |
 <code>
  :cunmap
 </code>
 | command-line                     |
|
 <code>
  :omap
 </code>
 |
 <code>
  :onoremap
 </code>
 |
 <code>
  :ounmap
 </code>
 | operator-pending                 |
|
 <code>
  :imap
 </code>
 |
 <code>
  :inoremap
 </code>
 |
 <code>
  :iunmap
 </code>
 | insert                           |
</p>
<p>
 E.g. this defines the mapping for normal mode only:
</p>
<p>
 <code>
  vim
:nmap <space> :echo "foo"<cr>
 </code>
</p>
<p>
 Unmap it again by using
 <code>
  :nunmap <space>
 </code>
 .
</p>
<p>
 For a few more but rather uncommon modes (or combinations of them), see
 <code>
  :h
map-modes
 </code>
 .
</p>
<p>
 So far, so good. There's only one problem that can be pretty confusing to
beginners:
 <code>
  :nmap
 </code>
 is
 <em>
  recursive
 </em>
 ! That is, the right-hand side takes other
mappings into account.
</p>
<p>
 So you defined a mapping that simply echoes "Foo":
</p>
<p>
 <code>
  vim
:nmap b :echo "Foo"<cr>
 </code>
</p>
<p>
 But what if you want to map the default behavior of
 <code>
  b
 </code>
 (going one word back) to
another key?
</p>
<p>
 <code>
  vim
:nmap a b
 </code>
</p>
<p>
 If you hit
 <kbd>
  a
 </kbd>
 , we expect the cursor to go back a word, but instead
"Foo" is printed in the command-line! Because the right-hand side,
 <code>
  b
 </code>
 , was
mapped to another action already, namely
 <code>
  :echo "Foo"<cr>
 </code>
 .
</p>
<p>
 The proper way to resolve this problem is to use a
 <em>
  non-recursive
 </em>
 mapping
instead:
</p>
<p>
 <code>
  vim
:nnoremap a b
 </code>
</p>
<p>
 Rule of thumb: Always use non-recursive mappings unless recursing is actually
desired.
</p>
<p>
 Look up your mappings by not giving a right-hand side. E.g.
 <code>
  :nmap
 </code>
 shows all
normal mappings and
 <code>
  :nmap <leader>
 </code>
 shows all normal mappings that start with
the mapleader.
</p>
<p>
 If you want to disable a standard mapping, map them to the special
 <code>
  <nop>
 </code>
 character, e.g.
 <code>
  :noremap <left> <nop>
 </code>
 .
</p>
<p>
 Related help:
</p>
<pre><code>:h key-notation
:h mapping
:h 05.3
</code></pre>
<h4>
 Mapleader?
</h4>
<p>
 The mapleader is simply a placeholder than can be used with custom mappings and
is set to
 <code>
  \
 </code>
 by default.
</p>
<p>
 <code>
  vim
nnoremap <leader>h :helpgrep<space>
 </code>
</p>
<p>
 This mapping is triggered by
 <code>
  \h
 </code>
 . If you want to use
 <code>
  <space>h
 </code>
 instead:
</p>
<p>
 <code>
  vim
let mapleader = ' '
nnoremap <leader>h :helpgrep<space>
 </code>
</p>
<p>
 Moreover, there is
 <code>
  <localleader>
 </code>
 that is the local counterpart to
 <code>
  <leader>
 </code>
 and is supposed to be used for mappings that are local to the buffer, eg.
filetype-specific plugins. It also defaults to
 <code>
  \
 </code>
 .
</p>
<p>
 <strong>
  Note
 </strong>
 : Set the mapleaders before mappings! All leader mappings that are in
effect already, won't change just because the mapleader was changed.
 <code>
  :nmap
<leader>
 </code>
 will show all normal mode leader mappings with the mapleader resolved
already, so use it to double-check your mappings.
</p>
<p>
 See
 <code>
  :h mapleader
 </code>
 and
 <code>
  :h maplocalleader
 </code>
 for more.
</p>
<h4>
 Registers?
</h4>
<p>
 Registers are slots that save text. Copying text into a register is called
 <strong>
  yanking
 </strong>
 and extracting text from a register is called
 <strong>
  pasting
 </strong>
 .
</p>
<p>
 Vim provides the following registers:
</p>
<p>
 | Type                | Character              | Filled by? | Readonly? | Contains text from? |
|---------------------|------------------------|------------|-----------|---------------------|
| Unnamed             |
 <code>
  "
 </code>
 | vim        | [ ]       | Last yank or deletion. (
 <code>
  d
 </code>
 ,
 <code>
  c
 </code>
 ,
 <code>
  s
 </code>
 ,
 <code>
  x
 </code>
 ,
 <code>
  y
 </code>
 ) |
| Numbered            |
 <code>
  0
 </code>
 to
 <code>
  9
 </code>
 | vim        | [ ]       | Register
 <code>
  0
 </code>
 : Last yank. Register
 <code>
  1
 </code>
 : Last deletion. Register
 <code>
  2
 </code>
 : Second last deletion. And so on. Think of registers
 <code>
  1
 </code>
 -
 <code>
  9
 </code>
 as a read-only
 <a href="https://en.wikipedia.org/wiki/Queue_(abstract_data_type)">
  queue
 </a>
 with 9 elements. |
| Small delete        |
 <code>
  -
 </code>
 | vim        | [ ]       | Last deletion that was less than one line. |
| Named               |
 <code>
  a
 </code>
 to
 <code>
  z
 </code>
 ,
 <code>
  A
 </code>
 to
 <code>
  Z
 </code>
 | user       | [ ]       | If you yank to register
 <code>
  a
 </code>
 , you replace its text. If you yank to register
 <code>
  A
 </code>
 , you append to the text in register
 <code>
  a
 </code>
 . |
| Read-only           |
 <code>
  :
 </code>
 ,
 <code>
  .
 </code>
 ,
 <code>
  %
 </code>
 | vim        | [x]       |
 <code>
  :
 </code>
 : Last command,
 <code>
  .
 </code>
 : Last inserted text,
 <code>
  %
 </code>
 : Current filename. |
| Alternate buffer    |
 <code>
  #
 </code>
 | vim        | [ ]       | Most of the time the previously visited buffer of the current window. See
 <code>
  :h alternate-file
 </code>
 |
| Expression          |
 <code>
  =
 </code>
 | user       | [ ]       | Evaluation of the VimL expression that was yanked. E.g. do this in insert mode:
 <code>
  <c-r>=5+5<cr>
 </code>
 and "10" will be inserted in the buffer. |
| Selection           |
 <code>
  +
 </code>
 ,
 <code>
  *
 </code>
 | vim        | [ ]       |
 <code>
  *
 </code>
 and
 <code>
  +
 </code>
 are the
 <a href="#clipboard">
  clipboard
 </a>
 registers. |
| Drop                |
 <code>
  ~
 </code>
 | vim        | [x]       | From last drag'n'drop. |
| Black hole          |
 <code>
  _
 </code>
 | vim        | [ ]       | If you don't want any other registers implicitly affected. E.g.
 <code>
  "_dd
 </code>
 deletes the current line without affecting registers
 <code>
  "
 </code>
 ,
 <code>
  1
 </code>
 ,
 <code>
  +
 </code>
 ,
 <code>
  *
 </code>
 . |
| Last search pattern |
 <code>
  /
 </code>
 | vim        | [ ]       | Last pattern used with
 <code>
  /
 </code>
 ,
 <code>
  ?
 </code>
 ,
 <code>
  :global
 </code>
 , etc. |
</p>
<p>
 Each register that is not readonly can be set by the user:
</p>
<p>
 <code>
  vim
:let @/ = 'register'
 </code>
</p>
<p>
 Afterwards
 <kbd>
  n
 </kbd>
 would jump to the next occurrence of "register".
</p>
<p>
 There are numerous exceptions when registers get implicitly filled, so be sure
to read
 <code>
  :h registers
 </code>
 .
</p>
<p>
 Yank with
 <code>
  y
 </code>
 and paste with
 <code>
  p
 </code>
 /
 <code>
  P
 </code>
 , but mind that Vim distinguishes between
characterwise and linewise visual selections. See
 <code>
  :h linewise
 </code>
 .
</p>
<p>
 <strong>
  Example: linewise
 </strong>
</p>
<p>
 <code>
  yy
 </code>
 (or just
 <code>
  Y
 </code>
 ) yanks the current line, move the cursor somewhere else, use
 <code>
  p
 </code>
 to paste below the current line
 <code>
  P
 </code>
 for pasting above it.
</p>
<p>
 <strong>
  Example: charwise
 </strong>
</p>
<p>
 Yank the first word with
 <code>
  0yw
 </code>
 , move somewhere else, paste after the cursor on
the current line with
 <code>
  p
 </code>
 and before the cursor with
 <code>
  P
 </code>
 .
</p>
<p>
 <strong>
  Example: explicit naming of register
 </strong>
</p>
<p>
 <code>
  "aY
 </code>
 yanks the current line into register
 <code>
  a
 </code>
 . Move to another line.
 <code>
  "AY
 </code>
 appends the current line to register
 <code>
  a
 </code>
 .
</p>
<p>
 I suggest playing around with with all these registers a bit and constantly
checking
 <code>
  :reg
 </code>
 , so you can see what's actually happening.
</p>
<p>
 <strong>
  Fun fact
 </strong>
 : In Emacs "yanking" stands for pasting (or
 <em>
  reinserting previously
killed text
 </em>
 ) not copying.
</p>
<h4>
 Ranges?
</h4>
<p>
 Ranges are pretty easy to understand, but many Vimmers don't know about their
full potential.
</p>
<ul>
 <li>
  Many commands take ranges.
 </li>
 <li>
  An address denotes a certain line.
 </li>
 <li>
  A range is either a single address or a pair of addresses separated by either
  <code>
   ,
  </code>
  or
  <code>
   ;
  </code>
  .
 </li>
 <li>
  Ranges tell commands which lines to act on.
 </li>
 <li>
  Most commands act only on the current line by default.
 </li>
 <li>
  Only
  <code>
   :write
  </code>
  and
  <code>
   :global
  </code>
  act on all lines by default.
 </li>
</ul>
<p>
 The usage of ranges is pretty intuitive, so here are some examples (using
 <code>
  :d
 </code>
 as short form of
 <code>
  :delete
 </code>
 ):
</p>
<p>
 | Command | Lines acted on |
|---------|----------------|
|
 <code>
  :d
 </code>
 | Current line. |
|
 <code>
  :.d
 </code>
 | Current line. |
|
 <code>
  :1d
 </code>
 | First line. |
|
 <code>
  :$d
 </code>
 | Last line. |
|
 <code>
  :1,$d
 </code>
 | All lines. |
|
 <code>
  :%d
 </code>
 | All lines (syntactic sugar for
 <code>
  1,$
 </code>
 ). |
|
 <code>
  :.,5d
 </code>
 | Current line to line 5. |
|
 <code>
  :,5d
 </code>
 | Also current line to line 5. |
|
 <code>
  :,+3d
 </code>
 | Current line and the next 3 lines. |
|
 <code>
  :1,+3d
 </code>
 | First line to current line + 3. |
|
 <code>
  :,-3d
 </code>
 | Current line and the last 3 lines. (Vim will prompt you, since this is a reversed range.) |
|
 <code>
  :3,'xdelete
 </code>
 | Lines 3 to the line marked by
 <a href="#marks">
  mark
 </a>
 x. |
|
 <code>
  :/^foo/,$delete
 </code>
 | From the next line that starts with "foo" to the end. |
|
 <code>
  :/^foo/+1,$delete
 </code>
 | From the line after the line that starts with "foo" to the end. |
</p>
<p>
 Note that instead of
 <code>
  ,
 </code>
 ,
 <code>
  ;
 </code>
 can be used as a separator. The difference is that
in the case of
 <code>
  from,to
 </code>
 , the
 <em>
  to
 </em>
 is relative to the current line, but when
using
 <code>
  from;to
 </code>
 , the
 <em>
  to
 </em>
 is relative to the address of
 <em>
  from
 </em>
 ! Assuming you're
on line 5,
 <code>
  :1,+1d
 </code>
 would delete lines 1 to 6, whereas
 <code>
  :1;+1d
 </code>
 would only
delete lines 1 and 2.
</p>
<p>
 The
 <code>
  /
 </code>
 address can be preceded with another address. This allows you to
 <em>
  stack
 </em>
 patterns, e.g.:
</p>
<p>
 <code>
  vim
:/foo//bar//quux/d
 </code>
</p>
<p>
 This would delete the first line containing "quux" after the first line
containing "bar" after the first line containing "foo" after the current line.
</p>
<p>
 Sometimes Vim automatically prepends the command-line with a range. E.g. start a
visual line selection with
 <code>
  V
 </code>
 , select some lines and type
 <code>
  :
 </code>
 . The command-line
will be populated with the range
 <code>
  '<,'>
 </code>
 , which means the following command will
use the previously selected lines as a range. (This is also why you sometimes
see mappings like
 <code>
  :vnoremap foo :<c-u>command
 </code>
 . Here
 <code>
  <c-u>
 </code>
 is used to remove
the range, because Vim will throw an error when giving a range to a command that
doesn't support it.)
</p>
<p>
 Another example is using
 <code>
  !!
 </code>
 in normal mode. This will populate the
command-line with
 <code>
  :.!
 </code>
 . If followed by an external program, that program's
output would replace the current line. So you could replace the current
paragraph with the output of ls by using
 <code>
  :?^$?+1,/^$/-1!ls
 </code>
 . Fancy!
</p>
<p>
 Related help:
</p>
<p>
 <code>
  :h cmdline-ranges
:h 10.3
 </code>
</p>
<h4>
 Marks?
</h4>
<p>
 You use marks to remember a position, that is line number and column, in a file.
</p>
<p>
 | Marks | Set by.. | Usage |
|-------|----------|-------|
|
 <code>
  a
 </code>
 -
 <code>
  z
 </code>
 | User | Local to file, thus only valid within one file. Jumping to a lowercase mark, means jumping within the current file. |
|
 <code>
  A
 </code>
 -
 <code>
  Z
 </code>
 | User | Global, thus valid between files. Also called
 <em>
  file marks
 </em>
 . Jumping to a file mark may switch to another buffer. |
|
 <code>
  0
 </code>
 -
 <code>
  9
 </code>
 | viminfo |
 <code>
  0
 </code>
 is the position when the viminfo file was written last. In practice this means when the last Vim process ended.
 <code>
  1
 </code>
 is the position of when the second last Vim process ended and so on. |
</p>
<p>
 Put
 <code>
  '
 </code>
 /
 <code>
  g'
 </code>
 or
 <code>
  `
 </code>
 /
 <code>
  g`
 </code>
 in front of a mark to form a motion.
</p>
<p>
 Use
 <code>
  mm
 </code>
 to remember the current position with mark "m". Move around the file
and then jump back via
 <code>
  'm
 </code>
 (first non-blank) or
 <code>
  `m
 </code>
 (exact column).
Lowercase marks will be remembered after exiting Vim, if you tell your viminfo
file to do so, see
 <code>
  :h viminfo-'
 </code>
 .
</p>
<p>
 Use
 <code>
  mM
 </code>
 to remember the current position with file mark "M". Switch to another
buffer and switch back via
 <code>
  'M
 </code>
 or
 <code>
  `M
 </code>
 .
</p>
<p>
 Other motions include:
</p>
<p>
 | Motion           | Jump to.. |
|------------------|-----------|
|
 <code>
  '[
 </code>
 ,
 <code>
  `[
 </code>
 | First line or character of previously changed or yanked text. |
|
 <code>
  ']
 </code>
 ,
 <code>
  `]
 </code>
 | Last line or character of previously changed or yanked text. |
|
 <code>
  '<
 </code>
 ,
 <code>
  `<
 </code>
 | Beginning line or character of last visual selection. |
|
 <code>
  '>
 </code>
 ,
 <code>
  `>
 </code>
 | Ending line or character of last visual selection. |
|
 <code>
  ''
 </code>
 ,
 <code>
  ``
 </code>
 | Position before latest jump. |
|
 <code>
  '"
 </code>
 ,
 <code>
  `"
 </code>
 | Position when last exiting the current buffer. |
|
 <code>
  '^
 </code>
 ,
 <code>
  `^
 </code>
 | Position where last insertion stopped. |
|
 <code>
  '.
 </code>
 ,
 <code>
  `.
 </code>
 | Position where last change was made. |
|
 <code>
  '(
 </code>
 ,
 <code>
  `(
 </code>
 | Start of current sentence. |
|
 <code>
  ')
 </code>
 ,
 <code>
  `)
 </code>
 | End of current sentence. |
|
 <code>
  '{
 </code>
 ,
 <code>
  `{
 </code>
 | Start of current paragraph. |
|
 <code>
  '}
 </code>
 ,
 <code>
  `}
 </code>
 | End of current paragraph. |
</p>
<p>
 Marks can also be used in a
 <a href="#ranges">
  range
 </a>
 . You probably saw this before and
wondered what it means: Select some text in visual mode and do
 <code>
  :
 </code>
 , the
command-line will be prepended with
 <code>
  :'<,'>
 </code>
 , which means the following command
would get a range that denotes the visual selection.
</p>
<p>
 Use
 <code>
  :marks
 </code>
 to list all marks. Read everything in
 <code>
  :h mark-motions
 </code>
 .
</p>
<h4>
 Completion?
</h4>
<p>
 Vim provides many different kinds of insert mode completions. If there are
multiple matches, a popup menu will let you navigate to the match of your
choice.
</p>
<p>
 Typical kinds of completion are tags, functions from imported modules or
libraries, file names, dictionary or simply words from the current buffer.
</p>
<p>
 Vim provides a mapping for each kind of completion and they all start with
 <code>
  <c-x>
 </code>
 (remember to use them in insert mode):
</p>
<p>
 | Mapping | Kind | Related help |
|---------|------|--------------|
|
 <code>
  <c-x><c-l>
 </code>
 | whole lines |
 <code>
  :h i^x^l
 </code>
 |
|
 <code>
  <c-x><c-n>
 </code>
 | keywords from current file |
 <code>
  :h i^x^n
 </code>
 |
|
 <code>
  <c-x><c-k>
 </code>
 | keywords from
 <code>
  'dictionary'
 </code>
 option |
 <code>
  :h i^x^k
 </code>
 |
|
 <code>
  <c-x><c-t>
 </code>
 | keywords from
 <code>
  'thesaurus'
 </code>
 option |
 <code>
  :h i^x^t
 </code>
 |
|
 <code>
  <c-x><c-i>
 </code>
 | keywords from current and included files |
 <code>
  :h i^x^i
 </code>
 |
|
 <code>
  <c-x><c-]>
 </code>
 | tags |
 <code>
  :h i^x^]
 </code>
 |
|
 <code>
  <c-x><c-f>
 </code>
 | file names |
 <code>
  :h i^x^f
 </code>
 |
|
 <code>
  <c-x><c-d>
 </code>
 | definitions or macros |
 <code>
  :h i^x^d
 </code>
 |
|
 <code>
  <c-x><c-v>
 </code>
 | Vim commands |
 <code>
  :h i^x^v
 </code>
 |
|
 <code>
  <c-x><c-u>
 </code>
 | user defined (as specified in
 <code>
  'completefunc'
 </code>
 ) |
 <code>
  :h i^x^u
 </code>
 |
|
 <code>
  <c-x><c-o>
 </code>
 | omni completion (as specified in
 <code>
  'omnifunc'
 </code>
 ) |
 <code>
  :h i^x^o
 </code>
 |
|
 <code>
  <c-x>s
 </code>
 | spelling suggestions |
 <code>
  :h i^Xs
 </code>
 |
</p>
<p>
 People might be confused about the difference between user defined completion
and omni completion, but technically they do the same thing. They take a
function that inspects the current position and return a list of suggestions.
User defined completion is defined by the user for their own personal purposes.
(Surprise!) It could be anything. Omni completion is meant for filetype-specific
purposes, like completing struct members or class methods, and is often set by
filetype plugins.
</p>
<p>
 Vim also allows for completing multiple kinds at once by setting the
 <code>
  'complete'
 </code>
 option. By default that option includes quite a lot, so be sure to
trim it to your taste. You can trigger this completion by using either
 <code>
  <c-n>
 </code>
 (next) and
 <code>
  <c-p>
 </code>
 (previous), which also happen to be the keys used for
choosing entries in the popup menu. See
 <code>
  :h i^n
 </code>
 and
 <code>
  :h 'complete'
 </code>
 for more on
this.
</p>
<p>
 Be sure to check out
 <code>
  :h 'completeopt'
 </code>
 for configuring the behaviour of the
popup menu. The default is quite sane, but I prefer adding "noselect" as well.
</p>
<p>
 Related help:
</p>
<p>
 <code>
  :h ins-completion
:h popupmenu-keys
:h new-omni-completion
 </code>
</p>
<h4>
 Motions? Operators? Text objects?
</h4>
<p>
 <strong>
  Motions
 </strong>
 move the cursor. You all know
 <code>
  h
 </code>
 /
 <code>
  j
 </code>
 /
 <code>
  k
 </code>
 /
 <code>
  l
 </code>
 . Or
 <code>
  w
 </code>
 and
 <code>
  b
 </code>
 . Even
 <code>
  /
 </code>
 is a motion. They also take a count.
 <code>
  2?the<cr>
 </code>
 jumps to the second last
occurrence of "the".
</p>
<p>
 See
 <code>
  :h navigation
 </code>
 and everything below for all available motions.
</p>
<p>
 <strong>
  Operators
 </strong>
 act on a region of text, e.g.
 <code>
  d
 </code>
 ,
 <code>
  ~
 </code>
 ,
 <code>
  gU
 </code>
 ,
 <code>
  >
 </code>
 to name just a
few. They get used in two contexts, either in normal or visual mode. In normal
mode, operators come first followed by a motion, e.g.
 <code>
  >j
 </code>
 . In visual mode,
operators simply act on the selection, e.g.
 <code>
  Vjd
 </code>
 .
</p>
<p>
 Like motions, operators take a count, e.g.
 <code>
  2gUw
 </code>
 makes the rest of the current
word and the next one uppercase. Since motions and operators take counts,
 <code>
  2gU2w
 </code>
 works just as well and executes
 <code>
  gU2w
 </code>
 twice.
</p>
<p>
 See
 <code>
  :h operator
 </code>
 for all available operators. Use
 <code>
  :set tildeop
 </code>
 to make
 <code>
  ~
 </code>
 act as an operator.
</p>
<p>
 <strong>
  Text objects
 </strong>
 act on the surrounding area, opposed to motions that act into
one direction. Actually they work on objects, e.g. a whole word, a whole
sentence, everything between parentheses, and so on.
</p>
<p>
 Text objects can't be used to move the cursor in normal mode, because even the
most-skilled cursors can't jump into two directions at the same time. It works
in visual mode though, because then one side of the object is already selected
and the cursor simply jumps to the other side.
</p>
<p>
 Text objects start with either
 <code>
  i
 </code>
 (think
 <em>
  inner
 </em>
 ) or
 <code>
  a
 </code>
 (think
 <em>
  around
 </em>
 )
followed by a character denoting the object. With
 <code>
  i
 </code>
 it only acts on the object
itself, with
 <code>
  a
 </code>
 on the object plus trailing whitespace. E.g.
 <code>
  diw
 </code>
 deletes the
current word and
 <code>
  ci(
 </code>
 changes everything between parentheses.
</p>
<p>
 Text objects take a count. Imagine
 <code>
  ((( )))
 </code>
 and the cursor on or between the
most inner parentheses, then
 <code>
  d2a(
 </code>
 will remove the 2 inner pairs of parentheses
and everything in between.
</p>
<p>
 See
 <code>
  :h text-objects
 </code>
 for all available text objects.
</p>
<h4>
 Autocmds?
</h4>
<p>
 On many occasions, Vim emits events. You hook into these events by using
autocmds.
</p>
<p>
 You wouldn't use Vim if there weren't autocmds. They're used all the time, even
if you don't even know it. Don't believe me? Check
 <code>
  :au
 </code>
 , but don't let the
output overwhelm you. These are all the autocmds that are in effect right now!
</p>
<p>
 See
 <code>
  :h {event}
 </code>
 for a quick overview of all available events and
 <code>
  :h
autocmd-events-abc
 </code>
 for more details.
</p>
<p>
 A typical example would be setting filetype-specific settings:
</p>
<p>
 <code>
  vim
autocmd FileType ruby setlocal shiftwidth=2 softtabstop=2 comments-=:#
 </code>
</p>
<p>
 But how does a buffer even know that it contains Ruby code? Because another
autocmd detected it as that and set the filetype accordingly which again
triggered the
 <code>
  FileType
 </code>
 event.
</p>
<p>
 One of the first things everyone adds to his vimrc is
 <code>
  filetype on
 </code>
 . This simply
means that
 <code>
  filetype.vim
 </code>
 is read at startup which sets autocmds for almost all
filetypes under the sun.
</p>
<p>
 If you're brave enough, have a look at it:
 <code>
  :e $VIMRUNTIME/filetype.vim
 </code>
 . Search
for "Ruby" and you'll find that Vim simply uses the file extension
 <code>
  .rb
 </code>
 to
detect Ruby files:
</p>
<p>
 <strong>
  NOTE
 </strong>
 : Autocmds of the same event are executed in the order they were
created.
 <code>
  :au
 </code>
 shows them in the correct order.
</p>
<p>
 <code>
  vim
au BufNewFile,BufRead *.rb,*.rbw  setf ruby
 </code>
</p>
<p>
 The
 <code>
  BufNewFile
 </code>
 and
 <code>
  BufRead
 </code>
 events in this case are hardcoded in the C
sources of Vim and get emitted everytime you open a file via
 <code>
  :e
 </code>
 and similar
commands. Afterwards all the hundreds of filetypes from
 <code>
  filetype.vim
 </code>
 are
tested for.
</p>
<p>
 Putting it in a nutshell, Vim makes heavy use of events and autocmds but also
exposes a clean interface to hook into that event-driven system for
customization.
</p>
<h4>
 Changelist? Jumplist?
</h4>
<p>
 The positions of the last 100 changes are kept in the
 <strong>
  changelist
 </strong>
 . Several
small changes on the same line will be merged together, but the position will be
that of the last change nevertheless (in case you added something in the middle
of the line).
</p>
<p>
 Every time you jump, the position
 <em>
  before
 </em>
 the jump is remembered in the
 <strong>
  jumplist
 </strong>
 . A jumplist has up to 100 entries. Each window has its own
jumplist. When you split a window, the jumplist is copied.
</p>
<p>
 A jump is one of the following commands:
 <code>
  '
 </code>
 ,
 <code>
  `
 </code>
 ,
 <code>
  G
 </code>
 ,
 <code>
  /
 </code>
 ,
 <code>
  ?
 </code>
 ,
 <code>
  n
 </code>
 ,
 <code>
  N
 </code>
 ,
 <code>
  %
 </code>
 ,
 <code>
  (
 </code>
 ,
 <code>
  )
 </code>
 ,
 <code>
  [[
 </code>
 ,
 <code>
  ]]
 </code>
 ,
 <code>
  {
 </code>
 ,
 <code>
  }
 </code>
 ,
 <code>
  :s
 </code>
 ,
 <code>
  :tag
 </code>
 ,
 <code>
  L
 </code>
 ,
 <code>
  M
 </code>
 ,
 <code>
  H
 </code>
 and commands
that start editing a new file.
</p>
<p>
 | List       | List all entries | Go to older position | Go to newer position |
|------------|------------------|----------------------|----------------------|
| jumplist   |
 <code>
  :jumps
 </code>
 |
 <code>
  [count]<c-o>
 </code>
 |
 <code>
  [count]<c-i>
 </code>
 |
| changelist |
 <code>
  :changes
 </code>
 |
 <code>
  [count]g;
 </code>
 |
 <code>
  [count]g,
 </code>
 |
</p>
<p>
 When you list all entries, a marker
 <code>
  >
 </code>
 will be used to show the current
position. Usually that will be below position 1, the latest position.
</p>
<p>
 If you want both lists to persist after restarting Vim, you need to use the
viminfo file and
 <code>
  :h viminfo-'
 </code>
 .
</p>
<p>
 <strong>
  NOTE
 </strong>
 : The position before the latest jump is also kept as a
 <a href="#marks">
  mark
 </a>
 and can be jumped to via
 <code>
  ``
 </code>
 or
 <code>
  ''
 </code>
 .
</p>
<p>
 Related help:
</p>
<p>
 <code>
  :h changelist
:h jumplist
 </code>
</p>
<h4>
 Undo tree?
</h4>
<p>
 The latest changes to the text state are remembered. You can use
 <em>
  undo
 </em>
 to
revert changes and
 <em>
  redo
 </em>
 to reapply previously reverted changes.
</p>
<p>
 The important bit to understand it that the data structure holding recent
changes is not a
 <a href="https://en.wikipedia.org/wiki/Queue_(abstract_data_type)">
  queue
 </a>
 but a
 <a href="https://en.wikipedia.org/wiki/Tree_(data_structure)">
  tree
 </a>
 ! Your changes are
nodes in the tree and each (but the top node) has a parent node. Each node keeps
information about the changed text and time. A branch is a series of nodes that
starts from any node and goes up to the top node. New branches get created when
you undo a change and then insert something else.
</p>
<p>
 <code>
  ifoo<esc>
obar<esc>
obaz<esc>
u
oquux<esc>
 </code>
</p>
<p>
 Now you have 3 lines and the undo tree looks like this:
</p>
<p>
 <code>
  foo(1)
       /
    bar(2)
   /      \
baz(3)   quux(4)
 </code>
</p>
<p>
 The undo tree has 4 changes. The numbers represent the
 <em>
  time
 </em>
 the nodes were
created.
</p>
<p>
 Now there are two ways to traverse this tree, let's call them
 <em>
  branch-wise
 </em>
 and
 <em>
  time-wise
 </em>
 .
</p>
<p>
 Undo (
 <code>
  u
 </code>
 ) and redo (
 <code>
  <c-r>
 </code>
 ) work branch-wise. They go up and down the current
branch.
 <code>
  u
 </code>
 will revert the text state to the one of node "bar". Another
 <code>
  u
 </code>
 will revert the text state even further, to the one of node "foo". Now
 <code>
  <c-r>
 </code>
 goes back to the state of node "bar" and another
 <code>
  <c-r>
 </code>
 to the state of node
"quux". (There's no way to reach node "baz" using branch-wise commands anymore.)
</p>
<p>
 Opposed to this,
 <code>
  g-
 </code>
 and
 <code>
  g+
 </code>
 work time-wise. Thus
 <code>
  g-
 </code>
 won't revert to the
state of node "bar", like
 <code>
  u
 </code>
 does, but to the chronologically previous state,
node "baz". Another
 <code>
  g-
 </code>
 would revert the state to the one of node "bar" and so
on. Thus,
 <code>
  g-
 </code>
 and
 <code>
  g+
 </code>
 simply go back and forth in time, respectively.
</p>
<p>
 | Command / Mapping | Action |
|-------------------|--------|
|
 <code>
  [count]u
 </code>
 ,
 <code>
  :undo [count]
 </code>
 | Undo [count] changes. |
|
 <code>
  [count]<c-r>
 </code>
 ,
 <code>
  :redo
 </code>
 | Redo [count] changes. |
|
 <code>
  U
 </code>
 | Undo all all changes to the line of the latest change. |
|
 <code>
  [count]g-
 </code>
 ,
 <code>
  :earlier [count]?
 </code>
 | Go to older text state [count] times. The "?" can be either "s", "m", "h", "d", or "f". E.g.
 <code>
  :earlier 2d
 </code>
 goes to the text state from 2 days ago.
 <code>
  :earlier 1f
 </code>
 will go to the state of the latest file save. |
|
 <code>
  [count]g+
 </code>
 ,
 <code>
  :later [count]?
 </code>
 | Same as as above, but other direction. |
</p>
<p>
 The undo tree is kept in memory and will be lost when Vim quits. See
 <a href="#handling-backup-swap-undo-and-viminfo-files">
  Handling
backup, swap, undo, and viminfo
files
 </a>
 for how to enable
persistent undo.
</p>
<p>
 If you're confused by the undo tree,
 <a href="https://github.com/mbbill/undotree">
  undotree
 </a>
 does a great job at visualizing
it.
</p>
<p>
 Related help:
</p>
<p>
 <code>
  :h undo.txt
:h usr_32
 </code>
</p>
<h4>
 Quickfix and location lists?
</h4>
<p>
 Every time an action has to return a list of locations,
 <em>
  quickfix
 </em>
 or
 <em>
  location
 </em>
 lists can be used. In this case a location is a file, a line number and
optionally a column.
</p>
<p>
 Examples are compiler errors assembled in a quickfix list or matches of an
external grep tool assembled in a location list.
</p>
<p>
 The big advantage over just putting that stuff in an empty buffer is that you
get a nice uniform interface for browsing the entries.
</p>
<p>
 At all time there's only one quickfix list, but every window can has its own
location list. Both type of lists
 <em>
  feel
 </em>
 the same, but use slightly different
commands for navigation.
</p>
<p>
 Most common commands:
</p>
<p>
 | Action         | Quickfix     | Location     |
|----------------|--------------|--------------|
| open window    |
 <code>
  :copen
 </code>
 |
 <code>
  :lopen
 </code>
 |
| close window   |
 <code>
  :cclose
 </code>
 |
 <code>
  :lclose
 </code>
 |
| next entry     |
 <code>
  :cnext
 </code>
 |
 <code>
  :lnext
 </code>
 |
| previous entry |
 <code>
  :cprevious
 </code>
 |
 <code>
  :lprevious
 </code>
 |
| first entry    |
 <code>
  :cfirst
 </code>
 |
 <code>
  :lfirst
 </code>
 |
| last entry     |
 <code>
  :clast
 </code>
 |
 <code>
  :llast
 </code>
 |
</p>
<p>
 See
 <code>
  :cc
 </code>
 and everything below for all commands.
</p>
<p>
 <strong>
  Example
 </strong>
 :
</p>
<p>
 Let's use our good old friend
 <code>
  grep
 </code>
 for searching the files in the current
directory recursively for a certain query and put the results in the quickfix
list.
</p>
<p>
 <code>
  vim
:let &grepprg = 'grep -Rn $* .'
:grep! foo
<grep output - hit enter>
:copen
 </code>
</p>
<p>
 Assuming any files contained the string "foo", it should be shown now in the
quickfix window.
</p>
<h4>
 Macros?
</h4>
<p>
 Vim allows
 <em>
  recording
 </em>
 typed characters into a
 <a href="#registers">
  register
 </a>
 . It's a
great way to automate certain tasks on the fly. (For more elaborate tasks,
 <a href="#vim-scripting">
  Vim
scripting
 </a>
 should be used instead.)
</p>
<ul>
 <li>
  Start recording by typing
  <code>
   q
  </code>
  followed by the register, e.g.
  <code>
   q
  </code>
  . (The
command-line will signify this via "recording @q".)
 </li>
 <li>
  Stop recording by hitting
  <code>
   q
  </code>
  once again.
 </li>
 <li>
  Execute the macro via
  <code>
   [count]@q
  </code>
  .
 </li>
 <li>
  Repeat the last used macro via
  <code>
   [count]@@
  </code>
  .
 </li>
</ul>
<p>
 <strong>
  Example 1:
 </strong>
</p>
<p>
 Insert a line and repeat it 10 times:
</p>
<p>
 <code>
  qq
iabc<cr><esc>
q
10@q
 </code>
</p>
<p>
 (The same could be done without macros:
 <code>
  oabc<esc>10.
 </code>
 )
</p>
<p>
 <strong>
  Example 2:
 </strong>
</p>
<p>
 For adding line numbers in front of all lines, start on the first line and add
"1. " to it manually. Increment the number under the cursor by using
 <code>
  <c-a>
 </code>
 ,
displayed as
 <code>
  ^A
 </code>
 .
</p>
<p>
 <code>
  qq
0yf jP0^A
q
1000@q
 </code>
</p>
<p>
 Here we simply hope that the file doesn't contain more than 1000 lines when
using
 <code>
  1000@q
 </code>
 , but we can also use a
 <em>
  recursive macro
 </em>
 , which executes until
the macro can't be applied to a line anymore:
</p>
<p>
 <code>
  qq
0yf jP0^A@q
q
@q
 </code>
</p>
<p>
 (The same could be done without macros:
 <code>
  :%s/^/\=line('.') . '. '
 </code>
 )
</p>
<p>
 Mind that I also show how to achieve the same without using macros, but this
mostly works only for such simple examples. For more complex automation, macros
are the bomb!
</p>
<p>
 Also see:
 <a href="#quickly-edit-your-macros">
  Quickly edit your macros
 </a>
</p>
<p>
 Related help:
</p>
<p>
 <code>
  :h recording
:h 'lazyredraw'
 </code>
</p>
<h4>
 Colorschemes?
</h4>
<p>
 Colorschemes are the way to style your Vim. Vim consists of many components and
each of those can be customized with different colors for the foreground,
background and a few other attributes like bold text etc. They can be set like
this:
</p>
<p>
 <code>
  vim
:highlight Normal ctermbg=1 guibg=red
 </code>
</p>
<p>
 This would paint the background of the editor red. See
 <code>
  :h :highlight
 </code>
 for more
information.
</p>
<p>
 So, colorschemes are mostly a collection of
 <code>
  :highlight
 </code>
 commands.
</p>
<p>
 Actually, most colorschemes are really 2 colorschemes! The example above sets
colors via
 <code>
  ctermbg
 </code>
 and
 <code>
  guibg
 </code>
 . The former definition will only be used if Vim
was started in a terminal emulator, e.g. xterm. The latter will be used in
graphical environments like gVim.
</p>
<p>
 If you ever happen to use a certain colorscheme in Vim running in a terminal
emulator and the colors don't look like the colors in the screenshot at all,
chances are that the colorscheme only defined colors for the GUI.
</p>
<p>
 I use
 <a href="https://github.com/morhetz/gruvbox">
  gruvbox
 </a>
 for the GUI and
 <a href="https://github.com/mhinz/vim-janah">
  janah
 </a>
 for the terminal.
</p>
<p>
 More colorschemes:
 <a href="#list-of-colorschemes-1">
  here
 </a>
</p>
<h4>
 Folding?
</h4>
<p>
 Every text (or source code) has a certain structure. If you have a structure, it
means you have regions of logically separated text. Folding allows to "fold"
such a region into a single line and displaying a short description. There are
many commands that act on these regions called
 <em>
  folds
 </em>
 . Folds can be nested.
</p>
<p>
 Vim distinguishes between several types of fold methods:
</p>
<p>
 | 'foldmethod' | Usage |
|--------------|-------|
| diff         | Used in diff windows to fold unchanged text. |
| expr         | Uses
 <code>
  'foldexpr'
 </code>
 to basically create a new fold method. |
| indent       | Folds based on indentation. |
| manual       | Create folds yourself via
 <code>
  zf
 </code>
 ,
 <code>
  zF
 </code>
 , and
 <code>
  :fold
 </code>
 . |
| marker       | Folds based on markers in the text (often in comments). |
| syntax       | Folds based on syntax, e.g. folding
 <code>
  if
 </code>
 blocks. |
</p>
<p>
 <strong>
  NOTE
 </strong>
 : Folding can be computationally intensive! If you experience any
performance drawbacks (small delays when typing), have a look at
 <a href="https://github.com/Konfekt/FastFold">
  FastFold
 </a>
 , which prevents Vim from
updating folds when it's not needed.
</p>
<p>
 Related help:
</p>
<p>
 <code>
  :h usr_28
:h folds
 </code>
</p>
<h4>
 Sessions?
</h4>
<p>
 If you save a
 <strong>
  view
 </strong>
 (
 <code>
  :h :mkview
 </code>
 ), the current state of the window (and
options and mappings) gets saved for later use (
 <code>
  :h :loadview
 </code>
 ).
</p>
<p>
 A
 <strong>
  session
 </strong>
 saves the views of all windows plus global settings. It basically
makes a snapshot of your current Vim instance and saves it in a session file.
Let me stress this: it saves the current state; everything done after saving a
session won't be part of the session file. To "update" a session, simply write
it out again.
</p>
<p>
 This makes it perfect for saving your
 <em>
  projects
 </em>
 and easy to switch between
them.
</p>
<p>
 Try it right now! Open a few windows and tabs and do
 <code>
  :mksession Foo.vim
 </code>
 . If
you omit the filename,
 <code>
  Session.vim
 </code>
 will be assumed. The file will be saved to
the current working directory, check
 <code>
  :pwd
 </code>
 . Restart Vim and do
 <code>
  :source
Foo.vim
 </code>
 and voilà, the buffer list, window layout, mappings, working directory
etc. should all be the same as before you saved the session. Do some more work
and update the session by overwriting the already existing session file with
 <code>
  :mksession! Foo.vim
 </code>
 .
</p>
<p>
 Note that a session file is really just a collection of Vim commands that are
supposed to restore a certain state of a Vim instance, so feel free to take a
look at it:
 <code>
  :vs Foo.vim
 </code>
 .
</p>
<p>
 You can tell Vim what things to save in a session by setting
 <code>
  'sessionoptions'
 </code>
 .
</p>
<p>
 For scripting purposes Vim keeps the name of the last sourced or written session
in the internal variable
 <code>
  v:this_session
 </code>
 .
</p>
<p>
 Related help:
</p>
<p>
 <code>
  :h Session
:h 'sessionoptions'
:h v:this_session
 </code>
</p>
<h4>
 Locality?
</h4>
<p>
 Many of the concepts mentioned above also have
 <em>
  local
 </em>
 counterparts:
</p>
<p>
 | Global | Local | Scope | Help |
|--------|-------|-------|------|
|
 <code>
  :set
 </code>
 |
 <code>
  :setlocal
 </code>
 | buffer or window |
 <code>
  :h local-options
 </code>
 |
|
 <code>
  :map
 </code>
 |
 <code>
  :map <buffer>
 </code>
 | buffer           |
 <code>
  :h :map-local
 </code>
 |
|
 <code>
  :autocmd
 </code>
 |
 <code>
  :autocmd * <buffer>
 </code>
 | buffer           |
 <code>
  :h autocmd-buflocal
 </code>
 |
|
 <code>
  :cd
 </code>
 |
 <code>
  :lcd
 </code>
 | window           |
 <code>
  :h :lcd
 </code>
 |
|
 <code>
  <leader>
 </code>
 |
 <code>
  <localleader>
 </code>
 | buffer           |
 <code>
  :h maplocalleader
 </code>
 |
</p>
<p>
 Variables also sport different scopes, but will be explained in
 <a href="#vim-scripting">
  Vim scripting
 </a>
 .
</p>
<h2>
 Usage
</h2>
<h4>
 Getting help offline
</h4>
<p>
 Vim comes with great documentation in the form of single text files with a
special layout. Vim uses a system based on tags for accessing certain parts of
those help files.
</p>
<p>
 First of all, read this:
 <code>
  :help :help
 </code>
 . This will open the file
 <code>
  $VIMRUNTIME/doc/helphelp.txt
 </code>
 in a new window and jump to the
 <code>
  :help
 </code>
 tag
within that file.
</p>
<p>
 A few simple rules:
</p>
<ul>
 <li>
  options are enclosed in single quotes, e.g.
  <code>
   :h 'textwidth'
  </code>
 </li>
 <li>
  VimL functions end in (), e.g.
  <code>
   :h reverse()
  </code>
 </li>
 <li>
  commands start with :, e.g.
  <code>
   :h :echo
  </code>
 </li>
</ul>
<p>
 You can use
 <code>
  <c-d>
 </code>
 (this is
 <kbd>
  ctrl
 </kbd>
 +
 <kbd>
  d
 </kbd>
 ) to list all tags that
match the currently entered query. E.g.
 <code>
  :h tab<c-d>
 </code>
 will get you a list of all
tags from
 <code>
  tab
 </code>
 over
 <code>
  'softtabstop'
 </code>
 to
 <code>
  setting-guitablabel
 </code>
 .
</p>
<p>
 You want to list all VimL functions? Simple:
 <code>
  :h ()<c-d>
 </code>
 . You want to list all
VimL functions that concern windows?
 <code>
  :h win*()<c-d>
 </code>
 .
</p>
<p>
 This quickly becomes second nature, but especially in the beginning, you
sometimes don't know any part of the tag you are looking for. You can only
imagine some keywords that could be involved.
 <code>
  :helpgrep
 </code>
 to the rescue!
</p>
<p>
 <code>
  :helpgrep backwards
 </code>
</p>
<p>
 This will look for "backwards" in all documentation files and jump to the first
match. The matches will be assembled in the quickfix list. Use
 <code>
  :cn
 </code>
 /
 <code>
  :cp
 </code>
 to
jump to the next/previous match. Or use
 <code>
  :copen
 </code>
 to open the quickfix window,
navigate to an entry and hit
 <code>
  <cr>
 </code>
 to jump to that match. See
 <code>
  :h quickfix
 </code>
 for
the whole truth.
</p>
<h4>
 Getting help offline (alternative)
</h4>
<p>
 This list was compiled by @chrisbra, one of the most active Vim developers, and
posted to
 <a href="https://groups.google.com/forum/#!forum/vim_dev">
  vim_dev
 </a>
 .
</p>
<p>
 It's reposted here with minor changes.
</p>
<hr/>
<p>
 If you know what you are looking for, it is usually easier to search for it
using the help system. Because the subjects follow a certain style guide.
</p>
<p>
 Also the help has the advantage of belonging to your particular Vim version, so
that obsolete topics or topics that have been added later won't turn up.
</p>
<p>
 Therefore, it is essential to learn the help system and the language it uses.
Here are some examples (not necessarily complete and I might have forgotten
something).
</p>
<ol>
 <li>
  <p>
   Options are enclosed in single quotes. So you would use
   <code>
    :h 'list'
   </code>
   to go to
the help topic for the list option. If you only know, you are looking for a
certain option, you can also do
   <code>
    :h options.txt
   </code>
   to open the help page which
describes all option handling and then you can search using regular
expressions e.g.
   <code>
    /width
   </code>
   . Certain options have their own namespace, e.g.
   <code>
    :h
cpo-a
   </code>
   ,
   <code>
    :h cpo-A
   </code>
   ,
   <code>
    :h cpo-b
   </code>
   , and so on.
  </p>
 </li>
 <li>
  <p>
   Normal mode commands are just that. Use
   <code>
    :h gt
   </code>
   to go to the help page for
the "gt" command.
  </p>
 </li>
 <li>
  <p>
   Regexp items always start with "/", so
   <code>
    :h /\+
   </code>
   takes you to the help item
for the "+" quantifier in Vim regexes. If you need to know anything about
regular expressions, start reading at
   <code>
    :h pattern.txt
   </code>
   .
  </p>
 </li>
 <li>
  <p>
   Key combinations. They usually start with a single letter indicating the mode
for which they can be used. E.g.
   <code>
    :h i_CTRL-X
   </code>
   takes you to the family of
CTRL-X commands for insert mode which can be used to auto complete different
things. Note that certain keys will always be written the same, e.g. Control
will always be CTRL. Note, for normal mode commands, the "n" is left away,
e.g.
   <code>
    :h CTRL-A
   </code>
   . In contrast
   <code>
    :h c_CTRL-R
   </code>
   will describe what CTRL-R does
when entering commands in the command line and
   <code>
    :h v_Ctrl-A
   </code>
   talks about
incrementing numbers in visual mode and
   <code>
    :h g_CTRL-A
   </code>
   talks about the g
   <c-a>
    command (thus you have to press "g" then
    <ctrl-a>
     ). Here the "g" stand for
the normal command "g" which always expect a second key before doing
something similar to the commands starting with "z".
    </ctrl-a>
   </c-a>
  </p>
 </li>
 <li>
  <p>
   Registers always start with "quote" so use
   <code>
    :h quote
   </code>
   to find out about the
special ":" register.
  </p>
 </li>
 <li>
  <p>
   Vim script (VimL) is available at
   <code>
    :h eval.txt
   </code>
   . Certain aspects of the
language are available at
   <code>
    :h expr-X
   </code>
   where 'X' is a single letter, e.g.
   <code>
    :h
expr-!
   </code>
   will take you to the topic describing the '!' (Not) operator for
VimL. Also important, see
   <code>
    :h function-list
   </code>
   to find a short description of
all functions available.
  </p>
 </li>
 <li>
  <p>
   Mappings are talked about in the help page
   <code>
    :h map.txt
   </code>
   . Use
   <code>
    :h mapmode-i
   </code>
   to find out about the
   <code>
    :imap
   </code>
   command. Also use
   <code>
    :map-topic
   </code>
   to find out
about certain subtopics particular for mappings (e.g.
   <code>
    :h :map-local
   </code>
   for
buffer-local mappings or
   <code>
    :h map_bar
   </code>
   for how the '|' is handled in mappings.
  </p>
 </li>
 <li>
  <p>
   Command definitions are talked about at
   <code>
    :h command-*
   </code>
   , so use :h command-bar
to find out about the '!' argument for custom commands.
  </p>
 </li>
 <li>
  <p>
   Window management commands always start with CTRL-W, so you find the
corresponding help at
   <code>
    :h CTRL-W_*
   </code>
   (e.g.
   <code>
    :h CTRL-W_p
   </code>
   for switch to the
previously accessed window). You can also access
   <code>
    :h windows.txt
   </code>
   and read
your way through, if you are looking for window handling command.
  </p>
 </li>
 <li>
  <p>
   Ex commands always start with ":", so
   <code>
    :h :s
   </code>
   covers the ":s" command.
  </p>
 </li>
 <li>
  <p>
   Use CTRL-D after typing a topic and let Vim try to complete to all available
topics.
  </p>
 </li>
 <li>
  <p>
   Use
   <code>
    :helpgrep
   </code>
   to search in all help pages (usually also includes help
pages by installed plugins). See
   <code>
    :h :helpgrep
   </code>
   for how to use it. Once you
have searched for a topic, all matches are available in the quickfix (or
location) window which can be opened with
   <code>
    :copen
   </code>
   or
   <code>
    :lopen
   </code>
   . There you
can also use
   <code>
    /
   </code>
   to further filter the matches.
  </p>
 </li>
 <li>
  <p>
   <code>
    :h helphelp
   </code>
   contains some information on how to use the help.
  </p>
 </li>
 <li>
  <p>
   The user manual. This describes help topics for beginners in a rather
friendly way. Start at
   <code>
    :h usr_toc.txt
   </code>
   to find the table of content (as you
might have guessed). Skimming over that help finding certain topics, .e.g
you will find an entry "Digraphs" and "Entering special characters" in
chapter 24 (so use
   <code>
    :h usr_24.txt
   </code>
   to go to that particular help page).
  </p>
 </li>
 <li>
  <p>
   Highlighting groups always start with
   <code>
    hl-*
   </code>
   . E.g.
   <code>
    :h hl-WarningMsg
   </code>
   talks
about the "WarningMsg" highlighting group.
  </p>
 </li>
 <li>
  <p>
   Syntax highlighting is namespaced to ":syn-topic", e.g.
   <code>
    :h :syn-conceal
   </code>
   talks about the conceal argument for the :syn command.
  </p>
 </li>
 <li>
  <p>
   Quickfix commands usually start with ":c", while location list commands
usually start with ":l".
  </p>
 </li>
 <li>
  <p>
   <code>
    :h BufWinLeave
   </code>
   talks about the BufWinLeave autocmd. Also
   <code>
    :h
autocommands-events
   </code>
   talks about all possible events.
  </p>
 </li>
 <li>
  <p>
   Startup arguments always start with "-", so
   <code>
    :h -f
   </code>
   takes you to the help of
the "-f" command switch of Vim.
  </p>
 </li>
 <li>
  <p>
   Compiled extra features always start with "+", so
   <code>
    :h +conceal
   </code>
   talks about
the conceal support.
  </p>
 </li>
 <li>
  <p>
   Error codes can be looked up directly in the help.
   <code>
    :h E297
   </code>
   takes you
exactly to the description of the error message. Sometimes however, those
error codes are not described, but rather are listed at the Vim command that
usually causes this. E.g.
   <code>
    :h hE128
   </code>
   takes you directly to the
   <code>
    :function
   </code>
   command.
  </p>
 </li>
 <li>
  <p>
   Documentation for included syntax files is usually available at
   <code>
    :h
ft-*-syntax
   </code>
   . E.g.
   <code>
    :h ft-c-syntax
   </code>
   talks about the C syntax file and the
options it provides. Sometimes, additional sections for omni completion (
   <code>
    :h
ft-php-omni
   </code>
   ) or filetype plugins (
   <code>
    :h ft-tex-plugin
   </code>
   ) are available.
  </p>
 </li>
</ol>
<p>
 Also a link to the user documentation (which describes certain commands more
from a user perspective and less detailed) will be mentioned at the top of help
pages if they are available. So
 <code>
  :h pattern.txt
 </code>
 mentions the user guide topics
 <code>
  :h 03.9
 </code>
 and
 <code>
  :h usr_27
 </code>
 .
</p>
<h4>
 Getting help online
</h4>
<p>
 If you have an issue you can't resolve or are in need of general guidance, see
the
 <a href="https://groups.google.com/forum/#!forum/vim_use">
  vim_use
 </a>
 mailing list.
Another great resource is using
 <a href="https://de.wikipedia.org/wiki/Internet_Relay_Chat">
  IRC
 </a>
 . The channel
 <code>
  #vim
 </code>
 on
 <a href="https://freenode.net">
  Freenode
 </a>
 is huge and usually full of helpful people.
</p>
<p>
 If you want to report a Vim bug, use the
 <a href="https://groups.google.com/forum/#!forum/vim_dev">
  vim_dev
 </a>
 mailing list.
</p>
<h4>
 Clipboard
</h4>
<p>
 Required
 <a href="#what-kind-of-vim-am-i-running">
  features
 </a>
 :
 <code>
  +clipboard
 </code>
 and optionally
 <code>
  +xterm_clipboard
 </code>
 if you want to use the
 <code>
  'clipboard'
 </code>
 option on a Unix system
with a Vim that doesn't have GUI support.
</p>
<p>
 Related help:
</p>
<p>
 <code>
  :h 'clipboard'
:h gui-clipboard
:h gui-selections
 </code>
</p>
<p>
 Also see:
 <a href="#bracketed-paste-or-why-do-i-have-to-set-paste-all-the-time">
  Bracketed paste (or why do I have to set 'paste' all the
time?)
 </a>
</p>
<h5>
 Clipboard usage (Windows, OSX)
</h5>
<p>
 Windows comes with a
 <a href="https://msdn.microsoft.com/en-us/library/windows/desktop/ms649012(v=vs.85).aspx">
  clipboard
 </a>
 and OSX comes with a
 <a href="https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/PasteboardGuide106/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008100-SW1">
  pasteboard
 </a>
 .
</p>
<p>
 Both work like most users would expect them to work. You copy selected text with
 <code>
  ctrl+c
 </code>
 /
 <code>
  cmd+c
 </code>
 and paste them in another application with
 <code>
  ctrl+v
 </code>
 /
 <code>
  cmd+v
 </code>
 .
</p>
<p>
 Note that copied text is actually transferred to the clipboard, so you can close
the application you copied from before pasting in another application without
problems.
</p>
<p>
 Whenever this happens, the clipboard register
 <code>
  *
 </code>
 gets filled with the
selection. From Vim use
 <code>
  "*y
 </code>
 and
 <code>
  "*p
 </code>
 to yank and paste from the clipboard
respectively.
</p>
<p>
 If you don't even want to specify the
 <code>
  *
 </code>
 register all the time, put this in
your vimrc:
</p>
<p>
 <code>
  vim
set clipboard=unnamed
 </code>
</p>
<p>
 Usually all yank/delete/put operations fill the
 <code>
  "
 </code>
 register, now the
 <code>
  *
 </code>
 register is used for the same operations, therefore simply
 <code>
  y
 </code>
 and
 <code>
  p
 </code>
 will be
enough.
</p>
<p>
 Let me repeat: Using the option above means that every yank/paste, even when
only used in the same Vim window, will alter the clipboard. Decide for yourself
if this is useful or not.
</p>
<p>
 If you're even too lazy to type
 <code>
  y
 </code>
 , you can send every visual selection to the
clipboard by using these settings:
</p>
<p>
 <code>
  vim
set clipboard=unnamed,autoselect
set guioptions+=a
 </code>
</p>
<p>
 Related help files:
</p>
<p>
 <code>
  :h clipboard-unnamed
:h autoselect
:h 'go_a'
 </code>
</p>
<h5>
 Clipboard usage (Linux, BSD, ...)
</h5>
<p>
 If your OS uses
 <a href="http://www.x.org/wiki">
  X
 </a>
 , things work a bit different. X
implements the
 <a href="http://www.x.org/releases/X11R7.7/doc/xproto/x11protocol.html">
  X Window System
Protocol
 </a>
 which
happens to be at major version 11 since 1987, hence X is also often called X11.
</p>
<p>
 Prior, in X10,
 <a href="http://www.x.org/releases/X11R7.7/doc/xorg-docs/icccm/icccm.html#Peer_to_Peer_Communication_by_Means_of_Cut_Buffers">
  cut
buffers
 </a>
 were introduced that kind of worked like a
 <em>
  clipboard
 </em>
 as in copied text was
actually hold by X and it was accessible by all ofter applications. This
mechanism still exists in X, but its use is deprecated now and most software
doesn't use it anymore.
</p>
<p>
 Nowadays data is transferred between applications by the means of
 <a href="http://www.x.org/releases/X11R7.7/doc/xorg-docs/icccm/icccm.html#Peer_to_Peer_Communication_by_Means_of_Selections">
  selections
 </a>
 .
From the 3
 <em>
  selection atoms
 </em>
 defined, only 2 are used in practice: PRIMARY and
CLIPBOARD.
</p>
<p>
 Selections work roughly like this:
</p>
<p>
 <code>
  Program A: <ctrl+c>
Program A: assert ownership of CLIPBOARD
Program B: <ctrl+v>
Program B: note that ownership of CLIPBOARD is hold by Program A
Program B: request data from Program A
Program A: respond to request and send data to Program B
Program B: receives data from Program A and inserts it into the window
 </code>
</p>
<p>
 | Selection | When used? | How to paste? | How to access from Vim? |
|-----------|------------|---------------|-------------------------|
| PRIMARY   | Selecting text              |
 <code>
  middle-click
 </code>
 ,
 <code>
  shift+insert
 </code>
 |
 <code>
  *
 </code>
 register |
| CLIPBOARD | Selecting text and
 <code>
  ctrl+c
 </code>
 |
 <code>
  ctrl+v
 </code>
 |
 <code>
  +
 </code>
 register |
</p>
<p>
 <strong>
  NOTE
 </strong>
 : Selections (no, not even the CLIPBOARD selection) are never kept in
the X server! Thus you lose the data copied with
 <code>
  ctrl+c
 </code>
 when the application
closes.
</p>
<p>
 Use
 <code>
  "*p
 </code>
 to paste the PRIMARY selection or
 <code>
  "+y1G
 </code>
 to yank the entire file to
the CLIPBOARD selection.
</p>
<p>
 If you happen to access one of the two registers all the time, consider using:
</p>
<p>
 <code>
  vim
set clipboard^=unnamed      " * register
" or
set clipboard^=unnamedplus  " + register
 </code>
</p>
<p>
 (The
 <code>
  ^=
 </code>
 is used to prepend to the default value,
 <code>
  :h :set^=
 </code>
 .)
</p>
<p>
 This will make all yank/delete/put operations use either
 <code>
  *
 </code>
 or
 <code>
  +
 </code>
 instead of
the unnamed register
 <code>
  "
 </code>
 . Afterwards you can simply use
 <code>
  y
 </code>
 or
 <code>
  p
 </code>
 for accessing
your chosen X selection.
</p>
<p>
 Related help:
</p>
<p>
 <code>
  vim
:h clipboard-unnamed
:h clipboard-unnamedplus
 </code>
</p>
<h4>
 Restore cursor position when opening file
</h4>
<p>
 Without this, you will always be at line 1 when opening a file. With this, you
will be at the position where you left off.
</p>
<p>
 Put this in your vimrc:
</p>
<p>
 <code>
  vim
autocmd BufReadPost *
    \ if line("'\"") > 1 && line("'\"") <= line("$") |
    \   exe "normal! g`\"" |
    \ endif
 </code>
</p>
<p>
 This simply does
 <code>
  g`"
 </code>
 (jump to position where you left off without changing
jumplist) if that position still exists (the file might have fewer lines since
it was altered by another program).
</p>
<p>
 This requires the use of a viminfo file:
 <code>
  :h viminfo-'
 </code>
 .
</p>
<h4>
 Handling backup, swap, undo, and viminfo files
</h4>
<p>
 Depending on the options, Vim creates up to 4 kinds of working files.
</p>
<p>
 <strong>
  Backup files
 </strong>
 :
</p>
<p>
 You can tell Vim to keep a backup of the original file before writing to it. By
default Vim keeps a backup but immediately removes it when writing to the file
was successful (
 <code>
  :set writebackup
 </code>
 ). If you always want the latest backup file
to persist,
 <code>
  :set backup
 </code>
 . Or you disable backups altogether,
 <code>
  :set nobackup
nowritebackup
 </code>
 .
</p>
<p>
 Let's see what I added last to my vimrc..
</p>
<p>
 <code>
  $ diff ~/.vim/vimrc ~/.vim/files/backup/vimrc-vimbackup
390d389
< command! -bar -nargs=* -complete=help H helpgrep <args>
 </code>
</p>
<p>
 Related help:
 <code>
  :h backup
 </code>
</p>
<p>
 <strong>
  Swap files
 </strong>
 :
</p>
<p>
 You came up with an idea for the best scifi novel ever. After being in the flow
for hours and writing several thousands of words.. power outage! That's the
moment you realize that the last time you saved
 <code>
  ~/wicked_alien_invaders_from_outer_space.txt
 </code>
 was.. well, you never did.
</p>
<p>
 But not all hope is lost! When editing a file, Vim creates a swap file that
contains unsaved changes. Try it for yourself, open any file and get the current
swap file by using
 <code>
  :swapname
 </code>
 . You can also disable swap file by putting
 <code>
  :set
noswapfile
 </code>
 in your vimrc.
</p>
<p>
 By default the swap file is created in the same directory as the edited file and
called something like
 <code>
  .file.swp
 </code>
 , updated either all 200 characters or when you
haven't typed anything for 4 seconds, and deleted when you stop editing the
file. You can change these numbers with
 <code>
  :h 'updatecount'
 </code>
 and
 <code>
  :h
'updatetime'
 </code>
 .
</p>
<p>
 Due to the power outage, the swap file was never deleted. If you do
 <code>
  vim
~/wicked_alien_invaders_from_outer_space.txt
 </code>
 , Vim will prompt you to recover
the file.
</p>
<p>
 Related help:
 <code>
  :h swap-file
 </code>
 and
 <code>
  :h usr_11
 </code>
</p>
<p>
 <strong>
  Undo files
 </strong>
 :
</p>
<p>
 The
 <a href="#undo-tree">
  undo tree
 </a>
 is kept in memory and will be lost when Vim quits.
If you want it to persist,
 <code>
  :set undofile
 </code>
 . This will save the undo file for
 <code>
  ~/foo.c
 </code>
 in
 <code>
  ~/foo.c.un~
 </code>
 .
</p>
<p>
 Related help:
 <code>
  :h 'undofile'
 </code>
 and
 <code>
  :h undo-persistence
 </code>
</p>
<p>
 <strong>
  Viminfo file
 </strong>
 :
</p>
<p>
 When backup, swap, and undo files are all about text state, viminfo files are
used for saving everything else that would otherwise be lost when quitting Vim.
The viminfo file keeps histories (command line, search, input), registers,
marks, buffer list, global variables etc.
</p>
<p>
 By default the viminfo is written to
 <code>
  ~/.viminfo
 </code>
 .
</p>
<p>
 Related help:
 <code>
  :h viminfo
 </code>
 and
 <code>
  :h 'viminfo'
 </code>
</p>
<hr/>
<p>
 If you're anything like me, you prefer keeping all these files in the same
place, e.g.
 <code>
  ~/.vim/files
 </code>
 :
</p>
<p>
 <code>
  set backup
set backupdir   =$HOME/.vim/files/backup/
set backupext   =-vimbackup
set backupskip  =
set directory   =$HOME/.vim/files/swap//
set updatecount =100
set undofile
set undodir     =$HOME/.vim/files/undo/
set viminfo     ='100,n$HOME/.vim/files/info/viminfo
 </code>
</p>
<p>
 The directory
 <code>
  ~/.vim/files
 </code>
 has to be created beforehand, otherwise Vim will
spew errors. If you often work on new hosts, you might want to automate it:
</p>
<p>
 <code>
  vim
if exists('*mkdir') && !isdirectory($HOME.'/.vim/files')
  call mkdir($HOME.'/.vim/files')
endif
 </code>
</p>
<p>
 NOTE: If you edit a file on a multi-user system and Vim prompts you that a swap
file already exists, it probably means that someone else is editing the file at
the moment. You lose this "feature" when you save your swap files in the home
directory.
</p>
<h4>
 Editing remote files
</h4>
<p>
 Vim comes with the netrw plugin that enables editing remote files. Actually it
transfers the remote file to a local temporary file via scp, opens a buffer
using that file, and writes the changes back to the remote file on saving.
</p>
<p>
 This is extremely useful if you want to use your local configuration opposed to
ssh'ing into a server and use whatever the admins want you to use.
</p>
<p>
 <code>
  :e scp://bram@awesome.site.com/.vimrc
 </code>
</p>
<p>
 If you have a
 <code>
  ~/.ssh/config
 </code>
 set up already, this gets used automatically:
</p>
<p>
 <code>
  Host awesome
    HostName awesome.site.com
    Port 1234
    User bram
 </code>
</p>
<p>
 Assuming the above content in
 <code>
  ~/.ssh/config
 </code>
 , this works just as well:
</p>
<p>
 <code>
  :e scp://awesome/.vimrc
 </code>
</p>
<p>
 Similar can be done with a
 <code>
  ~/.netrc
 </code>
 , see
 <code>
  :h netrw-netrc
 </code>
 .
</p>
<p>
 Make sure to read
 <code>
  :h netrw-ssh-hack
 </code>
 and
 <code>
  :h g:netrw_ssh_cmd
 </code>
 .
</p>
<hr/>
<p>
 Another possibility is using
 <a href="https://wiki.archlinux.org/index.php/Sshfs">
  sshfs
 </a>
 which uses
 <a href="https://en.wikipedia.org/wiki/Filesystem_in_Userspace">
  FUSE
 </a>
 to
mount a remote filesystem into your local filesystem.
</p>
<h4>
 Managing plugins
</h4>
<p>
 <a href="https://github.com/tpope/vim-pathogen">
  Pathogen
 </a>
 was the first popular tool for
managing plugins. Actually it just adjusts the
 <em>
  runtimepath
 </em>
 (
 <code>
  :h 'rtp'
 </code>
 ) to
include all the things put under a certain directory. You have to clone the
repositories of the plugins there yourself.
</p>
<p>
 Real plugin managers expose commands that help you installing and updating
plugins from within Vim. Hereinafter is a list of commonly used plugin managers
in alphabetic sequence:
</p>
<ul>
 <li>
  <a href="https://github.com/Shougo/neobundle.vim">
   neobundle
  </a>
  <sup>
   &#9733 1918, pushed 12 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/junegunn/vim-plug">
   plug
  </a>
  <sup>
   &#9733 4336, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/MarcWeber/vim-addon-manager">
   vim-addon-manager
  </a>
  <sup>
   &#9733 501, pushed 72 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/VundleVim/Vundle.vim">
   vundle
  </a>
  <sup>
   &#9733 11432, pushed 7 days ago
  </sup>
 </li>
</ul>
<p>
 Plug is my favorite, but your mileage may vary.
</p>
<h4>
 Block insert
</h4>
<p>
 This is a technique to insert the same text on multiple consecutive lines at the
same time. See this
 <a href="https://raw.githubusercontent.com/mhinz/vim-galore/master/media/block_insert.gif">
  demo
 </a>
 .
</p>
<p>
 Switch to visual block mode with
 <code>
  <c-v>
 </code>
 . Afterwards go down for a few lines.
Hit
 <code>
  I
 </code>
 or
 <code>
  A
 </code>
 and start entering your text.
</p>
<p>
 It might be a bit confusing at first, but text is always entered for the current
line and only after finishing the current insertion, the same text will be
applied to all other lines of the prior visual selection.
</p>
<p>
 So a simple example is
 <code>
  <c-v>3jItext<esc>
 </code>
 .
</p>
<p>
 If you have lines of different length and want to append the same text right
after the end of each line, do this:
 <code>
  <c-v>3j$Atext<esc>
 </code>
 .
</p>
<p>
 Sometime you need to place the cursor somewhere after the end of the current
line. You can't do that by default, but you can set the
 <code>
  virtualedit
 </code>
 option:
</p>
<p>
 <code>
  vim
set virtualedit=all
 </code>
</p>
<p>
 Afterwards
 <code>
  $10l
 </code>
 or
 <code>
  90|
 </code>
 work even after the end of the line.
</p>
<p>
 See
 <code>
  :h blockwise-examples
 </code>
 for more info. It might seem complicated at first,
but quickly becomes second nature.
</p>
<p>
 If you want to get real fancy, have a look at
 <a href="https://github.com/terryma/vim-multiple-cursors">
  multiple-cursors
 </a>
 .
</p>
<h4>
 Running external programs and using filters
</h4>
<p>
 Disclaimer: Vim is single-threaded, so running an external program in the
foreground will block everything else. Sure, you can use one of Vim's
programming interfaces, e.g. Lua, and use its thread support, but during that
time the Vim process is blocked nevertheless. Neovim fixed that by adding a
proper job API.
</p>
<p>
 (Apparently Bram is thinking about adding job control to Vim as well. If you
have a very recent version, see
 <code>
  :helpgrep startjob
 </code>
 .)
</p>
<p>
 Use
 <code>
  :!
 </code>
 to start a job. If you want to list the files in the current working
directory, use
 <code>
  :!ls
 </code>
 . Use
 <code>
  |
 </code>
 for piping in the shell as usual, e.g.
 <code>
  :!ls -1 |
sort | tail -n5
 </code>
 .
</p>
<p>
 Without a range, the output of
 <code>
  :!
 </code>
 will be shown in a scrollable window. On the
other hand, if a range is given, these lines will be
 <a href="https://en.wikipedia.org/wiki/Filter_(software)">
  filtered
 </a>
 . This means they
will be piped to the
 <a href="https://en.wikipedia.org/wiki/Standard_streams#Standard_input_.28stdin.29">
  stdin
 </a>
 of the filter program and after processing be replaced by the
 <a href="https://en.wikipedia.org/wiki/Standard_streams#Standard_output_.28stdout.29">
  stdout
 </a>
 of the filter. E.g. for prepending numbers to the next 5 lines, use this:
</p>
<pre><code>:.,+4!nl -ba -w1 -s' '
</code></pre>
<p>
 Since manually adding the range is quite burdensome, Vim also provides some
helpers for convenience. As always with ranges, you can also select lines in
visual mode and then hit
 <code>
  :
 </code>
 . There's also an operator
 <code>
  !
 </code>
 that takes a motion.
E.g.
 <code>
  !ip!sort
 </code>
 will sort the lines of the current paragraph.
</p>
<p>
 A good use case for filtering is the
 <a href="https://golang.org">
  Go programming
language
 </a>
 . The indentation is pretty opinionated, it even
comes with a filter called
 <code>
  gofmt
 </code>
 for indenting Go source code properly. So
plugins for Go often provide helper commands called
 <code>
  :Fmt
 </code>
 that basically do
 <code>
  :%!gofmt
 </code>
 , so they indent all lines in the file.
</p>
<p>
 People often use
 <code>
  :r !prog
 </code>
 to put the output of prog below the current line,
which is fine for scripts, but when doing it on the fly, I find it easier to use
 <code>
  !!ls
 </code>
 instead, which replaces the current line.
</p>
<pre><code>:h filter
:h :read!
</code></pre>
<h4>
 Cscope
</h4>
<p>
 <a href="http://cscope.sourceforge.net/">
  Cscope
 </a>
 does more things than
 <a href="http://ctags.sourceforge.net/">
  ctags
 </a>
 , but only supports C (and C++ and Java to
some extent).
</p>
<p>
 Whereas a tags file only knows where a symbol was defined, a cscope database
knows much more about your data:
</p>
<ul>
 <li>
  Where is this symbol defined?
 </li>
 <li>
  Where is this symbol used?
 </li>
 <li>
  What is this global symbol's definition?
 </li>
 <li>
  Where did this variable get its value?
 </li>
 <li>
  Where is this function in the source files?
 </li>
 <li>
  What functions call this function?
 </li>
 <li>
  What functions are called by this function?
 </li>
 <li>
  Where does the message "out of space" come from?
 </li>
 <li>
  Where is this source file in the directory structure?
 </li>
 <li>
  What files include this header file?
 </li>
</ul>
<h5>
 1. Build the database
</h5>
<p>
 Do this in the root of your project:
</p>
<p>
 <code>
  sh
$ cscope -bqR
 </code>
</p>
<p>
 This will create 3 files:
 <code>
  cscope{,.in,.po}.out
 </code>
 in the current working
directory. Think of them as your database.
</p>
<p>
 Unfortunately
 <code>
  cscope
 </code>
 only analyzes
 <code>
  *.[c|h|y|l]
 </code>
 files by default. If you want
to use cscope for a Java project instead, do this:
</p>
<p>
 <code>
  sh
$ find . -name "*.java" > cscope.files
$ cscope -bq
 </code>
</p>
<h5>
 2. Add the database
</h5>
<p>
 Open a connection to your freshly built database:
</p>
<p>
 <code>
  vim
:cs add cscope.out
 </code>
</p>
<p>
 Verify that the connection was made:
</p>
<p>
 <code>
  vim
:cs show
 </code>
</p>
<p>
 (Yes, you can add multiple connections.)
</p>
<h5>
 3. Query the database
</h5>
<p>
 <code>
  vim
:cs find <kind> <query>
 </code>
</p>
<p>
 E.g.
 <code>
  :cs find d foo
 </code>
 will list all functions that are called by
 <code>
  foo(...)
 </code>
 .
</p>
<p>
 | Kind | Explanation |
|------|-------------|
| s    |
 <strong>
  s
 </strong>
 ymbol: find all references to the token        |
| g    |
 <strong>
  g
 </strong>
 lobal: find global definition(s) of the token  |
| c    |
 <strong>
  c
 </strong>
 alls: find all calls to the function           |
| t    |
 <strong>
  t
 </strong>
 ext: find all instances of the text            |
| e    |
 <strong>
  e
 </strong>
 grep: egrep search for the word                |
| f    |
 <strong>
  f
 </strong>
 ile: open the filename                         |
| i    |
 <strong>
  i
 </strong>
 ncludes: find files that include the filename  |
| d    |
 <strong>
  d
 </strong>
 epends: find functions called by this function |
</p>
<p>
 I suggest some convenience mappings e.g.:
</p>
<p>
 <code>
  vim
nnoremap <buffer> <leader>cs :cscope find s  <c-r>=expand('<cword>')<cr><cr>
nnoremap <buffer> <leader>cg :cscope find g  <c-r>=expand('<cword>')<cr><cr>
nnoremap <buffer> <leader>cc :cscope find c  <c-r>=expand('<cword>')<cr><cr>
nnoremap <buffer> <leader>ct :cscope find t  <c-r>=expand('<cword>')<cr><cr>
nnoremap <buffer> <leader>ce :cscope find e  <c-r>=expand('<cword>')<cr><cr>
nnoremap <buffer> <leader>cf :cscope find f  <c-r>=expand('<cfile>')<cr><cr>
nnoremap <buffer> <leader>ci :cscope find i ^<c-r>=expand('<cfile>')<cr>$<cr>
nnoremap <buffer> <leader>cd :cscope find d  <c-r>=expand('<cword>')<cr><cr>
 </code>
</p>
<p>
 So, when
 <code>
  :tag
 </code>
 (or
 <code>
  <c-]>
 </code>
 ) jumps to a definition from the tags file,
 <code>
  :cstag
 </code>
 does the same, but also takes connected cscope databases into account. The
option
 <code>
  'cscopetag'
 </code>
 makes
 <code>
  :tag
 </code>
 act like
 <code>
  :cstag
 </code>
 automatically. This is very
convenient if you already have tag-related mappings.
</p>
<p>
 Related help:
 <code>
  :h cscope
 </code>
</p>
<h4>
 MatchIt
</h4>
<p>
 Since Vim is written in C, a lot of features assume C-like syntax. By default,
if your cursor is on
 <code>
  {
 </code>
 or
 <code>
  #endif
 </code>
 , you can use
 <code>
  %
 </code>
 to jump to the
corresponding
 <code>
  }
 </code>
 or
 <code>
  #ifdef
 </code>
 respectively.
</p>
<p>
 Vim comes bundled with a plugin called matchit.vim which is not enabled by
default. It makes
 <code>
  %
 </code>
 also cycle through HTML tags, if/else/endif constructs in
VimL etc. and introduces a few new commands.
</p>
<p>
 To always load the plugin, put this in your vimrc:
</p>
<p>
 <code>
  vim
if !exists('g:loaded_matchit')
  runtime macros/matchit.vim
endif
 </code>
</p>
<p>
 Since the documentation of matchit is pretty extensive, I suggest also doing the
following once:
</p>
<p>
 <code>
  vim
:!mkdir -p ~/.vim/doc
:!cp $VIMRUNTIME/macros/matchit.txt ~/.vim/doc
:helptags ~/.vim/doc
 </code>
</p>
<p>
 The plugin is ready to use now. See
 <code>
  :h matchit-intro
 </code>
 for the supported
commands and
 <code>
  :h matchit-languages
 </code>
 for the supported languages.
</p>
<p>
 That said, it's easy to define your own matching pairs:
</p>
<p>
 <code>
  vim
autocmd FileType python let b:match_words = '\<if\>:\<elif\>:\<else\>'
 </code>
</p>
<p>
 Afterwards you can cycle through these 3 statements in any Python file by using
 <code>
  %
 </code>
 (forward) or
 <code>
  g%
 </code>
 (backward).
</p>
<p>
 Related help:
</p>
<p>
 <code>
  :h matchit-install
:h matchit
:h b:match_words
 </code>
</p>
<h2>
 Tips
</h2>
<h4>
 Saner behavior of n and N
</h4>
<p>
 The direction of
 <code>
  n
 </code>
 and
 <code>
  N
 </code>
 depends on whether
 <code>
  /
 </code>
 or
 <code>
  ?
 </code>
 was used for
searching forward or backward respectively. This is pretty confusing to me.
</p>
<p>
 If you want
 <code>
  n
 </code>
 to always search forward and
 <code>
  N
 </code>
 backward, use this:
</p>
<p>
 <code>
  vim
nnoremap <expr> n  'Nn'[v:searchforward]
nnoremap <expr> N  'nN'[v:searchforward]
 </code>
</p>
<h4>
 Saner command-line history
</h4>
<p>
 If you're anything like me, you're used to going to next and previous items via
 <code>
  <c-n>
 </code>
 and
 <code>
  <c-p>
 </code>
 respectively. By default, this also works in the
command-line and recalls older or more recent command-lines from history.
</p>
<p>
 So far, so good. But
 <code>
  <up>
 </code>
 and
 <code>
  <down>
 </code>
 are even smarter! They recall the
command-line whose beginning matches the current command-line. E.g.
 <code>
  :echo <up>
 </code>
 may change to
 <code>
  :echo "Vim rocks!"
 </code>
 .
</p>
<p>
 Of course I don't want you to reach to the arrow keys, just map it instead:
</p>
<p>
 <code>
  vim
cnoremap <c-n>  <down>
cnoremap <c-p>  <up>
 </code>
</p>
<p>
 I depend on this behaviour several times a day.
</p>
<h4>
 Saner CTRL-L
</h4>
<p>
 By default
 <code>
  <c-l>
 </code>
 clears and redraws the screen (like
 <code>
  :redraw!
 </code>
 ). The
following mapping does the same, plus de-highlighting the matches found via
 <code>
  /
 </code>
 ,
 <code>
  ?
 </code>
 etc., plus fixing syntax highlighting (sometimes Vim loses highlighting due
to complex highlighting rules), plus force updating the syntax highlighting in
diff mode:
</p>
<p>
 <code>
  vim
nnoremap <leader>l :nohlsearch<cr>:diffupdate<cr>:syntax sync fromstart<cr><c-l>
 </code>
</p>
<h4>
 Disable audible and visual bells
</h4>
<p>
 <code>
  vim
set noerrorbells
set novisualbell
set t_vb=
 </code>
</p>
<p>
 See
 <a href="http://vim.wikia.com/wiki/Disable_beeping">
  Vim Wiki: Disable beeping
 </a>
 .
</p>
<h4>
 Quickly move current line
</h4>
<p>
 Sometimes I need a quick way to move the current line above or below:
</p>
<p>
 <code>
  vim
nnoremap [e  :<c-u>execute 'move -1-'. v:count1<cr>
nnoremap ]e  :<c-u>execute 'move +'. v:count1<cr>
 </code>
</p>
<p>
 These mappings also take a count, so
 <code>
  2]e
 </code>
 moves the current line 2 lines below.
</p>
<h4>
 Quickly add empty lines
</h4>
<p>
 <code>
  vim
nnoremap [<space>  :<c-u>put! =repeat(nr2char(10), v:count1)<cr>'[
nnoremap ]<space>  :<c-u>put =repeat(nr2char(10), v:count1)<cr>
 </code>
</p>
<p>
 Now
 <code>
  5[<space>
 </code>
 inserts 5 blank lines above the current line.
</p>
<h4>
 Quickly edit your macros
</h4>
<p>
 This is a real gem! The mapping takes a register (or
 <code>
  *
 </code>
 by default) and opens
it in the cmdline-window. Hit
 <code>
  <cr>
 </code>
 when you're done editing for setting the
register.
</p>
<p>
 I often use this to correct typos I did while recording a macro.
</p>
<p>
 <code>
  vim
nnoremap <leader>m  :<c-u><c-r><c-r>='let @'. v:register .' = '. string(getreg(v:register))<cr><c-f><left>
 </code>
</p>
<p>
 Use it like this
 <code>
  <leader>m
 </code>
 or
 <code>
  "q<leader>m
 </code>
 .
</p>
<p>
 Notice the use of
 <code>
  <c-r><c-r>
 </code>
 to make sure that the
 <code>
  <c-r>
 </code>
 is inserted
literally. See
 <code>
  :h c_^R^R
 </code>
 .
</p>
<h4>
 Quickly jump to header or source file
</h4>
<p>
 This technique can probably be applied to many filetypes. It sets
 <em>
  file marks
 </em>
 (see
 <code>
  :h marks
 </code>
 ) when leaving a source or header file, so you can quickly jump
back to the last accessed one by using
 <code>
  'C
 </code>
 or
 <code>
  'H
 </code>
 (see
 <code>
  :h 'A
 </code>
 ).
</p>
<p>
 <code>
  vim
autocmd BufLeave *.{c,cpp} mark C
autocmd BufLeave *.h       mark H
 </code>
</p>
<p>
 <strong>
  NOTE
 </strong>
 : The info is saved in the viminfo file, so make sure that
 <code>
  :set
viminfo?
 </code>
 includes
 <code>
  :h viminfo-'
 </code>
 .
</p>
<h4>
 Quickly change font size in GUI
</h4>
<p>
 I think this was taken from tpope's config:
</p>
<p>
 <code>
  vim
command! Bigger  :let &guifont = substitute(&guifont, '\d\+$', '\=submatch(0)+1', '')
command! Smaller :let &guifont = substitute(&guifont, '\d\+$', '\=submatch(0)-1', '')
 </code>
</p>
<h4>
 Change cursor style dependent on mode
</h4>
<p>
 I like to use a block cursor in normal mode, i-beam cursor in insert mode, and
underline cursor in replace mode. Also when using tmux in the middle.
</p>
<p>
 <code>
  vim
if empty($TMUX)
  let &t_SI = "\<Esc>]50;CursorShape=1\x7"
  let &t_EI = "\<Esc>]50;CursorShape=0\x7"
  let &t_SR = "\<Esc>]50;CursorShape=2\x7"
else
  let &t_SI = "\<Esc>Ptmux;\<Esc>\<Esc>]50;CursorShape=1\x7\<Esc>\\"
  let &t_EI = "\<Esc>Ptmux;\<Esc>\<Esc>]50;CursorShape=0\x7\<Esc>\\"
  let &t_SR = "\<Esc>Ptmux;\<Esc>\<Esc>]50;CursorShape=2\x7\<Esc>\\"
endif
 </code>
</p>
<p>
 This simply tells Vim to print a certain sequence of characters (
 <a href="https://en.wikipedia.org/wiki/Escape_sequence">
  escape
sequence
 </a>
 ) when entering/leaving
insert mode. The underlying terminal will process and evaluate it.
</p>
<p>
 There's one drawback though: there are many terminal emulator implementations
and not all use the same sequences for doing the same things. The sequences used
above might not work with your implementation. Your implementation might not
even support different cursor styles. Check the documentation.
</p>
<p>
 The example above works with iTerm2.
</p>
<h4>
 Don't lose selection when shifting sidewards
</h4>
<p>
 If you select one or more lines, you can use
 <code>
  <
 </code>
 and
 <code>
  >
 </code>
 for shifting them
sidewards. Unfortunately you immediately lose the selection afterwards.
</p>
<p>
 You can use
 <code>
  gv
 </code>
 to reselect the last selection (see
 <code>
  :h gv
 </code>
 ), thus you can work
around it like this:
</p>
<p>
 <code>
  vim
xnoremap <  <gv
xnoremap >  >gv
 </code>
</p>
<p>
 Now you can use
 <code>
  >>>>>
 </code>
 on your visual selection without any problems.
</p>
<p>
 <strong>
  NOTE
 </strong>
 : The same can be achieved using
 <code>
  .
 </code>
 , which repeats the last change.
</p>
<h4>
 Reload a file on saving
</h4>
<p>
 Using
 <a href="#autocmds">
  autocmds
 </a>
 you can do anything on saving a file, e.g. sourcing
it in case of a dotfile or running a linter to check for syntactical errors in
your source code.
</p>
<p>
 <code>
  vim
autocmd BufWritePost $MYVIMRC source $MYVIMRC
autocmd BufWritePost ~/.Xdefaults call system('xrdb ~/.Xdefaults')
 </code>
</p>
<h4>
 Smarter cursorline
</h4>
<p>
 I love the cursorline, but I only want to use it in the current window and not
when being in insert mode:
</p>
<p>
 <code>
  vim
autocmd WinEnter    * set cursorline
autocmd WinLeave    * set nocursorline
autocmd InsertEnter * set nocursorline
autocmd InsertLeave * set cursorline
 </code>
</p>
<h4>
 Faster keyword completion
</h4>
<p>
 The keyword completion (
 <code>
  <c-n>
 </code>
 /
 <code>
  <c-p>
 </code>
 ) tries completing whatever is listed in
the
 <code>
  'complete'
 </code>
 option. By default this also includes tags (which can be
annoying) and scanning all included files (which can be very slow). If you can
live without these things, disable them:
</p>
<p>
 <code>
  vim
set complete-=i   " disable scanning included files
set complete-=t   " disable searching tags
 </code>
</p>
<h2>
 Commands
</h2>
<p>
 Useful commands that are good to know. Use
 <code>
  :h :<command name>
 </code>
 to learn more
about them, e.g.
 <code>
  :h :global
 </code>
 .
</p>
<h4>
 :global
</h4>
<p>
 Execute a command on all matching lines. E.g.
 <code>
  :global /regexp/ print
 </code>
 will use
 <code>
  :print
 </code>
 on all lines that contain "regexp".
</p>
<p>
 Fun fact: You probably all know good old grep, the filter program written by Ken
Thompson. What does it do? It prints all lines matching a certain regular
expression! Now guess the short form of
 <code>
  :global /regexp/ print
 </code>
 ? That's right!
It's
 <code>
  :g/re/p
 </code>
 . Ken Thompson was inspired by vi's
 <code>
  :global
 </code>
 when he wrote grep.
</p>
<p>
 Despite its name,
 <code>
  :global
 </code>
 only acts on all lines by default, but it also takes
a range. Assume you want use
 <code>
  :delete
 </code>
 on all lines from the current line to the
next blank line (matched by the regular expression
 <code>
  ^$
 </code>
 ) that contain "foo":
</p>
<p>
 <code>
  vim
:,/^$/g/foo/d
 </code>
</p>
<h4>
 :normal and :execute
</h4>
<p>
 These commands are commonly used in Vim scripts.
</p>
<p>
 With
 <code>
  :normal
 </code>
 you can do normal mode mappings from the command-line. E.g.
 <code>
  :normal! 4j
 </code>
 will make the cursor go down 4 lines (without using any custom
mapping for "j" due to the "!").
</p>
<p>
 Mind that
 <code>
  :normal
 </code>
 also takes a count, so
 <code>
  :%norm! Iabc
 </code>
 would prepend "abc" to
every line.
</p>
<p>
 With
 <code>
  :execute
 </code>
 you can mix commands with expressions. Assume you edit a C
source file and want to switch to its header file:
</p>
<p>
 <code>
  vim
:execute 'edit' fnamemodify(expand('%'), ':r') . '.h'
 </code>
</p>
<p>
 Both commands are often used together. Assume you want to make the cursor go
down "n" lines:
</p>
<p>
 <code>
  vim
:let n = 4
:execute 'normal!' n . 'j'
 </code>
</p>
<h4>
 :redir
</h4>
<p>
 Many commands print messages and
 <code>
  :redir
 </code>
 allows to redirect that output. You
can redirect to files,
 <a href="#registers">
  registers
 </a>
 or variables.
</p>
<p>
 <code>
  vim
:redir => neatvar
:reg
:redir END
:echo neatvar
:" For fun let's also put it onto the current buffer.
:put =nicevar
 </code>
</p>
<p>
 Related help:
 <code>
  :h :redir
 </code>
</p>
<h2>
 Debugging
</h2>
<h4>
 General tips
</h4>
<p>
 If you encounter a strange behaviour, try reproducing it like this:
</p>
<p>
 <code>
  vim -u NONE -N
 </code>
</p>
<p>
 This will start Vim without vimrc (thus default settings) and in nocompatible
mode (which makes it use Vim defaults instead of vi defaults). (See
 <code>
  :h
--noplugin
 </code>
 for other combinations of what to load at start.)
</p>
<p>
 If you can still reproduce it now, it's most likely a bug in Vim itself! Report
it to the
 <a href="https://groups.google.com/forum/#!forum/vim_dev">
  vim_dev
 </a>
 mailing
list. Most of the time the issue won't be resolved at this time and you'll have
to further investigate.
</p>
<p>
 Plugins often introduce new/changed/faulty behaviour. E.g. if it happens on
saving, check
 <code>
  :verb au BufWritePost
 </code>
 to get a list of potential culprits.
</p>
<p>
 If you're using a plugin manager, comment them out until you find the culprit.
</p>
<p>
 Issue is still not resolved? If it's not a plugin, it must be your other
settings, so maybe your options or autocmds etc.
</p>
<p>
 Time to use binary search. Repeatedly split the search space in two until you
find the culprit line. Due to the nature of binary division, it won't take many
steps.
</p>
<p>
 In practice it works like this: Put the
 <code>
  :finish
 </code>
 command in the middle of your
vimrc. Vim will skip everything after it. If it still happens, the problem is in
the active upper half. Move the
 <code>
  :finish
 </code>
 to the middle of
 <em>
  that
 </em>
 half.
Otherwise the issue is in the inactive lower half. Move the
 <code>
  :finish
 </code>
 to the
middle of
 <em>
  that
 </em>
 half. And so on.
</p>
<h4>
 Profiling startup time
</h4>
<p>
 Vim startup feels slow? Time to crunch some numbers:
</p>
<p>
 <code>
  vim --startuptime /tmp/startup.log +q && vim /tmp/startup.log
 </code>
</p>
<p>
 The first column is the most important as it shows the elapsed absolute time. If
there is a big jump in time between two lines, the second line is either a very
big file or a file with faulty VimL code that is worth investigating.
</p>
<h4>
 Profiling at runtime
</h4>
<p>
 Required
 <a href="#what-kind-of-vim-am-i-running">
  feature
 </a>
 :
 <code>
  +profile
 </code>
</p>
<p>
 Vim provides a built-in capability for profiling at runtime and is a great way
to find slow code in your environment.
</p>
<p>
 The
 <code>
  :profile
 </code>
 command takes a bunch of sub-commands for specifying what to
profile.
</p>
<p>
 If you want to profile
 <em>
  everything
 </em>
 , do this:
</p>
<p>
 <code>
  :profile start /tmp/profile.log
:profile file *
:profile func *
<do something in Vim>
<quit Vim>
 </code>
</p>
<p>
 Vim keeps the profiling information in memory and only writes it out to the
logfile on exit. (Neovim has fixed this using
 <code>
  :profile dump
 </code>
 ).
</p>
<p>
 Have a look at
 <code>
  /tmp/profile.log
 </code>
 . All code that was executed during profiling
will be shown. Every line, how often it was executed and how much time it took.
</p>
<p>
 Most of the time that will be plugin code the user isn't familiar with, but if
you're investigating a certain issue, jump to the bottom of the log. Here are
two different sections
 <code>
  FUNCTIONS SORTED ON TOTAL TIME
 </code>
 and
 <code>
  FUNCTIONS SORTED ON
SELF TIME
 </code>
 that are worth gold. On a quick glance you can see, if a certain
function is taking too long.
</p>
<h4>
 Verbosity
</h4>
<p>
 Another useful way for observing what Vim is currently doing is increasing the
verbosity level. Currently Vim supports 9 different levels. See
 <code>
  :h 'verbose'
 </code>
 for the full list.
</p>
<p>
 <code>
  vim
:e /tmp/foo
:set verbose=2
:w
:set verbose=0
 </code>
</p>
<p>
 This would show all the files that get sourced, e.g. the undo file or various
plugins that act on saving.
</p>
<p>
 If you only want increase verbosity for a single command, there's also
 <code>
  :verbose
 </code>
 , which simply gets put in front of any other command. It takes the
verbosity level as count and defaults to 1:
</p>
<p>
 <code>
  vim
:verb set verbose
"  verbose=1
:10verb set verbose
"  verbose=10
 </code>
</p>
<p>
 It's very often used with its default verbosity level 1 to show where an option
was set last:
</p>
<p>
 <code>
  vim
:verb set ai?
"      Last set from ~/.vim/vimrc
 </code>
</p>
<p>
 Naturally, the higher the verbosity level the more overwhelming the output. But
fear no more, you can simply redirect the output to a file:
</p>
<p>
 <code>
  vim
:set verbosefile=/tmp/foo | 15verbose echo "foo" | vsplit /tmp/foo
 </code>
</p>
<h4>
 Debugging Vim scripts
</h4>
<p>
 If you ever used a command-line debugger before,
 <code>
  :debug
 </code>
 will quickly feel
familiar.
</p>
<p>
 Simply prepend
 <code>
  :debug
 </code>
 to any other command and you'll be put into debug mode.
That is, the execution will stop at the first line about to be executed and that
line will be displayed.
</p>
<p>
 See
 <code>
  :h >cont
 </code>
 and below for the 6 available debugger commands and note that,
like in gdb and similar debuggers, you can also use their short forms, that is
 <code>
  c
 </code>
 ,
 <code>
  q
 </code>
 ,
 <code>
  n
 </code>
 ,
 <code>
  s
 </code>
 ,
 <code>
  i
 </code>
 , and
 <code>
  f
 </code>
 .
</p>
<p>
 Apart from that those, you're free to use any Vim command, e.g.
 <code>
  :echo myvar
 </code>
 ,
which gets executed in the context of the current position in the code.
</p>
<p>
 You basically get a
 <a href="https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop">
  REPL
 </a>
 by
simply using
 <code>
  :debug 1
 </code>
 .
</p>
<p>
 It would be a pain if you had to single-step through every single line, so of
course we can define breakpoints, too. (Breakpoints are called breakpoints,
because the execution stops when they're hit, thus you can simply skip code
you're not interested in.) See
 <code>
  :h :breakadd
 </code>
 ,
 <code>
  :h :breakdel
 </code>
 , and
 <code>
  :h
:breaklist
 </code>
 for further details.
</p>
<p>
 Let's assume you want to know what code is run every time you save a file:
</p>
<p>
 ```vim
:au BufWritePost
" signify  BufWritePost
"     *         call sy#start()
:breakadd func *start
:w
" Breakpoint in "sy#start" line 1
" Entering Debug mode.  Type "cont" to continue.
" function sy#start
" line 1: if g:signify_locked
</p>
<blockquote>
 <p>
  s
  " function sy#start
  " line 3: endif
 </p>
 <p>
  " function sy#start
  " line 5: let sy_path = resolve(expand('%:p'))
  q
  :breakdel *
  ```
 </p>
</blockquote>
<p>
 As you can see, using
 <code>
  <cr>
 </code>
 will repeat the previous debugger command,
 <code>
  s
 </code>
 in
this case.
</p>
<p>
 <code>
  :debug
 </code>
 can be used in combination with the
 <a href="#verbosity">
  verbose
 </a>
 option.
</p>
<h4>
 Debugging syntax files
</h4>
<p>
 Syntax files are often the cause for slowdowns due to wrong and/or complex
regular expressions. If the
 <code>
  +profile
 </code>
 <a href="#what-kind-of-vim-am-i-running">
  feature
 </a>
 is compiled in, Vim provides the super useful
 <code>
  :syntime
 </code>
 command.
</p>
<p>
 <code>
  vim
:syntime on
" hit <c-l> a few times to redraw the window which causes the syntax rules to get applied again
:syntime off
:syntime report
 </code>
</p>
<p>
 The output contains important metrics. E.g. you can see which regexp takes too
long and should be optimized or which regexps are used all the time but never
even match.
</p>
<p>
 See
 <code>
  :h :syntime
 </code>
 .
</p>
<h2>
 Miscellaneous
</h2>
<h4>
 Additional resources
</h4>
<p>
 | Resource | Description |
|----------|-------------|
|
 <a href="http://www.moolenaar.net/habits.html">
  Seven habits of effective text editing
 </a>
 | By Bram Moolenaar, the author of Vim. |
|
 <a href="http://www.moolenaar.net/habits_2007.pdf">
  Seven habits of effective text editing 2.0 (PDF)
 </a>
 | See above. |
|
 <a href="http://www.ibm.com/developerworks/views/linux/libraryview.jsp?sort_order=asc&sort_by=Title&search_by=scripting+the+vim+editor">
  IBM DeveloperWorks: Scripting the Vim editor
 </a>
 | Five-part series on Vim scripting. |
|
 <a href="http://learnvimscriptthehardway.stevelosh.com">
  Learn Vimscript the Hard Way
 </a>
 | Develop a Vim plugin from scratch. |
|
 <a href="http://www.amazon.com/Practical-Vim-Edit-Speed-Thought/dp/1680501275/">
  Practical Vim (2nd Edition)
 </a>
 | Hands down the best book about Vim. |
|
 <a href="http://vimcasts.org/episodes/archive">
  Vimcasts.org
 </a>
 | Vim screencasts. |
|
 <a href="http://www.viemu.com/a-why-vi-vim.html">
  Why, oh WHY, do those #?@! nutheads use vi?
 </a>
 | Common misconceptions explained. |
|
 <a href="http://stackoverflow.com/a/1220118">
  Your problem with Vim is that you don't grok vi
 </a>
 | Concise, informative and correct. A real gem. |
</p>
<h4>
 Vim distributions
</h4>
<p>
 Vim distributions are Vim + custom settings + custom plugins from certain
authors and are therefore very opinionated.
</p>
<p>
 The problem with such distributions is that they tend to be used by beginners.
(More advanced users know how to choose their own plugins and settings after
all.) It all goes good until an issue appears. Now where is the problem? The
beginner doesn't know what to do and asks for advice on the internet. After long
back and forth they figure out that the problem was a weird mapping provided by
the distro. But the beginner thought it was a default Vim mapping... Time was
wasted, everyone is pissed.
</p>
<p>
 I don't have problems with distributions per se, but please, if you don't
understand exactly what they're doing, don't try to get help from others in case
of emergencies.
</p>
<p>
 I know that many people don't want to spend hours and hours on customizing an
editor (and actually you never stop customizing your vimrc when you finally got
hooked), but in the long-term it's much better and more time-efficient to learn
how to do stuff manually in the first place.
</p>
<p>
 Repeat after me: "A programmer should know their tools."
</p>
<p>
 Anyway, if you know what you're doing, you might get some inspiration from
looking at some distributions:
</p>
<ul>
 <li>
  <a href="http://cream.sourceforge.net">
   cream
  </a>
 </li>
 <li>
  <a href="https://github.com/carlhuda/janus.git">
   janus
  </a>
 </li>
 <li>
  <a href="https://github.com/spf13/spf13-vim">
   spf13
  </a>
  <sup>
   &#9733 7945, pushed 9 days ago
  </sup>
 </li>
</ul>
<h4>
 Standard plugins
</h4>
<p>
 Surprising to many people, Vim comes with a handful of plugins on its own that
all get loaded by default. Check
 <code>
  :scriptnames
 </code>
 after starting Vim to see all
sourced files.
</p>
<p>
 Most of them will never get used, so disable them as you see fit. They will
still be shown as sourced, but only the first lines actually get read before Vim
bails out. No further code (mappings, commands, logic) will be processed.
</p>
<p>
 | Plugin     | Disable it using..                  | Help |
|------------|-------------------------------------|------|
| 2html      |
 <code>
  let g:loaded_2html_plugin = 1
 </code>
 |
 <code>
  :h 2html
 </code>
 |
| getscript  |
 <code>
  let g:loaded_getscriptPlugin = 1
 </code>
 |
 <code>
  :h pi_getscript
 </code>
 |
| gzip       |
 <code>
  let g:loaded_gzip = 1
 </code>
 |
 <code>
  :h pi_gzip
 </code>
 |
| logipat    |
 <code>
  let g:loaded_logipat = 1
 </code>
 |
 <code>
  :h pi_logipat
 </code>
 |
| matchparen |
 <code>
  let g:loaded_matchparen = 1
 </code>
 |
 <code>
  :h pi_paren
 </code>
 |
| netrw      |
 <code>
  let g:loaded_netrwPlugin = 1
 </code>
 |
 <code>
  :h pi_netrw
 </code>
 |
| rrhelper   |
 <code>
  let g:loaded_rrhelper = 1
 </code>
 |
 <code>
  :e $VIMRUNTIME/plugin/rrhelper.vim
 </code>
 |
| spellfile  |
 <code>
  let g:loaded_spellfile_plugin = 1
 </code>
 |
 <code>
  :h spellfile.vim
 </code>
 |
| tar        |
 <code>
  let g:loaded_tarPlugin = 1
 </code>
 |
 <code>
  :h pi_tar
 </code>
 |
| vimball    |
 <code>
  let g:loaded_vimballPlugin = 1
 </code>
 |
 <code>
  :h pi_vimball
 </code>
 |
| zip        |
 <code>
  let g:loaded_zipPlugin = 1
 </code>
 |
 <code>
  :h pi_zip
 </code>
 |
</p>
<h4>
 Map CapsLock to Control
</h4>
<p>
 CapsLock belongs to the most useless keys on your keyboard, but it's much easier
to reach than the Control key, since it lies on your
 <a href="https://raw.githubusercontent.com/mhinz/vim-galore/master/media/homerow.png">
  home
row
 </a>
 .
Mapping CapsLock to Control is a great way to prevent or at least reduce
 <a href="https://de.wikipedia.org/wiki/Repetitive-Strain-Injury-Syndrom">
  RSI
 </a>
 if you
program a lot.
</p>
<p>
 Attention: When you get used to it, you can't live without it anymore.
</p>
<p>
 <strong>
  OSX
 </strong>
 :
</p>
<p>
 <code>
  System Preferences -> Keyboard -> Keyboard Tab -> Modifier Keys
 </code>
 . Change
"CapsLock" to "Control".
</p>
<p>
 <strong>
  Linux
 </strong>
 :
</p>
<p>
 To change the keys in X, put this in your
 <code>
  ~/.xmodmap
 </code>
 :
</p>
<pre><code>remove Lock = Caps_Lock
keysym Caps_Lock = Control_L
add Control = Control_L
</code></pre>
<p>
 Afterwards source it via
 <code>
  $ xmodmap ~/.xmodmap
 </code>
 .
</p>
<p>
 An alternative would be using
 <a href="https://github.com/alols/xcape">
  xcape
 </a>
 .
</p>
<p>
 <strong>
  Windows
 </strong>
 :
</p>
<p>
 See
 <a href="http://superuser.com/questions/764782/map-caps-lock-to-control-in-windows-8-1">
  superuser.com: Map Caps-Lock to Control in Windows
8.1
 </a>
 .
</p>
<h4>
 Easter eggs
</h4>
<p>
 | Command   | Message |
|-----------|---------|
|
 <code>
  :Ni!
 </code>
 |
 <code>
  Do you demand a shrubbery?
 </code>
 |
|
 <code>
  :h 'sm'
 </code>
 |
 <code>
  NOTE: Use of the short form is rated PG.
 </code>
 |
|
 <code>
  :h 42
 </code>
 |
 <code>
  What is the meaning of life, the universe and everything? Douglas Adams, the only person who knew what this question really was about is now dead, unfortunately.  So now you might wonder what the meaning of death is...
 </code>
 |
|
 <code>
  :h UserGettingBored
 </code>
 |
 <code>
  When the user presses the same key 42 times. Just kidding! :-)
 </code>
 |
|
 <code>
  :h bar
 </code>
 |
 <code>
  Ceci n'est pas une pipe.
 </code>
 |
|
 <code>
  :h holy-grail
 </code>
 |
 <code>
  You found it, Arthur!
 </code>
 |
|
 <code>
  :h map-modes
 </code>
 |
 <code>
  :nunmap can also be used outside of a monastery.
 </code>
 |
|
 <code>
  :help!
 </code>
 |
 <code>
  E478: Don't panic!
 </code>
 (Glitch? When used in a help buffer (
 <code>
  buftype=help
 </code>
 ) this works like
 <code>
  :h help.txt
 </code>
 instead.) |
|
 <code>
  :smile
 </code>
 | Try it out yourself. ;-) Added in 7.4.1005. |
</p>
<h4>
 Standard plugins
</h4>
<h4>
 Why hjkl for navigation?
</h4>
<p>
 When
 <a href="https://en.wikipedia.org/wiki/Bill_Joy">
  Bill Joy
 </a>
 created
 <a href="https://en.wikipedia.org/wiki/Vi">
  vi
 </a>
 , a predecessor of Vim, he did it on a
 <a href="https://en.wikipedia.org/wiki/ADM-3A">
  ADM-3A
 </a>
 which had no extra cursor buttons
but used, you might already guessed it, hjkl instead.
</p>
<p>
 Keyboard layout:
 <a href="https://raw.githubusercontent.com/mhinz/vim-galore/master/media/adm-3a-layout.jpg">
  click
 </a>
</p>
<p>
 This also shows why
 <code>
  ~
 </code>
 is used to denote the home directory on Unix systems.
</p>
<h2>
 Quirks
</h2>
<h4>
 Editing small files is slow
</h4>
<p>
 There are two things which can have a huge impact on performance:
</p>
<ol>
 <li>
  Complex
  <strong>
   regular expressions
  </strong>
  . Particular the Ruby syntax file caused
people to have slowdowns in the past. (Also see
  <a href="#debugging-syntax-files">
   Debugging syntax files
  </a>
  .)
 </li>
 <li>
  <strong>
   Screen redraws
  </strong>
  . Some features force all lines to redraw.
 </li>
</ol>
<p>
 | Typical culprit | Why? | Solution? |
|-----------------|------|-----------|
|
 <code>
  :set cursorline
 </code>
 | Causes all lines to redraw. |
 <code>
  :set nocursorline
 </code>
 |
|
 <code>
  :set cursorcolumn
 </code>
 | Causes all lines to redraw. |
 <code>
  :set nocursorcolumn
 </code>
 |
|
 <code>
  :set relativenumber
 </code>
 | Causes all lines to redraw. |
 <code>
  :set norelativenumber
 </code>
 |
|
 <code>
  :set foldmethod=syntax
 </code>
 | If the syntax file is slow already, this makes it even worse. |
 <code>
  :set foldmethod=manual
 </code>
 ,
 <code>
  :set foldmethod=marker
 </code>
 or
 <a href="https://github.com/Konfekt/FastFold">
  FastFold
 </a>
 |
|
 <code>
  :set synmaxcol=3000
 </code>
 | Due to internal representation, Vim has problems with long lines in general. Highlights columns till column 3000. |
 <code>
  :set synmaxcol=200
 </code>
 |
| matchparen.vim           | Loaded by default. Uses regular expressions to find the accompanying parenthesis. | Disable plugin:
 <code>
  :h matchparen
 </code>
 |
</p>
<p>
 <strong>
  NOTE
 </strong>
 : You only need to do this if you experience actual performance
drawbacks. In most cases using the things mentioned above is absolutely fine.
</p>
<h4>
 Editing huge files is slow
</h4>
<p>
 The biggest issue with big files is, that Vim reads the whole file at once. This
is done due to how buffers are represented internally.
(
 <a href="https://groups.google.com/forum/#!topic/vim_dev/oY3i8rqYGD4/discussion">
  Discussion on vim_dev@
 </a>
 )
</p>
<p>
 If you only want to read,
 <code>
  tail hugefile | vim -
 </code>
 is a good workaround.
</p>
<p>
 If you can live without syntax, settings and plugins for the moment:
</p>
<p>
 <code>
  $ vim -u NONE -N
 </code>
</p>
<p>
 This should make navigation quite a lot faster, especially since no expensive
regular expressions for syntax highlighting are used. You should also tell Vim
not to use swapfiles and viminfo files to avoid long delays on writing:
</p>
<p>
 <code>
  $ vim -n -u NONE -i NONE -N
 </code>
</p>
<p>
 Putting it in a nutshell, try to avoid using Vim when intending to write really
huge files. :\
</p>
<h4>
 Newline used for NUL
</h4>
<p>
 NUL characters (
 <code>
  \0
 </code>
 ) in a file, are stored as newline (
 <code>
  \n
 </code>
 ) in memory and
displayed in a buffer as
 <code>
  ^@
 </code>
 .
</p>
<p>
 See
 <code>
  man 7 ascii
 </code>
 and
 <code>
  :h NL-used-for-Nul
 </code>
 for more information.
</p>
<h4>
 Bracketed paste (or why do I have to set 'paste' all the time?)
</h4>
<p>
 Bracketed paste mode allows terminal emulators to distinguish between typed text
and pasted text.
</p>
<p>
 Did you ever tried pasting code into Vim and afterwards everything seemed messed
up?
</p>
<p>
 This only happens if you paste via
 <code>
  cmd+v
 </code>
 ,
 <code>
  shift-insert
 </code>
 ,
 <code>
  middle-click
 </code>
 etc.
because then you're just throwing text at the terminal emulator. Vim doesn't
know that you just pasted the text, it thinks you're an extremely fast typist.
Accordingly it tries to indent the lines and fails.
</p>
<p>
 Obviously this is not an issue, if you paste using Vim's registers, e.g.
 <code>
  "+p
 </code>
 ,
because then Vim knows that you're actually pasting.
</p>
<p>
 To workaround this, you have to
 <code>
  :set paste
 </code>
 , so it gets pasted as-is. See
 <code>
  :h
'paste'
 </code>
 and
 <code>
  :h 'pastetoggle'
 </code>
 .
</p>
<p>
 If you're fed up with toggling
 <code>
  'paste'
 </code>
 all the time, have a look at this fine
plugin that does it for you:
 <a href="https://github.com/ConradIrwin/vim-bracketed-paste">
  bracketed-paste
 </a>
 .
</p>
<p>
 Additional read from the same author as the plugin:
 <a href="http://cirw.in/blog/bracketed-paste">
  here
 </a>
 .
</p>
<p>
 <strong>
  Neovim
 </strong>
 : Neovim tries to make all of this much more seamless and sets
bracketed paste mode automatically if the terminal emulator supports it.
</p>
<h4>
 Delays when using escape key in terminal
</h4>
<p>
 If you live in the command-line, you probably use a so-called
 <em>
  terminal
emulator
 </em>
 like xterm, gnome-terminal, iTerm2, etc. (opposed to a real
 <a href="https://en.wikipedia.org/wiki/Computer_terminal">
  terminal
 </a>
 ).
</p>
<p>
 Like their ancestors, terminal emulators use
 <a href="https://en.wikipedia.org/wiki/Escape_sequence">
  escape
sequences
 </a>
 (or
 <em>
  control
sequences
 </em>
 ) to control things like moving the cursor, changing text colors, etc.
They're simply strings of ASCII characters starting with an escape character
(displayed in
 <a href="https://en.wikipedia.org/wiki/Caret_notation">
  caret notation
 </a>
 as
 <code>
  ^[
 </code>
 ). When such a string arrives, the terminal emulator looks up the
accompanying action in the
 <a href="https://en.wikipedia.org/wiki/Terminfo">
  terminfo
 </a>
 database.
</p>
<p>
 To make the problem clearer, I'll explain mapping timeouts first. They always
happen when there's ambiguity between mappings:
</p>
<p>
 <code>
  vim
:nnoremap ,a  :echo 'foo'<cr>
:nnoremap ,ab :echo 'bar'<cr>
 </code>
</p>
<p>
 Both mappings work as expected, but when typing
 <code>
  ,a
 </code>
 , there will be a delay of 1
second, because Vim waits whether the user keys in another
 <code>
  b
 </code>
 or not.
</p>
<p>
 Escape sequences pose the same problem:
</p>
<ul>
 <li>
  <code>
   <esc>
  </code>
  is used a lot for returning to normal mode or quitting an action.
 </li>
 <li>
  Cursor keys are encoded using escape sequences.
 </li>
 <li>
  Vim expects
  <kbd>
   Alt
  </kbd>
  (also called
  <em>
   Meta key
  </em>
  ) to send a proper 8-bit
encoding with the high bit set, but many terminal emulators don't support it
(or don't enable it by default) and send an escape sequence instead.
 </li>
</ul>
<p>
 You can test the above like this:
 <code>
  vim -u NONE -N
 </code>
 and type
 <code>
  i<c-v><left>
 </code>
 and
you'll see a sequence inserted that starts with
 <code>
  ^[
 </code>
 which denotes the escape
character.
</p>
<p>
 Putting it in a nutshell, Vim has a hard time distinguishing between a typed
 <code>
  <esc>
 </code>
 character and a proper escape sequence.
</p>
<p>
 By default Vim uses
 <code>
  :set timeout timeoutlen=1000
 </code>
 , so it delays on ambiguity of
mappings
 <em>
  and
 </em>
 key codes by 1 second. This is a sane value for mappings, but you
can define the key code timeout on its own which is the most common workaround
for this entire issue:
</p>
<p>
 <code>
  vim
set timeout           " for mappings
set timeoutlen=1000   " default value
set ttimeout          " for key codes
set ttimeoutlen=10    " unnoticeable small value
 </code>
</p>
<p>
 Under
 <code>
  :h ttimeout
 </code>
 you find a small table showing the relationship between
these options.
</p>
<p>
 If you're using tmux between Vim and your terminal emulator, also put this in
your
 <code>
  ~/.tmux.conf
 </code>
 :
</p>
<p>
 <code>
  tmux
set -sg escape-time 0
 </code>
</p>
<h2>
 List of colorschemes
</h2>
<p>
 Here's a list of commonly used colorschemes:
</p>
<ul>
 <li>
  <a href="https://github.com/plan9-for-vimspace/acme-colors">
   acme-colors
  </a>
  <sup>
   &#9733 8, pushed 263 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/chriskempson/base16-vim">
   base16
  </a>
  <sup>
   &#9733 754, pushed 77 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/whatyouhide/vim-gotham">
   gotham
  </a>
  <sup>
   &#9733 523, pushed 13 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/morhetz/gruvbox">
   gruvbox
  </a>
  <sup>
   &#9733 1573, pushed 13 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/mhinz/vim-janah">
   janah
  </a>
  <sup>
   &#9733 40, pushed 78 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/nanotech/jellybeans.vim">
   jellybeans
  </a>
  <sup>
   &#9733 908, pushed 43 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jonathanfilip/vim-lucius">
   lucius
  </a>
  <sup>
   &#9733 190, pushed 302 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/tomasr/molokai">
   molokai
  </a>
  <sup>
   &#9733 1777, pushed 174 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/jpo/vim-railscasts-theme">
   railscasts
  </a>
  <sup>
   &#9733 206, pushed 336 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/junegunn/seoul256.vim">
   seoul256
  </a>
  <sup>
   &#9733 484, pushed 36 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/altercation/vim-colors-solarized">
   solarized
  </a>
  (or a lighter variant:
  <a href="https://github.com/romainl/flattened">
   flattened
  </a>
  )
  <sup>
   &#9733 3824, pushed 11 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/chriskempson/vim-tomorrow-theme">
   tomorrow
  </a>
  <sup>
   &#9733 205, pushed 232 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/tpope/vim-vividchalk">
   vividchalk
  </a>
  <sup>
   &#9733 223, pushed 1522 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/kabbamine/yowish.vim">
   yowish
  </a>
  <sup>
   &#9733 59, pushed 7 days ago
  </sup>
 </li>
</ul>
