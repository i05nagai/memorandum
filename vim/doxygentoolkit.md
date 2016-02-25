# DoxygenToolkit
C, C++, Pythonで使えるDoxygen生成用のプラグイン。

## 使い方
関数の宣言部分で`:Dox`とするとDoxygen用のコメントが生成される。
```cpp
int
  foo(char mychar,
      int myint,
      double* myarray,
      int mask = DEFAULT)
{ //...
}
```

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
```

## 設定
`.vimrc`に下記を追加することで、タグやauthorなどを設定できる。
```
let g:DoxygenToolkit_briefTag_pre="@Synopsis  "
let g:DoxygenToolkit_paramTag_pre="@Param "
let g:DoxygenToolkit_returnTag="@Returns   "
let g:DoxygenToolkit_blockHeader="--------------------------------------------------------------------------"
let g:DoxygenToolkit_blockFooter="----------------------------------------------------------------------------"
let g:DoxygenToolkit_authorName="Mathias Lorente"
let g:DoxygenToolkit_licenseTag="My own license"   <-- !!! Does not end with "\<enter>"
```

## 参考
[vimwiki](http://vimwiki.net/?tips%2F18)

