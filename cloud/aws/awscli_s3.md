---
title: awscli s3
---

## awscli s3
aws s3

## CLI

```
aws s3 ls <s3-url> [option]
```

* `--summarize`
* `--recursive`
* `--human-readable`

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
