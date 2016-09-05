<h1>
 Awesome Site Reliability Engineering
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<p>
 A curated list of awesome
 <a href="https://www.usenix.org/conference/srecon14/technical-sessions/presentation/keys-sre">
  Site Reliability
 </a>
 and
 <a href="https://www.usenix.org/conference/srecon15/program/presentation/canahuati">
  Production
 </a>
 Engineering resources.
</p>
<h4>
 What is Site Reliability Engineering?
</h4>
<blockquote>
 <p>
  "Fundamentally, it's what happens when you ask a software engineer to design an operations function." - Ben Treynor Sloss, VP Google Engineering, founder of Google SRE
 </p>
</blockquote>
<h2>
 Contributing
</h2>
<p>
 Please take a look at the
 <a href="CONTRIBUTING.md">
  contribution guidelines
 </a>
 first.
Contributions are always welcome!
</p>
<h2>
 Contents
</h2>
<ul>
 <li>
  <a href="#culture">
   Culture
  </a>
 </li>
 <li>
  <a href="#education">
   Education
  </a>
 </li>
 <li>
  <a href="#books">
   Books
  </a>
 </li>
 <li>
  <a href="#hiring">
   Hiring
  </a>
 </li>
 <li>
  <a href="#reliability">
   Reliability
  </a>
 </li>
 <li>
  <a href="#alerting">
   Alerting
  </a>
 </li>
 <li>
  <a href="#monitoring">
   Monitoring
  </a>
 </li>
 <li>
  <a href="#on-call">
   On-Call
  </a>
 </li>
 <li>
  <a href="#post-mortem">
   Post-Mortem
  </a>
 </li>
 <li>
  <a href="#capacity-planning">
   Capacity Planning
  </a>
 </li>
 <li>
  <a href="#service-level-agreement">
   Service Level Agreement
  </a>
 </li>
 <li>
  <a href="#performance">
   Performance
  </a>
 </li>
 <li>
  <a href="#articles">
   Articles
  </a>
 </li>
 <li>
  <a href="#blogs">
   Blogs
  </a>
 </li>
 <li>
  <a href="#conferences">
   Conferences
  </a>
 </li>
 <li>
  <a href="#twitter">
   Twitter
  </a>
 </li>
</ul>
<h2>
 Culture
</h2>
<ul>
 <li>
  <a href="https://landing.google.com/sre/interview/ben-treynor.html">
   What is Site Reliability Engineering?
  </a>
 </li>
 <li>
  <a href="https://www.usenix.org/conference/srecon14/technical-sessions/presentation/keys-sre">
   Keys To SRE by Ben Treynor
  </a>
 </li>
 <li>
  <a href="https://landing.google.com/sre/resources.html">
   Google SRE Resources
  </a>
 </li>
 <li>
  <a href="https://www.usenix.org/conference/srecon15/program/presentation/canahuati">
   Notes from Production Engineering by Pedro Canahuati
  </a>
 </li>
 <li>
  <a href="https://www.usenix.org/conference/srecon15europe/program/presentation/underwood">
   PostOps: Recovery from Operations
  </a>
 </li>
 <li>
  <a href="https://www.atlassian.com/it-service/site-reliability-engineering-sre">
   Love DevOps? Wait 'till you meet SRE
  </a>
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=H4vMcD7zKM0">
   How Google Does Planet-Scale Engineering for Planet-Scale Infra
  </a>
 </li>
 <li>
  <a href="https://www.facebook.com/notes/facebook-engineering/site-reliability-engineering-at-facebook/291616313919/">
   Site Reliability Engineering at Facebook
  </a>
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=qJnS-EfIIIE&nohtml5=False">
   A History of Site Reliability Engineering at Uber
  </a>
 </li>
 <li>
  <a href="https://www.usenix.org/conference/srecon15/program/presentation/limoncelli">
   Case Study: Adopting SRE Principles at StackOverflow
  </a>
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=ggizCjUCCqE">
   Site Reliability Engineering at Dropbox
  </a>
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=yXI7r0_J29M">
   Site Reliability Engineers — Keeping Google up and running 24/7
  </a>
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=JLkr6UHXN44&nohtml5=False">
   Site Reliability Engineering at Salesforce
  </a>
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=lZI51YzIgVE">
   From Sys Admin to Netflix SRE
  </a>
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=iIuTnhdTzK0">
   SRE@Google: Thousands of DevOps Since 2004
  </a>
 </li>
 <li>
  <a href="https://www.usenix.org/conference/lisa15/conference-program/presentation/limoncelli">
   Transactional System Administration Is Killing Us and Must be Stopped
  </a>
 </li>
 <li>
  <a href="https://plus.google.com/+lizthegrey/posts/MLAJFVyEb2f">
   Maslow's hierarchy of SRE needs
  </a>
 </li>
 <li>
  <a href="https://www.usenix.org/conference/lisa13/technical-sessions/plenary/underwood">
   PostOps: A Non-Surgical Tale of Software, Fragility, and Reliability
  </a>
 </li>
 <li>
  <a href="https://www.socallinuxexpo.org/sites/default/files/presentations/Scale%20x14%20Slides.pdf">
   From SysAdmin to Netflix SRE
  </a>
 </li>
 <li>
  <a href="http://anthonycaiafa.com/2016/04/10/sre-cultural-narnia/">
   SRE: An incomplete guide to cultural Narnia
  </a>
 </li>
 <li>
  <a href="https://www.usenix.org/conference/srecon16/program/presentation/krishnan">
   Putting Together Great SRE Teams
  </a>
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=bwt6TZjefGM">
   Work at Google: Meet our Production Engineers for Site Reliability Hangout on Air
  </a>
 </li>
 <li>
  <a href="https://medium.com/production-ready/toil-a-word-every-engineer-should-know-f0b676e41c86">
   Toil: A Word Every Engineer Should Know
  </a>
 </li>
 <li>
  <a href="https://research.google.com/pubs/pub32583.html">
   Engineering Reliability into Web Sites: Google SRE
  </a>
 </li>
 <li>
  <a href="http://pages.catchpoint.com/DEVOPS-SRE-AMA-mkty.html">
   DEVOPS & SRE AMA - Building High Performance Organizations
  </a>
 </li>
 <li>
  <a href="https://www.gcppodcast.com/post/episode-38-site-reliability-engineering-with-paul-newson/">
   Site Reliability Engineering with Paul Newson
  </a>
 </li>
</ul>
<h2>
 Education
</h2>
<ul>
 <li>
  <a href="https://www.usenix.org/conference/srecon15/program/presentation/sebenik">
   Panel: Educating SRE
  </a>
 </li>
 <li>
  <a href="https://www.usenix.org/conference/srecon15/program/presentation/widdowson">
   From Zero to Hero: Recommended Practices for Training your Ever-Evolving SRE Teams
  </a>
 </li>
 <li>
  <a href="http://anthonycaiafa.com/2016/04/27/new-to-a-team/">
   New to an SRE team?
  </a>
 </li>
 <li>
  <a href="https://www.usenix.org/publications/login/june15/hixson">
   The Systems Engineering Side of Site Reliability Engineering
  </a>
 </li>
</ul>
<h2>
 Books
</h2>
<ul>
 <li>
  <a href="https://landing.google.com/sre/book.html">
   Site Reliability Engineering: How Google Runs Production Systems
  </a>
 </li>
 <li>
  <a href="http://the-cloud-book.com/">
   The Practice Of Cloud System Administration: Designing and Operating Large Distributed Systems
  </a>
 </li>
 <li>
  <a href="http://shop.oreilly.com/product/0636920000136.do">
   Web Operations - Keeping the Data On Time
  </a>
 </li>
 <li>
  <a href="http://atulgawande.com/book/the-checklist-manifesto/">
   The Checklist Manifesto: How to Get Things Right
  </a>
 </li>
</ul>
<h2>
 Hiring
</h2>
<ul>
 <li>
  <a href="https://www.usenix.org/conference/srecon15/program/presentation/fong">
   SRE Hiring
  </a>
 </li>
 <li>
  <a href="https://engineering.linkedin.com/engineering-culture/hiring-sres-linkedin">
   Hiring SREs at LinkedIn
  </a>
 </li>
 <li>
  <a href="https://www.usenix.org/publications/login/june15/hiring-site-reliability-engineers">
   Hiring Site Reliability Engineers
  </a>
 </li>
</ul>
<h2>
 Reliability
</h2>
<ul>
 <li>
  <a href="https://www.usenix.org/conference/srecon16/program/presentation/kroll">
   The Realities of the Job of Delivering Reliability
  </a>
 </li>
 <li>
  <a href="http://queue.acm.org/detail.cfm?id=2839461">
   Fail at Scale by Ben Maurer
  </a>
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=wrY7XoOnysg">
   Embracing Failure: Fault-Injection and Service Reliability
  </a>
 </li>
 <li>
  <a href="https://www.usenix.org/conference/lisa15/conference-program/presentation/krishnan">
   10 Years of Crashing Google
  </a>
 </li>
 <li>
  <a href="https://blog.twitter.com/2015/how-we-break-things-at-twitter-failure-testing">
   How we break things at Twitter: failure testing
  </a>
 </li>
 <li>
  <a href="http://queue.acm.org/detail.cfm?id=2745840">
   Reliable Cron across the Planet
  </a>
 </li>
 <li>
  <a href="https://blog.twitter.com/2014/push-our-limits-reliability-testing-at-twitter">
   Push our limits - reliability testing at Twitter
  </a>
 </li>
 <li>
  <a href="http://queue.acm.org/detail.cfm?ref=rss&id=2889274">
   The Verification of a Distributed System by Caitie McCaffrey
  </a>
 </li>
 <li>
  <a href="http://queue.acm.org/detail.cfm?id=2371516">
   Weathering the Unexpected
  </a>
 </li>
 <li>
  <a href="http://files.sans.org/summit/Threat_Hunting_Incident_Response_Summit_2016/PDFs/The-Remediation-Ballet-Performing-the-Delicate-Dance-of-Clean-Up-Matt-Linton-Google.pdf">
   The Remediation Ballet
  </a>
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=YFDwdRVTg4g">
   SRE Hour: Tech Talks by Box & Yelp
  </a>
 </li>
 <li>
  <a href="https://medium.com/production-ready/simplicity-a-prerequisite-for-reliability-8d000f8d18df#.74t9t0em2">
   Simplicity: A Prerequisite for Reliability
  </a>
 </li>
 <li>
  <a href="https://speakerdeck.com/garethr/the-two-sides-to-google-infrastructure-for-everyone-else">
   The Two Sides to Google Infrastructure for Everyone Else
  </a>
 </li>
 <li>
  <a href="https://www.usenix.org/conference/ures14west/summit-program/presentation/dickson">
   How Embracing Continuous Release Reduced Change Complexity
  </a>
 </li>
 <li>
  <a href="https://www.usenix.org/publications/login/october-2014-vol-39-no-5/making-push-green-reality">
   Making "Push On Green" a Reality
  </a>
 </li>
 <li>
  <a href="https://www.usenix.org/publications/login/dec14/ward">
   BeyondCorp: A New Approach to Enterprise Security
  </a>
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=dKe9S8u44Yk">
   Brainstorming Failure by Jeff Smith
  </a>
 </li>
 <li>
  <a href="http://cloudtweaks.com/2016/04/outages-and-downtime/">
   The Ripple Effect Of Outages And Downtime Cannot Be Underestimated
  </a>
 </li>
 <li>
  <a href="https://blog.twitter.com/2016/the-infrastructure-behind-twitter-efficiency-and-optimization">
   The infrastructure behind Twitter: efficiency and optimization
  </a>
 </li>
</ul>
<h2>
 Alerting
</h2>
<ul>
 <li>
  <a href="https://docs.google.com/document/d/199PqyG3UsyXlwieHaqbGiWVa8eMWi8zzAn0YfcApr8Q/preview#">
   My Philosophy on Alerting by Rob Ewaschuk
  </a>
 </li>
</ul>
<h2>
 Monitoring
</h2>
<ul>
 <li>
  <a href="https://www.usenix.org/conference/lisa13/working-theory-monitoring">
   A Working Theory-of-Monitoring
  </a>
 </li>
 <li>
  <a href="https://vimeo.com/131484321">
   The Evolution of Monitoring Systems at Google - Tony Rippy
  </a>
 </li>
 <li>
  <a href="https://www.usenix.org/conference/srecon15/program/presentation/serebryany">
   Monitoring without Infrastructure @ Airbnb
  </a>
 </li>
 <li>
  <a href="https://www.oreilly.com/ideas/monitoring-distributed-systems">
   Monitoring distributed systems
  </a>
 </li>
</ul>
<h2>
 On-Call
</h2>
<ul>
 <li>
  <a href="http://research.google.com/pubs/pub44813.html">
   Being an On-Call Engineer: A Google SRE Perspective
  </a>
 </li>
 <li>
  <a href="http://blogs.atlassian.com/2016/02/inside-atlassian-site-reliability-engineers-incident-management/">
   Inside Atlassian: how our site reliability engineers do incident management
  </a>
 </li>
 <li>
  <a href="http://blogs.atlassian.com/2016/02/inside-atlassian-sre-use-chatops-run-incident-management/">
   Inside Atlassian: how IT & SRE use ChatOps to run incident management
  </a>
 </li>
 <li>
  <a href="https://blog.heroku.com/archives/2014/5/9/incident-response-at-heroku">
   Incident Response at Heroku
  </a>
 </li>
</ul>
<h2>
 Post-Mortem
</h2>
<ul>
 <li>
  <a href="https://github.com/danluu/post-mortems">
   A collection of post-mortems
  </a>
 </li>
 <li>
  <a href="https://codeascraft.com/2012/05/22/blameless-postmortems/">
   Blameless PostMortems and a Just Culture
  </a>
 </li>
 <li>
  <a href="https://blog.box.com/blog/a-tale-of-postmortems/">
   A Tale of Postmortems
  </a>
 </li>
</ul>
<h2>
 Capacity Planning
</h2>
<ul>
 <li>
  <a href="https://www.usenix.org/system/files/login/articles/login_feb15_07_hixson.pdf">
   Capacity Planning
  </a>
 </li>
</ul>
<h2>
 Service Level Agreement
</h2>
<ul>
 <li>
  <a href="https://www.youtube.com/watch?v=tZ0-SISvCis">
   SLA Aware Maintenance for Operators - Joe Smith
  </a>
 </li>
 <li>
  <a href="http://er.educause.edu/articles/2010/6/if-its-in-the-cloud-get-it-on-paper-cloud-computing-contract-issues">
   If It's in the Cloud, Get It on Paper: Cloud Computing Contract Issues
  </a>
 </li>
 <li>
  <a href="http://www.wired.com/insights/2011/12/service-level-agreements-in-the-cloud-who-cares/">
   Service Level Agreements in the Cloud: Who cares?
  </a>
 </li>
 <li>
  <a href="https://blog.serverdensity.com/making-a-point-with-slas/">
   Making a point with SLAs
  </a>
 </li>
</ul>
<h2>
 Performance
</h2>
<ul>
 <li>
  <a href="https://www.usenix.org/conference/srecon16/program/presentation/gregg">
   Performance Checklists for SREs
  </a>
 </li>
</ul>
<h2>
 Programming
</h2>
<ul>
 <li>
  <a href="http://www.oreilly.com/pub/e/2712">
   Go Language for Ops and Site Reliability Engineering
  </a>
 </li>
 <li>
  <a href="https://www.usenix.org/sites/default/files/conference/protected-files/srecon16_slides_hamilton.pdf">
   Go for SREs using Python
  </a>
 </li>
</ul>
<h2>
 Articles
</h2>
<ul>
 <li>
  <a href="https://www.oreilly.com/ideas/what-is-sre-site-reliability-engineering">
   What is SRE (Site Reliability Engineering)?
  </a>
 </li>
 <li>
  <a href="http://www.wired.com/2016/04/google-ensures-services-almost-never-go/">
   Here’s How Google Makes Sure It (Almost) Never Goes Down
  </a>
 </li>
 <li>
  <a href="http://techcrunch.com/2016/03/02/are-site-reliability-engineers-the-next-data-scientists/">
   Are site reliability engineers the next data scientists?
  </a>
 </li>
 <li>
  <a href="http://googleresearch.blogspot.gr/2012/07/site-reliability-engineers-solving-most.html">
   Site Reliability Engineers: "solving the most interesting problems"
  </a>
 </li>
 <li>
  <a href="http://googleforstudents.blogspot.gr/2012/06/site-reliability-engineers-worlds-most.html">
   Site Reliability Engineers: the "world’s most intense pit crew"
  </a>
 </li>
 <li>
  <a href="http://searchitoperations.techtarget.com/feature/Site-reliability-engineering-kicks-rote-tasks-out-of-IT-ops">
   Site reliability engineering kicks rote tasks out of IT ops
  </a>
 </li>
 <li>
  <a href="http://danluu.com/google-sre-book/">
   Notes on Site Reliability Engineering
  </a>
 </li>
 <li>
  <a href="https://cloudplatform.googleblog.com/2016/07/adventures-in-SRE-land-welcome-to-Google-Mission-Control.html">
   Adventures in SRE-land: Welcome to Google Mission Control
  </a>
 </li>
</ul>
<h2>
 Real-time Messaging
</h2>
<ul>
 <li>
  <a href="https://hangops.slack.com/">
   #sre channel at Hangops Slack
  </a>
  - Discussion of Site Reliability Engineering generally.
 </li>
 <li>
  <a href="https://hangops.slack.com/">
   #incident_response channel at Hangops Slack
  </a>
  - Discussion about Incident Response.
 </li>
</ul>
<h2>
 Blogs
</h2>
<ul>
 <li>
  <a href="http://www.brendangregg.com/blog/index.html">
   Brendan Gregg's Blog
  </a>
  - Highly Techincal Blog Posts About Systems Internals, Performance and SRE.
 </li>
 <li>
  <a href="http://everythingsysadmin.com/">
   Everything Sysadmin
  </a>
  - Blog Posts About SysAdmin/DevOps/SRE by Tom Limoncelli.
 </li>
 <li>
  <a href="http://highscalability.com/">
   High Scalability
  </a>
  - Technical Blog Posts About Systems Architecture.
 </li>
 <li>
  <a href="https://rachelbythebay.com/w/">
   rachelbythebay
  </a>
  - Techincal Blog Posts.
 </li>
 <li>
  <a href="https://sreweekly.com/">
   SRE Weekly
  </a>
  - Weekly Site Reliability Newsletter.
 </li>
 <li>
  <a href="https://tinyletter.com/production-ready">
   Production Ready
  </a>
  - A mailing list about building resilient infrastructure and tools.
 </li>
</ul>
<h2>
 Conferences
</h2>
<ul>
 <li>
  <a href="https://www.usenix.org/conferences/byname/925">
   SRECon Conferences
  </a>
  - The Official SRE Conference.
 </li>
 <li>
  <a href="https://www.usenix.org/conferences/byname/5">
   LISA Conferences
  </a>
  - Prominent Conference About SysAdmin/DevOps/SRE.
 </li>
 <li>
  <a href="https://developers.google.com/events/sre/">
   SRE Tech Talks
  </a>
  - SRE Talks Hosted by Google.
 </li>
</ul>
<h2>
 Twitter
</h2>
<ul>
 <li>
  <a href="https://twitter.com/alicegoldfuss">
   Alice Goldfuss
  </a>
  - SRE @ New Relic - Tweets About the SRE Culture.
 </li>
 <li>
  <a href="https://twitter.com/brendangregg">
   Brendan Gregg
  </a>
  - SRE @ Netflix - Technical Resources about Systems, Performance and Site Reliability Engineers.
 </li>
 <li>
  <a href="https://twitter.com/caitie">
   Caitie McCaffrey
  </a>
  - Tweets About Reliability and Distributed Systems.
 </li>
 <li>
  <a href="https://twitter.com/relix42">
   Dave Hahn
  </a>
  - SRE @ Netflix.
 </li>
 <li>
  <a href="https://twitter.com/highscal">
   Highscal
  </a>
  - Feed of the High Scalability Blog.
 </li>
 <li>
  <a href="https://twitter.com/jennski">
   Jennifer Petoff
  </a>
  - Program Manager for Google's Site Reliability Engineering team.
 </li>
 <li>
  <a href="https://twitter.com/JesseDearing">
   Jesse DB
  </a>
  - SRE @ New Relic.
 </li>
 <li>
  <a href="https://twitter.com/jonahhorowitz">
   Jonah horowitz
  </a>
  - SRE @ Netflix.
 </li>
 <li>
  <a href="https://twitter.com/niallm">
   Niall Murphy
  </a>
  - SRE @ Google.
 </li>
 <li>
  <a href="https://twitter.com/Nick_Craver">
   Nick Craver
  </a>
  - SRE @ StackOverflow.
 </li>
 <li>
  <a href="https://twitter.com/SREBook">
   SREBook
  </a>
  - The Official Twitter Account of Site Reliability Engineering Book.
 </li>
 <li>
  <a href="https://twitter.com/SREcon">
   SREcon
  </a>
  - SRECon's Official Twitter Account.
 </li>
 <li>
  <a href="https://twitter.com/yesthattom">
   Thomas A. Limoncelli
  </a>
  - Prominent Author About SysAdmin/DevOps/SRE.
 </li>
 <li>
  <a href="https://twitter.com/tmu">
   Todd Underwood
  </a>
  - SRE @ Google.
 </li>
 <li>
  <a href="https://twitter.com/TwitterSRE">
   Twitter SRE
  </a>
  - The Official Twitter Account of Twitter's SRE team.
 </li>
 <li>
  <a href="https://twitter.com/usenix">
   USENIX Association
  </a>
  - The Official USENIX Twitter Account.
 </li>
</ul>
