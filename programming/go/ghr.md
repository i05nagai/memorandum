---
title: ghr
labels:
  - github
---

## ghr
Upload assets to github release.

## Install
For OSX,

```
$ brew tap tcnksm/ghr
$ brew install ghr
```

For Linux,

```
GHR_VERSION=v0.10.0
curl -L https://github.com/tcnksm/ghr/releases/download/${GHR_VERSION}/ghr_${GHR_VERSION}_linux_amd64.tar.gz | tar x
mv ghr_${GHR_VERSION}_linux_amd64/ghr /path/to/bin
rm -rf ghr_${GHR_VERSION}_linux_amd64/ghr
```

## CLI
```
$ ghr \
    -t TOKEN \        # Set Github API Token
    -u USERNAME \     # Set Github username
    -r REPO \         # Set repository name
    -c COMMIT \       # Set target commitish, branch or commit SHA
    -b BODY \         # Set text describing the contents of the release
    -p NUM \          # Set amount of parallelism (Default is number of CPU)
    -delete \         # Delete release and its git tag in advance if it exists
    -draft \          # Release as draft (Unpublish)
    -prerelease \     # Crate prerelease
    TAG PATH
```

## Usage
You need to export GITHUB token.

```
export GITHUB_TOKEN=""
```

Upload assets in `pkg/` with Git Tag `v0.1.0`

```
ghr v0.1 pkg/
```

```
ghr \
    -t ${GITHUB_TOKEN}
    -u USERNAME \
    -r REPO \
    -c COMMIT \
    -b BODY \
    v0.1
    path/to/assets/
```

## Tips

### Access tokns
You need to check at least following scopes

* [x] repo/public_repo


### Adding newline in body
?

## Reference
* [tcnksm/ghr: Upload multiple artifacts to GitHub Release in parallel](https://github.com/tcnksm/ghr)

