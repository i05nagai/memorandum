---
title: S3DistCp
---

## S3DistCP
Apache DistCp をS3用の最適化を加えたもの。
S3からHDFS、HDFSからS3の転送ができる。

```
s3-dist-cp --src s3://path/to/dir --dest hdfs:///path/to/dir
s3-dist-cp  --src hdfs:///path/to/dir --dest s3://path/to/dir
```


* `--srcPattern .*\.log`
    * 転送するファイルを限定する場合にpatternを指定する
* `--deleteOnSuccess`
    * 転送成功時に元ファイルを削除する

## Add step to EMR


```sh
s3_dist_cp_args="--src,s3://my-tables/incoming/hourly_table,--dest,/data/input/hourly_table,--targetSize,10,--groupBy,.*/hourly_table/.*(2017-).*/(\d\d)/.*\.(log)"
aws emr add-steps \
    --cluster-id j-ABC123456789Z \
    --steps "Name=LoadData,Jar=command-runner.jar,ActionOnFailure=CONTINUE,Type=CUSTOM_JAR,Args=s3-dist-cp,${s3_dist_cp_args}"
```

## Reference
* [S3DistCp (s3-dist-cp) - Amazon EMR](http://docs.aws.amazon.com/ja_jp/emr/latest/ReleaseGuide/UsingEMR_s3distcp.html)
* [Seven Tips for Using S3DistCp on Amazon EMR to Move Data Efficiently Between HDFS and Amazon S3 | AWS Big Data Blog](https://aws.amazon.com/blogs/big-data/seven-tips-for-using-s3distcp-on-amazon-emr-to-move-data-efficiently-between-hdfs-and-amazon-s3/)
