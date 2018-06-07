---
title: pyenv virtualenv
---

## pyenv virtualenv
以下を実行すると、`pyenv virtualenv`系のコマンドが使えるようになる。

```
brew install pyenv-virtualenv
```

`bash_profile`に以下を追加する。

```
# pyenv
if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi
```

### Create virtualenv
以下で現在pyenvに設定されているpython環境が`env_name`という名前で作成される。

```
pyenv virtualenv env_name
```

### Activate virtualenv environment
以下で、作成した`env_name`に入ることができる。

```
pyenv activate env_name
```

### Deactivate virtualenv environment

```
pyenv deactivate
```

## Reference
