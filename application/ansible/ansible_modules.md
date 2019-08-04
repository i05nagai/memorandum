---
title: ANsible Modules
---

## ANsible Modules
documentは、`ansible-doc module_name`で見ることができる。

#### docker
`docker run`などのかわり。

#### docker_images
`docker build`のかわり。


* `pip`
    * `name`
        * 必須
        * python packageの名前
    * `requirements`
        * 必須
        * `requirements.txt`を指定
* `copy`
    * local/remoteからremoteの指定pathにcopy
    * `dest`
        * 必須
        * srcがdirectoryならこちらもdirectory
        * remoteのabsolute path
    * `src`
        * localのabsolute pathかrelative path
        * pathが`/`で終わっていればdirectoryの中身がcopy
        * pathが`/`で終わっておらず、directoryを指定していればdirectoryごとcopy
        * 必須ではないのは、代わりに`content`を使う場合があるから
    * `content`
        * contentに記載した内容をもつfileをdestにcopy
    * remote_src: yes
        * remoteからremoteのcopy
* `fetch`
    * remoteからlocalへのcopy
* `template`
    * copy時にtemplateをinterpolateする
    * `src`
        * 必須
        * jinja2 templateへのabsolute/relative path
    * `dest`
        * 必須
        * remoteのabsoliute path
* `yum`
    * [yum - Manages packages with the yum package manager — Ansible Documentation](http://docs.ansible.com/ansible/latest/yum_module.html)
    * `name`
        * required
        * package name
        * `state=update`のときは`*`とすると`yum -y update`が実行される
    * `state`
        * present, installed, latest がinstall
        * absent, removedが削除
* `file`
* `script`
    * [script - Runs a local script on a remote node after transferring it — Ansible Documentation](http://docs.ansible.com/ansible/latest/script_module.html)
    * localのscriptをremoteで実行する
* `shell`
    * [shell - Execute commands in nodes. — Ansible Documentation](http://docs.ansible.com/ansible/latest/shell_module.html#shell)
    * remote node 上で`/bin/sh`を介して実行する
    * option
        * chdir
        * creates
        * executable
        * free_form
        * removes
* `command`
    * [command - Executes a command on a remote node — Ansible Documentation](http://docs.ansible.com/ansible/latest/command_module.html)
    * shellを解さずコマンドを実行するので、環境変数などが必要であれば`shell`  moduleを使う
    * remote nodeでcommandを実行する
    * option
        * chdir
        * creates
        * executable
        * free_form
        * removes
* `get_url`
    * [get_url - Downloads files from HTTP, HTTPS, or FTP to node — Ansible Documentation](http://docs.ansible.com/ansible/latest/get_url_module.html)
    * `checksum`
        * `algorith:hash`で渡すとchecksumを確認して、不一致であればDL
    * `force`
        * trueでファイルがDLされていても、再度DLする
* `template`
    * src
    * dest
* `mysql_user`
    * [mysql_user - Adds or removes a user from a MySQL database. — Ansible Documentation](http://docs.ansible.com/ansible/latest/mysql_user_module.html)
    * name
        * user name
    * password
        * password
    * host
        * MySQL usernameのhostの部分
        * login先ではない
    * login_host
        * login先のDBのhost
    * login_port
    * login_user
    * login_password
    * prvi
* `git`
    * clone
        * defaultはyes
        * cloneしないならno
    * dest
        * clone先
    * key_file
        * private key
        * deploy keyを登録している場合は使う
    * repo
        * repositoryのURL
        * git, ssh, httpsのどれか
    * accept_hostkey
        * hostのprivate keyを使うかどうか
        * defaultはno

private repositoryをcloneする場合は、deploy keyをgithubに登録する。

```
- name: Clone git repository
  git:
    repo: "ssh://git@github.com/user/repository.git"
    dest: "/path/to/remote"
    key_file: "/path/to/remote/.ssh/private_rsa_key"
    accept_hostkey: yes
```

#### lineinfile
- [lineinfile – Manage lines in text files — Ansible Documentation](https://docs.ansible.com/ansible/latest/modules/lineinfile_module.html)


#### shell

## Tips
Run locally
[deployment \- Run command on the Ansible host \- Stack Overflow](https://stackoverflow.com/questions/18900236/run-command-on-the-ansible-host)

For shell scripts,

```yaml
- name: Create a package
  become: no
  local_action:
    module: make
    target: make-target-here
```

```yaml
- name: Decrypt the credential
  become: no
  local_action: command cd /path/to/somewher && do-something
```


## Reference

