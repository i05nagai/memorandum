---
title: swagger codegen
---

## swagger codegen

## CLI
Generate code with chosen languagge

```
java -jar ${SWAGGER_PATH}/swagger-codegen-cli.jar generate <option>
```

* `(-a <authorization> | --auth <authorization>)`
* `--additional-properties <additional properties>...`
* `--api-package <api package>`
* `--artifact-id <artifact id>`
* `--artifact-version <artifact version>`
* `(-c <configuration file> | --config <configuration file>)`
    * Path to json configuration file. File content should be in a json format `{"optionKey":"optionValue", "optionKey1":"optionValue1"...}`
* `-D <system properties>...`
* `--git-repo-id <git repo id>`
* `--git-user-id <git user id>`
* `--group-id <group id>`
* `--http-user-agent <http user agent>`
* `(-i <spec file> | --input-spec <spec file>)`
    * location of the swagger spec, as URL or file (required)
* `--ignore-file-override <ignore file override location>`
* `--import-mappings <import mappings>...`
* `--instantiation-types <instantiation types>...`
* `--invoker-package <invoker package>`
* `(-l <language> | --lang <language>)`
    *  client language to generate (maybe class name in classpath, required)
* `--language-specific-primitives <language specific primitives>...`
* `--library <library>` `--model-name-prefix <model name prefix>`
* `--model-name-suffix <model name suffix>`
* `--model-package <model package>`
* `(-o <output directory> | --output <output directory>)`
    * where to write the generated files (current dir by default)
* `--release-note <release note>` `--remove-operation-id-prefix`
* `--reserved-words-mappings <reserved word mappings>...`
* `(-s | --skip-overwrite)`
    * specifies if the existing files should be overwritten during the generation.
* `(-t <template directory> | --template-dir <template directory>)`
    * folder containing the template files
* `--type-mappings <type mappings>...`
    * sets mappings between swagger spec types and generated code types in the format of swaggerType=generatedType,swaggerType=generatedType
    * For example: array=List,map=Map,string=String. You can also have multiple occurrences of this option.
* `(-v | --verbose)`


## Usage
See help

```
java -jar ${SWAGGER_PATH}/swagger-codegen-cli.jar help <subcommand>
```

```
java -jar ${SWAGGER_PATH}/swagger-codegen-cli.jar generate \
    --verbose \
    --output $(pwd) \
    --lang python-flask \
    --config /path/to/config.json \
    --input-spec ./ \
```

## Configuration

## Reference
