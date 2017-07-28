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

## Reference
* [シェルスクリプトで一日前の日付を求める - すがブロ](http://sugamasao.hatenablog.com/entry/20060423/1145806183)
