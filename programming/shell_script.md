## shell script

## Tips

### `[ :Unexpected operator in shell programming`
`sh`で実行しているため。
`bash`拡張のいくつかの記法が認識されていない。
以下のように実行すれば良い。

```shell
bash script.sh
```

* [linux - :Unexpected operator in shell programming - Stack Overflow](http://stackoverflow.com/questions/3411048/unexpected-operator-in-shell-programming)

### 環境変数一覧
`env`, `printenv`, `declare`, `set`のいずれかで見る
`set`は現在実行中のshellの変数の一覧が表示される。


### exportの有無
* [bash 環境変数とシェル変数 webzoit.net](http://www.webzoit.net/hp/it/internet/homepage/env/cs/server/os/type/unix/linux/shell/kind/sh_bash/environment/)

```
export VAL1="hoge"
VAL2="hoge"
```

`VAL1`は環境変数となる。
`VAL2`はシェル変数となる。
環境変数は、子プロセスでも有効。

* [シェル変数と環境変数の違いをコマンドラインで確認する - Qiita](http://qiita.com/kure/items/f76d8242b97280a247a1)

### test と `[` と `[[` コマンドの違い
* https://fumiyas.github.io/2013/12/15/test.sh-advent-calendar.html

bashなら`[[`で良い。

* `test`と`[`の違いは名前以外ない
* `[[`はword split, パス名展開がされない

```bash
line='foobar'
[ $line == foobar ]; echo $?
0

# foo bar == foobarに展開される
line='foo bar'
[ $line == foobar ]; echo $?
# bash: [: 引数が多すぎます
2

# file名に展開される
line='/*'
[ $line == foobar ]; echo $?
# bash: [: 引数が多すぎます
2

# 1 -eq 1 -o xxx == foobarに展開され、1 -eq 1でtrueになる
line='1 -eq 1 -o xxx'
[ $line == foobar ]; echo $?
0
```

`[[`はより期待される動作になる。

```bash
line='foobar'
[[ $line == foobar ]]; echo $?
0

line='foo bar'
[[ $line == foobar ]]; echo $?
1

line='/*'
[[ $line == foobar ]]; echo $?
1

line='1 -eq 1 -o dummy'
[[ $line == foobar ]]; echo $?
1
```

`[[`は数値の比較演算子で左右の値が算術式展開される。
`-ne`や`-eq`の比較をしたとき、評価された値を返す。

```bash
var=123
[ "$((var))" -eq 123 ]; echo $?
0

# varが評価される
[[ var -eq 123 ]]; echo $?
0

varname=var
[ "$(($varname))" -eq 123 ]; echo $?
0

# 変数にしてもOK
[[ $varname -eq 123 ]]; echo $?
0
```

`[[`は文字列の比較演算子 == の動作が異なる。
`[[`は右辺がquoteされてないとpattern matchになる。


```bash
[ /foobar == /fooba[rz] ]; echo $?
1

[ /foobar == '/fooba[rz]' ]; echo $?
1

# /foobarか/foobazでに一致
[[ /foobar == /fooba[rz] ]]; echo $?
0

[[ /foobar == '/fooba[rz]' ]]; echo $?
1

# /fooで始まる文字列に一致
[[ /foobar == /foo* ]]; echo $?
0

[[ /foobar == '/foo*' ]]; echo $?
1
```

`[[`は文字列の比較演算子の種類が多い。
以下の3つが追加で使える。

* `[[ str =~ regexp ]]`
    * strが正規表現に一致すれば真
* `[[ str1 < str2 ]]`
    * 現在のlocaleの辞書順でstr1がstr2より前なら真
* `[[ str1 > str2]]`
    * 現在のlocaleの辞書順でstr1がstr2よりなら真

`[[`は論理演算子が異なる。
以下の対応。

```bash
# -a と && が同じ結果
[ -n "$foo" -a -n "$bar" ]; echo $?
[[ -n $foo && -n $bar ]]; echo $?
# -oと ||が同じ結果
[ -n "$foo" -o -n "$bar" ]; echo $?
[[ -n $foo || -n $bar ]]; echo $?
```

### set option
* [set man page](http://linuxcommand.org/lc3_man_pages/seth.html)

* `set -e`
    * `set -o errexit`
    * errorがあればそこで処理を終了する
    * -e は command1 || command2 みたいなことが出来なくなる
* `set -u`
    * `set -o nounset`
    * 未定義の変数があれば処理を終了する
    * -uは付けといて良い
* `set -o pipefail`
    * pipelineのいずれかのcommandがfailしたらpipeline全体をfailにする
* `set -x`


### `-x`
`sh -x`やshebangの`#!/bin/bash -x`などとつけると、shell scriptの中のコマンドが出力される。
ciなどで便利。

`file.sh`が以下のようにかかれているとすると

```sh
echo "hoge"
```

```sh
$ sh file.sh
hoge

$ sh -x file.sh
+echo "hoge"
hoge
```

#### Reference
* [シェルスクリプトを書くときはset -euしておく - Qiita](http://qiita.com/youcune/items/fcfb4ad3d7c1edf9dc96)

## help
shell scriptを書いたら下記のような`usage`関数を書いておく。

```sh
function usage {
    cat <<EOF
$(basename ${0}) is a tool for ...

Usage:
    $(basename ${0}) [command] [<options>]

Options:
    --version, -v     print $(basename ${0}) version
    --help, -h        print this
EOF
}
```

versionもかく。

```sh
function version {
    echo "$(basename ${0}) version 0.0.1 "
}    
```

## option aruguments

### single-option

```sh
case ${1} in

    start)
        start
    ;;

    stop)
        stop
    ;;

    restart)
        start && stop
    ;;

    help|--help|-h)
        usage
    ;;

    version|--version|-v)
        version
    ;;
    
    *)
        echo "[ERROR] Invalid subcommand '${1}'"
        usage
        exit 1
    ;;
esac
```

### multiple-option

```sh
while [ $# -gt 0 ];
do
    case ${1} in

        --debug|-d)
            set -x
        ;;

        --host|-h)
            HOST=${2}
            shift
        ;;

        --port|-p)
            PORT=${2}
            shift
        ;;

        *)
            echo "[ERROR] Invalid option '${1}'"
            usage
            exit 1
        ;;
    esac
    shift
done
```

### reference
* [使いやすいシェルスクリプトを書く | SOTA](http://deeeet.com/writing/2014/05/18/shell-template/)
* [bashのヒアドキュメントを活用する - Qiita](http://qiita.com/take4s5i/items/e207cee4fb04385a9952)
