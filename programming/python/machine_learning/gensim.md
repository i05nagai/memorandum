---
title: Gensim
---

## Gensim

```
pip install gensim
```

## Computing loss
* gensimのword2vecはloss functionは下記issueで実装されている
    * https://github.com/RaRe-Technologies/gensim/blob/develop/gensim/models/word2vec.py#L440 で`compute_loss=True`を指定する
    * [gensim issue](https://github.com/RaRe-Technologies/gensim/issues/999)
    * [gensim issue](https://github.com/RaRe-Technologies/gensim/pull/1201)
* gensimのdoc2vecはloss functionの表示に対応していない
    * 以下の計算部分でのlossの計算が実装されていない
      * https://github.com/RaRe-Technologies/gensim/blob/develop/gensim/models/doc2vec.py#L81
    * word2vec側は実装されている
      * https://github.com/RaRe-Technologies/gensim/blob/develop/gensim/models/word2vec.py#L147

## logging
以下でlogggingがonになる。

```
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
```

## API
* [gensim: API Reference](https://radimrehurek.com/gensim/apiref.html)

* `gensim.models.doc2vec.Doc2Vec(documents=None, dm_mean=None, dm=1, dbow_words=0, dm_concat=0, dm_tag_count=1, docvecs=None, docvecs_mapfile=None, comment=None, trim_rule=None, **kwargs)`
    * `dm`
        * training algorithm
        * 1 = distribuited memory
        * otherwise = distributed bag of words
    * size
        * feature vectorのdimesionality
    * worker
        * threadの数
    * window
        * maximum distance between predicted word and context words
        * 学習に使う前後のword
    * seed
        * seed of random number genrator
    * alplha
        * initial learning rate
    * min_words
        * 出現頻度がこれ以下の単語は無視
    * max_vocab_size
        * Noneがno limit
    * sample
    * iter
        * num of iteration

## Tips

### Show 

```python
# define
# documents
# trim_rule
# num_iter
doc2vec = Doc2Vec(None, size=100, window=8, min_count=5, workers=4, trim_rule=trim_rule, iter=num_iter)
doc2vec.build_vocab(documents, trim_rule=trim_rule)
doc2vec.train(
    documents,
    total_examples=doc2vec.corpus_count,
    epochs=num_iter,
    compute_loss=True)
```

### Optimizing word2vec
* [Word2vec in Python, Part Two: Optimizing | RaRe Technologies](https://rare-technologies.com/word2vec-in-python-part-two-optimizing/)

## Reference
* [gensim: Topic modelling for humans](https://radimrehurek.com/gensim/)
* [gensim/doc2vec-lee.ipynb at develop · RaRe-Technologies/gensim](https://github.com/RaRe-Technologies/gensim/blob/develop/docs/notebooks/doc2vec-lee.ipynb)
