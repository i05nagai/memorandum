---
title: Terraform Cloud
---

## Terraform Cloud


- speculative plans
    - https://developer.hashicorp.com/terraform/cloud-docs/run/remote-operations#speculative-plans
    - Speculative plans are plan-only runs
    - Speculative plans can begin without waiting for other runs to finish because they don't affect real infrastructure.

## run modes

### Execution mode
There are two exectuon modes.

remote

- in remote mode, the terraform command will run on terraform cloud instead of your local computer
- You can pass secrets via terraform variable by CLI argument or TF_VAR. However, env vars supported by provider will not read the env

 local

- in this case, terraform cloud is used as a remote state store
- in local mode, a lot of features are not be able to use such as
    - VCS trigger runs or run from UI
    - apply confirmation on ui


### VCS Trigger
If you want to pass secret to VCS trigger, you need to register it in workspace setting.
There is no other way to pass sensitive variabels at the momemnt.
The variables can be passed via tfvars files.

### Apply and plan

- CLI
- API
- UI
- VCS

### destroy
- CLI
- API
- UI

### Speculative plan
- API
- UI
- VCS


## Organization

## Project


## Workspace

- assessments_enabled
- auto_apply
    - https://developer.hashicorp.com/terraform/cloud-docs/workspaces/settings#auto-apply
    - -auto-approve must be used
- auto_apply_run_trigger 
- auto_destroy_activity_duration
- auto_destroy_at
- file_triggers_enabled
    - Whether to filter runs based on the changed files in a VCS push
    - default to true
    - If disabled, any push will trigger a run.
- force_delete
- project_id
- queue_all_runs
- source_name
    - If set, this will be displayed on the workspace as "Created via "
- source_url
- speculative_enabled
- structured_run_output_enabled
    - Whether this workspace should show output from Terraform runs using the enhanced UI when available


## Execution Mode

## auto-approve

If you use local execution mode, `terraform apply -auto-approve` applies the plan without asking for confirmation.
This is because it will not run

If you use remote execution mode, `terraform apply -auto-approve` will ask you to approve the plan if you do not have a permisison(apply run) in the workspace.

If you use remote executoin mode with the team token, `terraform apply -auto-approve` will not ask you to approve the plan on the terminal but on the UI.




## Reference

