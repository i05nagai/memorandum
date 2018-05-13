---
title: asv
---

## airspeed velocity

numpy, scipyで使われているbenchmark用のpython library

* 
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

## Reference
* [GitHub - spacetelescope/asv: Airspeed Velocity: A simple Python benchmarking tool with web-based reporting](https://github.com/spacetelescope/asv)
* [airspeed velocity — airspeed velocity 0.3.dev1064+aa11c73c documentation](http://asv.readthedocs.io/en/latest/)
