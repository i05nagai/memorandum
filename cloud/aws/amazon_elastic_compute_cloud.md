---
title: Amazon Elastic Compute Cloud
---

## Amazon Elastic Compute Cloud

It's possible. I don't know if it's more maintenacibility to having multiple global variables


## Permissions
- https://docs.aws.amazon.com/AWSEC2/latest/APIReference/ec2-api-permissions.html

- https://docs.aws.amazon.com/AWSEC2/latest/APIReference/ec2-api-permissions.html#tags
    - CreateTags
    - DeleteTags


## Optimize Instance 
* [How Netflix Tunes EC2 Instances for Performance](https://www.slideshare.net/brendangregg/how-netflix-tunes-ec2-instances-for-performance)

## Adding repositories
* https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/add-repositories.html

## Monitoring

#### Metrics
* [List the Available CloudWatch Metrics for Your Instances \- Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html)


#### Calculate fingerprints
- [ssh \- Why does my OpenSSH key fingerprint not match the AWS EC2 console keypair fingerprint? \- Server Fault](https://serverfault.com/questions/603982/why-does-my-openssh-key-fingerprint-not-match-the-aws-ec2-console-keypair-finger)


Keys generated locally

```
openssl pkey -in id_rsa -pubout -outform DER | openssl md5 -c
```

Keys generated on AWS

```
openssl pkcs8 -in aws_private.pem -nocrypt -topk8 -outform DER | openssl sha1 -c
```

## Reference
* https://www.slideshare.net/brendangregg/how-netflix-tunes-ec2-instances-for-performance
