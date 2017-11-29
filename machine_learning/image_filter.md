---
title: Image Filter
---

## Image Filter


Intensity = (R + G + B) / 3

YCbCr

```
Y = 0.2126*R + 0.7152*G + 0.0722*B
```
o

## Blend mode
* https://en.wikipedia.org/wiki/Blend_modes

Here color is between 0.0(black) and 1.0(white).

Normal

$$
    f(a, b) = b
$$

Dissolve

$$
    
$$

Multiply

$$
    f(a, b) = ab
$$

Screen

$$
    f(a, b)
    =
    1 - (1 - a)(1 - b)
$$

Overlay

$$
    f(a, b)
    =
    \begin{cases}
        2ab
        &
        a < 0.5
        \\
        1 - 2(1 - a)(1 - b)
        &
        a >= 0.5
    \end{cases}
$$

Hard Light

Soft Light

Dodge and burn

Divide

Addition

Subtract

Difference

Darken Only

Lighten Only


## Reference
* https://dunnbypaul.net/blends/
* https://stackoverflow.com/questions/15007304/histogram-equalization-not-working-on-color-image-opencv
