---
title: Visual Studio Code cpp
---

## Visual Studio Code cpp
Install Microsoft C/C++ extension.
Do not forget to compile with `-g` option when you debug.

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

## Building your code
* Open command pallets
* Select the `Tasks: Configure Task`
* Click the `Create tasks.json file from template`
* Select Others

## Debugging
* Linux: GDB
* macOS: LLDB or GDB
* Windows: the Visual Studio Windows Debugger or GDB (using Cygwin or MinGW)

## Keymap
[Code Navigation in Visual Studio Code](https://code.visualstudio.com/docs/editor/editingevolved)

* `Shift+Cmd+B`
    *  Tasks: Run Build Task
* `Cmd+Shift+P`
    * open command pallets
* `Ctrl+Shift+O`
    * go to symbol
* `Ctrl+T`
    * open symbol by name
    * search
    * Search symbos
        * Start with `#`
    * Search file
        * Start with blank
* `Shfit+F12`, `Option+F12`
    * Find all references, Peek Definition
* `Shift + Ctr + backslach`
    * Bracket matching
* `F2`
    * Rename symbol
* `Cmd + F12`
* `Shift + ctrl + M`
    * open problems panel
* `Ctrl+P`
    * file search
* `Ctrl+Shift+F10`
    * Peek definition
* `F12`
    * Go to definition

Command

* `Switch Header/Source`
    * from command pallet



## Reference
* [C\+\+ programming with Visual Studio Code](https://code.visualstudio.com/docs/languages/cpp)
* [vscode\-cpptools/Getting started with IntelliSense configuration\.md at master · Microsoft/vscode\-cpptools](https://github.com/Microsoft/vscode-cpptools/blob/master/Documentation/Getting%20started%20with%20IntelliSense%20configuration.md)
