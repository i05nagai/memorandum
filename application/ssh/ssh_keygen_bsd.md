---
title: ssh-keygen BSD
---
## ssh-keygen
ssh-keygen command in BSD. e.g. OSX.

## CLI

```
ssh-keygen
```

* `-C comment`
    * Add comment to key
* `-c`
    * Requests changing the comment in the private and public key files.
    * This operation is only supported for `RSA1 keys` and keys stored in the newer `OpenSSH` format.
    * The program will prompt for the file containing the private keys, for the passphrase if the key has one, and for the new comment.
* `-E fingerprint_hash`
    * `sha256` by default
    * Valid options are: `md5` and `sha256`
    * Specifies the hash algorithm used when displaying key fingerprints.
* `-l`
* `-L`
    * Prints the contents of one or more certificates
* `-l`
    * Show fingerprint of specified public key file.
    * Private RSA1 keys are also supported.
    * For RSA and DSA keys ssh-keygen tries to find the matching public key file and prints its fingerprint.
    * If combined with -v, a visual ASCII art representation of the key is supplied with the fingerprint.
* `-f filename`
    * Specifies the filename of the key file.
* `-N new_passphrase`
    * Provides the new passphrase.

## Usage
Generate ssh key

```
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

Show finger print of public key in `md5`. You can specify private key as well.

```
ssh-keygen -E md5 -l -f /paht/to/public_key
```

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

