---
title: Ruby oneliner
---

## oneliner

#### ディレクトリ以下のファイルの最大行の長さを表示
* 1列目ファイル名
* 2列目行の長さ
* 3列目行番号

```ruby
ruby -e 'Dir.glob("mafipy/**/*.py").each{|f| puts [f.chop, File.open(f).to_a.map.with_index{|l, idx| [l.length, idx] }.max{|a, b| a[0] <=> b[0]}].join("\t") }'
```

#### Intersection of two files for each rows

```ruby
ruby -e 'a=File.read("editor.txt");b=File.read("editor.txt");print a.split & b.split'
```

```ruby
ruby -e 'a=File.read("editor.txt");b=File.read("editor.txt");print a.split & b.split'
```


## Reference
* http://reference.jumpingmonkey.org/programming_languages/ruby/ruby-one-liners.html
* http://maeharin.hatenablog.com/entry/20130113/ruby_oneliner
* http://maeharin.hatenablog.com/entry/20130110/p1
* http://takuya-1st.hatenablog.jp/entry/2013/08/19/194819
* http://djangoapplab.com/23/
