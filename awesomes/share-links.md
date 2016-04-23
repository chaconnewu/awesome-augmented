# Share Links [![awesome](https://cdn.rawgit.com/sindresorhus/awesome/master/media/badge.svg)](https://github.com/sindresorhus/awesome)

![share-links](https://cloud.githubusercontent.com/assets/499192/9524299/8315b54a-4cde-11e5-830a-34b3c4eb8bac.png)

A curated list of awesome social media `share-links`. Do you know of another service? Please see the [contributing guidelines](CONTRIBUTING.md) and make a pull request.

##### Table of Contents

- [Buffer](#buffer)
- [Delicious](#delicious)
- [Digg](#digg)
- [Echo JS](#echo-js)
- [Email](#email)
- [Facebook](#facebook)
- [Flattr](#flattr)
- [Flipboard](#flipboard)
- [Google Bookmarks](#google-bookmarks)
- [Google Plus](#google-plus)
- [Hacker News](#hacker-news)
- [Instapaper](#instapaper)
- [Line](#line)
- [LinkedIn](#linkedin)
- [Pinterest](#pinterest)
- [Pocket](#pocket)
- [Reddit](#reddit)
- [Renren](#renren)
- [Sina Weibo](#sina-weibo)
- [StumbleUpon](#stumbleupon)
- [Telegram](#telegram)
- [Tumblr](#tumblr)
- [Twitter](#twitter)
- [Viber](#viber)
- [Vkontakte](#vkontakte)
- [WhatsApp](#whatsapp)
- [Xing](#xing)

## Buffer
- URL: https://buffer.com/add
- Documentation: https://buffer.com/extras/button
- Parameters: `url`, `text`

```
https://buffer.com/add?text=This+is+the+content&url=https%3A%2F%2Fexample.com
```

## Delicious
- URL: https://delicious.com/post
- Documentation: https://delicious.com/tools
- Parameters: `url`, `title`, `notes`

```
https://delicious.com/post?url=https://example.com&title=This+is+the+title&notes=This+is+the+content
```

## Digg
- URL: http://digg.com/submit
- Documentation: `N/A`
- Parameters: `url`, `title`

```
http://digg.com/submit?url=https://example.com&title=This+is+the+title
```

## Echo JS
- URL: http://www.echojs.com/submit
- Documentation: http://www.echojs.com/submit
- Parameters: `u`, `t`

```
http://www.echojs.com/submit?u=https://example.com&t=This+is+the+title
```

## Email
- URL: `mailto:`
- Documentation: https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Email_links
- Parameters: `subject`, `body`

```
mailto:david.hasselhoff@example.com?subject=This+is+the+subject&body=This+is+the+content
```

## Facebook
- URL: https://facebook.com/sharer.php
- Documentation: https://developers.facebook.com/docs/sharing/reference/share-dialog
- Parameters: `app_id`, `link`, `u`

```
https://facebook.com/sharer.php?app_id=123456789&u=https://example.com
```

## Flattr
- URL: https://flattr.com/submit/auto
- Documentation: http://developers.flattr.net/auto-submit/
- Parameters: `user_id`, `url`, `title`, `content`, `description`, `language`, `tags`, `hidden`, `category`

```
https://flattr.com/submit/auto?user_id=account&url=https://example.com&title=This+is+the+title
```

## Flipboard
- URL: https://share.flipboard.com/bookmarklet/popout
- Documentation: https://about.flipboard.com/tools/
- Parameters: `v`, `title`, `url`, `t`

```
https://share.flipboard.com/bookmarklet/popout?v=2&title=This+is+the+title&url=http://example.com&t=201601010000
```

## Google Bookmarks
- URL: https://www.google.com/bookmarks/mark?op=edit
- Documentation: `N/A`
- Parameters: `annotation`, `bkmk`, `labels`, `op`, `title`

```
https://www.google.com/bookmarks/mark?op=edit&bkmk=https://example.com&title=This+is+the+title&annotation=This+is+the+content&labels=one,two
```

## Google Plus
- URL: https://plus.google.com/share
- Documentation: https://developers.google.com/+/web/share/
- Parameters: `url`

```
https://plus.google.com/share?url=https://example.com
```

## Hacker News
- URL: https://news.ycombinator.com/submitlink
- Documentation: https://news.ycombinator.com/bookmarklet.html
- Parameters: `u`, `t`

```
https://news.ycombinator.com/submitlink?u=https://example.com&t=This+is+the+title
```

## Instapaper
- URL: https://www.instapaper.com/text
- Documentation: `N/A`
- Parameters: `u`

```
https://www.instapaper.com/text?u=http://example.com
```

## LinkedIn
- URL: https://linkedin.com/shareArticle
- Documentation: https://developer.linkedin.com/docs/share-on-linkedin
- Parameters: `url`, `title`, `mini`, `summary`, `source`

```
https://linkedin.com/shareArticle?url=https://example.com&title=This+is+the+title
```

## Line
- URL: http://line.me/R/msg/text
- Documentation: https://media.line.me/howto/en/
- Parameters: `N/A`

```
http://line.me/R/msg/text?This+is+the+content
```

## Pinterest

- URL: https://pinterest.com/pin/create/bookmarklet
- Documentation: https://developers.pinterest.com/docs/pin-it/
- Parameters: `media`, `url`, `description`

```
https://pinterest.com/pin/create/bookmarklet?media=http://example.com/image.jpg&url=http://example.com&description=This+is+the+content
```

## Pocket

- URL: https://getpocket.com/save
- Documentation: https://getpocket.com/add
- Parameters: `title`, `url`

```
https://getpocket.com/save?title=This+is+the+title&url=http://example.com
```


## Reddit
- URL: http://reddit.com/submit
- Documentation: https://www.reddit.com/buttons
- Parameters: `url`, `title`

```
https://reddit.com/submit?url=http://example.com&title=This+is+the+title
```

## Renren
- URL: http://widget.renren.com/dialog/share
- Documentation: http://dev.renren.com/website/?widget=rrshare
- Parameters: `url`, `title`, `description`

```
http://widget.renren.com/dialog/share?resourceUrl=https://example.com&title=This+is+the+title&description=This+is+the+content
```

## Sina Weibo
- URL: http://service.weibo.com/share/share.php
- Documentation: http://open.weibo.com/wiki/ShareCode
- Parameters: `url`, `title`

```
http://service.weibo.com/share/share.php?url=https://example.com&title=This+is+the+title
```

## StumbleUpon
- URL: http://www.stumbleupon.com/submit
- Documentation: `N/A`
- Parameters: `url`, `title`

```
http://www.stumbleupon.com/submit?url=https://example.com&title=This+is+the+title
```

## Telegram
- URI: `tg://msg_url`
- Documentation: `N/A`
- Parameters: `text`, `url`

```
tg://msg_url?text=This+is+the+content
```

## Tumblr

- URL: https://www.tumblr.com/widgets/share/tool
- Documentation: https://www.tumblr.com/docs/en/share_button
- Parameters: `posttype`, `url`, `canonicalUrl`, `title`, `caption`

```
https://www.tumblr.com/widgets/share/tool?canonicalUrl=https://example.com&posttype=link&title=This+is+the+title&caption=This+is+the+content
```

## Twitter

- URL: https://twitter.com/share
- Documentation: https://dev.twitter.com/web/intents
- Parameters: `text`, `url`, `hashtags`, `via`, `related`, `in_reply_to`

```
https://twitter.com/share?url=https://example.com&text=This+is+the+content&via=account&hashtags=one,two
```

## Viber
- URI: `viber://forward`
- Documentation: https://www.viber.com/en/viber-share-button
- Parameters: `text`

```
viber://forward?text=This+is+the+content
```

## Vkontakte
- URL: http://vk.com/share.php
- Documentation: http://vk.com/dev/share_details
- Parameters: `url`

```
http://vk.com/share.php?url=https://example.com
```

## WhatsApp
- URI: `whatsapp://send`
- Documentation: https://www.whatsapp.com/faq/en/iphone/23559013
- Parameters: `text`

```
whatsapp://send?text=This+is+the+content
```

## Xing
- URL: https://www.xing.com/spi/shares/new
- Documentation: https://dev.xing.com/plugins/share_button/docs
- Parameters: `url`

```
https://www.xing.com/spi/shares/new?url=https://example.com
```

## License

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Vincent Klaiber](https://vinkla.com) has waived all copyright and related or neighboring rights to this work.
