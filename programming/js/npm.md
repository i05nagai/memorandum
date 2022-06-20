---
title: npm
---

## npm

## Install
npm is Installed accompanied by node.js.

update npm

```
npm update -g npm@latest
```

## comamds
install先はdefaultではカレントディレクトリの`node_modules`になる。
`-g`か`--global`でnpmのインストールされている場所にインストーるされる。

```
npm install <name>@<version>
```

`--save-dev`をつけてinstallすると、開発環境の依存packageとして`package.json`にpackageの情報を書き込んでくれる。
`--save`をつけると、一般の依存ライブラリとして`package.json`にかきこまれる。

```
npm install --save-dev grunt
```

対話形式でprojectの初期設定をする。
`package.json`が作られる。

```
npm init
```


## package.json
packageを管理するファイル。
`scripts`にコマンド名とコマンドを記載すると、npm commandでscriptを実行できる。
exeを実行するpackageをインストールした際に利用する。

```json
{
    "scripts": {
        "eslint": "eslint path/to/js"
    },
    "devDependencies": {
        "eslint": "^2.8.0"
    }
}
```

とすると以下のコマンドが使えるようになる。

```
npm run eslint
```

scriptsのコマンドに引数を渡すことはできない。

## package.json

#### peerDependencies
- [Peer Dependencies \| Node\.js](https://nodejs.org/es/blog/npm/peer-dependencies/)
- https://flaviocopes.com/npm-peer-dependencies/


## npm plugin



## Reference
* [npm package.json 日本語版 取扱説明書](http://liberty-technology.biz/PublicItems/npm/package.json.html)
* [npm-scriptsについて - Qiita](http://qiita.com/axross/items/a2a0d148e40b66074858)
