---
title: aws-cdk
---

## aws-cdk


#### UniqueID


#### PhysicalID
- If `core.Resource` is inherited, `physicalName: core.PhysicalName.GENERATE_IF_NEEDED` can be used to generate the physical name on the fly.


## ConstructNode

```
# accessible before synthesize
node.scope
# accessible before synthesize
node.unique_id
# accessible before synthesize
node.id
# accessible before synthesize
node.path
# accessible before synthesize
node.metadata
```

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

## Setup

```
# either
brew cask install dotnet
# and install SDK 3.1 https://dotnet.microsoft.com/download/dotnet-core/3.1

# or directly install sdk
brew cask install dotnet-sdk

# pip
pip install "pip==19.3.1"

yarn build
```


## Reference
