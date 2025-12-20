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

# Query

response

```
{
    "data": {
    },
    "errors": {
    }
}
```

## Pagination
https://www.apollographql.com/blog/understanding-pagination-rest-graphql-and-relay
https://medium.com/@chris.czurylo/implementing-pagination-in-graphql-and-go-using-gqlgen-2ea3786a71dc
https://relay.dev/graphql/connections.htm


```graphql
query PaginatePRs(
  $owner: String!
  $name: String!
  $pageSize: Int = 100
  $cursor: String
) {
  repository(owner: $owner, name: $name) {
    pullRequests(
      first: $pageSize
      after: $cursor
      states: OPEN
      orderBy: { field: UPDATED_AT, direction: DESC }
    ) {
      nodes {
        number
        title
        createdAt
        updatedAt
        url
        author { login }
        merged
      }
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
  rateLimit {
    cost
    remaining
    resetAt
  }
}

```


## Formatter
https://github.com/gqlgo/awesome-gqlgen

## Reference
- https://graphql.org/learn/
