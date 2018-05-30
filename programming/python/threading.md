---
title: threading
---

## threading


Smaple

```python
#!/usr/bin/pyhon

import threading
# pip install future is required in python2
import queue
import logging


class WorkerSample(threading.Thread):

    _queue = queue.Queue()

    def __init__(self, name):
        super(WorkerSample, self).__init__()
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
    for i in range(100000):
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
