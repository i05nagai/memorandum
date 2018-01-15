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
