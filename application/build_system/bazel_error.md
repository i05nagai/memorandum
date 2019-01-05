---
title: Bazel Error
---

## Bazel Error

#### Xcode version

```
INFO: Build options have changed, discarding analysis cache.
ERROR: /private/var/tmp/_bazel_admin/0099d101d51ced9465d2576ad460ef37/external/local_config_cc/BUILD:50:5: in apple_cc_toolchain rule @local_config_cc//:cc-compiler-darwin_x86_64: Xcode version must be specified to use an Apple CROSSTOOL. If your Xcode version has changed recently, try: "bazel clean --expunge" to re-run Xcode configuration
ERROR: Analysis of target '@gtest//:gtest' failed; build aborted: Analysis of target '@local_config_cc//:cc-compiler-darwin_x86_64' failed; build aborted
INFO: Elapsed time: 0.412s
INFO: 0 processes.
FAILED: Build did NOT complete successfully (3 packages loaded)
```

```
bazel clean --expunge
sudo xcode-select -s /Applications/Xcode.app/Contents/Developer
sudo xcodebuild -license
bazel clean --expunge 
```


#### bazel-builderror
The code bazel execute is defined below

* [bazel/collect\_coverage\.sh at master · bazelbuild/bazel](https://github.com/bazelbuild/bazel/blob/master/tools/test/collect_coverage.sh)
* [bazel/collect\_cc\_coverage\.sh at master · bazelbuild/bazel](https://github.com/bazelbuild/bazel/blob/master/tools/test/collect_cc_coverage.sh)

## Reference

