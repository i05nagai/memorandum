---
title: QUADPACK
---

## QUADPACK
numerical integration library written in fortran77.

## Methods
* qags
* qagi
    * general-purpose routine for infinite intervals
    * inifite interval is mapped to (0, 1]
    * use `qags` with 15-point
* qng
    * simple non-adaptive integrator
* qag
* qagp
* qawo
* qawf
* qas
* qawc



## Tips

### Hisotry
[Is QUADPACK kept up to date with the state\-of\-the\-art in numerical integration? \- Mathematics Stack Exchange](https://math.stackexchange.com/questions/2184821/is-quadpack-kept-up-to-date-with-the-state-of-the-art-in-numerical-integration)

* QUADPACK is not maintained anymore
* last update is in 1987
* GNU Scientific Library reimplement QUADPACK
* written in fortran77
* GSL documentation is helpful
    * [Numerical Integration — GSL 2\.5 documentation](https://www.gnu.org/software/gsl/doc/html/integration.html#qng-non-adaptive-gauss-kronrod-integration)

## Reference
* [quadpack](http://www.netlib.org/quadpack/)
* [QUADPACK \- Wikipedia](https://en.wikipedia.org/wiki/QUADPACK)
