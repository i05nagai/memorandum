---
title: Packer
---

## Packer

## Builder

#### AWS EBS
https://www.packer.io/docs/builders/amazon-ebs.html


* `instance_type`
    *  The EC2 instance type to use while building the AMI, such as t2.smal

## Provisioner

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

## CLI

```
packer build -var-file=variables.json <build>.json
```

## Reference
* https://www.packer.io/
