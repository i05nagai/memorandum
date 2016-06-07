# aws

## ec2
接続は以下の方法。

```sh
ssh -i key.pem username@ipaddress
```

* `key.pem`は、キーペア作成時にダウンロードできる秘密鍵
* `username`は、AMIインスタンスによって決まるrootユーザで、`ec2-user`もしくは`root`が多い。
* ipaddressはec2のアドレス

### tips
* SGのインバウンドは、HTTPの場合はAnywhereじゃないとだめ？
    * テザリングのせい？
* インスタンス作成後はstatusを`stop`にすればインスタンスタイプを変更できる。



## aws-cli

### zsh用の補完
下記を読み込む。
```zsh
source /usr/local/bin/aws_zsh_completer.sh
```

##

