# shell script

## Tips

### `[ :Unexpected operator in shell programming`
`sh`で実行しているため。
`bash`拡張のいくつかの記法が認識されていない。
以下のように実行すれば良い。

````shell
bash script.sh
```

* [linux - [ :Unexpected operator in shell programming - Stack Overflow](http://stackoverflow.com/questions/3411048/unexpected-operator-in-shell-programming)

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

```shell
echo "hoge"
```

```shell
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

```shell
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

```shell

function version {
    echo "$(basename ${0}) version 0.0.1 "
}    
```
## option aruguments
### single-option
```shell
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

```shell
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
