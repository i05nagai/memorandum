---
title: CPP Operator
---

## CPP Operator


## Bitwise shift operators
`v = lhs << rhs`

* `lhs` unsigned
    * `v = a * 2^{rhs}`
* `lhs > 0` signed and positive
    * until C++14
        * `v = lhs * 2^{rhs}`
    * since C++14
        * `v = lhs * 2^{rhs}`
* `lhs < 0` signed and negative
    * undefined
* `rhs < 0`
    * undefined

`v = lhs >> rhs`

* `lhs` unsigned
    * `v = (int)(a / 2^{rhs})`
* `lhs >= 0` signed
    * `v = (int)(a / 2^{rhs})`
* `lhs < 0` signed and negative
    * implementation defined
        * in most, rigth shift in base2
        * e.g. -5 >> 2 = (-101)_{2} >> 2 = (-1)_{2}
* `rhs < 0`
    * undefined


## Reference

