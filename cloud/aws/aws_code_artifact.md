---
title: AWS Code Artifact
---

## AWS Code Artifact

- Domain
    - Each repository is a member of a single domain and can't be moved to a different domain.
- Repository
     * Repositories are polyglot, which means that a single repository can contain packages of any supported type.
- Packages
    - A package is a bundle of software and the metadata that is required to resolve dependencies and install the software. 
    - namespace + package_name
        - namespace: @types/node,
        - package_name: node

## Packages

- You can't republish a package asset that already exists with different content.
- To republish the same asset with new content, delete the package version using the delete-package-versions
- Package versions published to a CodeArtifact repository are often available for download in less than one second. 

```
arn:aws:codeartifact:region-id:111122223333:package/<my_domain>/<my_repo>/<package-format>/<package-namespace>/<package-name>
```

version satatus

- Published
- Unfinished
- Unlisted
    - The package version's assets are available for download from the repository, but the package version is not included in the list of versions returned to package managers.
    - This means that npm's dependency resolution logic will not select the package version because the version does not appear in the list of available versions.
- Archived
- Disposed

Normalization

- CodeArtifact normalizes package names, package versions, and asset names before storing them, which means the names or versions in CodeArtifact may be different than the name or version provided when the package was published.
    - https://docs.aws.amazon.com/codeartifact/latest/ug/python-name-normalization.html
 

Formats and namespace

- generic
    * with namespace
- npm
    - `@npm/`
    - multiple registyies are not supported. But we can specify a specific repository for a scope
- nuget
    * no namespace?
- pypi
    * no namespace?
    - `/python//requests`
- maven
    * with namespace
    * multiple registries are allowed
    - `/maven/org.apache.logging.log4j/log4j-core`
- swift
    * with namespace
- ruby
    * gemfile can specify sources for a set of gems
    * https://stackoverflow.com/questions/16072412/ruby-bundler-multiple-sources-in-gemfile
- cargo


Namespaces

- 
maven/com.amazon~

## Package group
https://aws.amazon.com/blogs/aws/improve-the-security-of-your-software-supply-chain-with-amazon-codeartifact-package-group-configuration/

- Package groups can be used to apply configuration to multiple packages that match a defined pattern using package format, package namespace, and package name.


## Domain
- domain owner is an aws account


## Reposiotry
- repository administraor is an aws account

## Policy

- condition 1
    - domain owner or repository admin
    - identity policy allow
- condition 2
    - resource policy allows
    - identity policy allows


## Quotas
https://docs.aws.amazon.com/codeartifact/latest/ug/service-limits.html

non adjustable quotas

- Assets per package version
    - Each supported Region: 150
- Direct upstreams per repository
    - Each supported Region: 10
- Requests per second using a single authentication token
    - Each supported Region: 1,200
- Requests without authentication token per IP address
    - Each supported Region: 600
- Upstream repositories searched
    - Each supported Region: 25


## Reference


