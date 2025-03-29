---
title: HCP Terraform
---

## HCP Terraform


## API Tokens
https://developer.hashicorp.com/terraform/cloud-docs/users-teams-organizations/api-tokens


#### Team token
Each team can have one valid API token at a time. When a token is regenerated, the previous token immediately becomes invalid.



## Github Actions
- https://github.com/hashicorp/tfc-workflows-github/tree/main


- upload-configuration
    - Creates and uploads configuration files for a given HCP Terraform workspace.
- create-run
    - Performs a new plan run in HCP Terraform, using a configuration version and the workspace’s current variables.
- apply-run
    - Applies a run that is paused waiting for confirmation after a plan.
- discard-run
    - Skips any remaining work on runs that are paused waiting for confirmation or priority.
- cancel-run
    - Interrupts a run that is currently planning or applying.
- show-run
    - Returns run details for the corresponding Run ID.
- plan-output
    - Returns the plan details for the provided Plan ID.

## Reference
