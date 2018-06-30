---
title: rclone
---

## rclone
rsync for cloud storage.

## Install

```
cd /tmp
curl -L -O https://downloads.rclone.org/v1.42/rclone-v1.42-linux-amd64.zip
unzip rclone-v1.42-linux-amd64.zip
mv rclone-v1.42-linux-amd64/rclone ~/.bin
```

## Gdrive
* [Google drive](https://rclone.org/drive/)

Follow the instruction above.

```
rclone config
```

List gdrive dir

```
rclone lsd gdrive:
```

List gdrive files

```
rclone ls gdrive:
```

## CLI
Interactive configuration.

```
rclone config
```

List directory

```
rclone lsd <remote-name>:
```

List files

```
rclone ls <remote-name>:
```

List files

```
rclone sync source:path dest:path [flags]
```

* `--dry-run`


## Usage

Sync local path

```
rclone sync path/to/local remote-name:/path/to/remote --dry-run
```

## Configuration
* `~/.config/rclone/rclone.conf`

## Reference
* [rclone \- rsync for cloud storage](https://rclone.org/)
* [ncw/rclone: "rsync for cloud storage" \- Google Drive, Amazon Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Cloudfiles, Google Cloud Storage, Yandex Files](https://github.com/ncw/rclone)
