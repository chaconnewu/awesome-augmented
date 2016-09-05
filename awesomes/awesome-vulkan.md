<h1>
 Awesome Vulkan
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<p>
 <img alt="Vulkan demo scene" height="256px" src="https://github.com/SaschaWillems/Vulkan/blob/master/images/vulkanlogoscene.png"/>
</p>
<p>
 A curated list of awesome Vulkan libraries, debuggers and resources. Inspired by
 <a href="https://github.com/eug/awesome-opengl">
  awesome-opengl
 </a>
 and other awesome-... stuff.
</p>
<ul>
 <li>
  <strong>
   <a href="#hardware-support">
    Hardware Support
   </a>
  </strong>
 </li>
 <li>
  <strong>
   <a href="#sdk">
    SDK
   </a>
  </strong>
 </li>
 <li>
  <strong>
   <a href="#document">
    IHV Document
   </a>
  </strong>
 </li>
 <li>
  <strong>
   <a href="#tutorial">
    Tutorial
   </a>
  </strong>
 </li>
 <li>
  <strong>
   <a href="#apps">
    Apps
   </a>
  </strong>
 </li>
 <li>
  <strong>
   <a href="#samples">
    Samples
   </a>
  </strong>
 </li>
 <li>
  <strong>
   <a href="#libraries">
    Libraries
   </a>
  </strong>
 </li>
 <li>
  <strong>
   <a href="#bindings">
    Bindings
   </a>
  </strong>
 </li>
 <li>
  <strong>
   <a href="#tools">
    Tools
   </a>
  </strong>
 </li>
</ul>
<h2>
 Hardware Support
</h2>
<ul>
 <li>
  <a href="http://vulkan.gpuinfo.org/">
   gpuinfo
  </a>
  - Vulkan Hardware Database by Sascha Willems
 </li>
 <li>
  <a href="https://www.khronos.org/vulkan">
   Khronos
  </a>
 </li>
 <li>
  <a href="https://developer.nvidia.com/Vulkan">
   NVIDIA
  </a>
  <ul>
   <li>
    <a href="https://developer.nvidia.com/vulkan-driver">
     Driver for Desktop
    </a>
   </li>
   <li>
    <a href="https://developer.nvidia.com/vulkan-android">
     Driver for Android
    </a>
   </li>
   <li>
    <a href="https://developer.nvidia.com/embedded/vulkan">
     Driver for Linux for Tegra (L4T)
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="http://support.amd.com/en-us/kb-articles/Pages/Radeon-Vulkan-Beta.aspx">
   AMD
  </a>
 </li>
 <li>
  <a href="https://imgtec.com/tools/powervr-early-access-program/">
   Imagination
  </a>
 </li>
 <li>
  Intel
  <ul>
   <li>
    <a href="https://01.org/linuxgraphics/blogs/jekstrand/2016/open-source-vulkan-drivers-intel-hardware/">
     Open-source Driver
    </a>
   </li>
   <li>
    <a href="https://software.intel.com/en-us/blogs/2016/03/14/new-intel-vulkan-beta-1540204404-graphics-driver-for-windows-78110-1540">
     Driver for Windows
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="https://developer.qualcomm.com/software/adreno-gpu-sdk/gpu">
   Qualcomm
  </a>
 </li>
 <li>
  <a href="http://malideveloper.arm.com/resources/sdks/mali-vulkan-sdk/">
   ARM
  </a>
 </li>
</ul>
<h2>
 SDK
</h2>
<ul>
 <li>
  <a href="https://vulkan.lunarg.com/signin">
   For Windows & Linux
  </a>
 </li>
 <li>
  <a href="https://developer.android.com/ndk/guides/graphics/index.html">
   For Android
  </a>
 </li>
</ul>
<h2>
 Document
</h2>
<ul>
 <li>
  <a href="http://gpuopen.com/gaming-product/vulkan/">
   AMD
  </a>
  <ul>
   <li>
    <a href="http://32ipi028l5q82yhj72224m8j.wpengine.netdna-cdn.com/wp-content/uploads/2016/03/VulkanFastPaths.pdf">
     Vulkan Fast Paths
    </a>
   </li>
   <li>
    <a href="http://32ipi028l5q82yhj72224m8j.wpengine.netdna-cdn.com/wp-content/uploads/2016/03/Let_your_game_shine_optimizing_DirectX-12_and_Vulkan-performance_with_AMD_CodeXL.pdf">
     Let Your Game Shine – Optimizing DirectX 12 and Vulkan Performance with AMD CodeXL
    </a>
   </li>
   <li>
    <a href="http://32ipi028l5q82yhj72224m8j.wpengine.netdna-cdn.com/wp-content/uploads/2016/03/d3d12_vulkan_lessons_learned.pdf">
     D3D12 & Vulkan: Lessons Learned
    </a>
   </li>
   <li>
    <a href="http://gpuopen.com/say-hello/">
     Say Hello to a New Rendering API in Town!
    </a>
   </li>
   <li>
    <a href="http://gpuopen.com/vulkan-renderpasses/">
     Vulkan Renderpasses
    </a>
   </li>
   <li>
    <a href="http://gpuopen.com/performance-tweets-series-barriers-fences-synchronization/">
     Performance tweets series: Barriers, fences, synchronization
    </a>
   </li>
   <li>
    <a href="http://gpuopen.com/using-the-vulkan-validation-layers/">
     Using the Vulkan™ Validation Layers
    </a>
   </li>
   <li>
    <a href="http://32ipi028l5q82yhj72224m8j.wpengine.netdna-cdn.com/wp-content/uploads/2016/05/Most-common-mistakes-in-Vulkan-apps.pdf">
     Most common mistakes in Vulkan apps
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="https://developer.nvidia.com/taxonomy/term/586">
   NVIDIA
  </a>
  <ul>
   <li>
    <a href="http://on-demand.gputechconf.com/gtc/2016/presentation/s6138-christoph-kubisch-pierre-boudier-gpu-driven-rendering.pdf">
     GPU-Driven Rendering
    </a>
   </li>
   <li>
    <a href="http://developer.download.nvidia.com/gameworks/events/GDC2016/mschott_lbishop_gl_vulkan.pdf">
     GDC 16 - High-performance, Low-Overhead Rendering with OpenGL and Vulkan
    </a>
   </li>
   <li>
    <a href="http://developer.download.nvidia.com/gameworks/events/GDC2016/Vulkan_Essentials_GDC16_tlorach.pdf">
     GDC 16 - Vulkan and NVIDIA – The Essentials
    </a>
   </li>
   <li>
    <a href="https://developer.nvidia.com/engaging-voyage-vulkan">
     Engaging the Voyage to Vulkan
    </a>
   </li>
   <li>
    <a href="https://developer.nvidia.com/vulkan-shader-resource-binding">
     Vulkan Shader Resource Binding
    </a>
   </li>
   <li>
    <a href="https://developer.nvidia.com/vulkan-memory-management">
     Vulkan Memory Management
    </a>
   </li>
   <li>
    <a href="https://developer.nvidia.com/opengl-vulkan">
     OpenGL like Vulkan
    </a>
   </li>
   <li>
    <a href="https://developer.nvidia.com/transitioning-opengl-vulkan">
     Transitioning from OpenGL to Vulkan
    </a>
   </li>
   <li>
    <a href="http://on-demand.gputechconf.com/siggraph/2015/presentation/SIG1501-Piers-Daniell.pdf">
     Siggraph 15 talk - Vulkan on NVIDIA GPUs
    </a>
   </li>
  </ul>
 </li>
 <li>
  ARM
  <ul>
   <li>
    <a href="https://community.arm.com/groups/arm-mali-graphics/blog/2016/02/16/porting-a-graphics-engine-to-the-vulkan-api">
     Porting a Graphics Engine to the Vulkan API
    </a>
   </li>
   <li>
    <a href="https://community.arm.com/groups/arm-mali-graphics/blog/2016/04/19/massively-multi-thread-for-vulkan">
     Multi-Threading in Vulkan
    </a>
   </li>
   <li>
    <a href="http://malideveloper.arm.com/downloads/Presentations/GDC%202016/Theatre/Vulkan%20API%20key%20features%20on%20ARM%20architecture.pdf">
     Vulkan's Key Features on ARM Architecture
    </a>
   </li>
   <li>
    <a href="http://malideveloper.arm.com/downloads/Presentations/GDC%202016/Theatre/Get%20Your%20Engine%20Ready%20for%20Vulkan%20on%20Mobile.pdf">
     Get Your Engine Ready for Vulkan on Mobile
    </a>
   </li>
   <li>
    <a href="http://malideveloper.arm.com/downloads/deved/tutorial/SDK/Vulkan/1.0/tutorials.html">
     Mali Vulkan Tutorials
    </a>
    - Basic Vulkan tutorials from the
    <a href="http://malideveloper.arm.com/resources/sdks/mali-vulkan-sdk/">
     Mali Vulkan SDK
    </a>
   </li>
  </ul>
 </li>
 <li>
  Intel
  <ul>
   <li>
    <a href="https://github.com/GameTechDev/IntroductionToVulkan">
     API without Secrets: Introduction to Vulkan
    </a>
    [
    <a href="https://github.com/GameTechDev/IntroductionToVulkan/blob/master/license.txt">
     LICENSE
    </a>
    ]
   </li>
   <li>
    <a href="https://software.intel.com/en-us/api-without-secrets-introduction-to-vulkan-part-1">
     Part 1: The Beginning
    </a>
   </li>
   <li>
    <a href="https://software.intel.com/en-us/api-without-secrets-introduction-to-vulkan-part-2">
     Part 2: Swap Chain
    </a>
   </li>
   <li>
    <a href="https://software.intel.com/en-us/api-without-secrets-introduction-to-vulkan-part-3">
     Part 3: First Triangle
    </a>
   </li>
  </ul>
  <sup>
   &#9733 107, pushed 127 days ago
  </sup>
 </li>
 <li>
  <a href="http://blog.imgtec.com/tag/vulkan">
   Imagination
  </a>
  <ul>
   <li>
    <a href="https://imagination-technologies-cloudfront-assets.s3.amazonaws.com/idc-docs/gdc16/6_Efficient%20rendering%20with%20Vulkan%20on%20PowerVR.pdf">
     Efficient Rendering with Vulkan on PowerVR
    </a>
   </li>
   <li>
    <a href="https://imagination-technologies-cloudfront-assets.s3.amazonaws.com/idc-docs/gdc16/7_FrameworkIDC16.pdf">
     Migrating to Vulkan with the New PowerVR Graphics Framework
    </a>
   </li>
  </ul>
 </li>
 <li>
  Samgsung
  <ul>
   <li>
    <a href="https://community.arm.com/servlet/JiveServlet/download/96891546-24708/6-mmg-siggraph2016-vulkan-smedis.pdf">
     Siggraph 2016 - Best Practices for Mobile
    </a>
   </li>
  </ul>
 </li>
 <li>
  Epic
  <ul>
   <li>
    <a href="https://community.arm.com/servlet/JiveServlet/download/96891546-24708/6-mmg-siggraph2016-vulkan-smedis.pdf">
     Efficient use of Vulkan on UE4 Mobile
    </a>
   </li>
  </ul>
 </li>
</ul>
<h2>
 Tutorial
</h2>
<ul>
 <li>
  <a href="http://av.dfki.de/~jhenriques/development.html">
   jhenriques's tutorial
  </a>
 </li>
 <li>
  <a href="https://www.khronos.org/registry/vulkan/">
   Khronos
  </a>
  <ul>
   <li>
    <a href="https://www.khronos.org/registry/vulkan/specs/1.0/refguide/Vulkan-1.0-web.pdf">
     Vulkan 1.0 Quick Reference
    </a>
   </li>
   <li>
    <a href="https://www.khronos.org/registry/vulkan/specs/1.0-wsi_extensions/pdf/vkspec.pdf">
     Vulkan 1.0 Specification
    </a>
   </li>
   <li>
    <a href="https://www.khronos.org/developers/library/2016-gdc">
     GDC 2016 Presentations
    </a>
   </li>
   <li>
    <a href="https://www.khronos.org/assets/uploads/developers/library/2016-uk-chapter-moving-to-vulkan/Moving-to-Vulkan_Khronos-UK_May16.pdf">
     Moving to Vulkan Khronos UK May16
    </a>
   </li>
   <li>
    <a href="https://www.khronos.org/assets/uploads/developers/library/2016-siggraph/Khronos-3D-BOF-SIGGRAPH_Jul16.pdf">
     SIGGRPAH 2016 3D BOF
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="http://www.amazon.com/Vulkan-Programming-Guide-Official-Learning/dp/0134464540">
   Vulkan Programming Guide
  </a>
  - AKA the Red Book.
 </li>
 <li>
  Siggraph
  <ul>
   <li>
    <a href="http://nextgenapis.realtimerendering.com/">
     An overview of next-generation graphics APIs
    </a>
    - covers Vulkan, D3D12 etc.
   </li>
  </ul>
 </li>
 <li>
  <a href="https://github.com/philiptaylor/vulkan-sxs">
   vulkan-sxs
  </a>
  - explain the Vulkan API step by step and
  <a href="https://github.com/philiptaylor/vulkan-sync">
   vulkan-sync
  </a>
  - rephrase Vulkan's requirements on execution dependencies in a more precise form. [MIT]
  <sup>
   &#9733 12, pushed 185 days ago
  </sup>
 </li>
 <li>
  <a href="https://renderdoc.org/vulkan-in-30-minutes.html">
   Vulkan in 30 minutes
  </a>
  - by baldurk.
 </li>
 <li>
  <a href="https://vulkan-tutorial.com/">
   Tutorial by Overv
  </a>
  and
  <a href="https://github.com/Overv/VulkanTutorial">
   its github repository
  </a>
  . [CC BY-SA 4.0]
 </li>
</ul>
<h2>
 Apps
</h2>
<ul>
 <li>
  <a href="http://www.croteam.com/talos-principle-will-support-vulkan-first-screenshot-released/">
   The Talos Principle
  </a>
  - by Croteam.
 </li>
 <li>
  <a href="https://github.com/ValveSoftware/Dota-2-Vulkan/">
   Dota2
  </a>
  - by Valve.
 </li>
 <li>
  <a href="http://www.basemark.com/2015/11/10/basemark-extends-its-benchmarking-lead-with-a-vulkan-performance-test/">
   Basemark
  </a>
  - by Basemark.
 </li>
 <li>
  <a href="https://kishonti.net/news_single.jsp?id=31133884">
   GFXBench 5
  </a>
  - by Kishonti.
 </li>
 <li>
  <a href="https://www.unrealengine.com/blog/epic-games-unveils-protostar-at-samsung-galaxy-unpacked">
   ProtoStar
  </a>
  - by Epic, built with Unreal Engine 4 technology.
 </li>
 <li>
  <a href="https://en.wikipedia.org/wiki/Doom_(2016_video_game)">
   Doom
  </a>
  - by id Software.
 </li>
</ul>
<h2>
 Samples
</h2>
<ul>
 <li>
  Sascha Willems's
  <a href="https://github.com/SaschaWillems/Vulkan">
   samples
  </a>
  and
  <a href="https://github.com/SaschaWillems/VulkanSponza">
   Deferred rendering of  Sponza
  </a>
  and his talk of
  <a href="https://github.com/SaschaWillems/Vulkan/blob/master/documentation/Khronos_meetup_munich_fromGLtoVulkan.pdf">
   Khronos
   <em>
    meetup
   </em>
   munich
  </a>
  .
  <sup>
   &#9733 1157, pushed 128 days ago
  </sup>
 </li>
 <li>
  McNopper's
  <a href="https://github.com/McNopper/Vulkan">
   examples
  </a>
  <sup>
   &#9733 38, pushed 128 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/KhronosGroup">
   KhronosGroup
  </a>
  <ul>
   <li>
    <a href="https://github.com/KhronosGroup/Vulkan-Samples">
     Samples
    </a>
    <sup>
     &#9733 265, pushed 136 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/KhronosGroup/Vulkan-CTS">
     Conformance Tests (CTS)
    </a>
    <sup>
     &#9733 66, pushed 137 days ago
    </sup>
   </li>
  </ul>
 </li>
 <li>
  Google
  <ul>
   <li>
    <a href="https://github.com/googlesamples/vulkan-basic-samples">
     Android port of LunarG samples
    </a>
    .
   </li>
   <li>
    <a href="https://github.com/googlesamples/android-vulkan-tutorials">
     android tutorials
    </a>
    .
    <sup>
     &#9733 82, pushed 132 days ago
    </sup>
   </li>
  </ul>
  <sup>
   &#9733 48, pushed 125 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/nvpro-samples">
   nvpro-samples
  </a>
  - NVIDIA DesignWorks Samples. [
  <a href="https://github.com/nvpro-samples/gl_vk_threaded_cadscene/blob/master/LICENSE">
   LICENSE
  </a>
  ]
  <ul>
   <li>
    <a href="https://github.com/nvpro-samples/gl_vk_chopper">
     gl
     <em>
      vk
     </em>
     chopper
    </a>
    - Simple vulkan rendering example.
    <sup>
     &#9733 85, pushed 140 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/nvpro-samples/gl_vk_threaded_cadscene">
     gl
     <em>
      vk
     </em>
     threaded_cadscene
    </a>
    - OpenGL and Vulkan comparison on rendering a CAD scene using veraious techniques and
    <a href="https://developer.nvidia.com/vulkan-opengl-threaded-cad-scene-sample">
     the blog
    </a>
    about it.
    <sup>
     &#9733 42, pushed 135 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/nvpro-samples/gl_vk_bk3dthreaded">
     gl
     <em>
      vk
     </em>
     bk3dthreaded
    </a>
    - Vulkan sample rendering 3D with 'worker-threads'.
    <sup>
     &#9733 22, pushed 179 days ago
    </sup>
   </li>
   <li>
    <a href="https://github.com/nvpro-samples/gl_vk_supersampled">
     gl
     <em>
      vk
     </em>
     supersampled
    </a>
    - Vulkan sample showing a high quality super-sampled rendering.
    <sup>
     &#9733 20, pushed 185 days ago
    </sup>
   </li>
  </ul>
 </li>
 <li>
  <a href="https://github.com/NVIDIAGameWorks/GraphicsSamples">
   NVIDIA GameWorks Samples
  </a>
  - GameWorks cross-platform graphics API samples. [[LICENSE](https://github.com/NVIDIAGameWorks/GraphicsSamples/blob/master/license.txt)]
 </li>
 <li>
  <a href="https://github.com/LunarG/VulkanSamples">
   LunarG's samples
  </a>
  <sup>
   &#9733 211, pushed 129 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/krh/vkcube">
   vkcube
  </a>
  - 'vkcube' sample from krh, works under X, wayland and VT console with
drm/kms.
  <sup>
   &#9733 27, pushed 131 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/GameTechDev/stardust_vulkan">
   Stardust from Intel
  </a>
  - The Stardust sample application uses the Vulkan graphics API to efficiently render a cloud of animated particles. [[LICENSE](https://github.com/GameTechDev/stardust_vulkan/blob/master/license.txt)]
  <sup>
   &#9733 28, pushed 131 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/GPUOpen-LibrariesAndSDKs/HelloVulkan">
   Introductory Vulkan sample from AMD
  </a>
  . [MIT]
 </li>
 <li>
  <a href="https://github.com/Novum/vkQuake">
   Vulkan Quake port based on QuakeSpasm
  </a>
  .
 </li>
</ul>
<h2>
 Libraries
</h2>
<ul>
 <li>
  <a href="https://github.com/cinder/Cinder">
   Cinder
  </a>
  and
  <a href="https://libcinder.org/notes/vulkan">
   the story
  </a>
  <a href="https://forum.libcinder.org/#Topic/23286000002614007">
   behind
  </a>
  . [BSD]
  <sup>
   &#9733 2512, pushed 128 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/openframeworks-vk/openFrameworks">
   openFrameworks
  </a>
  - the most famouse C++ creative coding framework. [MIT]
 </li>
 <li>
  <a href="https://github.com/bkaradzic/bgfx">
   bgfx
  </a>
  - Cross-platform rendering library, bgfx backend is WIP. [[LICENSE](https://github.com/bkaradzic/bgfx/blob/master/LICENSE)]
  <sup>
   &#9733 1856, pushed 126 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/powervr-graphics/Native_SDK">
   PowerVR SDK
  </a>
  - C++ cross-platform 3D graphics SDK to speed up development of Vulkan and GLES. [[LICENSE](https://github.com/powervr-graphics/Native
  <em>
   SDK/blob/4.1/LICENSE
  </em>
  POWERVR_SDK.txt)]
  <sup>
   &#9733 144, pushed 151 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/glfw/glfw">
   glfw
  </a>
  and
  <a href="http://www.glfw.org/docs/3.2/vulkan.html">
   the guide
  </a>
  .  [[LICENSE](https://github.com/glfw/glfw/blob/master/COPYING.txt)]
  <sup>
   &#9733 1895, pushed 126 days ago
  </sup>
 </li>
 <li>
  <a href="https://moltengl.com/metalvk/">
   MetalVK
  </a>
  - run Vulkan on iOS and OS X. [Non-free]
 </li>
 <li>
  <a href="https://github.com/ocornut/imgui">
   imgui
  </a>
  - Immediate Mode Graphical User interface. [MIT]
  <sup>
   &#9733 3531, pushed 126 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/alexhultman/libvc">
   libvc
  </a>
  - Vulkan Compute for C++.  [[LICENSE](https://github.com/alexhultman/libvc/blob/master/LICENSE)]
  <sup>
   &#9733 28, pushed 173 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/GPUOpen-LibrariesAndSDKs/Anvil">
   AMD's Anvil
  </a>
  - cross-platform framework for Vulkan. [[LICENSE](https://github.com/GPUOpen-LibrariesAndSDKs/OutOfOrderRasterization/blob/master/LICENSE.txt)]
 </li>
 <li>
  <a href="https://github.com/google/vulkan-cpp-library">
   Google's vulkan-cpp-library
  </a>
  - Vulkan abstraction library using C++11 for memory, resource management, type and thread safety as well as system independency. [Apache]
 </li>
 <li>
  <a href="https://github.com/andy-thomason/Vookoo">
   Vookoo
  </a>
  - Vulkan Utititles Library. [MIT]
 </li>
 <li>
  <a href="https://github.com/nyorain/vpp">
   vpp
  </a>
  - Modern C++ Vulkan Abstraction focused on performance and a straightforward interface. [MIT]
 </li>
</ul>
<h2>
 Bindings
</h2>
<ul>
 <li>
  <a href="https://github.com/CapsAdmin/ffibuild/blob/master/examples/vulkan/libvulkan.lua">
   libvulkan.lua
  </a>
  - Lua bindings for Vulkan.
 </li>
 <li>
  <a href="https://github.com/ColonelThirtyTwo/dvulkan">
   dvulkan
  </a>
  - Auto-generated D bindings for Vulkan.
  <sup>
   &#9733 8, pushed 142 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/ParticlePeter/ErupteD">
   ErupteD
  </a>
  - Another Auto-generated D bindings for Vulkan.
 </li>
 <li>
  <a href="https://github.com/expipiplus1/vulkan">
   Haskell bindings for Vulkan
  </a>
  - [[LICENSE](https://github.com/expipiplus1/vulkan/blob/master/LICENSE)]
  <sup>
   &#9733 22, pushed 128 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/KhronosGroup/Vulkan-Hpp">
   Vulkan-hpp
  </a>
  Open-Source Vulkan C++ API originated from NVIDIA and
  <a href="https://developer.nvidia.com/open-source-vulkan-c-api">
   the blog
  </a>
  about it.
 </li>
 <li>
  <a href="https://github.com/mono/VulkanSharp">
   VulkanSharp
  </a>
  - C# bindings for Vulkan. [MIT]
  <sup>
   &#9733 74, pushed 130 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/tomaka/vulkano">
   Vulkano
  </a>
  - Safe and rich Rust wrapper around the Vulkan API. [MIT]
  <sup>
   &#9733 291, pushed 127 days ago
  </sup>
 </li>
 <li>
  <a href="https://www.lwjgl.org/">
   LWJGL
  </a>
  - Lightweight Java Game Library 3 has Vulkan bindings. [BSD]
 </li>
</ul>
<h2>
 Tools
</h2>
<ul>
 <li>
  <a href="https://developer.nvidia.com/nvidia-nsight-visual-studio-edition">
   Nsight™ Visual Studio Edition 5.2+
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/KhronosGroup/Vulkan-LoaderAndValidationLayers">
   LoaderAndValidationLayers
  </a>
  - from KhronosGroup. [MIT]
  <sup>
   &#9733 174, pushed 128 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/baldurk/renderdoc">
   renderdoc
  </a>
  - by baldurk, a stand-alone graphics debugging tool. [MIT]
  <sup>
   &#9733 972, pushed 126 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/LunarG/VulkanTools">
   VulkanTools
  </a>
  - LunarG's tools including layers,
  <code>
   vktrace
  </code>
  and
  <code>
   vkreplay
  </code>
  . [MIT]
  <sup>
   &#9733 77, pushed 129 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/GPUOpen-Tools/CodeXL">
   CodeXL
  </a>
  - CodeXL goes open source. [MIT]
  <sup>
   &#9733 247, pushed 127 days ago
  </sup>
 </li>
 <li>
  <a href="https://developer.qualcomm.com/software/adreno-gpu-sdk/tools">
   Qualcomm GPU Tools
  </a>
  .
 </li>
 <li>
  <a href="http://malideveloper.arm.com/resources/tools/mali-graphics-debugger/">
   Mali Graphics Debugger
  </a>
  .
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
 <a href="https://github.com/eug/awesome-opengl">
  awesome-opengl
 </a>
 - A curated list of awesome OpenGL libraries, debuggers and resources.
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
 <a href="https://github.com/vinjn/awesome-vulkan/blob/master/CONTRIBUTING.md">
  CONTRIBUTING
 </a>
 for details.
</p>
