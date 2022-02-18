---
title: Amazon Simple Storage Service
---

## Amazon Simple Storage Service

## CLI

```
aws s3 ls <S3Uri> or NONE <option>
```

* `--recursive`
* `--page-size <value>`
* `--human-readable`
* `--summarize`
* `--request-payer <value>`

```
aws s3 cp
aws s3 mv
aws s3 rm
aws s3 sync
```

```
# Create buckets
aws s3 mb <S3Uri> <region>
```

* `<S3Uri>`
    * `s3://mybucket`
* `--region us-west-1`

```
# Delete buckets
aws s3 rb
```

#### Enable event notification
* [How Do I Enable and Configure Event Notifications for an S3 Bucket? \- Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/enable-event-notifications.html)

## Tips

### Perforamnce Optimization
* [Server Access Logging - Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerLogs.html)

AmazonのGet requestは300 reuqest/sec, PUT/LIST/DELETE は100 request/sec が一応制限としてある。
この制限を超える場合は、自動的にGETの800 request/sec, PUT/LIST/DELETEは300 request/secまではscaleするようになる。
これを超える場合は事前にsupportに連絡した方が良い。

### Manage access
* [Managing Access Permissions to Your Amazon S3 Resources - Amazon Simple Storage Service](http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html)


* canned ACL
    * [Access Control List (ACL) Overview - Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl)
    * あらかじめ定義された権限
    * private
        * Owenerのみfull access control
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

#### Permission
* [Specifying Resources in a Policy \- Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)
    - ARN format of S3 bucekts and S3 objects


#### Lifecycle
* [Object Lifecycle Management \- Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html)


Transions actions

Transition to another storage class.

Expiration actions

* NoncurrentVersionTransition
* NoncurrentVersionExpiration


## Metric
- [How Do I Configure Request Metrics for an S3 Bucket? \- Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/configure-metrics.html)
- [How Do I Configure a Request Metrics Filter? \- Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/configure-metrics-filter.html)


## Batch

#### Invoke lambda
- [Invoke AWS Lambda function \- Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-invoke-lambda.html)


Example request

```
{
    "invocationSchemaVersion": "1.0",
    "invocationId": "111111111111111111111111111111111111111111111111111",
    "job": {
        "id": "f3cc4f60-61f6-4a2b-8a21-d07600c373ce"
    },
    "tasks": [
        {
            "taskId": "22222222222222222222",
            "s3Key": "customerImage1.jpg",
            "s3VersionId": "1",
            "s3BucketArn": "arn:aws:s3:us-east-1:0123456788:awsexamplebucket1"
        }
    ]
}
```

Example response

```
{
  "invocationSchemaVersion": "1.0",
  "treatMissingKeysAs" : "PermanentFailure",
  "invocationId" : "111111111111111111111111111111111111111111111111111",
  "results": [
    {
      "taskId": "22222222222222222222",
      "resultCode": "Succeeded",
      "resultString": "[\"Mary Major", \"John Stiles\"]"
    }
  ]
}
```

#### Directory marker
- [Apache Hadoop Amazon Web Services support – Experimental: Controlling the S3A Directory Marker Behavior](https://hadoop.apache.org/docs/stable/hadoop-aws/tools/hadoop-aws/directory_markers.html)


## Reference
* [s3 — AWS CLI 1.11.102 Command Reference](http://docs.aws.amazon.com/cli/latest/reference/s3/)
* [sync — AWS CLI 1.11.102 Command Reference](http://docs.aws.amazon.com/cli/latest/reference/s3/sync.html)
* [S3 sync で s3からファイルを同期させる時の注意点 ｜ Developers.IO](http://dev.classmethod.jp/cloud/aws/s3-sync-exact-timestamps/)
