<p>
 <img alt="header" src="https://raw.githubusercontent.com/loverajoel/jstips/master/resources/jstips-header-blog.gif"/>
</p>
<h1>
 Introducing JavaScript Tips
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<blockquote>
 <p>
  New year, new project.
  <strong>
   A JS tip per day!
  </strong>
 </p>
</blockquote>
<p>
 With great excitement, I introduce these short and useful daily JavaScript tips that will allow you to improve your code writing. With less than 2 minutes each day, you will be able to read about performance, conventions, hacks, interview questions and all the items that the future of this awesome language holds for us.
</p>
<p>
 At midday, no matter if it is a weekend or a holiday, a tip will be posted and tweeted.
</p>
<h3>
 Can you help us enrich it?
</h3>
<p>
 Please feel free to send us a PR with your own JavaScript tip to be published here.
Any improvements or suggestions are more than welcome!
 <a href="https://github.com/loverajoel/jstips/blob/master/CONTRIBUTING.md">
  Click to see the instructions
 </a>
</p>
<h3>
 Let’s keep in touch
</h3>
<p>
 To get updates, watch the repo and follow the
 <a href="https://twitter.com/tips_js">
  Twitter account
 </a>
 . Only one tweet will be sent per day. It is a deal!
</p>
<blockquote>
 <p>
  Don't forget to Star the repo, as this will help to promote the project!
 </p>
</blockquote>
<h3>
 Other language
</h3>
<p>
 <a href="https://github.com/loverajoel/jstips/blob/master/README-zh_CN.md">
  简体中文(simplified Chinese)
 </a>
</p>
<h1>
 Tips list
</h1>
<h2>
 #23 - Converting to number fast way
</h2>
<blockquote>
 <p>
  2016-01-23 by
  <a href="http://twitter.com/sonnyt">
   @sonnyt
  </a>
 </p>
</blockquote>
<p>
 Converting strings to numbers is extremely common. The easiest and fastest (
 <a href="https://jsperf.com/number-vs-parseint-vs-plus/29">
  jsPref
 </a>
 ) way to achieve that would be using the
 <code>
  +
 </code>
 (plus) operator.
</p>
<p>
 ```javascript
var one = '1';
</p>
<p>
 var numberOne = +one; // Number 1
```
</p>
<p>
 You can also use the
 <code>
  -
 </code>
 (minus) operator which type-converts the value into number but also negates it.
</p>
<p>
 ```javascript
var one = '1';
</p>
<p>
 var negativeNumberOne = -one; // Number -1
```
</p>
<h2>
 #22 - Empty an Array
</h2>
<blockquote>
 <p>
  2016-01-22 by
  <a href="https://github.com/microlv">
   microlv
  </a>
 </p>
</blockquote>
<p>
 You define an array and want to empty its contents.
Usually, you would do it like this:
</p>
<p>
 <code>
  javascript
// define Array
var list = [1, 2, 3, 4];
function empty() {
    //empty your array
    list = [];
}
empty();
 </code>
 But there is another way to empty an array that is more performant.
</p>
<p>
 You should use code like this:
 <code>
  javascript
var list = [1, 2, 3, 4];
function empty() {
    //empty your array
    list.length = 0;
}
empty();
 </code>
 *
 <code>
  list = []
 </code>
 assigns a reference to a new array to a variable, while any other references are unaffected.
which means that references to the contents of the previous array are still kept in memory, leading to memory leaks.
</p>
<ul>
 <li>
  <code>
   list.length = 0
  </code>
  deletes everything in the array, which does hit other references.
 </li>
</ul>
<p>
 However, if you have a copy of the array (A and Copy-A), if you delete its contents using
 <code>
  list.length = 0
 </code>
 , the copy will also lose its contents.
</p>
<p>
 Think about what will output:
```js
var foo = [1,2,3];
var bar = [1,2,3];
var foo2 = foo;
var bar2 = bar;
foo = [];
bar.length = 0;
console.log(foo, bar, foo2, bar2);
</p>
<p>
 //[] [] [1, 2, 3] []
```
Stackoverflow more detail:
 <a href="http://stackoverflow.com/questions/4804235/difference-between-array-length-0-and-array">
  difference-between-array-length-0-and-array
 </a>
</p>
<h2>
 #21 - Shuffle an Array
</h2>
<blockquote>
 <p>
  2016-01-21 by
  <a href="https://github.com/0xmtn/">
   @0xmtn
  </a>
 </p>
</blockquote>
<p>
 This snippet here uses
 <a href="https://www.wikiwand.com/en/Fisher%E2%80%93Yates_shuffle">
  Fisher-Yates Shuffling
 </a>
 Algorithm to shuffle a given array.
</p>
<p>
 <code>
  javascript
function shuffle(arr) {
    var i,
        j,
        temp;
    for (i = arr.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1));
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    return arr;    
};
 </code>
 An example:
</p>
<p>
 <code>
  javascript
var a = [1, 2, 3, 4, 5, 6, 7, 8];
var b = shuffle(a);
console.log(b);
// [2, 7, 8, 6, 5, 3, 1, 4]
 </code>
</p>
<h2>
 #20 - Return objects to enable chaining of functions
</h2>
<blockquote>
 <p>
  2016-01-20 by
  <a href="https://twitter.com/WakeStudio">
   @WakeskaterX
  </a>
 </p>
</blockquote>
<p>
 When creating functions on an object in Object Oriented Javascript, returning the object in the function will enable you to chain functions together.
</p>
<p>
 ```js
function Person(name) {
  this.name = name;
</p>
<p>
 this.sayName = function() {
    console.log("Hello my name is: ", this.name);
    return this;
  };
</p>
<p>
 this.changeName = function(name) {
    this.name = name;
    return this;
  };
}
</p>
<p>
 var person = new Person("John");
person.sayName().changeName("Timmy").sayName();
```
</p>
<h2>
 #19 - Safe string concatenation
</h2>
<blockquote>
 <p>
  2016-01-19 by
  <a href="https://twitter.com/gogainda">
   @gogainda
  </a>
 </p>
</blockquote>
<p>
 Suppose you have a couple of variables with unknown types and you want to concatenate them in a string. To be sure that the arithmetical operation is not be applied during concatenation, use
 <code>
  concat
 </code>
 :
</p>
<p>
 ```javascript
var one = 1;
var two = 2;
var three = '3';
</p>
<p>
 var result = ''.concat(one, two, three); //"123"
```
</p>
<p>
 This way of concatenting does exactly what you'd expect. In contrast, concatenation with pluses might lead to unexpected results:
```javascript
var one = 1;
var two = 2;
var three = '3';
</p>
<p>
 var result = one + two + three; //"33" instead of "123"
```
</p>
<p>
 Speaking about performance, compared to the
 <code>
  join
 </code>
 <a href="http://www.sitepoint.com/javascript-fast-string-concatenation/">
  type
 </a>
 of concatenation, the speed of
 <code>
  concat
 </code>
 is pretty much the same.
</p>
<p>
 You can read more about the
 <code>
  concat
 </code>
 function on MDN
 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/concat">
  page
 </a>
 .
</p>
<h2>
 #18 - Rounding the fast way
</h2>
<blockquote>
 <p>
  2016-01-18 by
  <a href="https://github.com/pklinger">
   pklinger
  </a>
 </p>
</blockquote>
<p>
 Today's tip is about performance.
 <a href="http://stackoverflow.com/questions/5971645/what-is-the-double-tilde-operator-in-javascript">
  Ever came across the double tilde
 </a>
 <code>
  ~~
 </code>
 operator? It is sometimes also called the double NOT bitwise operator. You can use it as a faster substitute for
 <code>
  Math.floor()
 </code>
 . Why is that?
</p>
<p>
 One bitwise shift
 <code>
  ~
 </code>
 transforms the 32 bit converted input into
 <code>
  -(input+1)
 </code>
 . The double bitwise shift therefore transforms the input into
 <code>
  -(-(input + 1)+1)
 </code>
 making it a great tool to round towards 0. For numeric input, it therefore mimics the
 <code>
  Math.ceil()
 </code>
 for negative and
 <code>
  Math.floor()
 </code>
 for positive input. On failure,
 <code>
  0
 </code>
 is returned, which might come in handy sometimes instead of
 <code>
  Math.floor()
 </code>
 , which returns a value of
 <code>
  NaN
 </code>
 on failure.
</p>
<p>
 ```javascript
// single ~
console.log(~1337)    // -1338
</p>
<p>
 // numeric input
console.log(~~47.11)  // -> 47
console.log(~~-12.88) // -> -12
console.log(~~1.9999) // -> 1
console.log(~~3)      // -> 3
</p>
<p>
 // on failure
console.log(~~[]) // -> 0
console.log(~~NaN)  // -> 0
console.log(~~null) // -> 0
</p>
<p>
 // greater than 32 bit integer fails
console.log(~~(2147483647 + 1) === (2147483647 + 1)) // -> 0
```
</p>
<p>
 Although
 <code>
  ~~
 </code>
 may perform better, for the sake of readability please use
 <code>
  Math.floor()
 </code>
 .
</p>
<h2>
 #17 - Node.js: Run a module if it is not "required"
</h2>
<blockquote>
 <p>
  2016-01-17 by
  <a href="https://twitter.com/odsdq">
   @odsdq
  </a>
 </p>
</blockquote>
<p>
 In node, you can tell your program to do two different things depending on whether the code is run from
 <code>
  require('./something.js')
 </code>
 or
 <code>
  node something.js
 </code>
 .  This is useful if you want to interact with one of your modules independently.
</p>
<p>
 <code>
  js
if (!module.parent) {
    // ran with `node something.js`
    app.listen(8088, function() {
        console.log('app listening on port 8088');
    })
} else {
    // used with `require('/.something.js')`
    module.exports = app;
}
 </code>
</p>
<p>
 See
 <a href="https://nodejs.org/api/modules.html#modules_module_parent">
  the documentation for modules
 </a>
 for more info.
</p>
<h2>
 #16 - Passing arguments to callback functions
</h2>
<blockquote>
 <p>
  2016-01-16 by
  <a href="https://twitter.com/minhazav">
   @minhazav
  </a>
 </p>
</blockquote>
<p>
 By default you cannot pass arguments to a callback function. For example:
```js
function callback() {
  console.log('Hi human');
}
</p>
<p>
 document.getElementById('someelem').addEventListener('click', callback);
 <code>
  You can take advantage of the closure scope in Javascript to pass arguments to callback functions. Check this example:
 </code>
 js
function callback(a, b) {
  return function() {
    console.log('sum = ', (a+b));
  }
}
</p>
<p>
 var x = 1, y = 2;
document.getElementById('someelem').addEventListener('click', callback(x, y));
```
</p>
<p>
 <strong>
  What are closures?
 </strong>
 Closures are functions that refer to independent (free) variables. In other words, the function defined in the closure 'remembers' the environment in which it was created.
 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures">
  Check MDN Documentation
 </a>
 to learn more.
</p>
<p>
 So this way the arguments
 <code>
  x
 </code>
 and
 <code>
  y
 </code>
 are in scope of the callback function when it is called.
</p>
<p>
 Another method to do this is using the
 <code>
  bind
 </code>
 method. For example:
```js
var alertText = function(text) {
  alert(text);
};
</p>
<p>
 document.getElementById('someelem').addEventListener('click', alertText.bind(this, 'hello'));
```
There is a very slight difference in performance of both methods, checkout
 <a href="http://jsperf.com/bind-vs-closure-23">
  jsperf
 </a>
 .
</p>
<h2>
 #15 - Even simpler way of using indexOf as a contains clause
</h2>
<blockquote>
 <p>
  2016-01-15 by
  <a href="https://twitter.com/jhogoforbroke">
   @jhogoforbroke
  </a>
 </p>
</blockquote>
<p>
 JavaScript by default does not have a contains method. And for checking existence of a substring in a string or an item in an array you may do this:
</p>
<p>
 ```javascript
var someText = 'javascript rules';
if (someText.indexOf('javascript') !== -1) {
}
</p>
<p>
 // or
if (someText.indexOf('javascript') >= 0) {
}
```
</p>
<p>
 But let's look at these
 <a href="https://github.com/strongloop/express">
  Expressjs
 </a>
 code snippets.
</p>
<p>
 <a href="https://github.com/strongloop/express/blob/2f8ac6726fa20ab5b4a05c112c886752868ac8ce/examples/mvc/lib/boot.js#L26">
  examples/mvc/lib/boot.js
 </a>
 <code>
  javascript
for (var key in obj) {
  // "reserved" exports
  if (~['name', 'prefix', 'engine', 'before'].indexOf(key)) continue;
 </code>
</p>
<p>
 <a href="https://github.com/strongloop/express/blob/2f8ac6726fa20ab5b4a05c112c886752868ac8ce/lib/utils.js#L93">
  lib/utils.js
 </a>
 <code>
  javascript
exports.normalizeType = function(type){
  return ~type.indexOf('/')
    ? acceptParams(type)
    : { value: mime.lookup(type), params: {} };
};
 </code>
</p>
<p>
 <a href="https://github.com/strongloop/express/blob/2f8ac6726fa20ab5b4a05c112c886752868ac8ce/examples/web-service/index.js#L35">
  examples/web-service/index.js
 </a>
 <code>
  javascript
// key is invalid
if (!~apiKeys.indexOf(key)) return next(error(401, 'invalid api key'));
 </code>
</p>
<p>
 The gotcha is the
 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_Operators">
  bitwise operator
 </a>
 <strong>
  ~
 </strong>
 , "Bitwise operators perform their operations on binary representations, but they return standard JavaScript numerical values."
</p>
<p>
 It transforms
 <code>
  -1
 </code>
 into
 <code>
  0
 </code>
 , and
 <code>
  0
 </code>
 evaluates to
 <code>
  false
 </code>
 in JavaScript:
</p>
<p>
 <code>
  javascript
var someText = 'text';
!!~someText.indexOf('tex'); // someText contains "tex" - true
!~someText.indexOf('tex'); // someText NOT contains "tex" - false
~someText.indexOf('asd'); // someText doesn't contain "asd" - false
~someText.indexOf('ext'); // someText contains "ext" - true
 </code>
</p>
<h3>
 String.prototype.includes()
</h3>
<p>
 ES6 introduced the
 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/includes">
  includes() method
 </a>
 and you can use it to determine whether or not a string includes another string:
</p>
<p>
 <code>
  javascript
'something'.includes('thing'); // true
 </code>
</p>
<p>
 With ECMAScript 2016 (ES7) it is even possible to use these techniques with Arrays:
</p>
<p>
 <code>
  javascript
!!~[1, 2, 3].indexOf(1); // true
[1, 2, 3].includes(1); // true
 </code>
</p>
<p>
 <strong>
  Unfortunately, it is only supported in Chrome, Firefox, Safari 9 or above and Edge; not IE11 or lower.
 </strong>
 <strong>
  It's better used in controlled environments.
 </strong>
</p>
<h2>
 #14 - Fat Arrow Functions #ES6
</h2>
<blockquote>
 <p>
  2016-01-13 by
  <a href="https://github.com/pklinger/">
   @pklinger
  </a>
 </p>
</blockquote>
<p>
 Introduced as a new feature in ES6, fat arrow functions may come as a handy tool to write more code in fewer lines. The name comes from its syntax,
 <code>
  =>
 </code>
 , which is a 'fat arrow', as compared to a thin arrow
 <code>
  ->
 </code>
 . Some programmers might already know this type of function from different languages such as Haskell, as 'lambda expressions', or as 'anonymous functions'. It is called anonymous, as these arrow functions do not have a descriptive function name.
</p>
<h3>
 What are the benefits?
</h3>
<ul>
 <li>
  Syntax: fewer LOC; no more typing
  <code>
   function
  </code>
  keyword over and over again
 </li>
 <li>
  Semantics: capturing the keyword
  <code>
   this
  </code>
  from the surrounding context
 </li>
</ul>
<h3>
 Simple syntax example
</h3>
<p>
 Have a look at these two code snippets, which do the exact same job, and you will quickly understand what fat arrow functions do:
</p>
<p>
 ```javascript
// general syntax for fat arrow functions
param => expression
</p>
<p>
 // may also be written with parentheses
// parentheses are required on multiple params
(param1 [, param2]) => expression
</p>
<p>
 // using functions
var arr = [5,3,2,9,1];
var arrFunc = arr.map(function(x) {
  return x * x;
});
console.log(arr)
</p>
<p>
 // using fat arrow
var arr = [5,3,2,9,1];
var arrFunc = arr.map((x) => x*x);
console.log(arr)
```
</p>
<p>
 As you can see, the fat arrow function in this case can save you time typing out the parentheses as well as the function and return keywords. I would advise you to always write parentheses around the parameter inputs, as the parentheses will be needed for multiple input parameters, such as in
 <code>
  (x,y) => x+y
 </code>
 . It is just a way to cope with forgetting them in different use cases. But the code above would also work like this:
 <code>
  x => x*x
 </code>
 . So far, these are only syntactical improvements, which lead to fewer LOC and better readability.
</p>
<h3>
 Lexically binding
 <code>
  this
 </code>
</h3>
<p>
 There is another good reason to use fat arrow functions. There is the issue with the context of
 <code>
  this
 </code>
 . With arrow functions, you don't need to worry about
 <code>
  .bind(this)
 </code>
 or setting
 <code>
  that = this
 </code>
 anymore, as fat arrow functions pick the context of
 <code>
  this
 </code>
 from the lexical surrounding. Have a look at the next
 <a href="https://jsfiddle.net/pklinger/rw94oc11/">
  example
 </a>
 :
</p>
<p>
 ```javascript
</p>
<p>
 // globally defined this.i
this.i = 100;
</p>
<p>
 var counterA = new CounterA();
var counterB = new CounterB();
var counterC = new CounterC();
var counterD = new CounterD();
</p>
<p>
 // bad example
function CounterA() {
  // CounterA's
 <code>
  this
 </code>
 instance (!! gets ignored here)
  this.i = 0;
  setInterval(function () {
    //
 <code>
  this
 </code>
 refers to global object, not to CounterA's
 <code>
  this
 </code>
 // therefore starts counting with 100, not with 0 (local this.i)
    this.i++;
    document.getElementById("counterA").innerHTML = this.i;
  }, 500);
}
</p>
<p>
 // manually binding that = this
function CounterB() {
  this.i = 0;
  var that = this;
  setInterval(function() {
    that.i++;
    document.getElementById("counterB").innerHTML = that.i;
  }, 500);
}
</p>
<p>
 // using .bind(this)
function CounterC() {
  this.i = 0;
  setInterval(function() {
    this.i++;
    document.getElementById("counterC").innerHTML = this.i;
  }.bind(this), 500);
}
</p>
<p>
 // fat arrow function
function CounterD() {
  this.i = 0;
  setInterval(() => {
    this.i++;
    document.getElementById("counterD").innerHTML = this.i;
  }, 500);
}
```
</p>
<p>
 Further information about fat arrow functions may be found at
 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions">
  MDN
 </a>
 . To see different syntax options visit
 <a href="http://jsrocks.org/2014/10/arrow-functions-and-their-scope/">
  this site
 </a>
 .
</p>
<h2>
 #13 - Tip to measure performance of a javascript block
</h2>
<blockquote>
 <p>
  2016-01-13 by
  <a href="https://twitter.com/manmadareddy">
   @manmadareddy
  </a>
 </p>
</blockquote>
<p>
 For quickly measuring performance of a javascript block, we can use the console functions like
 <a href="https://developer.chrome.com/devtools/docs/console-api#consoletimelabel">
  <code>
   console.time(label)
  </code>
 </a>
 and
 <a href="https://developer.chrome.com/devtools/docs/console-api#consoletimeendlabel">
  <code>
   console.timeEnd(label)
  </code>
 </a>
</p>
<p>
 ```javascript
console.time("Array initialize");
var arr = new Array(100),
    len = arr.length,
    i;
</p>
<p>
 for (i = 0; i < len; i++) {
    arr[i] = new Object();
};
console.timeEnd("Array initialize"); // Outputs: Array initialize: 0.711ms
```
</p>
<p>
 More info:
 <a href="https://github.com/DeveloperToolsWG/console-object">
  Console object
 </a>
 ,
 <a href="https://mathiasbynens.be/notes/javascript-benchmarking">
  Javascript benchmarking
 </a>
</p>
<p>
 Demo:
 <a href="https://jsfiddle.net/meottb62/">
  jsfiddle
 </a>
 -
 <a href="http://codepen.io/anon/pen/JGJPoa">
  codepen
 </a>
 (outputs in browser console)
</p>
<h2>
 #12 - Pseudomandatory parameters in ES6 functions #ES6
</h2>
<blockquote>
 <p>
  2016-01-12 by
  <a href="https://github.com/AvraamMavridis">
   Avraam Mavridis
  </a>
 </p>
</blockquote>
<p>
 In many programming languages the parameters of a function are by default mandatory and the developer has to explicitly define that a parameter is optional. In Javascript, every parameter is optional, but we can enforce this behavior without messing with the actual body of a function, taking advantage of
 <a href="http://exploringjs.com/es6/ch_parameter-handling.html#sec_parameter-default-values">
  <strong>
   es6's default values for parameters
  </strong>
 </a>
 feature.
</p>
<p>
 ```javascript
const _err = function( message ){
  throw new Error( message );
}
</p>
<p>
 const getSum = (a = _err('a is not defined'), b = _err('b is not defined')) => a + b
</p>
<p>
 getSum( 10 ) // throws Error, b is not defined
getSum( undefined, 10 ) // throws Error, a is not defined
 ```
</p>
<p>
 <code>
  _err
 </code>
 is a function that immediately throws an Error. If no value is passed for one of the parameters, the default value is going to be used,
 <code>
  _err
 </code>
 will be called and an Error will be thrown. You can see more examples for the
 <strong>
  default parameters feature
 </strong>
 on
 <a href="https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Functions/default_parameters">
  Mozilla's Developer Network
 </a>
</p>
<h2>
 #11 - Hoisting
</h2>
<blockquote>
 <p>
  2016-01-11 by
  <a href="https://twitter.com/squizzleflip">
   @squizzleflip
  </a>
 </p>
</blockquote>
<p>
 Understanding
 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var#var_hoisting">
  hoisting
 </a>
 will help you organize your function scope. Just remember, variable declarations and function definitions are hoisted to the top. Variable definitions are not, even if you declare and define a variable on the same line. Also, a variable
 <strong>
  declaration
 </strong>
 lets the system know that the variable exists while
 <strong>
  definition
 </strong>
 assigns it a value.
</p>
<p>
 ```javascript
function doTheThing() {
  // ReferenceError: notDeclared is not defined
  console.log(notDeclared);
</p>
<p>
 // Outputs: undefined
  console.log(definedLater);
  var definedLater;
</p>
<p>
 definedLater = 'I am defined!'
  // Outputs: 'I am defined!'
  console.log(definedLater)
</p>
<p>
 // Outputs: undefined
  console.log(definedSimulateneously);
  var definedSimulateneously = 'I am defined!'
  // Outputs: 'I am defined!'
  console.log(definedSimulateneously)
</p>
<p>
 // Outputs: 'I did it!'
  doSomethingElse();
</p>
<p>
 function doSomethingElse(){
    console.log('I did it!');
  }
</p>
<p>
 // TypeError: undefined is not a function
  functionVar();
</p>
<p>
 var functionVar = function(){
    console.log('I did it!');
  }
}
```
</p>
<p>
 To make things easier to read, declare all of your variables at the top of your function scope so it is clear which scope the variables are coming from. Define your variables before you need to use them. Define your functions at the bottom of your scope to keep them out of your way.
</p>
<h2>
 #10 - Check if a property is in a Object
</h2>
<blockquote>
 <p>
  2016-01-10 by
  <a href="https://www.twitter.com/loverajoel">
   @loverajoel
  </a>
 </p>
</blockquote>
<p>
 When you have to check if a property is present in an
 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects">
  object
 </a>
 , you probably are doing something like this:
</p>
<p>
 ```javascript
var myObject = {
  name: '@tips_js'
};
</p>
<p>
 if (myObject.name) { ... }
</p>
<p>
 ```
</p>
<p>
 That's ok, but you have to know that there are two native ways for this kind of thing, the
 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in">
  <code>
   in
  </code>
  operator
 </a>
 and
 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwnProperty">
  <code>
   Object.hasOwnProperty
  </code>
 </a>
 . Every object descended from
 <code>
  Object
 </code>
 , has both ways available.
</p>
<h3>
 See the big Difference
</h3>
<p>
 ```javascript
var myObject = {
  name: '@tips_js'
};
</p>
<p>
 myObject.hasOwnProperty('name'); // true
'name' in myObject; // true
</p>
<p>
 myObject.hasOwnProperty('valueOf'); // false, valueOf is inherited from the prototype chain
'valueOf' in myObject; // true
</p>
<p>
 ```
</p>
<p>
 Both differ in the depth at which they check the properties. In other words,
 <code>
  hasOwnProperty
 </code>
 will only return true if key is available on that object directly. However, the
 <code>
  in
 </code>
 operator doesn't discriminate between properties created on an object and properties inherited from the prototype chain.
</p>
<p>
 Here's another example:
</p>
<p>
 ```javascript
var myFunc = function() {
  this.name = '@tips_js';
};
myFunc.prototype.age = '10 days';
</p>
<p>
 var user = new myFunc();
</p>
<p>
 user.hasOwnProperty('name'); // true
user.hasOwnProperty('age'); // false, because age is from the prototype chain
```
</p>
<p>
 Check the
 <a href="https://jsbin.com/tecoqa/edit?js,console">
  live examples here
 </a>
 !
</p>
<p>
 I also recommend reading
 <a href="https://github.com/loverajoel/jstips/issues/62">
  this discussion
 </a>
 about common mistakes made when checking a property's existence in objects.
</p>
<h2>
 #09 - Template Strings
</h2>
<blockquote>
 <p>
  2016-01-09 by
  <a href="https://github.com/JakeRawr">
   @JakeRawr
  </a>
 </p>
</blockquote>
<p>
 As of ES6, JS now has template strings as an alternative to the classic end quotes strings.
</p>
<p>
 Ex:
Normal string
 <code>
  javascript
var firstName = 'Jake';
var lastName = 'Rawr';
console.log('My name is ' + firstName + ' ' + lastName);
// My name is Jake Rawr
 </code>
 Template String
 <code>
  javascript
var firstName = 'Jake';
var lastName = 'Rawr';
console.log(`My name is ${firstName} ${lastName}`);
// My name is Jake Rawr
 </code>
</p>
<p>
 You can do multi-line strings without
 <code>
  \n
 </code>
 and simple logic (ie 2+3) inside
 <code>
  ${}
 </code>
 in template strings.
</p>
<p>
 You are also able to to modify the output of template strings using a function; they are called [tagged template strings]
(https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/template
 <em>
  strings#Tagged
 </em>
 template_strings) for example usages of tagged template strings.
</p>
<p>
 You may also want to
 <a href="https://hacks.mozilla.org/2015/05/es6-in-depth-template-strings-2">
  read
 </a>
 to understand template strings more.
</p>
<h2>
 #08 - Converting a Node List to an Array
</h2>
<blockquote>
 <p>
  2016-01-08 by
  <a href="https://twitter.com/tevko">
   @Tevko
  </a>
 </p>
</blockquote>
<p>
 The
 <code>
  querySelectorAll
 </code>
 method returns an array-like object called a node list. These data structures are referred to as "Array-like", because they appear as an array, but can not be used with array methods like
 <code>
  map
 </code>
 and
 <code>
  forEach
 </code>
 . Here's a quick, safe, and reusable way to convert a node list into an array of DOM elements:
</p>
<p>
 ```javascript
const nodelist = document.querySelectorAll('div');
const nodelistToArray = Array.apply(null, nodelist);
</p>
<p>
 //later on ..
</p>
<p>
 nodelistToArray.forEach(...);
nodelistToArray.map(...);
nodelistToArray.slice(...);
</p>
<p>
 //etc...
```
</p>
<p>
 The
 <code>
  apply
 </code>
 method is used to pass an array of arguments to a function with a given
 <code>
  this
 </code>
 value.
 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/apply">
  MDN
 </a>
 states that
 <code>
  apply
 </code>
 will take an array-like object, which is exactly what
 <code>
  querySelectorAll
 </code>
 returns. Since we don't need to specify a value for
 <code>
  this
 </code>
 in the context of the function, we pass in
 <code>
  null
 </code>
 or
 <code>
  0
 </code>
 . The result is an actual array of DOM elements which contains all of the available array methods.
</p>
<p>
 Or if you are using ES2015 you can use the
 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_operator">
  spread operator
  <code>
   ...
  </code>
 </a>
</p>
<p>
 ```js
const nodelist = [...document.querySelectorAll('div')]; // returns a real array
</p>
<p>
 //later on ..
</p>
<p>
 nodelist.forEach(...);
nodelist.map(...);
nodelist.slice(...);
</p>
<p>
 //etc...
```
</p>
<h2>
 #07 - "use strict" and get lazy
</h2>
<blockquote>
 <p>
  2016-01-07 by
  <a href="https://twitter.com/nat5an">
   @nainslie
  </a>
 </p>
</blockquote>
<p>
 Strict-mode JavaScript makes it easier for the developer to write "secure" JavaScript.
</p>
<p>
 By default, JavaScript allows the programmer to be pretty careless, for example, by not requiring us to declare our variables with "var" when we first introduce them.  While this may seem like a convenience to the unseasoned developer, it's also the source of many errors when a variable name is misspelled or accidentally referred to out of its scope.
</p>
<p>
 Programmers like to make the computer do the boring stuff for us, and automatically check our work for mistakes. That's what the JavaScript "use strict" directive allows us to do, by turning our mistakes into JavaScript errors.
</p>
<p>
 We add this directive either by adding it at the top of a js file:
</p>
<p>
 <code>
  javascript
// Whole-script strict mode syntax
"use strict";
var v = "Hi!  I'm a strict mode script!";
 </code>
</p>
<p>
 or inside a function:
</p>
<p>
 <code>
  javascript
function f()
{
  // Function-level strict mode syntax
  'use strict';
  function nested() { return "And so am I!"; }
  return "Hi!  I'm a strict mode function!  " + nested();
}
function f2() { return "I'm not strict."; }
 </code>
</p>
<p>
 By including this directive in a JavaScript file or function, we will direct the JavaScript engine to execute in strict mode which disables a bunch of behaviors that are usually undesirable in larger JavaScript projects.  Among other things, strict mode changes the following behaviors:
* Variables can only be introduced when they are preceded with "var"
* Attempting to write to read-only properties generates a noisy error
* You have to call constructors with the "new" keyword
* "this" is not implicitly bound to the global object
* Very limited use of eval() allowed
* Protects you from using reserved words or future reserved words as variable names
</p>
<p>
 Strict mode is great for new projects, but can be challenging to introduce into older projects that don't already use it in most places.  It also can be problematic if your build chain concatenates all your js files into one big file, as this may cause all files to execute in strict mode.
</p>
<p>
 It is not a statement, but a literal expression, ignored by earlier versions of JavaScript.
Strict mode is supported in:
* Internet Explorer from version 10.
* Firefox from version 4.
* Chrome from version 13.
* Safari from version 5.1.
* Opera from version 12.
</p>
<p>
 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode">
  See MDN for a fuller description of strict mode
 </a>
 .
</p>
<h2>
 #06 - Writing a single method for arrays and a single element
</h2>
<blockquote>
 <p>
  2016-01-06 by
  <a href="https://twitter.com/mattfxyz">
   @mattfxyz
  </a>
 </p>
</blockquote>
<p>
 Rather than writing separate methods to handle an array and a single element parameter, write your functions so they can handle both. This is similar to how some of jQuery's functions work (
 <code>
  css
 </code>
 will modify everything matched by the selector).
</p>
<p>
 You just have to concat everything into an array first.
 <code>
  Array.concat
 </code>
 will accept an array or a single element.
</p>
<p>
 <code>
  javascript
function printUpperCase(words) {
  var elements = [].concat(words);
  for (var i = 0; i < elements.length; i++) {
    console.log(elements[i].toUpperCase());
  }
}
 </code>
</p>
<p>
 <code>
  printUpperCase
 </code>
 is now ready to accept a single node or an array of nodes as its parameter.
</p>
<p>
 <code>
  javascript
printUpperCase("cactus");
// => CACTUS
printUpperCase(["cactus", "bear", "potato"]);
// => CACTUS
//  BEAR
//  POTATO
 </code>
</p>
<h2>
 #05 - Differences between
 <code>
  undefined
 </code>
 and
 <code>
  null
 </code>
</h2>
<blockquote>
 <p>
  2016-01-05 by
  <a href="https://twitter.com/loverajoel">
   @loverajoel
  </a>
 </p>
</blockquote>
<ul>
 <li>
  <code>
   undefined
  </code>
  means a variable has not been declared, or has been declared but has not yet been assigned a value
 </li>
 <li>
  <code>
   null
  </code>
  is an assignment value that means "no value"
 </li>
 <li>
  Javascript sets unassigned variables with a default value of
  <code>
   undefined
  </code>
 </li>
 <li>
  Javascript never sets a value to
  <code>
   null
  </code>
  . It is used by programmers to indicate that a
  <code>
   var
  </code>
  has no value.
 </li>
 <li>
  <code>
   undefined
  </code>
  is not valid in JSON while
  <code>
   null
  </code>
  is
 </li>
 <li>
  <code>
   undefined
  </code>
  typeof is
  <code>
   undefined
  </code>
 </li>
 <li>
  <code>
   null
  </code>
  typeof is an
  <code>
   object
  </code>
  .
  <a href="http://www.2ality.com/2013/10/typeof-null.html">
   Why?
  </a>
 </li>
 <li>
  Both are primitives
 </li>
 <li>
  Both are
  <a href="https://developer.mozilla.org/en-US/docs/Glossary/Falsy">
   falsy
  </a>
  (
  <code>
   Boolean(undefined) // false
  </code>
  ,
  <code>
   Boolean(null) // false
  </code>
  )
 </li>
 <li>
  <p>
   You can know if a variable is
   <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined">
    undefined
   </a>
  </p>
  <p>
   <code>
    javascript
typeof variable === "undefined"
   </code>
  </p>
 </li>
 <li>
  <p>
   You can check if a variable is
   <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null">
    null
   </a>
  </p>
  <p>
   <code>
    javascript
variable === null
   </code>
  </p>
 </li>
 <li>
  <p>
   The
   <strong>
    equality
   </strong>
   operator considers them equal, but the
   <strong>
    identity
   </strong>
   doesn't
  </p>
  <p>
   ```javascript
null == undefined // true
  </p>
  <p>
   null === undefined // false
```
  </p>
 </li>
</ul>
<h2>
 #04 - Sorting strings with accented characters
</h2>
<blockquote>
 <p>
  2016-01-04 by
  <a href="https://twitter.com/loverajoel">
   @loverajoel
  </a>
 </p>
</blockquote>
<p>
 Javascript has a native method
 <strong>
  <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort">
   sort
  </a>
 </strong>
 that allows sorting arrays. Doing a simple
 <code>
  array.sort()
 </code>
 will treat each array entry as a string and sort it alphabetically. Also you can provide your
 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#Parameters">
  own custom sorting
 </a>
 function.
</p>
<p>
 <code>
  javascript
['Shanghai', 'New York', 'Mumbai', 'Buenos Aires'].sort();
// ["Buenos Aires", "Mumbai", "New York", "Shanghai"]
 </code>
</p>
<p>
 But when you try order an array of non ASCII characters like this
 <code>
  ['é', 'a', 'ú', 'c']
 </code>
 , you will obtain a strange result
 <code>
  ['c', 'e', 'á', 'ú']
 </code>
 . That happens because sort works only with the English language.
</p>
<p>
 See the next example:
</p>
<p>
 ```javascript
// Spanish
['único','árbol', 'cosas', 'fútbol'].sort();
// ["cosas", "fútbol", "árbol", "único"] // bad order
</p>
<p>
 // German
['Woche', 'wöchentlich', 'wäre', 'Wann'].sort();
// ["Wann", "Woche", "wäre", "wöchentlich"] // bad order
```
</p>
<p>
 Fortunately, there are two ways to overcome this behavior
 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare">
  localeCompare
 </a>
 and
 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Collator">
  Intl.Collator
 </a>
 provided by ECMAScript Internationalization API.
</p>
<blockquote>
 <p>
  Both methods have their own custom parameters in order to configure it to work adequately.
 </p>
</blockquote>
<h3>
 Using
 <code>
  localeCompare()
 </code>
</h3>
<p>
 ```javascript
['único','árbol', 'cosas', 'fútbol'].sort(function (a, b) {
  return a.localeCompare(b);
});
// ["árbol", "cosas", "fútbol", "único"]
</p>
<p>
 ['Woche', 'wöchentlich', 'wäre', 'Wann'].sort(function (a, b) {
  return a.localeCompare(b);
});
// ["Wann", "wäre", "Woche", "wöchentlich"]
```
</p>
<h3>
 Using
 <code>
  Intl.Collator()
 </code>
</h3>
<p>
 ```javascript
['único','árbol', 'cosas', 'fútbol'].sort(Intl.Collator().compare);
// ["árbol", "cosas", "fútbol", "único"]
</p>
<p>
 ['Woche', 'wöchentlich', 'wäre', 'Wann'].sort(Intl.Collator().compare);
// ["Wann", "wäre", "Woche", "wöchentlich"]
```
</p>
<ul>
 <li>
  For each method you can customize the location.
 </li>
 <li>
  According to
  <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare#Performance">
   Firefox
  </a>
  Intl.Collator is faster when comparing large numbers of strings.
 </li>
</ul>
<p>
 So when you are working with arrays of strings in a language other than English, remember to use this method to avoid unexpected sorting.
</p>
<h2>
 #03 - Improve Nested Conditionals
</h2>
<blockquote>
 <p>
  2016-01-03 by
  <a href="https://github.com/AlbertoFuente">
   AlbertoFuente
  </a>
 </p>
</blockquote>
<p>
 How can we improve and make a more efficient nested
 <code>
  if
 </code>
 statement in javascript?
</p>
<p>
 <code>
  javascript
if (color) {
  if (color === 'black') {
    printBlackBackground();
  } else if (color === 'red') {
    printRedBackground();
  } else if (color === 'blue') {
    printBlueBackground();
  } else if (color === 'green') {
    printGreenBackground();
  } else {
    printYellowBackground();
  }
}
 </code>
</p>
<p>
 One way to improve the nested
 <code>
  if
 </code>
 statement would be using the
 <code>
  switch
 </code>
 statement. Although it is less verbose and is more ordered, it's not recommended to use it because it's so difficult to debug errors. Here's
 <a href="https://toddmotto.com/deprecating-the-switch-statement-for-object-literals/">
  why
 </a>
 .
</p>
<p>
 <code>
  javascript
switch(color) {
  case 'black':
    printBlackBackground();
    break;
  case 'red':
    printRedBackground();
    break;
  case 'blue':
    printBlueBackground();
    break;
  case 'green':
    printGreenBackground();
    break;
  default:
    printYellowBackground();
}
 </code>
</p>
<p>
 But what if we have a conditional with several checks in each statement? In this case, if we want it less verbose and more ordered, we can use the conditional
 <code>
  switch
 </code>
 .
If we pass
 <code>
  true
 </code>
 as a parameter to the
 <code>
  switch
 </code>
 statement, it allows us to put a conditional in each case.
</p>
<p>
 <code>
  javascript
switch(true) {
  case (typeof color === 'string' && color === 'black'):
    printBlackBackground();
    break;
  case (typeof color === 'string' && color === 'red'):
    printRedBackground();
    break;
  case (typeof color === 'string' && color === 'blue'):
    printBlueBackground();
    break;
  case (typeof color === 'string' && color === 'green'):
    printGreenBackground();
    break;
  case (typeof color === 'string' && color === 'yellow'):
    printYellowBackground();
    break;
}
 </code>
</p>
<p>
 But we must always avoid having several checks in every condition and avoid using
 <code>
  switch
 </code>
 as much as possible. We also must take into account that the most efficient way to do this is through an
 <code>
  object
 </code>
 .
</p>
<p>
 ```javascript
var colorObj = {
  'black': printBlackBackground,
  'red': printRedBackground,
  'blue': printBlueBackground,
  'green': printGreenBackground,
  'yellow': printYellowBackground
};
</p>
<p>
 if (color in colorObj) {
  colorObj
 <a href="">
  color
 </a>
 ;
}
```
</p>
<p>
 Here you can find more information about
 <a href="http://www.nicoespeon.com/en/2015/01/oop-revisited-switch-in-js/">
  this
 </a>
 .
</p>
<h2>
 #02 - ReactJs - Keys in children components are important
</h2>
<blockquote>
 <p>
  2016-01-02  by
  <a href="https://twitter.com/loverajoel">
   @loverajoel
  </a>
 </p>
</blockquote>
<p>
 The
 <a href="https://facebook.github.io/react/docs/multiple-components.html#dynamic-children">
  key
 </a>
 is an attribute that you must pass to all components created dynamically from an array. It's a unique and constant id that React uses to identify each component in the DOM and to know whether it's a different component or the same one. Using keys ensures that the child component is preserved and not recreated and prevents weird things from happening.
</p>
<blockquote>
 <p>
  Key is not really about performance, it's more about identity (which in turn leads to better performance). Randomly assigned and changing values do not form an identity
  <a href="https://github.com/facebook/react/issues/1342#issuecomment-39230939">
   Paul O’Shannessy
  </a>
 </p>
</blockquote>
<ul>
 <li>
  Use an existing unique value of the object.
 </li>
 <li>
  <p>
   Define the keys in the parent components, not in child components
  </p>
  <p>
   ```javascript
//bad
...
render() {
   <div key="{{item.key}}>{{item.name}}</div">
    }
...
   </div>
  </p>
  <p>
   //good
   <mycomponent key="{{item.key}}/">
    ```
   </mycomponent>
  </p>
 </li>
 <li>
  <a href="https://medium.com/@robinpokorny/index-as-a-key-is-an-anti-pattern-e0349aece318#.76co046o9">
   Using array index is a bad practice.
  </a>
 </li>
 <li>
  <p>
   <code>
    random()
   </code>
   will not work
  </p>
  <p>
   <code>
    javascript
//bad
    <mycomponent key="{{Math.random()}}/">
    </mycomponent>
   </code>
  </p>
 </li>
 <li>
  <p>
   You can create your own unique id. Be sure that the method is fast and attach it to your object.
  </p>
 </li>
 <li>
  When the number of children is large or contains expensive components, use keys to improve performance.
 </li>
 <li>
  <a href="http://docs.reactjs-china.com/react/docs/animation.html">
   You must provide the key attribute for all children of ReactCSSTransitionGroup.
  </a>
 </li>
</ul>
<h2>
 #1 - AngularJs:
 <code>
  $digest
 </code>
 vs
 <code>
  $apply
 </code>
</h2>
<blockquote>
 <p>
  2016-01-01  by
  <a href="https://twitter.com/loverajoel">
   @loverajoel
  </a>
 </p>
</blockquote>
<p>
 One of the most appreciated features of AngularJs is the two-way data binding. In order to make this work AngularJs evaluates the changes between the model and the view through cycles(
 <code>
  $digest
 </code>
 ). You need to understand this concept in order to understand how the framework works under the hood.
</p>
<p>
 Angular evaluates each watcher whenever one event is fired. This is the known
 <code>
  $digest
 </code>
 cycle.
Sometimes you have to force it to run a new cycle manually and you must choose the correct option because this phase is one of the most influential in terms of performance.
</p>
<h3>
 <code>
  $apply
 </code>
</h3>
<p>
 This core method lets you to start the digestion cycle explicitly. That means that all watchers are checked; the entire application starts the
 <code>
  $digest loop
 </code>
 . Internally, after executing an optional function parameter, it calls
 <code>
  $rootScope.$digest();
 </code>
 .
</p>
<h3>
 <code>
  $digest
 </code>
</h3>
<p>
 In this case the
 <code>
  $digest
 </code>
 method starts the
 <code>
  $digest
 </code>
 cycle for the current scope and its children. You should notice that the parent's scopes will not be checked.
 and not be affected.
</p>
<h3>
 Recommendations
</h3>
<ul>
 <li>
  Use
  <code>
   $apply
  </code>
  or
  <code>
   $digest
  </code>
  only when browser DOM events have triggered outside of AngularJS.
 </li>
 <li>
  <p>
   Pass a function expression to
   <code>
    $apply
   </code>
   , this has an error handling mechanism and allows integrating changes in the digest cycle.
  </p>
  <p>
   <code>
    javascript
$scope.$apply(() => {
    $scope.tip = 'Javascript Tip';
});
   </code>
  </p>
 </li>
 <li>
  <p>
   If you only need to update the current scope or its children, use
   <code>
    $digest
   </code>
   , and prevent a new digest cycle for the whole application. The performance benefit is self-evident.
  </p>
 </li>
 <li>
  <code>
   $apply()
  </code>
  is a hard process for the machine and can lead to performance issues when there is a lot of binding.
 </li>
 <li>
  If you are using >AngularJS 1.2.X, use
  <code>
   $evalAsync
  </code>
  , which is a core method that will evaluate the expression during the current cycle or the next. This can improve your application's performance.
 </li>
</ul>
<h2>
 #0 - Insert item inside an Array
</h2>
<blockquote>
 <p>
  2015-12-29
 </p>
</blockquote>
<p>
 Inserting an item into an existing array is a daily common task. You can add elements to the end of an array using push, to the beginning using unshift, or to the middle using splice.
</p>
<p>
 Those are known methods, but it doesn't mean there isn't a more performant way. Here we go:
</p>
<p>
 Adding an element at the end of the array is easy with push(), but there is a more performant way.
</p>
<p>
 ```javascript
var arr = [1,2,3,4,5];
</p>
<p>
 arr.push(6);
arr[arr.length] = 6; // 43% faster in Chrome 47.0.2526.106 on Mac OS X 10.11.1
```
Both methods modify the original array. Don't believe me? Check the
 <a href="http://jsperf.com/push-item-inside-an-array">
  jsperf
 </a>
</p>
<p>
 Now if we are trying to add an item to the beginning of the array:
</p>
<p>
 ```javascript
var arr = [1,2,3,4,5];
</p>
<p>
 arr.unshift(0);
[0].concat(arr); // 98% faster in Chrome 47.0.2526.106 on Mac OS X 10.11.1
```
Here is a little more detail: unshift edits the original array; concat returns a new array.
 <a href="http://jsperf.com/unshift-item-inside-an-array">
  jsperf
 </a>
</p>
<p>
 Adding items in the middle of an array is easy with splice, and it's the most performant way to do it.
</p>
<p>
 <code>
  javascript
var items = ['one', 'two', 'three', 'four'];
items.splice(items.length / 2, 0, 'hello');
 </code>
</p>
<p>
 I tried to run these tests in various Browsers and OS and the results were similar. I hope these tips will be useful for you and encourage to perform your own tests!
</p>
<h3>
 License
</h3>
<p>
 <a href="http://creativecommons.org/publicdomain/zero/1.0/">
  <img alt="CC0" src="http://i.creativecommons.org/p/zero/1.0/88x31.png"/>
 </a>
</p>
