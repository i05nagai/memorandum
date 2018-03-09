---
title: multiprocessing
---

## multiprocessing


## Queue

* qsize()
    * Unix, OSXでは `NotImplementedError` になる場合がある
    * Note that this may raise NotImplementedError on Unix platforms like Mac OS X where sem_getvalue() is not implemented.

## Lock
* [Shared counter with Python's multiprocessing - Eli Bendersky's website](https://eli.thegreenplace.net/2012/01/04/shared-counter-with-pythons-multiprocessing)

## Logging
* [Logging Cookbook — Python 3.6.4 documentation](https://docs.python.org/3/howto/logging-cookbook.html#logging-to-a-single-file-from-multiple-processes)
* [performance - Python multiprocessing - Pipe vs Queue - Stack Overflow](https://stackoverflow.com/questions/8463008/python-multiprocessing-pipe-vs-queue)
* [Logging Cookbook — Python 3.6.4 documentation](https://docs.python.org/3/howto/logging-cookbook.html#a-more-elaborate-multiprocessing-example)



## Reference
* [16.6. multiprocessing — Process-based “threading” interface — Python 2.7.14 documentation](https://docs.python.org/2/library/multiprocessing.html)_
