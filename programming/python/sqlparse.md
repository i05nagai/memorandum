---
title: sqlparse
---

## sqlparse

```
pip install sqlparse
```

## CLI
CLIが使える。
optionは`sqlparse.format`と同じものが使える。

```
sqlformat --help
```


## Formatting

```
import sqlparse

sqlparse.split(sql, )
```

* keyword_case
    * Changes how keywords are formatted.
    Allowed values are `upper`, `lower`, and `capitalize`.
* identifier_case
    * Changes how identifiers are formatted. Allowed values are `upper`, `lower`, and `capitalize`.
* strip_comments
    * If True comments are removed from the statements.
* truncate_strings
    * If truncate_strings is a positive integer, string literals longer than the given value will be truncated.
* truncate_char (default: “[...]”)
    * If long string literals are truncated (see above) this value will be append to the truncated string.
* reindent
    * If True the indentations of the statements are changed.
* indent_tabs
    * If True tabs instead of spaces are used for indentation.
* indent_width
    * The width of the indentation, defaults to 2.
* wrap_after
    * The column limit for wrapping comma-separated lists.
    * If unspecified, it puts every item in the list on its own line.
* output_format
    * If given the output is additionally formatted to be used as a variable in a programming language.
    * Allowed values are `python` and `php`.

## Source code
* ttype
    * `tokens._TokenType`
    * `sqlparse.tokens`で定義されている
* `tlist`
    * TokenList
* `sql.Statement`
    * TokenListのsubclass
* `token`
    * `token.ttype`


## Reference
* [python-sqlparse — python-sqlparse 0.2.5.dev0 documentation](https://sqlparse.readthedocs.io/en/latest/)
* [andialbrecht/sqlparse: A non-validating SQL parser module for Python](https://github.com/andialbrecht/sqlparse)
