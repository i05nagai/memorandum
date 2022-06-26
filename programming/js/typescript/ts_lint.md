---
title: TSLint
---

## TSLint


```
npm install tslint --save-dev
```

## CLI


## Configuration

`tslint.json`

```json
{
    "defaultSeverity": "error",
    "extends": [
        "tslint:recommended"
    ],
    "jsRules": {},
    "rules": {},
    "rulesDirectory": []
}
```


- `extends?: string | string[]`
    - The name of a built-in configuration preset (see built-in presets below), or a path or array of paths to other configuration files which are extended by this configuration. This value is handled using node module resolution semantics. For example, a value of "tslint-config" would tell TSLint to try and load the main file of a module named “tslint-config” as a configuration file. Specific files inside node modules can also be specified, eg. "tslint-config/path/to/submodule". Relative paths to JSON files or JS modules are also supported, e.g. "./tslint-config".
- `rulesDirectory?: string | string[]`
    - A path to a directory or an array of paths to directories of custom rules. These values are handled using node module resolution semantics, if an index.js is placed in your rules directory. We fallback to use relative or absolute paths, if the module can’t be resolved. If you want to avoid module resolution you can directly use a relative or absolute path (e.g. with ./).
- `rules?: { [name: string]: RuleSetting }`
    - A map of rule names to their configuration settings.
    - These rules are applied to `.ts` and `.tsx` files.
    - Each rule is associated with an object containing:
        - `options?: any`
            - An array of values that are specific to a rule.
        - `severity?: "default" | "error" | "warning" | "off"`
            - Severity level. Level “error” will cause exit code 2.
        - Legacy: An array may be specified instead of the above object, and is equivalent to setting the rule with the default severity if the first value in the array is true, with configuration parameters in the remainder of the array.
            - `"no-empty": [true, "allow-empty-catch"]` is strictly equivalent to "no-empty": { "options": ['allow-empty-catch'], "severity": 'default' }
    - Legacy: A boolean value may be specified instead of the above object, and is equivalent to setting no options with default severity.
    - Any rules specified in this block will override those configured in any base configuration being extended.
- `jsRules?: any | boolean` Same format as rules or explicit true to copy all rule configurations for JS-compatible rules from rules. These rules are applied to .js and .jsx files.
- `defaultSeverity?: "error" | "warning" | "off"`
    - The severity level that is applied to rules in this config file as well as rules in any inherited config files which have their severity set to “default”. If undefined, “error” is used as the defaultSeverity.
- `linterOptions?: { exclude?: string[] }`
    - `exclude: string[]`
        - An array of globs. Any file matching these globs will not be linted. All exclude patterns are relative to the configuration file they were specified in.
    - `format: string`
        - Default lint formatter

## Reference
- https://palantir.github.io/tslint/#:~:text=TSLint%20is%20an%20extensible%20static,rules%2C%20configurations%2C%20and%20formatters.
