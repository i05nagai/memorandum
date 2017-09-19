---
title: threading
---

## threading
CPythonはGILなので、実行されるthreadは常に1つのみ。
IO待ちが長い場合以外でのメリットはあまりない。
multicoreのメリットを活かしたい場合はmultiprocessing moduleを使った方が良い。


## Usage
* [threading – Manage concurrent threads - Python Module of the Week](https://pymotw.com/2/threading/)

methodをthreadingする方法とthreading.Threadのsubclassを作る方法がある。

### method

### subclassing thread

```
import threading

class MyThread(threading.Thread):

    def run(self):
        logging.debug('running')
        return

for i in range(5):
    t = MyThread()
    t.start()
```

## API

* threading.Thread
    * `start()`
        * 必ず1度呼ばれる必要がある
    * `run()`
    * `join(timeout)`
        * timeoutが指定されていないない場合は、threadが終了するまで待つ
        * timeoutが指定されている場合はtimeoutまでthreadの終了をまつ
    * `daemon`
        * startを呼ぶ前にtrue/falseをsetする
    * `is_alive()`
        * run()が開始される前から、runが開始され終了されるまでtrueを返す
        * `threading.enumerate()`はaliveなthreadのiteratorを返す


## sample

```python
#!/usr/bin/pyhon

import threading
import queue
import logging


class WorkerSample(threading.Thread):

    _queue = queue.Queue()

    def __init__(self, name):
        super(WorkerSample, self).__init__()
        self.daemon = True
        self.name = name
        logging.basicConfig(filename='example.log', level=logging.DEBUG)

    def run(self):
        while True:
            if WorkerSample._queue.empty():
                return
            data = WorkerSample._queue.get()
            logging.debug('{0} {1} {2}'.format(
                self.name, data, WorkerSample._queue.qsize()))
            WorkerSample._queue.task_done()
        return

    @classmethod
    def put(cls, doc):
        WorkerSample._queue.put(doc)

    @classmethod
    def wait(cls):
        WorkerSample._queue.join()


def main():
    threads = []
    # generate worker
    for i in range(5):
        t = WorkerSample('worker{0}'.format(i))
        threads.append(t)

    # queueing data
    for i in range(5):
        WorkerSample.put(i)

    # start thread
    for t in threads:
        t.start()

    # wait for task is finished
    WorkerSample.wait()


if __name__ == '__main__':
    main()
```


## Reference
* [16.2. threading — Higher-level threading interface — Python 2.7.14rc1 documentation](https://docs.python.org/2/library/threading.html)
