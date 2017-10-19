
---
title: Chainer
---

## Chainer

## API

* `chainer.training.StandardUpdater(iterator, optimizer, converter=<function concat_examples>, device=None, loss_func=None)`
    * [chainer.training.StandardUpdater — Chainer 3.0.0 documentation](https://docs.chainer.org/en/stable/reference/core/generated/chainer.training.StandardUpdater.html#chainer.training.StandardUpdater)
    * converterで変換される
    * batchはconcat_exampelsで`[(x1, y1), (x2, y2), ...]`のarrayから要素ごとにjoinされた`(x12, y12)`のarrayになる
    * dictもうけつけている

* `to_device(device, x):`
    * [chainer/convert.py at 3dd6ff662d187c29391b4e276f2ee859ff38c0f7 · chainer/chainer · GitHub](https://github.com/chainer/chainer/blob/3dd6ff662d187c29391b4e276f2ee859ff38c0f7/chainer/dataset/convert.py#L7)

* `concat_examples`
    * batch処理する場合`[(x1, y1), (x2, y2), ...]`を`concat_examples`したものを入力として渡す

* `convert._concat_arrays`

* `chainer.cuda.get_array_module(*args)`
    * [chainer.cuda.get_array_module — Chainer 3.0.0 documentation](https://docs.chainer.org/en/stable/reference/util/generated/chainer.cuda.get_array_module.html#chainer.cuda.get_array_module)
    * numpyかcupyかを返す
    * cupyが利用可能ならcupyのget_array_moduleの戻り値, そうでなければnumpyを返す


## Tips
* source codeの`xp`はnumpyのnpかcupyのcpの一方を表している


## Reference

