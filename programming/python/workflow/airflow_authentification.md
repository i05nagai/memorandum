---
title: Airflow Authentification
---

## Airflow Authentification


## Google authentification
* [Security — Airflow Documentation](https://airflow.apache.org/security.html#google-authentication)

```cfg
[webserver]
authenticate = True
auth_backend = airflow.contrib.auth.backends.google_auth

[google]
client_id = google_client_id
client_secret = google_client_secret
oauth_callback_route = /oauth2callback
domain = example.com
```

1. Navigate to https://console.developers.google.com/apis/
2. Select `Credentials` from the left hand nav
3. Click `Create credentials` and choose `OAuth client ID`
    * OAuth concent screen で product nameを設定する
4. Choose `Web application`
5. Fill in the required information (the `Authorized redirect URIs` must be fully qualifed e.g. http://airflow.example.com/oauth2callback )
6. Click `Create`
7. Copy `Client ID`, `Client Secret`, and your redirect URI to your `airflow.cfg` according to the above example

## Reference
