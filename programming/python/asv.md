---
title: asv
---

## airspeed velocity

numpy, scipyで使われているbenchmark用のpython library

Projects which use asv

* https://github.com/astropy/astropy-benchmarks
* [pv/numpy-bench: Numpy benchmark results](https://github.com/pv/numpy-bench)

## Install

```python
pip install asv
```

また、別途`virtualenv`ないし、`conda`が必要。

### `virtualenv`を入れる
* [Virtualenv — virtualenv 15.1.0 documentation](http://virtualenv.pypa.io/en/stable/)

confを`env_type`が`virtualenv`の場合に必要。

```python
pip install virtualenv
```

### `conda`をいれる
`anaconda`もしくは`miniconda`をインストールすれば入る。

## Tutorial
* `results`と`html`はsubmodule管理するので、出力ディレクトリを変更する
    * `env`も統一感の為同じ位置にかえる
* resultsとhtmlはsubmodule化する
    * resultsが増えすぎる場合は

```
mkdir benchmarks
cd benchmarks
asv quickstart
```

`asv quickstart`で`asv.conf.json`が生成される。
依存するライブラリなどは、`asv.conf.json`の`matrix`に記載する。
benchamrkの実行は以下でできる。

```
asv run
```

実行結果から、htmlを作成する。

```
asv publish
```

localにhtmlサーバをたてし、htmlをpreviewする。

```
asv preview
```

```
cd bechmarks/html
git init
git commit --alow-empty -m "Initial commit"
git add .
git commit -m "Add first benchmarks"
git remote add origin https://github.com/i05nagai/mafipy_benchmarks.git
git push origin master
```

Settings -> OptionsからGithu pagesのSourceをmaster branchに変更する。
READMEを以下の形で書いておくと、Github pagesにたどり着けるので楽。

```
echo "
mafipy benchmraks
=================

mafipy benchmarks

reference
=========
* Benchmark pages

    * https://i05nagai.github.io/mafipy_benchmarks/
" > README.rst

```

## Usage

```
asv run 
asv publish
asv preview
```

## Using airspeed velocity

### Setting up a new benchmarking project
`asv`は`asv.conf.json`ファイルが設定ファイルとなっている。

`asv quickstart`コマンドを実行すると、`asv.conf.json`ファイルの雛形を生成してくれる。

```
$ asv quickstart
Is this the top level of your project repository? [y/n] n
Edit asv.conf.json to get started.
```

カレントディレクトリがprojectのrootであれば、`y`と回答すれば良い。
必要に応じて生成された`asv.conf.json`の中身を編集する。

## Configuration

`asv.conf.json`のreferenceに詳細がある。
[asv.conf.json reference — airspeed velocity 0.3.dev1071+390145a5 documentation](http://asv.readthedocs.io/en/latest/asv.conf.json.html).

* `project`
    * benchmarkを実行するprojectの名前
    * 通常はライブラリの名前`numpy`とか。
* `project_url`
    * projectのURL
    * ライブラリ用のHPなどを作っている場合は設定する
    * なければライブラリを管理しているGitHubのURLでもいれる
* `repo`
    * repositoryのURL
    * GitHubを使っている場合はGitHubのrepositoryのURLで良い
* `show_commit_url`
    * commit参照用のbase URL
    * asvはcommitごとにbenchmarkを実行するが、各benchmarkのcommitを参照できるようになる
    * githubの場合は`http://github.com/$OWNER/$REPO/commit/`の形で指定する。
        * `$OWNER`は自分のusernmae
        * `$REPO`はrepositoryの名前
* `environment_type`
    * benchmark実行用の仮想環境の生成方法を指定する
    * `conda`もしくは`virutalenv`を指定


指定したcommitからのbenchmarkを計測する。

```json
    "regressions_first_commits": {
       "some_benchmark": "352cdf",  // Consider regressions only after this commit
       "another_benchmark": null,   // Skip regression detection altogether
    }
```


### Running benchmarks

#### machine information


#### Environments

#### Benchmarking
再現性のために、全てのbenchmarkは別々のプロセスで実行される。

asvは`range`引数を渡すことで、範囲内のcommitのBenchmarkを計測することができる。
引数は、`git log`ないしMercurial logに渡されるので、`gitrevisions manpages`などのsyntaxが使える。

* [gitrevisions(7)](https://www.kernel.org/pub/software/scm/git/docs/gitrevisions.html)

例えば、gitのrepositoryで、branchが作られてからの全てのcommitのbenchmarkを測る場合は、以下のコマンドを実行する。

```
asv run mybranch@{u}..mybranch
```

例えば、特定のタグからの全てのコミットのbenchmarkを測る場合は、以下のコマンドを実行する。

```
asv run v0.1..master
```

また、次の引数も利用できる。
`ALL`はそのbranchの全てのコミットを実行する。
過去のコミットでbenchmarkが実行できないものについては`failed`となる。

```
asv run ALL
```

他のmachineで実行されたbenchmarkでこのmachineで実行されてないものを実行する。

```
asv run EXISTING
```

最後にbenchmarksを実行したcommitから追加されたcommitのbenchmarkを実行する。
CIで実行している場合は有用。

```
asv run NEW
```

また、このmachineで実行されていないbenchmarksを全て実行する場合は以下のようにする。

```
asv run --skip-existing-commits ALL
```

## Tips

### ValueError: Using the currently installed project version: operations requiring repository are not possible
以下のmessageがでている場合は、`pip install virtualenv`でvirtualenvをいれる。

```
virtualenv package not installed
```

###  Can not determine what kind of DVCS to use for URL '..'
`dvcs`が`.git`だと発生する。


### circle ci with asv
最初の`asv run`実行時にmachine情報が必要。
Circle CIにsshでログインして、`asv run`を実行すると、入力画面がでて`~/.asv-machine.json`が生成される。
この中身をコピーしておき、`asv run`の前に`~/.asv-machine.json`を配置する。

### KeyError
Fixed in `master` branch.  0.21 has this problem.

```
executing 'asv publish'
-[ 11.11%]  Loading machine info
-[ 22.22%]  Getting params, commits, tags and branches
-[ 33.33%]  Loading results
-[ 44.44%]  Detecting steps
-[ 55.56%]  Generating graphs
-[ 66.67%]  Generating output for SummaryGrid
-[ 77.78%]  Generating output for SummaryList
-[ 88.89%]  Generating output for RegressionsTraceback (most recent call last):
  File "/usr/local/bin/asv", line 11, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.6/site-packages/asv/main.py", line 38, in main
    result = args.func(args)
  File "/usr/local/lib/python3.6/site-packages/asv/commands/__init__.py", line 48, in run_from_args
    return cls.run_from_conf_args(conf, args)
  File "/usr/local/lib/python3.6/site-packages/asv/commands/publish.py", line 69, in run_from_conf_args
    return cls.run(conf=conf, env_spec=args.env_spec)
  File "/usr/local/lib/python3.6/site-packages/asv/commands/publish.py", line 193, in run
    cls.publish(conf, repo, benchmarks, graphs, revisions)
  File "/usr/local/lib/python3.6/site-packages/asv/plugins/regressions.py", line 61, in publish
    cls._save_feed(conf, benchmarks, regressions, revisions, revision_to_hash)
  File "/usr/local/lib/python3.6/site-packages/asv/plugins/regressions.py", line 124, in _save_feed
    revision = revisions[results.commit_hash]
KeyError: '4b10ae58a3aa6b8d6f9096f8f85ed06d4f88973a'
```

You need to delete all `commithash-....json` in your result dir.

## Reference
* [GitHub - spacetelescope/asv: Airspeed Velocity: A simple Python benchmarking tool with web-based reporting](https://github.com/spacetelescope/asv)
* [airspeed velocity — airspeed velocity 0.3.dev1064+aa11c73c documentation](http://asv.readthedocs.io/en/latest/)
