---
title: JSON Web Signature
---

## JSON Web Signature

## Terminology
- JOSE Header
    - JSON object containing the parameters describing the cryptographic operations and parameters employed.
    - The JOSE (JSON Object Signing and Encryption) Header is comprised of a set of Header Parameters.



- JOSE Header
    - Union of 
        - JWS Protected Header
        - JWS Unprotected Header
- JWS Payload
- JWS Signature


## JOSE Header

Parameters

- "alg" (Algorithm) Header Parameter
- "jku" (JWK Set URL) Header Parameter
- "jwk" (JSON Web Key) Header Parameter
- "kid" (Key ID) Header Parameter
- x5
    - "x5u" (X.509 URL) Header Parameter
    - "x5c" (X.509 Certificate Chain) Header Parameter
    - "x5t" (X.509 Certificate SHA-1 Thumbprint) Header Parameter
    - "x5t#S256" (X.509 Certificate SHA-256 Thumbprint) Header Parameter
- "typ" (Type) Header Parameter
- "cty" (Content Type) Header Parameter
- "crit" (Critical) Header Parameter




## Reference
- https://datatracker.ietf.org/doc/html/rfc7515
