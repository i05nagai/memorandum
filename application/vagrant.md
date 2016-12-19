# vagrant

## インストール
### windows
1. chocolatelyをいれる。
2. virtualboxいれる。
```
chocolatey install virtualbox
```
3. vagrantをインストール
```
choco install vagrant
```

## パッケージ
[vagrantbox.es](http://www.vagrantbox.es/)

## box作成
### windows
[hoge](http://tech.nitoyon.com/ja/blog/2014/02/20/vagrant-win-guest/)

1. `vagrant init bento/centos-7.2`を`centors_7.2`などのディレクトリを作って実行。
2. `vagrant up`でセットアップが始まる。
    * 下記のメッセージの後、SSHの接続で止まる場合はVagrantfileを編集して、virtualboxの起動GUIをONにする。
```
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2222
    default: SSH username: vagrant
    default: SSH auth method: private key
```
    * virtualboxのGUIをONにして、起動するとエラーがでてた。
```
ホストマシンの仮想化支援機能(VT-x/AMD-V)が使用できません。64ビット ゲストOSは64ビットCPUを検出できず、起動できません。
```
    * [このさいと](http://futurismo.biz/archives/1647)を参考に仮想化支援機能をONにする。
3. 


## 設定

* GUIをONにする。
```vagrant
config.vm.provider :virtualbox do |vb|
  vb.gui = true
end
```

## 仮想化支援機能のON
BIOSの仮想化支援機能をONにする。
1. BIOSの画面にはいる。
2. `Intel(R) Virtualization Technology: Enabled`でOK.

