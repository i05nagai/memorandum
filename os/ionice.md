---
title: ionice
---

## ionice


```
ionice [[-c class] [-n classdata] [-t]] -p PID [PID]...
ionice [-c class] [-n classdata] [-t] COMMAND [ARG]..
```

classは以下の3種類

* 0
    * none
* 1
    * real time
* 2
    * best-effor
* 3
    * idle
    * idle時のみ

## Reference
* https://linux.die.net/man/1/ionice
