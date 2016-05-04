<h1>
 Critical-path (Above-the-fold) CSS Tools
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<blockquote>
 <p>
  Tools to help prioritize above-the-fold CSS
 </p>
</blockquote>
<h3>
 Prioritize above-the-fold content first.
</h3>
<p>
 For best performance, PageSpeed Insights
 <a href="https://developers.google.com/speed/docs/insights/PrioritizeVisibleContent">
  recommends
 </a>
 inlining the critical (above-the-fold) CSS of your page directly into your HTML. This eliminates additional roundtrips and allows the browser to paint the above-fold experience to your user's screen sooner. The main idea is:
</p>
<ul>
 <li>
  Determine the above-the-fold styles for a page and write them between
  <code>
   <style>
   </style>
  </code>
 </li>
</ul>