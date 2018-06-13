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
        * more than 0
    * `*`
        * more than 0 or equal to 0


* `action=store`
    * default
* `action='append'`
    * `parser.parse_args('--foo 1 --foo 2'.split())`
        * `foo=['1', '2']`
* `action='append_const'`
* `action='count'`

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--verbose', '-v', action='count')
>>> parser.parse_args(['-vvv'])
Namespace(verbose=3)
```

* `action=store_const`
    * use with `consit` argument
* `action='store_true'`
    * for true/false flag
    * flagがついた場合trueが入る
* `action='store_false'`
    * for true/false flag
    * flagがついた場合falseが入る

```python
parser = argparse.ArgumentParser(description='')
parser.add_argument('--version', action='version')

group = parser.add_mutually_exclusive_group()
group.add_argument('--force', action='store_true')
group.add_argument('--no-force', action='store_false')
parser.set_defaults(force=False)
```

## Formatter
* [16.4. argparse — Parser for command-line options, arguments and sub-commands — Python 3.6.5 documentation](https://docs.python.org/3/library/argparse.html#formatter-class)
    * format of help messages

* `argparse.RawDescriptionHelpFormatter`
    * description is not modified
* `argparse.RawTextHelpFormatter`
* `argparse.MetavarTypeHelpFormatter`
* `argparse.ArgumentDefaultsHelpFormatter`
    * [python - Argparse: Way to include default values in '--help'? - Stack Overflow](https://stackoverflow.com/questions/12151306/argparse-way-to-include-default-values-in-help)
    * display default value in help message

```python
parser = argparse.ArgumentParser(
    # ... other options ...
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
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

## Tips

### no arugmnets
* [Display help message with python argparse when script is called without any arguments - Stack Overflow](https://stackoverflow.com/questions/4042452/display-help-message-with-python-argparse-when-script-is-called-without-any-argu)

```
if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)
```

## Reference
* [16.4. argparse — コマンドラインオプション、引数、サブコマンドのパーサー — Python 3.6.1 ドキュメント](https://docs.python.jp/3/library/argparse.html)
* [16.4. argparse — Parser for command-line options, arguments and sub-commands — Python 3.6.5 documentation](https://docs.python.org/3/library/argparse.html#formatter-class)
