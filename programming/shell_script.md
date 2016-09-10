# shell script

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
