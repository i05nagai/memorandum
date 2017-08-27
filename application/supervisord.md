---
title: supervisord
---

## supervisord
A process control system.


## Configuration files
`supervisord.conf`が慣習的に使われる。
`-c` optionでfilenameを指定することもできるが、無指定の場合はdefaultで`supervisord.conf`を探す。
探すpathは以下の順序で最初に見つけたものを利用する。

1. `$CWD/supervisord.conf`
2. `$CWD/etc/supervisord.conf`
3. `/etc/supervisord.conf`
4. `/etc/supervisor/supervisord.conf`
5. `../etc/supervisord.conf`
    * 実行ファイルからの相対path
6. `../supervisord.conf`
    * 実行ファイルからの相対path

file formatはWindows INI形式で、pythonのconfig parserでparseできる形式。
Environment variableを使う場合は、下記のように`%(ENV_NAME)s`とする。
以下の例では`LOGLEVEL`環境変数が参照される。

```ini
[program:example]
command=/usr/bin/example --loglevel=%(ENV_LOGLEVEL)s
```

* `[supervisod]`
    * supervisodのglobalなsetting
    * `nodaemon`
        * trueだとsupervisortがdaemonじゃなくforntendで起動する
    * `logfile`
        * supervisorのlogfileのpath
    * `pidfile`
        * supervisorが保持するpidの保存場所へのpath
    * `childlogdir`
        * defaultはpythonのtmpdir
        * `AUTO` child log file
* `[supervisorctl]`
    * `serverurl`
        * supervisordのserverのURL
        * unix socketを使う場合は`unix:///absolute/path/to/file.sock`
        * defaultは`http://localhost:9001`
* `[include]`
    * `files`
        * 読み込むconfigurationファイル
        * `*`, `?`が使える
* `[program:x]`
    * configuration fileは少なくとも1つの`program` headerを含む必要がある
    * `x`はprogram名
    * `command`
    * stdout_logfile
        * processのstdoutのlogへのpath
    * redirect_stderr
        * trueなら、processのstrderrをsupervisodのstdoutにredirectする
    * autostart
        * trueならsupervisodが立ち上がったときに自動でstart
    * autorestart
        * `RUNNING` stateでprcessが終了したときにsupervisorがそのprocessをrestartするか


## Reference
* [Supervisor: A Process Control System — Supervisor 3.3.3 documentation](http://supervisord.org/)
* [Supervisorで簡単にデーモン化 - Qiita](http://qiita.com/yushin/items/15f4f90c5663710dbd56)
