---
title: pritunl
---

## pritunl
VPN server

```sh
sudo tee -a /etc/apt/sources.list.d/mongodb-org-3.6.list << EOF
deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse
EOF

sudo tee -a /etc/apt/sources.list.d/pritunl.list << EOF
deb http://repo.pritunl.com/stable/apt xenial main
EOF

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com --recv 7568D9BB55FF9E5287D586017AE645C0CF8E292A
sudo apt-get update
sudo apt-get --assume-yes install pritunl mongodb-org
sudo systemctl start pritunl mongod
sudo systemctl enable pritunl mongod
```

## Configuration
* [Configuration](https://docs.pritunl.com/docs/configuration-5)


defaultのusernameとpasswordは`pritunl`
Webのinitialsetの項目は`/etc/pritunl.conf`に設定される。
直接設定を書くこともできる。

```conf
{
    "debug": false,
    "bind_addr": "0.0.0.0",
    "port": 443,
    "log_path": "/var/log/pritunl.log",
    "temp_path": "/tmp/pritunl_%r",
    "local_address_interface": "auto",
    "mongodb_uri": ""
}
```


## Reference
* [Pritunl - Open Source Enterprise Distributed OpenVPN and IPsec Server](https://pritunl.com/)
* [pritunlでCentOSにVPNサーバー構築 - Qiita](https://qiita.com/sue71/items/7b30766ddf070d4e3f25)
* [GitHub - jippi/docker-pritunl: Ubuntu Xenial + Pritunl](https://github.com/jippi/docker-pritunl)
* [Pritunl で簡単にVPNサーバを構築する - Carpe Diem](http://christina04.hatenablog.com/entry/2014/11/01/141627)
* [Getting Started](https://docs.pritunl.com/docs)
