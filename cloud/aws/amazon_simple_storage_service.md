---
title: Amazon Simple Storage Service
---

## Amazon Simple Storage Service

## Commands
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


* sync
    * EMRなど, S3からしかファイルを転送できないときに、git repositoryと同期するなどの用途で使う

完全に同期をとる。
`--delete`オプションをつけると、つけない場合は、更新があったファイルが上書き更新されるだけ。

* `--delete`
    * sourceで削除されたり、なくなったものは削除される
    * つけない場合は、更新があったファイルが上書き更新されるだけ
* `--exact-timestamps`
    * timestampの違いで同期する場合はこのオプションをつける
    * defaultでは、ファイルサイズが同じ場合は、同期されない
* `--dryrun`

```
aws s3 sync <from_path> <to_path>
```

## Tips

### Perforamnce Optimization
* [Server Access Logging - Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerLogs.html)

AmazonのGet requestは300 reuqest/sec, PUT/LIST/DELETE は100 request/sec が一応制限としてある。
この制限を超える場合は、自動的にGETの800 request/sec, PUT/LIST/DELETEは300 request/secまではscaleするようになる。
これを超える場合は事前にsupportに連絡した方が良い。

### Manage access
* [Managing Access Permissions to Your Amazon S3 Resources - Amazon Simple Storage Service](http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html)


* ACL
    * XML形式でS3/S#のObjectに付与する
    * resource based
    * An object ACL is the only way to manage access to objects not owned by the bucket owner
    * S3のBucketにACLを設定するのは、Log Delivery group to write access log objects to your bucket 
* Buckert Policy
    * JSON形式でS3に付与する
    * resource based
* User policies
    * IAMでuser/group/roleに対して権限を付与する
    * user based

### Routing
* [(Optional) Configuring a Webpage Redirect - Amazon Simple Storage Service](http://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html)

* `x-amz-website-redirect-location` propertyでredirectできる
* redirectは301


**Example1**

以下のobjectがある。

* index.html
* docs/article1.html
* docs/article2.html

`docs`へのaccessを`documents`にredicrectしたい。

```xml
<RoutingRules>
    <RoutingRule>
        <Condition>
          <KeyPrefixEquals>docs/</KeyPrefixEquals>
        </Condition>
        <Redirect>
          <ReplaceKeyPrefixWith>documents/</ReplaceKeyPrefixWith>
        </Redirect>
    </RoutingRule>
</RoutingRules>
```

**Example 2: Redirect requests for a deleted folder to a page**

`images` foldeを削除。
`images`へのaccessを全て`folderdeleted.html`へredirect

```xml
<RoutingRules>
<RoutingRule>
<Condition>
   <KeyPrefixEquals>images/</KeyPrefixEquals>
</Condition>
<Redirect>
  <ReplaceKeyWith>folderdeleted.html</ReplaceKeyWith>
</Redirect>
</RoutingRule>
</RoutingRules>
```

**Example 3: Redirect for an HTTP error**

404の場合にredirectする。

```xml
<RoutingRules>
  <RoutingRule>
    <Condition>
      <HttpErrorCodeReturnedEquals>404</HttpErrorCodeReturnedEquals>
    </Condition>
    <Redirect>
      <HostName>ec2-11-22-333-44.compute-1.amazonaws.com</HostName>
      <ReplaceKeyPrefixWith>report-404/</ReplaceKeyPrefixWith>
    </Redirect>
  </RoutingRule>
</RoutingRules>
```


## Reference
* [s3 — AWS CLI 1.11.102 Command Reference](http://docs.aws.amazon.com/cli/latest/reference/s3/)
* [sync — AWS CLI 1.11.102 Command Reference](http://docs.aws.amazon.com/cli/latest/reference/s3/sync.html)
* [S3 sync で s3からファイルを同期させる時の注意点 ｜ Developers.IO](http://dev.classmethod.jp/cloud/aws/s3-sync-exact-timestamps/)
