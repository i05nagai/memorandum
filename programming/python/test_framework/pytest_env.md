---
title: pytest-env
---

## pytest-env
pytest実行時に環境変数を渡せる。

```
pip install pytest-env
```

`setup.cfg`に以下のように設定をかく。

```
[tool:pytest]
env =
    HOME=~/tmp
    RUN_ENV=test
```

## Reference
* [MobileDynasty/pytest-env: pytest plugin used to set environment variables](https://github.com/MobileDynasty/pytest-env)
