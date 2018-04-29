---
title: mailgun
---

## mailgun
email service for developers.


## Usage

```
# Try our API. Copy & run this in your terminal.
curl -s --user 'api:key-3ax6xnjp29jd6fds4gc373sgvjxteol0' \
    https://api.mailgun.net/v3/samples.mailgun.org/messages \
    -F from='Excited User <excited@samples.mailgun.org>' \
    -F to='devs@mailgun.net' \
    -F subject='Hello' \
    -F text='Testing some Mailgun awesomeness!'
```

## Reference
* [Transactional Email API Service For Developers | Mailgun](https://www.mailgun.com/)
