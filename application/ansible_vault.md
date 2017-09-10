---
title: Ansible Vault
---

## Ansible Vault

## CLI

fileをencrypt

```
ansible-vault encrypt foo.yml bar.yml baz.yml
```

encryptされたfileをdecrypt

```
ansible-vault decrypt foo.yml bar.yml baz.yml
```

decryptして中身を確認する

```
ansible-vault view foo.yml bar.yml baz.yml
```

文字列をencryptする

```
ansible-vault encrypt_string –vault-id a_password_file ‘foobar’ –name ‘the_secret’
```

* variable name

## Reference
* [Ansible Vault — Ansible Documentation](http://docs.ansible.com/ansible/latest/vault.html#encrypt-string-for-use-in-yaml)
