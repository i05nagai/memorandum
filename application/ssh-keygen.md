
## ssh-keygen


## Tips

### Has passphrase or not
* [public key infrastructure - How to check if an SSH private key has passphrase or not? - Information Security Stack Exchange](https://security.stackexchange.com/questions/129724/how-to-check-if-an-ssh-private-key-has-passphrase-or-not)

Pass passphraseがついているかどうかは、鍵を見ればわかる。
以下のProc-Typeなどがついてればpassphraseつきの鍵。

```
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: DES-EDE3-CBC,556C1115CDA822F5

AHi/3++6PEIBv4kfpM57McyoSAAaT2ECxNOA5DRKxJQ9pr2D3aUeMBaBfWGrxd/Q
```

下記のコマンドでpassphraseの認証が求められるので、それでも確認可能。

```
ssh-keygen -yf path_to_key
```

## Reference
* 
