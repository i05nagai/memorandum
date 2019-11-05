---
title: setup.py
---

## setup.py

* [Packaging and distributing projects — Python Packaging User Guide](https://packaging.python.org/guides/distributing-packages-using-setuptools/)

* `setup.py`
* `setup.cfg`
* `README.rst`
* `MANIFEST.in`
    * [4. Creating a Source Distribution — Python 3.6.5 documentation](https://docs.python.org/3/distutils/sourcedist.html#specifying-the-files-to-distribute)

Basic boilerplate for `setup.py`.

```python
import distutils.core as core
VERSION = mafipy.__version__
NAME = "mafipy"
MAINTAINER = "i05nagai"
MAINTAINER_EMAIL = ""
DESCRIPTION = """ """
with open("README.rst") as f:
    LONG_DESCRIPTION = f.read()
LICENSE = ""
URL = ""
DOWNLOAD_URL = ""
CLASSIFIERS = """ \
Development Status :: 1 - Planning
Intended Audience :: Science/Research
Intended Audience :: Developers
Programming Language :: Python
Programming Language :: Python :: 3.5
Topic :: Software Development
Topic :: Scientific/Engineering
Operating System :: Unix
Operating System :: MacOS
"""

def main():
    cmdclass = {
        'test': PyTest,
        'benchmark': Benchmark,
        'benchmark_publish': BenchmarkPublish,
        'benchmark_preview': BenchmarkPreview,
    }

    metadata = dict(
        name=NAME,
        packages=[NAME],
        version=VERSION,
        description=DESCRIPTION,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        url=URL,
        download_url=DOWNLOAD_URL,
        license=LICENSE,
        classifiers=[_f for _f in CLASSIFIERS.split('\n') if _f],
        long_description=LONG_DESCRIPTION,
        tests_require=['pytest', 'pytest-cov'],
        cmdclass=cmdclass,
        ext_modules=ext_modules
    )
    core.setup(**metadata)


if __name__ == '__main__':
    main()
```

## Configuration
* `install_requires`
    * [Packaging and distributing projects — Python Packaging User Guide](https://packaging.python.org/guides/distributing-packages-using-setuptools/#install-requires)
    * [python - Reference requirements.txt for the install_requires kwarg in setuptools setup.py file? - Stack Overflow](https://stackoverflow.com/questions/14399534/reference-requirements-txt-for-the-install-requires-kwarg-in-setuptools-setup-py)
    * [pip/req_file.py at master · pypa/pip](https://github.com/pypa/pip/blob/master/src/pip/_internal/req/req_file.py#L60)
* `setup_requires`
    * [Building and Distributing Packages with Setuptools — setuptools 39.2.0 documentation](http://setuptools.readthedocs.io/en/latest/setuptools.html)


## setup.py sdist
* [4. Creating a Source Distribution — Python 3.6.5 documentation](https://docs.python.org/3/distutils/sourcedist.html#specifying-the-files-to-distribute)

source distribution.
platformに応じたソースコードの配布物を生成する。

### Configuration
* [2. Writing the Setup Script — Python 2.7.15 documentation](https://docs.python.org/2/distutils/setupscript.html#installing-package-data)
* [2. Writing the Setup Script — Python 2.7.15 documentation](https://docs.python.org/2/distutils/setupscript.html#listing-individual-modules)

Files included as source code

* all python files specified in `py_modules` と `packages`
* all C source files specified in `ext_modules`, `libraries`
* scripts scpefiled in `scripts`
* looks like test scripts like `test/test*.py`
    * currently Distuitls don't do anything
* `README.txt` or `README`
* `setup.py`, `setpup.cfg`
* all files that matches the `package_data`
    * [2. Writing the Setup Script — Python 3.6.5 documentation](https://docs.python.org/3/distutils/setupscript.html#distutils-installing-package-data)
* all files that matches the `data_files`
    * [2. Writing the Setup Script — Python 3.6.5 documentation](https://docs.python.org/3/distutils/setupscript.html#distutils-additional-files)
* files specified in `MANIFEST.in`
    * this files should be used specifying additional files
    * [scikit-learn/MANIFEST.in at master · scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn/blob/master/MANIFEST.in)
    * [incubator-airflow/MANIFEST.in at master · apache/incubator-airflow](https://github.com/apache/incubator-airflow/blob/master/MANIFEST.in)


```python
import setuptools
py_modules = ['mod1', 'pkg.mod2']
packages = ['mypkg']
packages = setuptools.find_packages(exclude=['tests*'])
package_dir = {'mypkg': 'src/mypkg'}
```


### CLI
Unixの場合は`.tar.gz`で、Windowsの場合は`.zip`がデフォルト。
`--formats`オプションで生成するファイルは指定可能。

```
python setup.py sdist --formats=gztar,zip
```

* --owner=root
* --group=root
* --formats=gztar,zip

## setup.py bdist_wheel
binary distribution.

## Tips

### Generate install_requires from requirements.txt
* `Install`
    * `numpy==1.10`
    * `installed_version`
        * `1.10`
    * `name`
        * `numpy`
    * `str(req)`
        * `numpy==1.10`

Generate from `requirements.txt`.

```python
import pip.req
install_reqs = pip.req.parse_requirements(
    'requirements.txt', session='hack')
install_requires = [str(r.req) for r in install_reqs]
# Be sure that your setup.py depends on pip
# you should specify `setup_requires` and 
setup_requires = ['pip==10.0.1']
```

### Custom commands
* [setuptools/\_\_init\_\_\.py at bb71fd1bed9f5e5e239ef99be82ed57e9f9b1dda · pypa/setuptools](https://github.com/pypa/setuptools/blob/bb71fd1bed9f5e5e239ef99be82ed57e9f9b1dda/setuptools/__init__.py#L137)
    * inherits `distutils.core.Command`
    * https://github.com/python/cpython/blob/master/Lib/distutils/cmd.py#L12
    * `user_options` does not support list


#### Manifest
- [4\. Creating a Source Distribution — Python 2\.7\.16 documentation](https://docs.python.org/2/distutils/sourcedist.html#the-manifest-in-template)


The list of commands

- `include`
- `exclude`
- `prune`
- `graft`

# Reference
* [4. ソースコード配布物を作成する — Python 2.7.x ドキュメント](http://docs.python.jp/2/distutils/sourcedist.html)
