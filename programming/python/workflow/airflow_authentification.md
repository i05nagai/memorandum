---
title: Airflow Authentification
---

## Airflow Authentification


## Google authentification
* [Security — Airflow Documentation](https://airflow.apache.org/security.html#google-authentication)

```
pip install Flask-OAuthlib
```

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
    * callback: `http://example.com/?next=%2Fadmin%2F`
6. Click `Create`
7. Copy `Client ID`, `Client Secret`, and your redirect URI to your `airflow.cfg` according to the above example

authentificateをONに、`/admin`は`302`でredirect、`/admin/airflow/noaccess`される。
health checkをする場合は`/health`にする。

URLにaccessすると以下のようなErrorがでる場合
[authentication - Google OAuth 2 authorization - Error: redirect_uri_mismatch - Stack Overflow](https://stackoverflow.com/questions/11485271/google-oauth-2-authorization-error-redirect-uri-mismatch)

```
Error: redirect_uri_mismatch
```


## GCR Docker
access tokenを使う方法。
docker configから

```sh
airflow connections \
    --add \
    --conn_id=docker \
    --conn_type=docker \
    --conn_host=https://asia.gcr.io \
    --conn_login=oauth2accesstoken
    --conn_password=$(cat /root/.docker/config.json) | sed 's/.*"password":"\([^"]\+\)".*/\1/') > /dev/null
```

gcloudから

```sh
airflow connections \
    --add \
    --conn_id=docker \
    --conn_type=docker \
    --conn_host=https://asia.gcr.io \
    --conn_login=oauth2accesstoken
    --conn_password=$(gcloud auth application-default print-access-token) > /dev/null
```


以下はだめ。
password too longになる。
custom hookを作るしかない。

```
airflow connections \
    --add \
    --conn_id=docker \
    --conn_type=docker \
    --conn_host=https://asia.gcr.io \
    --conn_login=_json_key \
    --conn_password=$(cat ${GOOGLE_APPLICATION_CREDENTIALS})
```


## Reference
