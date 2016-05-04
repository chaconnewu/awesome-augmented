<h1>
 Awesome Linux Containers
</h1>
<p>
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</p>
<h2>
 Table of Contents
</h2>
<ul>
 <li>
  <a href="#foundations">
   Foundations
  </a>
 </li>
 <li>
  <a href="#specifications">
   Specifications
  </a>
 </li>
 <li>
  <a href="#clouds">
   Clouds
  </a>
 </li>
 <li>
  <a href="#hypervisors">
   Hypervisors
  </a>
 </li>
 <li>
  <a href="#containers">
   Containers
  </a>
 </li>
 <li>
  <a href="#sandboxes">
   Sandboxes
  </a>
 </li>
 <li>
  <a href="#partial-access">
   Partial Access
  </a>
 </li>
 <li>
  <a href="#dashboard">
   Dashboard
  </a>
 </li>
 <li>
  <a href="#security">
   Security
  </a>
  <ul>
   <li>
    <a href="#tools">
     Tools
    </a>
   </li>
   <li>
    <a href="#links">
     Links
    </a>
   </li>
   <li>
    <a href="#levels-of-security-problems">
     Levels of security problems
    </a>
   </li>
   <li>
    <a href="#technologies-for-security">
     Technologies for security
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#another-information-sources">
   Another Information Sources
  </a>
 </li>
</ul>
<h2>
 Foundations
</h2>
<ul>
 <li>
  <a href="https://www.opencontainers.org/">
   OPEN CONTAINER INITIATIVE
  </a>
  <br/>
  The Open Container Initiative is a lightweight, open governance structure, to be formed under the auspices of the Linux Foundation, for the express purpose of creating open industry standards around container formats and runtime.
 </li>
 <li>
  <a href="https://cncf.io/">
   Cloud Native Computing Foundation
  </a>
  <br/>
  The Cloud Native Computing Foundation will create and drive the adoption of a new set of common container technologies informed by technical merit and end user value, and inspired by Internet-scale computing.
 </li>
 <li>
  <a href="https://www.cloudfoundry.org/foundation/">
   Cloud Foundry Foundation
  </a>
  <br/>
  The Cloud is our foundry.
 </li>
</ul>
<h2>
 Specifications
</h2>
<ul>
 <li>
  <a href="https://github.com/opencontainers/specs">
   Open Container Specifications
  </a>
  <br/>
  This project is where the Open Container Initiative Specifications are written. This is a work in progress.
 </li>
 <li>
  <a href="https://github.com/coreos/rkt/blob/master/Documentation/app-container.md">
   App Container basics
  </a>
  <br/>
  App Container (appc) is an open specification that defines several aspects of how to run applications in containers: an image format, runtime environment, and discovery protocol.
 </li>
 <li>
  <a href="https://wiki.freedesktop.org/www/Software/systemd/ContainerInterface/">
   Systemd Container Interface
  </a>
  <br/>
  Systemd is a suite of basic building blocks for a Linux system. It provides a system and service manager that runs as PID 1 and starts the rest of the system. If you write a container solution, please consider supporting the following interfaces.
 </li>
</ul>
<h2>
 Clouds
</h2>
<ul>
 <li>
  <a href="https://www.dotcloud.com/">
   Developer Cloud Platform
  </a>
  <br/>
  PaaS from Docker creators.
 </li>
 <li>
  <a href="https://cloud.google.com/container-engine/">
   Google Cloud Platform
  </a>
  <br/>
  Run Docker containers on Google Cloud Platform, powered by Kubernetes. Google Container Engine actively schedules your containers, based on declared needs, on a managed cluster of virtual machines.
 </li>
 <li>
  <a href="https://mesosphere.com/">
   Mesosphere
  </a>
  <br/>
  The Mesosphere Datacenter Operating System (DCOS) is a new kind of operating system that spans all of the machines in your datacenter or cloud. It provides a highly elastic, and highly scalable way of deploying applications, services and big data infrastructure on shared resources.
 </li>
 <li>
  <a href="http://kubernetes.io/">
   Kubernetes
  </a>
  <br/>
  Manage a cluster of Linux containers as a single system to accelerate Dev and simplify Ops.
 </li>
 <li>
  <a href="http://jelastic.com/">
   Jelastic
  </a>
  <br/>
  Unlimited PaaS and Container-Based IaaS in a Joint Cloud Solution for DevOps.
 </li>
 <li>
  <a href="https://github.com/cloudfoundry/warden">
   Warden
  </a>
  <span>
   &#9733 268, pushed 21 days ago
  </span>
  <br/>
  Manages isolated, ephemeral, and resource controlled environments. Part of Cloud Foundry - the open platform as a service project.
 </li>
 <li>
  <a href="https://aws.amazon.com/ecs/">
   Amazon EC2 Container Service
  </a>
  <br/>
  Container management service that supports Docker containers and allows you to easily run applications on a managed cluster of Amazon EC2 instances.
 </li>
 <li>
  <a href="https://www.joyent.com/">
   Joyent
  </a>
  <br/>
  High-Performance Container-Native Infrastructure for Today's Demanding Real-Time Web and Mobile Applications.
 </li>
</ul>
<h2>
 Hypervisors
</h2>
<ul>
 <li>
  <a href="https://github.com/veggiemonk/awesome-docker#cloud-infrastructure">
   Docker
  </a>
  <br/>
  An open platform for distributed applications for developers and sysadmins.
  <strong>
   Standard de facto
  </strong>
  .
 </li>
 <li>
  <a href="https://github.com/lxc/lxd">
   LXD
  </a>
  <span>
   &#9733 940, pushed 2 days ago
  </span>
  <br/>
  Daemon based on liblxc offering a REST API to manage LXC containers.
 </li>
 <li>
  <a href="https://openvz.org/Main_Page">
   OpenVZ
  </a>
  <br/>
  OpenVZ is container-based virtualization for Linux. OpenVZ creates multiple secure, isolated Linux containers (otherwise known as VEs or VPSs) on a single physical server enabling better server utilization and ensuring that applications do not conflict.
 </li>
</ul>
<h2>
 Containers
</h2>
<ul>
 <li>
  <a href="https://github.com/opencontainers/runc">
   runc
  </a>
  <span>
   &#9733 2738, pushed 2 days ago
  </span>
  <br/>
  runc is a CLI tool for spawning and running containers according to the OCS specification.
 </li>
 <li>
  <a href="https://github.com/p8952/bocker">
   Bocker
  </a>
  <span>
   &#9733 3260, pushed 251 days ago
  </span>
  <br/>
  Docker implemented in around 100 lines of bash.
 </li>
 <li>
  <a href="https://github.com/coreos/rkt">
   Rocket
  </a>
  <span>
   &#9733 5451, pushed 2 days ago
  </span>
  <br/>
  rkt (pronounced "rock-it") is a CLI for running app containers on Linux. rkt is designed to be composable, secure, and fast. Based on AppC specification.
 </li>
 <li>
  <a href="https://github.com/lxc/lxc">
   LXC
  </a>
  <span>
   &#9733 1433, pushed 2 days ago
  </span>
  <br/>
  LXC is the well known set of tools, templates, library and language bindings. It's pretty low level, very flexible and covers just about every containment feature supported by the upstream kernel.
 </li>
 <li>
  <a href="https://github.com/tailhook/vagga">
   Vagga
  </a>
  <span>
   &#9733 785, pushed 2 days ago
  </span>
  <br/>
  Vagga is a fully-userspace container engine inspired by Vagrant and Docker, specialized for development environments.
 </li>
 <li>
  <a href="https://github.com/xemul/libct">
   libct
  </a>
  <span>
   &#9733 85, pushed 173 days ago
  </span>
  <br/>
  Libct is a containers management library which provides convenient API for frontend programs to rule a container during its whole lifetime.
 </li>
 <li>
  <a href="https://libvirt.org/drvlxc.html">
   libvirt
  </a>
  <br/>
  A big toolkit to interact with the virtualization capabilities of recent versions of Linux (and other OSes).
 </li>
 <li>
  <a href="http://manpages.ubuntu.com/manpages/utopic/man1/systemd-nspawn.1.html">
   systemd-nspawn
  </a>
  <br/>
  Spawn a namespace container for debugging, testing and building. Part of
  <a href="https://wiki.freedesktop.org/www/Software/systemd/">
   systemd
  </a>
  .
 </li>
 <li>
  <a href="https://github.com/yandex/porto">
   porto
  </a>
  <span>
   &#9733 92, pushed 21 days ago
  </span>
  <br/>
  The main goal of Porto is to create a convenient, reliable interface over several Linux kernel mechanism such as cgroups, namespaces, mounts, networking etc.
 </li>
</ul>
<h2>
 Sandboxes
</h2>
<ul>
 <li>
  <a href="https://l3net.wordpress.com/projects/firejail/">
   Firejail
  </a>
  <br/>
  Firejail is a SUID sandbox program that reduces the risk of security breaches by restricting the running environment of untrusted applications using Linux namespaces, seccomp-bpf and Linux capabilities.
 </li>
 <li>
  <a href="https://github.com/google/nsjail">
   NsJail
  </a>
  <span>
   &#9733 276, pushed 8 days ago
  </span>
  <br/>
  NsJail is a process isolation tool for Linux. It makes use of the namespacing, resource control, and seccomp-bpf syscall filter subsystems of the Linux kernel.
 </li>
 <li>
  <a href="https://github.com/subuser-security/subuser">
   Subuser
  </a>
  <span>
   &#9733 508, pushed 6 days ago
  </span>
  <br/>
  Securing the Linux desktop with Docker.
 </li>
 <li>
  <a href="https://wiki.ubuntu.com/SecurityTeam/Specifications/SnappyConfinement">
   Snappy
  </a>
  <br/>
  Snappy Ubuntu Core is a new rendition of Ubuntu with transactional updates - a minimal server image with the same libraries as today’s Ubuntu, but applications are provided through a simpler mechanism.
 </li>
 <li>
  <a href="https://wiki.gnome.org/Projects/SandboxedApps">
   xdg-app
  </a>
  <br/>
  xdg-app is a system for building, distributing and running sandboxed desktop applications on Linux.
 </li>
</ul>
<h2>
 Partial Access
</h2>
<ul>
 <li>
  <a href="http://man7.org/linux/man-pages/man1/nsenter.1.html">
   nsenter
  </a>
  <br/>
  Run program with namespaces of other processes. Part of the util-linux.
 </li>
 <li>
  <a href="http://man7.org/linux/man-pages/man8/ip-netns.8.html">
   ip-netns
  </a>
  <br/>
  Process network namespace management. Part of the iproute2.
 </li>
 <li>
  <a href="http://man7.org/linux/man-pages/man1/unshare.1.html">
   unshare
  </a>
  <br/>
  Run program with some namespaces unshared from parent. Part of the util-linux.
 </li>
 <li>
  <a href="https://github.com/zalando/python-nsenter">
   python-nsenter
  </a>
  <span>
   &#9733 32, pushed 116 days ago
  </span>
  <br/>
  This Python package allows entering Linux kernel namespaces (mount, IPC, net, PID, user and UTS) by doing the "setns" syscall.
 </li>
 <li>
  <a href="https://pypi.python.org/pypi/butter">
   butter
  </a>
  <br/>
  Python library to interface to low level linux features (inotify, fanotify, timerfd, signalfd, eventfd, containers) with asyncio support.
 </li>
 <li>
  <a href="https://github.com/Friz-zy/pyspaces">
   pyspaces
  </a>
  <span>
   &#9733 51, pushed 261 days ago
  </span>
  <br/>
  Works with Linux namespaces through glibc with pure python.
 </li>
 <li>
  <a href="https://criu.org/Main_Page">
   CRIU
  </a>
  <br/>
  Checkpoint/Restore In Userspace is a software tool for Linux operating system. Using this tool, you can freeze a running application (or part of it) and checkpoint it to a hard drive as a collection of files. CRIU integrated with Docker and LXC to implement Live migration of containers.
 </li>
</ul>
<h2>
 Dashboard
</h2>
<ul>
 <li>
  <a href="https://lxc-webpanel.github.io/">
   LXC-Web-Panel
  </a>
  <br/>
  Web panel for LXC on Ubuntu.
 </li>
</ul>
<h2>
 Security
</h2>
<h3>
 Tools
</h3>
<ul>
 <li>
  <a href="https://github.com/docker/docker-bench-security">
   Docker bench security
  </a>
  <span>
   &#9733 1313, pushed 3 days ago
  </span>
  <br/>
  The Docker Bench for Security is a script that checks for dozens of common best-practices around deploying Docker containers in production.
 </li>
 <li>
  <a href="https://coreos.com/blog/vulnerability-analysis-for-containers/">
   CoreOS Clair
  </a>
  <br/>
  Open Source Vulnerability Analysis for your Containers.
 </li>
 <li>
  <a href="https://github.com/jfrazelle/bane">
   bane
  </a>
  <span>
   &#9733 279, pushed 2 days ago
  </span>
  <br/>
  Custom AppArmor profile generator for docker containers.
 </li>
 <li>
  <a href="https://github.com/OpenSCAP/container-compliance">
   OpenSCAP
  </a>
  <span>
   &#9733 113, pushed 250 days ago
  </span>
  <br/>
  The OpenSCAP ecosystem provides multiple tools to assist administrators and auditors with assessment, measurement and enforcement of security baselines.
 </li>
</ul>
<h3>
 Links
</h3>
<ul>
 <li>
  <a href="https://benchmarks.cisecurity.org/about/">
   CIS Security Benchmarks
  </a>
 </li>
 <li>
  <a href="https://opensource.com/business/14/7/docker-security-selinux">
   Are Docker containers really secure?
  </a>
 </li>
 <li>
  <a href="https://opensource.com/business/14/9/security-for-docker">
   Bringing new security features to Docker
  </a>
 </li>
 <li>
  <a href="http://www.slideshare.net/jpetazzo/docker-linux-containers-lxc-and-security">
   Docker, Linux Containers (LXC), and security
  </a>
 </li>
 <li>
  <a href="http://www.itworld.com/article/2920349/security/for-containers-security-is-problem-1.html">
   For containers, security is problem #1
  </a>
 </li>
 <li>
  <a href="https://mjg59.dreamwidth.org/33170.html">
   Linux Container Security
  </a>
 </li>
 <li>
  <a href="https://news.ycombinator.com/item?id=10030868">
   Ask HN: Best Linux sandbox?
  </a>
 </li>
 <li>
  <a href="https://benchmarks.cisecurity.org/tools2/docker/CIS_Docker_1.6_Benchmark_v1.0.0.pdf">
   CIS Docker 1.6 Benchmark v1.0.0
  </a>
 </li>
 <li>
  <a href="https://blog.docker.com/2015/05/understanding-docker-security-and-best-practices/">
   Understanding docker security and best practices
  </a>
 </li>
 <li>
  <a href="https://insights.ubuntu.com/2015/10/15/update-on-ubuntu-phone-security-issue/">
   Update on Ubuntu Phone security issue
  </a>
 </li>
 <li>
  <a href="https://www.lvh.io/posts/dont-expose-the-docker-socket-not-even-to-a-container.html">
   Don't expose the Docker socket (not even to a container)
  </a>
 </li>
 <li>
  <a href="http://rhelblog.redhat.com/?s=container&submit=Search">
   RedHut Blog
  </a>
  <ul>
   <li>
    <a href="https://access.redhat.com/articles/1353593">
     Introduction to Linux Containers
    </a>
   </li>
   <li>
    <a href="http://rhelblog.redhat.com/2015/07/07/whats-next-for-containers-user-namespaces/#more-1004">
     What’s Next for Containers? User Namespaces
    </a>
   </li>
   <li>
    <a href="http://rhelblog.redhat.com/2015/07/29/architecting-containers-part-1-user-space-vs-kernel-space/">
     Architecting Containers Part 1: Why Understanding User Space vs. Kernel Space Matters
    </a>
   </li>
   <li>
    <a href="http://rhelblog.redhat.com/2015/09/17/architecting-containers-part-2-why-the-user-space-matters-2/">
     Architecting Containers Part 2: Why the User Space Matters
    </a>
   </li>
  </ul>
 </li>
</ul>
<h3>
 Levels of security problems
</h3>
<p>
 1) regular application
</p>
<ul>
 <li>
  always untrusted -> know it
 </li>
 <li>
  suid bit -> mount with nosuid
 </li>
 <li>
  limit available syscall -> seccomp-bpf, grsec
 </li>
 <li>
  leak to another container (bug in namespaces, filesystem) -> user namespaces with different uid inside for each container: 1000 in container - 14293 and 15398 outside; security modules like selinux or apparmor
 </li>
</ul>
<p>
 2) system services like cron, ssh
</p>
<ul>
 <li>
  run as root -> isolate via bastion host or vm
 </li>
 <li>
  using /dev -> "devices" control group
  <br/>
  The following device nodes are created in the container by default.
  <br/>
  The Docker images are also mounted with nodev, which means that even if a device node was pre-created in the image, it could not be used by processes within the container to talk to the kernel.
  <br/>
  /dev/console,/dev/null,/dev/zero,/dev/full,/dev/tty*,/dev/urandom,/dev/random,/dev/fuse
 </li>
 <li>
  root calls -> capabilities (cap
  <em>
   sys
  </em>
  admin warning!)
  <br/>
  Here is the current list of capabilities that Docker uses: chown, dac
  <em>
   override, fowner, kill, setgid, setuid, setpcap, net
  </em>
  bind
  <em>
   service, net
  </em>
  raw, sys
  <em>
   chroot, mknod, setfcap, and audit
  </em>
  write.
  <br/>
  Docker removes several of these capabilities including the following:
  <br/>
  CAP
  <em>
   SETPCAP     Modify process capabilities
   <br/>
   CAP
  </em>
  SYS
  <em>
   MODULE  Insert/Remove kernel modules
   <br/>
   CAP
  </em>
  SYS
  <em>
   RAWIO   Modify Kernel Memory
   <br/>
   CAP
  </em>
  SYS
  <em>
   PACCT   Configure process accounting
   <br/>
   CAP
  </em>
  SYS
  <em>
   NICE    Modify Priority of processes
   <br/>
   CAP
  </em>
  SYS
  <em>
   RESOURCE    Override Resource Limits
   <br/>
   CAP
  </em>
  SYS
  <em>
   TIME    Modify the system clock
   <br/>
   CAP
  </em>
  SYS
  <em>
   TTY
  </em>
  CONFIG  Configure tty devices
  <br/>
  CAP
  <em>
   AUDIT
  </em>
  WRITE     Write the audit log
  <br/>
  CAP
  <em>
   AUDIT
  </em>
  CONTROL   Configure Audit Subsystem
  <br/>
  CAP
  <em>
   MAC
  </em>
  OVERRIDE    Ignore Kernel MAC Policy
  <br/>
  CAP
  <em>
   MAC
  </em>
  ADMIN   Configure MAC Configuration
  <br/>
  CAP
  <em>
   SYSLOG  Modify Kernel printk behavior
   <br/>
   CAP
  </em>
  NET
  <em>
   ADMIN   Configure the network
   <br/>
   CAP
  </em>
  SYS
  <em>
   ADMIN   Catch all
   <br/>
   uses /proc, /sys -> remount ro, drop cap
  </em>
  sys_admin; security modules like selinux or apparmor; some part of this fs are "namespace-aware"
  <br/>
  Docker mounts these file systems into the container as "read-only" mount points.
  <br/>
  . /sys
  <br/>
  . /proc/sys
  <br/>
  . /proc/sysrq-trigger
  <br/>
  . /proc/irq
  <br/>
  . /proc/bus
  <br/>
  Copy-on-write file systems
  <br/>
  Docker uses copy-on-write file systems. This means containers can use the same file system image as the base for the container. When a container writes content to the image, it gets written to a container specific file system. This prevents one container from seeing the changes of another container even if they wrote to the same file system image. Just as important, one container can not change the image content to effect the processes in another container.
 </li>
 <li>
  uid 0 -> user namespaces, uid 0 mappet to random uid outside
 </li>
</ul>
<p>
 3) system services like devices, network, filesystems
</p>
<ul>
 <li>
  root -> more of services should work on host outside; isolate sensitive functions, run as non-privileged context
 </li>
 <li>
  full privileges -> isolate on kernel level
 </li>
</ul>
<p>
 4) kernel drivers, network stack, security policies
</p>
<ul>
 <li>
  absolute privileges -> run it in separate vm
 </li>
</ul>
<p>
 5) general like immutable infrastructure
</p>
<ul>
 <li>
  container is ro
 </li>
 <li>
  write to small separate rw nosuid part
 </li>
</ul>
<p>
 <a href="http://www.slideshare.net/jpetazzo/docker-linux-containers-lxc-and-security">
  src
 </a>
 <br/>
 <a href="https://opensource.com/business/14/9/security-for-docker">
  src
 </a>
</p>
<h3>
 Technologies for security
</h3>
<p>
 Things are better. For example, most modern container technologies can make use of Linux's built-in security tools such as:
 <br/>
 <a href="http://wiki.apparmor.net/index.php/Main_Page">
  AppArmor
 </a>
 ,
 <a href="http://selinuxproject.org/page/Main_Page">
  SELinux
 </a>
 and
 <a href="http://man7.org/linux/man-pages/man2/seccomp.2.html">
  Seccomp
 </a>
 policies;
 <br/>
 <a href="https://grsecurity.net/">
  Grsecurity
 </a>
 ;
 <br/>
 <a href="https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Resource_Management_Guide/ch01.html">
  Control groups (cgroups)
 </a>
 ;
 <br/>
 <a href="http://man7.org/linux/man-pages/man7/namespaces.7.html">
  Kernel namespaces
 </a>
 <br/>
 <a href="http://www.itworld.com/article/2920349/security/for-containers-security-is-problem-1.html">
  src
 </a>
</p>
<p>
 Sure, you're deploying seccomp, but you can't use selinux inside your container, because the policy isn't per-namespace (?? lxc uses apparmore for each container...)
 <br/>
 <a href="http://selinuxproject.org/page/SVirt">
  sVirt
 </a>
 - selinux for kvm
 <br/>
 <a href="https://mjg59.dreamwidth.org/33170.html">
  src
 </a>
</p>
<p>
 Major kernel subsystems are not namespaced like:
 <br/>
 - SELinux
 <br/>
 - Cgroups
 <br/>
 - file systems under /sys
 <br/>
 - /proc/sys, /proc/sysrq-trigger, /proc/irq, /proc/bus
</p>
<p>
 Devices are not namespaced:
 <br/>
 - /dev/mem
 <br/>
 - /dev/sd* file system devices
 <br/>
 - kernel modules
</p>
<p>
 If you can communicate or attack one of these as a privileged process, you can own the system.
 <br/>
 <a href="https://opensource.com/business/14/7/docker-security-selinux">
  src
 </a>
</p>
<h2>
 Another Information Sources
</h2>
<ul>
 <li>
  <a href="https://github.com/draios/sysdig-container-ecosystem">
   sysdig-container-ecosystem
  </a>
  <span>
   &#9733 50, pushed 28 days ago
  </span>
  <br/>
  The ecosystem of awesome new technologies emerging around containers and microservices can be a little overwhelming, to say the least. We thought we might be able to help: welcome to the Container Ecosystem Project.
 </li>
 <li>
  <a href="http://doger.io/">
   doger.io
  </a>
  <br/>
  This page is an attempt to document the ins and outs of containers on Linux. This is not just restricted to programmers looking to implement containers or use container like features in their own code but also Sysadmins and Users who want to get more of a handle on how containers work 'under the hood'.
 </li>
</ul>
