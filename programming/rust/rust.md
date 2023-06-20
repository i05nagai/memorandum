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
- integration tests
    - integration tests in rust tests only public function
    - integration tests is placed in a dedicated `tests/` dir at the same leve of `src/`
    - you can put tests dir
    - you cannot create integration tests if it's a binary crate
        - If our project is a binary crate that only contains a src/main.rs file and doesn’t have a src/lib.rs file, we can’t create integration tests in the tests directory and bring functions defined in the src/main.rs file into scope with a use statement.
- there is no overloading

```
#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        let result = 2 + 2;
        assert_eq!(result, 4);
    }
}
```


## string

```
let s1 = String::from("1");
let s2 = String::from("2");
let s3 = s1 + &s2;
```

## Reference

