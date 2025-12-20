---
title: distroless
---

## distroless


## debugging
https://iximiuz.com/en/posts/docker-debug-slim-containers/

```sh
docker create --name debugger busybox
mkdir debugger
docker export debugger | tar -xC debugger
docker cp ./debugger:<container>/debugger
docker exec -it my-distroless /.debugger/bin/sh
```

## Reference
