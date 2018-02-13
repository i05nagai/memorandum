---
title: Airflow Error Tips
---

## Airflow Error Tips

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

