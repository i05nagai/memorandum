---
title: argparse
---

## argparse

### add_argument

```python
parser.add_argument('bar', nargs=1)
parser.add_argument('--foo', nargs='?', default='foo val')
```

* default
    * コマンドライン引数がない場合は、`default`の値が利用される
* const
    * オプション引数が指定されたがコマンドライン引数がない場合は、`const`の値が利用される
    * nargsが`?`の場合に使う
* nargs
    * 数字をかけば引数の数で、変数はlistでかえる
    * `?`
        * オプション引数
    * `+`
    * `*`

真偽値のflag

* `action='store_true'`
    * flagがついた場合trueが入る
* `action='store_false'`
    * flagがついた場合falseが入る

```python
parser = argparse.ArgumentParser(description='')
parser.add_argument('--version', action='version')

group = parser.add_mutually_exclusive_group()
group.add_argument('--force', action='store_true')
group.add_argument('--no-force', action='store_false')
parser.set_defaults(force=False)
```

## subcommand
* [15.4. argparse — Parser for command-line options, arguments and sub-commands — Python 2.7.14 documentation](https://docs.python.org/2/library/argparse.html#sub-commands)

subcommandの作成はsubparserの追加をする。

```python
def subcommand_a(args):
    pass

def subcommand_a(args):
    pass

# create the top-level parser
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('--foo', action='store_true', help='foo help')

# subpersers
subparsers = parser.add_subparsers(help='sub-command help')

# create the parser for the "a" command
parser_a = subparsers.add_parser('a', help='a help')
parser_a.add_argument('bar', type=int, help='bar help')
parser_a.set_defailts(func=subcommand_a)

# create the parser for the "b" command
parser_b = subparsers.add_parser('b', help='b help')
parser_b.add_argument('--baz', choices='XYZ', help='baz help')
parser_b.set_defailts(func=subcommand_b)

args = paser.parse_args()
args.func(args)
```

```
$ python subcommand.py
usage: PROG [-h] [--foo FOO] {subcommand_a,subcommand_b} ...

$ python subcommand.py subcommand_a
usage: PROG subcommand_a [-h] bar
```




## Namespace
* [15.4. argparse — Parser for command-line options, arguments and sub-commands — Python 2.7.14 documentation](https://docs.python.org/2/library/argparse.html#argparse.Namespace)
* parse_argsが引数を保持するためにnamespaceとして利用するclass
* object classのsubclass

## Reference
* [16.4. argparse — コマンドラインオプション、引数、サブコマンドのパーサー — Python 3.6.1 ドキュメント](https://docs.python.jp/3/library/argparse.html)
