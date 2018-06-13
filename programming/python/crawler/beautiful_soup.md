---
title: Beautiful Soup
---

## Beautiful Soup

```
pip install beautifulsoup4
```

DOMのparserを別途installすることができる。

```
pip install lxml
```

## Usage

```
from bs4 import BeautifulSoup

with open("index.html") as fp:
    soup = BeautifulSoup(fp)

soup = BeautifulSoup("<html>data</html>")
```


## API


## Reference
