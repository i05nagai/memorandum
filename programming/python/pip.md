---
title: pip
---

## pip

## Editable install
* [pip install — pip 9.0.1 documentation](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs)

`setup.py`との重複を防ぎつつ、`requirements.txt`を提供したい場合は`requirements.txt`に以下を記載する。

```
-e .
```

`-e`でsetuptoolsのdevelop modeでのinstallを実行するようになる。


## Reference
