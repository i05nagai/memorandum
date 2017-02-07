# oneline

## ディレクトリ以下のファイルの最大行の長さを表示
* 1列目ファイル名
* 2列目行の長さ
* 3列目行番号

```ruby
ruby -e 'Dir.glob("mafipy/**/*.py").each{|f| puts [f.chop, File.open(f).to_a.map.with_index{|l, idx| [l.length, idx] }.max{|a, b| a[0] <=> b[0]}].join("\t") }'
```
