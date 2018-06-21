---
title: Code Climate CLI
---

## Code Climate CLI
CLI for reporting to Code Climate.
In Code Climate 1.0, it's provided as single binary file for any languages.

## Install
```
curl -L https://codeclimate.com/downloads/test-reporter/test-reporter-latest-linux-amd64 > ./cc-test-reporter
chmod +x ./cc-test-reporter
```

## CLI
```
cc-test-reporter [flags]
cc-test-reporter [command]
```

Locate, parse, and re-format supported coverage sources. Upload pre-formatted coverage payloads to Code Climate servers.

```
cc-test-reporter after-build [flags]
```

* `-s, --batch-size int`
    * batch size for source files (default 500)
* `-e, --coverage-endpoint string`
    * endpoint to upload coverage information to (default "https://api.codeclimate.com/v1/test_reports")
* `-t, --coverage-input-type string`
    * type of input source to use [clover, cobertura, coverage.py, excoveralls, gcov, gocov, jacoco, lcov, simplecov]
* `--exit-code int`
    * exit code of the test run
* `-r, --id string`
    * reporter identifier
    * default ""
* `--insecure`
    * send coverage insecurely (without HTTPS)
* `-p, --prefix string`
    * the root directory where the coverage analysis was performed
    * default ""


To be run before a build

```
./cc-test-reporter before-build
```

* `-d, --debug`
    * run in debug mode

Infer and output information about the environment the reporter is running in.

```
cc-test-reporter env [flags]
```

* `-f, --format string`
    * formats the output (default "string")

Locate, parse, and re-format supported coverage sources.

```
cc-test-reporter format-coverage [coverage file] [flags]
```

* `--add-prefix string`
    * add this prefix to file paths
* `-t, --input-type string`
    * type of input source to use [clover, cobertura, coverage.py, excoveralls, gcov, gocov, jacoco, lcov, simplecov]
* `-o, --output string`
    * output path (default "coverage/codeclimate.json")
* `-p, --prefix string`
    * the root directory where the coverage analysis was performed (default "/home/administrator/programming/python/github/mafipy")

Combine (sum) multiple pre-formatted coverage payloads into one.

```
cc-test-reporter sum-coverage [flasg]
```

* `-o, --output string`
    * output path (default "coverage/codeclimate.json")
* `-p, --parts int`
    * total number of parts to sum
* `-d, --debug`
    * run in debug mode

Upload pre-formatted coverage payloads to Code Climate servers.

```
cc-test-reporter upload-coverage [flags]
```

* `-s, --batch-size int`
    * batch size for source files (default 500)
* `-e, --endpoint string`
    * endpoint to upload coverage information to (default "https://api.codeclimate.com/v1/test_reports")
* `-r, --id string`
    * reporter identifier (default "")
* `-i, --input string`
    * input path (default "coverage/codeclimate.json")
* `--insecure`
    * send coverage insecurely (without HTTPS)


## Usage

```
export CC_TEST_REPORTER_ID="ABC123"
#
./cc-test-reporter before-build
# get coverage reports
./cc-test-reporter after-build --exit-code $EXIT_CODE --coverage-input-type <type>
```

where `<type>` depends on language and coverage tools

For `pytest-cov` or `pytest`, you need to output coverage report as xml.

```
pytest --cov-report=xml
cc-test-reporter after-build --coverage-input-type coverage.py
```

## Configuration

## Tips

### Get your test reporter id
* [Finding Your Test Coverage ID](https://docs.codeclimate.com/docs/finding-your-test-coverage-token)

## Reference
* [CC\_TEST\_REPORTER\_ID: ABC123](https://docs.codeclimate.com/docs/configuring-test-coverage)
* [codeclimate/test-reporter: Code Climate Test Reporter](https://github.com/codeclimate/test-reporter)
