---
title: Cython Syntax
---

## Cython Syntax

## Type
* [Language Basics — Cython 0.28.2 documentation](http://docs.cython.org/en/latest/src/userguide/language_basics.html)

* `DEF FavouriteFood = u"spam"`
    * compile time constant
    * RHS can be python expression
        * list is not available
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
* [Special Methods of Extension Types — Cython 0.28.2 documentation](http://docs.cython.org/en/latest/src/userguide/special_methods.html)

* normal Python classes are supported
* extension types aka `cdef classes`
    * they are restricted compared to Python class
    * but more memory efficient and faster
* `cdef classes` stores their field as C struct
    * C level access

```
cdef class SinOfSquareFunction(Function):
    cpdef double evaluate(self, double x) except *:
        return sin(x**2)
```

Attributes of cdef classes

* all attributes must be pre0declared at compile-time
* attributes are by default only accecibile from cython
    * `cdef public double attr1`
* property can be declared to expose dynamic attributes to Python-space

Initalisation methods

* `__cinit__()`
    * c level initilization
    * for allocating c data
    * you cannot explicitly call the inherited `__cinit__()` method.
    * don't modify python objects in this method
* `__init__()`

FIniliztino method

* `__dealloc__()`
    * The counterpart to the `__cinit__()` method
    * you explicitly allocated (e.g. via malloc) in your `__cinit__()` method should be freed in your `__dealloc__()` method.

## Memory allocation
* [Memory Allocation — Cython 0.28.2 documentation](http://docs.cython.org/en/latest/src/tutorial/memory_allocation.html)


`malloc` is imported to `libc.stdlib`.

```
from libc.stdlib cimport malloc, free
```

C-API functions

* C-API functions for allocating memory on the Python heap are generally preferred over the low-level C functions above

```
from cpython.mem cimport PyMem_Malloc, PyMem_Realloc, PyMem_Free
```


```python
cdef class SomeMemory:

    cdef double* data

    def __cinit__(self, size_t number):
        # allocate some memory (uninitialised, may contain arbitrary data)
        self.data = <double*> PyMem_Malloc(number * sizeof(double))
        if not self.data:
            raise MemoryError()

    def resize(self, size_t new_number):
        # Allocates new_number * sizeof(double) bytes,
        # preserving the current content and making a best-effort to
        # re-use the original data location.
        mem = <double*> PyMem_Realloc(self.data, new_number * sizeof(double))
        if not mem:
            raise MemoryError()
        # Only overwrite the pointer if the memory was really reallocated.
        # On error (mem is NULL), the originally memory has not been freed.
        self.data = mem

    def __dealloc__(self):
        PyMem_Free(self.data)     # no-op if self.data is NULL
```

## Reference

