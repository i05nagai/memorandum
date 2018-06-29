---
title: Vault CLI
---

## Vault CLI


## CLI

```
Usage: vault <command> [args]
```

### Common commands
Read data and retrieves secrets

```
vault read
```

Write data, configuration, and secrets

```
vault write
```

Delete secrets and configuration

```
vault delete      
```

List data or secrets

```
vault list
```

Authenticate locally

```
vault login       
```

Start a Vault server

```
vault server      
```

Print seal and HA status

```
vault status
```

Unwrap a wrapped secret

```
vault unwrap      
```

### Other commands

Interact with audit devices             

```
vault audit          
```

Interact with auth methods              

```
vault auth           
```

Interact with Vault's Key-Value storage 

```
vault kv <subcommand> [options] [args]
```

* `delete`
    * Deletes versions in the KV store
* destroy
    * Permanently removes one or more versions in the KV store
* enable-versioning
    * Turns on versioning for a KV store
* get
    * Retrieves data from the KV store
* list
    * List data or secrets
* metadata
    * Interact with Vault's Key-Value storage
* patch
    * Sets or updates data in the KV store without overwriting
* put
    * Sets or updates data in the KV store
* rollback
    * Rolls back to a previous version of data
* undelete
    * Undeletes versions in the KV store

Interact with leases                    

```
vault lease          
```

Perform operator-specific tasks         

```
vault operator       
```

Retrieve API help for paths             

```
vault path-help      
```

Interact with policies

```
vault policy         
```

Interact with secrets engines           

```
vault secrets        
```

Initiate an SSH session                 

```
vault ssh            
```

Interact with tokens                    

```
vault token          
```

## Usage

`@cert.pem` is contents of the file

```
$ vault kv put secret/prod/cert/mysql cert=@cert.pem
```

## Configuration

## Reference
