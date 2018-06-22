---
title: Scipy Develop
---

## Scipy Develop


## Develop

```
apt-get install gfortran
apt-get install gfortran-7
```

```
git clone s
cd scipy
conda create -n scipy_dev python=3.6 numpy scipy Cython sphinx pytest
source activate scipy_dev
pip install pytest
python runtests.py -v
```


## Testing
```
runtests.py --help
```


## Tips

### ImportError
* [undefined symbol: \_gfortran\_stop\_numeric\_f08 · Issue \#8325 · scipy/scipy](https://github.com/scipy/scipy/issues/8325)

```
ImportError while importing test module '/lib/python3.6/site-packages/scipy/stats/tests/test_tukeylambda_stats.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
scipy/stats/__init__.py:346: in <module>
    from .stats import *
scipy/stats/stats.py:171: in <module>
    import scipy.special as special
scipy/special/__init__.py:640: in <module>
    from ._ufuncs import *
E   ImportError: /lib/python3.6/site-packages/scipy/special/_ufuncs.cpython-36m-x86_64-linux-gnu.so: undefined symbol: _gfortran_stop_numeric_f08
```

```
$ ldd /lib/python3.6/site-packages/scipy/special/_ufuncs.cpython-36m-x86_64-linux-gnu.so
        linux-vdso.so.1 =>  (0x00007ffeffde2000)
        libmkl_rt.so => not found
        libgfortran.so.4 => not found
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fb7b1eca000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007fb7b1cb4000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fb7b18ea000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fb7b2563000)
```

You need to add `LD_LIBRARY_PATH`

```
export LD_LIBRARY_PATH="$ORIGIN/"
export LD_LIBRARY_PATH="/path/to/anaconda_home/envs/<env-name>/lib:$LD_LIBRARY_PATH"
```

* [16\.04 \- How to install gcc\-7 or clang 4\.0? \- Ask Ubuntu](https://askubuntu.com/questions/859256/how-to-install-gcc-7-or-clang-4-0)
* [fortran \- How to install libgfortran\.so\.4 on ubuntu 16\.06 \- Stack Overflow](https://stackoverflow.com/questions/46516394/how-to-install-libgfortran-so-4-on-ubuntu-16-06)

For `libgfortran.so.4`, you need to install `gfortran-7`.

```
```

For `libmkl_rt.so`,


```
pip instal mkl
```

## Reference
