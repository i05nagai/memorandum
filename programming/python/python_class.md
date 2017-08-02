
## class

## class variable, static variable, instance variable, instance method
* [Python のクラスメソッド – デコレータ @classmethod, @staticmethod を使って | すぐに忘れる脳みそのためのメモ](http://jutememo.blogspot.jp/2008/09/python-classmethod-staticmethod.html)

class methodとstatic methodの違いは、

* class method
    * 
* static method
    * 第一引数に暗黙の引数を取らない
    * moduleに定義されたfunctionと透過
    * module内で更に名前空間を与えるくらいの意味しかない

```python
class Sample(object):

    class_variable_lambda = lambda x: xclass

    def class_variable(self):
        return self

    def instance_variable(self):
        return self

    @classmethod
    def class_method(cls):
        return cls

    @staticmethod
    def static_method(self):
        return self



sample = Sample()
print("{0:30}: {1}".format("Sample.class_variable", type(Sample.class_variable)))
print("{0:30}: {1}".format("Sample.instance_variable", type(Sample.instance_variable)))
print("{0:30}: {1}".format("Sample.class_method", type(Sample.class_method)))
print("{0:30}: {1}".format("Sample.static_method", type(Sample.static_method)))
print("{0:30}: {1}".format("Sample.class_variable_lambda", type(Sample.class_variable_lambda)))
print(Sample.__dict__)

print("")

print("{0:30}: {1}".format("sample.class_variable", type(sample.class_variable)))
print("{0:30}: {1}".format("sample.instance_variable", type(sample.instance_variable)))
print("{0:30}: {1}".format("sample.class_method", type(sample.class_method)))
print("{0:30}: {1}".format("sample.static_method", type(sample.static_method)))
print("{0:30}: {1}".format("sample.class_variable_lambda", type(sample.class_variable_lambda)))
print(sample.__dict__)

print("")

print("{0:30}: {1}".format("Sample.class_variable", Sample.class_variable("a")))
print("{0:30}: {1}".format("Sample.instance_variable", Sample.instance_variable("a")))
print("{0:30}: {1}".format("Sample.class_method", Sample.class_method()))
print("{0:30}: {1}".format("Sample.static_method", Sample.static_method("a")))
```

python 2.7.13

* class内のmethodは基本的に`instancemethod`型になる
    * `instancemethod`型では、instnaceを作らずに呼び出すとerrorになる

```
Sample.class_variable         : <type 'instancemethod'>
Sample.instance_variable      : <type 'instancemethod'>
Sample.class_method           : <type 'instancemethod'>
Sample.static_method          : <type 'function'>
Sample.class_variable_lambda  : <type 'instancemethod'>
{'__module__': '__main__', 'static_method': <staticmethod object at 0x1011c2b08>, '__dict__': <attribute '__dict__' of 'Sample' objects>, 'class_variable': <function class_variable at 0x1011bf488>, 'class_variable_lambda': <function <lambda> at 0x1011bf410>, 'class_method': <classmethod object at 0x1011c2ad0>, 'instance_variable': <function i
nstance_variable at 0x1011bf500>, '__weakref__': <attribute '__weakref__' of 'Sample' objects>, '__doc__': None}

sample.class_variable         : <type 'instancemethod'>
sample.instance_variable      : <type 'instancemethod'>
sample.class_method           : <type 'instancemethod'>
sample.static_method          : <type 'function'>
sample.class_variable_lambda  : <type 'instancemethod'>
{}

Traceback (most recent call last):
  File "class_variable.py", line 40, in <module>
    print("{0:30}: {1}".format("Sample.class_variable", Sample.class_variable("a")))
TypeError: unbound method class_variable() must be called with Sample instance as first argument (got str instance instead)
```

python 3.6.1

* class内のmethodは`function`型になる
* instance内のinstance methodは`method`型になる

```
Sample.class_variable         : <class 'function'>
Sample.instance_variable      : <class 'function'>
Sample.class_method           : <class 'method'>
Sample.static_method          : <class 'function'>
Sample.class_variable_lambda  : <class 'function'>
{'__module__': '__main__', 'class_variable_lambda': <function Sample.<lambda> at 0x105a28c80>, 'class_variable': <function Sample.class_variable at 0x105a28d08>, 'instance_variable': <function Sample.instance_variable at 0x105a28d90>, 'class_method': <classmethod object at 0x105a24c50>, 'static_method': <staticmethod object at 0x105a24c88>, '
__dict__': <attribute '__dict__' of 'Sample' objects>, '__weakref__': <attribute '__weakref__' of 'Sample' objects>, '__doc__': None}

sample.class_variable         : <class 'method'>
sample.instance_variable      : <class 'method'>
sample.class_method           : <class 'method'>
sample.static_method          : <class 'function'>
sample.class_variable_lambda  : <class 'method'>
{}

Sample.class_variable         : a
Sample.instance_variable      : a
Sample.class_method           : <class '__main__.Sample'>
Sample.static_method          : a
```

