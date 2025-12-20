---
title: yo
---

## yo


## CLI

Generate models from ddl under models directory

```
yo generate schema.sql --from-ddl -o models
```

Generate models under models directory

```
yo generate $SPANNER_PROJECT_NAME $SPANNER_INSTANCE_NAME $SPANNER_DATABASE_NAME -o models
```

-  -c, `--config string`
    -  path to Yo config file
- `--disable-default-modules`
    - disable the default modules for code generation
- `--disable-format`
    - disable to apply gofmt to generated files
- `--from-ddl`
    - toggle using DDL file
- `--global-module stringArray`
    - add a user defined module to global modules
- `--header-module string`
    - replace the default header module by user defined module
- `--ignore-fields stringArray`
    - fields to exclude from the generated Go code types
- `--ignore-tables stringArray`
    - tables to exclude from the generated Go code types
- -o, `--out string`
    - output path or file name
- -p, `--package string`
    - package name used in generated Go code
- `--suffix string`
    - output file suffix (default ".yo.go")
- `--tags string`
    - build tags to add to a package header
- `--type-module stringArray`
    - add a user defined module to type modules
- `--use-legacy-index-module`
    - use legacy index func name

Generate the autocompletion script for the specified shell

```
yo completion
```

yo create-template generates default template files 

```
yo create-template
```

yo generate generates Go code from ddl file.

```
yo generate
```

## Templates

- templates/type.go.tpl
    - Template for schema tables
- templates/index.go.tpl
    - Template for schema indexes
- templates/yo_db.go.tpl
    - Package level template generated once per package
- templates/yo_package.go.tpl
    - File header template generated once per file

## Reference
- https://github.com/cloudspannerecosystem/yo
