---
title: Corlo Image Processing an Applications
---

## Corlo Image Processing an Applications

## 1.1 Basics of Color Vision

* Wavelengths
    * 400nm to 700nm
* Spectral Power distribution

The human retina has three types of color phot-ceptor cells, called cones.

* cone
    * 3 types of color photo-receptor cless
* roads
    * 4-th type of photo-receptor
    * only effective at extremely low light levels
* CIE
    * Commission Internationale de L'Eclairage
    * 国際照明委員会
* Intensity
    * $I$
    * Unit is [Watts/m2]
* Brightness
    * $Br$
    * attribute of a visual sensation according to which an area appears to emit or less light
* Luminance
    * $Y$
    * defined by CIE since Brightness perception is very complex
    * radient power weighted by a spectral sensitivity function based on human vision
* Lightness
    * $L^{*}$
    * 
* Hue
    * $H$
* Saturation
    * $S$

Typ of color models

1. Colorimetric color models
2. Psychophysical color models
3. Physiologically inspired color moels
4. Opponent color models

Type of color models in image processing applications

1. Device-oriented color models
2. User-oriented color models
3. Device-indepedent color models


Color spaces

* HSL/HLS
    * Hue Saturation Lightness
    * color space
    * Human interepret a color based on its lightness, hue and saturation.
* CIE XYZ
    * $Y$ is luminance
    * device independent color space
    * useful for color management purpose
    * seldom used in image processing applications
    * derives other color spaces
* non-linear RGB
    * traditionally used for color image processing/analysis/storage
    * R/G/B colors are called primary colors
* YIQ
    * North Americal TV standard
    * used in computer graphics
* HSI
    * Hue Saturation and Intensity
    * used in computer graphics
* Hue Saturation Value
    * used in computer graphics

## 1.2. The CIE Chromaticity-based Models

* $$\Lambda := [380\mathrm{nm}, 780\mathrm{nm}]$$,
* $$S_{i}(\lambda)$$ $(i = 1, 2, 3)$
    * Absorption spectra for each cones
* $$S_{1}$$,
    * peak in the yellow-greeen
* $$S_{2}$$,
    * peak in the green
* $$S_{3}$$,
    * peak in the blue
* $C$
    * color
* $C: \Lambda \rightarrow \mathbb{R}$,
    * spectral energy distribution of color $C$
* $C_{i}$
    * $i$ th primary color
* $C_{i}:\Lambda \rightarrow \mathbb{R}$
    * SPectral Distribution for color $i$
    * Weight provided by absorption spectra for each wavelengths
* $\alpha_{i}$ $(i = 1 ,2, 3)$
    * Color sansation for color $i$
    * defined below based on young's theory
* $\beta_{k}$ $(k = 1, 2, 3)$,
    * weight of color combination

Assumption that three primary colors $$C_{k}$$ with Spectral Dstribution $$C_{k}(\lambda)$$ are available and let

$$
    \int_{\Lambda}
        C_{k}(\lambda)
    \ d\lambda
    =
    1
$$

Young's model assums that spectral energy distribution $C(\lambda)$ for color $C$ is linear combination of spectral distributions $C_{i}(\lambda)$ for primary colors $C_{i}$.

$$
\begin{equation}
    \alpha_{i}(C)
    :=
    \int_{\Lambda}
        S_{i}(\lambda)
        C_{i}(\lambda)
    \ d\lambda
    \label{chap01_01_01}
\end{equation}
$$

$$
\begin{eqnarray}
    \alpha_{i}(C)
    & := &
        \int_{\Lambda}
            \left(
                \sum_{k=1}^{3}
                    \beta_{k}
                    C_{k}(\lambda)
            \right)
            S_{i}(\lambda)
        \ d \lambda
    \nonumber
    \\
    & = &
        \sum_{k=1}^{3}
            \beta_{k}
            \int_{\Lambda}
                C_{k}(\lambda)
                S_{i}(\lambda)
            \ d \lambda
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \alpha_{i, k}
    & := &
        \alpha_{i}(C_{k})
    \nonumber
    \\
    & = &
        \int_{\Lambda}
            S_{i}(\lambda)
            C_{k}(\lambda)
        \ d\lambda
        \label{chap01_01_04}
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \sum_{k=1}^{3}
        \beta_{k} \alpha_{i, k}
    & = &
        \alpha_{i}(C)
    \nonumber
    \\
    & = &
        \int_{\Lambda}
            S_{i}(\lambda)
            C(\lambda)
        \ d\lambda
        \label{chap01_01_05}
\end{eqnarray}
$$

$$\beta_{k}$$ is obtained from $$\eqref{chap01_01_04}$$ and $$\eqref{chap01_01_05}$$.

* $w_{k}: \Lambda \rightarrow \mathbb{R}$,
    * 


## Reference
