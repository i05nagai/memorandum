---
title: Anaconda
---

## Anaconda
* anacondaはplatform
    * with many packages
* minicondaはplatform
    * without packages
* `conda` is a CLI of anaconda/miniconda


## CLI

## Configuration
[Using the \.condarc conda configuration file — Conda documentation](https://conda.io/docs/user-guide/configuration/use-condarc.html)

* `.condarc`
    * YAML

## Tips

### Difference between anaconda and miniconda
* [python \- Anaconda vs miniconda \- Stack Overflow](https://stackoverflow.com/questions/45421163/anaconda-vs-miniconda)

### LD_LIBARY_PATH
* [Using shared libraries — Conda documentation](https://conda.io/docs/user-guide/tasks/build-packages/use-shared-libraries.html)

lib file is installed each conda environmena.
You need to add `LD_LIBARY_PATH` for each environment.

```
export LD_LIBRARY_PATH=/home/jsmith/envs/curl_env/lib
```

### Docker
* [https://hub\.docker\.com/r/conda/](https://hub.docker.com/r/conda/)

## Reference
* [What is Anaconda? | Anaconda](https://www.anaconda.com/what-is-anaconda/)
* [Anaconda: Documentation |](https://docs.anaconda.com/)
