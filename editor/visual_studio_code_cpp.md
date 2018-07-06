---
title: Visual Studio Code cpp
---

## Visual Studio Code cpp
Install Microsoft C/C++ extension.
Do not forget to compile with `-g` option.

## Configuration
Generated for each workspace.
Directory `.vsocode` is created in the root of workspace.

* `.vscode`
    * `c_cpp_properties.json`
        * Open command pallet and run `C/Cpp: Edit configurations...`
    * `tasks.json`
        * build your own code
        * Command Palette run `Tasks: Configure Tasks..`. Then Create `tasks.json` file from templates
    * `launch.json`
        * debugging
        * `Debug->Configurre`
    * `settings.json`

## Debugging
* Linux: GDB
* macOS: LLDB or GDB
* Windows: the Visual Studio Windows Debugger or GDB (using Cygwin or MinGW)

## Keymap
* `Ctrl+Shift+O`
* `Ctrl+T`
    * search
    * Search symbos
        * Start with `#`
    * Search file
        * Start with blank
* `Ctrl+P`
* `Ctrl+Shift+F10`
    * Peek definition
* `F12`
    * Go to definition


## Reference
* [C\+\+ programming with Visual Studio Code](https://code.visualstudio.com/docs/languages/cpp)
* [vscode\-cpptools/Getting started with IntelliSense configuration\.md at master · Microsoft/vscode\-cpptools](https://github.com/Microsoft/vscode-cpptools/blob/master/Documentation/Getting%20started%20with%20IntelliSense%20configuration.md)
