---
title: awk
---

## awk

```
awk 'program' input-file1 input-file2 …
awk '{print $1}' <filename>
```

* `-F ":"`
    * separator
    * tab by default
* `-f <filename>`
    * path to program

## Actions
* `if( expression ) statement [ else statement ]`
* `while( expression ) statement`
* `for( expression ; expression ; expression ) statement`
* `for( var in array ) statement`
* `do statement while( expression )`
* `break`
* `continue`
* `{ [ statement ... ] }`
* `expression`
    * commonly var = expression
* `print [ expression-list ] [ > expression ]`
* `printf format [ , expression-list ] [ > expression ]`
* `return [ expression ]`
* `next`
    * skip remaining patterns on this input line
* nextfile
    * skip rest of this file, open next, start at top
* delete array[ expression ]
    * delete an array element
* delete array
    * delete all elements of array
* exit [ expression ]
    * exit immediately; status is expression

## Function
* [AWKのこういう時はどう書く? - Qiita](https://qiita.com/hirohiro77/items/713d5bcf60fef7e88dfa)


## Reference
* [The GNU Awk User’s Guide: Print Examples](https://www.gnu.org/software/gawk/manual/html_node/Print-Examples.html)
