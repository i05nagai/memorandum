---
title: Travis CI CLI
---

## Travis CI CLI
Travis CI provides CLI tools to manage Travis CI from CLI.

## Install
* Ruby1.9.3
* RubyGem

```
gem install travis --no-rdoc --no-ri
```

## CLI
You need to login with github authentification.

```
travis login
```

* -i, --[no-]interactive           be interactive and colorful
* -E, --[no-]explode               don't rescue exceptions
* --skip-version-check         don't check if travis client is up to date
* --skip-completion-check      don't check if auto-completion is set up
* -e, --api-endpoint URL           Travis API server to talk to
* -I, --[no-]insecure              do not verify SSL certificate of API endpoint
* --pro                        short-cut for --api-endpoint 'https://api.travis-ci.com/'
* --org                        short-cut for --api-endpoint 'https://api.travis-ci.org/'
* --staging                    talks to staging system
* -t, --token [ACCESS_TOKEN]       access token to use
* --debug                      show API requests
* --debug-http                 show HTTP(S) exchange
* -X, --enterprise [NAME]          use enterprise setup (optionally takes name for multiple setups)
* --adapter ADAPTER            Faraday adapter to use for HTTP requests
* -g, --github-token TOKEN         identify by GitHub token
* -T, --auto-token                 try to figure out who you are automatically (might send another apps token to Travis, token will not be stored)
* -p, --auto-password              try to load password from OSX keychain (will not be stored)
* -a, --auto                       shorthand for --auto-token --auto-password
* -u, --user LOGIN                 user to log in as
* -M, --no-manual                  do not use interactive login
* --list-github-token          instead of actually logging in, list found GitHub tokens
* --skip-token-check           don't verify the token with github

Check logined user.

```
travis accounts
```

```
travis encrypt
```

```
travis encrypt-file
```

```
travis sshkey
```

* -i, --[no-]interactive
    * be interactive and colorful
* -E, --[no-]explode
    * don't rescue exceptions
* --skip-version-check
    * don't check if travis client is up to date
* --skip-completion-check
    * don't check if auto-completion is set up
* -e, --api-endpoint URL
    * Travis API server to talk to
* -I, --[no-]insecure
    * do not verify SSL certificate of API endpoint
* --pro
    * short-cut for --api-endpoint 'https://api.travis-ci.com/'
* --org
    * short-cut for --api-endpoint 'https://api.travis-ci.org/'
* --staging
    * talks to staging system
* -t, --token [ACCESS_TOKEN]
    * access token to use
* --debug
    * show API requests
* --debug-http
    * show HTTP(S) exchange
* -X, --enterprise [NAME]
    * use enterprise setup (optionally takes name for multiple setups)
* --adapter ADAPTER
    * Faraday adapter to use for HTTP requests
* -r, --repo SLUG
    * repository to use (will try to detect from current git clone)
* -R, --store-repo SLUG
    * like --repo, but remembers value for current directory
* -D, --delete
    * remove SSH key
* -d, --description DESCRIPTION
    * set description
* -u, --upload FILE
    * upload key from given file
* -s, --stdin
    * upload key read from stdin
* -c, --check
    * set exit code depending on key existing
* -g, --generate
    * generate SSH key and set up for given GitHub user
* -p, --passphrase PASSPHRASE
    * pass phrase to decrypt with when using --upload

## Usage

## Configuration

## Tips


### Validating .travis.yml files
以下のサイトでonlineのvalidationができる。
* [Validate your .travis.yml file](http://lint.travis-ci.org/)

lint

```
travis lint /path/to/.travis.yml
```

### Encrypting your credentials
tokenがわかると誰でも通知できてしまうので、tokenを暗号化したものを`.travis.yml`に記載する。
暗号化はCommand line toolsをインストールし、以下を実行する。

```
travis encrypt "account_name:token#channel"
```

実行すると下記が出力される。

```
Detected repository as repository/name, is this correct? |yes| yes
Please add the following to your .travis.yml file:

  secure: "key"

  Pro Tip: You can add it automatically by running with --add.
```

`secure: "key"`の部分をコピーして`.travis.ylm`に以下のように貼り付ける。　

```yaml
notifications:
  slack:
    rooms:
      - secure: "key"
```

Travis CLIで、暗号化ができる。
どのくらい信頼度があるかは不明。

```
travis encrypt SOMEVAR=secretvalue
```

を実行すると

```
secure: ".... encrypted data ...."
```

と暗号化されたデータが得られる。
これを暗号化前のkeyとしてymlにおけば良い。


## Reference
* [Private Dependencies \- Travis CI](https://docs.travis-ci.com/user/private-dependencies/)
* [Encrypting Files \- Travis CI](https://docs.travis-ci.com/user/encrypting-files)
