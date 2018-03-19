---
title: proc
---

## proc
`/proc/`以下にpidごとにprocessの情報が作成されている。


* `fd/`
    * fd以下にはfile descriptorの情報
    * 利用されているfile descriptor

```sh
# get pid
for i in `ps aux | grep grep_text | awk '{print $2}'`
do
    ls -la /proc/$i/fd
done
```


## Reference
