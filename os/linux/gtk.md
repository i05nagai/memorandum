---
title: gtk
---

## gtk
gnome


## CLI

```
gsettings [--schemadir SCHEMADIR] COMMAND [ARGS...]
```

Commands

* help
    * Show this information
* list-schemas
    * List installed schemas
* list-relocatable-schemas
    * List relocatable schemas
* list-keys
    * List keys in a schema
* list-children
    * List children of a schema
* list-recursively
    * List keys and values, recursively
* range
    * Queries the range of a key
* get
    * Get the value of a key
* set
    * Set the value of a key
* reset
    * Reset the value of a key
* reset-recursively
    * Reset all values in a given schema
* writable
    * Check if a key is writable
* monitor
    * Watch for changes


```
gsettings [--schemadir SCHEMADIR] get SCHEMA[:PATH] KEY
```

* SCHEMADIR
    * A directory to search for additional schemas
* SCHEMA
    * The name of the schema
* PATH
    * The path, for relocatable schemas
* KEY
    * The key within the schema



## Usage
check the value of schema

```
gsettings get <schema>
```

## Configuration
`~/.config/gtk-3.0`にconfigがある。


* `org.gnome.desktop.interface`
    * schema
    * `gtk-key-theme`
        * Default
        * Emacs

## Reference
* [HowDoI/GSettings \- GNOME Wiki\!](https://developer.gnome.org/GSettings/)
* [Linuxデスクトップでキーバインドを自由に設定する方法 \- Qiita](https://qiita.com/syui/items/0701ef58a5c41c43786f)
