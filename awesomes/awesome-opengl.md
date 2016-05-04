<h1>
 awesome-opengl
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<p>
 A curated list of awesome OpenGL libraries, debuggers and resources. Inspired by awesome-... stuff.
</p>
<ul>
 <li>
  [Articles] (#articles)
 </li>
 <li>
  [Books] (#books)
 </li>
 <li>
  [Debug] (#debug)
 </li>
 <li>
  [GLSL Editors] (#glsl-editors)
 </li>
 <li>
  [Libraries] (#libraries)
 </li>
 <li>
  [Profile Loaders] (#profile-loaders)
 </li>
 <li>
  [References] (#references)
 </li>
 <li>
  [Talks] (#talks)
 </li>
 <li>
  [Videos] (#videos)
 </li>
 <li>
  [Websites] (#websites)
 </li>
</ul>
<h2>
 Articles
</h2>
<p>
 <em>
  OpenGL articles (non-tutorials)
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/LWJGL/lwjgl3-wiki/wiki/2.6.1.-Ray-tracing-with-OpenGL-Compute-Shaders-%28Part-I%29">
   (2014) Ray tracing with OpenGL Compute Shaders
  </a>
  by
  <strong>
   Kai Burjack
  </strong>
  - A detailed tutorial series about ray tracing using OpenGL (LWJGL).
 </li>
 <li>
  <a href="http://richg42.blogspot.com.au/2014/05/things-that-drive-me-nuts-about-opengl.html">
   (2014) Things that drive me nuts about OpenGL
  </a>
  by
  <strong>
   Rich Geldreich
  </strong>
  - A constructive (or not) criticism of GL API.
 </li>
 <li>
  <a href="https://fgiesen.wordpress.com/2011/07/09/a-trip-through-the-graphics-pipeline-2011-index">
   (2011) A trip through the graphics pipeline
  </a>
  by
  <strong>
   Fabian Giesen
  </strong>
  - A compreheensive and rich series about the D3D/OpenGL graphics pipeline.
 </li>
 <li>
  <a href="http://duriansoftware.com/joe/An-intro-to-modern-OpenGL.-Chapter-1:-The-Graphics-Pipeline.html">
   (2010) What is OpenGL?
  </a>
  by
  <strong>
   Joe Groff
  </strong>
  - A brief introduction to the building blocks of OpenGL.
 </li>
</ul>
<h2>
 Books
</h2>
<p>
 <em>
  Popular books about OpenGL
 </em>
</p>
<ul>
 <li>
  <a href="http://www.amazon.com/dp/1558603875">
   A Trip Down the Graphics Pipeline
  </a>
  by
  <strong>
   Jim Blinn
  </strong>
  - A popular book that contains wealth information about the graphics pipeline, and of the best sources to learn the core concepts of Computer Graphics.
 </li>
 <li>
  <a href="http://www.amazon.com/dp/0321399528">
   Computer Graphics
  </a>
  by
  <strong>
   John F. Hughes, et al.
  </strong>
  - Computer Graphics is indeed a must for anyone being involved in the design and implementation of Computer Graphics algorithms. However, this is not a OpenGL focused book, but contains valuable demonstrations of the technology.
 </li>
 <li>
  <a href="http://www.amazon.com/dp/0132545233">
   Interactive Computer Graphics
  </a>
  by
  <strong>
   Edward Angel and Dave Shreiner
  </strong>
  - A very dense book, covering several aspects at once. It pro provides several examples using OpenGL, but if you are trying to learn OpenGL on your own you might not find this helpful.
 </li>
 <li>
  <a href="http://www.amazon.com/dp/0321933885">
   OpenGL ES 3.0 Programming Guide
  </a>
  by
  <strong>
   Dan Ginsburg, et al.
  </strong>
  - It presents all the necessary information to use the OpenGL ES 3.0 API in a clear manner.
 </li>
 <li>
  <a href="http://www.amazon.com/dp/1439893764">
   OpenGL Insights
  </a>
  by
  <strong>
   Patrick Cozzi, Christophe Riccio
  </strong>
  - A rich and comprehensive resource to learn techniques and tips, covering several advanced topics of OpenGL.
 </li>
 <li>
  <a href="http://www.amazon.com/dp/0321773039">
   OpenGL Programming Guide
  </a>
  by
  <strong>
   Dave Shreiner, et al.
  </strong>
  - This book does a good job covering the basics and providing clear reference of the API.
 </li>
 <li>
  <a href="http://www.amazon.com/dp/0321637631">
   OpenGL Shading Language
  </a>
  by
  <strong>
   Randi J. Rost, et al.
  </strong>
  - A very clear and well written book about Shading Language. Also, it provides several explanations of writing shaders.
 </li>
 <li>
  <a href="http://www.amazon.com/dp/0321712617">
   OpenGL SuperBible
  </a>
  by
  <strong>
   Richard S. Wright, et al.
  </strong>
  - This book it cover the basic concept of computer graphics and clear examples using OpenGL. Definitely, it is a must for beginners.
 </li>
 <li>
  <a href="http://www.amazon.com/dp/1568814240">
   Real-Time Rendering
  </a>
  by
  <strong>
   Tomas Akenine-Moller, Eric Haines and Naty Hoffman
  </strong>
  - This book does a good job at explaining concepts for game engine, basis for game client programming as well as the necessary knowledge for understanding DirectX and OpenGL.
 </li>
</ul>
<h2>
 Debug
</h2>
<p>
 <em>
  Debugging and profiling libraries
 </em>
</p>
<ul>
 <li>
  <a href="http://apitrace.github.io">
   apitrace
  </a>
  - Tools for tracing OpenGL, Direct3D, and other graphics APIs.
 </li>
 <li>
  <a href="http://developer.amd.com/tools-and-sdks/opencl-zone/codexl/">
   CodeXL
  </a>
  - AMD's OpenGL debugger and profiler. It's the most recent version of gDEBugger.
 </li>
 <li>
  <a href="http://glsl-debugger.github.io">
   GL-SL Debugger
  </a>
  - GLSL-Debugger is a tool for debugging OpenGL programs.
 </li>
 <li>
  <a href="https://github.com/dtrebilco/glintercept">
   GLIntercept
  </a>
  - An OpenGL function call interceptor for Windows.
  <sup>
   8 GitHub links in total 74 links, ★ 68, pushed 125 days ago
  </sup>
  <sup>
   &#9733 68, pushed 125 days ago
  </sup>
 </li>
 <li>
  <a href="https://software.intel.com/en-us/gpa">
   Intel-GPA
  </a>
  - Intel's OpenGL Graphics Performance Analyzer.
 </li>
 <li>
  <a href="https://developer.nvidia.com/nvidia-nsight-visual-studio-edition">
   NVIDIA® Nsight™
  </a>
  - A development platform for graphics applications.
 </li>
 <li>
  <a href="https://github.com/ValveSoftware/vogl">
   vogl
  </a>
  - OpenGL capture and playback debugger developed by Valve.
  <sup>
   8 GitHub links in total 74 links, ★ 1233, pushed 6 days ago
  </sup>
  <sup>
   &#9733 1233, pushed 6 days ago
  </sup>
 </li>
</ul>
<h2>
 GLSL Editors
</h2>
<p>
 <em>
  Online GLSL Editors
 </em>
</p>
<ul>
 <li>
  <a href="http://glslsandbox.com">
   GLSL Sandbox
  </a>
  - Online live editor for fragment shaders.
 </li>
 <li>
  <a href="http://glslb.in">
   GLSLbin
  </a>
  - A fragment shader sandbox supporting
  <a href="https://github.com/stackgl/glslify">
   glslify
  </a>
  .
 </li>
 <li>
  <a href="http://shdr.bkcore.com">
   SHDR Editor
  </a>
  - Live GLSL shader editor, viewer and validator.
 </li>
 <li>
  <a href="https://www.shadertoy.com">
   Shader Toy
  </a>
  - Most popular live editor for fragment shaders.
 </li>
 <li>
  <a href="http://shaderfrog.com/">
   ShaderFrog
  </a>
  - WebGL Shader Editor and Composer
 </li>
</ul>
<h2>
 Libraries
</h2>
<p>
 <em>
  Useful libraries for OpenGL applications
 </em>
</p>
<ul>
 <li>
  <a href="http://assimp.sourceforge.net">
   assimp
  </a>
  - A portable library to import 3D models in a uniform manner.
 </li>
 <li>
  <a href="http://bulletphysics.org/wordpress">
   Bullet
  </a>
  - It provides state of the art collision detection, soft body and rigid body dynamics.
 </li>
 <li>
  <a href="http://freeglut.sourceforge.net">
   freeGLUT
  </a>
  - A mature library that allows to create/manage windows containing OpenGL contexts.
 </li>
 <li>
  <a href="http://www.glfw.org">
   GLFW
  </a>
  - A modern library for creating/interact windows with OpenGL contexts.
 </li>
 <li>
  <a href="http://glm.g-truc.net/0.9.6/index.html">
   glm
  </a>
  - A mathematics library for graphics software based on the GLSL specifications.
 </li>
 <li>
  <a href="https://github.com/mosra/magnum">
   Magnum
  </a>
  - Magnum is 2D/3D graphics engine for modern OpenGL.
  <sup>
   8 GitHub links in total 74 links, ★ 738, pushed 2 days ago
  </sup>
  <sup>
   &#9733 738, pushed 2 days ago
  </sup>
 </li>
 <li>
  <a href="http://newtondynamics.com/forum/newton.php">
   Newton
  </a>
  - Newton Dynamics is a cross-platform life-like physics.
 </li>
 <li>
  <a href="http://oglplus.org">
   OGLplus
  </a>
  - A collection of libraries which implement an object-oriented facade over OpenGL.
 </li>
 <li>
  <a href="http://www.libsdl.org">
   SDL
  </a>
  - A library designed to provide low level access to multimedia and graphics hardware.
 </li>
 <li>
  <a href="http://www.sfml-dev.org">
   SFML
  </a>
  - A simple interface to ease the development of games and multimedia applications.
 </li>
 <li>
  <a href="http://www.lonesock.net/soil.html">
   SOIL
  </a>
  - A tiny C library used primarily for uploading textures into OpenGL. (see
  <a href="https://bitbucket.org/SpartanJ/soil2">
   SOIL2
  </a>
  )
 </li>
</ul>
<h2>
 Profile Loaders
</h2>
<p>
 <em>
  Profile loaders for OpenGL
 </em>
</p>
<ul>
 <li>
  <a href="https://github.com/skaslev/gl3w">
   gl3w
  </a>
  - A simple OpenGL core profile loader.
  <sup>
   8 GitHub links in total 74 links, ★ 192, pushed 4 days ago
  </sup>
  <sup>
   &#9733 192, pushed 4 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/Dav1dde/glad">
   glad
  </a>
  - A multi profile loader-generator based on the official specs.
  <sup>
   8 GitHub links in total 74 links, ★ 198, pushed 3 days ago
  </sup>
  <sup>
   &#9733 198, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/nnesse/glbindify">
   glbindify
  </a>
  - A commmand line tool to generate C bindings for OpenGL, wgl, and glX.
  <sup>
   8 GitHub links in total 74 links, ★ 2, pushed 123 days ago
  </sup>
  <sup>
   &#9733 2, pushed 123 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/cginternals/glbinding">
   glbinding
  </a>
  - A profile loader leveraging C++11 features to provide type safety.
  <sup>
   8 GitHub links in total 74 links, ★ 294, pushed 8 days ago
  </sup>
  <sup>
   &#9733 294, pushed 8 days ago
  </sup>
 </li>
 <li>
  <a href="http://glew.sourceforge.net">
   GLEW
  </a>
  - A mature cross-platform library to load OpenGL extensions.
 </li>
 <li>
  <a href="https://bitbucket.org/alfonse/glloadgen/wiki/Home">
   glLoadGen
  </a>
  - A multi profile loader-generator written in Lua.
 </li>
</ul>
<h2>
 References
</h2>
<p>
 <em>
  OpenGL references
 </em>
</p>
<ul>
 <li>
  <a href="http://docs.gl">
   docs.GL
  </a>
  - docs.GL is an alternative documentation for OpenGL.
 </li>
 <li>
  <a href="http://web.eecs.umich.edu/~sugih/courses/eecs487/common/notes/APITables.xml">
   OpenGL API Tables
  </a>
  - Quick reference of API's for several OpenGL and GLSL versions.
 </li>
 <li>
  <a href="https://www.khronos.org/files/opengl43-quick-reference-card.pdf">
   OpenGL Cheat Sheet
  </a>
  - Quick reference card of OpenGL 4.3 commands and syntax.
 </li>
 <li>
  <a href="https://www.opengl.org/sdk/docs">
   OpenGL Docs
  </a>
  - Official documentation website.
 </li>
 <li>
  <a href="https://www.opengl.org/wiki/Main_Page">
   OpenGL Wiki
  </a>
  - Official OpenGL wiki.
 </li>
</ul>
<h2>
 Talks
</h2>
<p>
 <em>
  OpenGL related talks
 </em>
 *
 <a href="http://gdcvault.com/play/1020791/">
  Approaching Zero Driver Overhead in OpenGL
 </a>
 -
 <a href="http://www.slideshare.net/CassEveritt/approaching-zero-driver-overhead">
  Slides
 </a>
 -
 <a href="https://www.reddit.com/r/gamedev/comments/21mbo8/we_are_the_authors_of_approaching_zero_driver">
  AMA Reddit
 </a>
 by
 <strong>
  Cass Everitt, Tim Foley, John McDonald, Graham Sellers
 </strong>
 [1:15:54]
*
 <a href="https://www.youtube.com/watch?v=-bCeNzgiJ8I">
  How Modern OpenGL Can Radically Reduce Driver Overhead
 </a>
 by
 <strong>
  Cass Everitt, John McDonald
 </strong>
 [51:13]
*
 <a href="https://www.youtube.com/watch?v=45O7WTc6k2Y">
  Moving Your Games to OpenGL
 </a>
 by
 <strong>
  Rich Geldreich, Dan Ginsburg, Peter Lohrmann, Jason Mitchell
 </strong>
 [54:45]
</p>
<h2>
 Videos
</h2>
<p>
 <em>
  OpenGL video tutorials
 </em>
</p>
<ul>
 <li>
  <a href="https://www.youtube.com/playlist?list=PLbLaohICnSGUx0zZ4ffxEzQvWEzxWH839">
   CodeAcademy
  </a>
  - Several tutorial videos about modern OpenGL and rendering techniques.
 </li>
 <li>
  <a href="https://www.youtube.com/playlist?list=PLRwVmtr-pp06qT6ckboaOhnm9FxmzHpbY">
   Jamie King
  </a>
  - Compreheensive tutorials about modern OpenGL and Qt.
 </li>
 <li>
  <a href="https://www.youtube.com/playlist?list=PLSPw4ASQYyymu3PfG9gxywSPghnSMiOAW">
   MakingGamesWithBen
  </a>
  - Video tutorials (step-by-step) about OpenGL and game development.
 </li>
 <li>
  <a href="https://www.youtube.com/user/ACMSIGGRAPH/playlists">
   SIGGRAPH
  </a>
  - Popular conference about computer graphics.
 </li>
 <li>
  <a href="https://www.youtube.com/user/thebennybox/playlists">
   thebennybox
  </a>
  - Videos tutorials about OpenGL and game development.
 </li>
 <li>
  <a href="https://www.youtube.com/user/ThinMatrix/playlists">
   ThinMatrix
  </a>
  - Video tutorials about OpenGL and game development using Java.
 </li>
 <li>
  <a href="https://www.youtube.com/playlist?list=PLQVvvaa0QuDdfGpqjkEJSeWKGCP31__wD">
   sentdex
  </a>
  - Videos tutorials about OpenGL (immediate mode) using Python.
 </li>
</ul>
<h2>
 Websites
</h2>
<p>
 <em>
  OpenGL tutorial websites
 </em>
</p>
<ul>
 <li>
  <a href="http://learnopengl.com">
   Learn OpenGL
  </a>
  by
  <strong>
   Joey de Vries
  </strong>
 </li>
 <li>
  <a href="http://web.archive.org/web/20150311211412/http://www.arcsynthesis.org/gltut">
   Learning Modern 3D Graphics Programming
  </a>
  by
  <strong>
   Jason L. McKesson
  </strong>
 </li>
 <li>
  <a href="http://www.lighthouse3d.com/tutorials/glsl-core-tutorial">
   Light House 3D
  </a>
  by
  <strong>
   Light House 3D
  </strong>
 </li>
 <li>
  <a href="http://www.tomdalling.com/blog/category/modern-opengl">
   Modern OpenGL
  </a>
  by
  <strong>
   Tom Dalling
  </strong>
 </li>
 <li>
  <a href="https://github.com/McNopper/OpenGL">
   OpenGL Examples
  </a>
  by
  <strong>
   Norbert Nopper
  </strong>
  <sup>
   8 GitHub links in total 74 links, ★ 486, pushed 3 days ago
  </sup>
  <sup>
   &#9733 486, pushed 3 days ago
  </sup>
 </li>
 <li>
  <a href="http://ogldev.atspace.co.uk">
   OpenGL Step by Step
  </a>
  by
  <strong>
   Etay Meiri
  </strong>
 </li>
 <li>
  <a href="https://open.gl">
   OpenGL Tutorial
  </a>
  by
  <strong>
   Alexander Overvoorde
  </strong>
 </li>
 <li>
  <a href="http://antongerdelan.net/opengl/index.html">
   OpenGL Tutorial
  </a>
  by
  <strong>
   Anton Gerdelan
  </strong>
 </li>
 <li>
  <a href="http://www.opengl-tutorial.org">
   OpenGL Tutorial
  </a>
  by
  <strong>
   Bonder Wu
  </strong>
 </li>
 <li>
  <a href="http://www.songho.ca/opengl">
   OpenGL Tutorial
  </a>
  by
  <strong>
   Song Ho Ahn
  </strong>
 </li>
</ul>
<h2>
 Related lists
</h2>
<p>
 <em>
  Similar awesome lists
 </em>
 *
 <a href="https://github.com/sindresorhus/awesome">
  awesome
 </a>
 - A curated list of awesome lists.
*
 <a href="https://github.com/jbhuang0604/awesome-computer-vision">
  awesome-computer-vision
 </a>
 - A curated list of awesome computer vision resources.
*
 <a href="https://github.com/vinjn/awesome-vulkan">
  awesome-vulkan
 </a>
 - A curated list of awesome Vulkan projects and ecosystem.
*
 <a href="https://github.com/ellisonleao/magictools">
  gamedev
 </a>
 - A awesome list about game development.
*
 <a href="https://github.com/mattdesl/graphics-resources">
  graphics-resources
 </a>
 - A list of graphic programming resources.
</p>
<h2>
 License
</h2>
<p>
 <a href="http://creativecommons.org/licenses/by/4.0/">
  <img alt="Creative Commons License" src="http://i.creativecommons.org/l/by/4.0/88x31.png"/>
 </a>
</p>
<p>
 This work is licensed under a
 <a href="http://creativecommons.org/licenses/by/4.0/">
  Creative Commons Attribution 4.0 International License
 </a>
 .
</p>
<h2>
 Contributing
</h2>
<p>
 Please see
 <a href="https://github.com/eug/awesome-opengl/blob/master/CONTRIBUTING.md">
  CONTRIBUTING
 </a>
 for details.
</p>
