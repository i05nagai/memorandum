---
title: github CLI github enterprise importer
---

## github CLI github enterprise importer

```
```

## CLI

```
  gh-gei migrate-repo [options]
```

* `--github-source-org <github-source-org>`
    * (REQUIRED)
    * Uses GH_SOURCE_PAT env variable or --github-source-pat option. Will fall back to GH_PAT or --github-target-pat if not set.
* `--source-repo <source-repo>`
    * (REQUIRED)
* `--github-target-org <github-target-org>`
    * (REQUIRED)
    * Uses GH_PAT env variable or --github-target-pat option.
* `--target-repo <target-repo>`
    * Defaults to the name of source-repo
* `--target-api-url <target-api-url>`
    * The URL of the target API, if not migrating to github.com. Defaults to https://api.github.com
* `--ghes-api-url <ghes-api-url>`
    * Required if migrating from GHES. The API endpoint for your GHES instance. For example: http(s)://ghes.contoso.com/api/v3
* `--azure-storage-connection-string <azure-storage-connection-string>`
    * Required if migrating from GHES (Not required if migrating from GitHub Enterprise Server 3.8.0 or later).
    * The connection string for the Azure storage account, used to upload data archives pre-migration.
    * For example: `"DefaultEndpointsProtocol=https;AccountName=myaccount;AccountKey=mykey;EndpointSuffix=core.windows.net"`
* `--aws-bucket-name <aws-bucket-name>`
    * If using AWS, the name of the S3 bucket to upload the data archives to. Not required if migrating from GitHub Enterprise Server 3.8.0 or later.
* `--aws-access-key <aws-access-key>`
    * If uploading to S3, the AWS access key. If not provided, it will be read from AWS_ACCESS_KEY_ID environment variable. Not required if migrating from GitHub Enterprise Server 3.8.0 or later.
* `--aws-secret-key <aws-secret-key>`
    * If uploading to S3, the AWS secret key. If not provided, it will be read from AWS_SECRET_ACCESS_KEY environment variable. Not required if migrating from GitHub Enterprise Server 3.8.0 or later.
* `--aws-session-token <aws-session-token>`
    * If using AWS, the AWS session token. If not provided, it will be read from AWS_SESSION_TOKEN environment variable.
* `--aws-region <aws-region>`
    * If using AWS, the AWS region. If not provided, it will be read from AWS_REGION environment variable. Required if using AWS.
* `--no-ssl-verify`
    * Only effective if migrating from GHES. Disables SSL verification when communicating with your GHES instance. All other migration steps will continue to verify SSL. If your GHES instance has a self-signed SSL certificate then setting this flag will allow data to be extracted.
* `--skip-releases`
    * Skip releases when migrating.
* `--lock-source-repo`
    * Lock source repo when migrating.
* `--queue-only` 
    * Only queues the migration, does not wait for it to finish. Use the wait-for-migration command to subsequently wait for it to finish and view the status.
* `--target-repo-visibility <internal|private|public>`
    * The visibility of the target repo. Defaults to private. Valid values are public, private, or internal.
* `--github-source-pat <github-source-pat>`
* `--github-target-pat <github-target-pat>`
* `--keep-archive`
    * Keeps the archive on this machine after uploading to the blob storage account. Only applicable for migrations from GitHub Enterprise Server versions before 3.8.0 or when used with --use-github-storage.


## Reference
