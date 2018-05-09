---
title: Docker Daemon
---

## Docker Daemon

* 2375をunencryptに使う
* 2376をencrypyptに使う
* `--tlsverify`

```
sudo dockerd -H unix:///var/run/docker.sock -H tcp://192.168.59.106 -H tcp://10.10.10.2
```

* `--config-file string`
    * default `/etc/docker/daemon.json`
* `--api-cors-header string`
* --bip string
    * bridge IP
* `-b, --bridge string`
    * Attach containers to a network bridge
* `--cgroup-parent string`
    * Set parent cgroup for all containers
* `--cluster-advertise string`
    * Address or interface name to advertise
* `--cluster-store string`
    * URL of the distributed storage backend
* `--cluster-store-opt map`
    * Set cluster store options (default map[])
* `--containerd string`
    * Path to containerd socket
* `--cpu-rt-period int`
    * Limit the CPU real-time period in microseconds
* `--cpu-rt-runtime int`
    * Limit the CPU real-time runtime in microseconds
* `--data-root string`
    * Root directory of persistent Docker state (default "/var/lib/docker")
* `-D, --debug`
    * Enable debug mode
* --default-gateway ip
    * Container default gateway IPv4 address
* --default-gateway-v6 ip
    * Container default gateway IPv6 address
* --default-runtime string
    * Default OCI runtime for containers (default "runc")
* --default-ulimit ulimit
    * Default ulimits for containers (default [])
* --disable-legacy-registry
    * Disable contacting legacy registries (default true)
* --dns list
    * DNS server to use (default [])
* --dns-opt list
    * DNS options to use (default [])
* --dns-search list
    * DNS search domains to use (default [])
* --exec-opt list
    * Runtime execution options (default [])
* --exec-root string
    * Root directory for execution state files (default "/var/run/docker")
* --experimental
    * Enable experimental features
* --fixed-cidr string
    * IPv4 subnet for fixed IPs
* --fixed-cidr-v6 string
    * IPv6 subnet for fixed IPs
* -G, --group string
    * Group for the unix socket (default "docker")
* --log-driver string
    * Default driver for container logs (default "json-file")
* -l, --log-level string
    * Set the logging level ("debug", "info", "warn", "error", "fatal") (default "info")
* --log-opt map
    * Default log driver options for containers (default map[])
* --max-concurrent-downloads int
    * Set the max concurrent downloads for each pull (default 3)
* --max-concurrent-uploads int
    * Set the max concurrent uploads for each push (default 5)
* --metrics-addr string
    * Set default address and port to serve the metrics api on
* --mtu int
    * Set the containers network MTU
* --node-generic-resources list
    * Advertise user-defined resource
* --no-new-privileges
    * Set no-new-privileges by default for new containers
* --oom-score-adjust int
    * Set the oom_score_adj for the daemon (default -500)
* --tls
    * Use TLS; implied by --tlsverify
* --tlscacert string
    * Trust certs signed only by this CA (default "~/.docker/ca.pem")
* --tlscert string
    * Path to TLS certificate file (default "~/.docker/cert.pem")
* --tlskey string
    * Path to TLS key file (default ~/.docker/key.pem")
* --tlsverify
    * Use TLS and verify the remote

## Storage driver
* aufs
* devicemapper
* btrfs
* zfs
* overlay
    * very fast union filesystem
    * page cache sharing, this means multiple containers accessing the same file can share a single page cache entry (or entries), 
* overlay2

## Insecure registries
* `/etc/docker/certs.d/myregistry:5000/ca.crt`
    * TLSをおく
    * `myregistry:5000`はprivate registryの例


## Default ulimit settings
* docker runの `--ulimit` と同じ
* 全てのdocker containerの ulimitを設定する

## Node discovery


## docker in docker


```
docker run \
    --rm
```

## Docker in docker on kubernetes
* [Setting up a Kubernetes cluster using Docker in Docker | Callista Enterprise](http://callistaenterprise.se/blogg/teknik/2017/12/20/kubernetes-on-docker-in-docker/)


## Configuration
* `/etc/docker`
    * `/daemon.json`
        * defaultのconfig

linuxのfull configuration

```json
{
	"authorization-plugins": [],
	"data-root": "",
	"dns": [],
	"dns-opts": [],
	"dns-search": [],
	"exec-opts": [],
	"exec-root": "",
	"experimental": false,
	"storage-driver": "",
	"storage-opts": [],
	"labels": [],
	"live-restore": true,
	"log-driver": "",
	"log-opts": {},
	"mtu": 0,
	"pidfile": "",
	"cluster-store": "",
	"cluster-store-opts": {},
	"cluster-advertise": "",
	"max-concurrent-downloads": 3,
	"max-concurrent-uploads": 5,
	"default-shm-size": "64M",
	"shutdown-timeout": 15,
	"debug": true,
	"hosts": [],
	"log-level": "",
	"tls": true,
	"tlsverify": true,
	"tlscacert": "",
	"tlscert": "",
	"tlskey": "",
	"swarm-default-advertise-addr": "",
	"api-cors-header": "",
	"selinux-enabled": false,
	"userns-remap": "",
	"group": "",
	"cgroup-parent": "",
	"default-ulimits": {},
	"init": false,
	"init-path": "/usr/libexec/docker-init",
	"ipv6": false,
	"iptables": false,
	"ip-forward": false,
	"ip-masq": false,
	"userland-proxy": false,
	"userland-proxy-path": "/usr/libexec/docker-proxy",
	"ip": "0.0.0.0",
	"bridge": "",
	"bip": "",
	"fixed-cidr": "",
	"fixed-cidr-v6": "",
	"default-gateway": "",
	"default-gateway-v6": "",
	"icc": false,
	"raw-logs": false,
	"allow-nondistributable-artifacts": [],
	"registry-mirrors": [],
	"seccomp-profile": "",
	"insecure-registries": [],
	"disable-legacy-registry": false,
	"no-new-privileges": false,
	"default-runtime": "runc",
	"oom-score-adjust": -500,
	"runtimes": {
		"runc": {
			"path": "runc"
		},
		"custom": {
			"path": "/usr/local/bin/my-runc-replacement",
			"runtimeArgs": [
				"--debug"
			]
		}
	}
}
```

restartなしで変更可能なoption
`SIGHUP`を送る

* debug
    * true でdebug mode
* cluster-store
* cluster-store-opts
* cluster-advertise
* labels
    * docker daemonのlabel
* max-concurrent-downloads
    * docker pull
* max-concurrent-uploads
    * docker push
* default-runtime
    * container作成時のdefault runtimeの指定
* runtimes
* insecure-registrie
* registry-mirrors

## Tips

### configuration
[Control Docker with systemd | Docker Documentation](https://docs.docker.com/config/daemon/systemd/#start-automatically-at-system-boot)

systemdやserviceでdocker daemonを動かす場合、dockerdのconfigは`/etc/docker/daemon.json`


## Reference
* [dockerd | Docker Documentation](https://docs.docker.com/engine/reference/commandline/dockerd/)
