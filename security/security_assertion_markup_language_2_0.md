---
title: Security Assertion Markup Language 2.0
---

## Security Assertion Markup Language 2.0

- SAML Authority
    - Identity provider
- SAML Assetion
    - SAML assertion is provided by SAML Authority
- Relying Party
    - relying party is to 
- Service provider
- bearer
    - An important type of SAML assertion
    - Web Browser SSO


## Bearer

- `<ds:Signature>`
    - an integrity-preserving digital signature (not shown)
- `<saml:Issuer>`
    - the unique identifier of the identity provider
    - e.g. `https://idp.example.org/SAML2`
- `<saml:Subject>`
    - which identifies the authenticated principal 
    - `<saml:NameID>`
        - 
    - `<saml:SubjectConfirmation>`
            - `<saml:SubjectConfirmationData>`
- `<saml:Conditions>`
    - the conditions under which the assertion is to be considered valid
    - `<saml:AudienceRestriction>`
        - `<saml:Audience>https://sp.example.com/SAML2</saml:Audience>`
- `<saml:AuthnStatement>`
    - describes the act of authentication at the identity provider
    - `<saml:AuthnContext>`
        - `<saml:AuthnContextClassRef>`
            - e.g. `urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport`
- `<saml:AttributeStatement>`
    - presumably the service provider uses to make an access control decision
    - `<saml:Attribute>`
        `<saml:AttributeValue xsi:type="xs:string">member</saml:AttributeValue>`

## Reference
- https://en.wikipedia.org/wiki/SAML_2.0
