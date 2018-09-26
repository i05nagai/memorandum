---
title: glog
---

## glog
C++ implementation of the Google logging module.


## Usage

```
#include <glog/logging.h>

int main(int argc, char* argv[]) {
 // Initialize Google's logging library.
 google::InitGoogleLogging(argv[0]);

 // ...
 LOG(INFO) << "Found " << num_cookies << " cookies";
}
```

If you do not run `InitGoogleLogging`, the logs are written to STDERR with the following messages;

```
WARNING: Logging before InitGoogleLogging() is written to STDERR
I0923 15:23:53.049594 2753422208 sample.cc:7] message
```

### Security level

* INFO
* WARNING
* ERROR
* FATAL
    * a FATAL message terminates the program (after the message is logged)
* DFATAL
    * a FATAL error in debug mode (i.e., there is no NDEBUG macro defined), but avoids halting the program in production by automatically reducing the severity to ERROR.

File path

* by default `/tmp/<program name>.<hostname>.<user name>.log.<severity level>.<date>.<time>.<pid>`
    * e.g. `/tmp/hello_world.example.com.hamaji.log.INFO.20080709-222411.10474`
* by default, glog copies the log messages of severity level ERROR or FATAL to standard error (stderr) in addition to log files

### Flags

* `logtostderr (bool, default=false)`
* `stderrthreshold (int, default=2, which is ERROR)`
* `minloglevel (int, default=0, which is INFO)`
* `log_dir (string, default="")`
* `v (int, default=0)`
* `vmodule (string, default="")`

```
// GLOG_flagname
GLOG_logtostderr=1 ./your_application
```

Conditional / Occasional Logging



Debug Mode Support

```cpp
DLOG(INFO) << "Found cookies";
DLOG_IF(INFO, num_cookies > 10) << "Got lots of cookies";
DLOG_EVERY_N(INFO, 10) << "Got the " << google::COUNTER << "th cookie";
```


* CHECK Macros

```cpp
CHECK(fp->Write(x) == 4) << "Write failed!";
CHECK_NE(1, 2) << ": The world must be ending!";
CHECK_EQ(string("abc")[1], 'b');

// null
CHECK_NOTNULL(some_ptr); // return pointer
some_ptr->DoSomething();
struct S {
 S(Something* ptr) : ptr_(CHECK_NOTNULL(ptr)) {}
 Something* ptr_;
};
```

## Reference
* [google/glog: C\+\+ implementation of the Google logging module](https://github.com/google/glog)
* [How To Use Google Logging Library \(glog\)](http://rpg.ifi.uzh.ch/docs/glog.html)
