---
title: importlib
---

## importlib
In python2, use `imp` instead.

## Usage

## API

### importlib.util
* [31.5. importlib — The implementation of import — Python 3.6.5 documentation](https://docs.python.org/3/library/importlib.html#module-importlib.util)

* `importlib.util.spec_from_file_location(name, location, *, loader=None, submodule_search_locations=None)`
    * [Example](https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly)
    * Create `ModuleSpec`
    * `name` is module_name
    * `location` is module_name
* `importlib.util.module_from_spec(spec)`
    * Import from `ModuleSpec`


## Tips

### import file given path
* [python - How to import a module given the full path? - Stack Overflow](https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path)

```python
import importlib.util
import sys

# For illustrative purposes.
import tokenize
file_path = tokenize.__file__
module_name = tokenize.__name__

spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
# Optional; only necessary if you want to be able to import the module
# by name later.
sys.modules[module_name] = module
```

## Reference
* [31.5. importlib — The implementation of import — Python 3.6.5 documentation](https://docs.python.org/3/library/importlib.html)

