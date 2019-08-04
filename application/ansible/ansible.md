---
title: Ansible
---

## Ansible
* [Getting Started — Ansible Documentation](http://docs.ansible.com/ansible/latest/intro_getting_started.html)

## Conditionals
* [Conditionals — Ansible Documentation](http://docs.ansible.com/ansible/latest/playbooks_conditionals.html)

* `when:`
* `register: var_name`
    * Store results of commands
    * 保存した結果は、templates, action line, when statementで使える


## inventory
* [Working with Inventory — Ansible Documentation](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html)
- [Conditionals — Ansible Documentation](https://docs.ansible.com/ansible/latest/user_guide/playbooks_conditionals.html)

hostsの一覧がinventoryになる。
`production`や`staging`ごとにinventoryを作って管理する。

## Role
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

#### ansible.cfg
* [Ansible Configuration Settings — Ansible Documentation](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#avoiding-security-risks-with-ansible-cfg-in-the-current-directory)

If the directory of `ansible.cfg` is writable, ansible does not read this configuration automatically.
You need to either change the permission of the directory or specify `ANSIBLE_CONFIG` environment variables.

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
