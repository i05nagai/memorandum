---
title: Amazon Machine Image
---

## Amazon Machine Image

* Launch Permission
    * AMIのuserが権限を決める
    * Public
        * 全てのAWS accountに権限
    * explicit
        * 指定したAWS accountのみに権限
    * implicit


AMIのstorageによる分類。
以下の2種類存在する。

* Backed by Amazon EBS
    * AMIからinstanceを立ち上げるときにroot deviceがEBS
    * EBS snapshotからroot deviceが作られる
    * instanceがterminateしたときにroot volumeは削除される
    * 
* Backed by Instance store
    * AMIからinstanceを立ち上げるときにroot deviceがS3に保存されたtemplate


| Characteristic     | Amazon EBS-Backed          | Amazon Instance Store-Backed |
|--------------------|----------------------------|------------------------------|
| Boot time          | Usually less than 1 minute | Usually less than 5 minutes  |
| Size limit         | 16 TiB                     | 10 GiB                       |
| Root device volume | Amazon EBS volume          | Instance store volume        |

## Price
以下で異なる

* AMI backed
    * AMI storage
    * instance usage
* Amazon EBS Backed
    * volume storage
    * AMI usage
    * instance usage

## Create AMI
From consloe

From command line

* aws ec2 create-image
    * 

```
aws ec2 create-iamge --instance-id i-1234567890abcdef0 --name "My server" --description "An AMI for my server"
```



## Reference
* [Amazon Machine Images (AMI) - Amazon Elastic Compute Cloud](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)
