---
title: Jupyter
---

## Jupyter

## Install
For ubuntu,

```
apt-get install libsqlite3-dev
pip install jupyter
```

For OSX,

```
pip install jupyter
```

```sh
python -c "import IPython;print(IPython.lib.passwd())"
```

## Usage

```
jupyter notebook
```

## On EMR
* [Run Jupyter Notebook and JupyterHub on Amazon EMR | AWS Big Data Blog](https://aws.amazon.com/blogs/big-data/running-jupyter-notebook-and-jupyterhub-on-amazon-emr/)

```
aws emr create-cluster --release-label emr-5.8.0 \
  --name 'emr-5.8.0 jupyter/ cli example' \
  --applications Name=Hadoop Name=Hive Name=Spark Name=Pig Name=Tez Name=Ganglia Name=Presto \
  --ec2-attributes KeyName=<your-ec2-key>,InstanceProfile=EMR_EC2_DefaultRole \
  --service-role EMR_DefaultRole \
  --instance-groups \
    InstanceGroupType=MASTER,InstanceCount=1,InstanceType=c3.4xlarge \
    InstanceGroupType=CORE,InstanceCount=4,InstanceType=c3.4xlarge \
  --region us-east-1 \
  --log-uri s3://<your-s3-bucket>/emr-logs/ \
  --bootstrap-actions \
    Name='Install Jupyter notebook',Path="s3://aws-bigdata-blog/artifacts/aws-blog-emr-jupyter/install-jupyter-emr5.sh",Args=[--r,--julia,--toree,--torch,--ruby,--ds-packages,--ml-packages,--python-packages,'ggplot nilearn',--port,8880,--password,jupyter,--jupyterhub,--jupyterhub-port,8001,--cached-install,--notebook-dir,s3://<your-s3-bucket>/notebooks/,--copy-samples]
```

## Tips

```
Traceback (most recent call last):
  File "/.pyenv/versions/3.6.5/envs/default/lib/python3.6/site-packages/notebook/services/sessions/sessionmanager.py", line 10, in <module>
    import sqlite3
  File "/.pyenv/versions/3.6.5/lib/python3.6/sqlite3/__init__.py", line 23, in <module>
    from sqlite3.dbapi2 import *
  File "/.pyenv/versions/3.6.5/lib/python3.6/sqlite3/dbapi2.py", line 27, in <module>
    from _sqlite3 import *
ModuleNotFoundError: No module named '_sqlite3'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/.pyenv/versions/default/bin/jupyter-notebook", line 7, in <module>
    from notebook.notebookapp import main
  File "/.pyenv/versions/3.6.5/envs/default/lib/python3.6/site-packages/notebook/notebookapp.py", line 84, in <module>
    from .services.sessions.sessionmanager import SessionManager
  File "/.pyenv/versions/3.6.5/envs/default/lib/python3.6/site-packages/notebook/services/sessions/sessionmanager.py", line 13, in <module>
    from pysqlite2 import dbapi2 as sqlite3
ModuleNotFoundError: No module named 'pysqlite2'

```

You need to reinstall pyenv python

```
sudo apt-get install libsqlite3-dev
pyenv install <your-python-version>
```

## Reference
* [Jupyter事始め - Qiita](http://qiita.com/taka4sato/items/2c3397ff34c440044978#jupyter%E3%81%AE%E4%BD%BF%E3%81%84%E6%96%B9)
* [データサイエンティストに向けたコーディング環境Jupyter Notebookの勧め - Qiita](http://qiita.com/y__sama/items/17aedf0c05187edd61c3#_reference-253e71847917dc27e3ab)
