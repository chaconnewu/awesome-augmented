<h1>
 jQuery Tips Everyone Should Know
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<p>
 A collection of simple tips to help up your jQuery game.
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
  <a href="#tips">
   Tips
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
 Tips
</h2>
<ol>
 <li>
  <a href="#checking-if-jquery-loaded">
   Checking If jQuery Loaded
  </a>
 </li>
 <li>
  <a href="#back-to-top-button">
   Back to Top Button
  </a>
 </li>
 <li>
  <a href="#preload-images">
   Preload Images
  </a>
 </li>
 <li>
  <a href="#checking-if-images-are-loaded">
   Checking If Images Are Loaded
  </a>
 </li>
 <li>
  <a href="#fix-broken-images-automatically">
   Fix Broken Images Automatically
  </a>
 </li>
 <li>
  <a href="#toggle-classes-on-hover">
   Toggle Classes on Hover
  </a>
 </li>
 <li>
  <a href="#disabling-input-fields">
   Disabling Input Fields
  </a>
 </li>
 <li>
  <a href="#stop-the-loading-of-links">
   Stop the Loading of Links
  </a>
 </li>
 <li>
  <a href="#cache-jquery-selectors">
   Cache jQuery Selectors
  </a>
 </li>
 <li>
  <a href="#toggle-fadeslide">
   Toggle Fade/Slide
  </a>
 </li>
 <li>
  <a href="#simple-accordion">
   Simple Accordion
  </a>
 </li>
 <li>
  <a href="#make-two-divs-the-same-height">
   Make Two Divs the Same Height
  </a>
 </li>
 <li>
  <a href="#open-external-links-in-new-tabwindow">
   Open External Links in New Tab/Window
  </a>
 </li>
 <li>
  <a href="#find-element-by-text">
   Find Element By Text
  </a>
 </li>
 <li>
  <a href="#trigger-on-visibility-change">
   Trigger on Visibility Change
  </a>
 </li>
 <li>
  <a href="#ajax-call-error-handling">
   Ajax Call Error Handling
  </a>
 </li>
 <li>
  <a href="#chain-plugin-calls">
   Chain Plugin Calls
  </a>
 </li>
 <li>
  <a href="#sort-list-items-alphabetically">
   Sort List Items Alphabetically
  </a>
 </li>
</ol>
<h3>
 Checking If jQuery Loaded
</h3>
<p>
 Before you can do anything with jQuery you first need to make certain it has loaded:
</p>
<p>
 <code>
  javascript
if (typeof jQuery == 'undefined') {
  console.log('jQuery hasn\'t loaded');
} else {
  console.log('jQuery has loaded');
}
 </code>
</p>
<p>
 Now you're off...
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Back to Top Button
</h3>
<p>
 By using the
 <code>
  animate
 </code>
 and
 <code>
  scrollTop
 </code>
 methods in jQuery you don't need a plugin to create a simple scroll-to-top animation:
</p>
<p>
 <code>
  javascript
// Back to top
$('.top').click(function (e) {
  e.preventDefault();
  $('html, body').animate({scrollTop: 0}, 800);
});
 </code>
</p>
<p>
 <code>
  html
<!-- Create an anchor tag -->
<a class="top" href="#">Back to top</a>
 </code>
</p>
<p>
 Changing the
 <code>
  scrollTop
 </code>
 value changes where you wants the scrollbar to land. All you're really doing is animating the body of the document throughout the course of 800 milliseconds until it scrolls to the top of the document.
</p>
<p>
 <strong>
  Note:
 </strong>
 Watch for some
 <a href="https://github.com/jquery/api.jquery.com/issues/417">
  buggy behavior
 </a>
 with
 <code>
  scrollTop
 </code>
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
 Preload Images
</h3>
<p>
 If your web page uses a lot of images that aren't visible initially (e.g., on hover) it makes sense to preload them:
</p>
<p>
 ```javascript
$.preloadImages = function () {
  for (var i = 0; i < arguments.length; i++) {
    $('
 <img>
  ').attr('src', arguments[i]);
  }
};
 </img>
</p>
<p>
 $.preloadImages('img/hover-on.png', 'img/hover-off.png');
```
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Checking If Images Are Loaded
</h3>
<p>
 Sometimes you might need to check if your images have fully loaded in order to continue on with your scripts:
</p>
<p>
 <code>
  javascript
$('img').load(function () {
  console.log('image load successful');
});
 </code>
</p>
<p>
 You can also check if one particular image has loaded by replacing the
 <code>
  <img>
 </code>
 tag with an ID or class.
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Fix Broken Images Automatically
</h3>
<p>
 If you happen to find broken image links on your site replacing them one by one can be a pain. This simple piece of code can save a lot of headaches:
</p>
<p>
 <code>
  javascript
$('img').on('error', function () {
  if(!$(this).hasClass('broken-image')) {
    $(this).prop('src', 'img/broken.png').addClass('broken-image');
  }
});
 </code>
</p>
<p>
 Even if you don't have any broken links, adding this won't do any harm.
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Toggle Classes on Hover
</h3>
<p>
 Let's say you want to change the visual of a clickable element on your page when a user hovers over it. You can add a class to your element when the user is hovering; when the user stops hovering removes the class:
</p>
<p>
 <code>
  javascript
$('.btn').hover(function () {
  $(this).addClass('hover');
}, function () {
  $(this).removeClass('hover');
});
 </code>
</p>
<p>
 You just need to add the necessary CSS. If you want an even
 <em>
  simpler
 </em>
 way use the
 <code>
  toggleClass
 </code>
 method:
</p>
<p>
 <code>
  javascript
$('.btn').hover(function () {
  $(this).toggleClass('hover');
});
 </code>
</p>
<p>
 <strong>
  Note:
 </strong>
 CSS may be a faster solution in this case but it's still worthwhile to know this.
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Disabling Input Fields
</h3>
<p>
 At times you may want the submit button of a form or one of its text inputs to be disabled until the user has performed a certain action (e.g., checking the "I've read the terms" checkbox). Add the
 <code>
  disabled
 </code>
 attribute to your input so you can enable it when you want:
</p>
<p>
 <code>
  javascript
$('input[type="submit"]').prop('disabled', true);
 </code>
</p>
<p>
 All you need to do is run the
 <code>
  prop
 </code>
 method again on the input, but set the value of
 <code>
  disabled
 </code>
 to
 <code>
  false
 </code>
 :
</p>
<p>
 <code>
  javascript
$('input[type="submit"]').prop('disabled', false);
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
 Stop the Loading of Links
</h3>
<p>
 Sometimes you don't want links to go to a certain web page nor reload the page; you might want them to do something else like trigger some other script. This will do the trick of preventing the default action:
</p>
<p>
 <code>
  javascript
$('a.no-link').click(function (e) {
  e.preventDefault();
});
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
 Cache jQuery Selectors
</h3>
<p>
 Think of how many times you write the same selector over and over again in any project. Every
 <code>
  $('.element')
 </code>
 selector has to search the entire DOM each time, regardless if that selector had previously run. Instead, run the selector once and store the results in a variable:
</p>
<p>
 <code>
  javascript
var blocks = $('#blocks').find('li');
 </code>
</p>
<p>
 Now you can use the
 <code>
  blocks
 </code>
 variable wherever you want without having to search the DOM every time:
</p>
<p>
 ```javascript
$('#hideBlocks').click(function () {
  blocks.fadeOut();
});
</p>
<p>
 $('#showBlocks').click(function () {
  blocks.fadeIn();
});
```
</p>
<p>
 Caching jQuery selectors are an easy performance gain.
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Toggle Fade/Slide
</h3>
<p>
 Sliding and fading are something we use plenty in our animations with jQuery. You might just want to show an element when a user clicks something, which makes the
 <code>
  fadeIn
 </code>
 and
 <code>
  slideDown
 </code>
 methods perfect. But if you want that element to appear on the first click and then disappear on the second this will work just fine:
</p>
<p>
 ```javascript
// Fade
$('.btn').click(function () {
  $('.element').fadeToggle('slow');
});
</p>
<p>
 // Toggle
$('.btn').click(function () {
  $('.element').slideToggle('slow');
});
```
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Simple Accordion
</h3>
<p>
 This is a simple method for a quick accordion:
</p>
<p>
 ```javascript
// Close all panels
$('#accordion').find('.content').hide();
</p>
<p>
 // Accordion
$('#accordion').find('.accordion-header').click(function () {
  var next = $(this).next();
  next.slideToggle('fast');
  $('.content').not(next).slideUp('fast');
  return false;
});
```
</p>
<p>
 By adding this script all you really needs to do on your web page is the necessary HTML go get this working.
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Make Two Divs the Same Height
</h3>
<p>
 Sometimes you'll want two divs to have the same height no matter what content they have in them:
</p>
<p>
 <code>
  javascript
$('.div').css('min-height', $('.main-div').height());
 </code>
</p>
<p>
 This example sets the
 <code>
  min-height
 </code>
 which means that it can be bigger than the main div but never smaller. However, a more flexible method would be to loop over a set of elements and set the height to the height of the tallest element:
</p>
<p>
 <code>
  javascript
var $columns = $('.column');
var height = 0;
$columns.each(function () {
  if ($(this).height() > height) {
    height = $(this).height();
  }
});
$columns.height(height);
 </code>
</p>
<p>
 If you want
 <em>
  all
 </em>
 columns to have the same height:
</p>
<p>
 <code>
  javascript
var $rows = $('.same-height-columns');
$rows.each(function () {
  $(this).find('.column').height($(this).height());
});
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
 Open External Links in New Tab/Window
</h3>
<p>
 Open external links in a new browser tab or window and ensure links on the same origin open in the same tab or window:
</p>
<p>
 <code>
  javascript
$('a[href^="http"]').attr('target', '_blank');
$('a[href^="//"]').attr('target', '_blank');
$('a[href^="' + window.location.origin + '"]').attr('target', '_self');
 </code>
</p>
<p>
 <strong>
  Note:
 </strong>
 <code>
  window.location.origin
 </code>
 doesn't work in IE10.
 <a href="http://tosbourn.com/a-fix-for-window-location-origin-in-internet-explorer/">
  This fix
 </a>
 takes care of the issue.
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Find Element By Text
</h3>
<p>
 By using the
 <code>
  contains()
 </code>
 selector in jQuery you can find text in content of an element. If text doesn't exists, that element will be hidden:
</p>
<p>
 <code>
  javascript
var search = $('#search').val();
$('div:not(:contains("' + search + '"))').hide();
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
 Trigger on Visibility Change
</h3>
<p>
 Trigger JavaScript when the user is no longer focusing on a tab, or refocuses on a tab:
</p>
<p>
 <code>
  javascript
$(document).on('visibilitychange', function (e) {
  if (e.target.visibilityState === 'visible') {
    console.log('Tab is now in view!');
  } else if (e.target.visibilityState === 'hidden') {
    console.log('Tab is now hidden!');
  }
});
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
 Ajax Call Error Handling
</h3>
<p>
 When an Ajax call returns a 404 or 500 error the error handler will be executed. If the handler isn't defined, other jQuery code might not work anymore. Define a global Ajax error handler:
</p>
<p>
 <code>
  javascript
$(document).ajaxError(function (e, xhr, settings, error) {
  console.log(error);
});
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
 Chain Plugin Calls
</h3>
<p>
 jQuery allows for the "chaining" of plugin method calls to mitigate the process of repeatedly querying the DOM and creating multiple jQuery objects. Let's say the following snippet represents your plugin method calls:
</p>
<p>
 <code>
  javascript
$('#elem').show();
$('#elem').html('bla');
$('#elem').otherStuff();
 </code>
</p>
<p>
 This could be vastly improved by using chaining:
</p>
<p>
 <code>
  javascript
$('#elem')
  .show()
  .html('bla')
  .otherStuff();
 </code>
</p>
<p>
 An alternative is to cache the element in a variable (prefixed with
 <code>
  $
 </code>
 ):
</p>
<p>
 <code>
  javascript
var $elem = $('#elem');
$elem.hide();
$elem.html('bla');
$elem.otherStuff();
 </code>
</p>
<p>
 Both chaining and
 <a href="#cache-jquery-selectors">
  caching
 </a>
 methods in jQuery are best practices that lead to shorter and faster code.
</p>
<p>
 <sup>
  <a href="#table-of-contents">
   back to table of contents
  </a>
 </sup>
</p>
<h3>
 Sort List Items Alphabetically
</h3>
<p>
 Let's say you end up with too many items in a list. Maybe the content is produced by a CMS and you want to order them alphabetically:
</p>
<p>
 ```javascript
var ul = $('#list'),
lis = $('li', ul).get();
</p>
<p>
 lis.sort(function (a, b) {
  return ($(a).text().toUpperCase() < $(b).text().toUpperCase()) ? -1 : 1;
});
</p>
<p>
 ul.append(lis);
```
</p>
<p>
 There you go!
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
  <a href="https://github.com/AllThingsSmitty/jquery-tips-everyone-should-know/tree/master/translations/es-ES">
   Español
  </a>
 </li>
 <li>
  <a href="https://github.com/AllThingsSmitty/jquery-tips-everyone-should-know/tree/master/translations/fr-FR">
   Français
  </a>
 </li>
 <li>
  <a href="https://github.com/AllThingsSmitty/jquery-tips-everyone-should-know/tree/master/translations/ru-RU">
   русский
  </a>
 </li>
 <li>
  <a href="https://github.com/AllThingsSmitty/jquery-tips-everyone-should-know/tree/master/translations/zh-CN">
   简体中文
  </a>
 </li>
</ul>
