---
title: text/template
---

## text/template
Template like liquid template.

* Actions
    * surrounded by `{{ }}`
* pipeline
    * Chanied sequence of commands
*  command
    * simple value (argument)
    * function/method call
* arguments
    * An argument is a simple value,
* variables


```go
type Inventory struct {
	Material string
	Count    uint
}
sweaters := Inventory{"wool", 17}
tmpl, err := template.New("test").Parse("{{.Count}} items are made of {{.Material}}")
if err != nil { panic(err) }
err = tmpl.Execute(os.Stdout, sweaters)
if err != nil { panic(err) }
```

## Actions
* `{{ ACTION }}`
    * `{{` acitons' left delimiter by default
* `{{/* a comment */}}`

## Arguments
* An argument is a simple value, denoted by one of the following.



## Pipelines
Combination of followings

* Argument
* .Method
* functionName [Argument...]
    * e.g. `{{printf "%q" "output"}}`
        * `printf` is functionName
        * `"%q" "outout"` are arguments

## Variables
* `$variable := pipeline`

## Functions
* [template - The Go Programming Language](https://golang.org/pkg/text/template/#hdr-Functions)

Built in functions

* `printf`
* `print`
* `println`

## Examples

```
{{"\"output\""}}
{{`"output"`}}
```

## Reference
* [template - The Go Programming Language](https://golang.org/pkg/text/template/)
