---
title: Keras
---

## Keras

### Directory
* [Building powerful image classification models using very little data](https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html)

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

## Fin

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


* 
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

## Reference
* [Keras Documentation](https://keras.io/ja/)
* [Codes of Interest: Using Bottleneck Features for Multi-Class Classification in Keras and TensorFlow](http://www.codesofinterest.com/2017/08/bottleneck-features-multi-class-classification-keras.html)

