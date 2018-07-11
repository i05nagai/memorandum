---
title: QUADPACK
---

## QUADPACK
numerical integration library written in fortran77.

## Methods
* method endign in `e`
    * more detailed version with a name ending in E, as `dqage`.
    * These provide more information and control than the easier versions.


* qags
* qagi
    * general-purpose routine for infinite intervals
    * inifite interval is mapped to (0, 1]
    * use `qags` with 15-point
* qng
    * simple non-adaptive integrator
* qag
    * simple adaptive integrator
* qagp
* qawo
* qawf
* qas
* qawc
* `dqk15i.f`
    * 15 point rule for (semi)infinite interval.
* `qk15w.f`
    * 15 point rule for special singular weight functions.
* `dqc25c.f`
    * 25 point rule for Cauchy Principal Values
* `dqc25f.f`
    * 25 point rule for sin/cos integrand.
* `dqmomo.f`
    * Integrates k-th degree Chebychev polynomial times function with various explicit singularities.



## Tips

### Hisotry
[Is QUADPACK kept up to date with the state\-of\-the\-art in numerical integration? \- Mathematics Stack Exchange](https://math.stackexchange.com/questions/2184821/is-quadpack-kept-up-to-date-with-the-state-of-the-art-in-numerical-integration)

* QUADPACK is not maintained anymore
* last update is in 1987
* GNU Scientific Library reimplement QUADPACK
* written in fortran77
* GSL documentation is helpful
    * [Numerical Integration — GSL 2\.5 documentation](https://www.gnu.org/software/gsl/doc/html/integration.html#qng-non-adaptive-gauss-kronrod-integration)

### Meaning of prefixm

* Q- quadrature routine

* N - non-adaptive integrator
* A - adaptive integrator

* G - general integrand (user-defined)
* W - weight function with integrand

* S - singularities can be more readily integrated
* P - points of special difficulty can be supplied
* I - infinite range of integration
* O - oscillatory weight function, cos or sin
* F - Fourier integral
* C - Cauchy principal value

## Reference
* [quadpack](http://www.netlib.org/quadpack/)
* [QUADPACK \- Wikipedia](https://en.wikipedia.org/wiki/QUADPACK)
