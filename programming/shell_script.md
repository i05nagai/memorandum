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

### set -euを使う

* `set -e`
    * errorがあればそこで処理を終了する
* `set -u`
    * 未定義の変数があれば処理を終了する

-e は command1 || command2 みたいなことが出来なくなるの使うことないな。-uは付けといて良いが。

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
