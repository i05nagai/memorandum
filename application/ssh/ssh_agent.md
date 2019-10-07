---
title: ssh-agent
---

## ssh-agent

## Install

```
apt-get install -y openssh-client
```

local machineでssh-agentを起動し、agentに鍵を登録する。

```
ssh-agent zsh
ssh-add /path/to/key
ssh username@host-remote
```

remoteでagentが設定できるかは以下で確認できる。

```
ssh-add -l
```

でlocalでssh-addした鍵の情報が出力されればssh-agentが作動している。

## agent forward
remoteから更に別のmachineにsshする場合に、localの鍵を使ってremoteからsshできる。
localの`~/.ssh/config`に`ForwardAgent    yes`を書いておくか、remoteからのssh時に`-A`optionでSSHする

remote上で以下を実行する

```
ssh -A username2@host-remote-remote
# if ForwardAgent yes
# ssh username2@host-remote-remote
```

#### Timeout
- https://unix.stackexchange.com/questions/122511/configuring-the-default-timeout-for-the-ssh-agent

- By default, timeout is infinite.
- The value will be overridden by timeout of `ssh-add`


#### Run command
Run commands reading private key from a file.

```
# Run comands
ssh-agent bash <<EOF
    ssh-add ~/.ssh/id_rsa
    command
EOF
# Run comands
ssh-agent bash -c '
    ssh-add ~/.ssh/id_rsa \
    command
'
```

Run commands reading private key from environment variables

```
export KEY=$(cat /path/to/key)
ssh-agent bash -c '
    echo "${KEY}" | ssh-add -
    command
'
ssh-agent bash -c "
    echo \"${KEY}\" | ssh-add -
    command
"
```

## Reference
* [ssh-agentのforwardを利用し、ホストマシンとローカルVMの非公開鍵を共有する - MANA-DOT](http://blog.manaten.net/entry/ssh-agent-forward)
