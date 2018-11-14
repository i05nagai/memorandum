---
title: DoxygenToolkit
---

## DoxygenToolkit
C, C++, Pythonで使えるDoxygen comment generator.

## Usage
関数の宣言部分で`:Dox`とするとDoxygen用のコメントが生成される。

```cpp
/**
 * @brief
 *
 * @param mychar
 * @param myint
 * @param myarray
 * @param mask
 *
 * @return
 */
int foo(char mychar,
      int myint,
      double* myarray,
      int mask = DEFAULT)
{ //...
}
```

## Configuration

```vim
let g:DoxygenToolkit_briefTag_pre="@brief "
let g:DoxygenToolkit_paramTag_pre="@param "
let g:DoxygenToolkit_returnTag="@return  "
let g:DoxygenToolkit_blockHeader="--------------------------------------------------------------------------"
let g:DoxygenToolkit_blockFooter="----------------------------------------------------------------------------"
let g:DoxygenToolkit_authorName="Author Name"
let g:DoxygenToolkit_licenseTag="My own license" "  <-- !!! Does not end with "\<enter>"
" If you want to use /// as a prefix of comment in C++, you need to set
let g:DoxygenToolkit_commentType = "C++"
```

## Command

* `:DoxLic`
    * create doxygen license comments
* `:DoxAuthor`
    * This will generate the skeleton and leave the cursor just after @author tag if no variable define it, or just after the skeleton.
* `:Dox`
    * This will generate the skeleton and leave the cursor after the @brief tag
* `:DoxBlock`
* `:DoxUndoc(DEBUG)`
    * if you want to uncomment documents created from the code between


```cpp
#ifdef DEBUG
...
#endif
```

## Reference
[vimwiki](http://vimwiki.net/?tips%2F18)
