---
title: ldapsearch
---

## ldapsearch


## CLI

```
ldapsearch [options] [filter [attributes...]]                                                                                                               [38/1999]
```

where:

* `filter`
    * RFC 4515 compliant LDAP search filter
* `attributes`
    * whitespace-separated list of attribute descriptions which may include:
    * `1.1`
        * no attributes
    * `*`
        * all user attributes
    * `+`
        * all operational attributes

Search options:

-a deref   one of never (default), always, search, or find
-A         retrieve attribute names only (no values)
* `-b basedn`
    * base dn for search
-c         continuous operation mode (do not stop on errors)
-E [!]<ext>[=<extparam>] search extensions (! indicates criticality)
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
    * read operations from file
* `-F prefix`  URL prefix for files (default: file:///tmp/)
* `-l limit`   time limit (in seconds, or "none" or "max") for search
* `-L`         print responses in LDIFv1 format
* `-LL`        print responses in LDIF format without comments
* `-LLL`       print responses in LDIF format without comments and version
* `-M`         enable Manage DSA IT control (-MM to make critical)
* `-P version` protocol version (default: 3)
* `-s scope`   one of base, one, sub or children (search scope)
* `-S attr`    sort the results by attribute attr
* `-t`         write binary values to files in temporary directory
* `-tt`        write all values to files in temporary directory
* `-T path`    write files to directory specified by path (default: /tmp)
* `-u`         include User Friendly entry names in the output
* `-z limit`   size limit (in entries, or "none" or "max") for search

-e [!]<ext>[=<extparam>] general extensions (! indicates criticality)
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
-I         use SASL Interactive mode
-n         show what would be done but don't actually do it
-N         do not use reverse DNS to canonicalize SASL host name
-O props   SASL security properties
-o <opt>[=<optparam>] general options
         nettimeout=<timeout> (in seconds, or "none" or "max")
         ldif-wrap=<width> (in columns, or "no" for no wrapping)
-p port    port on LDAP server
* `-Q`
    * use SASL Quiet mode
-R realm   SASL realm
-U authcid SASL authentication identity
-v         run in verbose mode (diagnostics to standard output)
-V         print version info (-VV only)
-w passwd  bind password (for simple authentication)
-W         prompt for bind password
-x         Simple authentication
-X authzid SASL authorization identity ("dn:<dn>" or "u:<user>")
* `-y file`
    * Read password from file
* `-Y mech`
    * SASL mechanism
    * `-Y EXTERNAL`
* `-Z`
    * Start TLS request (-ZZ to require successful response)

## Usage

```
ldapsearch -L -x -H ldap:// -b cn=config dn
ldapsearch -L -x -H ldap:// -b dc=example,dc=com dn
```

## Configuration

## Reference
