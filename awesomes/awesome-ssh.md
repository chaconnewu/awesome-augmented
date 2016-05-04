<h1>
 Awesome SSH
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<blockquote>
 <p>
  A curated list of SSH
  <a href="#apps">
   apps
  </a>
  ,
  <a href="#libraries">
   libraries
  </a>
  and
  <a href="#resources">
   resources
  </a>
  .
 </p>
</blockquote>
<h2 align="center">
 <img src="https://raw.githubusercontent.com/moul/awesome-ssh/master/logo.jpg" width="400"/>
</h2>
<p>
 Inspired by the
 <a href="https://github.com/sindresorhus/awesome">
  awesome
 </a>
 list thing.
</p>
<p>
 Please read the
 <a href="CONTRIBUTING.md">
  contribution guidelines
 </a>
 if you want to contribute.
</p>
<p>
 <strong>
  Check out my
  <a href="http://manfredtouron.tumblr.com">
   blog
  </a>
  🦄 or say
  <em>
   hi
  </em>
  on
  <a href="https://twitter.com/moul">
   Twitter
  </a>
  .
 </strong>
</p>
<h2>
 Table of Contents
</h2>
<ul>
 <li>
  <a href="#apps">
   Apps
  </a>
  <ul>
   <li>
    <a href="#sshconfig">
     <code>
      .ssh/config
     </code>
    </a>
   </li>
   <li>
    <a href="#tools-using-the-ssh-protocol">
     Tools using the SSH protocol
    </a>
   </li>
   <li>
    <a href="#servers">
     Servers
    </a>
   </li>
   <li>
    <a href="#network">
     Network
    </a>
   </li>
   <li>
    <a href="#multiplexers">
     Multiplexers
    </a>
   </li>
   <li>
    <a href="#ssh-keys--authentication">
     SSH Keys / Authentication
    </a>
   </li>
   <li>
    <a href="#ssh-agent">
     SSH agent
    </a>
   </li>
   <li>
    <a href="#tools">
     Tools
    </a>
   </li>
   <li>
    <a href="#automation">
     Automation
    </a>
   </li>
   <li>
    <a href="#web">
     Web
    </a>
   </li>
   <li>
    <a href="#testing--honeypots">
     Testing / Honeypots
    </a>
   </li>
   <li>
    <a href="#alternatives-to-ssh">
     Alternatives to SSH
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#libraries">
   Libraries
  </a>
 </li>
 <li>
  <a href="#resources">
   Resources
  </a>
  <ul>
   <li>
    <a href="#tutorials">
     Tutorials
    </a>
   </li>
   <li>
    <a href="#security">
     Security
    </a>
   </li>
   <li>
    <a href="#documentation">
     Documentation
    </a>
   </li>
   <li>
    <a href="#community">
     Community
    </a>
   </li>
  </ul>
 </li>
</ul>
<h2>
 Apps
</h2>
<h3>
 <code>
  .ssh/config
 </code>
</h3>
<ul>
 <li>
  <a href="https://github.com/moul/advanced-ssh-config">
   advanced-ssh-config
  </a>
  <sup>
   &#9733 434, pushed 4 days ago
  </sup>
  : a transparent wrapper (ProxyCommand) that adds regex, aliases, gateways, includes, dynamic hostnames to SSH and ssh-config.
 </li>
 <li>
  <a href="https://github.com/emre/storm">
   storm
  </a>
  <sup>
   &#9733 2342, pushed 38 days ago
  </sup>
  : Manage your SSH like a boss.
 </li>
 <li>
  <a href="https://github.com/gaqzi/ansible-ssh-config">
   ansible-ssh-config
  </a>
  <sup>
   &#9733 45, pushed 21 days ago
  </sup>
  : Letting Ansible manage ssh config.
 </li>
 <li>
  <a href="https://github.com/mirakui/ec2ssh">
   ec2ssh
  </a>
  <sup>
   &#9733 158, pushed 4 days ago
  </sup>
  : A ssh_config manager for AWS EC2.
 </li>
 <li>
  <a href="https://github.com/dbrady/ssh-config">
   ssh-config
  </a>
  <sup>
   &#9733 67, pushed 264 days ago
  </sup>
  : A tool to help manage your .ssh/config file.
 </li>
</ul>
<h3>
 Tools using the SSH protocol
</h3>
<ul>
 <li>
  <a href="http://linux.die.net/man/1/scp">
   scp
  </a>
  : secure remote file copy utility over SSH.
 </li>
 <li>
  <a href="https://rsync.samba.org">
   rsync
  </a>
  : fast incremental transfer utility that supports SSH.
 </li>
 <li>
  <a href="https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol">
   sftp
  </a>
  : file transfer protocol over SSH.
 </li>
 <li>
  <a href="http://curl.haxx.se">
   curl
  </a>
  : command line tool and library to transfer data (support sftp).
 </li>
</ul>
<h3>
 Servers
</h3>
<ul>
 <li>
  <a href="https://github.com/moul/ssh2docker">
   ssh2docker
  </a>
  <sup>
   &#9733 32, pushed 11 days ago
  </sup>
  : SSH server to Docker containers.
 </li>
 <li>
  <a href="https://github.com/FiloSottile/whosthere">
   whosthere
  </a>
  <sup>
   &#9733 1098, pushed 75 days ago
  </sup>
  : A ssh server that knows who you are.
  <code>
   $ ssh whoami.filippo.io
  </code>
  .
 </li>
 <li>
  <a href="https://github.com/gliderlabs/sshfront">
   sshfront
  </a>
  <sup>
   &#9733 136, pushed 293 days ago
  </sup>
  : Programmable SSH frontend
 </li>
 <li>
  <a href="https://github.com/shazow/ssh-chat">
   ssh-chat
  </a>
  <sup>
   &#9733 1920, pushed 80 days ago
  </sup>
  - Chat over SSH.
 </li>
 <li>
  <a href="https://github.com/dokku/sshcommand">
   sshcommand
  </a>
  <sup>
   &#9733 243, pushed 30 days ago
  </sup>
  - Turn SSH into a thin client specifically for your app
 </li>
 <li>
  <a href="https://github.com/joushou/sshmuxd">
   sshmuxd
  </a>
  <sup>
   &#9733 638, pushed 19 days ago
  </sup>
  - sshmux frontend
 </li>
 <li>
  <a href="https://github.com/jquast/x84">
   x84
  </a>
  <sup>
   &#9733 202, pushed 106 days ago
  </sup>
  - A python telnet/ssh server for modern UTF-8 and classic cp437 network virtual terminals. In spirit of classic software such as ami/x, teleguard, renegade, iniquity. http://x84.readthedocs.org/
 </li>
</ul>
<h3>
 Network
</h3>
<ul>
 <li>
  <a href="https://mosh.mit.edu">
   Mosh
  </a>
  - The mobile shell.
 </li>
 <li>
  <a href="https://github.com/libfuse/sshfs">
   sshfs
  </a>
  <sup>
   &#9733 160, pushed 4 days ago
  </sup>
  : Filesystem client based on the SSH File Transfer Protocol.
 </li>
 <li>
  <a href="https://github.com/inconshreveable/ngrok">
   ngrok
  </a>
  <sup>
   &#9733 6976, pushed 24 days ago
  </sup>
  : Introspected tunnels to localhost.
 </li>
 <li>
  <a href="https://github.com/progrium/localtunnel">
   localtunnel
  </a>
  <sup>
   &#9733 2873, pushed 485 days ago
  </sup>
  : Expose localhost servers to the Internet.
 </li>
 <li>
  <a href="https://github.com/apenwarr/sshuttle">
   sshuttle
  </a>
  <sup>
   &#9733 6763, pushed 11 days ago
  </sup>
  - Transparent proxy server that works as a poor man's VPN. Forwards over ssh. Doesn't require admin. Works with Linux and MacOS. Supports DNS tunneling.
 </li>
 <li>
  <a href="https://github.com/stealth/sshttp">
   sshttp
  </a>
  <sup>
   &#9733 353, pushed 56 days ago
  </sup>
  - SSH/HTTP(S) multiplexer. Run a webserver and a sshd on the same port w/o changes.
 </li>
 <li>
  <a href="https://github.com/jamescun/switcher">
   switcher
  </a>
  <sup>
   &#9733 715, pushed 467 days ago
  </sup>
  - Run SSH and HTTP(S) on the same port
 </li>
 <li>
  <a href="https://github.com/yrutschle/sslh">
   sslh
  </a>
  <sup>
   &#9733 813, pushed 5 days ago
  </sup>
  - Applicative Protocol Multiplexer (i.e: SSH + HTTPS)
 </li>
 <li>
  <a href="https://github.com/aphyr/tund">
   tund
  </a>
  <sup>
   &#9733 304, pushed 84 days ago
  </sup>
  - SSH reverse tunnel daemon
 </li>
 <li>
  <a href="http://www.harding.motd.ca/autossh/">
   autossh
  </a>
  - Automatically respawn ssh session after network interruption.
 </li>
 <li>
  <a href="https://github.com/aluzzardi/wssh">
   wssh
  </a>
  <sup>
   &#9733 804, pushed 8 days ago
  </sup>
  - SSH to WebSockets Bridge
 </li>
 <li>
  <a href="https://github.com/vieux/docker-volume-sshfs">
   docker-volume-sshfs
  </a>
  <sup>
   &#9733 50, pushed 42 days ago
  </sup>
  - sshfs docker volume plugin.
 </li>
</ul>
<h3>
 Multiplexers
</h3>
<ul>
 <li>
  <a href="https://tmux.github.io">
   tmux
  </a>
  : Terminal multiplexer.
 </li>
 <li>
  <a href="https://github.com/duncs/clusterssh">
   clusterssh
  </a>
  <sup>
   &#9733 286, pushed 2 days ago
  </sup>
  - Cluster Admin Via SSH
 </li>
 <li>
  <a href="https://github.com/dennishafemann/tmux-cssh">
   tmux-cssh
  </a>
  <sup>
   &#9733 210, pushed 27 days ago
  </sup>
  : TMUX with a "ClusterSSH"-like behaviour.
 </li>
 <li>
  <a href="https://github.com/Ganneff/tm">
   tm
  </a>
  <sup>
   &#9733 15, pushed 4 days ago
  </sup>
  : tmux manager / helper
 </li>
 <li>
  <a href="https://github.com/wouterdebie/i2cssh">
   i2cssh
  </a>
  <sup>
   &#9733 228, pushed 75 days ago
  </sup>
  - csshX like ssh tool for iTerm2
 </li>
 <li>
  <a href="http://sourceforge.net/projects/clusterssh/">
   ClusterSSH
  </a>
  - Controls a number of xterm windows via a single graphical console.
 </li>
</ul>
<h3>
 SSH keys / Authentication
</h3>
<ul>
 <li>
  <a href="https://github.com/authy/authy-ssh">
   authy-ssh
  </a>
  <sup>
   &#9733 628, pushed 70 days ago
  </sup>
  - Easy two-factor authentication for ssh servers
 </li>
 <li>
  <a href="https://github.com/chrishunt/github-auth">
   github-auth
  </a>
  <sup>
   &#9733 334, pushed 279 days ago
  </sup>
  - SSH key management for GitHub users.
 </li>
 <li>
  <a href="https://github.com/substack/cipherhub">
   cipherhub
  </a>
  <sup>
   &#9733 385, pushed 586 days ago
  </sup>
  - Encrypt messages based on SSH public keys with easy import from GitHub
 </li>
 <li>
  <a href="http://www.ryanbrink.com/slack-ssh-session-notifications/">
   Slack notifications
  </a>
  - Guide to setup Slack notifications (can be modified for other services).
 </li>
</ul>
<h3>
 SSH agent
</h3>
<ul>
 <li>
  <a href="https://github.com/ccontavalli/ssh-ident">
   ssh-ident
  </a>
  <sup>
   &#9733 351, pushed 12 days ago
  </sup>
  - Different agents and different keys for different projects, with ssh.
 </li>
 <li>
  <a href="https://github.com/robbyrussell/oh-my-zsh/tree/master/plugins/ssh-agent">
   oh-my-zsh/plugins/ssh-agent
  </a>
  - ssh-agent plugin for ZSH.
 </li>
</ul>
<h3>
 Tools
</h3>
<ul>
 <li>
  <a href="https://github.com/Russell91/sshrc">
   sshrc
  </a>
  <sup>
   &#9733 3240, pushed 2 days ago
  </sup>
  - bring your .bashrc, .vimrc, etc. with you when you
  <code>
   ssh
  </code>
 </li>
</ul>
<h3>
 Automation
</h3>
<ul>
 <li>
  <a href="https://github.com/ansible/ansible">
   ansible
  </a>
  <sup>
   &#9733 16550, pushed 2 days ago
  </sup>
  - App deployment, configuration management and orchestration over SSH.
 </li>
 <li>
  <a href="https://github.com/rapidloop/rtop">
   rtop
  </a>
  <sup>
   &#9733 1399, pushed 216 days ago
  </sup>
  - Interactive, remote system monitoring tool based on SSH.
 </li>
 <li>
  <a href="https://www.netfort.gr.jp/~dancer/software/dsh.html.en">
   DSH - Dancer's shell / distributed shell
  </a>
  - Wrapper for executing multiple remote shell commands from one command line.
 </li>
 <li>
  <a href="https://code.google.com/p/parallel-ssh/">
   parallel-ssh
  </a>
  - Provides parallel versions of OpenSSH and related tools.
 </li>
 <li>
  <a href="https://code.google.com/p/sshpt/">
   SSH Power Tool
  </a>
  - Execute commands and upload files to many servers simultaneously without using pre-shared keys.
 </li>
</ul>
<h3>
 Web
</h3>
<ul>
 <li>
  <a href="https://chrome.google.com/webstore/detail/secure-shell/pnhechapfaindjhompbnflcldabbghjo?hl=en">
   Secure Shell chrome extension
  </a>
 </li>
 <li>
  <a href="https://github.com/liftoff/GateOne">
   GateOne
  </a>
  <sup>
   &#9733 3811, pushed 8 days ago
  </sup>
  - HTML5-powered terminal emulator and SSH client
 </li>
 <li>
  <a href="https://github.com/skavanagh/KeyBox">
   KeyBox
  </a>
  <sup>
   &#9733 1078, pushed 9 days ago
  </sup>
  - web-based SSH console that centrally manages administrative access to systems.
 </li>
</ul>
<h3>
 Testing / Honeypots
</h3>
<ul>
 <li>
  <a href="https://github.com/shazow/ssh-hammer">
   ssh-hammer
  </a>
  <sup>
   &#9733 4, pushed 433 days ago
  </sup>
  - SSH load testing tool.
 </li>
 <li>
  <a href="https://github.com/desaster/kippo">
   kippo
  </a>
  <sup>
   &#9733 628, pushed 195 days ago
  </sup>
  - SSH Honeypot
 </li>
 <li>
  <a href="https://github.com/micheloosterhof/cowrie">
   cowrie
  </a>
  <sup>
   &#9733 384, pushed 4 days ago
  </sup>
  - SSH Honeypot (based on kippo)
 </li>
 <li>
  <a href="http://linux.die.net/man/8/sshmitm">
   sshmitm
  </a>
  - SSH monkey-in-the-middle
 </li>
</ul>
<h3>
 Alternatives to SSH
</h3>
<ul>
 <li>
  <a href="https://github.com/yudai/gotty">
   GoTTY
  </a>
  <sup>
   &#9733 6321, pushed 20 days ago
  </sup>
  : Share your terminal as web application
 </li>
 <li>
  <a href="http://www.telnet.org/htm/faq.htm">
   telnet
  </a>
  : An unencrypted network protocol and an application used to connect to remote computers and issue commands.
 </li>
 <li>
  <a href="https://en.wikipedia.org/wiki/Remote_Shell">
   rsh
  </a>
  : An unencrypted network protocol and application used to connect to remote computers and issue commands.
 </li>
</ul>
<h2>
 Libraries
</h2>
<ul>
 <li>
  C/C++
  <ul>
   <li>
    <a href="https://www.libssh.org">
     libssh
    </a>
    : The SSH library.
   </li>
   <li>
    <a href="https://github.com/substack/libssh">
     substack/libssh
    </a>
    <sup>
     &#9733 34, pushed 68 days ago
    </sup>
    : multiplatform C library implementing the SSHv2 and SSHv1 protocol on client and server side.
   </li>
  </ul>
 </li>
 <li>
  Golang
  <ul>
   <li>
    <a href="https://godoc.org/golang.org/x/crypto/ssh">
     crypto/ssh
    </a>
    - built-in SSH client and server library.
   </li>
   <li>
    <a href="https://github.com/pkg/sftp">
     sftp
    </a>
    <sup>
     &#9733 247, pushed 4 days ago
    </sup>
    - SFTP support for the go.crypto/ssh package.
   </li>
   <li>
    <a href="https://github.com/shazow/go-sshkit">
     go-sshkit
    </a>
    <sup>
     &#9733 5, pushed 127 days ago
    </sup>
    - Toolkit for building SSH servers and clients in Go.
   </li>
  </ul>
 </li>
 <li>
  Java
  <ul>
   <li>
    <a href="http://www.jcraft.com/jsch/">
     jsch
    </a>
    - pure java, BSD licensed, SSH2 client library.
   </li>
  </ul>
 </li>
 <li>
  Javascript/Node.js
  <ul>
   <li>
    <a href="https://github.com/mscdex/ssh2">
     ssh2
    </a>
    <sup>
     &#9733 1945, pushed 4 days ago
    </sup>
    - SSH2 client and server modules written in pure JavaScript for node.js
   </li>
  </ul>
 </li>
 <li>
  Python
  <ul>
   <li>
    <a href="https://github.com/paramiko/paramiko">
     paramiko
    </a>
    <sup>
     &#9733 2553, pushed 4 days ago
    </sup>
    : Native Python SSHv2 protocol library.
   </li>
  </ul>
 </li>
 <li>
  Ruby
  <ul>
   <li>
    <a href="https://github.com/net-ssh/net-ssh">
     net-ssh
    </a>
    <sup>
     &#9733 475, pushed 2 days ago
    </sup>
    - Pure Ruby implementation of an SSH (protocol 2) client
   </li>
  </ul>
 </li>
</ul>
<h2>
 Resources
</h2>
<h3>
 Tutorials
</h3>
<ul>
 <li>
  <a href="https://www.digitalocean.com/community/tutorials/how-to-use-ssh-to-connect-to-a-remote-server-in-ubuntu">
   How to use SSH to Connect to a Remote Server
  </a>
 </li>
 <li>
  <a href="https://blog.0xbadc0de.be/archives/300">
   Best practices
  </a>
 </li>
</ul>
<h3>
 Security
</h3>
<ul>
 <li>
  <a href="https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2016-0777">
   01/14/2016
  </a>
  - Integer Overflow CVE 2016 077[7-8]
 </li>
 <li>
  <a href="https://wiki.mozilla.org/Security/Guidelines/OpenSSH">
   Security/Guidelines/OpenSSH - MozillaWiki
  </a>
  - sshd_config for 6.7+, 5.3
 </li>
 <li>
  <a href="https://github.com/BetterCrypto/Applied-Crypto-Hardening/tree/master/src/configuration/SSH/OpenSSH">
   Applied-Crypto-Hardening
  </a>
  - sshd_config for 6.X
 </li>
</ul>
<h3>
 Documentation
</h3>
<ul>
 <li>
  <a href="http://linux.die.net/man/1/ssh">
   man page
  </a>
 </li>
 <li>
  <a href="http://www.openssh.com/specs.html">
   Specifications (OpenSSH)
  </a>
 </li>
 <li>
  <a href="https://en.wikipedia.org/wiki/Secure_Shell">
   Wikipedia article
  </a>
 </li>
</ul>
<h3>
 Community
</h3>
<ul>
 <li>
  <a href="http://stackoverflow.com/questions/tagged/ssh">
   StackOverflow
  </a>
 </li>
 <li>
  <a href="http://serverfault.com/questions/tagged/ssh">
   ServerFault
  </a>
 </li>
</ul>
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
 <a href="https://github.com/moul">
  Manfred Touron
 </a>
 has waived all copyright and related or neighboring rights to this work.
</p>
