---
title: Airflow Error Tips
---

## Airflow Error Tips

### EOF read where object expected airflow
Workerのようになっている場合は、workerのMemroyなどのresourceが足りていない

```
WorkerLostError: Worker exited prematurely: signal 9 (SIGKILL).
```

### airflow smtp error Connection refused
slaでmailを送ろうとしたが、smtpに接続できない。
slaをoffにする。

### Error ALTER TABLE dag MODIFY last_scheduler_run DATETIME(6) NULL
resetdbなどで以下のエラーがでる場合がある。

```
sqlalchemy.exc.ProgrammingError: (_mysql_exceptions.ProgrammingError) (1064, "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '(6) NULL' at line 1") [SQL: u'ALTER TABLE dag MODIFY last_scheduler_run DATETIME(6) NULL']
```

mili secondが必要なので、 MySQLのversionを5.6.4にあげる必要がある。

* [AIRFLOW-748 Cannot upgradedb from airflow 1.7.0 to 1.8.0a4 - ASF JIRA](https://issues.apache.org/jira/browse/AIRFLOW-748)

### Error with --debug
debugで立ち上げるとエラーになる。

```
airflow webserver --debug
```

とすると、エラーがでる。
2017/5/2にmasterで修正済みらしい。

* [AIRFLOW-1165 airflow webservice crashes on ubuntu16 - python3 - ASF JIRA](https://issues.apache.org/jira/browse/AIRFLOW-1165)

### TemplateNotFound Error
TemplateNotFoundというエラーがでる場合、bashcommandの引数の最後にスペースがあるか確認する。
Bash scriptを直接呼ぶ場合は、最後にスペースが必要。
そうでない場合は、引数はJinja templateとして扱われるので、`BashOperator`classの引数`template`に空でも値を渡す必要がある。。

* [python - TemplateNotFound error when running simple Airflow BashOperator - Stack Overflow](https://stackoverflow.com/questions/42147514/templatenotfound-error-when-running-simple-airflow-bashoperator)

### Error: SMTP Error
`airflow.cfg`内の`[smtp] smtp_starttls = False`にする

```
WARNING - section/key [smtp/smtp_user] not found in config
```


### Error. No such transport: sqla
`airflow.cfg`にCeleryのbrokerのURLに`sqla+mysql`と書いていると起こる。
Celeryの依存パッケージである `kombu`の問題らしい。
最新の`kombu`では解決しているので、updateする。

* [AIRFLOW-797 CLONE - No such transport: sqla when using CeleryExecutor - ASF JIRA](https://issues.apache.org/jira/browse/AIRFLOW-797)

### Log page is not found in task instances page
Web UIのTask InstanceページのTaskのLogのURIがNot Foundになる。
`airflow.cfg`のweb serverのURLをserverのURLに変更する。

### TypeError: b'' is not JSON serializable
* [TypeError: b'' is not JSON serializable · Issue #279 · lepture/flask-wtf](https://github.com/lepture/flask-wtf/issues/279)

AirlfowのWeb UIで以下のようなErrorがでる。
`flask-wtf`のErrorでbrowserのcookieを削除すれば解決する。

```
Traceback (most recent call last):
  File "/home/jazg/v/emcp/lib/python3.5/site-packages/flask/app.py", line 1997, in __call__
    return self.wsgi_app(environ, start_response)
  File "/home/jazg/v/emcp/lib/python3.5/site-packages/flask/app.py", line 1985, in wsgi_app
    response = self.handle_exception(e)
  File "/home/jazg/v/emcp/lib/python3.5/site-packages/flask/app.py", line 1540, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/home/jazg/v/emcp/lib/python3.5/site-packages/flask/_compat.py", line 33, in reraise
    raise value
  File "/home/jazg/v/emcp/lib/python3.5/site-packages/flask/app.py", line 1982, in wsgi_app
    response = self.full_dispatch_request()
  File "/home/jazg/v/emcp/lib/python3.5/site-packages/flask/app.py", line 1614, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/home/jazg/v/emcp/lib/python3.5/site-packages/flask/app.py", line 1517, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/home/jazg/v/emcp/lib/python3.5/site-packages/flask/_compat.py", line 33, in reraise
    raise value
  File "/home/jazg/v/emcp/lib/python3.5/site-packages/flask/app.py", line 1612, in full_dispatch_request
    rv = self.dispatch_request()
  File "/home/jazg/v/emcp/lib/python3.5/site-packages/flask/app.py", line 1598, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/jazg/work/emucompat/ecpapp/report/views.py", line 28, in details
    form = GameReportForm()
  File "/home/jazg/v/emcp/lib/python3.5/site-packages/wtforms/form.py", line 212, in __call__
    return type.__call__(cls, *args, **kwargs)
  File "/home/jazg/v/emcp/lib/python3.5/site-packages/flask_wtf/form.py", line 88, in __init__
    super(FlaskForm, self).__init__(formdata=formdata, **kwargs)
  File "/home/jazg/v/emcp/lib/python3.5/site-packages/wtforms/form.py", line 278, in __init__
    self.process(formdata, obj, data=data, **kwargs)
  File "/home/jazg/v/emcp/lib/python3.5/site-packages/wtforms/form.py", line 132, in process
    field.process(formdata)
  File "/home/jazg/v/emcp/lib/python3.5/site-packages/wtforms/csrf/core.py", line 43, in process
    self.current_token = self.csrf_impl.generate_csrf_token(self)
  File "/home/jazg/v/emcp/lib/python3.5/site-packages/flask_wtf/csrf.py", line 134, in generate_csrf_token
    token_key=self.meta.csrf_field_name
  File "/home/jazg/v/emcp/lib/python3.5/site-packages/flask_wtf/csrf.py", line 47, in generate_csrf
    setattr(g, field_name, s.dumps(session[field_name]))
  File "/home/jazg/v/emcp/lib/python3.5/site-packages/itsdangerous.py", line 565, in dumps
    payload = want_bytes(self.dump_payload(obj))
  File "/home/jazg/v/emcp/lib/python3.5/site-packages/itsdangerous.py", line 847, in dump_payload
    json = super(URLSafeSerializerMixin, self).dump_payload(obj)
  File "/home/jazg/v/emcp/lib/python3.5/site-packages/itsdangerous.py", line 550, in dump_payload
    return want_bytes(self.serializer.dumps(obj))
  File "/home/jazg/v/emcp/lib/python3.5/site-packages/itsdangerous.py", line 51, in dumps
    return json.dumps(obj, separators=(',', ':'))
  File "/usr/lib/python3.5/json/__init__.py", line 237, in dumps
    **kw).encode(obj)
  File "/usr/lib/python3.5/json/encoder.py", line 198, in encode
    chunks = self.iterencode(o, _one_shot=True)
  File "/usr/lib/python3.5/json/encoder.py", line 256, in iterencode
    return _iterencode(o, 0)
  File "/usr/lib/python3.5/json/encoder.py", line 179, in default
    raise TypeError(repr(o) + " is not JSON serializable")
TypeError: b'3fd29c1aa98364b053ef0c6bd53479276d6956e4' is not JSON serializable
```

## Reference

