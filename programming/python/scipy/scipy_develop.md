---
title: Scipy Develop
---

## Scipy Develop


## Develop

```
apt-get install gfortran
```

```
git clone s
cd scipy
conda create -n scipy_dev python=3.6 numpy scipy Cython sphinx pytest
source activate scipy_dev
pip install pytest
python runtests.py -v
```

## Tips

### ImportError
* [undefined symbol: \_gfortran\_stop\_numeric\_f08 · Issue \#8325 · scipy/scipy](https://github.com/scipy/scipy/issues/8325)

```
ImportError while importing test module '/home/administrator/programming/python/github/scipy/build/testenv/lib/python3.6/site-packages/scipy/stats/tests/test_tukeylambda_stats.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
scipy/stats/__init__.py:346: in <module>
    from .stats import *
scipy/stats/stats.py:171: in <module>
    import scipy.special as special
scipy/special/__init__.py:640: in <module>
    from ._ufuncs import *
E   ImportError: /home/administrator/programming/python/github/scipy/build/testenv/lib/python3.6/site-packages/scipy/special/_ufuncs.cpython-36m-x86_64-linux-gnu.so: undefined symbol: _gfortran_stop_numeric_f08
```

```
apt-get install libgfortran3
```

## Reference
