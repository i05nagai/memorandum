---
title: kafkacat
---

## kafkacat

## install

```
```


## CLI

General options:

* `-C | -P | -L | -Q`
    * Mode: Consume, Produce, Metadata List, Query mode
* `-G <group-id>`
    * Mode: High-level KafkaConsumer (Kafka 0.9 balanced consumer groups)
    * Expects a list of topics to subscribe to
* `-t <topic>`
    * Topic to consume from, produce to, or list
* `-p <partition>`
    * Partition
* `-b <brokers,..>`
    * Bootstrap broker(s) (host[:port])
* `-D <delim>`
    * Message delimiter character:
        * `a-z.. | \r | \n | \t | \xNN`
        * Default: `\n`
* -E                 Do not exit on non fatal error
* -K <delim>         Key delimiter (same format as -D)
* -c <cnt>           Limit message count
* -X list            List available librdkafka configuration properties
* -X prop=val        Set librdkafka configuration property.
                 Properties prefixed with "topic." are
                 applied as topic properties.
* -X dump            Dump configuration and exit.
* -d <dbg1,...>
    * Enable librdkafka debugging:
    * `all,generic,broker,topic,metadata,queue,msg,protocol,cgrp,security,fetch,feature`
* -q                 Be quiet (verbosity set to 0)
* -v                 Increase verbosity
* -V                 Print version
* -h                 Print usage help

Producer options:

  -z snappy|gzip     Message compression. Default: none
  -p -1              Use random partitioner
  -D <delim>         Delimiter to split input into messages
  -K <delim>         Delimiter to split input key and message
  -l                 Send messages from a file separated by
                     delimiter, as with stdin.
                     (only one file allowed)
  -T                 Output sent messages to stdout, acting like tee.
  -c <cnt>           Exit after producing this number of messages
  -Z                 Send empty messages as NULL messages
  file1 file2..      Read messages from files.
                     With -l, only one file permitted.
                     Otherwise, the entire file contents will
                     be sent as one single message.

Consumer options:

* `-o <offset>`
    * Offset to start consuming from:
    * `beginning | end | stored`
    * `<value>`
        * absolute offset
    * `-<value>`
        * relative offset from end
* `-e`
    * Exit successfully when last message received
* `-f <fmt..>`
    * Output formatting string, see below.
                     Takes precedence over -D and -K.
* `-J`
    * Output with JSON envelope
  -D <delim>         Delimiter to separate messages on output
  -K <delim>         Print message keys prefixing the message
                     with specified delimiter.
  -O                 Print message offset using -K delimiter
  -c <cnt>           Exit after consuming this number of messages
  -Z                 Print NULL messages and keys as "NULL"(instead of empty)
  -u                 Unbuffered output

Metadata options (-L):

* `-t <topic>`
    * Topic to query (optional)

Query options (-Q):

* `-t <t>:<p>:<ts>`
    * Get offset for topic <t>,
                 partition <p>, timestamp <ts>.
                 Timestamp is the number of milliseconds
                 since epoch UTC.
                 Requires broker >= 0.10.0.0 and librdkafka >= 0.9.3.
                 Multiple -t .. are allowed but a partition
                 must only occur once.

Format string tokens:
  %s                 Message payload
  %S                 Message payload length (or -1 for NULL)
  %R                 Message payload length (or -1 for NULL) serialized
                     as a binary big endian 32-bit signed integer
  %k                 Message key
  %K                 Message key length (or -1 for NULL)
  %T                 Message timestamp (milliseconds since epoch UTC)
  %t                 Topic
  %p                 Partition
  %o                 Message offset
  \n \r \t           Newlines, tab
  \xXX \xNNN         Any ASCII character
 Example:
  -f 'Topic %t [%p] at offset %o: key %k: %s\n'


Consumer mode (writes messages to stdout):

```
kafkacat -b <broker> -t <topic> -p <partition>
```

```
kafkacat -C -b ...
```

High-level KafkaConsumer mode:

```
kafkacat -b <broker> -G <group-id> topic1 top2 ^aregex\d+
```

Producer mode (reads messages from stdin):

```
... | kafkacat -b <broker> -t <topic> -p <partition>
```

```
kafkacat -P -b ...
```

Metadata listing:
  kafkacat -L -b <broker> [-t <topic>]

Query offset by timestamp:
  kafkacat -Q -b broker -t <topic>:<partition>:<timestamp>

## Usage

```
kafkacat -b mybroker -G mygroup topic1 topic2
```

Produce messages from file (one file is one message)

```
kafkacat -P -b mybroker -t filedrop -p 0 myfile1.bin /etc/motd thirdfile.tgz
```

```
kafkacat -C -b mybroker -t syslog -p 0 -o -2000 -e
```

Output consumed messages in JSON envelope

```
kafkacat -C -b mybroker -t syslog -J
```

## Reference
- [edenhill/kafkacat: Generic command line non\-JVM Apache Kafka producer and consumer](https://github.com/edenhill/kafkacat)
- https://github.com/edenhill/kcat
