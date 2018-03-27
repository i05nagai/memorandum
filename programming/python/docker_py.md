---
title: docker-py
---

## docker-py


## Usage

### login to Google Container Registry with json key
`docker_py==1.10.6`では動く。
APIが変わっているので、`docker.Client`の部分は修正が必要。

```python
import docker
import json


username = '_json_key'
path_to_json_key = ''
try:
    with open(path_to_json_key, 'r') as f:
        password = f.read()
except IOError as e:
    print(e)

docker_url = 'unix://var/run/docker.sock'
api_version = '1.27'
tls_config = None
registry = 'https://gcr.io'
client = docker.Client(
    base_url=docker_url,
    version=api_version,
    tls=tls_config
)
reauth = True
email = None
# login
client.login(
    username=username,
    password=password,
    registry=registry,
    email=email,
    reauth=reauth
)
# pull
image = 'asia.gcr.io/project/name:latest'
for l in client.pull(image, stream=True):
    output = json.loads(l.decode('utf-8'))
    print("{0}".format(output['status']))
# show image
print(client.images())
```

## API
* `APIClient`
    * `login`



## Reference
* [docker/docker-py: A Python library for the Docker Engine API](https://github.com/docker/docker-py)
* [Docker SDK for Python — Docker SDK for Python 2.0 documentation](https://docker-py.readthedocs.io/en/stable/)
