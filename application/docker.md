# docker

## settings
`~/.docker/config.json`に設定をかく。

### detach key
下記で`ctrl-\`にdetach keyを変更可能。

```json
{
    "detachKeys": "ctrl-\\"
}
```


## completion

### zsh
```shell
curl -L https://raw.githubusercontent.com/docker/compose/$(docker-compose version --short)/contrib/completion/zsh/_docker-compose > ~/.zsh/completion/_docker-compose
```

### reference
* [コマンドライン補完 — Docker-docs-ja 1.12.RC ドキュメント](http://docs.docker.jp/compose/completion.html)

## mac

```shell
sudo port install docker
```

```
brew cask install docker
```

### error

#### docker: Cannot connect to the Docker daemon. Is the docker daemon running on this host?.

```
docker-machine start default  # 立ち上げ
```

## reference
* [Dockerfile のベストプラクティス — Docker-docs-ja 1.9.0b ドキュメント](http://docs.docker.jp/engine/articles/dockerfile_best-practice.html)
