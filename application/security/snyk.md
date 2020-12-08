---
title: Synk
---

## Synk

## CLI

```
snyk
```


## Usage

Sign into Snyk.

```
snyk auth [api-token]
```

Test for any known vulnerabilities.

```
snyk test
snyk test --all-projects --detection-depth=<number> --exclude=<comma seperated list of directory names>
```

Configure your policy file to update, auto patch and ignore vulnerabilities in npm & yarn projects.

```
snyk wizard
```

Protect your code from vulnerabilities and optionally suppress specific vulnerabilities. Note: Node.js only.

```
snyk protect
```

Record the state of dependencies and any vulnerabilities on snyk.io.

```
# you can define project name explictly
snyk monitor --projcet-name=...
snyk monitor --all-projects --detection-depth=<number> --exclude=<comma seperated list of directory names>
```

Display the Snyk policy for a package.

```
snyk policy
```

Modifies the `.snyk` policy to ignore stated issues.

```
snyk ignore
snyk ignore --id='npm:braces:20180219' --expiry='2018-04-01' --reason='testing'
```

Manage Snyk's configuration, note that this configuration is stored on your machine and applies to all Snyk CLI calls.

```
snyk config
```


* `--all-projects`
    * (test & monitor commands only)
    * Auto detect all projects in working directory.
    * Note gradle is not supported, use --all-sub-projects instead.
* `--detection-depth=<number>`
    * (test & monitor commands only)
    * Use with --all-projects to indicate how many sub-directories to search.
    * Defaults to 2 (the current working directory and one sub-directory).
* `--exclude=<comma seperated list of directory names>`
    * (test & monitor commands only)
    * Can only be used with --all-projects to indicate sub-directories to exclude.
    * Directories must be comma seperated.
    * If using with --detection-depth exclude ignores directories at any level deep.
* `--dev`
    * Include devDependencies (defaults to production only).
* `--file=<File>`
    * Sets package file.
    * e.g. `--file=setup.py,Dockerfile`
    * `--file` and `--all-projects` are mutually exclusive option
* `--org=<org-name>`
    * Specify the org machine-name to run Snyk with a specific
    * organization. For more help run `snyk help orgs`.
* `--ignore-policy`
    * Ignores the current policy in .snyk file, org level ignores and project policy on snyk.io.
* `--trust-policies`
    * Applies and uses ignore rules from your dependencies's Snyk policies, otherwise ignore policies are only shown as a suggestion.
* `--show-vulnerable-paths=<none|some|all>`
    * (test command only)
    * Display the dependency paths from the top level dependencies, down to the vulnerable packages.
    * Defaults to "some" (a few example paths).
    * "false" is an alias for "none".
    * Doesn't affect output in JSON mode.
* `--project-name=<string>`
    * Specify a custom Snyk project name.
* `--policy-path`
    * Manually pass a path to a policy file.
* `--insecure`
    * Ignore unknown certificate authorities.
* `--json`
    * Return results in JSON format.
* `--dry-run`
    * Don't apply updates or patches during protect.
* `--severity-threshold=<low|medium|high>`
    * Only report vulnerabilities of provided level or higher.
* `-q, --quiet`
* `--print-deps`
    * (test and monitor commands only)
    * Print the dependency tree before sending it for analysis.
* `--prune-repeated-subdependencies`
    * (test and monitor command only)
    * Prune dependency trees, removing duplicate sub-dependencies.  Will still find all vulnerabilities, but potentially not all of the vulnerable paths.
* `--remote-repo-url=<string>`
    * (monitor command only)
    * Set or override the remote URL for the repository that you would like to monitor.
* `--fail-on=<all|upgradable|patchable>`
    * Only fail when there are vulnerabilities that can be fixed.  All fails when there is at least one vulnerability that can be either upgraded or patched.  Upgradable fails when there is at least one vulnerability that can be upgraded.  Patchable fails when there is at least one vulnerability that can be patched.  If vulnerabilities do not have a fix and this option is being used tests will pass.  


## Usage

```
# run vulnerability check
snyk test --all-projects --detection-depth=<number> --exclude=<comma seperated list of directory names>
# report the issue to snyk.io
snyk monitor --all-projects --detection-depth=<number> --exclude=<comma seperated list of directory names>
```

## Concepts

* Security issues
    * Sum total of security issues broken down by severity. Security issues are vulnerabilities found when scanning your projects.
* License issues


## Install
- [Continuous Integration: language support – Snyk](https://support.snyk.io/hc/en-us/articles/360004032157-Continuous-Integration-language-support)

```
npm install -g snyk
```

## Configuration

`.snyk` plicy file


## Scan For Ruby, Python, Java, Go, and .NET

Run `synk test` by providing `SNYK_TOKEN` environment variables.

## License policy
- [Configuring license policies – Snyk](https://support.snyk.io/hc/en-us/articles/360003520598-Configuring-license-policies)

## Tips

#### 413 error when run snyk monitor
- [Snyk monitor is failing – Snyk](https://support.snyk.io/hc/en-us/articles/360001889797-Snyk-monitor-is-failing)


## Reference
- [Snyk \| Develop Fast\. Stay Secure](https://snyk.io/)
- [Snyk basics – Snyk](https://support.snyk.io/hc/en-us/categories/360000449098-Snyk-basics)
