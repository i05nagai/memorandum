## date
dateコマンドについて。
BSD系とGNUでopstionが違う。

## Tips

### snippet
For GNU,

today

```
date +%Y%m%d
date +%Y-%m-%d
```

a day before today

```
date --date '1 day ago' +%Y%m%d
date --date '1 day ago' +%Y-%m-%d
```


For OSX

unixtime to date

```
date -r 1282368345
```

`-u`でUTC

```
date -u -r 1282368345
```

## Tips

### Unixtime
Posix timeともいう。
UTCでの1970/1/1 00:00:00からの経過時間を表す。



## Reference
* [シェルスクリプトで一日前の日付を求める - すがブロ](http://sugamasao.hatenablog.com/entry/20060423/1145806183)
* [Unix time - Wikipedia](https://en.wikipedia.org/wiki/Unix_time)
