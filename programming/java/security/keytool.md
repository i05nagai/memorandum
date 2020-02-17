---
title: keytool
---

## keytool


## CLI

See data in keystore

```
keytool -list -v -keystore server.keystore.jks
```

```
keytool -gencert <option>
```

* -rfc
* -infile infile
* -outfile outfile
* -alias alias
* -sigalg sigalg}
* -dname dname
* -startdate startdate
* `-ext ext`
    * multiple options are allowed
    * The ext value shows what X.509 extensions will be embedded in the certificate. Read Common Options for the grammar of -ext.
    * e.g. `-ext SAN=DNS:{FQDN}`
* -validity valDays
* -keypass keypass
* -keystore keystore
* -storepass storepass
* -storetype storetype
    * `-storetype pkcs12`
        * if you choose `pkcs12`, keypass and storepass must be same
* -providername provider_name
* -providerClass provider_class_name {-providerArg provider_arg}
* -v
* -protected
* -Jjavaoption

Export a key in keystore

```
keytool \
    -keystore server.keystore.jks \
    -alias <alias-in-keystore> \
    -storepass <passwowrd-for-keystore> \
    -certreq -file credential/kafka-server.cert-file
```

#### Import a certificate

```
keytool \
    -import \
        -alias foo \
        -file certfile.cer \
        -keystore publicKey.keystore.jks
```


#### Deleete a certificate

```
keytool -delete -alias alias -keystore publicKey.keystore.jks
```

#### Show list of certificates

```
keytool \
    -keystore kafka.server.keystore.jks \
    -alias kafka-server \
    -storepass serverkeystore \
    -list
```

#### Check certificates fingerprints

```
openssl x509 -noout -fingerprint -sha256 -inform pem -in [certificate-file.crt]
openssl x509 -noout -fingerprint -sha1 -inform pem -in [certificate-file.crt]
openssl x509 -noout -fingerprint -md5 -inform pem -in [certificate-file.crt]
```


## Reference
- [keytool](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/keytool.html)
