---
title: Blade
---

## Blade
Blade is a HTML Template Compiler, inspired by Jade & Haml, implemented in JavaScript, so it will run on your microwave oven.
下記のようにかくとHTMLを生成してくれる。
同じようなものに、Jade, Hamlがある。


```
!!! 5
html
    head
        title Blade
    body
        #nav
            ul
                - for(var i in nav)
                    li
                        a(href=nav[i])= i
        #content.center
            h1 Blade is cool
```

## Reference
* [bminer/node-blade: Blade - HTML Template Compiler, inspired by Jade & Haml](https://github.com/bminer/node-blade)
