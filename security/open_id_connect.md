---
title: OpenID connect
---

## OpenID connect


- OpenID Provider (IDP)
    - An OpenID Provider (OP) is an entity that has implemented the OpenID Connect and OAuth 2.0 protocols, OP’s can sometimes be referred to by the role it plays, such as: a security token service, an identity provider (IDP), or an authorization server.
- Client
    - A client is a piece of software that requests tokens either for authenticating a user or for accessing a resource (also often called a relying party or RP). A client must be registered with the OP. Clients can be web applications, native mobile and desktop applications, etc.
- RP (Client)
    - RP stands for Relying Party, an application or website that outsources its user authentication function to an IDP.


## OpenID Core
https://openid.net/specs/openid-connect-core-1_0.html

- 1. The RP (Client) sends a request to the OpenID Provider (OP).
- 2. The OP authenticates the End-User and obtains authorization.
- 3. The OP responds with an ID Token and usually an Access Token.
- 4. The RP can send a request with the Access Token to the UserInfo Endpoint.
- 5. The UserInfo Endpoint returns Claims about the End-User.


## Reference
