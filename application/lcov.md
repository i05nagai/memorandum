---
title: lcov
---

## lcov
gcovのcoverageの結果を見やすく整形する。

## CLI

```
lcov
```

Creating tracefiles

```
lcov -c --gcov-tool TOOL--base-directory DIR --output-file <path>
```

Combine tracefile files

```
lcov --add-tracefile file.info --add-tracefile coverage.dat --output-file coverage.dat
```

* -z, --zerocounters
    * Reset all execution counts to zero
* -c, --capture
    * Capture coverage data
    * generate tracefiles
* `-a, --add-tracefile FILE`
    * Add contents of tracefiles
* -e, --extract FILE PATTERN
    * Extract files matching PATTERN from FILE
* -r, --remove FILE PATTERN
    * Remove files matching PATTERN from FILE
* -l, --list FILE
    * List contents of tracefile FILE
* --diff FILE DIFF
    * Transform tracefile FILE according to DIFF
* --summary FILE
    * Show summary coverage data for tracefiles

* -i, --initial
    * Capture initial zero coverage data
* -t, --test-name NAME
    * Specify test name to be stored with data
* `-o, --output-file FILENAME`
    * Write data to FILENAME instead of stdout
* `-d, --directory DIR`
    * Use .da files in DIR instead of kernel
* `-f, --follow`
    * Follow links when searching .da files
* -k, --kernel-directory KDIR
    * Capture kernel coverage data only from KDIR
* `-b, --base-directory DIR`
    * Use DIR as base directory for relative paths
* --convert-filenames
    * Convert filenames when applying diff
* --strip DEPTH
    * Strip initial DEPTH directory levels in diff
* --path PATH
    * Strip PATH from tracefile when applying diff
* --(no-)checksum
    * Enable (disable) line checksumming
* --(no-)compat-libtool
    * Enable (disable) libtool compatibility mode
* `--gcov-tool TOOL`
    * path to gcov
    * Specify gcov tool location
* `--ignore-errors ERRORS`
    * Continue after ERRORS (gcov, source, graph)
* --no-recursion
    * Exclude subdirectories from processing
* --to-package FILENAME
    * Store unprocessed coverage data in FILENAME
* --from-package FILENAME
    * Capture from unprocessed data in FILENAME
* --no-markers
    * Ignore exclusion markers in source code
* --derive-func-data
    * Generate function data from line data
* --list-full-path
    * Print full path during a list operation
* --(no-)external
    * Include (ignore) data for external files
* --config-file FILENAME
    * Specify configuration file location
* --rc SETTING=VALUE
    * Override configuration file setting
* --compat MODE=on|off|auto
    * Set compat MODE (libtool, hammer, split_crc)


## Reference
* [LCOV Code Coverage \- The Document Foundation Wiki](https://wiki.documentfoundation.org/Development/Lcov#Combine_lcov_tracefiles)
