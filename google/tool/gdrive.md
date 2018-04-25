---
title: gdrive
---

## gdrive
Google drive CLI clinet.
maitenanceされてない。

## Install

```
brew install gdrive
```

適当にcommandを実行すると認証用のURLが表示される。
browserでaccessして、google accountでloginすると、認証用のcodeが表示されるのでcopyしてはる。


## Usage

### list
fileの表示.
web UIの画面のように階層てきには表示されない。

```
gdrive list
```

* `--absolute`
    * pathを表示
* `--query <query>`
    * default `trashed = false and 'me' in owners`
    * https://developers.google.com/drive/search-parameters
    * folderだけ
        * `mimeType = 'application/vnd.google-apps.folder'`
    * folder以外
        * `mimeType != 'application/vnd.google-apps.folder'`
    * file名(not path)に`docs`を含む。
        * `name contains 'docs'`
    * folder`<ID>`以下のfile/folder
        * `gdrive list --query "'<ID>' in parents"`

docsという名前のfolder

```
gdrive list --query "name contains 'docs' and mimeType = 'application/vnd.google-apps.folder'"
```

### info
IDを指定する。

```
gdrive info <ID>
```

### download

```
gdrive [global] download [options] <fileId>
```

* `--path <path> `
    * DL先のpath
    * 
* `-r, --recursive`
    * 再帰的にDL

folderをDL

```
gdrive download --recursive --path /path/to/dl <ID>
```

### download query
queryにMatchするものをDL


### upload

```
gdrive upload --recursive <path>
```

* `-p, --parent <ID>`
    * 親directory
* `-r, --recursive `

### sync download


### sync upload
`.gdriveignore`に`.gitignore`と同じ構文でsyncしないfileを指定できる。
sync先の`<fileId>`は空である必要がある。

```
gdrive [global] sync upload [options] <path> <fileId>
```

`<path>`のdirを`<ID>`とsync

* `--keep-remote`
    * Keep remote file when a conflict is encountered
* `--keep-local`
    * Keep local file when a conflict is encountered
* `--keep-largest`
    * Keep largest file when a conflict is encountered
* `--dry-run`


```
# <id> はhoge dirのid
gdrive sync uploda --keep-remote /local/hoge <id>
```

directory以下の特定のfileをsyncしたい場合は`.gdriveignore`を以下のように生成する。

```
.
├── a
│   └── aa
│       └── file.sh
├── b
│   └── ba
│       └── file.sh
└── c
    └── file.sh
```

```
echo '*' > .gdriveignore
find . -name sync_file_name | sed 's/.\//!\//' >> .gdriveignore
```

```.giginore
*

# a
!a
a/*

# aa
!a/aa
a/aa/*

# file.sh
!a/aa/file.sh

# b
!b
b/*

# ba
!b/ba
b/ba/*

# file.sh
!b/ba/file.sh

# c
!c
c/*

# file.sh
!c/file.sh
```


## Reference
* [prasmussen/gdrive: Google Drive CLI Client](https://github.com/prasmussen/gdrive)
