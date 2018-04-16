---
title: fluentd buffer
---

## fluentd buffer
[Buffer Plugin Overview | Fluentd](https://docs.fluentd.org/v0.12/articles/buffer-plugin-overview)

* set of chunks
* chunkはrecordsのcollectionで一つのblobにまとめたもの
* chunckはoutput queueへflushされる



* buffer_type
    * file, memory
    * output pluginのbackend
* buffer_chunk_limit
    * default 8MB
    * maximum size of chunck
* buffer_queue_limit
    * default 256
    * limitをこえるとerror handling mechanismを呼び出す
* flush_interval
    * default 60
    * 次のbuffer flushまでの秒数

* detect_subservice false
* buffer_queue_full_action block
* disable_retry_limit
* num_threads 2

### file

* buffer_path
    * buffer_typeがpathのときfileのpathを指定
* retry_wait
* max_retry_wait 30
* `retry_limit`

### memory


## Reference
