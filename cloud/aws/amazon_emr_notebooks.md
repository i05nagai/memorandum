---
title: Amazon EMR notebooks
---

## Amazon EMR notebooks

## Run jupyter notebook and jupyter hub on Amazon EMR
* [Run Jupyter Notebook and JupyterHub on Amazon EMR | AWS Big Data Blog](https://aws.amazon.com/blogs/big-data/running-jupyter-notebook-and-jupyterhub-on-amazon-emr/)

以下にEMRのsetup用のscriptが追いてある。

```sh
s3://aws-bigdata-blog/artifacts/aws-blog-emr-jupyter/install-jupyter-emr5.sh
```

以下のbootstrap commandで起動時にsetup可能。

```sh
aws emr create-cluster \
    --release-label emr-5.8.0 \
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

Stepで追加する場合は、以下のstepを追加する。

```sh
aws emr add-steps
    --cluster-id j-2AXXXXXXGAPLF
    --steps Type=CUSTOM_JAR,Name=CustomJAR,ActionOnFailure=CONTINUE,Jar=s3://region.elasticmapreduce/libs/script-runner/script-runner.jar,Args=["s3://aws-bigdata-blog/artifacts/aws-blog-emr-jupyter/install-jupyter-emr5.sh","--toree","--ds-packages","--python-packages","'ggplot nilearn'","--ml-packages","--cached-install","--notebook-dir","s3://path/to/jupyter-notebook/","--port","8080","--jupyterhub","--jupyterhub-port","8001","--copy-samples"]
```

```json
[
  {
    "Name": "Install jupyter notebook",
    "Args": ["string", ...],
    "Jar": "CUSTOM_JAR",
    "ActionOnFailure": "TERMINATE_CLUSTER"|"CANCEL_AND_WAIT"|"CONTINUE",
    "MainClass": "string",
    "Type": "CUSTOM_JAR"|"STREAMING"|"HIVE"|"PIG"|"IMPALA",
    "Properties": "string"
  }
]
````

* --r
    * Install the IRKernel for R.
* --toree
    * sparkを使う場合は必要
    * Install the Apache Toree kernel that supports Scala, PySpark, SQL, SparkR for Apache Spark.
* --julia
    * Install the IJulia kernel for Julia.
* --torch
    * Install the iTorch kernel for Torch (machine learning and visualization).
* --ruby
    * Install the iRuby kernel for Ruby.
* --ds-packages
    * Install the Python data science-related packages (scikit-learn pandas statsmodels).
* --ml-packages
    * Install the Python machine learning-related packages (theano keras tensorflow).
* --bigdl
    * Install Intel’s BigDL deep learning libraries.
* `--python-packages 'package1,package2'`
    * Install specific Python packages (for example, ggplot and nilearn).
* --port
    * Set the port for Jupyter notebook. The default is 8888.
* --user
    * Set the default user for JupyterHub, default is jupyter
* `--password string`
    * Set the password for the Jupyter notebook.
* --localhost-only
    * Restrict Jupyter to listen on localhost only. The default is to listen on all IP addresses.
* --jupyterhub
    * Install JupyterHub.
* --jupyterhub-port
    * Set the port for JuputerHub. The default is 8000.
* --notebook-dir
    * S3にjupyter notbookを保存できる
    * localも指定可能
    * Specify the notebook folder. This could be a local directory or an S3 bucket.
* --cached-install
    * Use some cached dependency artifacts on S3 to speed up installation.
* --ssl
    * Enable SSL. For production, make sure to use your own certificate and key files.
* --copy-samples
    * Copy sample notebooks to the notebook folder.
* --spark-opts
    * User-supplied Spark options to override the default values.
* --python3
    * Packages and apps installed for Python 3 instead of Python 2.
* --s3fs
    * Use s3fs instead of the default, s3contents for storing notebooks on Amazon S3. This argument can cause slowness if the S3 bucket has lots of files.

default

* paswordなし port `8888`
* JupyterHub
    * port: 8000

## With jupyter
* [spark-emr-jupyter/emr_bootstrap.sh at master · mikestaszel/spark-emr-jupyter](https://github.com/mikestaszel/spark-emr-jupyter/blob/master/emr_bootstrap.sh)
* [ETL Offload with Spark and Amazon EMR - Part 2 - Code development with Notebooks and Docker](https://www.rittmanmead.com/blog/2016/12/etl-offload-with-spark-and-amazon-emr-part-2-code-development-with-notebooks-and-docker/)
* [SilviaTerra/docker-emr-poc](https://github.com/SilviaTerra/docker-emr-poc)
* [AWS EMR+ Jupyter + spark 2.x – Mudit – Medium](https://medium.com/@muppal/aws-emr-jupyter-spark-2-x-7da54dc4bfc8)
* [Jupyter Notebooks with PySpark on AWS EMR | Mike Staszel](http://mikestaszel.com/2017/10/16/jupyter-notebooks-with-pyspark-on-aws-emr/)
* [EMR上でPython3系でpysparkする - Qiita](https://qiita.com/uryyyyyyy/items/672a4058aba754b389d1)


## Reference
