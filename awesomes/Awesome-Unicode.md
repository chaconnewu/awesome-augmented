<p>
 <img alt="" src="https://raw.githubusercontent.com/jagracey/Awesome-Unicode/58f28d08aef7f36eb6cdca22d25e7654cd8de5ae/resources/banner.jpg"/>
</p>
<h1>
 Awesome Unicode
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<blockquote>
 <p>
  A curated list of delightful Unicode tidbits, packages and resources.
 </p>
</blockquote>
<p>
 <em>
  Please read the
  <a href="CONTRIBUTING.md">
   contribution guidelines
  </a>
  before contributing.
 </em>
 <em>
  Key Unicode terminology is defined in the
  <a href="GLOSSARY.md">
   glossary
  </a>
  .
 </em>
</p>
<p>
 <br>
  <br/>
 </br>
</p>
<h1>
 Foreword
</h1>
<p>
 Unicode is Awesome! Prior to Unicode, international communication was grueling- everyone had defined their seperate extended character set in the upperhalf of ASCII (called Code Pages) that would conflict- Just think, German speakers coordinating with Korean speakers over which 127 character Code Page to use. Thankfully the Unicode standard caught on and unified communication. Unicode 8.0 standardizes over 120,000 characters from over 129 scripts - some modern, some ancient, and some still undeciphered. Unicode handles left-to-right and right-to-left text, combining marks, and includes diverse cultural, political, religious characters and emojis. Unicode is awesomely human - and ultimately underappreciated.
</p>
<p>
 <br/>
</p>
<h1>
 Contents
</h1>
<ul>
 <li>
  <a href="#quick-unicode-background">
   Quick Unicode Background
  </a>
  <ul>
   <li>
    <a href="#what-characters-does-the-unicode-standard-include">
     What Characters Does the Unicode Standard Include?
    </a>
   </li>
   <li>
    <a href="#unicode-character-encodings">
     Unicode Character Encodings
    </a>
   </li>
   <li>
    <a href="#lets-talk-numbers">
     Lets talk Numbers
    </a>
   </li>
   <li>
    <a href="#utf-16-surrogate-pairs">
     UTF-16 Surrogate Pairs
    </a>
   </li>
   <li>
    <a href="#calculating-surrogate-pairs">
     Calculating Surrogate Pairs
    </a>
   </li>
   <li>
    <a href="#composing--decomposing">
     Composing & Decomposing
    </a>
   </li>
   <li>
    <a href="#myths-of-unicode">
     Myths of Unicode
    </a>
   </li>
   <li>
    <a href="#applied-unicode-encodings">
     Applied Unicode Encodings
    </a>
   </li>
   <li>
    <a href="#source-code">
     Source Code
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#awesome-characters-list">
   Awesome Characters List
  </a>
  <ul>
   <li>
    <a href="#special-characters">
     Special Characters
    </a>
   </li>
   <li>
    <a href="#variable-identifiers-can-effectively-include-whitespace">
     Variable identifiers can effectively include whitespace!
    </a>
   </li>
   <li>
    <a href="#modifiers">
     Modifiers
    </a>
   </li>
   <li>
    <a href="#collision-uppercase-transformation-collisions">
     Uppercase Transformation Collisions
    </a>
   </li>
   <li>
    <a href="#collision-lowercase-transformation-collisions">
     Lowercase Transformation Collisions
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#quirks-and-troubleshooting">
   Quirks and Troubleshooting
  </a>
  <ul>
   <li>
    <a href="#one-to-many-case-mappings">
     One-To-Many Case Mappings
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#awesome-packages--libraries">
   Awesome Packages & Libraries
  </a>
 </li>
 <li>
  <a href="#emojis">
   Emojis
  </a>
  <ul>
   <li>
    <a href="#diversity">
     Diversity
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#creatively-naming-variables-and-methods">
   Creatively Naming Variables and Methods
  </a>
  <ul>
   <li>
    <a href="#recursive-html-tag-renaming-script">
     Recursive HTML Tag Renaming Script
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#unicode-fonts">
   Unicode Fonts
  </a>
 </li>
 <li>
  <a href="#more-reading">
   More Reading
  </a>
 </li>
 <li>
  <a href="#exploring-deeper-into-unicode-yourself">
   Exploring Deeper into Unicode Yourself
  </a>
 </li>
 <li>
  <a href="#overview-map">
   Overview Map
  </a>
  <ul>
   <li>
    <a href="#a-map-of-the-basic-multilingual-plane">
     A map of the Basic Multilingual Plane
    </a>
   </li>
   <li>
    <a href="#unicode-blocks">
     Unicode Blocks
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#principles-of-the-unicode-standard">
   Principles of the Unicode Standard
  </a>
 </li>
 <li>
  <a href="#unicode-versions">
   Unicode Versions
  </a>
 </li>
 <li>
  <a href="#contributing">
   Contributing
  </a>
 </li>
 <li>
  <a href="#code-of-conduct">
   Code of Conduct
  </a>
 </li>
 <li>
  <a href="#license">
   License
  </a>
 </li>
</ul>
<h1>
 Quick Unicode Background
</h1>
<h2>
 What Characters Does the Unicode Standard Include?
</h2>
<p>
 The Unicode Standard defines codes for characters used in all the major languages written today. Scripts include the European alphabetic scripts, Middle Eastern right-to-left scripts, and many scripts of Asia.
</p>
<p>
 The Unicode Standard further includes punctuation marks, diacritics, mathematical symbols, technical symbols, arrows, dingbats, emoji, etc. It provides codes for diacritics, which are modifying character marks such as the tilde (~), that are used in conjunction with base characters to represent accented letters (ñ, for example). In all, the Unicode Standard, Version 9.0 provides codes for 128,172 characters from the world's alphabets, ideograph sets, and symbol collections.
</p>
<p>
 The majority of common-use characters fit into the first 64K code points, an area of the codespace that is called the basic multilingual plane, or BMP for short. There are sixteen other supplementary planes available for encoding other characters, with currently over 850,000 unused code points. More characters are under consideration for addition to future versions of the standard.
</p>
<p>
 The Unicode Standard also reserves code points for private use. Vendors or end users can assign these internally for their own characters and symbols, or use them with specialized fonts. There are 6,400 private use code points on the BMP and another 131,068 supplementary private use code points, should 6,400 be insufficient for particular applications.
</p>
<h2>
 Unicode Character Encodings
</h2>
<p>
 Character encoding standards define not only the identity of each character and its numeric value, or code point, but also how this value is represented in bits.
</p>
<p>
 The Unicode Standard defines three encoding forms that allow the same data to be transmitted in a byte, word or double word oriented format (i.e. in 8, 16 or 32-bits per code unit). All three encoding forms encode the same common character repertoire and can be efficiently transformed into one another without loss of data. The Unicode Consortium fully endorses the use of any of these encoding forms as a conformant way of implementing the Unicode Standard.
</p>
<p>
 UTF-8 is popular for HTML and similar protocols. UTF-8 is a way of transforming all Unicode characters into a variable length encoding of bytes. It has the advantages that the Unicode characters corresponding to the familiar ASCII set have the same byte values as ASCII, and that Unicode characters transformed into UTF-8 can be used with much existing software without extensive software rewrites.
</p>
<p>
 UTF-16 is popular in many environments that need to balance efficient access to characters with economical use of storage. It is reasonably compact and all the heavily used characters fit into a single 16-bit code unit, while all other characters are accessible via pairs of 16-bit code units.
</p>
<p>
 UTF-32 is useful where memory space is no concern, but fixed width, single code unit access to characters is desired. Each Unicode character is  encoded in a single 32-bit code unit when using UTF-32.
</p>
<p>
 All three encoding forms need at most 4 bytes (or 32-bits) of data for each character.
</p>
<h2>
 Lets talk Numbers
</h2>
<p>
 The Unicode characterset is divided into 17 core segments called "planes", which are further divided into blocks. Each plane has space for 65,536 (2¹⁶) codepoints, supporting a grand total of 1,114,112 codepoints. There are two "Private Use Area" planes (#16 & #17) that are allocated to be used however one wishes. These two Private Use planes account for 131,072 codepoints.
</p>
<p>
 | #  | Name                                    | Range                  |
|-----|-----------------------------------------|------------------------|
| 1.  |
 <strong>
  Basic Multilingual Plane
 </strong>
 | (U+0000 to U+FFFF)     |
| 2.  |
 <strong>
  Supplementary Multilingual Plane
 </strong>
 | (U+10000 to U+1FFFF)   |
| 3.  |
 <strong>
  Supplementary Ideographic Plane
 </strong>
 | (U+20000 to U+2FFFF)   |
| 4.  | Tertiary Ideographic Plane              | (U+30000 to U+3FFFF)   |
| 5.  | Plane 5 (unassigned)                    | (U+40000 to U+4FFFF)   |
| 6.  | Plane 6 (unassigned)                    | (U+50000 to U+5FFFF)   |
| 7.  | Plane 7 (unassigned)                    | (U+60000 to U+6FFFF)   |
| 8.  | Plane 8 (unassigned)                    | (U+70000 to U+7FFFF)   |
| 9.  | Plane 9 (unassigned)                    | (U+80000 to U+8FFFF)   |
| 10. | Plane 10 (unassigned)                   | (U+90000 to U+9FFFF)   |
| 11. | Plane 11 (unassigned)                   | (U+A0000 to U+AFFFF)   |
| 12. | Plane 12 (unassigned)                   | (U+B0000 to U+BFFFF)   |
| 13. | Plane 13 (unassigned)                   | (U+C0000 to U+CFFFF)   |
| 14. | Plane 14 (unassigned)                   | (U+D0000 to U+DFFFF)   |
| 15. |
 <strong>
  Supplementary Special-purpose Plane
 </strong>
 | (U+E0000 to U+EFFFF)   |
| 16. |
 <strong>
  Supplementary Private Use Area - A
 </strong>
 | (U+F0000 to U+FFFFF)   |
| 17. |
 <strong>
  Supplementary Private Use Area - B
 </strong>
 | (U+100000 to U+10FFFF) |
</p>
<p>
 The first plane is called the Basic Multilingual Plane or BMP. It contains the code points from U+0000 to U+FFFF, which are the most frequently used characters. The other sixteen planes (U+010000 → U+10FFFF) are called supplementary planes or astral planes.
</p>
<h2>
 UTF-16 Surrogate Pairs
</h2>
<blockquote>
 <p>
  Characters outside the BMP, e.g. U+1D306 tetragram for centre (𝌆), can only be encoded in UTF-16 using two 16-bit code units: 0xD834 0xDF06. This is called a surrogate pair. Note that a surrogate pair only represents a single character.
  The first code unit of a surrogate pair is always in the range from 0xD800 to 0xDBFF, and is called a high surrogate or a lead surrogate.
  The second code unit of a surrogate pair is always in the range from 0xDC00 to 0xDFFF, and is called a low surrogate or a trail surrogate.
 </p>
</blockquote>
<p>
 --
 <a href="https://mathiasbynens.be/notes/javascript-encoding#surrogate-pairs">
  Mathias Bynens
 </a>
</p>
<blockquote>
 <p>
  Surrogate pair: A representation for a single abstract character that consists of a
  sequence of two 16-bit code units, where the first value of the pair is a high-surrogate
  code unit and the second value is a low-surrogate code unit. Surrogate pairs are used only in UTF-16. (See Section 3.9, Unicode Encoding
  Forms.) --
  <a href="http://unicode.org/versions/Unicode8.0.0/ch03.pdf#page=47">
   Unicode 8.0.0 Chapter 3 - Surrogates
  </a>
 </p>
</blockquote>
<h2>
 Calculating Surrogate Pairs
</h2>
<p>
 The Unicode character
 <strong>
  💩 Pile of Poo (U+1F4A9)
 </strong>
 in UTF-16 must be encoded as a surrogate pair, i.e. two surrogates. To convert any code point to a surrogate pair, use the following algorithm (in JavaScript). Keep in mind that we're using hexidecimal notation.
</p>
<p>
 ```javascript
 var High
 <em>
  Surrogate = function(Code
 </em>
 Point){ return Math.floor((Code
 <em>
  Point - 0x10000) / 0x400) + 0xD800 };
 var Low
 </em>
 Surrogate  = function(Code
 <em>
  Point){ return (Code
 </em>
 Point - 0x10000) % 0x400 + 0xDC00 };
</p>
<p>
 // Reverses The Conversion
 var Code
 <em>
  Point = function(High
 </em>
 Surrogate, Low
 <em>
  Surrogate){
    return (High
 </em>
 Surrogate - 0xD800) * 0x400 + Low_Surrogate - 0xDC00 + 0x10000;
 };
```
</p>
<p>
 ```javascript
</p>
<blockquote>
 <p>
  var codepoint = 0x1F4A9;                                 // 0x1F4A9 == 128169
  High
  <em>
   Surrogate(codepoint).toString(16)
   "d83d"                                                     // 0xD83D == 55357
  Low
  </em>
  Surrogate(codepoint).toString(16)
   "dca9"                                                     // 0xDCA9 == 56489
 </p>
 <p>
  String.fromCharCode(  High
  <em>
   Surrogate(codepoint) , Low
  </em>
  Surrogate(codepoint) );
    "💩"
  String.fromCodePoint(0x1F4A9)
    "💩"
  '\ud83d\udca9'
    "💩"
  ```
 </p>
</blockquote>
<h2>
 Composing & Decomposing
</h2>
<p>
 Unicode includes a mechanism for modifying character shape that greatly extends the supported glyph repertoire. This covers the use of combining diacritical marks. They are inserted after the main character. Multiple combining diacritics may be stacked over the same character. Unicode also contains precomposed versions of most letter/diacritic combinations in normal use.
</p>
<p>
 Certain sequences of characters can also be represented as a single character, called a precomposed character (or composite or decomposible character). For example, the character "ü" can be encoded as the single code point U+00FC "ü" or as the base character U+0075 "u" followed by the non-spacing character U+0308 "¨". The Unicode Standard encodes precomposed characters for compatibility with established standards such as Latin 1, which includes many precomposed characters such as "ü" and "ñ".
</p>
<p>
 Precomposed characters may be decomposed for consistency or analysis. For example, in alphabetizing (collating) a list of names, the character "ü" may be decomposed into a "u" followed by the non-spacing character "¨". Once the character has been decomposed, it may be easier for the collation to work with the character because it can be processed as a "u" with modifications. This allows easier alphabetical sorting for languages where character modifiers do not affect alphabetical order. The Unicode Standard defines the
 <a href="http://unicode.org/versions/Unicode8.0.0/ch03.pdf#page=44">
  decompositions
 </a>
 for all precomposed characters. It also defines normalization forms to provide for unique representations of characters.
</p>
<h2>
 Myths of Unicode
</h2>
<p>
 <em>
  From Mark Davis's
  <a href="http://macchiato.com/slides/UnicodeMyths.pdf">
   Unicode Myths
  </a>
  slides.
 </em>
 -
 <strong>
  Unicode is simply a 16-bit code
 </strong>
 - Some people are under the misconception that Unicode is simply a 16-bit code where each character takes 16 bits and therefore there are 65,536 possible characters. This is not, actually, correct. It is the single most common myth about Unicode, so if you thought that, don't feel bad.
</p>
<ul>
 <li>
  <p>
   <strong>
    You can use any unassigned codepoint for internal use
   </strong>
   - No. Eventually that hole will be filled with a different character. Instead use private use or noncharacters.
  </p>
 </li>
 <li>
  <p>
   <strong>
    Every Unicode code point represents a character
   </strong>
   - No. There are lots of nonCharacters (FFFE, FFFF, 1FFFE,…)
There are also surrogate code points, private and unassigned codepoints, and control/format “characters" (RLM, ZWNJ,…)
  </p>
 </li>
 <li>
  <p>
   <strong>
    Unicode will run out of space
   </strong>
   - If it were linear, we would run out in 2140 AD. But it isn't linear. See http://www.unicode.org/roadmaps/
  </p>
 </li>
 <li>
  <p>
   <strong>
    Case mappings are 1-1
   </strong>
   - No. They can also be:
  </p>
  <ul>
   <li>
    One-to-many: (ß → SS )
   </li>
   <li>
    Contextual: (…Σ ↔ …ς AND …ΣΤ… ↔ …στ… )
   </li>
   <li>
    Locale-sensitive: ( I ↔ ı AND İ ↔ i )
   </li>
  </ul>
 </li>
</ul>
<h2>
 Applied Unicode Encodings
</h2>
<p>
 | Encoding Type             |  Raw Encoding                         |
|---------------------------|---------------------------------------|
|HTML Entity (Decimal)      | 🖖                             |
|HTML Entity (Hexadecimal)  | 🖖                             |
|URL Escape Code            | %F0%9F%96%96                          |
|UTF-8 (hex)                | 0xF0 0x9F 0x96 0x96 (f09f9696)        |
|UTF-8 (binary)             | 11110000:10011111:10010110:10010110   |
|UTF-16/UTF-16BE (hex)      | 0xD83D 0xDD96 (d83ddd96)              |
|UTF-16LE (hex)             | 0x3DD8 0x96DD (3dd896dd)              |
|UTF-32/UTF-32BE (hex)      | 0x0001F596 (0001f596)                 |
|UTF-32LE (hex)             | 0x96F50100 (96f50100)                 |
|Octal Escape Sequence      | \360\237\226\226                      |
</p>
<h2>
 Source Code
</h2>
<p>
 |Encoding Type| Raw Encoding|
|-------------|-------------|
| JavaScript  | \u1F596     |
| JSON        | \u1F596     |
| C           | \u1F596     |
| C++         | \u1F596     |
| Java        | \u1F596     |
| Python      | \u1F596     |
| Perl        | \x{1F596}   |
| Ruby        | \u{1F596}   |
| CSS         | \01F596     |
</p>
<h1>
 Awesome Characters List
</h1>
<p>
 <center>
  <a href="https://xkcd.com/1137/">
   <img alt="" src="http://imgs.xkcd.com/comics/rtl.png "/>
  </a>
 </center>
</p>
<h2>
 Special Characters
</h2>
<p>
 The Unicode Consortium published a
 <a href="http://www.unicode.org/charts/PDF/U2000.pdf">
  general punctuation chart
 </a>
 where you can find more details.
</p>
<p>
 | Char     | Name                                     | Description                                                                                                                                                                                    |
|----------|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|
 <code>
  '﻿'
 </code>
 | U+FEFF (Byte Order Mark - BOM)           | has the important property of unambiguity on byte reorder. It is also zerowidth, and invisible. In non-complying software (like the PHP interpreter) this leads to all sorts of fun behaviour. |
|
 <code>
  '￯'
 </code>
 | '\uFFEF' Reversed Byte Order Mark (BOM) | does not equate to a legal character, other than the beginning of text.                                                                                                                        |
|
 <code>
  '​'
 </code>
 | '\u200B' zero-width non-break space     | (a character with no appearance and no effect other than preventing the formation of ligatures).                                                                                               |
|
 <code>
  ' '
 </code>
 | U+00A0 NO-BREAK SPACE                    | force adjacent characters to stick together. Well known as
 <code>
  &nbsp;
 </code>
 in HTML.                                                                                                                          |
|
 <code>
  '­'
 </code>
 | U+00AD SOFT HYPHEN                       | (in HTML: ­) like ZERO WIDTH SPACE, but show a hyphen if (and only if) a break occurs.                                                                                                         |
|
 <code>
  '‍'
 </code>
 | U+200D ZERO WIDTH JOINER                 | force adjacent characters to be joined together (e.g., arabic characters or supported emoji). Can be used this to compose sequentially combined emoji.                                         |
|
 <code>
  '⁠'
 </code>
 | U+2060 WORD JOINER                       | the same as U+00A0, but completely invisible. Good for writing @font-face on Twitter.                                                                                                          |
|
 <code>
  ' '
 </code>
 | U+1680 OGHAM SPACE MARK                  | a space that looks like a dash. Great to bring programmers close to madness: 1 +  2 === 3.                                                                                                     |
|
 <code>
  ';'
 </code>
 | U+037E GREEK QUESTION MARK               | a look-alike to the semicolon. Also a fun way to annoy developers.                                                                                                                             |
|
 <code>
  '‭'
 </code>
 | U+202D                                   | change the text direction to Left-to-Right.                                                                                                                                                    |
|
 <code>
  '‮'
 </code>
 ‭ ‭ | U+202E                                   | change the text direction to Right-to-Left:                                                                                                                                     |
|
 <code>
  'ꓸ'
 </code>
 | U+A4F8 LISU LETTER TONE MYA TI |A lookalike for the period character. |
|
 <code>
  'ꓹ'
 </code>
 | U+A4F9 LISU LETTER TONE NA PO |A lookalike for the comma character.|
|
 <code>
  'ꓼ'
 </code>
 | U+A4FC LISU LETTER TONE MYA NA |A lookalike for the semi-colon character.|
|
 <code>
  'ꓽ'
 </code>
 | U+A4FD LISU LETTER TONE MYA JEU|A lookalike for the colon character.|
|
 <code>
  '︀'
 </code>
 |
 <strong>
  Variation Selectors
 </strong>
 ( U+FE00 to U+FE0F & U+E0100 to U+E01EF )  | a block of 256 zero width characters that posess the ID
 <em>
  Continue proprerty- meaning they can be used in variable names (not the first letter). What makes these special is the fact that mouse cursors pass over them as they are combining characters - unlike most other zero width characters.|
|
  <code>
   'ᅟ'
  </code>
  |
  <strong>
   U+115F HANGUL CHOSEONG FILLER
  </strong>
  | In general it produces a space. Rendered as zero width (invisible) if not explicitly supported in rendering. Designated ID
 </em>
 Start|
|
 <code>
  'ᅠ'
 </code>
 |
 <strong>
  U+1160 HANGUL JUNGSEONG FILLER
 </strong>
 | Perhaps it produces a space? Rendered as zero width (invisible) if not explicitly supported in rendering. Designated ID
 <em>
  Start|
|
  <code>
   'ㅤ'
  </code>
  |
  <strong>
   U+3164 HANGUL FILLER
  </strong>
  | In general it produces a space. Rendered as zero width (invisible) if not explicitly supported in rendering. Designated ID
 </em>
 Start |
 <br>
  <br/>
 </br>
</p>
<h4>
 Wait a second... what did I just read?
</h4>
<p>
 <br>
  <br/>
 </br>
</p>
<h2>
 Variable identifiers can effectively include whitespace!
</h2>
<p>
 The
 <strong>
  U+3164 HANGUL FILLER
 </strong>
 character displays as an advancing whitespace character. The character is rendered as completely invisible (and non advancing, i.e. "zero width"), if not explicitly
 <a href="http://unicode.org/faq/unsup_char.html">
  supported in rendering
 </a>
 . That means the ugly character replacement (�) symbol should never be displayed.
</p>
<p>
 I'm not yet sure why U+3164 was specified to behave this way. Interestingly, U+3164 was added to Unicode in version 1.1 (1993)- so the consortium must have had a lot of time to think it through. Anyway, here are a few examples.
</p>
<p>
 ```javascript
</p>
<blockquote>
 <p>
  var ᅟ = 'foo';
  undefined
  ᅟ
  'foo'
 </p>
 <p>
  var ㅤ= alert;
  undefined
  var foo = 'bar'
  undefined
  if ( foo ===ㅤ
  <code>
   baz
  </code>
  ){}    // alert
  undefined
 </p>
 <p>
  var varㅤfooㅤ\u{A60C}ㅤπ = 'bar';
  undefined
  varㅤfooㅤꘌㅤπ
  'bar'
 </p>
</blockquote>
<p>
 ``
 <code>
  <br>
**NOTE:** I've tested U+3164 rendering on Ubuntu and OS X with the following:
 </code>
 node
 <code>
  ,
 </code>
 php
 <code>
  ,
 </code>
 ruby
 <code>
  ,
 </code>
 python3.5
 <code>
  ,
 </code>
 scala
 <code>
  ,
 </code>
 vim
 <code>
  ,
 </code>
 cat
 <code>
  ,
 </code>
 chrome
 <code>
  +
 </code>
 github gist`. Atom is the only system that fails by (incorrectly) displaying empty boxes. I have yet to test it out on Emacs and Sublime. From what I understand, the Unicode Consortium will not reassign or rename characters or codepoints, but may be convinced to change character properties like ID
 <em>
  Start/ID
 </em>
 Continue.
</p>
<p>
 <br/>
</p>
<h2>
 Modifiers
</h2>
<p>
 The zero-width joiner (ZWJ) is a non-printing character used in the computerized typesetting of some complex scripts such as the Arabic script or any Indic script. When placed between two characters that would otherwise not be connected, a ZWJ causes them to be printed in their connected forms.
</p>
<p>
 The zero-width non-joiner (ZWNJ) is a non-printing character used in the computerization of writing systems that make use of ligatures. When placed between two characters that would otherwise be connected into a ligature, a ZWNJ causes them to be printed in their final and initial forms, respectively. This is also an effect of a space character, but a ZWNJ is used when it is desirable to keep the words closer together or to connect a word with its morpheme.
</p>
<p>
 ```javascript
</p>
<blockquote>
 <p>
  'a'
   "a"
 </p>
 <p>
  'a\u{0308}'
   "ä"
 </p>
 <p>
  'a\u{20DE}\u{0308}'
   "a⃞̈"
 </p>
 <p>
  'a\u{20DE}\u{0308}\u{20DD}'
   "a⃞̈⃝"
 </p>
</blockquote>
<p>
 // Modifying Invisible Characters
</p>
<blockquote>
 <p>
  '\u{200E}\u{200E}\u{200E}\u{200E}\u{200E}\u{200E}\u{200E}\u{200E}\u{200E}\u{200E}'
   "‎‎‎‎‎‎‎‎‎‎"
 </p>
 <p>
  '\u{200E}\u{200E}\u{200E}\u{200E}\u{200E}\u{200E}\u{200E}\u{200E}\u{200E}\u{200E}'.length
   10
  ```
 </p>
</blockquote>
<h2>
 :collision: Uppercase Transformation Collisions
</h2>
<p>
 | Char | Code Point | Output Char |
|------|------------|-------------|
| ß | 0x00DF |
 <code>
  SS
 </code>
 |
| ı | 0x0131 |
 <code>
  I
 </code>
 |
| ſ | 0x017F |
 <code>
  S
 </code>
 |
| ﬀ | 0xFB00 |
 <code>
  FF
 </code>
 |
| ﬁ | 0xFB01 |
 <code>
  FI
 </code>
 |
| ﬂ | 0xFB02 |
 <code>
  FL
 </code>
 |
| ﬃ | 0xFB03 |
 <code>
  FFI
 </code>
 |
| ﬄ | 0xFB04 |
 <code>
  FFL
 </code>
 |
| ﬅ | 0xFB05 |
 <code>
  ST
 </code>
 |
| ﬆ | 0xFB06 |
 <code>
  ST
 </code>
 |
</p>
<h2>
 :collision: Lowercase Transformation Collisions
</h2>
<p>
 | Char | Code Point | Output Char |
|------|------------|-------------|
| K | 0x212A |
 <code>
  k
 </code>
 |
</p>
<h1>
 Quirks and Troubleshooting
</h1>
<ul>
 <li>
  <p>
   <strong>
    String length is typically determined by counting codepoints.
   </strong>
   This means that surrogate pairs would count as two characters. Combining multiple diacritics may be stacked over the same character.
   <code>
    a + ̈  == ̈a
   </code>
   , increasing length, while only producing a single character.
  </p>
 </li>
 <li>
  <p>
   <strong>
    Similarily, reversing strings often is a non-trivial task.
   </strong>
   Again, surrogate pairs and diacritics must be reversed together.
   <a href="https://github.com/mathiasbynens/esrever">
    ES Reverser
   </a>
   provides a pretty good solution.
  </p>
 </li>
 <li>
  <p>
   <strong>
    Upper and lower case mappings are not always one-to-one.
   </strong>
   They can also be:
  </p>
  <ul>
   <li>
    One-to-many: (ß → SS )
   </li>
   <li>
    Contextual: (…Σ ↔ …ς AND …ΣΤ… ↔ …στ… )
   </li>
   <li>
    Locale-sensitive: ( I ↔ ı AND İ ↔ i )
   </li>
  </ul>
 </li>
</ul>
<h3>
 One-To-Many Case Mappings
</h3>
<p>
 <em>
  Most of the below characters express their one-to-many case mappings when uppercased- while others should be lowercased. This list should be split up
 </em>
</p>
<p>
 | Code Point                                      | Character | Name                                                                     | Mapped Character | Mapped Code Points     |
|-------------------------------------------------|-----------|--------------------------------------------------------------------------|------------------|------------------------|
|
 <a href="https://codepoints.net/U+00DF?lang=en">
  U+00DF
 </a>
 |
 <code>
  ß
 </code>
 | LATIN SMALL LETTER SHARP S                                               |
 <code>
  s
 </code>
 ,
 <code>
  s
 </code>
 | U+0073, U+0073         |
|
 <a href="https://codepoints.net/U+0130?lang=en">
  U+0130
 </a>
 |
 <code>
  İ
 </code>
 | LATIN CAPITAL LETTER I WITH DOT ABOVE                                    |
 <code>
  i
 </code>
 ,
 <code>
  ̇
 </code>
 | U+0069, U+0307         |
|
 <a href="https://codepoints.net/U+0149?lang=en">
  U+0149
 </a>
 |
 <code>
  ŉ
 </code>
 | LATIN SMALL LETTER N PRECEDED BY APOSTROPHE                              |
 <code>
  ʼ
 </code>
 ,
 <code>
  n
 </code>
 | U+02BC, U+006E         |
|
 <a href="https://codepoints.net/U+01F0?lang=en">
  U+01F0
 </a>
 |
 <code>
  ǰ
 </code>
 | LATIN SMALL LETTER J WITH CARON                                          |
 <code>
  j
 </code>
 ,
 <code>
  ̌
 </code>
 | U+006A, U+030C         |
|
 <a href="https://codepoints.net/U+0390?lang=en">
  U+0390
 </a>
 |
 <code>
  ΐ
 </code>
 | GREEK SMALL LETTER IOTA WITH DIALYTIKA AND TONOS                         |
 <code>
  ι
 </code>
 ,
 <code>
  ̈
 </code>
 ,
 <code>
  ́
 </code>
 | U+03B9, U+0308, U+0301 |
|
 <a href="https://codepoints.net/U+03B0?lang=en">
  U+03B0
 </a>
 |
 <code>
  ΰ
 </code>
 | GREEK SMALL LETTER UPSILON WITH DIALYTIKA AND TONOS                      |
 <code>
  υ
 </code>
 ,
 <code>
  ̈
 </code>
 ,
 <code>
  ́
 </code>
 | U+03C5, U+0308, U+0301 |
|
 <a href="https://codepoints.net/U+0587?lang=en">
  U+0587
 </a>
 |
 <code>
  և
 </code>
 | ARMENIAN SMALL LIGATURE ECH YIWN                                         |
 <code>
  ե
 </code>
 ,
 <code>
  ւ
 </code>
 | U+0565, U+0582         |
|
 <a href="https://codepoints.net/U+1E96?lang=en">
  U+1E96
 </a>
 |
 <code>
  ẖ
 </code>
 | LATIN SMALL LETTER H WITH LINE BELOW                                     |
 <code>
  h
 </code>
 ,
 <code>
  ̱
 </code>
 | U+0068, U+0331         |
|
 <a href="https://codepoints.net/U+1E97?lang=en">
  U+1E97
 </a>
 |
 <code>
  ẗ
 </code>
 | LATIN SMALL LETTER T WITH DIAERESIS                                      |
 <code>
  t
 </code>
 ,
 <code>
  ̈
 </code>
 | U+0074, U+0308         |
|
 <a href="https://codepoints.net/U+1E98?lang=en">
  U+1E98
 </a>
 |
 <code>
  ẘ
 </code>
 | LATIN SMALL LETTER W WITH RING ABOVE                                     |
 <code>
  w
 </code>
 ,
 <code>
  ̊
 </code>
 | U+0077, U+030A         |
|
 <a href="https://codepoints.net/U+1E99?lang=en">
  U+1E99
 </a>
 |
 <code>
  ẙ
 </code>
 | LATIN SMALL LETTER Y WITH RING ABOVE                                     |
 <code>
  y
 </code>
 ,
 <code>
  ̊
 </code>
 | U+0079, U+030A         |
|
 <a href="https://codepoints.net/U+1E9A?lang=en">
  U+1E9A
 </a>
 |
 <code>
  ẚ
 </code>
 | LATIN SMALL LETTER A WITH RIGHT HALF RING                                |
 <code>
  a
 </code>
 ,
 <code>
  ʾ
 </code>
 | U+0061, U+02BE         |
|
 <a href="https://codepoints.net/U+1E9E?lang=en">
  U+1E9E
 </a>
 |
 <code>
  ẞ
 </code>
 | LATIN CAPITAL LETTER SHARP S                                             |
 <code>
  s
 </code>
 ,
 <code>
  s
 </code>
 | U+0073, U+0073         |
|
 <a href="https://codepoints.net/U+1F50?lang=en">
  U+1F50
 </a>
 |
 <code>
  ὐ
 </code>
 | GREEK SMALL LETTER UPSILON WITH PSILI                                    |
 <code>
  υ
 </code>
 ,
 <code>
  ̓
 </code>
 | U+03C5, U+0313         |
|
 <a href="https://codepoints.net/U+1F52?lang=en">
  U+1F52
 </a>
 |
 <code>
  ὒ
 </code>
 | GREEK SMALL LETTER UPSILON WITH PSILI AND VARIA                          |
 <code>
  υ
 </code>
 ,
 <code>
  ̓
 </code>
 ,
 <code>
  ̀
 </code>
 | U+03C5, U+0313, U+0300 |
|
 <a href="https://codepoints.net/U+1F54?lang=en">
  U+1F54
 </a>
 |
 <code>
  ὔ
 </code>
 | GREEK SMALL LETTER UPSILON WITH PSILI AND OXIA                           |
 <code>
  υ
 </code>
 ,
 <code>
  ̓
 </code>
 ,
 <code>
  ́
 </code>
 | U+03C5, U+0313, U+0301 |
|
 <a href="https://codepoints.net/U+1F56?lang=en">
  U+1F56
 </a>
 |
 <code>
  ὖ
 </code>
 | GREEK SMALL LETTER UPSILON WITH PSILI AND PERISPOMENI                    |
 <code>
  υ
 </code>
 ,
 <code>
  ̓
 </code>
 ,
 <code>
  ͂
 </code>
 | U+03C5, U+0313, U+0342 |
|
 <a href="https://codepoints.net/U+1F80?lang=en">
  U+1F80
 </a>
 |
 <code>
  ᾀ
 </code>
 | GREEK SMALL LETTER ALPHA WITH PSILI AND YPOGEGRAMMENI                    |
 <code>
  ἀ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F00, U+03B9         |
|
 <a href="https://codepoints.net/U+1F81?lang=en">
  U+1F81
 </a>
 |
 <code>
  ᾁ
 </code>
 | GREEK SMALL LETTER ALPHA WITH DASIA AND YPOGEGRAMMENI                    |
 <code>
  ἁ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F01, U+03B9         |
|
 <a href="https://codepoints.net/U+1F82?lang=en">
  U+1F82
 </a>
 |
 <code>
  ᾂ
 </code>
 | GREEK SMALL LETTER ALPHA WITH PSILI AND VARIA AND YPOGEGRAMMENI          |
 <code>
  ἂ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F02, U+03B9         |
|
 <a href="https://codepoints.net/U+1F83?lang=en">
  U+1F83
 </a>
 |
 <code>
  ᾃ
 </code>
 | GREEK SMALL LETTER ALPHA WITH DASIA AND VARIA AND YPOGEGRAMMENI          |
 <code>
  ἃ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F03, U+03B9         |
|
 <a href="https://codepoints.net/U+1F84?lang=en">
  U+1F84
 </a>
 |
 <code>
  ᾄ
 </code>
 | GREEK SMALL LETTER ALPHA WITH PSILI AND OXIA AND YPOGEGRAMMENI           |
 <code>
  ἄ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F04, U+03B9         |
|
 <a href="https://codepoints.net/U+1F85?lang=en">
  U+1F85
 </a>
 |
 <code>
  ᾅ
 </code>
 | GREEK SMALL LETTER ALPHA WITH DASIA AND OXIA AND YPOGEGRAMMENI           |
 <code>
  ἅ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F05, U+03B9         |
|
 <a href="https://codepoints.net/U+1F86?lang=en">
  U+1F86
 </a>
 |
 <code>
  ᾆ
 </code>
 | GREEK SMALL LETTER ALPHA WITH PSILI AND PERISPOMENI AND YPOGEGRAMMENI    |
 <code>
  ἆ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F06, U+03B9         |
|
 <a href="https://codepoints.net/U+1F87?lang=en">
  U+1F87
 </a>
 |
 <code>
  ᾇ
 </code>
 | GREEK SMALL LETTER ALPHA WITH DASIA AND PERISPOMENI AND YPOGEGRAMMENI    |
 <code>
  ἇ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F07, U+03B9         |
|
 <a href="https://codepoints.net/U+1F88?lang=en">
  U+1F88
 </a>
 |
 <code>
  ᾈ
 </code>
 | GREEK CAPITAL LETTER ALPHA WITH PSILI AND PROSGEGRAMMENI                 |
 <code>
  ἀ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F00, U+03B9         |
|
 <a href="https://codepoints.net/U+1F89?lang=en">
  U+1F89
 </a>
 |
 <code>
  ᾉ
 </code>
 | GREEK CAPITAL LETTER ALPHA WITH DASIA AND PROSGEGRAMMENI                 |
 <code>
  ἁ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F01, U+03B9         |
|
 <a href="https://codepoints.net/U+1F8A?lang=en">
  U+1F8A
 </a>
 |
 <code>
  ᾊ
 </code>
 | GREEK CAPITAL LETTER ALPHA WITH PSILI AND VARIA AND PROSGEGRAMMENI       |
 <code>
  ἂ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F02, U+03B9         |
|
 <a href="https://codepoints.net/U+1F8B?lang=en">
  U+1F8B
 </a>
 |
 <code>
  ᾋ
 </code>
 | GREEK CAPITAL LETTER ALPHA WITH DASIA AND VARIA AND PROSGEGRAMMENI       |
 <code>
  ἃ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F03, U+03B9         |
|
 <a href="https://codepoints.net/U+1F8C?lang=en">
  U+1F8C
 </a>
 |
 <code>
  ᾌ
 </code>
 | GREEK CAPITAL LETTER ALPHA WITH PSILI AND OXIA AND PROSGEGRAMMENI        |
 <code>
  ἄ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F04, U+03B9         |
|
 <a href="https://codepoints.net/U+1F8D?lang=en">
  U+1F8D
 </a>
 |
 <code>
  ᾍ
 </code>
 | GREEK CAPITAL LETTER ALPHA WITH DASIA AND OXIA AND PROSGEGRAMMENI        |
 <code>
  ἅ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F05, U+03B9         |
|
 <a href="https://codepoints.net/U+1F8E?lang=en">
  U+1F8E
 </a>
 |
 <code>
  ᾎ
 </code>
 | GREEK CAPITAL LETTER ALPHA WITH PSILI AND PERISPOMENI AND PROSGEGRAMMENI |
 <code>
  ἆ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F06, U+03B9         |
|
 <a href="https://codepoints.net/U+1F8F?lang=en">
  U+1F8F
 </a>
 |
 <code>
  ᾏ
 </code>
 | GREEK CAPITAL LETTER ALPHA WITH DASIA AND PERISPOMENI AND PROSGEGRAMMENI |
 <code>
  ἇ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F07, U+03B9         |
|
 <a href="https://codepoints.net/U+1F90?lang=en">
  U+1F90
 </a>
 |
 <code>
  ᾐ
 </code>
 | GREEK SMALL LETTER ETA WITH PSILI AND YPOGEGRAMMENI                      |
 <code>
  ἠ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F20, U+03B9         |
|
 <a href="https://codepoints.net/U+1F91?lang=en">
  U+1F91
 </a>
 |
 <code>
  ᾑ
 </code>
 | GREEK SMALL LETTER ETA WITH DASIA AND YPOGEGRAMMENI                      |
 <code>
  ἡ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F21, U+03B9         |
|
 <a href="https://codepoints.net/U+1F92?lang=en">
  U+1F92
 </a>
 |
 <code>
  ᾒ
 </code>
 | GREEK SMALL LETTER ETA WITH PSILI AND VARIA AND YPOGEGRAMMENI            |
 <code>
  ἢ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F22, U+03B9         |
|
 <a href="https://codepoints.net/U+1F93?lang=en">
  U+1F93
 </a>
 |
 <code>
  ᾓ
 </code>
 | GREEK SMALL LETTER ETA WITH DASIA AND VARIA AND YPOGEGRAMMENI            |
 <code>
  ἣ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F23, U+03B9         |
|
 <a href="https://codepoints.net/U+1F94?lang=en">
  U+1F94
 </a>
 |
 <code>
  ᾔ
 </code>
 | GREEK SMALL LETTER ETA WITH PSILI AND OXIA AND YPOGEGRAMMENI             |
 <code>
  ἤ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F24, U+03B9         |
|
 <a href="https://codepoints.net/U+1F95?lang=en">
  U+1F95
 </a>
 |
 <code>
  ᾕ
 </code>
 | GREEK SMALL LETTER ETA WITH DASIA AND OXIA AND YPOGEGRAMMENI             |
 <code>
  ἥ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F25, U+03B9         |
|
 <a href="https://codepoints.net/U+1F96?lang=en">
  U+1F96
 </a>
 |
 <code>
  ᾖ
 </code>
 | GREEK SMALL LETTER ETA WITH PSILI AND PERISPOMENI AND YPOGEGRAMMENI      |
 <code>
  ἦ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F26, U+03B9         |
|
 <a href="https://codepoints.net/U+1F97?lang=en">
  U+1F97
 </a>
 |
 <code>
  ᾗ
 </code>
 | GREEK SMALL LETTER ETA WITH DASIA AND PERISPOMENI AND YPOGEGRAMMENI      |
 <code>
  ἧ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F27, U+03B9         |
|
 <a href="https://codepoints.net/U+1F98?lang=en">
  U+1F98
 </a>
 |
 <code>
  ᾘ
 </code>
 | GREEK CAPITAL LETTER ETA WITH PSILI AND PROSGEGRAMMENI                   |
 <code>
  ἠ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F20, U+03B9         |
|
 <a href="https://codepoints.net/U+1F99?lang=en">
  U+1F99
 </a>
 |
 <code>
  ᾙ
 </code>
 | GREEK CAPITAL LETTER ETA WITH DASIA AND PROSGEGRAMMENI                   |
 <code>
  ἡ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F21, U+03B9         |
|
 <a href="https://codepoints.net/U+1F9A?lang=en">
  U+1F9A
 </a>
 |
 <code>
  ᾚ
 </code>
 | GREEK CAPITAL LETTER ETA WITH PSILI AND VARIA AND PROSGEGRAMMENI         |
 <code>
  ἢ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F22, U+03B9         |
|
 <a href="https://codepoints.net/U+1F9B?lang=en">
  U+1F9B
 </a>
 |
 <code>
  ᾛ
 </code>
 | GREEK CAPITAL LETTER ETA WITH DASIA AND VARIA AND PROSGEGRAMMENI         |
 <code>
  ἣ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F23, U+03B9         |
|
 <a href="https://codepoints.net/U+1F9C?lang=en">
  U+1F9C
 </a>
 |
 <code>
  ᾜ
 </code>
 | GREEK CAPITAL LETTER ETA WITH PSILI AND OXIA AND PROSGEGRAMMENI          |
 <code>
  ἤ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F24, U+03B9         |
|
 <a href="https://codepoints.net/U+1F9D?lang=en">
  U+1F9D
 </a>
 |
 <code>
  ᾝ
 </code>
 | GREEK CAPITAL LETTER ETA WITH DASIA AND OXIA AND PROSGEGRAMMENI          |
 <code>
  ἥ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F25, U+03B9         |
|
 <a href="https://codepoints.net/U+1F9E?lang=en">
  U+1F9E
 </a>
 |
 <code>
  ᾞ
 </code>
 | GREEK CAPITAL LETTER ETA WITH PSILI AND PERISPOMENI AND PROSGEGRAMMENI   |
 <code>
  ἦ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F26, U+03B9         |
|
 <a href="https://codepoints.net/U+1F9F?lang=en">
  U+1F9F
 </a>
 |
 <code>
  ᾟ
 </code>
 | GREEK CAPITAL LETTER ETA WITH DASIA AND PERISPOMENI AND PROSGEGRAMMENI   |
 <code>
  ἧ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F27, U+03B9         |
|
 <a href="https://codepoints.net/U+1FA0?lang=en">
  U+1FA0
 </a>
 |
 <code>
  ᾠ
 </code>
 | GREEK SMALL LETTER OMEGA WITH PSILI AND YPOGEGRAMMENI                    |
 <code>
  ὠ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F60, U+03B9         |
|
 <a href="https://codepoints.net/U+1FA1?lang=en">
  U+1FA1
 </a>
 |
 <code>
  ᾡ
 </code>
 | GREEK SMALL LETTER OMEGA WITH DASIA AND YPOGEGRAMMENI                    |
 <code>
  ὡ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F61, U+03B9         |
|
 <a href="https://codepoints.net/U+1FA2?lang=en">
  U+1FA2
 </a>
 |
 <code>
  ᾢ
 </code>
 | GREEK SMALL LETTER OMEGA WITH PSILI AND VARIA AND YPOGEGRAMMENI          |
 <code>
  ὢ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F62, U+03B9         |
|
 <a href="https://codepoints.net/U+1FA3?lang=en">
  U+1FA3
 </a>
 |
 <code>
  ᾣ
 </code>
 | GREEK SMALL LETTER OMEGA WITH DASIA AND VARIA AND YPOGEGRAMMENI          |
 <code>
  ὣ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F63, U+03B9         |
|
 <a href="https://codepoints.net/U+1FA4?lang=en">
  U+1FA4
 </a>
 |
 <code>
  ᾤ
 </code>
 | GREEK SMALL LETTER OMEGA WITH PSILI AND OXIA AND YPOGEGRAMMENI           |
 <code>
  ὤ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F64, U+03B9         |
|
 <a href="https://codepoints.net/U+1FA5?lang=en">
  U+1FA5
 </a>
 |
 <code>
  ᾥ
 </code>
 | GREEK SMALL LETTER OMEGA WITH DASIA AND OXIA AND YPOGEGRAMMENI           |
 <code>
  ὥ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F65, U+03B9         |
|
 <a href="https://codepoints.net/U+1FA6?lang=en">
  U+1FA6
 </a>
 |
 <code>
  ᾦ
 </code>
 | GREEK SMALL LETTER OMEGA WITH PSILI AND PERISPOMENI AND YPOGEGRAMMENI    |
 <code>
  ὦ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F66, U+03B9         |
|
 <a href="https://codepoints.net/U+1FA7?lang=en">
  U+1FA7
 </a>
 |
 <code>
  ᾧ
 </code>
 | GREEK SMALL LETTER OMEGA WITH DASIA AND PERISPOMENI AND YPOGEGRAMMENI    |
 <code>
  ὧ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F67, U+03B9         |
|
 <a href="https://codepoints.net/U+1FA8?lang=en">
  U+1FA8
 </a>
 |
 <code>
  ᾨ
 </code>
 | GREEK CAPITAL LETTER OMEGA WITH PSILI AND PROSGEGRAMMENI                 |
 <code>
  ὠ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F60, U+03B9         |
|
 <a href="https://codepoints.net/U+1FA9?lang=en">
  U+1FA9
 </a>
 |
 <code>
  ᾩ
 </code>
 | GREEK CAPITAL LETTER OMEGA WITH DASIA AND PROSGEGRAMMENI                 |
 <code>
  ὡ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F61, U+03B9         |
|
 <a href="https://codepoints.net/U+1FAA?lang=en">
  U+1FAA
 </a>
 |
 <code>
  ᾪ
 </code>
 | GREEK CAPITAL LETTER OMEGA WITH PSILI AND VARIA AND PROSGEGRAMMENI       |
 <code>
  ὢ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F62, U+03B9         |
|
 <a href="https://codepoints.net/U+1FAB?lang=en">
  U+1FAB
 </a>
 |
 <code>
  ᾫ
 </code>
 | GREEK CAPITAL LETTER OMEGA WITH DASIA AND VARIA AND PROSGEGRAMMENI       |
 <code>
  ὣ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F63, U+03B9         |
|
 <a href="https://codepoints.net/U+1FAC?lang=en">
  U+1FAC
 </a>
 |
 <code>
  ᾬ
 </code>
 | GREEK CAPITAL LETTER OMEGA WITH PSILI AND OXIA AND PROSGEGRAMMENI        |
 <code>
  ὤ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F64, U+03B9         |
|
 <a href="https://codepoints.net/U+1FAD?lang=en">
  U+1FAD
 </a>
 |
 <code>
  ᾭ
 </code>
 | GREEK CAPITAL LETTER OMEGA WITH DASIA AND OXIA AND PROSGEGRAMMENI        |
 <code>
  ὥ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F65, U+03B9         |
|
 <a href="https://codepoints.net/U+1FAE?lang=en">
  U+1FAE
 </a>
 |
 <code>
  ᾮ
 </code>
 | GREEK CAPITAL LETTER OMEGA WITH PSILI AND PERISPOMENI AND PROSGEGRAMMENI |
 <code>
  ὦ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F66, U+03B9         |
|
 <a href="https://codepoints.net/U+1FAF?lang=en">
  U+1FAF
 </a>
 |
 <code>
  ᾯ
 </code>
 | GREEK CAPITAL LETTER OMEGA WITH DASIA AND PERISPOMENI AND PROSGEGRAMMENI |
 <code>
  ὧ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F67, U+03B9         |
|
 <a href="https://codepoints.net/U+1FB2?lang=en">
  U+1FB2
 </a>
 |
 <code>
  ᾲ
 </code>
 | GREEK SMALL LETTER ALPHA WITH VARIA AND YPOGEGRAMMENI                    |
 <code>
  ὰ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F70, U+03B9         |
|
 <a href="https://codepoints.net/U+1FB3?lang=en">
  U+1FB3
 </a>
 |
 <code>
  ᾳ
 </code>
 | GREEK SMALL LETTER ALPHA WITH YPOGEGRAMMENI                              |
 <code>
  α
 </code>
 ,
 <code>
  ι
 </code>
 | U+03B1, U+03B9         |
|
 <a href="https://codepoints.net/U+1FB4?lang=en">
  U+1FB4
 </a>
 |
 <code>
  ᾴ
 </code>
 | GREEK SMALL LETTER ALPHA WITH OXIA AND YPOGEGRAMMENI                     |
 <code>
  ά
 </code>
 ,
 <code>
  ι
 </code>
 | U+03AC, U+03B9         |
|
 <a href="https://codepoints.net/U+1FB6?lang=en">
  U+1FB6
 </a>
 |
 <code>
  ᾶ
 </code>
 | GREEK SMALL LETTER ALPHA WITH PERISPOMENI                                |
 <code>
  α
 </code>
 ,
 <code>
  ͂
 </code>
 | U+03B1, U+0342         |
|
 <a href="https://codepoints.net/U+1FB7?lang=en">
  U+1FB7
 </a>
 |
 <code>
  ᾷ
 </code>
 | GREEK SMALL LETTER ALPHA WITH PERISPOMENI AND YPOGEGRAMMENI              |
 <code>
  α
 </code>
 ,
 <code>
  ͂
 </code>
 ,
 <code>
  ι
 </code>
 | U+03B1, U+0342, U+03B9 |
|
 <a href="https://codepoints.net/U+1FBC?lang=en">
  U+1FBC
 </a>
 |
 <code>
  ᾼ
 </code>
 | GREEK CAPITAL LETTER ALPHA WITH PROSGEGRAMMENI                           |
 <code>
  α
 </code>
 ,
 <code>
  ι
 </code>
 | U+03B1, U+03B9         |
|
 <a href="https://codepoints.net/U+1FC2?lang=en">
  U+1FC2
 </a>
 |
 <code>
  ῂ
 </code>
 | GREEK SMALL LETTER ETA WITH VARIA AND YPOGEGRAMMENI                      |
 <code>
  ὴ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F74, U+03B9         |
|
 <a href="https://codepoints.net/U+1FC3?lang=en">
  U+1FC3
 </a>
 |
 <code>
  ῃ
 </code>
 | GREEK SMALL LETTER ETA WITH YPOGEGRAMMENI                                |
 <code>
  η
 </code>
 ,
 <code>
  ι
 </code>
 | U+03B7, U+03B9         |
|
 <a href="https://codepoints.net/U+1FC4?lang=en">
  U+1FC4
 </a>
 |
 <code>
  ῄ
 </code>
 | GREEK SMALL LETTER ETA WITH OXIA AND YPOGEGRAMMENI                       |
 <code>
  ή
 </code>
 ,
 <code>
  ι
 </code>
 | U+03AE, U+03B9         |
|
 <a href="https://codepoints.net/U+1FC6?lang=en">
  U+1FC6
 </a>
 |
 <code>
  ῆ
 </code>
 | GREEK SMALL LETTER ETA WITH PERISPOMENI                                  |
 <code>
  η
 </code>
 ,
 <code>
  ͂
 </code>
 | U+03B7, U+0342         |
|
 <a href="https://codepoints.net/U+1FC7?lang=en">
  U+1FC7
 </a>
 |
 <code>
  ῇ
 </code>
 | GREEK SMALL LETTER ETA WITH PERISPOMENI AND YPOGEGRAMMENI                |
 <code>
  η
 </code>
 ,
 <code>
  ͂
 </code>
 ,
 <code>
  ι
 </code>
 | U+03B7, U+0342, U+03B9 |
|
 <a href="https://codepoints.net/U+1FCC?lang=en">
  U+1FCC
 </a>
 |
 <code>
  ῌ
 </code>
 | GREEK CAPITAL LETTER ETA WITH PROSGEGRAMMENI                             |
 <code>
  η
 </code>
 ,
 <code>
  ι
 </code>
 | U+03B7, U+03B9         |
|
 <a href="https://codepoints.net/U+1FD2?lang=en">
  U+1FD2
 </a>
 |
 <code>
  ῒ
 </code>
 | GREEK SMALL LETTER IOTA WITH DIALYTIKA AND VARIA                         |
 <code>
  ι
 </code>
 ,
 <code>
  ̈
 </code>
 ,
 <code>
  ̀
 </code>
 | U+03B9, U+0308, U+0300 |
|
 <a href="https://codepoints.net/U+1FD3?lang=en">
  U+1FD3
 </a>
 |
 <code>
  ΐ
 </code>
 | GREEK SMALL LETTER IOTA WITH DIALYTIKA AND OXIA                          |
 <code>
  ι
 </code>
 ,
 <code>
  ̈
 </code>
 ,
 <code>
  ́
 </code>
 | U+03B9, U+0308, U+0301 |
|
 <a href="https://codepoints.net/U+1FD6?lang=en">
  U+1FD6
 </a>
 |
 <code>
  ῖ
 </code>
 | GREEK SMALL LETTER IOTA WITH PERISPOMENI                                 |
 <code>
  ι
 </code>
 ,
 <code>
  ͂
 </code>
 | U+03B9, U+0342         |
|
 <a href="https://codepoints.net/U+1FD7?lang=en">
  U+1FD7
 </a>
 |
 <code>
  ῗ
 </code>
 | GREEK SMALL LETTER IOTA WITH DIALYTIKA AND PERISPOMENI                   |
 <code>
  ι
 </code>
 ,
 <code>
  ̈
 </code>
 ,
 <code>
  ͂
 </code>
 | U+03B9, U+0308, U+0342 |
|
 <a href="https://codepoints.net/U+1FE2?lang=en">
  U+1FE2
 </a>
 |
 <code>
  ῢ
 </code>
 | GREEK SMALL LETTER UPSILON WITH DIALYTIKA AND VARIA                      |
 <code>
  υ
 </code>
 ,
 <code>
  ̈
 </code>
 ,
 <code>
  ̀
 </code>
 | U+03C5, U+0308, U+0300 |
|
 <a href="https://codepoints.net/U+1FE3?lang=en">
  U+1FE3
 </a>
 |
 <code>
  ΰ
 </code>
 | GREEK SMALL LETTER UPSILON WITH DIALYTIKA AND OXIA                       |
 <code>
  υ
 </code>
 ,
 <code>
  ̈
 </code>
 ,
 <code>
  ́
 </code>
 | U+03C5, U+0308, U+0301 |
|
 <a href="https://codepoints.net/U+1FE4?lang=en">
  U+1FE4
 </a>
 |
 <code>
  ῤ
 </code>
 | GREEK SMALL LETTER RHO WITH PSILI                                        |
 <code>
  ρ
 </code>
 ,
 <code>
  ̓
 </code>
 | U+03C1, U+0313         |
|
 <a href="https://codepoints.net/U+1FE6?lang=en">
  U+1FE6
 </a>
 |
 <code>
  ῦ
 </code>
 | GREEK SMALL LETTER UPSILON WITH PERISPOMENI                              |
 <code>
  υ
 </code>
 ,
 <code>
  ͂
 </code>
 | U+03C5, U+0342         |
|
 <a href="https://codepoints.net/U+1FE7?lang=en">
  U+1FE7
 </a>
 |
 <code>
  ῧ
 </code>
 | GREEK SMALL LETTER UPSILON WITH DIALYTIKA AND PERISPOMENI                |
 <code>
  υ
 </code>
 ,
 <code>
  ̈
 </code>
 ,
 <code>
  ͂
 </code>
 | U+03C5, U+0308, U+0342 |
|
 <a href="https://codepoints.net/U+1FF2?lang=en">
  U+1FF2
 </a>
 |
 <code>
  ῲ
 </code>
 | GREEK SMALL LETTER OMEGA WITH VARIA AND YPOGEGRAMMENI                    |
 <code>
  ὼ
 </code>
 ,
 <code>
  ι
 </code>
 | U+1F7C, U+03B9         |
|
 <a href="https://codepoints.net/U+1FF3?lang=en">
  U+1FF3
 </a>
 |
 <code>
  ῳ
 </code>
 | GREEK SMALL LETTER OMEGA WITH YPOGEGRAMMENI                              |
 <code>
  ω
 </code>
 ,
 <code>
  ι
 </code>
 | U+03C9, U+03B9         |
|
 <a href="https://codepoints.net/U+1FF4?lang=en">
  U+1FF4
 </a>
 |
 <code>
  ῴ
 </code>
 | GREEK SMALL LETTER OMEGA WITH OXIA AND YPOGEGRAMMENI                     |
 <code>
  ώ
 </code>
 ,
 <code>
  ι
 </code>
 | U+03CE, U+03B9         |
|
 <a href="https://codepoints.net/U+1FF6?lang=en">
  U+1FF6
 </a>
 |
 <code>
  ῶ
 </code>
 | GREEK SMALL LETTER OMEGA WITH PERISPOMENI                                |
 <code>
  ω
 </code>
 ,
 <code>
  ͂
 </code>
 | U+03C9, U+0342         |
|
 <a href="https://codepoints.net/U+1FF7?lang=en">
  U+1FF7
 </a>
 |
 <code>
  ῷ
 </code>
 | GREEK SMALL LETTER OMEGA WITH PERISPOMENI AND YPOGEGRAMMENI              |
 <code>
  ω
 </code>
 ,
 <code>
  ͂
 </code>
 ,
 <code>
  ι
 </code>
 | U+03C9, U+0342, U+03B9 |
|
 <a href="https://codepoints.net/U+1FFC?lang=en">
  U+1FFC
 </a>
 |
 <code>
  ῼ
 </code>
 | GREEK CAPITAL LETTER OMEGA WITH PROSGEGRAMMENI                           |
 <code>
  ω
 </code>
 ,
 <code>
  ι
 </code>
 | U+03C9, U+03B9         |
|
 <a href="https://codepoints.net/U+FB00?lang=en">
  U+FB00
 </a>
 |
 <code>
  ﬀ
 </code>
 | LATIN SMALL LIGATURE FF                                                  |
 <code>
  f
 </code>
 ,
 <code>
  f
 </code>
 | U+0066, U+0066         |
|
 <a href="https://codepoints.net/U+FB01?lang=en">
  U+FB01
 </a>
 |
 <code>
  ﬁ
 </code>
 | LATIN SMALL LIGATURE FI                                                  |
 <code>
  f
 </code>
 ,
 <code>
  i
 </code>
 | U+0066, U+0069         |
|
 <a href="https://codepoints.net/U+FB02?lang=en">
  U+FB02
 </a>
 |
 <code>
  ﬂ
 </code>
 | LATIN SMALL LIGATURE FL                                                  |
 <code>
  f
 </code>
 ,
 <code>
  l
 </code>
 | U+0066, U+006C         |
|
 <a href="https://codepoints.net/U+FB03?lang=en">
  U+FB03
 </a>
 |
 <code>
  ﬃ
 </code>
 | LATIN SMALL LIGATURE FFI                                                 |
 <code>
  f
 </code>
 ,
 <code>
  f
 </code>
 ,
 <code>
  i
 </code>
 | U+0066, U+0066, U+0069 |
|
 <a href="https://codepoints.net/U+FB04?lang=en">
  U+FB04
 </a>
 |
 <code>
  ﬄ
 </code>
 | LATIN SMALL LIGATURE FFL                                                 |
 <code>
  f
 </code>
 ,
 <code>
  f
 </code>
 ,
 <code>
  l
 </code>
 | U+0066, U+0066, U+006C |
|
 <a href="https://codepoints.net/U+FB05?lang=en">
  U+FB05
 </a>
 |
 <code>
  ﬅ
 </code>
 | LATIN SMALL LIGATURE LONG S T                                            |
 <code>
  s
 </code>
 ,
 <code>
  t
 </code>
 | U+0073, U+0074         |
|
 <a href="https://codepoints.net/U+FB06?lang=en">
  U+FB06
 </a>
 |
 <code>
  ﬆ
 </code>
 | LATIN SMALL LIGATURE ST                                                  |
 <code>
  s
 </code>
 ,
 <code>
  t
 </code>
 | U+0073, U+0074         |
|
 <a href="https://codepoints.net/U+FB13?lang=en">
  U+FB13
 </a>
 |
 <code>
  ﬓ
 </code>
 | ARMENIAN SMALL LIGATURE MEN NOW                                          |
 <code>
  մ
 </code>
 ,
 <code>
  ն
 </code>
 | U+0574, U+0576         |
|
 <a href="https://codepoints.net/U+FB14?lang=en">
  U+FB14
 </a>
 |
 <code>
  ﬔ
 </code>
 | ARMENIAN SMALL LIGATURE MEN ECH                                          |
 <code>
  մ
 </code>
 ,
 <code>
  ե
 </code>
 | U+0574, U+0565         |
|
 <a href="https://codepoints.net/U+FB15?lang=en">
  U+FB15
 </a>
 |
 <code>
  ﬕ
 </code>
 | ARMENIAN SMALL LIGATURE MEN INI                                          |
 <code>
  մ
 </code>
 ,
 <code>
  ի
 </code>
 | U+0574, U+056B         |
|
 <a href="https://codepoints.net/U+FB16?lang=en">
  U+FB16
 </a>
 |
 <code>
  ﬖ
 </code>
 | ARMENIAN SMALL LIGATURE VEW NOW                                          |
 <code>
  վ
 </code>
 ,
 <code>
  ն
 </code>
 | U+057E, U+0576         |
|
 <a href="https://codepoints.net/U+FB17?lang=en">
  U+FB17
 </a>
 |
 <code>
  ﬗ
 </code>
 | ARMENIAN SMALL LIGATURE MEN XEH                                          |
 <code>
  մ
 </code>
 ,
 <code>
  խ
 </code>
 | U+0574, U+056D         |
</p>
<h1>
 Awesome Packages & Libraries
</h1>
<ul>
 <li>
  <a href="https://github.com/jagracey/PhantomScript">
   PhantomScript
  </a>
  - :ghost: :flashlight: Invisible JavaScript code execution & social engineering
 </li>
 <li>
  <a href="https://github.com/mathiasbynens/esrever">
   ESReverser
  </a>
  - A Unicode-aware string reverser written in JavaScript.
 </li>
 <li>
  <a href="https://github.com/reinderien/mimic">
   mimic
  </a>
  - [ab]using Unicode to create tragedy
 </li>
 <li>
  <a href="https://github.com/LuminosoInsight/python-ftfy">
   python-ftfy
  </a>
  - Given Unicode text, make its representation consistent and possibly less broken.
  <sup>
   &#9733 1161, pushed 136 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/vim-utils/vim-troll-stopper">
   vim-troll-stopper
  </a>
  - Stop Unicode trolls from messing with your code.
 </li>
</ul>
<h1>
 Emojis
</h1>
<ul>
 <li>
  <a href="http://www.unicode.org/emoji/charts/full-emoji-list.html">
   Unicode Consortium's Emoji Chart
  </a>
 </li>
 <li>
  <a href="http://emojipedia.org/">
   Emojipedia
  </a>
  - Information about specific emoji, news blog.
 </li>
 <li>
  <a href="http://emojitracker.com/">
   emojitracker
  </a>
  - Realtime emoji use on Twitter.
 </li>
 <li>
  <a href="http://www.emojifoundation.com/">
   World Translation Foundation
  </a>
  - A way to promote, explore, and translate the written word into the pictorial alphabet of Emoji.
 </li>
 <li>
  <a href="http://caniemoji.com/android-2/">
   Can I Emoji?
  </a>
  - Displays the current status of native Emoji support across iOS, Android and Windows.
 </li>
 <li>
  <a href="http://www.name.com/blog/how-tos/2015/12/want-an-emoji-url-this-is-how-you-register-one/">
   How to register an emoji URL
  </a>
 </li>
</ul>
<h2>
 Diversity
</h2>
<p>
 The Unicode Consortium has made a huge effort better reflect and incorporate human diversity, including cultural practices. Here is the Consortium's
 <a href="http://unicode.org/reports/tr51/#Diversity">
  diversity report
 </a>
 .
</p>
<p>
 Emojis of mixed gender situations are now available, such as same sex families, holding hands, and kissing. The real kicker are
 <a href="http://www.unicode.org/emoji/charts/emoji-zwj-sequences.html">
  Emoji combined sequences
 </a>
 . Basically:
</p>
<p>
 | Code Points | Recipe   | Combined |
|-------------|----------|----------|
| U+1F469 U+200D U+2764 U+FE0F U+200D U+1F469 |
 <img alt="👩" height="36" src="http://unicode.org/reports/tr51/images/apple/apple_1f469.png" width="auto">
  <img alt="❤️‍" height="36" src="http://unicode.org/reports/tr51/images/other/zwj.png" width="auto">
   <img alt="❤️‍" height="36" src="http://unicode.org/reports/tr51/images/apple/apple_2764.png" width="auto">
    <img alt="❤️‍" height="36" src="http://unicode.org/reports/tr51/images/other/zwj.png" width="auto">
     <img alt="👩" height="36" src="http://unicode.org/reports/tr51/images/apple/apple_1f469.png" width="auto">
      |
      <img alt="couple with heart: woman, woman" height="36" src="http://unicode.org/reports/tr51/images/apple/apple_1f469_200d_2764_fe0f_200d_1f469.png" width="auto">
       |
|U+1F468 U+200D U+1F468 U+200D U+1F467 U+200D U+1F466|
       <img height="36" src="https://raw.githubusercontent.com/jagracey/Awesome-Unicode/c575db618a89c88624a8c3bdfe57eada064cbf14/resources/family%3B%20man%2C%20man%2C%20girl%2C%20boy%20-%20fallback%20-%20ZWJ.jpg" width="auto">
        |
        <img height="36" src="https://raw.githubusercontent.com/jagracey/Awesome-Unicode/58f28d08aef7f36eb6cdca22d25e7654cd8de5ae/resources/family%3B%20man%2C%20man%2C%20girl%2C%20boy.png" width="auto">
         |
        </img>
       </img>
      </img>
     </img>
    </img>
   </img>
  </img>
 </img>
</p>
<p>
 Further, emojis now support skin color modifiers.
</p>
<blockquote>
 <p>
  Five symbol modifier characters that provide for a range of skin tones for human emoji were released in Unicode Version 8.0 (mid-2015). These characters are based on the six tones of the Fitzpatrick scale, a recognized standard for dermatology (there are many examples of this scale online, such as FitzpatrickSkinType.pdf). The exact shades may vary between implementations. --
  <a href="http://unicode.org/reports/tr51/#Diversity">
   Unicode Consortium's Diversity report
  </a>
 </p>
</blockquote>
<p>
 | Code    | Name                                | Samples                                                                                                                                                                                                            |
|---------|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| U+1F3FB | EMOJI MODIFIER FITZPATRICK TYPE-1-2 |
 <img height="20" src="http://www.unicode.org/reports/tr51/images/other/swatch-type-1-2.png" width="20">
  <img height="20" src="http://www.unicode.org/reports/tr51/images/other/swatch-type-1-2-bw.png" width="20">
   |
| U+1F3FC | EMOJI MODIFIER FITZPATRICK TYPE-3   |
   <img height="20" src="http://www.unicode.org/reports/tr51/images/other/swatch-type-3.png" width="20">
    <img height="20" src="http://www.unicode.org/reports/tr51/images/other/swatch-type-3-bw.png" width="20">
     |
| U+1F3FD | EMOJI MODIFIER FITZPATRICK TYPE-4   |
     <img height="20" src="http://www.unicode.org/reports/tr51/images/other/swatch-type-4.png" width="20">
      <img height="20" src="http://www.unicode.org/reports/tr51/images/other/swatch-type-4-bw.png" width="20">
       |
| U+1F3FE | EMOJI MODIFIER FITZPATRICK TYPE-5   |
       <img height="20" src="http://www.unicode.org/reports/tr51/images/other/swatch-type-5.png" width="20">
        <img height="20" src="http://www.unicode.org/reports/tr51/images/other/swatch-type-5-bw.png" width="20">
         |
| U+1F3FF | EMOJI MODIFIER FITZPATRICK TYPE-6   |
         <img height="20" src="http://www.unicode.org/reports/tr51/images/other/swatch-type-6.png" width="20">
          <img height="20" src="http://www.unicode.org/reports/tr51/images/other/swatch-type-6-bw.png" width="20">
           |
          </img>
         </img>
        </img>
       </img>
      </img>
     </img>
    </img>
   </img>
  </img>
 </img>
</p>
<p>
 Just follow the desired Emoji with one of the skin color modifiers
 <code>
  \u{1F466}\u{1F3FE}
 </code>
 .
</p>
<p align="center">
 <img alt="" height="36" src="http://unicode.org/reports/tr51/images/other/person.png" width="auto">
  <font size="36">
   +
  </font>
  <img alt="" height="36" src="http://unicode.org/reports/tr51/images/other/swatch-type-5.png" width="auto">
   <font size="36">
    →
   </font>
   <img alt="" height="36" src="http://unicode.org/reports/tr51/images/other/person-5.png" width="auto">
   </img>
  </img>
 </img>
</p>
<p align="center">
 <img alt="" height="48" src="http://unicode.org/reports/tr51/images/other/palette-with-gray.png" width="auto">
 </img>
</p>
<h1>
 Creatively Naming Variables and Methods
</h1>
<p>
 <em>
  Examples are written in JavaScript (ES6)
 </em>
</p>
<p>
 In general, characters designated the
 <a href="https://codepoints.net/search?IDS=1">
  ID
  <em>
   START
  </em>
 </a>
 property may be used at the beggining of a variable name. Characters designated with the
 <a href="https://codepoints.net/search?IDC=1">
  ID
 </a>
</p>
CONTINUE
property may be used after the first character of a variable.
<p>
 ```javascript
</p>
<p>
 function rand(μ,σ){ ... };
</p>
<p>
 String.prototype.reverseⵑ = function(){..};
</p>
<p>
 Number.prototype.isTrueɁ = function(){..};
</p>
<p>
 var WhatDoesThisDoɁɁɁɁ = 42
```
</p>
<p>
 Here are some really creative variable names from
 <a href="https://mathiasbynens.be/notes/javascript-identifiers#examples">
  Mathias Bynes
 </a>
</p>
<p>
 ```javascript
// How convenient!
var π = Math.PI;
</p>
<p>
 // Sometimes, you just have to use the Bad Parts of JavaScript:
var ಠ_ಠ = eval;
</p>
<p>
 // Code, Y U NO WORK?!
var ლ
 <em>
  ಠ益ಠ
 </em>
 ლ = 42;
</p>
<p>
 // How about a JavaScript library for functional programming?
var λ = function() {};
</p>
<p>
 // Obfuscate boring variable names for great justice
var \u006C\u006F\u006C\u0077\u0061\u0074 = 'heh';
</p>
<p>
 // …or just make up random ones
var Ꙭൽↈⴱ = 'huh';
</p>
<p>
 // While perfectly valid, this doesn’t work in most browsers:
var foo\u200Cbar = 42;
</p>
<p>
 // This is
 <em>
  not
 </em>
 a bitwise left shift (
 <code>
  <<
 </code>
 ):
var 〱〱 = 2;
// This is, though:
〱〱 << 〱〱; // 8
</p>
<p>
 // Give yourself a discount:
var price
 <em>
  9̶9̶
 </em>
 89 = 'cheap';
</p>
<p>
 // Fun with Roman numerals
var Ⅳ = 4;
var Ⅴ = 5;
Ⅳ + Ⅴ; // 9
</p>
<p>
 // Cthulhu was here
var Hͫ̆̒̐ͣ̊̄ͯ͗͏̵̗̻̰̠̬͝ͅE̴̷̬͎̱̘͇͍̾ͦ͊͒͊̓̓̐_̫̠̱̩̭̤͈̑̎̋ͮͩ̒͑̾͋͘Ç̳͕̯̭̱̲̣̠̜͋̍O̴̦̗̯̹̼ͭ̐ͨ̊̈͘͠M̶̝̠̭̭̤̻͓͑̓̊ͣͤ̎͟͠E̢̞̮̹͍̞̳̣ͣͪ͐̈T̡̯̳̭̜̠͕͌̈́̽̿ͤ̿̅̑Ḧ̱̱̺̰̳̹̘̰́̏ͪ̂̽͂̀͠ = 'Zalgo';
```
</p>
<p>
 And here's some
 <a href="https://davidwalsh.name/unicode-css-classes">
  Unicode CSS Classes
 </a>
 from David Walsh
```html
 <!-- place this within the document head -->
 <meta charset="utf-8"/>
</p>
<p>
 <!-- error message -->
</p>
<div class="ಠ_ಠ">
 You do not have access to this page.
</div>
<p>
 <!-- success message -->
</p>
<div class="❤">
 Your changes have been saved successfully!
</div>
<p>
 ```
</p>
<p>
 ```css
.ಠ_ಠ {
    border: 1px solid #f00;
}
</p>
<p>
 .❤ {
    background: lightgreen;
}
```
</p>
<h2>
 Recursive HTML Tag Renaming Script
</h2>
<p>
 If you want to rename all your HTML tags to what appears as nothing, the following script is just what your looking for.
</p>
<p>
 <em>
  Do note however that HTML does not support all unicode characters.
 </em>
 ```javascript
// U+1160 HANGUL JUNGSEONG FILLER
transformAllTags('ᅠ');
</p>
<p>
 // An actual HTML element node designed to look like a comment node, using the U+01C3 LATIN LETTER RETROFLEX CLICK 
//  <ǃ-- name="viewport" content="width=device-width">
 <!--ǃ---->
 transformAllTags('ǃ--');
</p>
<p>
 // or even <ᅠ⃝
transformAllTags('\u{1160}\u{20dd}');
</p>
<p>
 // and for a bonus, all existing tag names will have each character ensquared. h⃞t⃞m⃞l⃞
transformAllTags();
</p>
<p>
 function transformAllTags (newName){
   // querySelectorAll doesn't actually return an array.
   Array.from(document.querySelectorAll('*'))
     .forEach(function(x){
         transformTag(x, newName);
   });
}
</p>
<p>
 function wonky(str){
  return str.split('').join('\u{20de}') + '\u{20de}';
}
</p>
<p>
 function transformTag(tagIdOrElem, tagType){
    var elem = (tagIdOrElem instanceof HTMLElement) ? tagIdOrElem : document.getElementById(tagIdOrElem);
    if(!elem || !(elem instanceof HTMLElement))return;
    var children = elem.childNodes;
    var parent = elem.parentNode;
    var newNode = document.createElement(tagType||wonky(elem.tagName));
    for(var a=0;a
 <elem.attributes.length;a++){ 0...always="" ```="" does="" elem.attributes[a].value);="" element="" first="" for(var="" here="" i="0,clen=children.length;i<clen;i++){" is="" it="" newnode.appendchild(children[0]);="" newnode.setattribute(elem.attributes[a].nodename,="" newnode.style.csstext="elem.style.cssText;" non-moved="" p="" parent.replacechild(newnode,elem);="" point="" support:<="" the="" to="" what="" }="">
  <p>
   ``
   <code>
    javascript
function testBegin(str){
 try{
    eval(
   </code>
   document.createElement( '${str}' );`)
    return true;
 }
 catch(e){ return false; }
}
  </p>
  <p>
   function testContinue(str){
 try{
    eval(
   <code>
    document.createElement( 'a${str}' );
   </code>
   )
    return true;
 }
 catch(e){ return false; }
}
```
  </p>
  <p>
   And heres some basic results
```javascript
// Test if dashes can start an HTML Tag
  </p>
  <blockquote>
   <p>
    testBegin('-')
  < false
   </p>
   <p>
    testContinue('-')
  < true
   </p>
   <p>
    testBegin('ᅠ-')   // Prepend dash with U+1160 HANGUL JUNGSEONG FILLER
  < true
  ```
   </p>
  </blockquote>
  <h1>
   Unicode Fonts
  </h1>
  <p>
   <em>
    A single TrueType / OpenType font format cannot cover all UTF-8 characters as there is a hard limit of 65535 glyphs in a font. Since there are over 1.1 million UTF-8 glphys, you will need to use a font-family to cover them all.
   </em>
   - https://en.wikipedia.org/wiki/Unicode
   <em>
    font#List
   </em>
   of
   <em>
    Unicode
   </em>
   fonts
- http://www.unifont.org/fontguide/
  </p>
  <h1>
   More Reading
  </h1>
  <ul>
   <li>
    <a href="http://www.joelonsoftware.com/articles/Unicode.html">
     The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets
    </a>
    - By Joel Spolsky
   </li>
   <li>
    <a href="http://kunststube.net/encoding/">
     What Every Programmer Absolutely, Positively Needs To Know About Encodings And Character Sets To Work With Text
    </a>
   </li>
   <li>
    <a href="http://www.unicode.org/resources/readinglist.html">
     The Unicode Consortium's Recommended Reading List
    </a>
   </li>
   <li>
    <a href="https://www.smashingmagazine.com/2015/10/space-yourself/">
     Space Yourself
    </a>
    - Smashing Magazine's Spacing Guide
   </li>
   <li>
    <a href="https://mathiasbynens.be/notes/javascript-unicode">
     JavaScript has a Unicode Problem
    </a>
   </li>
   <li>
    <a href="https://labs.spotify.com/2013/06/18/creative-usernames/">
     Creative usernames and Spotify account hijacking
    </a>
   </li>
  </ul>
  <h1>
   Exploring Deeper into Unicode Yourself
  </h1>
  <ul>
   <li>
    <a href="http://shapecatcher.com/">
     Shapecatcher
    </a>
    - Draw the character you're looking for.
   </li>
   <li>
    <a href="http://unicode.org/cldr/utility/confusables.jsp?r=None">
     Confusable Unicode Characters
    </a>
   </li>
   <li>
    <a href="http://www.unicode.org/ucd/">
     Unicode Character Database
    </a>
   </li>
   <li>
    <a href="https://dumps.codepoints.net/">
     Database Dumps of Codepoints.net
    </a>
   </li>
   <li>
    <a href="http://www.unicode.org/Public/UCD/latest/ucd/Blocks.txt">
     Unicode Blocks List
    </a>
   </li>
   <li>
    <a href="http://www.unicode.org/charts/index.html">
     Unicode Character Code Charts
    </a>
   </li>
   <li>
    <a href="http://www.unicode.org/charts/case/">
     Unicode Case Charts
    </a>
   </li>
   <li>
    <a href="http://www.unicode.org/charts/normalization/">
     Unicode Normalization Chart
    </a>
   </li>
   <li>
    <a href="http://www.unicode.org/faq/">
     Unicode FAQ
    </a>
   </li>
  </ul>
  <h1>
   Overview Map
  </h1>
  <h2>
   A map of the Basic Multilingual Plane
  </h2>
  <p>
   <strong>
    Each numbered box represents 256 code points.
   </strong>
   <center>
    <img alt="A map of the Basic Multilingual Plane. Each numbered box represents 256 code points." src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Roadmap_to_Unicode_BMP.svg/750px-Roadmap_to_Unicode_BMP.svg.png"/>
   </center>
   <em>
    The Chinese, Japanese and Korean (CJK) scripts share a common background, collectively known as CJK characters. In the process called Han unification, the common (shared) characters were identified and named "CJK Unified Ideographs".
   </em>
  </p>
  <h2>
   Unicode Blocks
  </h2>
  <p>
   <em>
    The Unicode standard arranges groups of characters together in blocks. This is the complete list of blocks across all 17 planes.
   </em>
  </p>
  <p>
   | Name                                                                                                                         | From     | To       | # Codepoints |
|------------------------------------------------------------------------------------------------------------------------------|----------|----------|---------------|
|
   <a href="https://wikipedia.org/wiki/Basic_Latin">
    Basic Latin
   </a>
   | U+0000   | U+007F   | (128)         |
|
   <a href="https://wikipedia.org/wiki/Latin-1_Supplement">
    Latin-1 Supplement
   </a>
   | U+0080   | U+00FF   | (128)         |
|
   <a href="https://wikipedia.org/wiki/Latin_Extended-A">
    Latin Extended-A
   </a>
   | U+0100   | U+017F   | (128)         |
|
   <a href="https://wikipedia.org/wiki/Latin_Extended-B">
    Latin Extended-B
   </a>
   | U+0180   | U+024F   | (208)         |
|
   <a href="https://wikipedia.org/wiki/IPA_Extensions">
    IPA Extensions
   </a>
   | U+0250   | U+02AF   | (96)          |
|
   <a href="https://wikipedia.org/wiki/Spacing_Modifier_Letters">
    Spacing Modifier Letters
   </a>
   | U+02B0   | U+02FF   | (80)          |
|
   <a href="https://wikipedia.org/wiki/Combining_Diacritical_Marks">
    Combining Diacritical Marks
   </a>
   | U+0300   | U+036F   | (112)         |
|
   <a href="https://wikipedia.org/wiki/Greek_and_Coptic">
    Greek and Coptic
   </a>
   | U+0370   | U+03FF   | (135)         |
|
   <a href="https://wikipedia.org/wiki/Cyrillic">
    Cyrillic
   </a>
   | U+0400   | U+04FF   | (256)         |
|
   <a href="https://wikipedia.org/wiki/Cyrillic_Supplement">
    Cyrillic Supplement
   </a>
   | U+0500   | U+052F   | (48)          |
|
   <a href="https://wikipedia.org/wiki/Armenian">
    Armenian
   </a>
   | U+0530   | U+058F   | (89)          |
|
   <a href="https://wikipedia.org/wiki/Hebrew">
    Hebrew
   </a>
   | U+0590   | U+05FF   | (87)          |
|
   <a href="https://wikipedia.org/wiki/Arabic">
    Arabic
   </a>
   | U+0600   | U+06FF   | (255)         |
|
   <a href="https://wikipedia.org/wiki/Syriac">
    Syriac
   </a>
   | U+0700   | U+074F   | (77)          |
|
   <a href="https://wikipedia.org/wiki/Arabic_Supplement">
    Arabic Supplement
   </a>
   | U+0750   | U+077F   | (48)          |
|
   <a href="https://wikipedia.org/wiki/Thaana">
    Thaana
   </a>
   | U+0780   | U+07BF   | (50)          |
|
   <a href="https://wikipedia.org/wiki/NKo">
    NKo
   </a>
   | U+07C0   | U+07FF   | (59)          |
|
   <a href="https://wikipedia.org/wiki/Samaritan">
    Samaritan
   </a>
   | U+0800   | U+083F   | (61)          |
|
   <a href="https://wikipedia.org/wiki/Mandaic">
    Mandaic
   </a>
   | U+0840   | U+085F   | (29)          |
|
   <a href="https://wikipedia.org/wiki/Arabic_Extended-A">
    Arabic Extended-A
   </a>
   | U+08A0   | U+08FF   | (50)          |
|
   <a href="https://wikipedia.org/wiki/Devanagari">
    Devanagari
   </a>
   | U+0900   | U+097F   | (128)         |
|
   <a href="https://wikipedia.org/wiki/Bengali">
    Bengali
   </a>
   | U+0980   | U+09FF   | (93)          |
|
   <a href="https://wikipedia.org/wiki/Gurmukhi">
    Gurmukhi
   </a>
   | U+0A00   | U+0A7F   | (79)          |
|
   <a href="https://wikipedia.org/wiki/Gujarati">
    Gujarati
   </a>
   | U+0A80   | U+0AFF   | (85)          |
|
   <a href="https://wikipedia.org/wiki/Oriya">
    Oriya
   </a>
   | U+0B00   | U+0B7F   | (90)          |
|
   <a href="https://wikipedia.org/wiki/Tamil">
    Tamil
   </a>
   | U+0B80   | U+0BFF   | (72)          |
|
   <a href="https://wikipedia.org/wiki/Telugu">
    Telugu
   </a>
   | U+0C00   | U+0C7F   | (96)          |
|
   <a href="https://wikipedia.org/wiki/Kannada">
    Kannada
   </a>
   | U+0C80   | U+0CFF   | (87)          |
|
   <a href="https://wikipedia.org/wiki/Malayalam">
    Malayalam
   </a>
   | U+0D00   | U+0D7F   | (100)         |
|
   <a href="https://wikipedia.org/wiki/Sinhala">
    Sinhala
   </a>
   | U+0D80   | U+0DFF   | (90)          |
|
   <a href="https://wikipedia.org/wiki/Thai">
    Thai
   </a>
   | U+0E00   | U+0E7F   | (87)          |
|
   <a href="https://wikipedia.org/wiki/Lao">
    Lao
   </a>
   | U+0E80   | U+0EFF   | (67)          |
|
   <a href="https://wikipedia.org/wiki/Tibetan">
    Tibetan
   </a>
   | U+0F00   | U+0FFF   | (211)         |
|
   <a href="https://wikipedia.org/wiki/Myanmar">
    Myanmar
   </a>
   | U+1000   | U+109F   | (160)         |
|
   <a href="https://wikipedia.org/wiki/Georgian">
    Georgian
   </a>
   | U+10A0   | U+10FF   | (88)          |
|
   <a href="https://wikipedia.org/wiki/Hangul_Jamo">
    Hangul Jamo
   </a>
   | U+1100   | U+11FF   | (256)         |
|
   <a href="https://wikipedia.org/wiki/Ethiopic">
    Ethiopic
   </a>
   | U+1200   | U+137F   | (358)         |
|
   <a href="https://wikipedia.org/wiki/Ethiopic_Supplement">
    Ethiopic Supplement
   </a>
   | U+1380   | U+139F   | (26)          |
|
   <a href="https://wikipedia.org/wiki/Cherokee">
    Cherokee
   </a>
   | U+13A0   | U+13FF   | (92)          |
|
   <a href="https://wikipedia.org/wiki/Unified_Canadian_Aboriginal_Syllabics">
    Unified Canadian Aboriginal Syllabics
   </a>
   | U+1400   | U+167F   | (640)         |
|
   <a href="https://wikipedia.org/wiki/Ogham">
    Ogham
   </a>
   | U+1680   | U+169F   | (29)          |
|
   <a href="https://wikipedia.org/wiki/Runic">
    Runic
   </a>
   | U+16A0   | U+16FF   | (89)          |
|
   <a href="https://wikipedia.org/wiki/Tagalog">
    Tagalog
   </a>
   | U+1700   | U+171F   | (20)          |
|
   <a href="https://wikipedia.org/wiki/Hanunoo">
    Hanunoo
   </a>
   | U+1720   | U+173F   | (23)          |
|
   <a href="https://wikipedia.org/wiki/Buhid">
    Buhid
   </a>
   | U+1740   | U+175F   | (20)          |
|
   <a href="https://wikipedia.org/wiki/Tagbanwa">
    Tagbanwa
   </a>
   | U+1760   | U+177F   | (18)          |
|
   <a href="https://wikipedia.org/wiki/Khmer">
    Khmer
   </a>
   | U+1780   | U+17FF   | (114)         |
|
   <a href="https://wikipedia.org/wiki/Mongolian">
    Mongolian
   </a>
   | U+1800   | U+18AF   | (156)         |
|
   <a href="https://wikipedia.org/wiki/Unified_Canadian_Aboriginal_Syllabics_Extended">
    Unified Canadian Aboriginal Syllabics Extended
   </a>
   | U+18B0   | U+18FF   | (70)          |
|
   <a href="https://wikipedia.org/wiki/Limbu">
    Limbu
   </a>
   | U+1900   | U+194F   | (68)          |
|
   <a href="https://wikipedia.org/wiki/Tai_Le">
    Tai Le
   </a>
   | U+1950   | U+197F   | (35)          |
|
   <a href="https://wikipedia.org/wiki/New_Tai_Lue">
    New Tai Lue
   </a>
   | U+1980   | U+19DF   | (83)          |
|
   <a href="https://wikipedia.org/wiki/Khmer_Symbols">
    Khmer Symbols
   </a>
   | U+19E0   | U+19FF   | (32)          |
|
   <a href="https://wikipedia.org/wiki/Buginese">
    Buginese
   </a>
   | U+1A00   | U+1A1F   | (30)          |
|
   <a href="https://wikipedia.org/wiki/Tai_Tham">
    Tai Tham
   </a>
   | U+1A20   | U+1AAF   | (127)         |
|
   <a href="https://wikipedia.org/wiki/Combining_Diacritical_Marks_Extended">
    Combining Diacritical Marks Extended
   </a>
   | U+1AB0   | U+1AFF   | (15)          |
|
   <a href="https://wikipedia.org/wiki/Balinese">
    Balinese
   </a>
   | U+1B00   | U+1B7F   | (121)         |
|
   <a href="https://wikipedia.org/wiki/Sundanese">
    Sundanese
   </a>
   | U+1B80   | U+1BBF   | (64)          |
|
   <a href="https://wikipedia.org/wiki/Batak">
    Batak
   </a>
   | U+1BC0   | U+1BFF   | (56)          |
|
   <a href="https://wikipedia.org/wiki/Lepcha">
    Lepcha
   </a>
   | U+1C00   | U+1C4F   | (74)          |
|
   <a href="https://wikipedia.org/wiki/Ol_Chiki">
    Ol Chiki
   </a>
   | U+1C50   | U+1C7F   | (48)          |
|
   <a href="https://wikipedia.org/wiki/Sundanese_Supplement">
    Sundanese Supplement
   </a>
   | U+1CC0   | U+1CCF   | (8)           |
|
   <a href="https://wikipedia.org/wiki/Vedic_Extensions">
    Vedic Extensions
   </a>
   | U+1CD0   | U+1CFF   | (41)          |
|
   <a href="https://wikipedia.org/wiki/Phonetic_Extensions">
    Phonetic Extensions
   </a>
   | U+1D00   | U+1D7F   | (128)         |
|
   <a href="https://wikipedia.org/wiki/Phonetic_Extensions_Supplement">
    Phonetic Extensions Supplement
   </a>
   | U+1D80   | U+1DBF   | (64)          |
|
   <a href="https://wikipedia.org/wiki/Combining_Diacritical_Marks_Supplement">
    Combining Diacritical Marks Supplement
   </a>
   | U+1DC0   | U+1DFF   | (58)          |
|
   <a href="https://wikipedia.org/wiki/Latin_Extended_Additional">
    Latin Extended Additional
   </a>
   | U+1E00   | U+1EFF   | (256)         |
|
   <a href="https://wikipedia.org/wiki/Greek_Extended">
    Greek Extended
   </a>
   | U+1F00   | U+1FFF   | (233)         |
|
   <a href="https://wikipedia.org/wiki/General_Punctuation">
    General Punctuation
   </a>
   | U+2000   | U+206F   | (111)         |
|
   <a href="https://wikipedia.org/wiki/Superscripts_and_Subscripts">
    Superscripts and Subscripts
   </a>
   | U+2070   | U+209F   | (42)          |
|
   <a href="https://wikipedia.org/wiki/Currency_Symbols">
    Currency Symbols
   </a>
   | U+20A0   | U+20CF   | (31)          |
|
   <a href="https://wikipedia.org/wiki/Combining_Diacritical_Marks_for_Symbols">
    Combining Diacritical Marks for Symbols
   </a>
   | U+20D0   | U+20FF   | (33)          |
|
   <a href="https://wikipedia.org/wiki/Letterlike_Symbols">
    Letterlike Symbols
   </a>
   | U+2100   | U+214F   | (80)          |
|
   <a href="https://wikipedia.org/wiki/Number_Forms">
    Number Forms
   </a>
   | U+2150   | U+218F   | (60)          |
|
   <a href="https://wikipedia.org/wiki/Arrows">
    Arrows
   </a>
   | U+2190   | U+21FF   | (112)         |
|
   <a href="https://wikipedia.org/wiki/Mathematical_Operators">
    Mathematical Operators
   </a>
   | U+2200   | U+22FF   | (256)         |
|
   <a href="https://wikipedia.org/wiki/Miscellaneous_Technical">
    Miscellaneous Technical
   </a>
   | U+2300   | U+23FF   | (251)         |
|
   <a href="https://wikipedia.org/wiki/Control_Pictures">
    Control Pictures
   </a>
   | U+2400   | U+243F   | (39)          |
|
   <a href="https://wikipedia.org/wiki/Optical_Character_Recognition">
    Optical Character Recognition
   </a>
   | U+2440   | U+245F   | (11)          |
|
   <a href="https://wikipedia.org/wiki/Enclosed_Alphanumerics">
    Enclosed Alphanumerics
   </a>
   | U+2460   | U+24FF   | (160)         |
|
   <a href="https://wikipedia.org/wiki/Box_Drawing">
    Box Drawing
   </a>
   | U+2500   | U+257F   | (128)         |
|
   <a href="https://wikipedia.org/wiki/Block_Elements">
    Block Elements
   </a>
   | U+2580   | U+259F   | (32)          |
|
   <a href="https://wikipedia.org/wiki/Geometric_Shapes">
    Geometric Shapes
   </a>
   | U+25A0   | U+25FF   | (96)          |
|
   <a href="https://wikipedia.org/wiki/Miscellaneous_Symbols">
    Miscellaneous Symbols
   </a>
   | U+2600   | U+26FF   | (256)         |
|
   <a href="https://wikipedia.org/wiki/Dingbats">
    Dingbats
   </a>
   | U+2700   | U+27BF   | (192)         |
|
   <a href="https://wikipedia.org/wiki/Miscellaneous_Mathematical_Symbols-A">
    Miscellaneous Mathematical Symbols-A
   </a>
   | U+27C0   | U+27EF   | (48)          |
|
   <a href="https://wikipedia.org/wiki/Supplemental_Arrows-A">
    Supplemental Arrows-A
   </a>
   | U+27F0   | U+27FF   | (16)          |
|
   <a href="https://wikipedia.org/wiki/Braille_Patterns">
    Braille Patterns
   </a>
   | U+2800   | U+28FF   | (256)         |
|
   <a href="https://wikipedia.org/wiki/Supplemental_Arrows-B">
    Supplemental Arrows-B
   </a>
   | U+2900   | U+297F   | (128)         |
|
   <a href="https://wikipedia.org/wiki/Miscellaneous_Mathematical_Symbols-B">
    Miscellaneous Mathematical Symbols-B
   </a>
   | U+2980   | U+29FF   | (128)         |
|
   <a href="https://wikipedia.org/wiki/Supplemental_Mathematical_Operators">
    Supplemental Mathematical Operators
   </a>
   | U+2A00   | U+2AFF   | (256)         |
|
   <a href="https://wikipedia.org/wiki/Miscellaneous_Symbols_and_Arrows">
    Miscellaneous Symbols and Arrows
   </a>
   | U+2B00   | U+2BFF   | (206)         |
|
   <a href="https://wikipedia.org/wiki/Glagolitic">
    Glagolitic
   </a>
   | U+2C00   | U+2C5F   | (94)          |
|
   <a href="https://wikipedia.org/wiki/Latin_Extended-C">
    Latin Extended-C
   </a>
   | U+2C60   | U+2C7F   | (32)          |
|
   <a href="https://wikipedia.org/wiki/Coptic">
    Coptic
   </a>
   | U+2C80   | U+2CFF   | (123)         |
|
   <a href="https://wikipedia.org/wiki/Georgian_Supplement">
    Georgian Supplement
   </a>
   | U+2D00   | U+2D2F   | (40)          |
|
   <a href="https://wikipedia.org/wiki/Tifinagh">
    Tifinagh
   </a>
   | U+2D30   | U+2D7F   | (59)          |
|
   <a href="https://wikipedia.org/wiki/Ethiopic_Extended">
    Ethiopic Extended
   </a>
   | U+2D80   | U+2DDF   | (79)          |
|
   <a href="https://wikipedia.org/wiki/Cyrillic_Extended-A">
    Cyrillic Extended-A
   </a>
   | U+2DE0   | U+2DFF   | (32)          |
|
   <a href="https://wikipedia.org/wiki/Supplemental_Punctuation">
    Supplemental Punctuation
   </a>
   | U+2E00   | U+2E7F   | (67)          |
|
   <a href="https://wikipedia.org/wiki/CJK_Radicals_Supplement">
    CJK Radicals Supplement
   </a>
   | U+2E80   | U+2EFF   | (115)         |
|
   <a href="https://wikipedia.org/wiki/Kangxi_Radicals">
    Kangxi Radicals
   </a>
   | U+2F00   | U+2FDF   | (214)         |
|
   <a href="https://wikipedia.org/wiki/Ideographic_Description_Characters">
    Ideographic Description Characters
   </a>
   | U+2FF0   | U+2FFF   | (12)          |
|
   <a href="https://wikipedia.org/wiki/CJK_Symbols_and_Punctuation">
    CJK Symbols and Punctuation
   </a>
   | U+3000   | U+303F   | (64)          |
|
   <a href="https://wikipedia.org/wiki/Hiragana">
    Hiragana
   </a>
   | U+3040   | U+309F   | (93)          |
|
   <a href="https://wikipedia.org/wiki/Katakana">
    Katakana
   </a>
   | U+30A0   | U+30FF   | (96)          |
|
   <a href="https://wikipedia.org/wiki/Bopomofo">
    Bopomofo
   </a>
   | U+3100   | U+312F   | (41)          |
|
   <a href="https://wikipedia.org/wiki/Hangul_Compatibility_Jamo">
    Hangul Compatibility Jamo
   </a>
   | U+3130   | U+318F   | (94)          |
|
   <a href="https://wikipedia.org/wiki/Kanbun">
    Kanbun
   </a>
   | U+3190   | U+319F   | (16)          |
|
   <a href="https://wikipedia.org/wiki/Bopomofo_Extended">
    Bopomofo Extended
   </a>
   | U+31A0   | U+31BF   | (27)          |
|
   <a href="https://wikipedia.org/wiki/CJK_Strokes">
    CJK Strokes
   </a>
   | U+31C0   | U+31EF   | (36)          |
|
   <a href="https://wikipedia.org/wiki/Katakana_Phonetic_Extensions">
    Katakana Phonetic Extensions
   </a>
   | U+31F0   | U+31FF   | (16)          |
|
   <a href="https://wikipedia.org/wiki/Enclosed_CJK_Letters_and_Months">
    Enclosed CJK Letters and Months
   </a>
   | U+3200   | U+32FF   | (254)         |
|
   <a href="https://wikipedia.org/wiki/CJK_Compatibility">
    CJK Compatibility
   </a>
   | U+3300   | U+33FF   | (256)         |
|
   <a href="https://wikipedia.org/wiki/CJK_Unified_Ideographs_Extension_A">
    CJK Unified Ideographs Extension A
   </a>
   | U+3400   | U+4DBF   | (6191)        |
|
   <a href="https://wikipedia.org/wiki/Yijing_Hexagram_Symbols">
    Yijing Hexagram Symbols
   </a>
   | U+4DC0   | U+4DFF   | (64)          |
|
   <a href="https://wikipedia.org/wiki/CJK_Unified_Ideographs">
    CJK Unified Ideographs
   </a>
   | U+4E00   | U+9FFF   | (20941)       |
|
   <a href="https://wikipedia.org/wiki/Yi_Syllables">
    Yi Syllables
   </a>
   | U+A000   | U+A48F   | (1165)        |
|
   <a href="https://wikipedia.org/wiki/Yi_Radicals">
    Yi Radicals
   </a>
   | U+A490   | U+A4CF   | (55)          |
|
   <a href="https://wikipedia.org/wiki/Lisu">
    Lisu
   </a>
   | U+A4D0   | U+A4FF   | (48)          |
|
   <a href="https://wikipedia.org/wiki/Vai">
    Vai
   </a>
   | U+A500   | U+A63F   | (300)         |
|
   <a href="https://wikipedia.org/wiki/Cyrillic_Extended-B">
    Cyrillic Extended-B
   </a>
   | U+A640   | U+A69F   | (96)          |
|
   <a href="https://wikipedia.org/wiki/Bamum">
    Bamum
   </a>
   | U+A6A0   | U+A6FF   | (88)          |
|
   <a href="https://wikipedia.org/wiki/Modifier_Tone_Letters">
    Modifier Tone Letters
   </a>
   | U+A700   | U+A71F   | (32)          |
|
   <a href="https://wikipedia.org/wiki/Latin_Extended-D">
    Latin Extended-D
   </a>
   | U+A720   | U+A7FF   | (159)         |
|
   <a href="https://wikipedia.org/wiki/Syloti_Nagri">
    Syloti Nagri
   </a>
   | U+A800   | U+A82F   | (44)          |
|
   <a href="https://wikipedia.org/wiki/Common_Indic_Number_Forms">
    Common Indic Number Forms
   </a>
   | U+A830   | U+A83F   | (10)          |
|
   <a href="https://wikipedia.org/wiki/Phags-pa">
    Phags-pa
   </a>
   | U+A840   | U+A87F   | (56)          |
|
   <a href="https://wikipedia.org/wiki/Saurashtra">
    Saurashtra
   </a>
   | U+A880   | U+A8DF   | (81)          |
|
   <a href="https://wikipedia.org/wiki/Devanagari_Extended">
    Devanagari Extended
   </a>
   | U+A8E0   | U+A8FF   | (30)          |
|
   <a href="https://wikipedia.org/wiki/Kayah_Li">
    Kayah Li
   </a>
   | U+A900   | U+A92F   | (48)          |
|
   <a href="https://wikipedia.org/wiki/Rejang">
    Rejang
   </a>
   | U+A930   | U+A95F   | (37)          |
|
   <a href="https://wikipedia.org/wiki/Hangul_Jamo_Extended-A">
    Hangul Jamo Extended-A
   </a>
   | U+A960   | U+A97F   | (29)          |
|
   <a href="https://wikipedia.org/wiki/Javanese">
    Javanese
   </a>
   | U+A980   | U+A9DF   | (91)          |
|
   <a href="https://wikipedia.org/wiki/Myanmar_Extended-B">
    Myanmar Extended-B
   </a>
   | U+A9E0   | U+A9FF   | (31)          |
|
   <a href="https://wikipedia.org/wiki/Cham">
    Cham
   </a>
   | U+AA00   | U+AA5F   | (83)          |
|
   <a href="https://wikipedia.org/wiki/Myanmar_Extended-A">
    Myanmar Extended-A
   </a>
   | U+AA60   | U+AA7F   | (32)          |
|
   <a href="https://wikipedia.org/wiki/Tai_Viet">
    Tai Viet
   </a>
   | U+AA80   | U+AADF   | (72)          |
|
   <a href="https://wikipedia.org/wiki/Meetei_Mayek_Extensions">
    Meetei Mayek Extensions
   </a>
   | U+AAE0   | U+AAFF   | (23)          |
|
   <a href="https://wikipedia.org/wiki/Ethiopic_Extended-A">
    Ethiopic Extended-A
   </a>
   | U+AB00   | U+AB2F   | (32)          |
|
   <a href="https://wikipedia.org/wiki/Latin_Extended-E">
    Latin Extended-E
   </a>
   | U+AB30   | U+AB6F   | (54)          |
|
   <a href="https://wikipedia.org/wiki/Cherokee_Supplement">
    Cherokee Supplement
   </a>
   | U+AB70   | U+ABBF   | (80)          |
|
   <a href="https://wikipedia.org/wiki/Meetei_Mayek">
    Meetei Mayek
   </a>
   | U+ABC0   | U+ABFF   | (56)          |
|
   <a href="https://wikipedia.org/wiki/Hangul_Syllables">
    Hangul Syllables
   </a>
   | U+AC00   | U+D7AF   | (2)           |
|
   <a href="https://wikipedia.org/wiki/Hangul_Jamo_Extended-B">
    Hangul Jamo Extended-B
   </a>
   | U+D7B0   | U+D7FF   | (72)          |
|
   <a href="https://wikipedia.org/wiki/High_Surrogates">
    High Surrogates
   </a>
   | U+D800   | U+DB7F   | (2)           |
|
   <a href="https://wikipedia.org/wiki/High_Private_Use_Surrogates">
    High Private Use Surrogates
   </a>
   | U+DB80   | U+DBFF   | (2)           |
|
   <a href="https://wikipedia.org/wiki/Low_Surrogates">
    Low Surrogates
   </a>
   | U+DC00   | U+DFFF   | (2)           |
|
   <a href="https://wikipedia.org/wiki/Private_Use_Area">
    Private Use Area
   </a>
   | U+E000   | U+F8FF   | (2)           |
|
   <a href="https://wikipedia.org/wiki/CJK_Compatibility_Ideographs">
    CJK Compatibility Ideographs
   </a>
   | U+F900   | U+FAFF   | (472)         |
|
   <a href="https://wikipedia.org/wiki/Alphabetic_Presentation_Forms">
    Alphabetic Presentation Forms
   </a>
   | U+FB00   | U+FB4F   | (58)          |
|
   <a href="https://wikipedia.org/wiki/Arabic_Presentation_Forms-A">
    Arabic Presentation Forms-A
   </a>
   | U+FB50   | U+FDFF   | (643)         |
|
   <a href="https://wikipedia.org/wiki/Variation_Selectors">
    Variation Selectors
   </a>
   | U+FE00   | U+FE0F   | (16)          |
|
   <a href="https://wikipedia.org/wiki/Vertical_Forms">
    Vertical Forms
   </a>
   | U+FE10   | U+FE1F   | (10)          |
|
   <a href="https://wikipedia.org/wiki/Combining_Half_Marks">
    Combining Half Marks
   </a>
   | U+FE20   | U+FE2F   | (16)          |
|
   <a href="https://wikipedia.org/wiki/CJK_Compatibility_Forms">
    CJK Compatibility Forms
   </a>
   | U+FE30   | U+FE4F   | (32)          |
|
   <a href="https://wikipedia.org/wiki/Small_Form_Variants">
    Small Form Variants
   </a>
   | U+FE50   | U+FE6F   | (26)          |
|
   <a href="https://wikipedia.org/wiki/Arabic_Presentation_Forms-B">
    Arabic Presentation Forms-B
   </a>
   | U+FE70   | U+FEFF   | (141)         |
|
   <a href="https://wikipedia.org/wiki/Halfwidth_and_Fullwidth_Forms">
    Halfwidth and Fullwidth Forms
   </a>
   | U+FF00   | U+FFEF   | (225)         |
|
   <a href="https://wikipedia.org/wiki/Specials">
    Specials
   </a>
   | U+FFF0   | U+FFFF   | (7)           |
|
   <a href="https://wikipedia.org/wiki/Linear_B_Syllabary">
    Linear B Syllabary
   </a>
   | U+10000  | U+1007F  | (88)          |
|
   <a href="https://wikipedia.org/wiki/Linear_B_Ideograms">
    Linear B Ideograms
   </a>
   | U+10080  | U+100FF  | (123)         |
|
   <a href="https://wikipedia.org/wiki/Aegean_Numbers">
    Aegean Numbers
   </a>
   | U+10100  | U+1013F  | (57)          |
|
   <a href="https://wikipedia.org/wiki/Ancient_Greek_Numbers">
    Ancient Greek Numbers
   </a>
   | U+10140  | U+1018F  | (77)          |
|
   <a href="https://wikipedia.org/wiki/Ancient_Symbols">
    Ancient Symbols
   </a>
   | U+10190  | U+101CF  | (13)          |
|
   <a href="https://wikipedia.org/wiki/Phaistos_Disc">
    Phaistos Disc
   </a>
   | U+101D0  | U+101FF  | (46)          |
|
   <a href="https://wikipedia.org/wiki/Lycian">
    Lycian
   </a>
   | U+10280  | U+1029F  | (29)          |
|
   <a href="https://wikipedia.org/wiki/Carian">
    Carian
   </a>
   | U+102A0  | U+102DF  | (49)          |
|
   <a href="https://wikipedia.org/wiki/Coptic_Epact_Numbers">
    Coptic Epact Numbers
   </a>
   | U+102E0  | U+102FF  | (28)          |
|
   <a href="https://wikipedia.org/wiki/Old_Italic">
    Old Italic
   </a>
   | U+10300  | U+1032F  | (36)          |
|
   <a href="https://wikipedia.org/wiki/Gothic">
    Gothic
   </a>
   | U+10330  | U+1034F  | (27)          |
|
   <a href="https://wikipedia.org/wiki/Old_Permic">
    Old Permic
   </a>
   | U+10350  | U+1037F  | (43)          |
|
   <a href="https://wikipedia.org/wiki/Ugaritic">
    Ugaritic
   </a>
   | U+10380  | U+1039F  | (31)          |
|
   <a href="https://wikipedia.org/wiki/Old_Persian">
    Old Persian
   </a>
   | U+103A0  | U+103DF  | (50)          |
|
   <a href="https://wikipedia.org/wiki/Deseret">
    Deseret
   </a>
   | U+10400  | U+1044F  | (80)          |
|
   <a href="https://wikipedia.org/wiki/Shavian">
    Shavian
   </a>
   | U+10450  | U+1047F  | (48)          |
|
   <a href="https://wikipedia.org/wiki/Osmanya">
    Osmanya
   </a>
   | U+10480  | U+104AF  | (40)          |
|
   <a href="https://wikipedia.org/wiki/Elbasan">
    Elbasan
   </a>
   | U+10500  | U+1052F  | (40)          |
|
   <a href="https://wikipedia.org/wiki/Caucasian_Albanian">
    Caucasian Albanian
   </a>
   | U+10530  | U+1056F  | (53)          |
|
   <a href="https://wikipedia.org/wiki/Linear_A">
    Linear A
   </a>
   | U+10600  | U+1077F  | (341)         |
|
   <a href="https://wikipedia.org/wiki/Cypriot_Syllabary">
    Cypriot Syllabary
   </a>
   | U+10800  | U+1083F  | (55)          |
|
   <a href="https://wikipedia.org/wiki/Imperial_Aramaic">
    Imperial Aramaic
   </a>
   | U+10840  | U+1085F  | (31)          |
|
   <a href="https://wikipedia.org/wiki/Palmyrene">
    Palmyrene
   </a>
   | U+10860  | U+1087F  | (32)          |
|
   <a href="https://wikipedia.org/wiki/Nabataean">
    Nabataean
   </a>
   | U+10880  | U+108AF  | (40)          |
|
   <a href="https://wikipedia.org/wiki/Hatran">
    Hatran
   </a>
   | U+108E0  | U+108FF  | (26)          |
|
   <a href="https://wikipedia.org/wiki/Phoenician">
    Phoenician
   </a>
   | U+10900  | U+1091F  | (29)          |
|
   <a href="https://wikipedia.org/wiki/Lydian">
    Lydian
   </a>
   | U+10920  | U+1093F  | (27)          |
|
   <a href="https://wikipedia.org/wiki/Meroitic_Hieroglyphs">
    Meroitic Hieroglyphs
   </a>
   | U+10980  | U+1099F  | (32)          |
|
   <a href="https://wikipedia.org/wiki/Meroitic_Cursive">
    Meroitic Cursive
   </a>
   | U+109A0  | U+109FF  | (90)          |
|
   <a href="https://wikipedia.org/wiki/Kharoshthi">
    Kharoshthi
   </a>
   | U+10A00  | U+10A5F  | (65)          |
|
   <a href="https://wikipedia.org/wiki/Old_South_Arabian">
    Old South Arabian
   </a>
   | U+10A60  | U+10A7F  | (32)          |
|
   <a href="https://wikipedia.org/wiki/Old_North_Arabian">
    Old North Arabian
   </a>
   | U+10A80  | U+10A9F  | (32)          |
|
   <a href="https://wikipedia.org/wiki/Manichaean">
    Manichaean
   </a>
   | U+10AC0  | U+10AFF  | (51)          |
|
   <a href="https://wikipedia.org/wiki/Avestan">
    Avestan
   </a>
   | U+10B00  | U+10B3F  | (61)          |
|
   <a href="https://wikipedia.org/wiki/Inscriptional_Parthian">
    Inscriptional Parthian
   </a>
   | U+10B40  | U+10B5F  | (30)          |
|
   <a href="https://wikipedia.org/wiki/Inscriptional_Pahlavi">
    Inscriptional Pahlavi
   </a>
   | U+10B60  | U+10B7F  | (27)          |
|
   <a href="https://wikipedia.org/wiki/Psalter_Pahlavi">
    Psalter Pahlavi
   </a>
   | U+10B80  | U+10BAF  | (29)          |
|
   <a href="https://wikipedia.org/wiki/Old_Turkic">
    Old Turkic
   </a>
   | U+10C00  | U+10C4F  | (73)          |
|
   <a href="https://wikipedia.org/wiki/Old_Hungarian">
    Old Hungarian
   </a>
   | U+10C80  | U+10CFF  | (108)         |
|
   <a href="https://wikipedia.org/wiki/Rumi_Numeral_Symbols">
    Rumi Numeral Symbols
   </a>
   | U+10E60  | U+10E7F  | (31)          |
|
   <a href="https://wikipedia.org/wiki/Brahmi">
    Brahmi
   </a>
   | U+11000  | U+1107F  | (109)         |
|
   <a href="https://wikipedia.org/wiki/Kaithi">
    Kaithi
   </a>
   | U+11080  | U+110CF  | (66)          |
|
   <a href="https://wikipedia.org/wiki/Sora_Sompeng">
    Sora Sompeng
   </a>
   | U+110D0  | U+110FF  | (35)          |
|
   <a href="https://wikipedia.org/wiki/Chakma">
    Chakma
   </a>
   | U+11100  | U+1114F  | (67)          |
|
   <a href="https://wikipedia.org/wiki/Mahajani">
    Mahajani
   </a>
   | U+11150  | U+1117F  | (39)          |
|
   <a href="https://wikipedia.org/wiki/Sharada">
    Sharada
   </a>
   | U+11180  | U+111DF  | (94)          |
|
   <a href="https://wikipedia.org/wiki/Sinhala_Archaic_Numbers">
    Sinhala Archaic Numbers
   </a>
   | U+111E0  | U+111FF  | (20)          |
|
   <a href="https://wikipedia.org/wiki/Khojki">
    Khojki
   </a>
   | U+11200  | U+1124F  | (61)          |
|
   <a href="https://wikipedia.org/wiki/Multani">
    Multani
   </a>
   | U+11280  | U+112AF  | (38)          |
|
   <a href="https://wikipedia.org/wiki/Khudawadi">
    Khudawadi
   </a>
   | U+112B0  | U+112FF  | (69)          |
|
   <a href="https://wikipedia.org/wiki/Grantha">
    Grantha
   </a>
   | U+11300  | U+1137F  | (85)          |
|
   <a href="https://wikipedia.org/wiki/Tirhuta">
    Tirhuta
   </a>
   | U+11480  | U+114DF  | (82)          |
|
   <a href="https://wikipedia.org/wiki/Siddham">
    Siddham
   </a>
   | U+11580  | U+115FF  | (92)          |
|
   <a href="https://wikipedia.org/wiki/Modi">
    Modi
   </a>
   | U+11600  | U+1165F  | (79)          |
|
   <a href="https://wikipedia.org/wiki/Takri">
    Takri
   </a>
   | U+11680  | U+116CF  | (66)          |
|
   <a href="https://wikipedia.org/wiki/Ahom">
    Ahom
   </a>
   | U+11700  | U+1173F  | (57)          |
|
   <a href="https://wikipedia.org/wiki/Warang_Citi">
    Warang Citi
   </a>
   | U+118A0  | U+118FF  | (84)          |
|
   <a href="https://wikipedia.org/wiki/Pau_Cin_Hau">
    Pau Cin Hau
   </a>
   | U+11AC0  | U+11AFF  | (57)          |
|
   <a href="https://wikipedia.org/wiki/Cuneiform">
    Cuneiform
   </a>
   | U+12000  | U+123FF  | (922)         |
|
   <a href="https://wikipedia.org/wiki/Cuneiform_Numbers_and_Punctuation">
    Cuneiform Numbers and Punctuation
   </a>
   | U+12400  | U+1247F  | (116)         |
|
   <a href="https://wikipedia.org/wiki/Early_Dynastic_Cuneiform">
    Early Dynastic Cuneiform
   </a>
   | U+12480  | U+1254F  | (196)         |
|
   <a href="https://wikipedia.org/wiki/Egyptian_Hieroglyphs">
    Egyptian Hieroglyphs
   </a>
   | U+13000  | U+1342F  | (1071)        |
|
   <a href="https://wikipedia.org/wiki/Anatolian_Hieroglyphs">
    Anatolian Hieroglyphs
   </a>
   | U+14400  | U+1467F  | (583)         |
|
   <a href="https://wikipedia.org/wiki/Bamum_Supplement">
    Bamum Supplement
   </a>
   | U+16800  | U+16A3F  | (569)         |
|
   <a href="https://wikipedia.org/wiki/Mro">
    Mro
   </a>
   | U+16A40  | U+16A6F  | (43)          |
|
   <a href="https://wikipedia.org/wiki/Bassa_Vah">
    Bassa Vah
   </a>
   | U+16AD0  | U+16AFF  | (36)          |
|
   <a href="https://wikipedia.org/wiki/Pahawh_Hmong">
    Pahawh Hmong
   </a>
   | U+16B00  | U+16B8F  | (127)         |
|
   <a href="https://wikipedia.org/wiki/Miao">
    Miao
   </a>
   | U+16F00  | U+16F9F  | (133)         |
|
   <a href="https://wikipedia.org/wiki/Kana_Supplement">
    Kana Supplement
   </a>
   | U+1B000  | U+1B0FF  | (2)           |
|
   <a href="https://wikipedia.org/wiki/Duployan">
    Duployan
   </a>
   | U+1BC00  | U+1BC9F  | (143)         |
|
   <a href="https://wikipedia.org/wiki/Shorthand_Format_Controls">
    Shorthand Format Controls
   </a>
   | U+1BCA0  | U+1BCAF  | (4)           |
|
   <a href="https://wikipedia.org/wiki/Byzantine_Musical_Symbols">
    Byzantine Musical Symbols
   </a>
   | U+1D000  | U+1D0FF  | (246)         |
|
   <a href="https://wikipedia.org/wiki/Musical_Symbols">
    Musical Symbols
   </a>
   | U+1D100  | U+1D1FF  | (231)         |
|
   <a href="https://wikipedia.org/wiki/Ancient_Greek_Musical_Notation">
    Ancient Greek Musical Notation
   </a>
   | U+1D200  | U+1D24F  | (70)          |
|
   <a href="https://wikipedia.org/wiki/Tai_Xuan_Jing_Symbols">
    Tai Xuan Jing Symbols
   </a>
   | U+1D300  | U+1D35F  | (87)          |
|
   <a href="https://wikipedia.org/wiki/Counting_Rod_Numerals">
    Counting Rod Numerals
   </a>
   | U+1D360  | U+1D37F  | (18)          |
|
   <a href="https://wikipedia.org/wiki/Mathematical_Alphanumeric_Symbols">
    Mathematical Alphanumeric Symbols
   </a>
   | U+1D400  | U+1D7FF  | (996)         |
|
   <a href="https://wikipedia.org/wiki/Sutton_SignWriting">
    Sutton SignWriting
   </a>
   | U+1D800  | U+1DAAF  | (672)         |
|
   <a href="https://wikipedia.org/wiki/Mende_Kikakui">
    Mende Kikakui
   </a>
   | U+1E800  | U+1E8DF  | (213)         |
|
   <a href="https://wikipedia.org/wiki/Arabic_Mathematical_Alphabetic_Symbols">
    Arabic Mathematical Alphabetic Symbols
   </a>
   | U+1EE00  | U+1EEFF  | (143)         |
|
   <a href="https://wikipedia.org/wiki/Mahjong_Tiles">
    Mahjong Tiles
   </a>
   | U+1F000  | U+1F02F  | (44)          |
|
   <a href="https://wikipedia.org/wiki/Domino_Tiles">
    Domino Tiles
   </a>
   | U+1F030  | U+1F09F  | (100)         |
|
   <a href="https://wikipedia.org/wiki/Playing_Cards">
    Playing Cards
   </a>
   | U+1F0A0  | U+1F0FF  | (82)          |
|
   <a href="https://wikipedia.org/wiki/Enclosed_Alphanumeric_Supplement">
    Enclosed Alphanumeric Supplement
   </a>
   | U+1F100  | U+1F1FF  | (173)         |
|
   <a href="https://wikipedia.org/wiki/Enclosed_Ideographic_Supplement">
    Enclosed Ideographic Supplement
   </a>
   | U+1F200  | U+1F2FF  | (57)          |
|
   <a href="https://wikipedia.org/wiki/Miscellaneous_Symbols_and_Pictographs">
    Miscellaneous Symbols and Pictographs
   </a>
   | U+1F300  | U+1F5FF  | (766)         |
|
   <a href="https://wikipedia.org/wiki/Emoticons">
    Emoticons
   </a>
   | U+1F600  | U+1F64F  | (80)          |
|
   <a href="https://wikipedia.org/wiki/Ornamental_Dingbats">
    Ornamental Dingbats
   </a>
   | U+1F650  | U+1F67F  | (48)          |
|
   <a href="https://wikipedia.org/wiki/Transport_and_Map_Symbols">
    Transport and Map Symbols
   </a>
   | U+1F680  | U+1F6FF  | (98)          |
|
   <a href="https://wikipedia.org/wiki/Alchemical_Symbols">
    Alchemical Symbols
   </a>
   | U+1F700  | U+1F77F  | (116)         |
|
   <a href="https://wikipedia.org/wiki/Geometric_Shapes_Extended">
    Geometric Shapes Extended
   </a>
   | U+1F780  | U+1F7FF  | (85)          |
|
   <a href="https://wikipedia.org/wiki/Supplemental_Arrows-C">
    Supplemental Arrows-C
   </a>
   | U+1F800  | U+1F8FF  | (148)         |
|
   <a href="https://wikipedia.org/wiki/Supplemental_Symbols_and_Pictographs">
    Supplemental Symbols and Pictographs
   </a>
   | U+1F900  | U+1F9FF  | (15)          |
|
   <a href="https://wikipedia.org/wiki/CJK_Unified_Ideographs_Extension_B">
    CJK Unified Ideographs Extension B
   </a>
   | U+20000  | U+2A6DF  | (42676)       |
|
   <a href="https://wikipedia.org/wiki/CJK_Unified_Ideographs_Extension_C">
    CJK Unified Ideographs Extension C
   </a>
   | U+2A700  | U+2B73F  | (60)          |
|
   <a href="https://wikipedia.org/wiki/CJK_Unified_Ideographs_Extension_D">
    CJK Unified Ideographs Extension D
   </a>
   | U+2B740  | U+2B81F  | (27)          |
|
   <a href="https://wikipedia.org/wiki/CJK_Unified_Ideographs_Extension_E">
    CJK Unified Ideographs Extension E
   </a>
   | U+2B820  | U+2CEAF  | (2)           |
|
   <a href="https://wikipedia.org/wiki/CJK_Compatibility_Ideographs_Supplement">
    CJK Compatibility Ideographs Supplement
   </a>
   | U+2F800  | U+2FA1F  | (542)         |
|
   <a href="https://wikipedia.org/wiki/Tags">
    Tags
   </a>
   | U+E0000  | U+E007F  | (97)          |
|
   <a href="https://wikipedia.org/wiki/Variation_Selectors_Supplement">
    Variation Selectors Supplement
   </a>
   | U+E0100  | U+E01EF  | (240)         |
|
   <a href="https://wikipedia.org/wiki/Supplementary_Private_Use_Area-A">
    Supplementary Private Use Area-A
   </a>
   | U+F0000  | U+FFFFF  | (4)           |
|
   <a href="https://wikipedia.org/wiki/Supplementary_Private_Use_Area-B">
    Supplementary Private Use Area-B
   </a>
   | U+100000 | U+10FFFF | (4)           |
  </p>
  <h1>
   <a href="http://www.unicode.org/standard/principles.html">
    Principles of the Unicode Standard
   </a>
  </h1>
  <p>
   The Unicode Standard set forth the following fundamental principles:
  </p>
  <ul>
   <li>
    <strong>
     Universal repertoire
    </strong>
    - Every writing system ever used shall be respected and represented in the standard
   </li>
   <li>
    <strong>
     Logical order
    </strong>
    - In bidirectional text are the characters stored in logical order, not in a way that the representaion
   </li>
   <li>
    <strong>
     Efficiency
    </strong>
    - The documentation must be efficient and complete.
   </li>
   <li>
    <strong>
     Unification
    </strong>
    - Where different cultures or languages use the same character, it shall be only included once. This point is
   </li>
   <li>
    <strong>
     Characters, not glyphs
    </strong>
    - Only characters, not glyphs shall be encoded. In a nutshell, glyphs are the actual graphical
   </li>
   <li>
    <strong>
     Dynamic composition
    </strong>
    - New characters can be composed of other, already standardized characters. For example, the character “Ä” can be composed of an “A” and a dieresis sign (“ ¨ ”).
   </li>
   <li>
    <strong>
     Semantics
    </strong>
    - Included characters must be well defined and distinguished from others.
   </li>
   <li>
    <strong>
     Stability
    </strong>
    - Once defined characters shall never be removed or their codepoints reassigned. In the case of an error, a codepoint shall be deprecated.
   </li>
   <li>
    <strong>
     Plain Text
    </strong>
    - Characters in the standard are text and never mark-up or metacharacters.
   </li>
   <li>
    <strong>
     Convertibility
    </strong>
    - Every other used encoding shall be representable in terms of a Unicode encoding.
   </li>
  </ul>
  <p>
   Note: Principle descriptions are from
   <a href="https://codepoints.net/about#unicode">
    codepoints.net
   </a>
  </p>
  <h1>
   Unicode Versions
  </h1>
  <ul>
   <li>
    <a href="http://www.unicode.org/versions/Unicode9.0.0/">
     Version 9.0.0
    </a>
    (Latest Version, August 2016 - adds exactly 7,500 characters)
   </li>
   <li>
    <a href="http://www.unicode.org/versions/Unicode8.0.0/">
     Version 8.0.0
    </a>
   </li>
   <li>
    <a href="http://www.unicode.org/versions/Unicode7.0.0/">
     Version 7.0.0
    </a>
   </li>
   <li>
    <a href="http://www.unicode.org/versions/Unicode6.3.0/">
     Version 6.3.0
    </a>
   </li>
   <li>
    <a href="http://www.unicode.org/versions/Unicode6.2.0/">
     Version 6.2.0
    </a>
   </li>
   <li>
    <a href="http://www.unicode.org/versions/Unicode6.1.0/">
     Version 6.1.0
    </a>
   </li>
   <li>
    <a href="http://www.unicode.org/versions/Unicode6.0.0/">
     Version 6.0.0
    </a>
   </li>
   <li>
    <a href="http://www.unicode.org/versions/Unicode5.2.0/">
     Version 5.2.0
    </a>
   </li>
   <li>
    <a href="http://www.unicode.org/versions/Unicode5.1.0/">
     Version 5.1.0
    </a>
   </li>
   <li>
    Version 5.0.0 (unavailable)
   </li>
   <li>
    <a href="http://www.unicode.org/versions/Unicode4.0.1/">
     Version 4.0.1
    </a>
   </li>
   <li>
    <a href="http://www.unicode.org/versions/corrigendum5.html">
     Version 4.0.0
    </a>
   </li>
  </ul>
  <p>
   <br>
    <br/>
   </br>
  </p>
  <h1>
   Contributing
  </h1>
  <p>
   See the
   <em>
    Awesome Unicode
   </em>
   <a href="CONTRIBUTING.md">
    contribution guide
   </a>
   for details on how to contribute.
  </p>
  <h1>
   Code of Conduct
  </h1>
  <p>
   See the
   <a href="CODE-OF-CONDUCT.md">
    Code of Conduct
   </a>
   for details. Basically it comes down to:
  </p>
  <blockquote>
   <p>
    In the interest of fostering an open and welcoming environment, we as
  contributors and maintainers pledge to making participation in our project and
  our community a harassment-free experience for everyone, regardless of age, body
  size, disability, ethnicity, gender identity and expression, level of experience,
  nationality, personal appearance, race, religion, or sexual identity and orientation.
   </p>
  </blockquote>
  <h1>
   License
  </h1>
  <p>
   <a href="https://creativecommons.org/publicdomain/zero/1.0/">
    <img alt="CC0" src="http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg"/>
   </a>
  </p>
  <p>
   To the extent possible under law,
   <a href="https://github.com/jagracey/Awesome-Unicode/graphs/contributors">
    the
contributors
   </a>
   have waived all copyright and related or neighboring rights to this work. See the
   <a href="LICENSE">
    license file
   </a>
   for details.
  </p>
 </elem.attributes.length;a++){>
</p>