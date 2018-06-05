---
title: pypi
---

## pypi

## Test PyPI
* [Register · TestPyPI](https://test.pypi.org/account/register/)
* [Using TestPyPI — Python Packaging User Guide](https://packaging.python.org/guides/using-testpypi/)

Upload package to Test PyPI

```
twine upload \
  --repository-url https://test.pypi.org/legacy/ \
  --username ${USERNAME} \
  --password ${PASSWORD} \
  dist/*
```

Install from Test PyPI.

```
pip install \
  --index-url https://test.pypi.org/simple/ \
  'mafipy==0.1.dev0'
```


## Configuration
* [6. The Python Package Index (PyPI) — Python 2.7.15 documentation](https://docs.python.org/2/distutils/packageindex.html)
* [6. The Python Package Index (PyPI) — Python 3.6.5 documentation](https://docs.python.org/3.6/distutils/packageindex.html)

`setup.py upload/register` check the existence of `$HOME/.pypirc`

```
[distutils]
index-servers =
    pypi

[pypi]
repository: <repository-url>
username: <username>
password: <password>
```

* `repositoy`
    * by default `https://www.python.org/pypi`


## Tips

### Filename or contents already exists
* [Help · PyPI](https://pypi.org/help/#file-name-reuse)

You cannot upload file with same filename.
You need to test with Test PyPI before uloading.


## Reference
* [PyPI – the Python Package Index · PyPI](https://pypi.org/)
