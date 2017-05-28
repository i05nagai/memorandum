---
title: embulk
---

## embulk

## Install

```sh
curl --create-dirs -o ~/.embulk/bin/embulk -L "https://dl.embulk.org/embulk-latest.jar"
chmod +x ~/.embulk/bin/embulk
echo 'export PATH="$HOME/.embulk/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

For OSX

```sh
brew install embulk
```


## Plugins

### embulk-input-gcs
* [GitHub - embulk/embulk-input-gcs: Embulk plugin that loads records from Google Cloud Storage](https://github.com/embulk/embulk-input-gcs)

```
embulk gem install embulk-input-gcs
```

* 

### embulk-output-bigquery
* [GitHub - embulk/embulk-output-bigquery: Embulk output plugin to load/insert data into Google BigQuery](https://github.com/embulk/embulk-output-bigquery)

```
embulk gem install embulk-output-bigquery
```

## Reference
