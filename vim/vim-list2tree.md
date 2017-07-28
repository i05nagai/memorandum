---
title: vim-list2tree
---

## vim-list2tree


```
call dein#add('shinespark/vim-list2tree', {'lazy': 1, 'on_cmd': 'List2Tree'})
```

以下のように記載して

```
* .
  * dir
    * file
    * file
    * file
  * dir
    * dir
      * file
      * file
  * file
```

`:'<,'>List2Tree`を実行すれば以下のような感じになる。


```
.
├── dir
│   ├── file
│   ├── file
│   └── file
├── dir
│   └── dir
│       ├── file
│       └── file
└── file
```


## Reference
* [shinespark/vim-list2tree: list of markdown to tree.](https://github.com/shinespark/vim-list2tree)
