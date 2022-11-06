---
title: Packer
---

## Packer

```
{
  "builders": [
    {
      "type": "amazon-ebs",
      "access_key": "...",
      "secret_key": "...",
      "region": "us-east-1",
      "source_ami": "ami-fce3c696",
      "instance_type": "t2.micro",
      "ssh_username": "ubuntu",
      "ami_name": "packer {{timestamp}}"
    }
  ],
  "provisioners": [
    {
      "type": "shell",
      "script": "setup_things.sh"
    }
  ]
}
```


## Builder

#### AWS EBS
https://www.packer.io/plugins/builders/amazon

* `instance_type`
    *  The EC2 instance type to use while building the AMI, such as t2.smal

## Provisioner

#### shell

```
{
  "provisioners": [
    {
      "type": "shell",
      "playbook_file": "./playbook.yml"
    }
  ],
}
```

#### error-cleanup-provisioner

```
{
  "error-cleanup-provisioner": {
    "type": "shell-local",
    "inline": ["echo 'rubber ducky'> ducky.txt"]
  }
}
```

#### Ansible
https://www.packer.io/docs/provisioners/ansible.html

* `ansible_env_vars`
* `command`
* `ssh_host_key_file`
    * The SSH key that will be used to run the SSH server on the host machine to forward commands to the target machine
* `ssh_authorized_key_file `
    * the SSH public key of Ansible ssh_user
* `user`
    * ansible user

```
{
  "provisioners": [
    {
      "type": "ansible",
      "playbook_file": "./playbook.yml"
    }
  ],
}
```

## Variables
https://www.packer.io/docs/templates/legacy_json_templates/user-variables


## CLI

```
packer build -var-file=variables.json <build>.json
```

## Reference
* https://www.packer.io/
