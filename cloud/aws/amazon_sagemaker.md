---
title: Amazon SageMaker
---

## Amazon SageMaker



## Errors

#### error during Notebook creation

```
+ aws s3 cp s3://aws-glue-jes-prod-us-east-1-assets/sagemaker/assets/ . --recursive
13:20:34 fatal error: An error occurred (AccessDenied) when calling the ListObjectsV2 operation: Access Denied
```

You need `ListBucket` permmission.

```
To use this operation in an AWS Identity and Access Management (IAM) policy, you must have permissions to perform the s3:ListBucket action. The bucket owner has this permission by default and can grant this permission to others. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to Your Amazon S3 Resources.
```

## Reference
* [Machine Learning Models & Algorithms | Amazon SageMaker on AWS](https://aws.amazon.com/sagemaker/)
