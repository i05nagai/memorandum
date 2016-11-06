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

## Cachegrind

## Helgrind

## DRD

## Reference
* [pdf](http://www.eidos.ic.i.u-tokyo.ac.jp/~tau/lecture/programming_languages/gen/slides/07-valgrind.pdf)
* [Valgrindの結果の見方、日本語訳、など役に立つことまとめ - 結果だけでなく過程も見てください](http://d.hatena.ne.jp/taiyakisun/20150902/1441214819)
