---
title: ReStructuredText
---

## ReStructuredText

## Install

```
pip install sphinx sphinx-autobuild
pip install doc8
```

```
# for rst2html
pip install docutils
```

## Configuration
* [Configuration — restructuredtext 1\.0 documentation](https://docs.restructuredtext.net/articles/configuration.html)

If it is "", then rst2html.py is used to render the preview page.
If it is a valid folder, then conf.py from that folder is used by Sphinx to render the preview page.
If it is not set, then this extension shows a list of options before generating a preview page.

## kyebind
* `Cmd+shift+r`
    * `ctrl+shift+r`
    * preview
* `Cmd+k Cmd+r`
    * `ctrl+k ctrl+r`
    * preview to side

Linting is available if `doc8` is installed.

## Reference
* [vscode\-restructuredtext/vscode\-restructuredtext: reStructuredText Language Support in Visual Studio Code](https://github.com/vscode-restructuredtext/vscode-restructuredtext)
* [reStructuredText \- Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext)
* [reStructuredText Extension for Visual Studio Code — restructuredtext 1\.0 documentation](https://docs.restructuredtext.net/)
