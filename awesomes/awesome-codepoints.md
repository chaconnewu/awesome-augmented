<h1>
 Awesome Code Points
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<p>
 This is a curated list of characters in Unicode, that have interesting (and
maybe not widely known) features or are awesome in some other way.
</p>
<h2>
 Table of Contents
</h2>
<ol>
 <li>
  <a href="#standalone-code-points">
   Standalone code points
  </a>
 </li>
 <li>
  <a href="#code-points-that-affect-others">
   Code points that affect others
  </a>
  <ol>
   <li>
    <a href="#breaking-and-gluing-other-characters">
     Breaking and Gluing other characters
    </a>
   </li>
  </ol>
 </li>
 <li>
  <a href="#record-holders-and-extremes">
   Record holders and extremes
  </a>
 </li>
 <li>
  <a href="#for-funsies">
   For funsies
  </a>
  <ol>
   <li>
    <a href="#games">
     Games
    </a>
   </li>
  </ol>
 </li>
 <li>
  <a href="#contributing-your-code-points">
   Contributing
  </a>
 </li>
 <li>
  <a href="#license">
   License
  </a>
 </li>
</ol>
<h2>
 Standalone Code Points
</h2>
<ul>
 <li>
  <p>
   The code points of the Unicode blocks
   <a href="https://codepoints.net/box_drawing">
    Box
Drawing
   </a>
   (U+2500 to U+257F) and
   <a href="https://codepoints.net/block_elements">
    Block
Elements
   </a>
   (U+2580 to U+259F) cover
most of your monospace command-line visualization needs.
  </p>
  <pre><code>╭───────╮
│Unicode│
│rules! │
╰┬─────┬╯
</code></pre>
 </li>
 <li>
  <a href="https://codepoints.net/U+2E2E">
   U+2E2E
  </a>
  REVERSED QUESTION MARK - the “irony
mark” to express irony/sarcasm. A useful character⸮
 </li>
 <li>
  <a href="https://codepoints.net/U+D800">
   U+D800
  </a>
  to
  <a href="https://codepoints.net/U+DFFF">
   U+DFFF
  </a>
  - surrogate code points. They are
only reserved to ease
  <a href="https://en.wikipedia.org/wiki/UTF-16">
   UTF-16
encoding
  </a>
  .
 </li>
 <li>
  <a href="https://codepoints.net/U+FEFF">
   U+FEFF
  </a>
  ZERO WIDTH NO-BREAK SPACE - it’s name
suggests, that it can be used like U+2060 WORD JOINER. And in fact the
latter was introduced to inherit its semantics. This is because U+FEFF had
become a special beacon called the
  <a href="https://en.wikipedia.org/wiki/Byte_order_mark">
   byte order
mark
  </a>
  , that was placed on
the beginning of some UTF-8 files. In complying software (including many
text editors) this character is stripped from the start of a file and
handled as metadata. In non-complying software (like the PHP interpreter)
this leads to all sorts of fun behaviour.
 </li>
 <li>
  <a href="https://codepoints.net/U+FFFD">
   U+FFFD
  </a>
  REPLACEMENT CHARACTER - when a
character cannot be displayed (e.g., decoding an erroneous UTF-8 sequency),
this code point steps into the breach.
 </li>
 <li>
  <a href="https://codepoints.net/U+1D455">
   U+1D455
  </a>
  is missing. It would be an italic
small “h”. It was not encoded, because it would be identical to the Planck
constant ℎ (
  <a href="https://codepoints.net/U+210E">
   U+210E
  </a>
  ).
 </li>
</ul>
<h2>
 Code Points that Affect Others
</h2>
<ul>
 <li>
  <p>
   <a href="https://codepoints.net/U+202D">
    U+202D
   </a>
   and
   <a href="https://codepoints.net/U+202E">
    U+202E
   </a>
   - change the text direction.
Relevant XKCD:
  </p>
  <p>
   <a href="https://xkcd.com/1137/">
    <img alt="" src="http://imgs.xkcd.com/comics/rtl.png "/>
   </a>
  </p>
 </li>
 <li>
  <a href="https://codepoints.net/U+FE0E">
   U+FE0E
  </a>
  VARIATION SELECTOR-15 - force
colorful emoji. If this code point follows an emoji, an explicit colorful
rendering of the emoji is requested (if the client supports it).
 </li>
 <li>
  <a href="https://codepoints.net/U+FE0F">
   U+FE0F
  </a>
  VARIATION SELECTOR-16 - force
black-
  <em>
   &
  </em>
  -white emoji. If this code point follows an emoji, an explicit
monochrome rendering of the emoji is requested (if the client supports it).
 </li>
 <li>
  <p>
   Diacritics and combining marks: There is a
   <a href="https://codepoints.net/search?gc=Mn">
    host of
characters
   </a>
   , that add
to the characters before. Those are called Combining Marks. Unicode
provides a
   <a href="http://unicode.org/faq/char_combmark.html">
    handy FAQ
   </a>
   on the
details, but in a nutshell: If you add one after a character, it is placed
on top of that previous one. So,
   <code>
    a + ̊˚ = å
   </code>
   . This
   <em>
    may
   </em>
   lead to all kinds
of funny problems, because for some combinations there are pre-composed
characters. Our little
   <code>
    å
   </code>
   here can also be encoded as U+00E5. You might
note, that while this has a length of one character, the combination of
   <code>
    a
   </code>
   and combining ring has a length of two characters.
  </p>
  <p>
   Of course, one can also do fun things with those characters like
   <a href="http://stackoverflow.com/a/1732454/113195">
    this answer
   </a>
   on StackOverflow.
  </p>
 </li>
 <li>
  <p>
   The
   <a href="https://codepoints.net/U+1F1E6..U+1F1FF">
    Regional Indicator Symbols
   </a>
   U+1F1E6 to U+1F1FF resemble the 26 latin characters. They are used to
create flag emoji. Since the Unicode consortium didn’t feel like getting on
board with international politics, the solution to flags is to combine
these 26 characters to the respective ISO code for a country. Examples:
  </p>
  <p>
   Country | ISO Code | Code Points       | Emoji (if supported)
--------|----------|-------------------|---------------------
USA     | US       | U+1F1FA + U+1F1F8 | 🇺🇸
Germany | DE       | U+1F1E9 + U+0F1EA | 🇩🇪
China   | CN       | U+1F1E8 + U+0F1F3 | 🇨🇳
  </p>
 </li>
 <li>
  <p>
   Skin color of emoji: There are five code points, that control the skin color
of emoji,
   <a href="https://codepoints.net/U+1F3FB..U+1F3FF">
    U+1F3FB to U+1F3FF
   </a>
   .
They are called “Emoji Modifier Fitzpatrick Type” 1 to 6, with 1 the palest
and 6 the darkest. If one of these characters follows an emoji, that emoji
is meant to be rendered in the appropriate skin color of
   <a href="https://en.wikipedia.org/wiki/Fitzpatrick_scale">
    the Fitzpatrick
scale
   </a>
   . If no such
modifier is added, the skin tone should be unnatural, e. g., bright yellow.
Fun fact: Since the Fitzpatrick modifiers are normal code points, emoji
with such skin colors have the length 2, which Twitter users noticed first.
Here is a comparison chart
   <a href="http://www.unicode.org/reports/tr51/tr51-2.html#Diversity">
    directly from the
specification
   </a>
   :
  </p>
  <p>
   Code    | Name                                | Samples
--------|-------------------------------------|---------
U+1F3FB | EMOJI MODIFIER FITZPATRICK TYPE-1-2 |
   <img alt="" height="20" src="http://www.unicode.org/reports/tr51/images/other/swatch-type-1-2.png" width="auto">
    <img alt="" height="20" src="http://www.unicode.org/reports/tr51/images/other/swatch-type-1-2-bw.png" width="auto">
     U+1F3FC | EMOJI MODIFIER FITZPATRICK TYPE-3   |
     <img alt="" height="20" src="http://www.unicode.org/reports/tr51/images/other/swatch-type-3.png" width="auto">
      <img alt="" height="20" src="http://www.unicode.org/reports/tr51/images/other/swatch-type-3-bw.png" width="auto">
       U+1F3FD | EMOJI MODIFIER FITZPATRICK TYPE-4   |
       <img alt="" height="20" src="http://www.unicode.org/reports/tr51/images/other/swatch-type-4.png" width="auto">
        <img alt="" height="20" src="http://www.unicode.org/reports/tr51/images/other/swatch-type-4-bw.png" width="auto">
         U+1F3FE | EMOJI MODIFIER FITZPATRICK TYPE-5   |
         <img alt="" height="20" src="http://www.unicode.org/reports/tr51/images/other/swatch-type-5.png" width="auto">
          <img alt="" height="20" src="http://www.unicode.org/reports/tr51/images/other/swatch-type-5-bw.png" width="auto">
           U+1F3FF | EMOJI MODIFIER FITZPATRICK TYPE-6   |
           <img alt="" height="20" src="http://www.unicode.org/reports/tr51/images/other/swatch-type-6.png" width="auto">
            <img alt="" height="20" src="http://www.unicode.org/reports/tr51/images/other/swatch-type-6-bw.png" width="auto"/>
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
 </li>
</ul>
<h3>
 Breaking and Gluing other characters
</h3>
<ul>
 <li>
  <a href="https://codepoints.net/U+00A0">
   U+00A0
  </a>
  NO-BREAK SPACE - force adjacent
characters to stick together. Well known as
  <code>
  </code>
  in HTML.
 </li>
 <li>
  <a href="https://codepoints.net/U+00AD">
   U+00AD
  </a>
  SOFT HYPHEN - (in HTML:
  <code>
   ­
  </code>
  )
like ZERO WIDTH SPACE, but show a hyphen if (and only if) a break occurs.
 </li>
 <li>
  <a href="https://codepoints.net/U+200B">
   U+200B
  </a>
  ZERO WIDTH SPACE - the inverse to
U+00A0: create no space, but allow word breaking.
 </li>
 <li>
  <a href="https://codepoints.net/U+200D">
   U+200D
  </a>
  ZERO WIDTH JOINER - force adjacent
characters to be joined together (e.g., arabic characters or supported
emoji). Apple uses this to compose some emoji like different families.
 </li>
 <li>
  <a href="https://codepoints.net/U+2060">
   U+2060
  </a>
  WORD JOINER - the same as
U+00A0, but completely invisible. Good for writing
  <code>
   @font-face
  </code>
  on Twitter.
 </li>
</ul>
<p>
 For better comparison of which code point has which effect, consult this
table:
</p>
<p>
 | U+00A0 | U+00AD | U+200B | U+200D | U+2060
---------------|--------|--------|--------|--------|--------
create space   |   ✓    |   ✗    |   ✗    |   ✗    |   ✗
allow breaking |   ✗    |   ✓    |   ✓    |   ✗    |   ✗
possible change|   ✗    |   ✓    |   ✗    |   ✓    |   ✗
</p>
<p>
 Smashing Magazine featured
 <a href="http://www.smashingmagazine.com/2015/10/space-yourself/">
  a comprehensive
article
 </a>
 on the
different types of whitespace.
</p>
<h2>
 Record Holders and Extremes
</h2>
<ul>
 <li>
  <a href="https://codepoints.net/U+0000">
   U+0000
  </a>
  <control>
   - first code point.
  </control>
 </li>
 <li>
  <a href="https://codepoints.net/U+EFFFF">
   U+EFFFF
  </a>
  (
  <em>
   non-character
  </em>
  ) - last (currently
defined) code point.
  <a href="https://codepoints.net/U+10FFFF">
   U+10FFFF
  </a>
  is the
ultimately last one, but it is a private use character, that is guaranteed
to be never defined by Unicode.
 </li>
 <li>
  <a href="https://codepoints.net/U+1F402">
   U+1F402
  </a>
  OX - shortest name.
 </li>
 <li>
  <a href="https://codepoints.net/U+FBFB">
   U+FBFB
  </a>
  ARABIC LIGATURE UIGHUR KIRGHIZ YEH
WITH HAMZA ABOVE WITH ALEF MAKSURA INITIAL FORM - longest name: 82
characters.
 </li>
 <li>
  <a href="https://codepoints.net/U+FDFA">
   U+FDFA
  </a>
  ARABIC LIGATURE SALLALLAHOU ALAYHE
WASALLAM - longest decomposition form: 18 characters.
 </li>
 <li>
  <a href="https://codepoints.net/U+5146">
   U+5146
  </a>
  and
  <a href="https://codepoints.net/U+16B61">
   U+16B61
  </a>
  - code points that represent the
highest “single-digit” number. In both cases that’s 1,000,000,000,000, a
trillion.
 </li>
 <li>
  <a href="https://codepoints.net/U+0F33">
   U+0F33
  </a>
  TIBETAN DIGIT HALF ZERO - code point that
represents the
  <em>
   lowest
  </em>
  “single-digit” number and at the same time the
only negative one, -½.
 </li>
 <li>
  The trophy for most useless code points goes to
  <a href="https://codepoints.net/U+0080">
   U+0080
  </a>
  ,
  <a href="https://codepoints.net/U+0081">
   U+0081
  </a>
  and
  <a href="https://codepoints.net/U+0099">
   U+0099
  </a>
  . These so-called C1 control
characters are more or less unspecified. They got into Unicode, because
they were present in the very first version of what should later become ISO
10646, the ISO-standardized version of Unicode. They
  <a href="http://unicode.org/mail-arch/unicode-ml/y2015-m10/0050.html">
   were meant to be part
of an upgrade to ISO
2022
  </a>
  , that
never came to be.
 </li>
 <li>
  <a href="https://codepoints.net/U+006F">
   U+006F
  </a>
  LATIN SMALL LETTER O - leads the list
of characters with confusable shapes. Of all the possible mappings in the
  <a href="http://www.unicode.org/reports/tr39/#Data_Files">
   list of confusable
characters
  </a>
  , the small “o”
leads with a whopping 73 entries of similar looking glyphs, followed by
  <a href="https://codepoints.net/U+006C">
   U+006C
  </a>
  LATIN SMALL LETTER L with 70
entries.
 </li>
</ul>
<h2>
 For Funsies
</h2>
<ul>
 <li>
  <a href="https://codepoints.net/U+1680">
   U+1680
  </a>
  OGHAM SPACE MARK - a space that looks
like a dash. Great to bring programmers close to madness:
  <code>
   1 +  2 === 3
  </code>
  .
 </li>
 <li>
  <a href="https://codepoints.net/U+037E">
   U+037E
  </a>
  GREEK QUESTION MARK - a look-alike to
the semicolon. Also a fun way to annoy developers.
 </li>
 <li>
  <a href="https://codepoints.net/U+1DD2">
   U+1DD2
  </a>
  COMBINING US ABOVE - this is the most
romantic code point.
 </li>
 <li>
  <a href="https://codepoints.net/U+F8FF">
   U+F8FF
  </a>
  PRIVATE USE CODEPOINT - this private
use code point is rendered as Apple logo on many Apple devices.
 </li>
 <li>
  <a href="https://codepoints.net/U+1F574">
   U+1F574
  </a>
  MAN IN BUSINESS SUIT LEVITATING -
A rather curious character, that only made it into Unicode for its
appearance in the Webdings font (for reasons of backwards compatibility).
 </li>
 <li>
  <a href="https://codepoints.net/U+1F596">
   U+1F596
  </a>
  RAISED HAND WITH PART BETWEEN
MIDDLE AND RING FINGERS - the Vulcan salute. Live long and prosper!
🖖
 </li>
 <li>
  <a href="https://codepoints.net/U+1F918">
   U+1F918
  </a>
  SIGN OF THE HORNS - Rock on!
🤘
 </li>
</ul>
<h3>
 Games
</h3>
<p>
 For plain-text gaming, Unicode is well equipped with several complete sets:
</p>
<ul>
 <li>
  <a href="https://codepoints.net/U+2654..U+265F">
   Chess figures
  </a>
  .
 </li>
 <li>
  <a href="https://codepoints.net/U+2660..U+2667">
   Card suits
  </a>
  and even a whole
  <a href="https://codepoints.net/playing_cards">
   deck of
cards
  </a>
  complete with joker and back
of card.
 </li>
 <li>
  <a href="https://codepoints.net/U+2680..U+2685">
   Die faces
  </a>
  and a nice
  <a href="https://codepoints.net/U+1F3B2">
   die
emoji
  </a>
  .
 </li>
 <li>
  <a href="https://codepoints.net/U+2686..U+2689">
   Go pieces
  </a>
  .
 </li>
 <li>
  <a href="https://codepoints.net/U+26C0..U+26C3">
   Draughts (or checkers) pieces
  </a>
  .
 </li>
 <li>
  <a href="https://codepoints.net/U+2616,U+2617,U+26C9,U+26CA">
   Shogi pieces
  </a>
  , a
  <a href="https://en.wikipedia.org/wiki/Shogi">
   Japanese variant of chess
  </a>
  .
 </li>
 <li>
  <a href="https://codepoints.net/domino_tiles">
   Domino tiles
  </a>
 </li>
 <li>
  <a href="https://codepoints.net/mahjong_tiles">
   Mahjong tiles
  </a>
 </li>
</ul>
<h2>
 Contributing Your Code Points
</h2>
<p>
 See
 <a href="CONTRIBUTING.md">
  the contribution guide
 </a>
 for details.
</p>
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
 <a href="https://github.com/Codepoints/awesome-codepoints/graphs/contributors">
  the
contributors
 </a>
 have waived all copyright and related or neighboring rights to this work. See
 <a href="LICENSE">
  the license file
 </a>
 for details.
</p>
