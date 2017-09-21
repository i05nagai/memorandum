---
title: queue
---

## queue

## API

* `Queue.task_done()`
    * queue consumner threadで使われたqueueが終了したことを知らせる
    * `get()`でtaskを取得し、その後`task_done()`でtaskをdequeueする

## Reference
* [8.10. Queue — A synchronized queue class — Python 2.7.14 documentation](https://docs.python.org/2/library/queue.html)
