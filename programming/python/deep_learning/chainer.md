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


* chainer.dataset.concat_examples(batch, device=None, padding=None)
    * [chainer.dataset.concat_examples — Chainer 3.0.0 documentation](http://docs.chainer.org/en/stable/reference/core/generated/chainer.dataset.concat_examples.html#chainer.dataset.concat_examples)
    * exampleが`(x, y)`でbatchが`[(x1, y1), (x2, y2)]`のとき`x1`と`x2`を一つのarrayにして、`y1`と`y2`を一つのarrayにする



* resnet.predict
    * https://github.com/chainer/chainer/blob/master/chainer/links/model/vision/resnet.py#L440

* `chainer.links.Convolution2D(self, in_channels, out_channels, ksize=None, stride=1, pad=0, nobias=False, initialW=None, initial_bias=None)`
    * in_channels
    * out_channels
    * ksize
        * kernel size
    * stride
    * pad
    * nobias
    * initialW
    * initial_bias

* chainer.functions.convolution_2d(x, W, b=None, stride=1, pad=0, cover_all=False)[source]
    * [chainer.functions.convolution_2d — Chainer 3.0.0 documentation](http://docs.chainer.org/en/stable/reference/generated/chainer.functions.convolution_2d.html)
    * Convolution2DFunctionを読んでapplyしている

* `class chainer.FunctionNode`
    * [chainer.FunctionNode — Chainer 3.0.0 documentation](http://docs.chainer.org/en/stable/reference/core/generated/chainer.FunctionNode.html#chainer-functionnode)
    * apply時にinputsの要素は全て`Variable`に変換される
    * forward_cpuかfoward_gpuがだいたい実行される

* class chainer.Variable(data=None, *, name=None, grad=None, requires_grad=True)[source]
    * [chainer.Variable — Chainer 3.0.0 documentation](http://docs.chainer.org/en/stable/reference/core/generated/chainer.Variable.html#chainer.Variable)
    * `.data`はndarrayにもあるので、`.data`を直接呼ぶのではなく`array`を呼べはndarrayと混同することをさけることができる

* chainer.as_variable
    * [chainer.as_variable — Chainer 3.0.0 documentation](http://docs.chainer.org/en/stable/reference/core/generated/chainer.as_variable.html)
    * Variableならreturn
    * そうでなければVariable(x)

* chainer.cuda.get_device_from_array(*arrays)
    * [chainer.cuda.get_device_from_array — Chainer 3.0.0 documentation](http://docs.chainer.org/en/stable/reference/util/generated/chainer.cuda.get_device_from_array.html#chainer.cuda.get_device_from_array) o
    * [chainer/cuda.py at v3.0.0 · chainer/chainer](https://github.com/chainer/chainer/blob/v3.0.0/chainer/cuda.py#L91)
    * DummyDeviceTypeかndarray.deviceが変える

chainer.util

* chainer.util.conv.py
    * [chainer/conv.py at master · chainer/chainer](https://github.com/chainer/chainer/blob/master/chainer/utils/conv.py)
    * `im2col_cpu(img, kh, kw, sy, sx, ph, pw, pval=0, cover_all=False, dy=1, dx=1, out_h=None, out_w=None)`

## Tips
* source codeの`xp`はnumpyのnpかcupyのcpの一方を表している


## Reference
* [chainer-ResNet/predict.py at master · yasunorikudo/chainer-ResNet](https://github.com/yasunorikudo/chainer-ResNet/blob/master/v2/predict.py)
