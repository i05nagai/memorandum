---
title: pytz
---

## pytz

## Install

```
pip install pytz
```




Sample

```python
import pytz
import datetime


def main():
    # https://docs.python.org/2.7/library/datetime.html#strftime-and-strptime-behavior
    date_time = datetime.datetime.strptime('2017-01-01 00:00:00', "%Y-%m-%d %H:%M:%S")
    JST = pytz.timezone('Asia/Tokyo')
    UTC = pytz.timezone('UTC')
    USE = pytz.timezone('US/Eastern')
    date_time_utc = UTC.localize(date_time)
    date_time_jst = JST.localize(date_time)
    date_time_edt = JST.localize(date_time)

    print('{0} = date_time_utc'.format(date_time_utc))
    print('{0} = date_time_jst'.format(date_time_jst))
    print('{0} = date_time_jst < date_time_utc'.format(date_time_jst < date_time_utc))

    date_time_from_utc_to_jst = JST.normalize(date_time_utc.astimezone(JST))
    date_time_from_jst_to_utc = UTC.normalize(date_time_jst.astimezone(UTC))
    print('{0} = date_time_from_utc_to_jst'.format(date_time_from_utc_to_jst))
    print('{0} = date_time_from_jst_to_utc'.format(date_time_from_jst_to_utc))


if __name__ == '__main__':
    main()
```

## Reference
