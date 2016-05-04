<h1>
 Awesome LaTeX
</h1>
<p>
 This is a curated list of awesome stuff for the (La)TeX typesetting system.
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
 <a href="https://codeclimate.com/github/egeerardyn/awesome-LaTeX">
  <img alt="Issue Count" src="https://codeclimate.com/github/egeerardyn/awesome-LaTeX/badges/issue_count.svg"/>
 </a>
 <a href="LICENSE.md">
  <img alt="License: CC BY-SA 4.0" src="https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg?style=flat"/>
 </a>
</p>
<h2>
 Contents
</h2>
<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->
<ul>
 <li>
  <a href="#awesome-latex">
   Awesome LaTeX
  </a>
  <ul>
   <li>
    <a href="#contents">
     Contents
    </a>
   </li>
   <li>
    <a href="#distributions">
     Distributions
    </a>
   </li>
   <li>
    <a href="#engines">
     Engines
    </a>
    <ul>
     <li>
      <a href="#latex-formulas-on-the-web">
       LaTeX formulas on the web
      </a>
     </li>
    </ul>
   </li>
   <li>
    <a href="#editors">
     Editors
    </a>
    <ul>
     <li>
      <a href="#latex-focussed">
       LaTeX-focussed
      </a>
     </li>
     <li>
      <a href="#general-purpose-text-editors">
       General purpose text editors
      </a>
     </li>
     <li>
      <a href="#online-editors">
       Online editors
      </a>
     </li>
    </ul>
   </li>
   <li>
    <a href="#bibliography-tools">
     Bibliography tools
    </a>
   </li>
   <li>
    <a href="#misc-tools">
     Misc. Tools
    </a>
   </li>
   <li>
    <a href="#latex-compatible-gui-tools">
     LaTeX-compatible GUI tools
    </a>
   </li>
   <li>
    <a href="#packages">
     Packages
    </a>
    <ul>
     <li>
      <a href="#tables">
       Tables
      </a>
     </li>
     <li>
      <a href="#graphics">
       Graphics
      </a>
      <ul>
       <li>
        <a href="#pstricks">
         PSTricks
        </a>
       </li>
       <li>
        <a href="#tikz">
         TikZ
        </a>
       </li>
      </ul>
     </li>
    </ul>
   </li>
   <li>
    <a href="#templates">
     Templates
    </a>
   </li>
   <li>
    <a href="#symbols">
     Symbols
    </a>
   </li>
   <li>
    <a href="#resources">
     Resources
    </a>
   </li>
   <li>
    <a href="#tutorials">
     Tutorials
    </a>
   </li>
   <li>
    <a href="#books">
     Books
    </a>
   </li>
   <li>
    <a href="#blogs">
     Blogs
    </a>
   </li>
   <li>
    <a href="#social-media">
     Social media
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#meta-awesome-latex">
   Meta Awesome-LaTeX
  </a>
  <ul>
   <li>
    <a href="#legend">
     Legend
    </a>
   </li>
  </ul>
 </li>
</ul>
<!-- /TOC -->
<h2>
 Distributions
</h2>
<ul>
 <li>
  <a href="https://tug.org/mactex/">
   MacTeX
  </a>
  - Most common LaTeX distribution for Mac OS X, basically TeXLive with some Mac-specific tools added.
  <img alt="Mac" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/apple.svg"/>
 </li>
 <li>
  <a href="http://www.tug.org/texlive/">
   TeX Live
  </a>
  - Most common LaTeX distribution for Unices and Linux, but also works on Windows.
  <img alt="Linux" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/linux.svg"/>
  <img alt="Windows" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/windows.svg"/>
 </li>
 <li>
  <a href="http://miktex.org">
   MikTeX
  </a>
  - Most common LaTeX distribution for Windows (only).
  <img alt="Windows" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/windows.svg"/>
 </li>
</ul>
<h2>
 Engines
</h2>
<ul>
 <li>
  <a href="http://www.tug.org/applications/pdftex/">
   pdfTeX
  </a>
  - TeX compiler that produces PDF files immediately instead of DVI files (nowadays, this is the standard compiler for many users).
  <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
 </li>
 <li>
  <a href="http://xetex.sourceforge.net">
   XeTeX
  </a>
  - TeX compiler that provides better unicode and font support than TeX/pdfTeX (i.e. you can use the  fonts of your operating system instead of only TeX fonts).
  <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
 </li>
 <li>
  <a href="http://www.luatex.org">
   LuaTeX
  </a>
  - (La)TeX compiler that supports Lua code for scripting and has improved unicode and font support than standard TeX/pdfTeX.
  <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
 </li>
</ul>
<h3>
 LaTeX formulas on the web
</h3>
<ul>
 <li>
  <a href="https://www.mathjax.org">
   MathJaX
  </a>
  - JavaScript engine to render mathematical formulas on the web. The outcome looks really slick.
  <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
 </li>
 <li>
  <a href="http://www.forkosh.com/mimetex.html">
   mimeTeX
  </a>
  - mimeTeX is a rather old tool to render LaTeX formulas to PNG figures for your web site, without actually needing a LaTeX installation on your server.
  <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
 </li>
 <li>
  <a href="http://www.forkosh.com/mathtex.html">
   mathTeX
  </a>
  - mathTeX is the successor of mimeTeX: it produces nicer-looking images but it requires LaTeX to be installed on your server.
  <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
 </li>
</ul>
<h2>
 Editors
</h2>
<p>
 Because editing LaTeX code with notepad is not awesome.
</p>
<h3>
 LaTeX-focussed
</h3>
<p>
 Some of the most awesome editor for LaTeX do just that: edit LaTeX
</p>
<ul>
 <li>
  <a href="http://kile.sourceforge.net">
   Kile
  </a>
  - Just a great LaTeX editor originally from the Linux/KDE community, but runs just fine on Windows and OS X as well.
  <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
 </li>
 <li>
  <a href="http://www.xm1math.net/texmaker/">
   TeXMaker
  </a>
  - Pretty good alternative to Kile.
 </li>
 <li>
  <a href="http://www.texstudio.org">
   TeXStudio
  </a>
  - Cross-platform LaTeX editor that stems from TeXMaker.
 </li>
 <li>
  <a href="http://www.winedt.com">
   WinEdt
  </a>
  - The LaTeX editor many people swear by. Only for
  <img alt="Windows" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/windows.svg"/>
  .
 </li>
 <li>
  <a href="http://www.texniccenter.org">
   TeXnicCenter
  </a>
  - A quite old but free and decent editor for LaTeX.
  <img alt="Windows" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/windows.svg"/>
 </li>
 <li>
  <a href="https://www.lyx.org">
   LyX
  </a>
  - Cross-platform WYSIWYM editor that uses LaTeX behind the scenes to render documents.
  <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
 </li>
 <li>
  <a href="http://pages.uoregon.edu/koch/texshop/">
   TeXshop
  </a>
  - No-nonsense editor for LaTeX documents which is included in MacTeX.
  <img alt="Mac" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/apple.svg"/>
 </li>
 <li>
  <a href="https://www.tug.org/texworks/">
   TeXWorks
  </a>
  - No-nonsense editor for LaTeX code, modeled after TeXShop, but this one is cross-platform.
  <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
 </li>
 <li>
  <a href="http://www.bakoma-tex.com">
   BakomaTex
  </a>
  - Commercial LaTeX editor that allows to edit your document both using its source code and WYSIWYG.
 </li>
 <li>
  <a href="http://www.inlage.com/home">
   Inlage
  </a>
  - Commercial LaTeX editor with handwritten formula recognition, Excel importing and more nifty features.
  <img alt="Windows" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/windows.svg"/>
 </li>
</ul>
<h3>
 General purpose text editors
</h3>
<p>
 These editors are no one-trick ponies: sure, they edit LaTeX, but they can do a lot more!
</p>
<ul>
 <li>
  <p>
   <a href="https://atom.io">
    Atom
   </a>
   <a href="https://github.com/mehcode/awesome-atom">
    <img alt="Atom" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
   </a>
   <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
  </p>
  <ul>
   <li>
    <a href="https://atom.io/packages/latextools">
     LaTeXTools
    </a>
    - An Atom port of the Sublime Text package of the same name.
    <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
   </li>
  </ul>
 </li>
 <li>
  <p>
   <a href="http://www.sublimetext.com">
    Sublime Text
   </a>
   <a href="https://github.com/dreikanter/sublime-bookmarks">
    <img alt="Sublime Text" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
   </a>
  </p>
  <ul>
   <li>
    <a href="http://www.latexing.com">
     LaTeXing
    </a>
    - Commercial plug-in to edit LaTeX.
   </li>
   <li>
    <a href="https://github.com/SublimeText/LaTeXTools">
     LaTeXTools
    </a>
    <span>
     &#9733 1172, pushed 2 days ago
    </span>
    - Free LaTeX plugin for Sublime Text.
    <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
   </li>
  </ul>
 </li>
 <li>
  <p>
   <a href="https://www.gnu.org/software/emacs/">
    Emacs
   </a>
   <a href="https://github.com/emacs-tw/awesome-emacs">
    <img alt="Emacs" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
   </a>
   <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
  </p>
  <ul>
   <li>
    <a href="https://www.gnu.org/software/auctex/">
     AucTeX
    </a>
    - Emacs plugin for LaTeX that also shows a preview of equations and figures.
    <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
   </li>
  </ul>
 </li>
 <li>
  <p>
   <a href="http://www.vim.org">
    Vim
   </a>
   <a href="https://github.com/mhinz/vim-galore">
    <img alt="Vim" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
   </a>
   <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
  </p>
  <ul>
   <li>
    <a href="http://vim-latex.sourceforge.net">
     Vim-LaTeX
    </a>
    <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
   </li>
   <li>
    <a href="https://github.com/xuhdev/vim-latex-live-preview">
     LaTeX Live Preview
    </a>
    <span>
     &#9733 127, pushed 48 days ago
    </span>
    - Instantly previews your LaTeX document.
    <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
   </li>
  </ul>
 </li>
</ul>
<h3>
 Online editors
</h3>
<p>
 Online editors that allow you to edit documents collaboratively.
</p>
<ul>
 <li>
  <a href="https://www.authorea.com">
   Authorea
  </a>
  - Online editor with built-in git support and bibliography tools.
 </li>
 <li>
  <a href="https://www.sharelatex.com">
   ShareLaTeX
  </a>
  - Has pretty great LaTeX documentation and simple version control.
 </li>
 <li>
  <a href="https://www.overleaf.com">
   Overleaf
  </a>
  - Online editor, also with a WYSIWYM editor and git support.
 </li>
 <li>
  <a href="https://papeeria.com">
   Papeeria
  </a>
  - Online editor with built-in git support.
 </li>
 <li>
  <a href="http://jaxedit.com/page/jaxedit.html">
   JaxEdit
  </a>
  - Online LaTeX editor with Live Preview and nice presentation mode.
 </li>
</ul>
<h2>
 Bibliography tools
</h2>
<ul>
 <li>
  <a href="http://jabref.sourceforge.net">
   JabRef
  </a>
  - Very powerful cross-platform (Java) bibtex editor. The GUI looks quite dated, though.
  <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
 </li>
 <li>
  <a href="http://bibdesk.sourceforge.net">
   Bibdesk
  </a>
  - Great bibliography editor for
  <img alt="Mac" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/apple.svg"/>
  .
 </li>
 <li>
  <a href="https://www.zotero.org">
   Zotero
  </a>
  - Reference manager for your browser that also exports to bibtex and integrates with many LaTeX editors.
 </li>
 <li>
  <a href="https://www.mendeley.com">
   Mendeley
  </a>
  - Both an app and cloud client to manage your references and PDFs. Can sync out to a bibtex file for your LaTeX workflow.
 </li>
</ul>
<h2>
 Build Tools
</h2>
<p>
 Compiling LaTeX documents can be tedious, build tools help you to manage the compilation process.
</p>
<ul>
 <li>
  <a href="https://www.ctan.org/pkg/arara">
   Arara
  </a>
  (
  <a href="https://github.com/cereda/arara">
   GitHub repo
  </a>
  ) - Simple tool that allows you to specify which tools to call inside your document and it can be extended quite easily.
  <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
 </li>
 <li>
  <a href="https://www.ctan.org/pkg/latexmk">
   latexmk
  </a>
  - Build tool that is the commonly used by many LaTeX editors (LaTeXing, TeXShop, ...) to build your LaTeX files.
  <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
 </li>
</ul>
<h2>
 Misc. Tools
</h2>
<ul>
 <li>
  <a href="http://pandoc.org">
   Pandoc
  </a>
  - This program converts almost any document format (LaTeX, DOC, markdown, ...) to almost any other format. A great tool to aid workflows where multiple formats are used.
  <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
 </li>
 <li>
  <a href="https://www.codecogs.com/latex/eqneditor.php">
   Codecogs Eqn Editor
  </a>
  - Online LaTeX equation editor that allows you to produce figures containing an equation.
 </li>
 <li>
  <a href="http://www.chachatelier.fr/latexit/">
   LaTeXiT
  </a>
  - LaTeXit is an equation editor that makes it easy to drag-and-drop rendered equations (as PDF, PNG, ...) into your non-LaTeX documents on the Mac.
  <img alt="Mac" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/apple.svg"/>
 </li>
 <li>
  <a href="http://klatexformula.sourceforge.net">
   KLaTeXFormula
  </a>
  - Cross-platform alternative for LaTeXit.
  <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
 </li>
 <li>
  <a href="http://equalx.sourceforge.net">
   EqualX
  </a>
  - Graphical LaTeX formula editor.
  <img alt="Windows" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/windows.svg"/>
  <img alt="Linux" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/linux.svg"/>
  <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
 </li>
 <li>
  <a href="http://baruch.ev-en.org/proj/chktex/">
   ChkTeX
  </a>
  - Linter / code checker for LaTeX documents.
  <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
 </li>
</ul>
<h2>
 LaTeX-compatible GUI tools
</h2>
<ul>
 <li>
  <a href="http://www.tikzedt.org">
   TikzEdt
  </a>
  (also:
  <a href="https://github.com/hchapman/tikzedt">
   GitHub repo
  </a>
  ) - WYSIWYG and text-based editor for TikZ pictures.
  <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
 </li>
 <li>
  <a href="https://github.com/fredokun/TikZ-Editor">
   TikZ-Editor
  </a>
  <span>
   &#9733 59, pushed 474 days ago
  </span>
  - Live-previewing editor for TikZ figures.
  <img alt="Mac" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/apple.svg"/>
  <img alt="Linux" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/linux.svg"/>
  <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
 </li>
 <li>
  <a href="http://ipe.otfried.org">
   IPE
  </a>
  - Drawing tool that integrates well with LaTeX commands and documents.
  <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
 </li>
 <li>
  <a href="http://www.geogebra.org/cms/">
   GeoGebra
  </a>
  - Cross-platform geometry tool with output to TikZ.
  <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
 </li>
 <li>
  <a href="https://wiki.gnome.org/Apps/Dia">
   Dia
  </a>
  - Cross-platform diagramming tool that can export to PSTricks and MetaPost code.
  <img alt="foss" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
 </li>
</ul>
<h2>
 Packages
</h2>
<ul>
 <li>
  <a href="http://ctan.org">
   CTAN
  </a>
  - The Comprehensive TeX Archive Network is the place to look for useful packages and documentation.
 </li>
</ul>
<h3>
 Tables
</h3>
<ul>
 <li>
  <a href="https://www.ctan.org/pkg/excel2latex?lang=en">
   Excel2LaTeX
  </a>
  - Excel (2010 and older) macros to produce LaTeX
  <code>
   tabular
  </code>
  code.
  <img alt="Windows" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/windows.svg"/>
  <img alt="Mac" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/apple.svg"/>
 </li>
 <li>
  <a href="http://www.freecode.com/projects/csv2latex">
   csv2latex
  </a>
  - Converts CSV files from your favorite programs to LaTeX
  <code>
   tabular
  </code>
  s.
  <img alt="Linux" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/linux.svg"/>
  <img alt="Mac" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/apple.svg"/>
 </li>
 <li>
  <a href="http://www.tablesgenerator.com">
   Tables Generator
  </a>
  - This website provides a graphical interface to input your table and produces properly-formatted code for LaTeX, Markdown, HTML, ...
 </li>
 <li>
  <a href="https://www.ctan.org/pkg/pgfplotstable?lang=en">
   pgfplotstable
  </a>
  - This package dis­plays nu­mer­i­cal ta­bles rounded to de­sired pre­ci­sion in var­i­ous dis­play for­mats. It can even read CSV files to include directly in your LaTeX document.
 </li>
</ul>
<h3>
 Graphics
</h3>
<h4>
 PSTricks
</h4>
<p>
 PSTricks is a great library to draw figures for inclusion in PostScript/DVI files.
</p>
<h4>
 TikZ
</h4>
<p>
 TikZ is an awesome package with many plugins that allow you to create figures from within your LaTeX documents.
Typically, it is easier to get to work with
 <code>
  pdflatex
 </code>
 than PSTricks is.
</p>
<ul>
 <li>
  <a href="http://www.texample.net">
   TeXample
  </a>
  - Blog about LaTex, with a big collection of TikZ figures.
 </li>
 <li>
  <a href="http://sciences-indus-cpge.papanicola.info/-LaTeX-en-SI-">
   LaTeX en SI
  </a>
  - Useful website with some custom packages to draw special plots (Bode, Nyquist, electrical schematics, block schematics, ...) using TikZ. Note that everything is in French.
 </li>
 <li>
  <a href="http://altermundus.com/pages/tkz/index.html">
   tkz
  </a>
  - A collection of TikZ-based packages to make plots and graphs.
 </li>
 <li>
  <a href="http://pgfplots.sourceforge.net">
   pgfplots
  </a>
  - A truely awesome plotting library on top of and in the style of TikZ/pgf. This library can load in CSV data files, perform some calculations and create beautiful plots.
 </li>
 <li>
  <a href="http://bit.ly/gNfVn9">
   A very minimal introduction to TikZ (PDF)
  </a>
  - A short introductory document to the world of TikZ, written by Jacques Crémer.
 </li>
</ul>
<h2>
 Templates
</h2>
<ul>
 <li>
  <a href="http://www.latextemplates.com">
   LaTeX templates
  </a>
  - Collection of templates for papers, posters, resumés, theses, books, presentations, … for LaTeX.
 </li>
 <li>
  <a href="http://www.howtotex.com/category/templates/">
   HowtoTeX: templates
  </a>
  - Different templates for LaTeX under a CC-NC-SA license.
 </li>
</ul>
<h2>
 Symbols
</h2>
<ul>
 <li>
  <a href="http://www.ctan.org/tex-archive/info/symbols/comprehensive/">
   Comprehensive LaTeX symbol list
  </a>
  - A very extensive list of symbols for LaTeX. Available in
  <a href="http://mirrors.ctan.org/info/symbols/comprehensive/symbols-a4.pdf">
   A4
  </a>
  and
  <a href="http://mirrors.ctan.org/info/symbols/comprehensive/symbols-letter.pdf">
   letter
  </a>
  sizes.
 </li>
 <li>
  <a href="http://detexify.kirelabs.org/classify.html">
   Detexify
  </a>
  - You draw the symbol and this site/app will tell you the LaTeX command.
 </li>
</ul>
<h2>
 Resources
</h2>
<ul>
 <li>
  <a href="https://www.tug.org">
   TUG
  </a>
  - The TeX User Group is a way to get in touch with other (La)TeX users.
 </li>
 <li>
  <a href="http://texdoc.net">
   TeXDoc
  </a>
  - Online interface to the
  <code>
   texdoc
  </code>
  utility to browse LaTeX packages and documentation.
 </li>
 <li>
  <a href="http://www.dickimaw-books.com/latexresources.html">
   Dickimaw Books: LaTeX resources
  </a>
  - Great overview of resources useful for LaTeX.
 </li>
 <li>
  <a href="http://www.tug.org/texshowcase/">
   TUG: TeX showcase
  </a>
  - Website from the TUG that shows some examples of what LaTeX can do.
 </li>
 <li>
  <a href="http://www.texample.net">
   TeXample
  </a>
  - Blog about LaTex, with a big collection of TikZ figures.
 </li>
 <li>
  <a href="http://latex-cookbook.net">
   LaTeX cookbook
  </a>
  - Sibling of TeXample, contains quite a bit of example code.
 </li>
 <li>
  <a href="http://www.howtotex.com/general/12-great-resources-for-getting-started-with-latex/">
   12 Great resources for getting started with LaTeX
  </a>
  - Nice overview of useful resources for beginners.
 </li>
 <li>
  <a href="https://github.com/MartinThoma/LaTeX-examples/">
   MartinThoma's LaTeX example
  </a>
  - GitHub repository containing example LaTeX documents.
 </li>
 <li>
  <a href="http://latex.howtotex.com">
   HowtoTeX LaTeX
  </a>
  - Start page with useful resources for LaTeX users.
 </li>
 <li>
  <a href="http://mactex-wiki.tug.org/wiki/index.php/TeX_Extras">
   MacTeX Wiki: TeX Extras
  </a>
  - Overview of useful tools for LaTeX. Many of them are specific for Mac, but quite a bit are useful for other platforms as well.
 </li>
 <li>
  <a href="http://latex-community.org/index.php">
   LaTeX community
  </a>
  - Forum and blog about LaTeX.
 </li>
</ul>
<h2>
 Tutorials
</h2>
<ul>
 <li>
  <a href="http://mirrors.ctan.org/info/lshort/english/lshort.pdf">
   The (Not So) Short Introduction to LaTeX2e
  </a>
  - A very comprehensive introduction to LaTeX.
 </li>
</ul>
<h2>
 Books
</h2>
<ul>
 <li>
  <a href="https://en.wikibooks.org/wiki/LaTeX">
   WikiBooks: LaTeX
  </a>
  - The LaTeX wikibook. Not really a paper book, but it is equally extensive.
 </li>
 <li>
  <a href="http://www.informit.com/store/latex-companion-9780201362992">
   The LaTeX Companion, F. Mittelbach (2004)
  </a>
 </li>
 <li>
  <a href="http://www.informit.com/store/latex-graphics-companion-9780321508928">
   LaTeX Graphics Companion, M. Goossens (2007)
  </a>
 </li>
</ul>
<h2>
 Blogs
</h2>
<ul>
 <li>
  <a href="http://texblog.net">
   TeXblog
  </a>
  - Blog about LaTeX and everything related.
 </li>
</ul>
<h2>
 Social media
</h2>
<ul>
 <li>
  <a href="https://www.linkedin.com/groups/1600297">
   LinkedIn: TeX/LaTeX User Group
  </a>
 </li>
 <li>
  <a href="https://twitter.com/TeXtip">
   Twitter: @TeXtip
  </a>
  - Tips related to (La)TeX by
  <a href="http://www.johndcook.com/">
   John D. Cook
  </a>
  .
 </li>
 <li>
  <a href="http://tex.stackexchange.com">
   TeX.StackExchange
  </a>
  - StackExchange TeX section.
 </li>
</ul>
<hr/>
<!-- Icons -->
<h1>
 Meta Awesome-LaTeX
</h1>
<p>
 If you want to contribute, please do read our
 <a href="CONTRIBUTING.md">
  CONTRIBUTING
 </a>
 guidelines.
</p>
<h2>
 Legend
</h2>
<p>
 The icons indicating Mac, Linux and Windows compatibility show when a program is
 <em>
  only
 </em>
 available for those platforms. So absence of those icons means that the software is fully cross-platform.
</p>
<p>
 |       Logo          | Description                                            |
|:-------------------:|:-------------------------------------------------------|
|
 <img alt="Mac" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/apple.svg"/>
 |
 <a href="http://www.apple.com/osx/">
  Mac OS X
 </a>
 |
|
 <img alt="Linux" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/linux.svg"/>
 |
 <a href="http://www.linux.org">
  GNU/Linux
 </a>
 |
|
 <img alt="Windows" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/windows.svg"/>
 |
 <a href="https://www.microsoft.com/windows">
  Microsoft Windows
 </a>
 |
|
 <img alt="FOSS" src="https://cdn.rawgit.com/egeerardyn/awesome-LaTeX/700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg"/>
 |
 <a href="https://opensource.org">
  Free Open-Source Software
 </a>
 |
</p>
<hr/>
<p>
 All trademarks are property of their respective owners.
</p>
