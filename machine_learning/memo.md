## Memo for machine learning

* 大量のdataを処理中のresumeの機能
* 出力fileはsuffixで区別するように、suffixを引数で受け取る
    * suffixにはparameterや手法の名前をいれて、区別する
    * e.g. `word_count<suffix>.csv`
* NLPで良くある集計
    * 単語の出現頻度を数える
    * 各単語の出現位置を数える
    * 単語の出現回数をgroupingして数える
        * 0-1回出現した単語
        * 2-5回出現した単語
    * 1文の単語の総数を数える
    * 形態素解析した結果
* 形態素解析
* これらの集計のscriptは小さいdataでtestしたい
    * samplingがいる
* 200GBのstorageがあるとは思って良い
* memoryは8GB以下くらいを想定する
