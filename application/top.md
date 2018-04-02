---
title: top
---

## top
top command

* VIRTはmalloc()しただけで増える。RESは増えない
* PR（優先度）とNI（nice値）は低いほど優先される
* swappingとはプロセス丸ごとディスクに追い出すこと
* pagingとはpage単位で二次記憶に追い出すこと

## key
* shift+o
    * 表示された特定のキーを押してEnterすると任意の列でソートできる
* shift+p
* shift+m

## Terms
* 

```
Cpu(s): 77.1%us,  8.4%sy,  0.0%ni,  0.1%id, 14.3%wa,  0.0%hi,  0.2%si,  0.0%st
#       user      system    nice     idle   I/O wait hardware  software  steal
#                                                    interrupt interrupt
```

* PR
    * priority
* NI
    * nice
    * 相対優先度
    * 0が基準で、負だと優先度が高く、正だと優先度が低い。
* VIRT
    * virtual memory
* RES
    * Resident
    * スワップしていない、使用した物理メモリのサイズ。
* SHR
    * shared memory
    * 他のプロセスと共有される可能性のあるメモリのサイズ。
* S
    * state
    * D: 割り込み不能
    * R: 実行中
    * S: スリープ状態
    * T: 停止中
    * Z: ゾンビプロセス
* %CPU
    * CPU使用率
* %MEM
    * メモリ使用率
* TIME+
    * 実行時間


## Commands
top実行中


* `h`
    * helpを表示
* `H`
    * 全thread表示/非表示
* `V`
    * tree形式でProcessの関係を表示
* `E`
    * summaryのMemory scaleを変更
* `e`
    * processのMemoryの単位を変更
* `F`
    * fieldを選択できる
    * sortするfieldの選択もできる
    * 矢印キーでソートしたいfieldを選択して、`s`を



## Reference
* [topコマンドの使い方 - Qiita](http://qiita.com/k0kubun/items/7368c323d90f24a00c2f)
