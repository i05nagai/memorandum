---
title: asdf
---

## asdf

## asdf-java
- https://github.com/halcyon/asdf-java

```
asdf plugin-add java https://github.com/halcyon/asdf-java.git
```

```
asdf list-all java
```

Add the line below `.zshrc`

```
. ~/.asdf/plugins/java/set-java-home.zsh
```

OSX integration. Add the line below to `.asdfrc`

```
java_macos_integration_enable=yes
```

```
asdf install java openjdk-21
```

## asdf dotnet
https://stackoverflow.com/questions/70820780/vscode-or-anothers-editors-dont-recognize-sdk-dotnet-installed-with-asdf
vscode doest not recognize asdf dotnet

```
export DOTNET_MSBUILD_SDK_RESOLVER_SDKS_DIR=$(echo $HOME/.asdf/installs/dotnet-core/8.0.114/sdk/*/Sdks)
export DOTNET_MSBUILD_SDK_RESOLVER_SDKS_VER=8.0.114
export DOTNET_MSBUILD_SDK_RESOLVER_CLI_DIR=$(echo $HOME/.asdf/installs/dotnet-core/8.0.114)
```


## Reference
- https://asdf-vm.com/
