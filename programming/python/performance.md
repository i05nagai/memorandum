---
title:
---

## Performance
Pythonでperformanceを測る方法。

### CPU
* `line_profiler` module
* `cProfiler` module
* デコレータの自作
* Unix time command
* perf tools

### memory
* `memory_profiler`
    * 遅い

## line_profiler
指定した関数の一行ごとの実行時間を計測する。

```
pip install line_profiler
```

インストールすると`kernprof`コマンドが使えるようになっている。
測定したい関数の前に`@profile`をつける。

```
kernprof -l -v file.py
```

* `-l`
* `-v`
    * 標準出力に測定結果を出力
    * 指定しないと`.lprof`ファイルを出力
* `file.py`
    * 実行ファイル

出力は下記のような感じ。

```
Wrote profile results to numpy_test.py.lprof
Timer unit: 1e-06 s

Total time: 1.77984 s
File: numpy_test.py
Function: main at line 34

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    34                                           @profile
    35                                           def main():
    36         1            3      3.0      0.0      vec_size = 1000000
    37         1            4      4.0      0.0      vec_list = range(vec_size)
    38                                               # list
    39         1       530979 530979.0     29.8      norm_square_list(vec_list)
    40         1       329726 329726.0     18.5      norm_square_list_comprehension(vec_list)
    41                                               # generator
    42         1            7      7.0      0.0      vec_generator = range(vec_size)
    43         1       329748 329748.0     18.5      norm_square_generator_comprehension(vec_generator)
    44                                               # array
    45         1       105255 105255.0      5.9      vec_array = array("l", range(vec_size))
    46         1       472837 472837.0     26.6      norm_square_array(vec_array)
    47                                               # numpy
    48         1         3969   3969.0      0.2      vec_np = np.arange(vec_size)
    49         1         6373   6373.0      0.4      norm_square_numpy(vec_np)
    50         1          942    942.0      0.1      norm_square_numpy_dot(vec_np)
```

### @profileのエラーをなくす
単体テストの実行時などに`line_profiler`を使わない時は`@profile`のエラーをなくしたいときがある。

```
if "__buildin__" not in dir() or not hasattr(__builtin__, "profiler"):
    def profile(func):
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        return inner
```


## Reference
