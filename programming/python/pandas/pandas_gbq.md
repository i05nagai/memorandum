---
title: pandas-gbq
---

## pandas-gbq


## Install
```
pip install pandas-gbq
```

## API
* `pandas.read_gbq(query, project_id=None, index_col=None, col_order=None, reauth=False, verbose=True, private_key=None, dialect='legacy', **kwargs)`
    * Google bigqueryから読み込む
    * dialectは`standard`か'legacy'
    * index_col
        * 結果のcolumnのDataFrame名
    * private_key
        * jupyter notebookを別serverで動かしている場合に有用


## Reference
