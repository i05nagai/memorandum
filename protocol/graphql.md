---
title: GraphQL
---

## GraphQL


```
type Query {
  me: User
}

type User {
  id: ID
  name: String
}
```

```
{
  me {
    name
  }
}
```

```
{
  "me": {
    "name": "Luke Skywalker"
  }
}
```

## Metafields

- `__typename`


```
{
  search(text: "an") {
    __typename
    ... on Human {
      name
    }
    ... on Droid {
      name
    }
    ... on Starship {
      name
    }
  }
}
```

## Schemas

```
type Character {
  name: String!
  appearsIn: [Episode!]!
}
```

built-in types

- `String`
- `String!`
    - non nullable
- `[Episode!]!`
    - non nullable array of nonnullable Episode

Arguments

```
type Starship {
  id: ID!
  name: String!
  length(unit: LengthUnit = METER): Float
}
```

Arguments can be either required or optional. When an argument is optional, we can define a default value - if the unit argument is not passed, it will be set to METER by default.

Enum

```
enum Episode {
  NEWHOPE
  EMPIRE
  JEDI
}
```


## Reference
- https://graphql.org/learn/
