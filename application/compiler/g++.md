---
title: g++
---

## g++

## Install
For ubuntu 16.04, by default version `<=5` is available.

```
# for 4
apt-get install g++
apt-cache search g++ | grep 'g++'
apt-cache show 'g++'
# for 5
apt-get install g++-5
apt-cache search g++ | grep 'g++-5'
apt-cache show 'g++-5'
```

To install `6>=`

```
add-apt-repository ppa:ubuntu-toolchain-r/test
apt-get update
```

```
# for 6
apt-get install g++-6
apt-cache search g++ | grep 'g++-6'
apt-cache show 'g++-6'
# for 7
apt-get install g++-7
apt-cache search g++ | grep 'g++-7'
apt-cache show 'g++-7'
```

## Reference
