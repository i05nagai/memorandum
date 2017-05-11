# valgrind

## callgrind

## Memcheck

### Usage

```shell
valgrind --leak-check=full ./a.out
```

### Output
出力のサンプルは以下のようになる。

```
==23525== Invalid free() / delete / delete[] / realloc()
==23525==    at 0x1000089DF: free (in /usr/local/Cellar/valgrind/HEAD/lib/valgrind/vgpreload_memcheck-amd64-darwin.so)
==23525==    by 0x100000F4F: main (sample.c:8)
==23525==  Address 0x10081f510 is 0 bytes inside a block of size 4 free'd
==23525==    at 0x1000089DF: free (in /usr/local/Cellar/valgrind/HEAD/lib/valgrind/vgpreload_memcheck-amd64-darwin.so)
==23525==    by 0x100000F46: main (sample.c:7)
==23525==
==23525==
==23525== HEAP SUMMARY:
==23525==     in use at exit: 34,997 bytes in 426 blocks
==23525==   total heap usage: 507 allocs, 82 frees, 41,129 bytes allocated
==23525==
==23525== 4 bytes in 1 blocks are definitely lost in loss record 1 of 81
==23525==    at 0x10000859B: malloc (in /usr/local/Cellar/valgrind/HEAD/lib/valgrind/vgpreload_memcheck-amd64-darwin.so)
==23525==    by 0x100000F26: main (sample.c:4)
==23525==
==23525== LEAK SUMMARY:
==23525==    definitely lost: 4 bytes in 1 blocks
==23525==    indirectly lost: 0 bytes in 0 blocks
==23525==      possibly lost: 0 bytes in 0 blocks
==23525==    still reachable: 0 bytes in 0 blocks
==23525==         suppressed: 34,993 bytes in 425 blocks
==23525==
==23525== For counts of detected and suppressed errors, rerun with: -v
==23525== ERROR SUMMARY: 2 errors from 2 contexts (suppressed: 17 from 17)
```

上記のうち最初の7行はメモリリークしている箇所を表している。

```
==23525== Invalid free() / delete / delete[] / realloc()
==23525==    at 0x1000089DF: free (in /usr/local/Cellar/valgrind/HEAD/lib/valgrind/vgpreload_memcheck-amd64-darwin.so)
==23525==    by 0x100000F4F: main (sample.c:8)
==23525==  Address 0x10081f510 is 0 bytes inside a block of size 4 free'd
==23525==    at 0x1000089DF: free (in /usr/local/Cellar/valgrind/HEAD/lib/valgrind/vgpreload_memcheck-amd64-darwin.so)
==23525==    by 0x100000F46: main (sample.c:7)
```

* `definitely lost`
* `indirectly lost`
* `possibly lost`
* `still reachable`
* `suppressed`

```
==7913== HEAP SUMMARY:
==7913==     in use at exit: 0 bytes in 0 blocks
→プログラム終了時使用されているヒープは0byte、つまりリークなし！

==7913==   total heap usage: 1 allocs, 2 frees, 40 bytes allocated
→確保した回数、解放した回数、確保されたメモリ量。

==7913== All heap blocks were freed -- no leaks are possible
→確保されたメモリはすべて解放されておりリークはない。
```

### Explanation of error messages from Memcheck

#### `Invalid read of size 4`

#### `Invalid write of size 4`

#### 4.2.2. Use of uninitialised values 

```
Conditional jump or move depends on uninitialised value(s)
   at 0x402DFA94: _IO_vfprintf (_itoa.h:49)
   by 0x402E8476: _IO_printf (printf.c:36)
   by 0x8048472: main (tests/manuel1.c:8)
```



#### `Use of uninitialised or unaddressable values in system calls`

#### Illegal frees

#### When a heap block is freed with an inappropriate deallocation function

#### Overlapping source and destination blocks

#### Fishy argument values

#### 4.2.8. Memory leak detection
Memcheckはheap領域のmalloc/newなどのコマンドを追跡するため、プログラムがメモリ領域をfreeしたかしてないかの判定ができる。

`--leak-check`が適切に設定されていると、Memcheckはroot-set内のpointerからブロックにアクセスできるかを確認する。
ここで、root-setは以下の2つからなる。

* (a). すべてのスレッドのgeneral-purpose regisiter 
* (b). stackを含むアクセス可能なclinetのメモリ内の初期化され、整列された、ポインタサイズのデータ

解放されていないblockにアクセスする方法は2種類ある。

* 

## 5. Cachegrind: a cache and branch-prediction profiler

## 5.2 Using Cachegind, cg_annotate and cg_merge

### 5.2.1 Running Cachegrind

```
valgrind --tool=cachegrind prog
```

```
==31751== I   refs:      27,742,716
==31751== I1  misses:           276
==31751== LLi misses:           275
==31751== I1  miss rate:        0.0%
==31751== LLi miss rate:        0.0%
==31751== 
==31751== D   refs:      15,430,290  (10,955,517 rd + 4,474,773 wr)
==31751== D1  misses:        41,185  (    21,905 rd +    19,280 wr)
==31751== LLd misses:        23,085  (     3,987 rd +    19,098 wr)
==31751== D1  miss rate:        0.2% (       0.1%   +       0.4%)
==31751== LLd miss rate:        0.1% (       0.0%   +       0.4%)
==31751== 
==31751== LL misses:         23,360  (     4,262 rd +    19,098 wr)
==31751== LL miss rate:         0.0% (       0.0%   +       0.4%)
```

### 5.2.2 Output file
上の要約に加えて、詳細な情報をファイルに出力する。
デフォルトでは、`cachegrind.out.<pid>`である。

pidがつくのは、

* fileをrenameをしなくて良い
* spawnした子プロセスも`--trace-children=yes`で計測できる

### 5.2.3 Running cg_annotate

```
cg_annotate output_file
```

`output_file`はcachegrindの出力したファイルを指定する。

出力のサンプルは次の節。

### 5.2.4 The Output Preamble

```
--------------------------------------------------------------------------------
I1 cache:              65536 B, 64 B, 2-way associative
D1 cache:              65536 B, 64 B, 2-way associative
LL cache:              262144 B, 64 B, 8-way associative
Command:               concord vg_to_ucode.c
Events recorded:       Ir I1mr ILmr Dr D1mr DLmr Dw D1mw DLmw
Events shown:          Ir I1mr ILmr Dr D1mr DLmr Dw D1mw DLmw
Event sort order:      Ir I1mr ILmr Dr D1mr DLmr Dw D1mw DLmw
Threshold:             99%
Chosen for annotation:
Auto-annotation:       off
```

## Helgrind

## DRD

## Reference
* [pdf](http://www.eidos.ic.i.u-tokyo.ac.jp/~tau/lecture/programming_languages/gen/slides/07-valgrind.pdf)
* [Valgrindの結果の見方、日本語訳、など役に立つことまとめ - 結果だけでなく過程も見てください](http://d.hatena.ne.jp/taiyakisun/20150902/1441214819)
