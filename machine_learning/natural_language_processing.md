---
title: Natural Language Processing
---

## Natural Language Processing


### Stemming
* runningなどの品詞をrunなどになおす
* Porter stemming
* Snowball stemming (Porter2 or English stemming)

### stop-word removal
* `and, is, has`などを削除
* [簡易的な日本語ストップワードの取得メソッド - test.py](http://testpy.hatenablog.com/entry/2016/10/05/004949)

http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt

### TF-IDF
* TFはdoumentに現れる単語の頻度
* IDFは全部のdocumentに単語が現れた比率の逆数
* 多くの文書に出てる単語は重要でない

## Preprocessing

### Best practice
* [Data preparation for doc2vec - Google Groups](https://groups.google.com/forum/#!topic/gensim/17Knu4Xoe9U)
* [自然言語処理における前処理の種類とその威力 - Qiita](https://qiita.com/Hironsan/items/2466fe0f344115aff177)
* [Python3×日本語：自然言語処理の前処理まとめ - Qiita](https://qiita.com/chamao/items/7edaba62b120a660657e)
* [Regexp.ja · neologd/mecab-ipadic-neologd Wiki](https://github.com/neologd/mecab-ipadic-neologd/wiki/Regexp.ja)
* [sentencepiece/normalization.md at master · google/sentencepiece](https://github.com/google/sentencepiece/blob/master/doc/normalization.md)


### emoticon
* [Emoji Sentiment Ranking v1.0](http://kt.ijs.si/data/Emoji_sentiment_ranking/)


## Reference
* [詳解 LOUDS (12) trie として使う - アスペ日記](http://d.hatena.ne.jp/takeda25/20120421/1335017170)
* [日本語形態素解析の裏側を覗く！MeCab はどのように形態素解析しているか - クックパッド開発者ブログ](http://techlife.cookpad.com/entry/2016/05/11/170000)
* [MeCab ソースコードリーディング私的メモ（形態素解析編） - あらびき日記](https://abicky.net/2016/05/16/061221/)

