---
title: xclip
---

## xclip
Access an X server selection for reading or writing.

## Install

```
apt-get install xclip
```

## CLI

```
xclip [OPTION] [FILE]...
```

* -i, -in
    * read text into X selection from standard input or files
    * default
* -o, -out
    * prints the selection to standard out (generally for piping to a file or program)
* -l, -loops
    * number of selection requests to wait for before exiting
* -d, -display
    * X display to connect to (eg localhost:0")
* -selection
    * selection to access ("primary", "secondary", "clipboard" or "buffer-cut")
* -noutf8
    * don't treat text as utf-8, use old unicode
* -target
    * use the given target atom
* -silent
    * errors only, run in background (default)
* -quiet
    * run in foreground, show what's happening
* -verbose
    * running commentar

## Usage
Copy to clipboard

```
pwd | xclip -selection clipboard
```

Paste to terminal

```
xclip -selection clipboard -out
```

## Reference
* [How to use clipboard from command\-line in Ubuntu?](http://jeromyanglim.tumblr.com/post/33559321824/how-to-use-clipboard-from-command-line-in-ubuntu)
