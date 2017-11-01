---
title: Ansible
---

## Ansible
* [Getting Started — Ansible Documentation](http://docs.ansible.com/ansible/latest/intro_getting_started.html)

```
ansible-playbook -i test-inventory -l test-server --start-at='target task name' --step test.yml
```

* -i
    * inventory
* -l
    * host-patter
* --start-at
    * 指定したtaskから実行
* --step
    * taskごとに実行
* `-u`
    * sshで接続するときのremote user名
* `-m`
    * コマンドを実行するときに指定する

## Commands
* [ansibleで特定のtaskを特定のhostに実行する - Qiita](http://qiita.com/346@github/items/00122556cb2bd6f57998)

```
ansible-playbook 
```

## Conditionals
* [Conditionals — Ansible Documentation](http://docs.ansible.com/ansible/latest/playbooks_conditionals.html)

* `when:`
* `register: var_name`
    * commandの結果を保存できる
    * 保存した結果は、templates, action line, when statementで使える


## Playbook

### inventory
hostsの一覧がinventoryになる。
`production`や`staging`ごとにinventoryを作って管理する。

### Role
* [Roles — Ansible Documentation](http://docs.ansible.com/ansible/latest/playbooks_reuse_roles.html)

Roleは自動で変数のファイルなどを読み込むためのfile構造。
例えば以下のようになる。

```
site.yml
webservers.yml
fooservers.yml
roles/
   common/
     tasks/
     handlers/
     files/
     templates/
     vars/
     defaults/
     meta/
   webservers/
     tasks/
     defaults/
     meta/
```

それぞれのdirectoryの役割は

* tasks
    * このroleで実行されるtask
    * tasksの下に`main.yml`や`debian.yml`などを追いて、`main.yml`でincludeするのは良く使われる
* handlers
    * このroleとこれ以外のroleで使われrう
* defaults
    * このroleのDefaultの変数
* vars
    * その他の変数
* files
    * roleを通してdeployされるファイル
* templates
    * contains templates which can be deployed via this role.
* meta
    * defines some meta data for this role. See below for more details.

tasks, templates, tasksのfileを指定するときは、直接file名の指定で利用できる。


Roleを使うときは、`role:`以下にrole名を記載

```yaml
---
- hosts: webservers
  roles:
     - common
     - webservers
```

`{{ role_path }}`でroleへのpathを参照できる。
`files`においているfileについては、直接参照できる。

```yaml
- copy:
    src: "{{ role_path }}/files/foo.conf"
    dest: /etc/foo.conf
```


`meta/main.yml`にrole間の依存関係を記述できる。

```yaml
---
dependencies:
  - { role: common, some_parameter: 3 }
  - { role: apache, apache_port: 80 }
  - { role: postgres, dbname: blarg, other_parameter: 12 }
```

Roleとして検索されるdirectoryは

* playbookからの相対pathにある`roles/`
* defaultで`/etc/ansible/roles`
 
Communityで定義されたRoleは以下のsiteにある。

* [Ansible Galaxy | Find, reuse, and share the best Ansible content](https://galaxy.ansible.com/)

## Variables
* [Variables — Ansible Documentation](http://docs.ansible.com/ansible/latest/playbooks_variables.html)

変数名は、英数字と`_`のみで、開始文字は英字のみ。
以下のようにmapで定義もできる。
`.`と`[]`で参照できるが、`[]`が良い。


```
foo:
  field1: one
  field2: two
```

```
foo['field1']
foo.field1
```

playbookでの変数の定義は`vars:`に記載する。

```
- hosts: webservers
  vars:
    http_port: 80
```

jinja2 templateでansibleで定義した変数が使える。
`var_files:`に変数を定義したfileを指定することで、変数を読み込める。


```
  vars_files:
    - /vars/external_vars.yml
```

```yaml
---
# in the above example, this would be vars/external_vars.yml
somevar: somevalue
password: magic
```

commandlineからの実行時に変数を渡すこともできる。
passwordなどのsensitiveな情報を渡すときに使える。
`--extra-vars`optionで指定する。
JSON形式でもOK。
`key=value`は全てstringとして扱われるので、listや配列はJSONが必須。

```
ansible-playbook release.yml --extra-vars "version=1.23.45 other_variable=foo"
ansible-playbook release.yml --extra-vars '{"pacman":"mrs","ghosts":["inky","pinky","clyde","sue"]}'
```

### Loops
各taskの中で繰り返し処理を記載できる。

```yaml
- name: add several users
  user:
    name: "{{ item }}"
    state: present
    groups: "wheel"
  with_items:
     - testuser1
     - testuser2
```

複数の値をloopしたい場合は

```yaml
- name: add several users
  user:
    name: "{{ item.name }}"
    state: present
    groups: "{{ item.groups }}"
  with_items:
    - { name: 'testuser1', groups: 'wheel' }
    - { name: 'testuser2', groups: 'root' }
```


## BestPractices

### Vault and variables
* [Best Practices — Ansible Documentation](http://docs.ansible.com/ansible/latest/playbooks_best_practices.html#best-practices-for-variables-and-vaults)


## Multi environment
* [How to Manage Multistage Environments with Ansible | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-manage-multistage-environments-with-ansible)


## tips
ansibleを実行する時は、同じディレクトリの`ansible.cfg`ファイルを読んでいる

inventoryで指定された`gropu_name`にpingできる。

```shell
ansible group_name -m ping
```

### Directory Structure
* [AnsibleをBest Practicesのディレクトリ構成にする - Qiita](http://qiita.com/yuki-k/items/5609f7a23abbafa4ea08)



## module
documentは、`ansible-doc module_name`で見ることができる。

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

## module
documentは、`ansible-doc module_name`で見ることができる。

### docker
`docker run`などのかわり。

### docker_images
`docker build`のかわり。


## Become
他のuserになることができる。

* become
    * Trueで`become_user`で指定しているuserになる
* become_user
    * なりたいuser. defaultでは`root`
* become_method
* become_flags

## Check mode
check modeで実行するとdry runになる。
check modeで動かすためには、moduleがcheck modeに対応している必要がある。

```
ansible-playbook foo.yml --check
```

taskごとにcheck mode時の挙動を設定できる。

* `check_mode: yes`にすると、`--check`がなくてもcheck modeになる
* `check_mode: no`で`--check`がついていても無視する

`--diff`をつけると、変更前との差分を表示する。
diffが大量にでる場合があるので、その場合はdiffをhostに限定するなどする。

```
ansible-playbook foo.yml --check --diff --limit foo.example.com
```

## Configuration file
* [Configuration file — Ansible Documentation](http://docs.ansible.com/ansible/latest/intro_configuration.html)

* `{{ ansible_managed }}`
    * ansibleが自動で設定していることを明示するために、config fileのcommenなどに書かれる

## Using Vault in playbooks
* [Ansible Vaultを利用して秘密情報を暗号化する ｜ Developers.IO](http://dev.classmethod.jp/server-side/ansible/ansible-vault-introduction/)

playbookやplaybook内の文字列をencyrptする機能としてVaultがある。
file全体のencryptはv1.5から、文字列のencryptはv2.3から導入されている。

```
ansible-vault
```

```yaml
notsecret: myvalue
mysecret: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          66386439653236336462626566653063336164663966303231363934653561363964363833313662
          6431626536303530376336343832656537303632313433360a626438346336353331386135323734
          62656361653630373231613662633962316233633936396165386439616533353965373339616234
          3430613539666330390a313736323265656432366236633330313963326365653937323833366536
          34623731376664623134383463316265643436343438623266623965636363326136
other_plain_text: othervalue
```

## reference
* [Ansible コーディング規約 (の例) — そこはかとなく書くよん。](http://tdoc.info/blog/2014/10/09/ansible_coding.html)
* [Ansibleのインベントリファイルでステージを切り替える - Qiita](https://qiita.com/NewGyu/items/5de31d76d2488ab27ed6)
