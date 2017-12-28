---
title: Chromium
---

## Chromium
Source code

```
git clone https://chromium.googlesource.com/chromium/src
```

### CSS
画像処理部分は`skia image library`を使っている。
`src/cc/paint`にCSSのfilter部分のcodeがある。
`render_surface_filters.cc`にfilterのcolor matrixの定義がある。
matrixはsize201次元配列で書かれている。
添字の対応は以下のようになる。

$$
\left(
    \begin{array}{ccccc}
        a_{0} &
        a_{1} &
        a_{2} &
        a_{3} &
        a_{4}
        \\
        a_{5} &
        a_{6} &
        a_{7} &
        a_{8} &
        a_{9}
        \\
        a_{10} &
        a_{11} &
        a_{12} &
        a_{13} &
        a_{14}
        \\
        a_{15} &
        a_{16} &
        a_{17} &
        a_{18} &
        a_{19}
    \end{array}
\right)
$$

Brightness

$$
\left(
    \begin{array}{ccccc}
        s &
        0 &
        0 &
        0 &
        0
        \\
        0 &
        s &
        0 &
        0 &
        0
        \\
        0 &
        0 &
        s &
        0 &
        0
        \\
        0 &
        0 &
        0 &
        1.0 &
        0
    \end{array}
\right)
$$

Contrast

$$
\left(
    \begin{array}{ccccc}
        s &
        0 &
        0 &
        0 &
        (-0.5s + 0.5) \times 255
        \\
        0 &
        s &
        0 &
        0 &
        (-0.5s + 0.5) \times 255
        \\
        0 &
        0 &
        s &
        0 &
        (-0.5s + 0.5) \times 255
        \\
        0 &
        0 &
        0 &
        1.0 &
        0
    \end{array}
\right)
$$

Saturation

$$
\begin{eqnarray}
    & &
    \left(
        \begin{array}{ccccc}
            0.213 + 0.787s &
            0.715 - 0.715s &
            1.0 - (0.213 + 0.787s + 0.715 - 0.715s) &
            0 &
            0
            \\
            0.213 - 0.213s &
            0.715 + 0.285s &
            1.0 - (0.213 - 0.213s + 0.715 + 0.285s) &
            0 &
            0
            \\
            0.213 - 0.213s &
            0.715 - 0.715s &
            1.0 - (0.213 - 0.213s + 0.715 - 0.715s) &
            0 &
            0
            \\
            0 &
            0 &
            0 &
            1.0 &
            0
        \end{array}
    \right)
    \\
    & = &
    \left(
        \begin{array}{ccccc}
            0.213 + 0.787s &
            0.715 - 0.715s &
            0.072 - 0.072s &
            0 &
            0
            \\
            0.213 - 0.213s &
            0.715 + 0.285s &
            0.072 - 0.072s &
            0 &
            0
            \\
            0.213 - 0.213s &
            0.715 - 0.715s &
            0.072 + 0.928s &
            0 &
            0
            \\
            0 &
            0 &
            0 &
            1.0 &
            0
        \end{array}
    \right)
\end{eqnarray}
$$

## Reference
