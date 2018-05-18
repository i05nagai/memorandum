---
title: Embulk
---

## Embulk


## Install

For Linux,

```sh
curl --create-dirs -o ~/.embulk/bin/embulk -L "https://dl.embulk.org/embulk-latest.jar"
chmod +x ~/.embulk/bin/embulk
echo 'export PATH="$HOME/.embulk/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

For OSX,

```sh
brew install embulk
embulk selfupdate
```

## CLI
* `--log-level [LEVEL]`
    * error, warn, info, debug or trace

```
embulk run config.yml
```

```
embulk mkbundle /path/to/bundle_dir
```

で`bundle_dir`が作成され、Gemifileなどが作られる。
Gemfileでinstallする場合は

```
cd /path/to/bundle_dir
embulk bundle
```

でOK。
bundle_dir内にのjruby directoryにgemが保存される。


## Configuration
* [Configuration — Embulk 0.8 documentation](http://www.embulk.org/docs/built-in.html)


### liquid template
* [大量データの転送にEmbulkを使ってみたら本当に楽だった - VOYAGE GROUP techlog](http://techlog.voyagegroup.com/entry/2017/07/31/173839)

liquidテンプレートが使える。
includeで、別ファイルの設定や変数などを読み込むことができる。
includeするファイル名は`_name_of_template.yml.liquid`とすると以下でincludeできる。
liquid tagの中を以下のようにかく。

```liquid
{{ "{% include 'path/to/inc' " }}%}
```

大事なのは、

* file名の接頭辞は`_`
* 拡張子は`.yml.liquid`
* includeするときは、接頭辞と拡張子は省略
* include字のpathはquotationで囲む
* includeするファイルは、includeしているファイルと同じか下の階層でないとだめ
    * pathに`..` は使えない
* `in`や`out`の設定をincludeする場合は、`in`や`out`の下でincludeする

```yaml
in:
  {{% include 'common_input_mysql' %}}
  table: user
out:
  {{% include 'common_output_mysql' %}}
  table: user
```

## Pluginsたち
* [Embulk(エンバルク)プラグインのまとめ - Qiita](http://qiita.com/hiroysato/items/da45e52fb79c39547f69)
    * 一覧

大きく以下に分かれる。

* input plugin
* output plugin

これに属さないものとして、

* csv fromatter plugin
    * 各input/output pluginが中間ファイルとしてcsvを出力することがある
* local executor plugin
    * embulkの実行時のthread数とか実行に関係するもの
* guess executor
    * 転送元の設定をguessする

とかがある。

pluginの管理にGemfileが使える。
defualtのinstall先は`/home/shiro/.embulk/jruby/1.9`の下になる。
install先を変更する場合は`embulk bundle --path /path/to/install_dir`とする。

```
bundle init
echo "gem 'embulk-input-mysql'" >> Gemfile
embulk bundle
```

でGemfileに記載されているpluginがembulkのplugin用のディレクトリにinstallされる。
`embulk mkbundle /path/to/bundle_dir`をすると`/path/to/bundle_dir`に雛形が作られるので、それを利用しても良い。
`mkbundle`自体は雛形を作るだけで、特にinstallなどは関係ない。
`mkbundle` 実行後は bundle_dirに移動して`embulk budnle install`を実行する。
必要であれば、`--path`をつける。

```
embulk run -b /path/to/bundle_dir /path/to/conf.yml
```


## Tips

### Expected object to load ConfigSource but got null
Configurationが正しくない。
例えば、include用の`*.yml.liquid`などをrunした時などに表示される。

### JsonMappingException
以下のエラーのときは、configで設定が必要な項目に値が設定されてない場合が多い。
または、`{{ "{% include 'path/to/inc' " }}%}`とpathをquotationで囲む。

```
Error: org.embulk.config.ConfigException: com.fasterxml.jackson.databind.JsonMappingException: Setting null to a task field is not allowed. Use Optional<T> (com.google.common.base.Optional) to represent null.
```

### RaiseException + path prefix
path_prefixで指定したファイル名と一緒にこのエラーがでている場合は、 `path_prefix`のpathが存在しているかチェックする。

```
Error: org.jruby.exceptions.RaiseException: (Errno::ENOENT) /path/to/intermediate_file.1013.5932.csv
```

### Error: org.jruby.exceptions.RaiseException: (Error)
csvの改行系のエラーの場合が多い。

* allow_quoted_newlines: true

```
Error: org.jruby.exceptions.RaiseException: (Error) failed during waiting a Load job, get_job(), errors:[{:reason=>"invalid", :message=>"Too many errors encountered."}, {:reason=>"invalid", :location=>"mediaupload-snapshot", :message=>"CSV table references column position .., but line starting at position:.... contains only .. columns."}]
```

configに以下を指定すると、複数threadで動作しなくなるので、error messageとして、error positionが出る場合はエラーの場所を追いやすい。

```yaml
exec:
  max_threads: 1
  min_output_tasks: 1
```

### Bad character (ASCII 0)
`compress`がついている場合は除く。
Threadごとに処理しているFileがlogの最初に表示されるので、どのthreadで落ちているかを確認して、処理しているfileを確認。
拡張子前の4桁の数字は、再実行しても不変なので、どのfileで落ちるかはわかる。
落ちたbyte数が表示されるので、該当の場所に移動する。

```
2017-08-17 04:03:36.460 +0000 [ERROR] (Ruby-0-Thread-4: /path/to/plugin.  ): embulk-output-bigquery: failed during waiting a Load job, get_job(xxx, xxxx), errors:[{:reason=>"invalid", :location=>"file-00000000", :message=>"CSV table encountered too many errors, giving up. Rows: 48441; errors: 1."}, {:reason=>"invalid", :location=>"file-00000000", :message=> "Error detected while parsing row starting at position: 23984771. Error: Bad character (ASCII 0) encountered."}]
```

## Reference
* [embulk/embulk-output-bigquery: Embulk output plugin to load/insert data into Google BigQuery](https://github.com/embulk/embulk-output-bigquery#mode)
* [Embulk YAMLメモ(Hishidama's Embulk YAML Memo)](http://www.ne.jp/asahi/hishidama/home/tech/embulk/yaml.html)
* [embulk/embulk: Embulk: Pluggable Bulk Data Loader. http://www.embulk.org](https://github.com/embulk/embulk)
