---
title: Keras
---

## Keras

### Directory
* [Building powerful image classification models using very little data](https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html)


## API

* keras.models.Sequential
    * layer instanceの

```
model = Sequential([
    Dense(32, input_shape=(784,)),
    Activation('relu'),
    Dense(10),
    Activation('softmax'),
])
```

* ImageDataGenerator
    * http://aidiary.hatenablog.com/entry/20161212/1481549365
    * https://keras.io/preprocessing/image/
    * featurewise_center
    * simplewise_center
    * featurewise_std_normalization
    * simplewise_std_normalization
    * rescale
        * 他のtransformationをする前にdataにかけるfactor
    * preprocessing_function
        * 他のtransformationを実行する前に適用する関数
        * 引数は3dim numpy array

```python
keras.preprocessing.image.ImageDataGenerator(
    featurewise_center=False,
    samplewise_center=False,
    featurewise_std_normalization=False,
    samplewise_std_normalization=False,
    zca_whitening=False,
    rotation_range=0.,
    width_shift_range=0.,
    height_shift_range=0.,
    shear_range=0.,
    zoom_range=0.,
    channel_shift_range=0.,
    fill_mode='nearest',
    cval=0.,
    horizontal_flip=False,
    vertical_flip=False,
    rescale=None,
    dim_ordering=K.image_dim_ordering())
```

```
data/
    train/
        dogs/
            dog001.jpg
            dog002.jpg
            ...
        cats/
            cat001.jpg
            cat002.jpg
            ...
    validation/
        dogs/
            dog001.jpg
            dog002.jpg
            ...
        cats/
            cat001.jpg
            cat002.jpg
            ...
```

* ImageDataGenerator.flow_from_directory
    * derectory名を辞書順にsortして、順にfileを読んでいく
    * 上の例では、1 epochの順で以下の順で読み込まれ、読み込む際にaugumentationの設定に基いて画像を変換する
        * dogs/dog001.jpg
        * dogs/dog002.jpg
        * cats/cat001.jpg
        * cats/cat002.jpg


* `from keras.utils.np_utils import to_categorical`
    * 一次元の整数labelのarryaから2次元の0-1のvectorに変換する

```
# from
[0, 1, 2, 1]
# to
[
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [0, 1, 9],
]
```

* `fit`
    * `x`
        * numpy array
        * 入力のlayerが複数あるときはlist of numpy array、多次元であってもlayerが1つならnumpy array
    * `batch_size`
        * Integer/None
        * defaultは32
    * `epochs`
        * Integer
        * 1 epochで全て`(x, y)`のdataを1度学習に使う
    * `steps_per_epoch`
        * interger/None
        * number of unique samples / batch_size
        * `None`だと,sampleをbatch sizeで割ったもの
    * `validation_split`
        * [0, 1]で指定
        * `x`の一部を`validation_data`にする
    * `validation_data`
        * generator for validation data
        * tuple `(inputs, labels)` or
        * tuple `(inputs, labels, sample_weights)`
        * modelの学習には使われない
    * `validation_steps`
        * `steps_per_epoch`が指定された場合のみ意味をもつ
        * batchを適用する回数
    * `shuffle`
        * `True`の場合は、epochの前にtraining dataをshuffleする
        * `'batch'`を指定した場合は、batchごとにshuffleする

* `fit_generator(self, generator, steps_per_epoch=None, epochs=1, verbose=1, callbacks=None, validation_data=None, validation_steps=None, class_weight=None, max_queue_size=10, workers=1, use_multiprocessing=False, shuffle=True, initial_epoch=0)`
    * `generator`
    * `steps_per_epoch`
        * number of unique samples / batch_size
        * `None`にはできない
    * `validation_data`
        * generator for validation data
        * tuple (inputs, labels)
        * tuple (inputs, labels, sample_weights)
    * `validation_steps`
        * `validation_data`が`generator`の場合のみ意味をもつ
        * epochの終了時にvalidationに使うvalidationの数
        * 通常validtion dataのsample数と同じ

## Dataset
* [Datasets - Keras Documentation](https://keras.io/datasets/)

### CIFAR10

* Dataset of 50,000 32x32 color training images
* labeled over 10 categories, and 10,000 test images.

```
from keras.datasets import cifar10
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
```

* x_train, x_test
    * uint8 array of RGB image data with shape (num_samples, 3, 32, 32).
* y_train, y_test
    * uint8 array of category labels (integers in range 0-9) with shape (num_samples,).

### CIFAR100

* Dataset of 50,000 32x32 color training images
* labeled over 100 categories, and 10,000 test images.

```
from keras.datasets import cifar100
(x_train, y_train), (x_test, y_test) = cifar100.load_data(label_mode='fine')
```

### IMDB Movie reviews sentiment classification
* Dataset of 25,000 movies reviews from IMDB
* labeled by sentiment (positive/negative)

```python
from keras.datasets import imdb

(x_train, y_train), (x_test, y_test) = imdb.load_data(path="imdb.npz",
                                                      num_words=None,
                                                      skip_top=0,
                                                      maxlen=None,
                                                      seed=113,
                                                      start_char=1,
                                                      oov_char=2,
                                                      index_from=3)
```

* x_train, x_test
    * list of sequences, which are lists of indexes (integers).
    * If the num_words argument was specific, the maximum possible index value is num_words-1. If the maxlen argument was specified, the largest possible sequence length is maxlen.
* y_train, y_test
    * list of integer labels (1 or 0).
    * positive or negative
* path
    * if you do not have the data locally (at '~/.keras/datasets/' + path), it will be downloaded to this location.
* num_words
    * integer or None
    * Top most frequent words to consider. Any less frequent word will appear as oov_char value in the sequence data.
* skip_top
    * integer.
    * Top most frequent words to ignore (they will appear as oov_char value in the sequence data).
* maxlen
    * int.
    * Maximum sequence length. Any longer sequence will be truncated.
* seed
    * int.
    * Seed for reproducible data shuffling.
* start_char
    * int.
    * The start of a sequence will be marked with this character. Set to 1 because 0 is usually the padding character.
* oov_char
    * int.
    * words that were cut out because of the num_words or skip_top limit will be replaced with this character.
* index_from
    * int.
    * Index actual words with this index and higher.

### Reuters newswire topics classification

### MNIST database of handwritten digits

### Fashion-MNIST database of fashion articles

### Boston housing price regression dataset

## Data Augmentation

## Fine tuning
* [Building powerful image classification models using very little data](https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html)
* [Fine-tuning a Keras model. Updated to the Keras 2.0 API. · GitHub](https://gist.github.com/fchollet/7eb39b44eb9e16e59632d25fb3119975)
* [Updated to the Keras 2.0 API. · GitHub](https://gist.github.com/fchollet/f35fbc80e066a49d65f1688a7e99f069)

## Layer
* Dense(units, activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)
    * 以下の計算をするlayer
    * unitsは出力のvectorの次元
    * activationを指定しない場合は、恒等関数
    * `output = activation(dot(input, kernel) + bias)`
        * kernelはweight matrix
        * biasのvector

* Flattern()

```python
model = Sequential()
model.add(Conv2D(64, 3, 3,
         border_mode='same',
         input_shape=(3, 32, 32)))
# now: model.output_shape == (None, 64, 32, 32)
model.add(Flatten())
# now: model.output_shape == (None, 65536)
```

* `Conv2D(filters, kernel_size, strides=(1, 1), padding='valid', data_format=None, dilation_rate=(1, 1), activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)`


## one-hot vector
整数でclass表現したものを、0, 1のvectorに変更する。
kerasではto_categoricalで整数でcategory付したものを0, 1のvector表現に変更できる。

```python
from keras.utils.np_utils import to_categorical
labels = []
for i in range(3):
    labels += [i] * 2
# [0, 0, 1, 1, 2, 2]
# [
#     [1, 0, 0],
#     [1, 0, 0],
#     [0, 1, 0],
#     [0, 1, 0],
#     [0, 0, 1],
#     [0, 0, 1],
# ]
labels = to_categorical(labels)
```

```
ValueError: You are passing a target array of shape (1536, 1) while using as loss `categorical_crossentropy`. `categorical_crossentropy` expects targets to be binary matrices (1s and 0s) of shape
(samples, classes). If your targets are integer classes, you can convert them to the expected format via:
from keras.utils.np_utils import to_categorical
y_binary = to_categorical(y_int)
```

### Change the number of CPU core

```python
config = tf.ConfigProto(
    intra_op_parallelism_threads=1,
    inter_op_parallelism_threads=1,
    allow_soft_placement=True,
    device_count = {'CPU': 1})
session = tf.Session(config=config)
K.set_session(session)
```

### from Caffe to Keras
* [Converting a Deep learning model from Caffe to Keras - Nicolò Valigi](http://nicolovaligi.com/converting-deep-learning-model-caffe-keras.html)
* [GitHub - ethereon/caffe-tensorflow: Caffe models in TensorFlow](https://github.com/ethereon/caffe-tensorflow)

```
docker run -ti --rm bvlc/caffe:cpu caffe --version
```

```
git clone https://github.com/ethereon/caffe-tensorflow.git
cd caffe-tensorflow
python convert.py \
  --caffemodel=/path/to/caffeweight.caffemodel \
  --code-output-path=./pascal_voc_tf/keras.py \
  --data-output-path=./pascal_voc_tf/ \
  /path/to/caffelayer.prototxt
```

### Memory usage
* [Keras shoot-out, part 2: a deeper look at memory usage](https://medium.com/@julsimon/keras-shoot-out-part-2-a-deeper-look-at-memory-usage-8a2dd997de81)
* [TensorflowでGPUを制限・無効化する - Qiita](https://qiita.com/kikusumk3/items/907565559739376076b9)
* [Python: Keras/TensorFlow で GPU のメモリを必要な分だけ確保する - CUBE SUGAR CONTAINER](http://blog.amedama.jp/entry/2017/06/07/220723)
* [EMR上でPython3系でpysparkする - Qiita](https://qiita.com/uryyyyyyy/items/672a4058aba754b389d1)
* [memory leak when using tensorflow · Issue #2102 · keras-team/keras](https://github.com/keras-team/keras/issues/2102)

backendごとに設定する。

```python
from keras.models import load_model
from keras.backend import backend

def set_tensorflow_config(
        allow_growth=True,
        num_gpu=1,
        per_process_gpu_memory_fraction=1.0):
        import tensorflow as tf
        from keras.backend.tensorflow_backend import set_session

        gpu_options = tf.GPUOptions(allow_growth=allow_growth)
        gpu_options.per_process_gpu_memory_fraction = per_process_gpu_memory_fraction
        visible_device_list = ",".join(str(i) for i in range(num_gpu))
        gpu_options.visible_device_list = visible_device_list

        config = tf.ConfigProto(gpu_options=gpu_options)
        session = tf.Session(config=config)
        set_session(session)
```

sessionのclearをする。
backendのmemoryが開放されるかは、backendによるので明示的にmemoryを開放するには、`K.clear_session()`をする。

```python
import keras.backend as K

K.clear_session()
```

## Reference
* [Keras Documentation](https://keras.io/ja/)
* [Codes of Interest: Using Bottleneck Features for Multi-Class Classification in Keras and TensorFlow](http://www.codesofinterest.com/2017/08/bottleneck-features-multi-class-classification-keras.html)
* [Useful Keras features – Towards Data Science – Medium](https://medium.com/towards-data-science/https-medium-com-manishchablani-useful-keras-features-4bac0724734c)

