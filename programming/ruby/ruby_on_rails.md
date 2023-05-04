---
title: Ruby On Rails
---

## Ruby On Rails

## directory structure
- `app/`
    - Contains the controllers, models, views, helpers, mailers, channels, jobs, and assets for your application. You'll focus on this folder for the remainder of this guide.
- `bin/`
- `config/`
    - Contains configuration for your application's routes, database, and more.
- `config.ru`
- `db/`
- `lib/`
- `log/`
- `public/`
- `Rakefile`
- `storage/`
- `test/`
- `tmp/`
- `vendor/`
-

## configuration
https://guides.rubyonrails.org/configuring.html

## Routes
https://guides.rubyonrails.org/routing.html


```
get '/patients/:id', to: 'patients#show'
get '/patients/:id', to: 'patients#show', as: 'patient'

```

## Unscoped associations
- https://github.com/markets/unscoped_associations
- https://apidock.com/rails/v5.2.3/ActiveRecord/QueryMethods/unscope
- https://marcanguera.net/blog/introducing-unscoped-associations


## Reference
