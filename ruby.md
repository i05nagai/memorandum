# ruby


## tips

### ファイル読み込み1
```ruby
File.open("filename") do |file|
    #1行ずつ
    file.each_line do |line|

    end
    #1度によみこみ
    file.read.split('\n').each |line|

    end
    #1文字ずつ
    file.each_char |char|

    end
end
```

### ファイル読み込み4
ファイルロック+読みこみ
```ruby
File.open("filename") do |file|
    file.flock(File::LOCK_EX)
    file.each_line |line|

    end
end
```

### ファイル読み込み1
```ruby

```

### n進数へ変換
```ruby
a = 255
n = 3
p a.to_s(n) #n進数
```

### n進数から数値へ変換

```ruby
a = '1011011'
p ("0b" + a).oct 
```

## 配列

### 逆からeach
reverse_each


