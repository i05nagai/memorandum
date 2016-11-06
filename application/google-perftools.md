# google-perftools

## Install

### mac

```shell
brew install google-perftools
```

で`/usr/local/lib`に`libprofiler`などがインストールされる。
macではまともに動かなそう。


## Usage
1. `-lprofiler`をlinkしてBuildする。
2. 以下の通り、`CPUPROFILE`を指定して、プログラムを実行する。

```shell
export CPUPROFILE=prof.out
./target
```

`prof.out`がプログラムと同じディレクトリにできる。

元のプログラムとprof fileを指定する。

```shell
pprof ./target ./prof.out
```

## tcmalloc

## heap profiler

## heap checker

## cpu profiler

1. 実行ファイルに`-lprofiler`
2. 環境変数`CPUPROFILE`を以下のように設定
    * `$ CPUPROFILE=/tmp/prof.out <path/to/binary> [binary args]`
3. pprofを実行
```shell
$ pprof <path/to/binary> /tmp/prof.out      # -pg-like text output
$ pprof --gv <path/to/binary> /tmp/prof.out # really cool graphical output
```

## everything one

## configuration option

## environment variables

## compiling on non-linux systems

## performance


## old system issues

## 64-bit issues


## reference
* [gperftools/gperftools: Main gperftools repository](https://github.com/gperftools/gperftools)
* [google-perftoolsでC++プログラムのプロファイリング - ぬうぱんの備忘録](http://nu-pan.hatenablog.com/entry/20140410/1397099300)
* [Google-perftoolsを使ってCPUプロファイリングをとる - PS3 Linux Information Site / Cell/B.E.のパワーを体験しよう](http://cell.fixstars.com/ps3linux/index.php/Google-perftools%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6CPU%E3%83%97%E3%83%AD%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AA%E3%83%B3%E3%82%B0%E3%82%92%E3%81%A8%E3%82%8B)
* [Google Performance Tools を使う（その1） : リード開発メモ](http://freed411.doorblog.jp/archives/35003125.html)
* [プロファイルプログラムで時間が掛かっている場所を特定する(google-perftool) - Qiita](http://qiita.com/kmikmy/items/672efc5e2cde4826bbc7)
