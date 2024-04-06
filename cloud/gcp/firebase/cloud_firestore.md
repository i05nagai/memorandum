---
title: Cloud Firestore
---

## Cloud Firestore
Cloud Firestore is a cloud-hosted, NoSQL database.


- collection contains documents
- document is key-value mapping

- Cloud Firestore
    - It's suitable for applications with rich data models requiring queryability, scalability, and high availability.
    - It also offers low latency client synchronization and offline data access.
    - Stores data as collections of documents.
    - Offline support for Apple, Android, and web clients.
    - Indexed queries with compound sorting and filtering.
    - Advanced write and transaction operations.
    - a regional and multi-region solution that scales automatically.
    - 99.999% uptime
- Realtime Database
    - It is the classic Firebase JSON database.
    - It's suitable for applications with simple data models requiring simple lookups and low-latency synchronization with limited scalability.
    - Stores data as one large JSON tree.
    - Offline support for Apple and Android clients.
    - Deep queries with limited sorting and filtering features.
    - Basic write and transaction operations.
    - a regional solution.
    - 99.95% uptime


Data types
https://firebase.google.com/docs/firestore/manage-data/data-types?authuser=0


## API
https://firebase.google.com/docs/reference/js/v8

The namespace style is v8 (old) API.

```
// old API should not be used.
import firebase from "firebase/compat/app";
export const app = firebase.initializeApp(firebaseConfig);
export const db = firebase.firestore();
db.collections('cllct');
```

Moduler API is new.
https://firebase.google.com/docs/reference/js

```
import * as firebase from "firebase/app";
import * as firestore from "firebase/firestore";

export const app = firebase.initializeApp(firebaseConfig);
export const db = firestore.getFirestore(app);
firestore.collections(db, 'cllct')
```



## Reference
- https://firebase.google.com/docs/firestore
