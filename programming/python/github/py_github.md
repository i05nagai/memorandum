---
title: PyGitHub
---

## PyGitHub
Python2 and Python3.

```
pip install pygithub
```


## Example

```python
from github import Github

# First create a Github instance:

# using username and password
g = Github("user", "password")

# or using an access token
g = Github("access_token")

# Github Enterprise with custom hostname
g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)
```

## API
* [Reference — PyGithub 1.40a3 documentation](http://pygithub.readthedocs.io/en/latest/reference.html)


## Reference
* [PyGithub/PyGithub: Typed interactions with the GitHub API v3](https://github.com/PyGithub/PyGithub)
* [PyGithubを使って、GitHubの情報を取得してみた ｜ Developers.IO](https://dev.classmethod.jp/etc/get-github-info-using-pygithub/)
* [PyGithub Quickstart Examples - Chase Seibert Blog](https://chase-seibert.github.io/blog/2016/07/22/pygithub-examples.html)
