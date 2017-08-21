---
title: benchmark
---

## benchmark
googleの提供しているc++ bencharmk library

libaryとして使う場合にcmakeでbuildする場合は、`set`でtestをoffにしておくと良い。

```cmake
option(BENCHMARK_ENABLE_TESTING "disable tests in google/benchmark" OFF)
add_subdirectory(path/to/bencharmk)
```


## Usage

```cpp
#include "benchmark/benchmark.h"

static void BenchmarkSample(benchmark::State& state)
{
    while(state.KeepRunning()) {
        const int arg0 = state.range(0)
        const int arg1 = state.range(1)
        SampleFunc(arg0, arg1);
    }
}
// Args({range(0), range(1)})
BENCHMARK(BenchmarkSample)
    ->Args({1<<10, 1})
    ->Args({1<<10, 8})
    ->Args({1<<10, 64})
    ->Args({1<<10, 512})
    ->Args({8<<10, 1})
    ->Args({8<<10, 8})
    ->Args({8<<10, 64})
    ->Args({8<<10, 512});
BENCHMARK_MAIN();
```

Argsの入力値を機械的に生成する場合は関数を渡すことができる。
その場合は、`Apply`を使って以下のようにする


```cpp
#include "benchmark/benchmark.h"
static void CustomArguments(benchmark::internal::Benchmark* b) {
  for (int i = 0; i <= 10; ++i) {
    for (int j = 32; j <= 1024 * 1024; j *= 8) {
      b->Args({i, j});
    }
  }
}
BENCHMARK(BM_SetInsert)->Apply(CustomArguments);
```

また、測定したい処理が返り値を返す場合は、返り値自身は不要であることが多い。
ただ、compilerのオプションで、規約としてunused variableを許容していない場合は、代入することも難しい。
また、代入しない変数は最適化の段階で削除される場合もある。
このような場合は`DoNotOptimize`を使う。

```cpp
#include "benchmark/benchmark.h"

static void BenchmarkSample(benchmark::State& state)
{
    while(state.KeepRunning()) {
        const int arg0 = state.range(0)
        const int arg1 = state.range(1)
        benchmark::DoNotOptimize(SampleFunc(arg0, arg1));
    }
}
// Args({range(0), range(1)})
BENCHMARK(BenchmarkSample)
    ->Args({1<<10, 1})
    ->Args({1<<10, 8})
    ->Args({1<<10, 64})
    ->Args({1<<10, 512})
    ->Args({8<<10, 1})
    ->Args({8<<10, 8})
    ->Args({8<<10, 64})
    ->Args({8<<10, 512});
BENCHMARK_MAIN();
```
```


## Reference
* [GitHub - google/benchmark: A microbenchmark support library](https://github.com/google/benchmark)
