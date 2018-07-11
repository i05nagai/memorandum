---
title: scipy integrate
---

## scipy integrate


## API


### quad
Implemented in `quadpack.py`, which is wrapper for quadpack written in fortran.

* `dblquad`
    * `quad` for 2-dim
* `tplquad`
    * `quad` for 3-dim
    * call `nquad`
* `nquad`
    * `quad` for n-dim
    * wrapper of `quad`
    * [scipy\.integrate\.nquad — SciPy v1\.1\.0 Reference Guide](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.nquad.html#scipy.integrate.nquad)


* `def nquad(func, ranges, args=None, opts=None, full_output=False):`
    * `ranges`
        * `((a1, b1), ..., (an, bn))`

* `nquad->NQuad->quad`
    * `->_quad`
        * `->_quadpack._qagse`
        * `-> _quadpack._qagie`
       * `-> _quadpack._qagpe`
    * `->_quad_weight`
        * `->_quadpack._qawoe`
        * `->_quadpack._qawfe`
        * `->_quadpack._qawfe`
        * `->_quadpack._qawse`
        * `->_quadpack._qawce`



### quadrature

* Compute a definite integral using fixed-tolerance Gaussian quadrature.
* multiple order Gaussian quadrature


### fixed_quad
fixed_quad

* fixed interval
* fixed-order Gaussian quadrature


### romberg
[scipy\.integrate\.romberg — SciPy v1\.1\.0 Reference Guide](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.romberg.html#scipy.integrate.romberg)

* [Romberg's method \- Wikipedia](https://en.wikipedia.org/wiki/Romberg's_method)


### romb
[scipy\.integrate\.romb — SciPy v1\.1\.0 Reference Guide](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.romb.html#scipy.integrate.romb)

* romberg integration using samples of a function

### simp
[scipy\.integrate\.simps — SciPy v1\.1\.0 Reference Guide](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.simps.html#scipy.integrate.simps)

* [numpy\.trapz — NumPy v1\.14 Manual](https://docs.scipy.org/doc/numpy/reference/generated/numpy.trapz.html)
* Simpthon methods

### cumtrapz
* `def cumtrapz(y, x=None, dx=1.0, axis=-1, initial=None):`



* `def simps(y, x=None, dx=1, axis=-1, even='avg'):`

### qmc

Supported dimension `?`


Comparison with other methods

* quadrature


## Reference
* [Integration \(scipy\.integrate\) — SciPy v1\.1\.0 Reference Guide](https://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html)
