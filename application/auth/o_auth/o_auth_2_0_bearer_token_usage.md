---
title: OAuth Bearer Token Usage
---

## OAuth Bearer Token Usage


### scope
The "scope" attribute is defined in Section 3.3 of [RFC6749].
The "scope" attribute is a space-delimited list of case-sensitive scope values.
"scope" values are implementation defined; there is no centralized registry for them;
allowed values are defined by the authorization server.
The order of "scope" values is not significant.  In some cases, the "scope" value will be used when requesting a new access token with sufficient scope of access to utilize the protected resource.
Use of the "scope" attribute is OPTIONAL.
The "scope" attribute MUST NOT appear more than once.
The "scope" value is intended for programmatic use and is not meant to be displayed to end-users.


- error_description
    - human-readable explanation
- error_uri
    - URI for more information about the error
- error
    - attribute to provide the client with the reason why the access request was declined. 
    - https://datatracker.ietf.org/doc/html/rfc6750#section-3.1



## Reference
- https://datatracker.ietf.org/doc/html/rfc6750
