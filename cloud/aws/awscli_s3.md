---
title: awscli s3
---

## awscli s3
aws s3

## CLI
基本的には、linuxのCLIのcp, ls, mvなどが使える。
* ls
* cp
* mv
* mb
* rb

unix styleのwildcardsは使えないが、以下が使える。

* `*`
    * すべてにまっち
* `?`
    * 任意の一文字にマッチ
* `[sequence]`
    * sequenceで指定された任意の一文字にマッチ
* `[!sequence]`
    * sequenceで指定されてない任意の一文字にマッチ

exclude, includeは指定したpathからの相対パスで指定する。
例えば、source pathが`path/to/source`の場合は、`path/to/source/hoge`以下のファイルを全て除外するなら`--exclude 'hoge/*'`という感じで指定する。

includeとexcludeは順序依存である。
以下は、拡張子が`.txt`のファイルのみ扱う。

```
--exclude "*" --include "*.txt"
```

以下は、対象となるファイルはない。

```
--include "*.txt" --exclude "*"
```

includeとexcludeは複数指定することもできる。
特定の名前のdirectoryやfileを除去する場合は以下のようにする必要がある。
この場合は`hoge_directory-name/`や`hoge-file-name.md`なども除外される。

```
--include "*" --exclude "*directory-name/*" --exclude "*file-name.md"
```

### aws s3 ls

```
aws s3 ls <s3-url> [option]
```

* `--summarize`
* `--recursive`
* `--human-readable`


### aws s3 sync
* EMRなど, S3からしかファイルを転送できないときに、git repositoryと同期するなどの用途で使う

```
aws s3 sync <from_path> <to_path>
```

完全に同期をとる。
`--delete`オプションをつけると、つけない場合は、更新があったファイルが上書き更新されるだけ。

* `--delete`
    * sourceで削除されたり、なくなったものは削除される
    * つけない場合は、更新があったファイルが上書き更新されるだけ
* `--exact-timestamps`
    * timestampの違いで同期する場合はこのオプションをつける
    * defaultでは、ファイルサイズが同じ場合は、同期されない
* `--dryrun`

## Usage
Get list of directory in path

```
aws s3 ls s3://path/to/dir/ | awk '{print $2}'
```

Change date format in paths

```sh
mv_date_noslash_to_slash() {
  local PATH_FROM=$1
  local PATH_TO_BASE=$2
  files=`aws s3 ls ${PATH_FROM} | awk '{print $2}'`
  for filename in ${files}; do
    # python one liner
    # `python -c "from __future__ import print_function; import datetime as d; print(d.datetime.strptime('${filename}', '%Y%m%d/').strftime('%Y/%m/%d/'), end='')" | tr -d '\n'`
    # for BSD date conversion
    filename_new=`date -j -f "%Y%m%d/" ${filename} +"%Y/%m/%d/"`
    aws s3 cp --recursive ${PATH_FROM}${filename} ${PATH_TO}${filename_new}
  done
}
```

## Reference
