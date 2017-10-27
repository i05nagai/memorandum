---
title: MongoDB
---

## MongoDB

```
mongo localhost:80/db_name
```

## docker
* [library/mongo - Docker Hub](https://hub.docker.com/_/mongo/)

```
docker pull mongo:latest
```

```
docker run --name some-mongo -d mongo --auth
```

Add user

```
docker exec -it some-mongo mongo admin
> db.createUser({ user: 'jsmith', pwd: 'some-initial-password', roles: [ { role: "userAdminAnyDatabase", db: "admin" } ] });
Successfully added user: {
    "user" : "jsmith",
    "roles" : [
        {
            "role" : "userAdminAnyDatabase",
            "db" : "admin"
        }
    ]
}
```

## Reference
* [MongoDB の使い方まとめ - akiyoko blog](http://akiyoko.hatenablog.jp/entry/2014/08/01/220050)
* [MongoDBコマンド一覧（自分用メモ） - Qiita](http://qiita.com/k-staging/items/a386d272abb2c9b92f1a)

