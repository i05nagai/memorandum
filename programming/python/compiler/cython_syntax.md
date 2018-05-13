---
title: Cython Syntax
---

## Cython Syntax

## Type
* [Language Basics — Cython 0.28.2 documentation](http://docs.cython.org/en/latest/src/userguide/language_basics.html)

* `DEF FavouriteFood = u"spam"`
    * compile time constant
* `cdef int`
* `cdef double`
* `cdef float`

```python
cdef struct Grail:
    int age
    float volume

cdef union Food:
    char *spam
    float *eggs

cdef enum CheeseType:
    cheddar, edam,
    camembert

cdef enum CheeseState:
    hard = 1
    soft = 2
    runny = 3
```

Grouping

```
cdef:
    struct Spam:
        int tons
```

Use anonymous enum as constatn

```
cdef enum:
    tons_of_spam = 3
```

## Control
Comple time conditional statement

```
IF UNAME_SYSNAME == "Windows":
    include "icky_definitions.pxi"
ELIF UNAME_SYSNAME == "Darwin":
    include "nice_definitions.pxi"
ELIF UNAME_SYSNAME == "Linux":
    include "penguin_definitions.pxi"
ELSE:
    include "other_definitions.pxi"
```

## Function
* python funciton
    * They take Python objects as parameters and return Python objects.
* C functions
    * C functions are defined using the new cdef statement.
    * cannot call outside the module

```python
def integrate(Function f, double a, double b, int N):
    cdef int i
    return i

cdef int integrate(Function g, double a, python_obj):
    cdef int i
    return i

cdef object integrate(Function g, double a, python_obj):
    cdef int i
    return python_obj
```

* If no type is specified for a parameter or return value, it is assumed to be a Python object.
* `cpdef`
    * use the faster C calling conventions when being called from other Cython code
    * there is a tiny overhead in calling a cpdef method from Cython compared to calling a cdef method
* `cdef`

Exception

* In function without `except`, if an exception is detected in such a function, a warning message is printed and the exception is ignored
* If you want to probagate exceptions but not handle, declare with `cdef int spam() except -1:`
    * whenever an exception occurs inside spam, it will immediately return with the value -1
    * you cannot return `-1`
* `cdef int spam() except? -1:`
    * `?` indicates that the value `-1` only indicates a possible value
* `cdef int spam() except *:`

Automatic type

| C types                                           | From Python types | To Python types |
|---------------------------------------------------|-------------------|-----------------|
| [unsigned] char, [unsigned] short, int, long      | int, long         | int             |
| unsigned int, unsigned long, [unsigned] long long | int, long         | long            |
| float, double, long double                        | int, long, float  | float           |
| char*                                             | str/bytes         | str/bytes [2]   |
| struct, union                                     |                   | dict [3]        |


## Class

```
cdef class SinOfSquareFunction(Function):
    cpdef double evaluate(self, double x) except *:
        return sin(x**2)
```

## Reference

