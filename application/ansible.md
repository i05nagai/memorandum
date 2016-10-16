# ansible

## tips
ansibleを実行する時は、同じディレクトリの`ansible.cfg`ファイルを読んでいる

inventoryで指定された`gropu_name`にpingできる。

```shell
ansible group_name -m ping
```

## module
documentは、`ansible-doc module_name`で見ることができる。

### docker
`docker run`などのかわり。

### docker_images
`docker build`のかわり。



## reference
* [Ansible コーディング規約 (の例) — そこはかとなく書くよん。](http://tdoc.info/blog/2014/10/09/ansible_coding.html)
