---
title: Keras
---

## Keras

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


## Reference
* [Keras Documentation](https://keras.io/ja/)
* 
