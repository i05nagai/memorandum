---
title: Chromium
---

## Chromium
Source code

```
git clone https://chromium.googlesource.com/chromium/src
```

## Build on osx
- https://github.com/chromium/chromium/blob/main/docs/README.md
- https://github.com/chromium/chromium/blob/main/docs/mac_build_instructions.md

#### gn
- https://groups.google.com/a/chromium.org/g/chromium-dev/c/HJqd8JCebJA?pli=1
gn needs to be installed.
There is a prebuild binary. But it might not work.

```
git clone https://gn.googlesource.com/gn
cd gn
python build/gen.py # --allow-warning if you want to build with warnings.
ninja -C out
cp out/cp /path/to/
```


```
git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
export PATH="$PATH:/path/to/depot_tools"

caffeinate fetch chromium

cd /path/to/chromium
brew install ninja

gclient sync

cd chromium
gn gen out/Default
```

```
# build targets
gn ls out/Default
```

### CSS
画像処理部分は`skia image library`を使っている。
`src/cc/paint`にCSSのfilter部分のcodeがある。
`render_surface_filters.cc`にfilterのcolor matrixの定義がある。
matrixはsize201次元配列で書かれている。
添字の対応は以下のようになる。

$$
\left(
    \begin{array}{ccccc}
        a_{0} &
        a_{1} &
        a_{2} &
        a_{3} &
        a_{4}
        \\
        a_{5} &
        a_{6} &
        a_{7} &
        a_{8} &
        a_{9}
        \\
        a_{10} &
        a_{11} &
        a_{12} &
        a_{13} &
        a_{14}
        \\
        a_{15} &
        a_{16} &
        a_{17} &
        a_{18} &
        a_{19}
    \end{array}
\right)
$$

Brightness

$$
\left(
    \begin{array}{ccccc}
        s &
        0 &
        0 &
        0 &
        0
        \\
        0 &
        s &
        0 &
        0 &
        0
        \\
        0 &
        0 &
        s &
        0 &
        0
        \\
        0 &
        0 &
        0 &
        1.0 &
        0
    \end{array}
\right)
$$

Contrast

$$
\left(
    \begin{array}{ccccc}
        s &
        0 &
        0 &
        0 &
        (-0.5s + 0.5) \times 255
        \\
        0 &
        s &
        0 &
        0 &
        (-0.5s + 0.5) \times 255
        \\
        0 &
        0 &
        s &
        0 &
        (-0.5s + 0.5) \times 255
        \\
        0 &
        0 &
        0 &
        1.0 &
        0
    \end{array}
\right)
$$

Saturation

$$
\begin{eqnarray}
    & &
    \left(
        \begin{array}{ccccc}
            0.213 + 0.787s &
            0.715 - 0.715s &
            1.0 - (0.213 + 0.787s + 0.715 - 0.715s) &
            0 &
            0
            \\
            0.213 - 0.213s &
            0.715 + 0.285s &
            1.0 - (0.213 - 0.213s + 0.715 + 0.285s) &
            0 &
            0
            \\
            0.213 - 0.213s &
            0.715 - 0.715s &
            1.0 - (0.213 - 0.213s + 0.715 - 0.715s) &
            0 &
            0
            \\
            0 &
            0 &
            0 &
            1.0 &
            0
        \end{array}
    \right)
    \\
    & = &
    \left(
        \begin{array}{ccccc}
            0.213 + 0.787s &
            0.715 - 0.715s &
            0.072 - 0.072s &
            0 &
            0
            \\
            0.213 - 0.213s &
            0.715 + 0.285s &
            0.072 - 0.072s &
            0 &
            0
            \\
            0.213 - 0.213s &
            0.715 - 0.715s &
            0.072 + 0.928s &
            0 &
            0
            \\
            0 &
            0 &
            0 &
            1.0 &
            0
        \end{array}
    \right)
\end{eqnarray}
$$

## Directory structure
* [Getting Around the Chromium Source Code Directory Structure - The Chromium Projects](https://www.chromium.org/developers/how-tos/getting-around-the-chrome-source-code)

* android_webview
    * Provides a facade over src/content suitable for integration into the android platform. NOT intended for usage in individual android applications (APK). More information about the Android WebView source code organization.
* apps
    * Chrome packaged apps.
* base
    * Common code shared between all sub-projects. This contains things like string manipulation, generic utilities, etc. Add things here only if it must be shared between more than one other top-level project. 
* breakpad
    * Google's open source crash reporting project. This is pulled directly from Google Code's Subversion repository.
* build
    * Build-related configuration shared by all projects.
* cc
    * The Chromium compositor implementation.
* chrome
    * The Chromium browser (see below).
* chrome/test/data
    * Data files for running certain tests.
* components
    * directory for components that have the Content Module as the uppermost layer they depend on.
* content
    * The core code needed for a multi-process sandboxed browser (see below). More information about why we have separated out this code.
* device
    * Cross-platform abstractions of common low-level hardware APIs.
* net
    * The networking library developed for Chromium. This can be used separately from Chromium when running our simple test_shell in the webkit repository. See also chrome/common/net.
* sandbox
    * The sandbox project which tries to prevent a hacked renderer from modifying the system.
* skia
    * Google's Skia graphics library developed for Android. This is a copy from Android's tree. Our additional classes in ui/gfx wrap Skia.
* sql
    * Our wrap around sqlite.
* testing
    * Contains Google's open-sourced GTest code which we use for unit testing.
* third_party
    * A bunch of external libraries such as image decoders and compression libraries. There are also some Chrome-specific third-party libraries in chrome/third_party. Adding new packages.
* tools
* ui/gfx
    * Shared graphics classes. These form the base of Chromium's UI graphics.
* ui/views
    * A simple framework for doing UI development, providing rendering, layout and event handling. Most of the browser UI is implemented in this system. This directory contains the base objects. Some more browser-specific objects are in chrome/browser/ui/views.
* url
    * Google's open source URL parsing and canonicalization library.
* v8
    * The V8 Javascript library. This is pulled directly from Google Code's Subversion repository.
* webkit
    * All of Chromium's Webkit-related stuff:
    * appcache:
    * base:
    * blob:
    * build:
        * Project files and configurations for the rest of the projects.
    * data:
        * Most of the directories contain data used by unit tests of our porting layer. the layout_tests directory is WebKit's layout test suite that we pull directly from Apple.
    * glue:
        * The glue layer is the embedding layer. It converts between Webcore types and our application's types (mostly STL), and provides more convenient methods that mirror a lot of Webcore's objects we need access to.
    * tools:
        * layout_tests: Scripts for running WebCore's layout tests.
        * merge: Scripts for helping merge to WebKit's tree.
        * npapi_layout_test_plugin: A special plug-in used by some of our tests to exercise the plugin layer.
        * test_shell: A very simple standalone browser. This allows testing of our glue and port code without having to compile and run the very large Chromium application.

* [How Chromium Displays Web Pages - The Chromium Projects](https://www.chromium.org/developers/design-documents/displaying-a-web-page-in-chrome)
* [Multi-process Architecture - The Chromium Projects](https://www.chromium.org/developers/design-documents/multi-process-architecture)
* [Design Documents - The Chromium Projects](https://www.chromium.org/developers/design-documents)

## Reference

Hi Ryan, thank you for the kind message! It was intresting opportunity to be involeved with your well-maintained pipelines. I'll reach out to you if I need some help. Thank you :)
