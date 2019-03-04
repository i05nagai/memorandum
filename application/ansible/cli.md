---
title: CLI
---

## CLI

## ansible-playbook

```
ansible-playbook 
```

```
ansible-playbook -i test-inventory -l test-server --start-at='target task name' --step test.yml
```

* `-i`
    * inventory
* `-l`
    * host-patter
* `--start-at <task>`
    * execute from specified task
* `--step <task>`
    * execute a specified task
* `-u`
    * a username when SSH client connects to remote server
* `-m`
    * コマンドを実行するときに指定する

## ansible
[ansible — Ansible Documentation](https://docs.ansible.com/ansible/latest/cli/ansible.html)

```
ansible 
```

* `--private-key`
* `--become-user <BECOME_USER>`
* `--limit <SUBSET>`
* `--inventory-file <iventory>`

## Usage

## Configuration

## Reference
* [ansibleで特定のtaskを特定のhostに実行する - Qiita](http://qiita.com/346@github/items/00122556cb2bd6f57998)
