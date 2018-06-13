---
title: textwrap
---

## textwrap


* `dedent(str)`
    * delete indent in tripple-quoated strings

```python
def test():
    # end first line with \ to avoid the empty line!
    s = '''\
    hello
      world
    '''
    print repr(s)          # prints '    hello\n      world\n    '
    print repr(dedent(s))  # prints 'hello\n  world\n'
```

## Usage


## Reference
* https://docs.python.org/2/library/textwrap.html
