---
title: Pillow
---

## Pillow

## Install

```
pip install Pillow
```

## API

### Filter

```python
from PIL import ImageFilter
im1 = im.filter(ImageFilter.BLUR)
im2 = im.filter(ImageFilter.MinFilter(3))
im3 = im.filter(ImageFilter.MinFilter)  # same as MinFilter(3)
```

* BLUR
* CONTOUR
* DETAIL
* EDGE_ENHANCE
* EDGE_ENHANCE_MORE
* EMBOSS
* FIND_EDGES
* SMOOTH
* SMOOTH_MORE
* SHARPEN

## Tips

* check format

```python
img = Image.open(filename)
print(img.format)  # 'JPEG'
```

* show image

```python
img = Image.open(filename)
img.show()
```

* show image in jupyter-notebook

```python
from matplotlib.pyplot import imshow
import numpy as np
from PIL import Image

%matplotlib inline
pil_im = Image.open('data/empire.jpg', 'r')
imshow(np.asarray(pil_im))
```

## Reference
* [Pillow — Pillow (PIL Fork) 4.3.0 documentation](https://pillow.readthedocs.io/en/4.3.x/)
