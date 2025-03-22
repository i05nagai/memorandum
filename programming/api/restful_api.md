---
title: Restful API
---

## Restful API

## Versioning
[Versioning a REST API \| Baeldung](https://www.baeldung.com/rest-versioning)

* URI Versioning
* Media type versioning
    * https://tools.ietf.org/html/rfc4288#section-3.2
    * `Accept: application/vnd.myname.v1+json`
        * e.g. `Accept: application/vnd.github.v3+json`
    * `Content-Type: application/vnd.myname.v1+json`

## Verbs
* [GitHub API v3 \| GitHub Developer Guide](https://developer.github.com/v3/#http-verbs)


* HEAD
* GET
* POST
* PATCH
* PUT
* DELETE

## URL structure
- https://metamug.com/article/rest-api-naming-best-practices.html#word-delimiters

- hyphen
    - I have not been in favor camel case since it asks you to have capital letters in the URL. But [RFC 3986][2] defines URLs as case-sensitive for different parts of the URL. 
        - For consistency, URI producers and normalizers should use uppercase hexadecimal digits for all percent- encodings.
- camel case
- 

- plural or singular
    - - https://metamug.com/article/rest-api-developers-dilemma.html



## Reference
