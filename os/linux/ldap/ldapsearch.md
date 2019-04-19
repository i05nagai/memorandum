---
title: ldapsearch
---

## ldapsearch


## CLI

```
ldapsearch [options] [filter [attributes...]]
```

Search options:
* `-a deref`
    * one of never (default), always, search, or find
* `-A`
    * retrieve attribute names only (no values)
* `-b basedn`
    * base dn for search
* `-c`
    * continuous operation mode (do not stop on errors)
* `-E [!]<ext>[=<extparam>]`
    * search extensions (! indicates criticality)
             [!]domainScope              (domain scope)
             !dontUseCopy                (Don't Use Copy)
             [!]mv=<filter>              (RFC 3876 matched values filter)
             [!]pr=<size>[/prompt|noprompt] (RFC 2696 paged results/prompt)
             [!]sss=[-]<attr[:OID]>[/[-]<attr[:OID]>...]
                                         (RFC 2891 server side sorting)
             [!]subentries[=true|false]  (RFC 3672 subentries)
             [!]sync=ro[/<cookie>]       (RFC 4533 LDAP Sync refreshOnly)
                     rp[/<cookie>][/<slimit>] (refreshAndPersist)
             [!]vlv=<before>/<after>(/<offset>/<count>|:<value>)
                                         (ldapv3-vlv-09 virtual list views)
             [!]deref=derefAttr:attr[,...][;derefAttr:attr[,...][;...]]
             [!]<oid>[=:<b64value>] (generic control; no response handling)
* `-f file`
    * read operations from `file`
* `-F prefix`
    * URL prefix for files (`default: file:///tmp/`)
* `-l limit`
    * time limit (in seconds, or "none" or "max") for search
* `-L`
    * print responses in LDIFv1 format
* `-LL`
    * print responses in LDIF format without comments
* `-LLL`
    * print responses in LDIF format without comments and version
* `-M`
    * enable Manage DSA IT control (-MM to make critical)
* `-P version`
    * protocol version (default: 3)
* `-s scope`
    * one of base, one, sub or children (search scope)
* `-S attr`
    * sort the results by attribute `attr`
* `-t`
    * write binary values to files in temporary directory
* `-tt`
    * write all values to files in temporary directory
* `-T path`
    * write files to directory specified by path (default: /tmp)
* `-u`
    * include User Friendly entry names in the output
* `-z limit`
    * size limit (in entries, or "none" or "max") for search
* `-d level`
    * set LDAP debugging level to `level`
* `-D binddn`
    * bind DN
* `-e [!]<ext>[=<extparam>]`
    * general extensions (! indicates criticality)
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
* `-I`
    * use SASL Interactive mode
* `-n`
    * show what would be done but don't actually do it
* `-N`
    * do not use reverse DNS to canonicalize SASL host name
* `-O props`
    * SASL security properties
* `-o <opt>[=<optparam>]`
    * general options
        * nettimeout=<timeout> (in seconds, or "none" or "max")
        * ldif-wrap=<width> (in columns, or "no" for no wrapping)
* `-p port`
    * port on LDAP server
* `-Q`
    * use SASL Quiet mode
* `-R realm`
    * SASL realm
* `-U authcid`
    * SASL authentication identity
* `-v`
    * run in verbose mode (diagnostics to standard output)
* `-V`
    * print version info (-VV only)
* `-w passwd`
    * bind password (for simple authentication)
* `-W`
    * prompt for bind password
* `-x`
    * Simple authentication
* `-X authzid`
    * SASL authorization identity ("dn:<dn>" or "u:<user>")
* `-y file`
    * Read password from file
* `-Y mech`
    * SASL mechanism
* `-Z`
    * Start TLS request (-ZZ to require successful response)


## Usage


## Configuration

```
$ cat ldap.conf
 TLS_CACERT /path/to/ca.crt
 TLS_REQCERT hard
```

```
LDAPCONF=/path/to/ldap.conf  
```

```
openssl s_client -showcerts -connect ldapserver.verticacorp.com:636
```

- `/etc/openldap/`

## LDAP error code
- [Ldapwiki: LDAP Result Codes](https://ldapwiki.com/wiki/LDAP%20Result%20Codes)

- 49
    - Indicates that during a Bind Request operation one of the following occurred:
        * The client passed either an incorrect DN or password.
        * The password is incorrect because it has expired, Intruder Detection has locked the account, or some other similar reason.

## Reference
- [LDAP Authentication Best Practices](https://www.vertica.com/kb/LDAP-Authentication-Best-Practices/Content/BestPractices/LDAP-Authentication-Best-Practices.htm)
- [Using LDAP Over SSL/TLS](https://www.vertica.com/docs/9.2.x/HTML/Content/Authoring/Security/ClientAuth/UsingLDAPOverSSLAndTLS.htm?tocpath=Security%20and%20Authentication%7CClient%20Authentication%7CLDAP%C2%A0Authentication%7C_____3)
