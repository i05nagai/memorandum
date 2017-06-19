## python/datetime
日付まわりの変換まとめ

* datetime
    * 日付と時刻
* date
    * 日付
* time
    * 時刻

## datetime
```python
DT = datetime.datetime(y, m, d, h, m, s)
D = datetime.date(y, m, d)
T = datetime.time(h, m, s)
```

```python
time.min == time(0, 0, 0, 0)
```

date to datetime
日付DのAM00:00に変換

```
datetime.combine(D, time.min)
```


## Reference
* [Pythonの日付処理とTimeZone | Nekoya press](http://nekoya.github.io/blog/2013/06/21/python-datetime/)
