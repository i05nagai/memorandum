---
title: Github Enterprise
---

## Github Enterprise

## Enterprise

- support entitlement
    - https://docs.github.com/en/enterprise-cloud@latest/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/managing-support-entitlements-for-your-enterprise


## Organization


## Migrations
https://docs.github.com/en/migrations/using-github-enterprise-importer/migrating-between-github-products/migrating-repositories-from-githubcom-to-github-enterprise-cloud


#### From Github.com to GHE.com
https://docs.github.com/en/migrations/using-github-enterprise-importer/migrating-between-github-products/about-migrations-between-github-products#data-that-is-migrated-from-githubcom

- We strongly recommend that you perform a trial run of your migration and complete your production migration soon after.
- repsitoryのPRのautolink


## Github enterprise managed user

#### Restrictions
https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/abilities-and-restrictions-of-managed-user-accounts

- General
    - Managed user accounts can contribute only to private and internal repositories within their enterprise and their own private repositories. 
    - On GitHub.com, they have read-only access to the wider GitHub community. These visibility and access restrictions apply to all requests, including API requests.
- Authentication
    - Managed user accounts authenticate using only your identity provider, and have no password or two-factor authentication methods stored on GitHub. As a result, they do not see the sudo prompt when taking sensitive actions.
- Github Actions
    - Managed user accounts cannot create workflow templates for GitHub Actions.
    - While GitHub-hosted runners can be used in repositories owned by organizations, they are not available for repositories owned by managed user accounts.
    - Enterprise Managed Users can trigger workflows in organizations where they are not members by forking the organization repository, then creating a pull request targeting the organization repository.
- Github Apps
- 

- interactiosn
    - On GitHub.com, managed user accounts can view all public repositories, but cannot interact with repositories outside of the enterprise in any of the following ways:
        - Push code to the repository
        - Create issues or pull requests within the repository
        - Create or comment on discussions within the repository
        - Comment on issues or pull requests, or add reactions to comments
        - Star, watch, or fork the repository
        - Managed user accounts cannot follow users outside of the enterprise.

#### Which should i choose

- https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/choosing-an-enterprise-type-for-github-enterprise-cloud
- https://www.arnica.io/blog/a-complete-guide-enterprise-managed-users-vs-bring-your-own-users-on-github


## EMU with Okta
First setup SAML2.0:https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/configuring-authentication-for-enterprise-managed-users/configuring-saml-single-sign-on-with-okta-for-enterprise-managed-users

- In Otak, Install the Okta application for your environment.
    - https://www.okta.com/integrations/github-enterprise-managed-user/
- In the application on Okta, click the Assignments tab and assign the application to your Okta account.
- Click the Sign on tab and Click Edit
    - Next to "Enterprise Name," type the name of your enterprise with managed users.
        - Can be found in `https://github.com/enterprises/<enterprise-name>`
- In Github Enterprise, Go to identity provider
    - https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/configuring-authentication-for-enterprise-managed-users/configuring-saml-single-sign-on-for-enterprise-managed-users#configure-your-enterprise

SCIM: https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/provisioning-user-accounts-with-scim/configuring-scim-provisioning-with-okta

- To configure provisioning, the setup user with the @SHORT-CODE_admin username will need to provide a personal access token (classic) with the scim:enterprise scope.
    - https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/getting-started-with-enterprise-managed-users#create-a-personal-access-token


setup user

- After you require SAML SSO for your enterprise and save SAML settings, the setup user will continue to have access to the enterprise and will remain signed in to GitHub along with the managed user accounts provisioned by your IdP who will also have access to the enterprise.

## Reference







