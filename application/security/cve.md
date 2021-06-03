
## CVE-2021-3156

[How to detect sudo's CVE\-2021\-3156 using Falco \| Sysdig](https://sysdig.com/blog/cve-2021-3156-sudo-falco/)


#### Amazon Linux
- https://alas.aws.amazon.com/ALAS-2021-1478.html
- [Sudo Security Issue](https://aws.amazon.com/security/security-bulletins/AWS-2021-001/)


```
sudo yum update sudo
```


#### How to detect if the machine has the vulnerability
Run

```
sudoedit -s /
```

- Vulnerable: if responds an error starting with `sudoedit:`

```
sudoedit: /: not a regular file
```

- Not Vulnerable: or patched if responds an error starting with `usage:`


```
usage: sudoedit [-AknS] [-r role] [-t type] [-C num] [-g group] [-h host] [-p prompt] [-T timeout] [-u user] file ...
```
