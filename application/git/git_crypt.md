---
title: git-crypt
---

## git-crypt


#### setup repository

```
git-crypt init
```

Add `.gitattributes` then specify the paths you want encrypt.

```
/path/to/file filter=git-crypt diff=git-crypt
*.key filter=git-crypt diff=git-crypt
dir/** filter=git-crypt diff=git-crypt
```

```
git add .gitattributes
git commit
```

#### Adding user

You can add users

```
git-crypt add-gpg-user USER_ID
```

#### Export key

You can export symetric key whic can lock/unlock repo without gpg.

```
git-crypt export-key /path/to/key
git-crypt unlock /path/to/key
```

## Reference
- [AGWA/git\-crypt: Transparent file encryption in git](https://github.com/AGWA/git-crypt)
