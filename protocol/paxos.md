---
title: Paxos
---

## Paxos

- faulty processor
    - may communicate one value to a given processro and another value to some other process.

- $n$ isolated processors
- $m \le n$ faulty processors
- $p = n - m$ non faulty processors

An algorithm is said to achieve interactive consistency if it suffices

- (1) The nonfaulty processors compute exaclyt the same vector,
- (2) the elment of this vector corresponding to a given nonfaulty processor is the private value of that processor.

Paxos achieves interactive consistency.

Interactive consistency is guaranteed if and only if $n \ge 3m + 1$.

## Single fault case

- faulty processors may send a wrong value or refuse to send the message
- if nonfaulty processors fail to receive the message from faulty one. the nonfaulty processors use random values

- processors: p, q, r, s
- a processor will agree with the value v if at least two of the threa reports. Otherwise, the processor will recrod NIL

- (1) No faulty processors
- (2) q is a faulty processor
    - (a) p, r, s do not recieve anything -> record NIL
    - (b) p recieved $V_{q}$ from r, s
        - p recieved $V_{q}$ from r, s
            - -> r, s had agreed with $V_{q}$
            - -> r, s recieved $V_{q}$ from other processors (s, q and r, q)
    - (c) p received $V_{q}$ from nonfaulty+faulty processors q, r/ q, s
        - p recieved $V_{q}$ from q, r
            - -> p records $V_{q}$
            - -> s received $V_{q}$ from p and r


## A Procedure for n >= 3m + 1


## Reference
- https://en.wikipedia.org/wiki/Paxos_(computer_science)
