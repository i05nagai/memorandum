---
title: LaTeX
---

## LaTeX

## Tips

### Font T1/cmr/m/n/10=ecrm1000 at 10.0pt not loadable: Metric (TFM) file not fou

`tlmgr search --file ecrm1000.tfm --global`

```
! Font T1/cmr/m/n/10=ecrm1000 at 10.0pt not loadable: Metric (TFM) file not fou
nd.
<to be read again>
                   relax
                   l.105 \fontencoding\encodingdefault\selectfont

                   pandoc: Error producing PDF
```

下記で必要なパッケージをインストール。

`tlmgr install ec`

* [Error in TeX Live – Font ... not loadable: Metric (TFM) file not found - TeX - LaTeX Stack Exchange](http://tex.stackexchange.com/questions/75166/error-in-tex-live-font-not-loadable-metric-tfm-file-not-found)


### Cannot determine type of tlpdb from /root/texmf!

```
Cannot determine type of tlpdb from /root/texmf!
cannot setup TLPDB in /root/texmf at /usr/bin/tlmgr line 5713.
The command '/bin/sh -c tlmgr install ec' returned a non-zero code: 2
```

## Reference
* [oda_tex.dvi](https://www.math.tohoku.ac.jp/tmj/oda_tex.pdf)

