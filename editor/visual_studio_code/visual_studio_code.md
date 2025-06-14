---
title: Visual Studio Code
---

## Visual Studio Code

## Install

```
brew cask install visual-studio-code
```

For ubuntu 16.04,

```
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt-get update
sudo apt-get install code # or code-insiders
```

## Settings
* Windows
    * `%APPDATA%\Code\User\settings.json`
* Mac
    * `$HOME/Library/Application Support/Code/User/settings.json`
* Linux
    * `$HOME/.config/Code/User/settings.json`

## Go
Debug

* go fileを開く
* Debug -> Open configuration
* `launch.json`が作成される
* `"env": {"GOPATH": "${env:GOPATH}"}`を追加する
* `${env:Name}`


## Keymarp

On linux,

* `Ctlr+Alt+-`
    * navigate back
* `Ctlr+Shift+-`
    * navigate fort

## Javascript
Install `tsd` file

```
npm install tsd -g
```

```
tsd install node --save
```

jsconfig

```
{
  "compilerOptions": {
    "target": "ES6",
    "module": "commonjs"
  }
}
```


## .vscode directory

#### settings.json
- Contains workspace-specific settings.
- Overrides user settings for only this workspace or folder.

Example use cases:
Turning on/off specific linters for just this project.
Customizing editor formats or auto-save behavior for a specific codebase.

#### launch.json
Holds debug configurations for your application.
Defines how to run or debug code for various environments (Node.js, Python, C#, etc.).

Example use cases:

Attaching a debugger to a running process.
Setting breakpoints and environment variables.

#### tasks.json
Defines tasks that can be run from the VS Code Task Runner (e.g., build scripts, test runners).

Example use cases:
Running a build command (npm run build or make build) directly from the integrated terminal with a single click/shortcut.
Automating code formatting, linting, or deployment scripts.

#### extensions.json
Specifies recommended or required extensions for your project.
When someone opens the project, VS Code can suggest installing these extensions for a better development experience.

#### Others

You can add other JSON files that certain extensions or tools might require.
For example, custom config files for third-party tools that integrate tightly with VS Code might be placed here.
Less common, but sometimes you’ll see specialized config files that follow this pattern if an extension specifically looks for them in .vsc

## Reference

