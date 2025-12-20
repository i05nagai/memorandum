---
title: HTTP
---

## HTTP


## Preflight reuqest
https://docs.sensedia.com/en/faqs/Latest/apis/preflight.html

- It is an HTTP request of the OPTIONS method, sent before the request itself, in order to determine if it is safe to send it.


## Headers

#### Cache-Control
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control

#### Referrer-Policy

#### X-Content-Type-Options

#### Content-Security-Policy

- frame-ancestors


#### X-Frame-Options
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options

- `DENY`
- `ALLOW-FROM uri`
- `SAMEORIGIN`


#### X-Forwarded-For

https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For

#### CORS
- https://metamug.com/article/api-cors.html
- https://docs.sensedia.com/en/faqs/Latest/apis/preflight.html

Cross Origin Resource Sharing

- 1. Client
    - Make a preflight request if server supports OPTIONS method
- 2. Server
    - Response with CORS headers
- 3. Client
    - actual request
- 4. Server
    - response with data

Headers from Server

- Access-Control-Allow-Origin
    - This header specifies which origin(s) are allowed to make requests to your API.
    - You can set it to a specific origin or use a wildcard (*) to allow requests from any origin.
- Access-Control-Allow-Methods
    - This header lists the HTTP methods (e.g., GET, POST, PUT, DELETE) that are allowed for the API.
- Access-Control-Allow-Headers
    - Use this header to specify which HTTP headers can be used in the actual request.
- Access-Control-Expose-Headers
    - If your API uses custom headers, you can include them in this header to make them accessible to the client-side JavaScript.
- Access-Control-Allow-Credentials
    - If your API requires authentication and you want to allow credentials (e.g., cookies, HTTP authentication) to be included in the request, set this header to "true." Be aware that setting this header requires the client-side request to include the "withCredentials" option.
- Access-Control-Max-Age
    - This header specifies how long the results of a preflight request can be cached in seconds. A preflight request is an initial request sent by the browser before the actual request, used to check if the server allows the actual request.


## Reference
