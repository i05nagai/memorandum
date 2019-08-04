---
title: journald
---

## journald
systemdで標準的なlog管理service.
`/var/run/log/journal` に保存される。
OSを再起動するときえるので、永続化する場合は`/var/log/journal`のdirectoryを作る。
If the directoyr exists, the logs are stored in the directory.

* 保存用ディレクトリーの全容量に対して10%以上
* 該当ディレクトリーのファイルシステムの空き容量が15%以下

The contents stored as log

* systemdのserviceとして起動したdaemonの標準出力／標準エラー出力の内容
* localのprocessがsyslogに出力したmessage
* journald独自のAPI（library関数）に対して出力したメッセージ



`/dev/log`からLogをとって、rsyslogdに渡す。

## CLI
* [journalctl 最低限覚えておくコマンド - Qiita](https://qiita.com/aosho235/items/9fbff75e9cccf351345c)


* --system                Show the system journal
* --user                  Show the user journal for the current user
* -M --machine=CONTAINER     Operate on local container
* -S --since=DATE            Show entries not older than the specified date
* -U --until=DATE            Show entries not newer than the specified date
* -c --cursor=CURSOR         Show entries starting at the specified cursor
* --after-cursor=CURSOR   Show entries after the specified cursor
* --show-cursor           Print the cursor after all the entries
* -b --boot[=ID]             Show current boot or the specified boot
* --list-boots            Show terse information about recorded boots
* -k --dmesg                 Show kernel message log from the current boot
* -u --unit=UNIT             Show logs from the specified unit
* --user-unit=UNIT        Show logs from the specified user unit
* -t --identifier=STRING     Show entries with the specified syslog identifier
* -p --priority=RANGE        Show entries with the specified priority
* -g --grep=PATTERN          Show entries with MESSSAGE matching PATTERN
* --case-sensitive[=BOOL] Force case sensitive or insenstive matching
* -e --pager-end             Immediately jump to the end in the pager
* -f --follow                Follow the journal
* -n --lines[=INTEGER]       Number of journal entries to show
* --no-tail               Show all lines, even in follow mode
* -r --reverse               Show the newest entries first
* -o --output=STRING         Change journal output mode (short, short-precise,
* -x --catalog               Add message explanations where available
* --no-full               Ellipsize fields
* `-a --all`
    * Show all fields, including long and unprintable
* -q --quiet                 Do not show info messages and privilege warning
* --no-pager              Do not pipe output into a pager
* --no-hostname           Suppress output of hostname field
* -m --merge                 Show entries from all available journals
* -D --directory=PATH        Show journal files from directory
* --file=PATH             Show journal file
* --root=ROOT             Operate on files below a root directory
* --interval=TIME         Time interval for changing the FSS sealing key
* --verify-key=KEY        Specify FSS verification key
* --force                 Override of the FSS key pair with --setup-keys

* -N --fields                List all field names currently used
* -F --field=FIELD           List all values that a specified field takes
* --disk-usage            Show total disk usage of all journal files
* --vacuum-size=BYTES     Reduce disk usage below specified size
* --vacuum-files=INT      Leave only the specified number of journal files
* --vacuum-time=TIME      Remove journal files older than specified time
* --verify                Verify journal file consistency
* --sync                  Synchronize unwritten journal messages to disk
* --flush                 Flush all journal data from /run into /var
* --rotate                Request immediate rotation of the journal files
* --header                Show journal header information
* `--list-catalog`
    * Show all message IDs in the catalog
* --dump-catalog          Show entries in the message catalog
* --update-catalog        Update the message catalog database
* --new-id128             Generate a new 128-bit ID
* --setup-keys            Generate a new FSS key pair short-iso, short-iso-precise, short-full,
* `-l, `
* `-o, --output=`
    * short, short-precise, short-iso, short-full, short-monotonic, short-unix, verbose, export, json, json-pretty, json-sse, cat
* `-e --pager-end`
    * pagerの最後にjump


lessでlogを表示

```
journalctl
```

lessなし

```
journalctl -l --no-pager
```

特定serviceのLog

```
journalctl -u hoge.service
```

tail -f

```
journalctl -f
```

最近のmessage

```
journalctl -e
journalctl -xe
```

特定のserviceのmessage

```
journalctl -u sshd
journalctl -u httpd
journalctl -u nginx
journalctl -u mysqld
journalctl -u cronie
journalctl -u updatedb
journalctl -u 'up*'
```

## Configuration
`/etc/systemd/journald.conf`

* SystemMaxUse
* RuntimeMaxUse

## Reference
* [RHEL7/CentOS7のjournaldについてのもろもろ - めもめも](http://enakai00.hatenablog.com/entry/20141130/1417310904)
