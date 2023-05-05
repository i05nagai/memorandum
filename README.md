# memorandum 

* [GitHub Pages](http://i05nagai.github.io/memorandum/)
    * [book](http://i05nagai.github.io/memorandum/book/)
    * [finance](http://i05nagai.github.io/memorandum/finance/)
    * [machine learning](http://i05nagai.github.io/memorandum/machine_learning/)
    * [math](http://i05nagai.github.io/memorandum/math/)

## Run local server

```
gem install bundler
bundle install --path=vendor/bundle
bundle exec jekyll s
# Wait for running server
```

The server run on `http://127.0.0.1:4000/memorandum/` by default.
Incremental build is faster when you edit existing pages

```
bundle exec jekyll s --incremental
```

## Travleshoots

#### Error when installing eventmachine
If you see the error containing,

```
An error occurred while installing eventmachine (1.2.7), and Bundler cannot continue.
```

You do either

```
bundle config build.eventmachine --with-openssl-dir="$(brew --prefix libressl)"
bundle install --path=vendor/bundle
```

or

```
gem install eventmachine '1.2.7' -- --with-openssl-dir=$(brew --prefix libressl)
```
