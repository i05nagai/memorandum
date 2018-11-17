---
title: Coveralls
---

## Coveralls

## C/C++
* [eddyxu/cpp-coveralls: Upload gcov results to coveralls.io](https://github.com/eddyxu/cpp-coveralls)
* [google/benchmark: A microbenchmark support library](https://github.com/google/benchmark)

### Setup with CMake
* [JoakimSoderberg/coveralls-cmake: Coveralls JSON coverage generator and uploader for CMake](https://github.com/JoakimSoderberg/coveralls-cmake)
    * configuration of coverall with CMake
* [JoakimSoderberg/coveralls-cmake-example: Example project for coveralls-cmake](https://github.com/JoakimSoderberg/coveralls-cmake-example)
    * sample project of the above

Follow the following steps.

1. Include the `Coveralls.cmake` script in `CMakeLists.txt`
    * Configure `CMakeLists.txt` as follows

```cmake
# Add project cmake modules to path to include `Coveralls.cmake`.
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${PROJECT_SOURCE_DIR}/cmake)

# We probably don't want this to run on every build.
option(COVERALLS "Generate coveralls data" OFF)

if (COVERALLS)
    include(Coveralls)
endif()
```

2. Add coverage settings to your compile flags by writing

```cmake
if (COVERALLS)
    include(Coveralls)
    coveralls_turn_on_coverage()
endif()
```

or

```cmake
if (COVERALLS)
    include(Coveralls)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -O0 -fprofile-arcs -ftest-coverage")
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -g -O0 -fprofile-arcs -ftest-coverage")
endif()
```

3. Setup your target
    * sourceを指定して`coveralls_setup`に渡す

```cmake
if (COVERALLS)
    set(COVERAGE_SRCS awesome.c code.c files.c)

    # Create the coveralls target.
    coveralls_setup(
        "${COVERAGE_SRCS}" # The source files.
        ON                 # If we should upload.
        "${PROJECT_SOURCE_DIR}/CMakeModules/") # (Optional) Alternate project cmake module path.
endif()
```

Then

```
coveralls --verbose --include <path> --exclude <path> --gcov-options '\-lp' --root . --build-root <path-to-objs>
```

## CLI
https://github.com/eddyxu/cpp-coveralls
Then run

* `--verbose`
* `--include`
* `--exclude`
* `--gcov FILE`
    * set the location of gcov
* `--gcov-options GCOV_OPTS`
    * set the options given to gcov
* `--root <DIR>`
    * set the root directory
* `--build-root <DIR>`
    * set the directory from which gcov will be called
* `--exclude-pattern REGEXP`
* `--exclude-lines-pattern REGEXP`
* `--coveralls-yaml FILE`
* `--no-gcov`
    * do not run gcov
* `--repo-token`


### for

```
-g -O0 -fprofile-arcs -ftest-coverage
-g -O0 -fprofile-arcs -ftest-coverage
```

## Reference
* [Coveralls](https://coveralls.zendesk.com/hc/en-us)
