---
title: JAAS
---

## JAAS


## Configuration

```
<entry name> { 
    <LoginModule> <flag> <LoginModule options>;
    <LoginModule> <flag> <LoginModule options>;
    . . .
};
```

Example

```
JaasSample {
  com.sun.security.auth.module.Krb5LoginModule required;
};
```


Java options

```
-Djavax.net.ssl.keyStore=${com.sun.aas.instanceRoot}/path/ks-name
-Djavax.net.ssl.trustStore=${com.sun.aas.instanceRoot}/path/ts-name
```


## Keystore and truststore
- [Creating Java Keystores and Truststores \| 5\.2\.x \| Cloudera Documentation](https://www.cloudera.com/documentation/enterprise/5-2-x/topics/cm_sg_create_key_trust.html)
- [Generating a KeyStore and TrustStore \(Configuring Java CAPS for SSL Support\)](https://docs.oracle.com/cd/E19509-01/820-3503/6nf1il6er/index.html)
- [keytool](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/keytool.html)
- [Working with Certificates and SSL \(Sun Java System Application Server Platform Edition 8\.2 Administration Guide\)](https://docs.oracle.com/cd/E19830-01/819-4712/ablqw/index.html)



- keystore
    - The keystore contains private keys and certificates used by SSL servers to authenticate themselves to SSL clients. By convention, such files are referred to as keystores.
- truststore
    - When used as a truststore, the file contains certificates of trusted SSL servers, or of Certificate Authorities trusted to identify servers. There are no private keys in the truststore.

```
keytool <option>
```

* -certreq
    * Generates a certificate request
* -changealias
    * Changes an entry's alias
* -delete
    * Deletes an entry
* -exportcert
    * Exports certificate
* -genkeypair
    * Generates a key pair
* -genseckey
    * Generates a secret key
* -gencert
    * Generates certificate from a certificate request
* -importcert
    * Imports a certificate or a certificate chain
* -importpass
    * Imports a password
* -importkeystore
    * Imports one or all entries from another keystore
* -keypasswd
    * Changes the key password of an entry
* -list
    * Lists entries in a keystore
* -printcert
    * Prints the content of a certificate
* -printcertreq
    * Prints the content of a certificate request
* -printcrl
    * Prints the content of a CRL file
* -storepasswd
    * Changes the store password of a keystore

Generate key store

```
keytool -keystore clientkeystore -genkey -alias client
```

## Reference
- [16\. Security](https://docs.spring.io/spring-cloud-dataflow/docs/1.1.0.M1/reference/html/getting-started-security.html)
- [JAAS Authentication](https://docs.oracle.com/javase/7/docs/technotes/guides/security/jgss/tutorials/AcnOnly.html)
- [JAAS Login Configuration File](https://docs.oracle.com/javase/7/docs/technotes/guides/security/jgss/tutorials/LoginConfigFile.html)
