---
title: Terraform Cloud
---

## Terraform Cloud


- speculative plans
    - https://developer.hashicorp.com/terraform/cloud-docs/run/remote-operations#speculative-plans
    - Speculative plans are plan-only runs
    - Speculative plans can begin without waiting for other runs to finish because they don't affect real infrastructure.

## run modes

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
- 

## Reference

