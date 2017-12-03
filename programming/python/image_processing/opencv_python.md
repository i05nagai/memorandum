---
title: OpenCV python
---

## OpenCV

```
pip install opencv-python
```

```python
import numpy as np
import cv2


def show_img(img):
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Load an color image in grayscale
img = cv2.imread('messi5.jpg',0)
```

## Reference
* [Python版OpenCV入門](http://opencv.blog.jp/python/nyumon)
* [OpenCV: OpenCV-Python Tutorials](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)

