---
title: Typescript
---

## Typescript


## Install

```
npm -g typescript
```

## CLI

```
tsc helloworld.ts
```

## configuration
- [TypeScript: Handbook \- tsconfig\.json](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html)

```json
{
"compilerOptions": {
  "module": "commonjs",
  "noImplicitAny": true,
  "removeComments": true,
  "preserveConstEnums": true,
  "sourceMap": true
},
"files": [
  "core.ts",
  "sys.ts",
  "types.ts",
  "scanner.ts",
  "parser.ts",
  "utilities.ts",
  "binder.ts",
  "checker.ts",
  "emitter.ts",
  "program.ts",
  "commandLineParser.ts",
  "tsc.ts",
  "diagnosticInformationMap.generated.ts"
]
}
```

## Type

- By default null and undefined are subtypes of all other types. That means you can assign null and undefined to something like number.

#### Unkown type
https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-0.html#new-unknown-top-type
unknown is the type-safe counterpart of any.
Anything is assignable to `unknown`, but `unknown` isn’t assignable to anything but itself and `any` without a type assertion or a control flow based narrowing.
Likewise, no operations are permitted on an unknown without first asserting or narrowing to a more specific type.

## Type Definition
Union

```
type A = number | null | undefined;
```

```
type Fish = { swim: () => void };
type Bird = { fly: () => void };
type Human = { swim?: () => void; fly?: () => void };
```

```
typeof padding === "number"
```

type predicate

```
function isFish(pet: Fish | Bird): pet is Fish {
  return (pet as Fish).swim !== undefined;
}
```

Array

```
type A = string[];
```

string type

```
interface Shape {
  kind: "circle" | "square";
  radius?: number;
  sideLength?: number;
}
```

optional

```
interface A {
  xPos?: number;
}
let xPos = opts.xPos === undefined ? 0 : opts.xPos;
```

index

```
interface Animal {
  name: string;
}
 
interface Dog extends Animal {
  breed: string;
}
 
// Error: indexing with a numeric string might get you a completely separate type of Animal!
interface NotOkay {
  [x: number]: Animal;
 // 'number' index type 'Animal' is not assignable to 'string' index type 'Dog'.
  [x: string]: Dog;
}
```

Object type

- use interface
- use anonymous type

```
function greet(person: { name: string; age: number }) {
  return "Hello " + person.name;
}
```


## control satatements
- for of
    - iterate over Iterable
- for in
    - iterate properties of objects

## JSX
[TypeScript: Documentation \- JSX](https://www.typescriptlang.org/docs/handbook/jsx.html)

## generics
- https://stackoverflow.com/questions/54751710/checking-type-of-a-generic-param-in-typescript


If you feel so... We would have had higher chance to get fired and spend more time to find a job with less condition. I believe in better situtaion for next 20 years.



## Reference

