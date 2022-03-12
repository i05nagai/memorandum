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

## Typeo

- By default null and undefined are subtypes of all other types. That means you can assign null and undefined to something like number.


## JSX
[TypeScript: Documentation \- JSX](https://www.typescriptlang.org/docs/handbook/jsx.html)

## Reference

