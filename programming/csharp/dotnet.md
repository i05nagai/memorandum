---
title: dotnet
---

## dotnet

## Install on OSX

```
brew install dotnet@8

==> dotnet@8
For other software to find dotnet you may need to set:
  export DOTNET_ROOT="/opt/homebrew/opt/dotnet@8/libexec"

dotnet@8 is keg-only, which means it was not symlinked into /opt/homebrew,
because this is an alternate version of another formula.

If you need to have dotnet@8 first in your PATH, run:
  echo 'export PATH="/opt/homebrew/opt/dotnet@8/bin:$PATH"' >> ~/.zshrc

zsh completions have been installed to:
  /opt/homebrew/opt/dotnet@8/share/zsh/site-functions

```

```
export DOTNET_ROOT="/opt/homebrew/opt/dotnet@8/libexec"
export PATH="/opt/homebrew/opt/dotnet@8/bin:$PATH"
export DOTNET_MSBUILD_SDK_RESOLVER_SDKS_VER=8.0.114
export DOTNET_MSBUILD_SDK_RESOLVER_SDKS_DIR=$DOTNET_ROOT/sdk/${DOTNET_MSBUILD_SDK_RESOLVER_SDKS_VER}
export DOTNET_MSBUILD_SDK_RESOLVER_CLI_DIR=$DOTNET_ROOT/
```



## Reference
