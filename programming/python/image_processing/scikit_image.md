---
title: scikit-image
---

## scikit-image

## API

* skimage.io.imread
    * [Module: io — skimage v0.14dev docs](http://scikit-image.org/docs/dev/api/skimage.io.html#skimage.io.imread)
    * Return
        * GrayImage: MxN
        * RGB: MxNx3
        * RGBA: MxNx4

* skimage.exposure.adjust_gamma()
* skimage.exposure.equalize_adapthist(image, kernel_size=None, clip_limit=0.01, nbins=256, **kwargs)
    * color imageの場合はRGB->HSVに変換して、VをequalizeしてRGBに戻す
* skimage.exposure.equalize_hist(image[, …])
* skimage.exposure.histogram(image[, nbins])
    * return:
        * hist: array
        * bin_centers: array

* skimage.transpose.resize(image, output_shape, order=1, mode=None, cval=0, clip=True, preserve_range=False)
    * 画像のresize
    * output_shape
        * tuple of ndarray (rows, cols[, dim])
        * channelは省略可能、省略すると保持される

## Reference

