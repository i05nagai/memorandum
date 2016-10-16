# lldb

## debug

### breakpoint
`br`が省略形として使える。

#### ファイルへのbreakpoint
`hoge.c`の8行目にbreakpoint

```
b hoge.c:8
```

#### 関数へのbreakpoint
`foo(double)`関数へのbreakpoint

```
br set -n foo(double)
br set --name foo(double)
```


### 
