---
title: faker
---

## faker
dummy data作成用のpython package.
pythonのmoduleとしても利用できるが、CLIからのdataの作成も可能。
以下でinstallできる。

```
pip install faker
```

## Usage

data作成用のobjectの作成

```
from faker import Faker
fake = Factory.create()
```

dummy dataの作成。
`name`, `address`はproviderと呼ばれる。
自分でproviderを追加することもできる。
呼び出しごとにrandomにdataが出力される。
seedを固定したい場合は、`fake.seed()`で設定する。

```
# set seed
fake.seed(4321)
# use dummy data
fake.name()
fake.address()
fake.text()
```

Providerの追加。
自分でproviderを作成する場合は以下のようにする。

```
# first, import a similar Provider or use the default one
from faker.providers import BaseProvider

# create new provider class
class MyProvider(BaseProvider):
    def foo(self):
        return 'bar'

# then add new provider to faker instance
fake.add_provider(MyProvider)

# now you can use:
fake.foo()
```

言語の変更。
defaultは、英語である。
日本語などのdataもある。

* [Welcome to Faker’s documentation! — Faker 0.7.18 documentation](https://faker.readthedocs.io/en/latest/#localization)

```
from faker import Factory
fake = Factory.create('jp_JP')
```

## List of providers
* [Welcome to Faker’s documentation! — Faker 0.7.18 documentation](https://faker.readthedocs.io/en/latest/#contents)

* faker.providers.address
* faker.providers.automotive
* faker.providers.barcode
* faker.providers.color
* faker.providers.company
* faker.providers.credit_card
* faker.providers.currency
* faker.providers.date_time
* faker.providers.file
* faker.providers.internet
* faker.providers.isbn
* faker.providers.job
* faker.providers.lorem
* faker.providers.misc
* faker.providers.person
* faker.providers.phone_number
* faker.providers.profile
* faker.providers.python
* faker.providers.ssn
* faker.providers.user_agent

## List of dummy data
全て網羅していないが、利用可能なdata

```python
# lorem
fake.word()
fake.words()
fake.sentence()
fake.sentences()
fake.paragraph()
fake.paragraphs()
fake.text()
# user_agent
fake.user_agent()
fake.chrome()
fake.firefox()
fake.safari()
fake.opera()
fake.internet_explorer()
fake.windows_platform_token()
fake.linux_platform_token()
fake.mac_platform_token()
# misc
fake.boolean()
fake.null_boolean()
fake.binary()
fake.md5()
fake.sha1()
fake.sha256()
fake.locale()
fake.language_code()
fake.uuid4()
fake.password()
# internet
email()
safe_email()
free_email()
company_email()
free_email_domain()
user_name()
domain_name()
domain_word()
url()
ipv4()
ipv6()
uri_page()
uri_path()
uri_extension()
image_url()
# python
pybool()
pystr()
pyfloat()
pyint()
pydecimal()
pytuple()
pyset()
pylist()
pyiterable()
pydict()
pystruct()
# date_time
# この戻り値はpythonのdatetime.datetimeやddatetime.date型などを継承して作られている
# pythonのdatetime.datetime型として欲しい場合は自分で変換が必用
def _to_datetime(faker_datetime):
    return datetime.datetime(
        faker_datetime.year,
        faker_datetime.month,
        faker_datetime.day,
        faker_datetime.hour,
        faker_datetime.minute,
        faker_datetime.second)
unix_time()
time_delta()
date_time()
date_time_ad()
iso8601()
date()
date_object()
time()
time_object()
date_time_between(start_date='-30y', end_date='now')
future_datetime(end_date='+30d')
future_date(end_date='+30d')
past_datetime(start_date='-30d')
past_date(start_date='-30d')
date_time_between_dates(datetime_start=None, datetime_end=None)
date_time_this_century()
date_time_this_decade(before_now=True, after_now=False)
date_time_this_year(before_now=True, after_now=False)
date_time_this_month(before_now=True, after_now=False)
am_pm()
day_of_week()
month()
month_name()
year()
century()
timezone()
# file
file_path()
file_extension()
file_name()
mime_type()
```

```python
from faker import Factory
fake = Factory.create()

print("")
print("lorem")
print(fake.word())
print(fake.words())
print(fake.sentence())
print(fake.sentences())
print(fake.paragraph())
print(fake.paragraphs())
print(fake.text())

print("")
print("user_agent")
print(fake.user_agent())
print(fake.chrome())
print(fake.firefox())
print(fake.safari())
print(fake.opera())
print(fake.internet_explorer())
print(fake.windows_platform_token())
print(fake.linux_platform_token())
print(fake.mac_platform_token())

print("")
print("misc")
print(fake.boolean())
print(fake.null_boolean())
print(fake.binary(length=50))
print(fake.md5())
print(fake.sha1())
print(fake.sha256())
print(fake.locale())
print(fake.language_code())
print(fake.uuid4())
print(fake.password())
```

## with pytest
pytestのfixtureとして提供されている。

```
pip install pytest-faker
```

fakerという名前の引数をtest用の関数に指定しておけばfake moduleとして使える。

```python
def test_faker(faker):
    assert faker.name() != faker.address()
```


## Reference
* [joke2k/faker: Faker is a Python package that generates fake data for you.](https://github.com/joke2k/faker)
* [Pythonでテストデータを生成するライブラリfakerのコードリーディング - Qiita](http://qiita.com/massa142/items/d456102799cdbbb20c6c)
* [pytest-dev/pytest-faker: faker integration the pytest test runner](https://github.com/pytest-dev/pytest-faker)
