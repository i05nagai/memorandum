---
title: Github Enterprise Cloud
---

## Github Enterprise Cloud

## EMU
- setup user
    - When you create a trial account, Admin work email will be tied to a setup user `<shortcode>_admin`
    - set up user is not provisioned by IdP



#### acount management with Okta
https://www.okta.com/integrations/github-enterprise-managed-user/
https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/configuring-authentication-for-enterprise-managed-users/configuring-saml-single-sign-on-with-okta-for-enterprise-managed-users

provisioning

- (1) create an account in Okta for github setup user
    - email is a google group email address
- (2) Create a Github EMU trial account
    - Account email: email of the otka user
    - Account name: put a name
- (3) 
- (3) account will be provisioned based on email address


```
isMemberOfGroupName("github-enterprise-enterprise-owner") ? "enterprise_owner" : isMemberOfGroupName("github-enterprise-billing_manager") ? "billing_manager" : isMemberOfGroupName("github-enterprise-guest_collaborator") ? "guest_collaborator" : "user"
Groups.startsWith("github-enterprise-")
```

- SCIM provsioning will create EM users in enterprise
    - default role is member
- Push Groups will create a linkd IDP group in enterprise settings
- In organization, you can sync 


#### SCIM with other IDP
https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/provisioning-user-accounts-with-scim/provisioning-users-and-groups-with-scim-using-the-rest-api


```
Key Points:

Setup User Independence: The setup user is not tied to Okta or any other IdP. It is a standalone account that exists outside of the provisioning system.
Accessing the Setup User: You should always access the setup user account using the credentials created during the initial setup or by using the SAML recovery codes. This ensures that the setup user remains separate from the managed user accounts provisioned by Okta.
No Association with Okta: There is no way to associate or assign an Okta user to the setup user account. The setup user is meant to remain independent for administrative purposes.
Recommended Approach:

Continue to use the setup user account for tasks like creating the personal access token (classic) for SCIM provisioning or recovering access to your enterprise.
Use the SAML recovery codes to log in to the setup user account when needed.
For all other enterprise administration tasks, use a provisioned managed user account with the enterprise owner role.
```


## Migration
https://docs.github.com/en/migrations/overview/planning-your-migration-to-github


### Github.com to Github.com
https://docs.github.com/en/migrations/overview/migration-paths-to-github#githubcom-to-githubcom


## Migration tools


### Github Enterprise importer
https://docs.github.com/en/migrations/using-github-enterprise-importer/completing-your-migration-with-github-enterprise-importer/reclaiming-mannequins-for-github-enterprise-importer

### projects
https://github.com/timrogers/gh-migrate-project


## Reference
- https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-user-access-to-your-organizations-repositories/managing-outside-collaborators/adding-outside-collaborators-to-repositories-in-your-organization
