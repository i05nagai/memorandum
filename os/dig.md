---
title: dig
---

## dig

For ubuntu

```
apt-get install dnsutils
```

## CLI

```
dig [@server] [-b address] [-c class] [-f filename] [-k filename] [-m] [-p port#] [-q name] [-t type] [-x addr] [-y [hmac:]name:key] [-4] [-6] [name] [type] [class] [queryopt...]
```

* `-x`
    * this option is supplied to indicate a reverse lookup

## Usage

```
dig +qr www.isc.org any -x 127.0.0.1 isc.org ns +noqr
```

```
dig +trace example.com
```

## Query options
You can add query with the form `+keyword=value`.

* `+qr`
    * Print [do not print] the query as it is sent. By default, the query is not printed.
* `+trace`
* `+terse`
    * Provide a terse answer. The default is to print the answer in a verbose form.

## Output
* https://ns1.com/blog/decoding-dig-output
* https://ns1.com/blog/using-dig-trace

* `NOERROR`
* `SERVFAIL`
* `NXDOMAIN`
* `REFUSED`


## Reference
* https://linux.die.net/man/1/dig
