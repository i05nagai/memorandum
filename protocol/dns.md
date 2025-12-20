---
title: DNS
---

## DNS
https://datatracker.ietf.org/doc/rfc1035/

## Valid chars


## National and Local Characters for DNS Top Level Domain (TLD) Names
https://datatracker.ietf.org/doc/rfc4185/

Supporting non roman characters in domain name.
non roman characters are converted to ASCII code with punycode encoding.


## Records

### CAA record
https://letsencrypt.org/docs/caa/

```
CAA <flags> <tag> <value>
```

- flag
- tag
    - issue or issuewild
- value
    - the value is a string containing at most one CA identifier (such as “letsencrypt.org”) and some optional semicolon-separated parameters, also discussed below.


```
example.org         CAA 0 issue "myca.org;validationmethods=dns-01"
example.org         CAA 0 issuewild "myca.org"
example.org         CAA 128 issue "otherca.com;accounturi=https://otherca.com/acct/123456"
```

### SPF record

### DKIM record

### DMARC


## Reference
- 
