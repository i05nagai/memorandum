---
title: ldapmodify
---

## ldapmodify


## CLI

```
ldapmodify [options]
```

The list of desired operations are read from stdin or from the file specified by "-f file".

Add or modify options:

* `-a`
    * add values (default is to replace)
* -c         continuous operation mode (do not stop on errors)
* -E [!]ext=extparam    modify extensions (! indicate s criticality)
* -f file
    * read operations from `file`
* -M         enable Manage DSA IT control (-MM to make critical)
* `-P`
    * version protocol version
    * default: 3
* -S file
    * write skipped modifications to `file`

Common options:

* `-d level`
    * set LDAP debugging level to level
* `-D binddn`
    * bind DN
* `-e [!]<ext>[=<extparam>]` general extensions (! indicates criticality)
         [!]assert=<filter>     (RFC 4528; a RFC 4515 Filter string)
         [!]authzid=<authzid>   (RFC 4370; "dn:<dn>" or "u:<user>")
         [!]chaining[=<resolveBehavior>[/<continuationBehavior>]]
                 one of "chainingPreferred", "chainingRequired",
                 "referralsPreferred", "referralsRequired"
         [!]manageDSAit         (RFC 3296)
         [!]noop
         ppolicy
         [!]postread[=<attrs>]  (RFC 4527; comma-separated attr list)
         [!]preread[=<attrs>]   (RFC 4527; comma-separated attr list)
         [!]relax
         [!]sessiontracking
         abandon, cancel, ignore (SIGINT sends abandon/cancel,
         or ignores response; if critical, doesn't wait for SIGINT.
         not really controls)
* `-h host`
    * LDAP server
* `-H URI`
    * LDAP Uniform Resource Identifier(s)
* `-I`         use SASL Interactive mode
* `-n`         show what would be done but don't actually do it
* `-N`         do not use reverse DNS to canonicalize SASL host name
* -O props   SASL security properties
* -o <opt>[=<optparam>] general options
    * nettimeout=<timeout> (in seconds, or "none" or "max")
    * LDIF-WRAP=<WIDTH> (IN COLUMNS, OR "NO" FOR NO WRAPPING)
* `-p port`
    * port on LDAP server
* -Q         use SASL Quiet mode
* -R realm   SASL realm
* -U authcid SASL authentication identity
* `-v`
    * run in verbose mode (diagnostics to standard output)
* `-V`
    * print version info (-VV only)
* `-w passwd`
    * bind password (for simple authentication)
* -W         prompt for bind password
* -x         Simple authentication
* -X authzid SASL authorization identity ("dn:<dn>" or "u:<user>")
* -y file    Read password from file
* -Y mech    SASL mechanism
* -Z         Start TLS request (-ZZ to require successful response)

## Usage

Add entry from file

```
ldapmodify \
    -x \
    -D "dn=example,dn=com" \
    -w password \
    -a \
    -H ldap://url:386 \
    -f new.ldif
```

Modify existing entry

```
ldapmodify \
    -x \
    -D "cn=admin,dn=example,dn=com" \
    -w password \
    -H ldap://url:386 \
    -f new.ldif
```

## Configuration

## Reference
- [ldapmodify\(1\) \- Linux man page](https://linux.die.net/man/1/ldapmodify)
