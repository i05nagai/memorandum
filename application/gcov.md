---
title: gcov
---

## gcov
Testing code coverage for C/C++.


## CLI

```
gcov [options] files
```

* `-a`, `--all-blocks`
* `-b`, `--branch-probabilities`
* `-i`, `--json-format`,
* `-j`, `--human-readable`
* `-k`, `--use-colors`,
* `-m`, `--demangled-names`
* `-o directory|file`, `--object-directory directory`, `--object-file file`
    * Specify either the directory containing the gcov data files, or the object path name. 
    * he .gcno, and .gcda data files are searched for using this option.
* `-s directory`, `--source-prefix directory`
    * A prefix for source file names to remove when generating the output coverage files
* `-w`, `--verbose`,
* `-v`, `--version`

## Reference
* [Using the GNU Compiler Collection \(GCC\): Gcov](https://gcc.gnu.org/onlinedocs/gcc/Gcov.html)
* [Generating Code Coverage Report Using GNU Gcov & Lcov\.](https://medium.com/@naveen.maltesh/generating-code-coverage-report-using-gnu-gcov-lcov-ee54a4de3f11)
