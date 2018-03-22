---
title: Airflow plugins
---

## Airflow plugins
* `$AIRFLOW_HOME/plugins`においたファイルをpluginとして利用できる
    * hooks, operators,などを拡張する際に使う

## Examples
* [blue-yonder/airflow-plugin-demo: Example for an airflow plugin](https://github.com/blue-yonder/airflow-plugin-demo)

```python
import time
import random

from airflow import models
from airflow import utils as airflow_utils


class BookData(models.BaseOperator):
    @airflow_utils.apply_defaults
    def __init__(self, **kwargs):
        super(BookData, self).__init__(
            task_id='book_data',
            **kwargs)

    def execute(self, context):
        waiting_time = 2 + random.random() * 2
        time.sleep(waiting_time)
```

DAGからimportできるようにになる。

```python
from airflow.operators import BookData
```

## Reference
