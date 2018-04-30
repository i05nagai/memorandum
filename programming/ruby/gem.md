---
title: gem
---

## gem


## Tips

### SSL
* [RubyGem のSSL証明書の有効期限切れ \- Marginalia](http://d.hatena.ne.jp/obelisk2+marginalia/20170118/1484717722)

ubutnu 16.04で以下のerror

```
ERROR:  Could not find a valid gem 'bundler' (>= 0), here is why:
          Unable to download data from https://rubygems.org/ - SSL_connect returned=1 errno=0 state=error: certificate verify failed (https://rubygems.org/specs.4.8.gz)
```

```
gem sources --remove https://rubygems.org/
gem sources --add http://rubygems.org
sudo gem update --system
```

## Reference
