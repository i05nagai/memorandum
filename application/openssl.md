---
title: openssl
---
## openssl

## Install

For ubuntu 16.04, install v1.1.0

```
cd /tmp
VERSION="openssl-1.1.0h"
wget https://www.openssl.org/source/${VERSION}.tar.gz
tar xzvf ${VERSION}.tar.gz
cd ${VERSION}
./config -Wl,--enable-new-dtags,-rpath,'$(LIBRPATH)'
make
sudo make install
```


## self signed certification
以下で、10年間有効な自己署名証明書が作れる。

```
openssl genrsa 2048 > server.key
openssl req -new -key server.key > server.csr
openssl x509 -days 3650 -req -signkey server.key < server.csr > server.crt
```

* certificate file
    * server.crt
* certificate key file
    * server.key

* [オレオレ証明書をopensslで作る（詳細版） - ろば電子が詰まっている](http://d.hatena.ne.jp/ozuma/20130511/1368284304)

## CLI

#### s_client

- `/etc/ssl/certs/`

```
openssl s_client -connect <host>:<port> 
```

#### req

```
openssl req <option>
```

* -help               Display this summary
* -inform PEM|DER     Input format - DER or PEM
* -outform PEM|DER    Output format - DER or PEM
* `-in infile`
    * Input file
* `-out outfile`
    * Output file
* `-key val`
    * Private key to use
* -keyform format     Key file format
* `-pubkey`
    * Output public key
* `-new`
    * New request
* -config infile      Request template file
* -keyout outfile     File to send the key to
* `-passin val`
    * Private key password source
    * val can be one of
        * `pass:<row-password>`
        * `file:<path-to-file>`
* `-passout val`
    * Output file pass phrase source
* `-rand val`
    * Load the file(s) into the random number generator
* -writerand outfile  Write random data to the specified file
* -newkey val         Specify as type:bits
* -pkeyopt val        Public key options as opt:value
* -sigopt val         Signature parameter in n:v form
* -batch              Do not ask anything during request generation
* -newhdr             Output "NEW" in the header lines
* -modulus            RSA modulus
* -verify             Verify signature on REQ
* -nodes              Don't encrypt the output key
* -noout              Do not output REQ
* -verbose            Verbose output
* -utf8               Input characters are UTF8 (default ASCII)
* -nameopt val        Various certificate name options
* -reqopt val         Various request text options
* -text               Text form of request
* -x509
    * Output a x509 structure instead of a cert request (Required by some CA's)
* -subj val           Set or modify request subject
* -subject            Output the request's subject
* -multivalue-rdn     Enable support for multivalued RDNs
* -days +int          Number of days cert is valid for
* -set_serial val     Serial number to use
* -addext val         Additional cert extension key=value pair (may be given more than once)
* -extensions val     Cert extension section (override value in config file)
* -reqexts val        Request extension section (override value in config file)
* -precert            Add a poison extension (implies -new)
* -*                  Any supported digest
* -engine val         Use engine, possibly a hardware device
* -keygen_engine val  Specify engine to be used for key generation operations


#### genrsa

```
openssl genrsa
```

* -3
    * Use 3 for the E value
* -F4                 Use F4 (0x10001) for the E value
* -f4                 Use F4 (0x10001) for the E value
* `-out outfile`
    * Output the key to specified file
* -rand val           Load the file(s) into the random number generator
* -writerand outfile  Write random data to the specified file
* `-passout val`
    * Output file pass phrase source
* -*
    * Encrypt the output with any supported cipher
    * `-des3`
* -engine val         Use engine, possibly a hardware device
* -primes +int        Specify number of primes


#### rsa

```
openssl rsa 
openssl rsa -passin pass:x -in server.pass.key -out server.key
```

* `-inform format`
    * Input format, one of DER PEM
* `-outform format`
    * Output format, one of DER PEM PVK
* `-in val`
    * Input file
* `-out outfile`
    * Output file
* -pubin             Expect a public key in input file
* -pubout            Output a public key
* `-passout val`
    * Output file pass phrase source
* `-passin val`
    * Input file pass phrase source
* -RSAPublicKey_in   Input is an RSAPublicKey
* -RSAPublicKey_out  Output is an RSAPublicKey
* -noout             Don't print key out
* -text              Print the key in text
* -modulus           Print the RSA key modulus
* -check             Verify key consistency
* -*                 Any supported cipher
* -pvk-strong        Enable 'Strong' PVK encoding level (default)
* -pvk-weak          Enable 'Weak' PVK encoding level
* -pvk-none          Don't enforce PVK encoding
* -engine val        Use engine, possibly a hardware device

#### x509

```
openssl x509 -req -sha256 -days 365 -in server.csr -signkey server.key -out server.crt
```

* `-inform format`
    * Input format - default PEM (one of DER or PEM)
* `-in infile`
    * Input file - default stdin
* `-outform format`
    * Output format - default PEM (one of DER or PEM)
* `-out outfile`
    * Output file - default stdout
* -keyform PEM|DER      Private key format - default PEM
* `-passin val`
    * Private key password/pass-phrase source
* -serial               Print serial number value
* -subject_hash         Print subject hash value
* -issuer_hash          Print issuer hash value
* -hash                 Synonym for -subject_hash
* -subject              Print subject DN
* -issuer               Print issuer DN
* -email                Print email address(es)
* -startdate            Set notBefore field
* -enddate              Set notAfter field
* -purpose              Print out certificate purposes
* -dates                Both Before and After dates
* -modulus              Print the RSA key modulus
* -pubkey               Output the public key
* -fingerprint          Print the certificate fingerprint
* `-alias`
    * Output certificate alias
* -noout                No output, just status
* -nocert               No certificate output
* -ocspid               Print OCSP hash values for the subject name and public key
* -ocsp_uri             Print OCSP Responder URL(s)
* -trustout             Output a trusted certificate
* -clrtrust             Clear all trusted purposes
* -clrext               Clear all certificate extensions
* -addtrust val         Trust certificate for a given purpose
* -addreject val        Reject certificate for a given purpose
* -setalias val         Set certificate alias
* `-days int`
    * How long till expiry of a signed certificate - def 30 days
* -checkend intmax      Check whether the cert expires in the next arg seconds. Exit 1 if so, 0 if not
* `-signkey infile`
    * Self sign cert with arg
* -x509toreq            Output a certification request object
* `-req`
    * Input is a certificate request, sign and output
* `-CA infile`
    * Set the CA certificate, must be PEM format
* `-CAkey val`
    * The CA key, must be PEM format; if not in CAfile
* -CAcreateserial       Create serial number file if it does not exist
* -CAserial val         Serial file
* -set_serial val       Serial number to use
* -text                 Print the certificate in text form
* -ext val              Print various X509V3 extensions
* -C                    Print out C code forms
* -extfile infile       File with X509V3 extensions to add
* -rand val             Load the file(s) into the random number generator
* -writerand outfile    Write random data to the specified file
* -extensions val       Section from config file to use
* -nameopt val          Various certificate name options
* -certopt val          Various certificate text options
* -checkhost val        Check certificate matches host
* -checkemail val       Check certificate matches email
* -checkip val          Check certificate matches ipaddr
* -CAform PEM|DER       CA format - default PEM
* -CAkeyform format     CA key format - default PEM
* -sigopt val           Signature parameter in n:v form
* -force_pubkey infile  Force the Key to put inside certificate
* -next_serial          Increment current certificate serial number
* -clrreject            Clears all the prohibited or rejected uses of the certificate
* -badsig               Corrupt last byte of certificate signature (for test)
* `-*`
    * Any supported digest
    * e.g. `-sha256`
* -subject_hash_old     Print old-style (MD5) issuer hash value
* -issuer_hash_old      Print old-style (MD5) subject hash value
* -engine val           Use engine, possibly a hardware device
* -preserve_dates       preserve existing dates when signing

## Usage
[The Most Common OpenSSL Commands](https://www.sslshopper.com/article-most-common-openssl-commands.html)

Check a Certificate Signing Request (CSR)

```
openssl req -text -noout -verify -in CSR.csr
```

check private key

```
openssl rsa -in privateKey.key -check
```

Check a certificate

```
openssl x509 -in certificate.crt -text -noout
```

Check a PKCS#12 file (.pfx or .p12)

```
openssl pkcs12 -info -in keyStore.p12
```

## PEM file
* [How to SSL - PEM Files](http://how2ssl.com/articles/working_with_pem_files/)
* [How to SSL - OpenSSL tips and common commands](http://how2ssl.com/articles/openssl_commands_and_tips/)

## Reference


