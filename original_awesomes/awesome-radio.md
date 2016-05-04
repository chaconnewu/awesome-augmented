<h1>
 Awesome Radio
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<p>
 A curated list of awesome radio resources. Inspired by awesome-*.
</p>
<p>
 I recently pulled out my CB radio and installed it in my truck. This inspired me
to create an open source repository of all the radio related resources I found
helpful and my notes on the subject.
</p>
<p>
 This project is aimed at hackers who enjoy all aspects of radio communication.
While a lot of this technology isn't usable by citizens and is heavily regulated
by the FCC, just knowing anything about it is special. I've been interested in
learning the ins and outs of radio, as well as hearing stories, new and old.
</p>
<h2>
 General
</h2>
<h3>
 Links
</h3>
<ul>
 <li>
  <a href="http://en.wikipedia.org/wiki/Radio">
   Radio (wikipedia)
  </a>
 </li>
 <li>
  <a href="http://en.wikipedia.org/wiki/Radio_spectrum">
   Radio Spectrum (wikipedia)
  </a>
 </li>
 <li>
  <a href="http://en.wikipedia.org/wiki/Skywave">
   Skywave (skip) (wikipedia)
  </a>
 </li>
 <li>
  <a href="http://www.windytan.com/2014/02/mystery-signal-from-helicopter.html">
   Mystery signal from a
helicopter
  </a>
 </li>
 <li>
  <a href="http://hackaday.io/project/1538-PortableSDR">
   Portable SDR
  </a>
 </li>
</ul>
<h2>
 CB
</h2>
<p>
 Citizens band radio, or CB, is a two way radio spectrum dedicated to open use by
anyone for almost any purpose. In the US and many other countries, it
does not require a license to operate. CB consists of 40 channels between 26.965
MHz and 27.405 MHz with channel 09 being dedicated to emergencies.
</p>
<p>
 CB is more popular among truckers and radio enthusiasts, but its usefulness
does not stop there. It's great for long distance travel on popular trucking
routes. You can tune to channel 19 (an unofficial trucker's channel) and get
real time traffic updates, alternate routes and accident warnings.
</p>
<p>
 Given a good antenna that's properly tuned, a typical range to expect out of
your CB is about 2 - 5 miles (3.2 - 8 kilometers).
</p>
<h3>
 General Use
</h3>
<p>
 I've found a lot of my information on Jeep and trucker forums. From my own
experience, it seems about half the CB transmission I hear include a handle of
some kind. I also hear a lot of swearing, so I wouldn't sweat accidentally
letting a "fuck" or a "shit" go.
</p>
<p>
 CB is public. Very public. That seems like a "no shit" kind of thing, but with
the current generation pretty much only using cell phones, it's easy to forget
that using something as "primitive" as a CB radio is essentially
 <a href="http://en.wikipedia.org/wiki/Citizens_band_radio#Working_skip">
  broadcast to
the world
 </a>
 .
</p>
<p>
 Truckers tend to use channel 19. This is a good channel to monitor for traffic
conditions.
</p>
<p>
 Channel 9 is for emergencies only. No general chatter on this channel. If you
are broke down, or your car catches fire, besides calling 911, this is a good
channel to transmit on for help.
</p>
<p>
 Around Portland, I hear a lot of chatter on channels 6, 17 and 28. These are
good channels for entertaining conversation.
</p>
<h3>
 SWR
</h3>
<p>
 <a href="http://en.wikipedia.org/wiki/Standing_wave_ratio">
  SWR
 </a>
 , or Standing Wave Ratio
is a measurement of efficiency when connecting your antenna to your radio.
</p>
<p>
 Optimum ratio is 1:1, although you'll probably end up with 1.3:1 or so. Anything
higher than 2:1 should be considered a no-no since it can damage your radio and
give poor transmission. Read up on
 <a href="http://www.rightchannelradios.com/tuning-cb-antenna-adjusting-swr">
  how to tune
SWR
 </a>
 .
</p>
<h3>
 Installing a mobile CB
</h3>
<p>
 Installing your CB right is key to A) not damaging your radio hardware and B)
getting good range and quality on both the receiving and transmitting ends.
</p>
<p>
 Following the advice in the following articles will ensure you have a quality
setup.
</p>
<h3>
 Links
</h3>
<ul>
 <li>
  <a href="http://www.rightchannelradios.com/">
   Right Channel Radios
  </a>
  - Good online shop
for parts, radios, antennas and mounts.
 </li>
 <li>
  <a href="http://www.cbslang.com/">
   CB Slang
  </a>
  - mostly humorous, but kinda helpful.
 </li>
 <li>
  <a href="http://en.wikipedia.org/wiki/List_of_CB_slang">
   CB Slang (wikipedia)
  </a>
 </li>
 <li>
  <a href="http://www.jeepforum.com/forum/f8/cb-radio-etiquette-jeep-trail-1169815/">
   CB Talk and etiquette
  </a>
 </li>
 <li>
  <a href="http://cbradiomagazine.com/Articles/How%20to%20Shoot%20Skip.htm">
   Skip
  </a>
 </li>
 <li>
  <a href="http://www.somethingawful.com/news/cb-handles/">
   Silly CB Handles
  </a>
 </li>
 <li>
  <a href="http://www.advancedspecialties.net/cb-radio-faq.htm">
   CB FAQ
  </a>
 </li>
 <li>
  <a href="http://www.radioreference.com/apps/db/?aid=7731">
   Frequency Table
  </a>
 </li>
</ul>
<h2>
 SDR (Software Defined Radio)
</h2>
<p>
 Software Defined Radio is a way to define components that are typically
hardware, such as filters and amplifiers, as software. It has been around for a
while, but with the cost of digital electronics needed to run SDR becoming
increasingly cheaper, we are seeing a rise in hacker folk playing and building
with SDR.
</p>
<p>
 I would like contributors for this section.
</p>
<h3>
 Links
</h3>
<ul>
 <li>
  <a href="http://gqrx.dk/">
   Gqrx
  </a>
 </li>
 <li>
  <a href="http://sdrsharp.com">
   sdrsharp on .NET
  </a>
 </li>
</ul>
<h3>
 Hardware
</h3>
<ul>
 <li>
  <strong>
   Recommended starter hardware
  </strong>
  On the low end,
  <a href="http://sdr.osmocom.org/trac/wiki/rtl-sdr">
   RTL-SDR
  </a>
  is a super-cheap usb
dongle, around which a thriving community has been founded.
 </li>
 <li>
  On the other side of the cost spectrum,
  <a href="http://www.pervices.com/">
   pervices
  </a>
  makes some really high-throughput, PCIe devices for when you need to log all
the traffic ever. The software and community support for this is less good,
though (for which you can blame @outofculture).
 </li>
 <li>
  You can also browse through the
  <a href="https://gnuradio.org/redmine/projects/gnuradio/wiki/Hardware">
   big
list
  </a>
  of all
compatible hardware.
 </li>
 <li>
  Antennas are their own body of options and tradeoffs, about which I know
nothing.
 </li>
</ul>
<h3>
 Software
</h3>
<p>
 Depending on the hardware you're using, it may ship with some demo software to
play around with. This is great for just getting a chance to see some waves and
start to get an idea of what's possible. Otherwise,
 <a href="https://gnuradio.org/redmine/">
  GNU
Radio
 </a>
 is going to where you'll spend your time.
It's mainly just a library, but it also has a supporting gui for combining
processing blocks that then outputs python. Once you're more comfortable, you
can also just use GNURadio to do any device tuning, setup and i/o, and then use
numpy for the signal manipulation math.
</p>
<p>
 Just visualizing and manually inspecting a signal is a valuable part of learning
how to work with them.
 <a href="http://www.baudline.com/">
  Baudline
 </a>
 is a janky old
thing, but it's the best there is. Be forewarned that learning the UI won't come
easily to anyone.
</p>
<h2>
 Amateur Radio (a.k.a Ham Radio)
</h2>
<p>
 The hobby of Amateur Radio has a long and proud tradition. The very first radio
amateurs were true pioneers of radio technology. Amateurs 'invented' and refined
much of the early radio technology and were the first to transmit music, radio
plays, and information to the handful of people who had the new fangled radio
receivers.
</p>
<p>
 After World War II the hobby of amateur radio flourished. Radio clubs sprang up
in schools all over the world and kids went home each night to build some new
contraption, or have a chat with someone over the wireless. These young people
became the mainstay of the technical professions and developed much of the
modern technology we use today.
(
 <a href="http://www.wia.org.au/licenses/foundation/about/">
  WIA
 </a>
 )
</p>
<p>
 <a href="http://www.arrl.org/what-is-ham-radio">
  What is Ham Radio?
 </a>
</p>
<h3>
 Links
</h3>
<ul>
 <li>
  American Radio Relay League -
  <a href="http://www.arrl.org/">
   ARRL
  </a>
 </li>
 <li>
  The Wireless Institute of Australia
  <a href="http://www.wia.org.au/">
   WIA
  </a>
 </li>
 <li>
  Radio Society of Great Britain -
  <a href="http://rsgb.org/">
   RSGB
  </a>
 </li>
 <li>
  Pakistan Amateur Radio Society -
  <a href="http://www.pakhams.com/">
   PARS
  </a>
 </li>
 <li>
  <a href="http://www.iaru.org/">
   The International Amateur Radio Union
  </a>
 </li>
 <li>
  <a href="http://www.arrl.org/news/amateur-radio-transponder-will-accompany-japanese-asteroid-mission-into-deep-space">
   Japanese asteroid mission
  </a>
 </li>
 <li>
  <a href="https://en.wikipedia.org/wiki/Slow-scan_television">
   Slow-scan Television
  </a>
 </li>
</ul>
<p>
 I would like contributors for this section.
</p>
<h3>
 Amateur Radio License
</h3>
<ul>
 <li>
  In the
  <a href="http://www.arrl.org/getting-licensed">
   US
  </a>
  there are three license
classes—Technician, General and Extra.
 </li>
 <li>
  <a href="http://www.wia.org.au/licenses/foundation/about/">
   The Foundation Licence
  </a>
  in
Australia.
 </li>
 <li>
  [Foundation Licence]
(http://rsgb.org/main/clubs-training/for-students/foundation/) in the UK.
 </li>
 <li>
  In
  <a href="http://www.pakhams.com/index.php?option=com_content&view=article&id=75&Itemid=92">
   Pakistan
  </a>
  first you apply for SWL (Short Wave Listener) membership and then you are
eligible to
  <a href="http://www.pta.gov.pk/index.php?option=com_content&view=article&id=466%3Aamateur-wireless-license&catid=138%3Aguidelines&Itemid=349">
   apply for the HAM
License
  </a>
  .
 </li>
</ul>
<h2>
 Public Health and Safety
</h2>
<p>
 Police and fire in the United States typically communicate over trunked radio.
This makes it hard to scan using normal reciever without trunk tracking
abilities. See more in the
 <a href="#trunking">
  trunking
 </a>
 section.
</p>
<h3>
 Trunking
</h3>
<p>
 While not strictly specific to public health and safety, it is usually the first
thing that comes to mind when talking about trunked radio.
</p>
<p>
 Trunked radio is a form of digital-two-way communication where multiple
organizations can share a small spectrum of real frequencies without hearing
another organizations conversations. A user can choose a logical channel or
group and the base station will find an empty frequency to transmit on.
</p>
<h3>
 Links
</h3>
<ul>
 <li>
  <a href="http://www.project25.org/">
   Project 25
  </a>
 </li>
 <li>
  <a href="http://en.wikipedia.org/wiki/Project_25">
   Project 25 wikipedia
  </a>
 </li>
 <li>
  <a href="http://en.wikipedia.org/wiki/Trunked_radio_system">
   Trunked Radio wikipedia
  </a>
 </li>
</ul>
