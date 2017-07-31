---
title:
---

## Install

### OSX
OSXはxcodeのcommadline toolsがいれるものと競合する。
homebrewなどで入れた時には明示的にパスを通す必要がある。

```
brew install llvm
```

以下のようなものが出力される。
インストールしたものを使う場合は、

```sh
echo 'export LDFLAGS="-L/usr/local/opt/llvm/lib -Wl,-rpath,/usr/local/opt/llvm/lib $LDFLAGS"' >> ~/.zshrc
echo 'export PATH="/usr/local/opt/llvm/bin:$PATH"' >> ~/.zshrc
```

などとする。

```
==> Downloading https://homebrew.bintray.com/bottles/libffi-3.2.1.el_capitan.bottle.tar.gz
######################################################################## 100.0%
==> Pouring libffi-3.2.1.el_capitan.bottle.tar.gz
==> Caveats
This formula is keg-only, which means it was not symlinked into /usr/local.

Some formulae require a newer version of libffi.

For compilers to find this software you may need to set:
    LDFLAGS:  -L/usr/local/opt/libffi/lib
For pkg-config to find this software you may need to set:
    PKG_CONFIG_PATH: /usr/local/opt/libffi/lib/pkgconfig

==> Summary
🍺  /usr/local/Cellar/libffi/3.2.1: 16 files, 296.9KB
==> Installing llvm
==> Downloading https://homebrew.bintray.com/bottles/llvm-4.0.0.el_capitan.bottle.tar.gz
######################################################################## 100.0%
==> Pouring llvm-4.0.0.el_capitan.bottle.tar.gz
==> Caveats
LLVM executables are installed in /usr/local/opt/llvm/bin.
Extra tools are installed in /usr/local/opt/llvm/share/llvm.
To use the bundled libc++ please add the following LDFLAGS:
  LDFLAGS="-L/usr/local/opt/llvm/lib -Wl,-rpath,/usr/local/opt/llvm/lib"

This formula is keg-only, which means it was not symlinked into /usr/local.

macOS already provides this software and installing another version in
parallel can cause all kinds of trouble.

If you need to have this software first in your PATH run:
  echo 'export PATH="/usr/local/opt/llvm/bin:$PATH"' >> ~/.zshrc

For compilers to find this software you may need to set:
    LDFLAGS:  -L/usr/local/opt/llvm/lib
    CPPFLAGS: -I/usr/local/opt/llvm/include

If you need Python to find bindings for this keg-only formula, run:
  echo /usr/local/opt/llvm/lib/python2.7/site-packages >> /usr/local/lib/python2.7/site-packages/llvm.pth
  mkdir -p /Users/admin/.local/lib/python3.5/site-packages
  echo 'import site; site.addsitedir("/usr/local/lib/python2.7/site-packages")' >> /Users/admin/.local/lib/python3.5/site-packages/homebrew.pth
==> Summary
🍺  /usr/local/Cellar/llvm/4.0.0: 2,245 files, 1GB
```
