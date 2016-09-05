<p align="center">
 <img alt="light bulb icon" src="https://rawgit.com/AllThingsSmitty/css-protips/master/media/logo.svg">
 </img>
</p>
<h1>
 CSS Protips
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<p>
 A collection of tips to help take your CSS skills pro.
</p>
<blockquote>
 <p>
  For other great lists check out
  <a href="https://github.com/sindresorhus/">
   @sindresorhus
  </a>
  's curated list of
  <a href="https://github.com/sindresorhus/awesome/">
   awesome lists
  </a>
  .
 </p>
</blockquote>
<h2>
 Table of Contents
</h2>
<ul>
 <li>
  <a href="#protips">
   Protips
  </a>
 </li>
 <li>
  <a href="#support">
   Support
  </a>
 </li>
 <li>
  <a href="#translations">
   Translations
  </a>
 </li>
 <li>
  <a href="CONTRIBUTING.md">
   Contribution Guidelines
  </a>
 </li>
</ul>
<h2>
 Protips
</h2>
<ol>
 <li>
  <a href="#use-not-to-applyunapply-borders-on-navigation">
   Use
   <code>
    :not()
   </code>
   to Apply/Unapply Borders on Navigation
  </a>
 </li>
 <li>
  <a href="#add-line-height-to-body">
   Add
   <code>
    line-height
   </code>
   to
   <code>
    body
   </code>
  </a>
 </li>
 <li>
  <a href="#vertically-center-anything">
   Vertically-Center Anything
  </a>
 </li>
 <li>
  <a href="#comma-separated-lists">
   Comma-Separated Lists
  </a>
 </li>
 <li>
  <a href="#select-items-using-negative-nth-child">
   Select Items Using Negative
   <code>
    nth-child
   </code>
  </a>
 </li>
 <li>
  <a href="#use-svg-for-icons">
   Use SVG for Icons
  </a>
 </li>
 <li>
  <a href="#use-the-lobotomized-owl-selector">
   Use the "Lobotomized Owl" Selector
  </a>
 </li>
 <li>
  <a href="#use-max-height-for-pure-css-sliders">
   Use
   <code>
    max-height
   </code>
   for Pure CSS Sliders
  </a>
 </li>
 <li>
  <a href="#inherit-box-sizing">
   Inherit
   <code>
    box-sizing
   </code>
  </a>
 </li>
 <li>
  <a href="#equal-width-table-cells">
   Equal-Width Table Cells
  </a>
 </li>
 <li>
  <a href="#get-rid-of-margin-hacks-with-flexbox">
   Get Rid of Margin Hacks With Flexbox
  </a>
 </li>
 <li>
  <a href="#use-attribute-selectors-with-empty-links">
   Use Attribute Selectors with Empty Links
  </a>
 </li>
 <li>
  <a href="#style-default-links">
   Style "Default" Links
  </a>
 </li>
 <li>
  <a href="#consistent-vertical-rhythm">
   Consistent Vertical Rhythm
  </a>
 </li>
 <li>
  <a href="#intrinsic-ratio-boxes">
   Intrinsic Ratio Boxes
  </a>
 </li>
 <li>
  <a href="#style-broken-images">
   Style Broken Images
  </a>
 </li>
 <li>
  <a href="#use-rem-for-global-sizing-use-em-for-local-sizing">
   Use
   <code>
    rem
   </code>
   for Global Sizing; Use
   <code>
    em
   </code>
   for Local Sizing
  </a>
 </li>
 <li>
  <a href="#hide-autoplay-videos-that-arent-muted">
   Hide Autoplay Videos That Aren't Muted
  </a>
 </li>
 <li>
  <a href="#use-root-for-flexible-type">
   Use
   <code>
    :root
   </code>
   for Flexible Type
  </a>
 </li>
 <li>
  <a href="#set-font-size-on-form-elements-for-a-better-mobile-experience">
   Set
   <code>
    font-size
   </code>
   on Form Elements for a Better Mobile Experience
  </a>
 </li>
</ol>
<h3>
 Use
 <code>
  :not()
 </code>
 to Apply/Unapply Borders on Navigation
</h3>
<p>
 Instead of putting on the border...
</p>
<p>
 <code>
  css
/* add border */
.nav li {
  border-right: 1px solid #666;
}
 </code>
</p>
<p>
 ...and then taking it off the last element...
</p>
<p>
 <code>
  css
/* remove border */
.nav li:last-child {
  border-right: none;
}
 </code>
</p>
<p>
 ...use the
 <code>
  :not()
 </code>
 pseudo-class to only apply to the elements you want:
</p>
<p>
 <code>
  css
.nav li:not(:last-child) {
  border-right: 1px solid #666;
}
 </code>
</p>
<p>
 Sure, you can use
 <code>
  .nav li + li
 </code>
 or even
 <code>
  .nav li:first-child ~ li
 </code>
 , but with
 <code>
  :not()
 </code>
 the intent is very clear and the CSS selector defines the border the way a human would describe it.
</p>
<p>
 <a href="http://codepen.io/AllThingsSmitty/pen/LkymvO">
  <strong>
   Demo
  </strong>
 </a>
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Add
 <code>
  line-height
 </code>
 to
 <code>
  body
 </code>
</h3>
<p>
 You don't need to add
 <code>
  line-height
 </code>
 to each
 <code>
  <p>
 </code>
 ,
 <code>
  <h*>
 </code>
 ,
 <em>
  et al
 </em>
 . separately. Instead, add it to
 <code>
  body
 </code>
 :
</p>
<p>
 <code>
  css
body {
  line-height: 1.5;
}
 </code>
</p>
<p>
 This way textual elements can inherit from
 <code>
  body
 </code>
 easily.
</p>
<p>
 <a href="http://codepen.io/AllThingsSmitty/pen/VjbdYd">
  <strong>
   Demo
  </strong>
 </a>
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Vertically-Center Anything
</h3>
<p>
 No, it's not black magic, you really can center elements vertically:
</p>
<p>
 ```css
html, body {
  height: 100%;
  margin: 0;
}
</p>
<p>
 body {
  -webkit-align-items: center;
  -ms-flex-align: center;
  align-items: center;
  display: -webkit-flex;
  display: flex;
}
```
</p>
<p>
 Want to center something else? Vertically, horizontally...anything, anytime, anywhere? CSS-Tricks has
 <a href="https://css-tricks.com/centering-css-complete-guide/">
  a nice write-up
 </a>
 on doing all of that.
</p>
<p>
 <strong>
  Note:
 </strong>
 Watch for some
 <a href="https://github.com/philipwalton/flexbugs#3-min-height-on-a-flex-container-wont-apply-to-its-flex-items">
  buggy behavior
 </a>
 with flexbox in IE11.
</p>
<p>
 <a href="http://codepen.io/AllThingsSmitty/pen/GqmGqZ">
  <strong>
   Demo
  </strong>
 </a>
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Comma-Separated Lists
</h3>
<p>
 Make list items look like a real, comma-separated list:
</p>
<p>
 <code>
  css
ul > li:not(:last-child)::after {
  content: ",";
}
 </code>
</p>
<p>
 Use the
 <code>
  :not()
 </code>
 pseudo-class so no comma is added to the last item.
</p>
<p>
 <strong>
  Note:
 </strong>
 This tip may not be ideal for accessibility, specifically screen readers. And copy/paste from the browser doesn't work with CSS-generated content. Proceed with caution.
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Select Items Using Negative
 <code>
  nth-child
 </code>
</h3>
<p>
 Use negative
 <code>
  nth-child
 </code>
 in CSS to select items 1 through n.
</p>
<p>
 ```css
li {
  display: none;
}
</p>
<p>
 /* select items 1 through 3 and display them */
li:nth-child(-n+3) {
  display: block;
}
```
</p>
<p>
 Or, since you've already learned a little about
 <a href="#use-not-to-applyunapply-borders-on-navigation">
  using
  <code>
   :not()
  </code>
 </a>
 , try:
</p>
<p>
 <code>
  css
/* select items 1 through 3 and display them */
li:not(:nth-child(-n+3)) {
  display: none;
}
 </code>
</p>
<p>
 Well that was pretty easy.
</p>
<p>
 <a href="http://codepen.io/AllThingsSmitty/pen/WxjKZp">
  <strong>
   Demo
  </strong>
 </a>
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Use SVG for Icons
</h3>
<p>
 There's no reason not to use SVG for icons:
</p>
<p>
 <code>
  css
.logo {
  background: url("logo.svg");
}
 </code>
</p>
<p>
 SVG scales well for all resolution types and is supported in all browsers
 <a href="http://caniuse.com/#search=svg">
  back to IE9
 </a>
 . So ditch your .png, .jpg, or .gif-jif-whatev files.
</p>
<p>
 <strong>
  Note:
 </strong>
 If you have SVG icon-only buttons for sighted users and the SVG fails to load, this will help maintain accessibility:
</p>
<p>
 <code>
  css
.no-svg .icon-only:after {
  content: attr(aria-label);
}
 </code>
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Use the "Lobotomized Owl" Selector
</h3>
<p>
 It may have a strange name but using the universal selector (
 <code>
  *
 </code>
 ) with the adjacent sibling selector (
 <code>
  +
 </code>
 ) can provide a powerful CSS capability:
</p>
<p>
 <code>
  css
* + * {
  margin-top: 1.5em;
}
 </code>
</p>
<p>
 In this example, all elements in the flow of the document that follow other elements will receive
 <code>
  margin-top: 1.5em
 </code>
 .
</p>
<p>
 For more on the "lobotomized owl" selector, read
 <a href="http://alistapart.com/article/axiomatic-css-and-lobotomized-owls">
  Heydon Pickering's post
 </a>
 on
 <em>
  A List Apart
 </em>
 .
</p>
<p>
 <a href="http://codepen.io/AllThingsSmitty/pen/grRvWq">
  <strong>
   Demo
  </strong>
 </a>
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Use
 <code>
  max-height
 </code>
 for Pure CSS Sliders
</h3>
<p>
 Implement CSS-only sliders using
 <code>
  max-height
 </code>
 with overflow hidden:
</p>
<p>
 ```css
.slider {
  max-height: 200px;
  overflow-y: hidden;
  width: 300px;
}
</p>
<p>
 .slider:hover {
  max-height: 600px;
  overflow-y: scroll;
}
```
</p>
<p>
 The element expands to the
 <code>
  max-height
 </code>
 value on hover and the slider displays as a result of the overflow.
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Inherit
 <code>
  box-sizing
 </code>
</h3>
<p>
 Let
 <code>
  box-sizing
 </code>
 be inherited from
 <code>
  html
 </code>
 :
</p>
<p>
 ```css
html {
  box-sizing: border-box;
}
</p>
<p>
 *, *:before, *:after {
  box-sizing: inherit;
}
```
</p>
<p>
 This makes it easier to change
 <code>
  box-sizing
 </code>
 in plugins or other components that leverage other behavior.
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Equal-Width Table Cells
</h3>
<p>
 Tables can be a pain to work with so try using
 <code>
  table-layout: fixed
 </code>
 to keep cells at equal width:
</p>
<p>
 <code>
  css
.calendar {
  table-layout: fixed;
}
 </code>
</p>
<p>
 Pain-free table layouts.
</p>
<p>
 <a href="http://codepen.io/AllThingsSmitty/pen/jALALm">
  <strong>
   Demo
  </strong>
 </a>
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Get Rid of Margin Hacks With Flexbox
</h3>
<p>
 When working with column gutters you can get rid of
 <code>
  nth-
 </code>
 ,
 <code>
  first-
 </code>
 , and
 <code>
  last-child
 </code>
 hacks by using flexbox's
 <code>
  space-between
 </code>
 property:
</p>
<p>
 ```css
.list {
  display: flex;
  justify-content: space-between;
}
</p>
<p>
 .list .person {
  flex-basis: 23%;
}
```
</p>
<p>
 Now column gutters always appear evenly-spaced.
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Use Attribute Selectors with Empty Links
</h3>
<p>
 Display links when the
 <code>
  <a>
 </code>
 element has no text value but the
 <code>
  href
 </code>
 attribute has a link:
</p>
<p>
 <code>
  css
a[href^="http"]:empty::before {
  content: attr(href);
}
 </code>
</p>
<p>
 That's pretty convenient.
</p>
<p>
 <a href="http://codepen.io/AllThingsSmitty/pen/zBzXRx">
  <strong>
   Demo
  </strong>
 </a>
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Style "Default" Links
</h3>
<p>
 Add a style for "default" links:
</p>
<p>
 <code>
  css
a[href]:not([class]) {
  color: #008000;
  text-decoration: underline;
}
 </code>
</p>
<p>
 Now links that are inserted via a CMS, which don't usually have a
 <code>
  class
 </code>
 attribute, will have a distinction without generically affecting the cascade.
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Consistent Vertical Rhythm
</h3>
<p>
 Use a universal selector (
 <code>
  *
 </code>
 ) within an element to create a consistent vertical rhythm:
</p>
<p>
 <code>
  css
.intro > * {
  margin-bottom: 1.25rem;
}
 </code>
</p>
<p>
 Consistent vertical rhythm provides a visual aesthetic that makes content far more readable.
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Intrinsic Ratio Boxes
</h3>
<p>
 To create a box with an intrinsic ratio, all you need to do is apply top or bottom padding to a div:
</p>
<p>
 ```css
.container {
  height: 0;
  padding-bottom: 20%;
  position: relative;
}
</p>
<p>
 .container div {
  border: 2px dashed #ddd;
  height: 100%;
  left: 0;
  position: absolute;
  top: 0;
  width: 100%;
}
```
</p>
<p>
 Using 20% for padding makes the height of the box equal to 20% of its width. No matter the width of the viewport, the child div will keep its aspect ratio (100% / 20% = 5:1).
</p>
<p>
 <a href="http://codepen.io/AllThingsSmitty/pen/jALZvE">
  <strong>
   Demo
  </strong>
 </a>
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Style Broken Images
</h3>
<p>
 Make broken images more aesthetically-pleasing with a little bit of CSS:
</p>
<p>
 <code>
  css
img {
  display: block;
  font-family: Helvetica, Arial, sans-serif;
  font-weight: 300;
  height: auto;
  line-height: 2;
  position: relative;
  text-align: center;
  width: 100%;
}
 </code>
</p>
<p>
 Now add pseudo-elements rules to display a user message and URL reference of the broken image:
</p>
<p>
 ```css
img:before {
  content: "We're sorry, the image below is broken :(";
  display: block;
  margin-bottom: 10px;
}
</p>
<p>
 img:after {
  content: "(url: " attr(src) ")";
  display: block;
  font-size: 12px;
}
```
</p>
<p>
 Learn more about styling for this pattern in
 <a href="https://github.com/ireade/">
  Ire Aderinokun
 </a>
 's
 <a href="http://bitsofco.de/styling-broken-images/">
  original post
 </a>
 .
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Use
 <code>
  rem
 </code>
 for Global Sizing; Use
 <code>
  em
 </code>
 for Local Sizing
</h3>
<p>
 After setting the base font size at the root (
 <code>
  html { font-size: 16px; }
 </code>
 ), set the font size for textual elements to
 <code>
  em
 </code>
 :
</p>
<p>
 ```css
h2 {
  font-size: 2em;
}
</p>
<p>
 p {
  font-size: 1em;
}
```
</p>
<p>
 Then set the font-size for modules to
 <code>
  rem
 </code>
 :
</p>
<p>
 ```css
article {
  font-size: 1.25rem;
}
</p>
<p>
 aside .module {
  font-size: .9rem;
}
```
</p>
<p>
 Now each module becomes compartmentalized and easier to style, more maintainable, and flexible.
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Hide Autoplay Videos That Aren't Muted
</h3>
<p>
 This is a great trick for a custom user stylesheet. Avoid overloading a user with sound from a video that autoplays when the page is loaded. If the sound isn't muted, don't show the video:
</p>
<p>
 <code>
  css
video[autoplay]:not([muted]) {
  display: none;
}
 </code>
</p>
<p>
 Once again, we're taking advantage of using the
 <a href="#use-not-to-applyunapply-borders-on-navigation">
  <code>
   :not()
  </code>
 </a>
 pseudo-class.
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Use
 <code>
  :root
 </code>
 for Flexible Type
</h3>
<p>
 The type font size in a responsive layout should be able to adjust with each viewport. You can calculate the font size based on the viewport height and width using
 <code>
  :root
 </code>
 :
</p>
<p>
 <code>
  css
:root {
  font-size: calc(1vw + 1vh + .5vmin);
}
 </code>
</p>
<p>
 Now you can utilize the
 <code>
  root em
 </code>
 unit based on the value calculated by
 <code>
  :root
 </code>
 :
</p>
<p>
 <code>
  css
body {
  font: 1em/1.6 sans-serif;
}
 </code>
</p>
<p>
 <a href="http://codepen.io/AllThingsSmitty/pen/XKgOkR">
  <strong>
   Demo
  </strong>
 </a>
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Set
 <code>
  font-size
 </code>
 on Form Elements for a Better Mobile Experience
</h3>
<p>
 To avoid mobile browsers (iOS Safari,
 <em>
  et al
 </em>
 .) from zooming in on HTML form elements when a
 <code>
  <select>
 </code>
 drop-down is tapped, add
 <code>
  font-size
 </code>
 to the selector rule:
</p>
<p>
 <code>
  css
input[type="text"],
input[type="number"],
select,
textarea {
  font-size: 16px;
}
 </code>
</p>
<p>
 :dancer:
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h2>
 Support
</h2>
<p>
 Current versions of Chrome, Firefox, Safari, Opera, Edge, and IE11.
</p>
<h2>
 Translations
</h2>
<ul>
 <li>
  <a href="https://github.com/AllThingsSmitty/css-protips/tree/master/translations/es-ES">
   Español
  </a>
 </li>
 <li>
  <a href="https://github.com/AllThingsSmitty/css-protips/tree/master/translations/fr-FR">
   Français
  </a>
 </li>
 <li>
  <a href="https://github.com/AllThingsSmitty/css-protips/tree/master/translations/it-IT">
   Italiano
  </a>
 </li>
 <li>
  <a href="https://github.com/AllThingsSmitty/css-protips/tree/master/translations/ja-JP">
   日本語
  </a>
 </li>
 <li>
  <a href="https://github.com/AllThingsSmitty/css-protips/tree/master/translations/pt-BR">
   Português do Brasil
  </a>
 </li>
 <li>
  <a href="https://github.com/AllThingsSmitty/css-protips/tree/master/translations/ru-RU">
   Русский
  </a>
 </li>
 <li>
  <a href="https://github.com/AllThingsSmitty/css-protips/tree/master/translations/zh-CN">
   简体中文
  </a>
 </li>
</ul>
