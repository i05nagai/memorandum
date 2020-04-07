---
title: aws-cdk
---

## aws-cdk


## Tips

#### vscode config
Create `jsconfig.json` in the root of the repository.

```
{
    "compilerOptions": {
        "moduleResolution": "node",
        "sourceMap": true,
        "noImplicitAny": false,
        "allowSyntheticDefaultImports": true,
        "baseUrl": ".",
        "paths": {
            "@aws-cdk/*": [
                "./packages/@aws-cdk/*/lib"
            ]
        }
    },
    "include": [
        "./packages/@aws-cdk/**/*"
    ]
}
```

## Reference
