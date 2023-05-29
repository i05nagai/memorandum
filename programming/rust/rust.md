---
title: rust
---

## rust


`op1 + op2 -> op1.add(op2)`

- refrence
    - only one mutable reference to the object can exists in the same scope

- `const MAX_V: i32 = 10;`
    - type annotation is required
- `(i32, u32, i32)`
    - tuple type
- `function(&var)`
    - pass reference
- `function(&mut var)`
    - pass mutable reference
- `fn function(var: &type)) -> ret_type`
- `fn function(var: &mut type)) -> ret_type`
- `&self`
- glob import
    - `use module_name::*;`
- question mark operator
    - https://doc.rust-lang.org/reference/expressions/operator-expr.html#the-question-mark-operator - `f.read_to_string(&mut s)?;`
    - used with Result type
    - If Result is an Ok, it returns the content. If Err, it returns Err to to the caller function.
    - The operator actually returns the function in the middle of the function execution.
    - `f.open("fle")?.read_to_string(&mut s)?;`
- traits needs to be defined in the same scope by importing or defining
- there is no overloading


## string

```
let s1 = String::from("1");
let s2 = String::from("2");
let s3 = s1 + &s2;
```

## Reference

