# code climate
コードの品質をはかる。
coverallsは、coverageのみだが、code climateはコードの品質という点でcoverageや

## codeclimate cli
dockerで提供されているが別途packageも入手可能。

```shell
docker pull codeclimate/codeclimate
```

### OSX

```shell
brew tap codeclimate/formulae
brew install codeclimate
```

## Supported languages
* Ruby
* Python
* Javascript

## Test Coverage



### python
CI環境などで以下を行うようにする。

1. `codeclimate-test-reporter`をinstall
	* `codeclimate-test-reporter`を`requirements.txt`に追加
	* `pip install codeclimate-test-reporter` 
2. coverageの結果を出力する
	* 対応しているreport形式は以下
	* 以下はどれも実行ディレクトリに`.coverage`というレポートを生成する
	* `pytest`
	* `nose`
	* `coverage.py`
3. 生成された`.coverage`を`codeclimate-test-reporter`でcodeclimateへ送る

```shell
export CODECLIMATE_REPO_TOKEN=<token>
codeclimate-test-reporter 
```

もしくは、

```shell
codeclimate-test-reporter --token <token>
```

### Reference
* [Code Climate](https://codeclimate.com/repos/583d8d021ddf8a227f000437/coverage_setup)
* [Setting Up Test Coverage](https://docs.codeclimate.com/docs/setting-up-test-coverage#section-how-to)
* [codeclimate/python-test-reporter: Uploads Python test coverage data to Code Climate https://codeclimate.com](https://github.com/codeclimate/python-test-reporter)

## Analysis Configuration

### Switching to engines-based analysis
python, php, ruby, javascriptのみ対応。

#### Python
以下の3つに対応。

* Complexity
	* Radonによる複雑度。cyclmatic complexityを計測。
* Style
	* pep8
* Duplication
	* Duplication engine

### Configuring Your Code Climate Analysis


### Disabling Individual Engines



### Example .codeclimate.yml

#### Refrence
* [Example .codeclimate.yml](https://docs.codeclimate.com/docs/example-codeclimateyml)


## Reference
* [Code Climate](https://docs.codeclimate.com/)
* [Code ClimateをPythonリポジトリに適用する - Qiita](http://qiita.com/vmmhypervisor/items/b642b22f6a78f1f8668d)

