---
title: swig
---

## swig


## CLI

Supported Target Language Options

- -csharp         - Generate C# wrappers
- -d              - Generate D wrappers
- -go             - Generate Go wrappers
- -guile          - Generate Guile wrappers
- -java           - Generate Java wrappers
- -javascript     - Generate Javascript wrappers
- -lua            - Generate Lua wrappers
- -octave         - Generate Octave wrappers
- -perl5          - Generate Perl 5 wrappers
- -php7           - Generate PHP 7 wrappers
- -python         - Generate Python wrappers
- -r              - Generate R (aka GNU S) wrappers
- -ruby           - Generate Ruby wrappers
- -scilab         - Generate Scilab wrappers
- -tcl8           - Generate Tcl 8 wrappers
- -xml            - Generate XML wrappers


Experimental Target Language Options

- mzscheme       - Generate MzScheme/Racket wrappers
- ocaml          - Generate OCaml wrappers

General Options

-addextern      - Add extra extern declarations
-c++            - Enable C++ processing
-co <file>      - Check <file> out of the SWIG library
-copyctor       - Automatically generate copy constructors wherever possible
-cpperraswarn   - Treat the preprocessor #error statement as #warning (default)

* -cppext <ext>   - Change file extension of generated C++ files to <ext> (default is cxx)
-copyright      - Display copyright notices
-debug-classes  - Display information about the classes found in the interface
-debug-module <n>- Display module parse tree at stages 1-4, <n> is a csv list of stages
-debug-symtabs  - Display symbol tables information
-debug-symbols  - Display target language symbols in the symbol tables
-debug-csymbols - Display C symbols in the symbol tables
-debug-lsymbols - Display target language layer symbols
-debug-tags     - Display information about the tags found in the interface
-debug-template - Display information for debugging templates
-debug-top <n>  - Display entire parse tree at stages 1-4, <n> is a csv list of stages
-debug-typedef  - Display information about the types and typedefs in the interface
-debug-typemap  - Display typemap debugging information
-debug-tmsearch - Display typemap search debugging information
-debug-tmused   - Display typemaps used debugging information
-directors      - Turn on director mode for all the classes, mainly for testing
-dirprot        - Turn on wrapping of protected members for director classes (default)
-D<symbol>      - Define a symbol <symbol> (for conditional compilation)
-E              - Preprocess only, does not generate wrapper code
-external-runtime [file] - Export the SWIG runtime stack
-fakeversion <v>- Make SWIG fake the program version number to <v>
-fcompact       - Compile in compact mode
-features <list>- Set global features, where <list> is a comma separated list of
               features, eg -features directors,autodoc=1
               If no explicit value is given to the feature, a default of 1 is used

-fastdispatch   - Enable fast dispatch mode to produce faster overload dispatcher code
-Fmicrosoft     - Display error/warning messages in Microsoft format
-Fstandard      - Display error/warning messages in commonly used format
-fvirtual       - Compile in virtual elimination mode
-help           - Display help
-I-             - Don't search the current directory
-I<dir>         - Look for SWIG files in directory <dir>
-ignoremissing  - Ignore missing include files
-importall      - Follow all #include statements as imports
-includeall     - Follow all #include statements
-l<ifile>       - Include SWIG library file <ifile>
-macroerrors    - Report errors inside macros
-makedefault    - Create default constructors/destructors (the default)
-M              - List all dependencies
-MD             - Is equivalent to `-M -MF <file>`, except `-E` is not implied
-MF <file>      - Generate dependencies into <file> and continue generating wrappers
-MM             - List dependencies, but omit files in SWIG library
-MMD            - Like `-MD`, but omit files in SWIG library
-module <name>  - Set module name to <name>
-MP             - Generate phony targets for all dependencies
-MT <target>    - Set the target of the rule emitted by dependency generation
-nocontract     - Turn off contract checking
-nocpperraswarn - Do not treat the preprocessor #error statement as #warning
-nodefault      - Do not generate default constructors nor default destructors
-nodefaultctor  - Do not generate implicit default constructors
-nodefaultdtor  - Do not generate implicit default destructors
-nodirprot      - Do not wrap director protected members
-noexcept       - Do not wrap exception specifiers
-nofastdispatch - Disable fast dispatch mode (default)
-nopreprocess   - Skip the preprocessor step
-notemplatereduce - Disable reduction of the typedefs in templates
* -O              - Enable the optimization options:
    * -fastdispatch -fvirtual
* -o <outfile>    - Set name of C/C++ output file to <outfile>
* -oh <headfile>  - Set name of C++ output header file for directors to <headfile>
* -outcurrentdir  - Set default output dir to current dir instead of input file's path
* -outdir <dir>   - Set language specific files output directory to <dir>
* -pcreversion    - Display PCRE version information
* -small          - Compile in virtual elimination and compact mode
* -swiglib        - Report location of SWIG library and exit
* -templatereduce - Reduce all the typedefs in templates
* -v              - Run in verbose mode
* -version        - Display SWIG version number
* -Wall           - Remove all warning suppression, also implies -Wextra
* -Wallkw         - Enable keyword warnings for all the supported languages
* -Werror         - Treat warnings as errors
* -Wextra         - Adds the following additional warnings: 202,309,403,405,512,321,322
* -w<list>        - Suppress/add warning messages, eg -w401,+321 - see Warnings.html
* -xmlout <file>  - Write XML version of the parse tree to <file> after normal processing


## Tips
Options can also be defined using the SWIG_FEATURES environment variable, for example:

```
$ SWIG_FEATURES="-Wall"
$ export SWIG_FEATURES
$ swig -python interface.i
```

is equivalent to:

```
$ swig -Wall -python interface.i
```

```
$ echo "-Wall -python interface.i" > args.txt
$ swig @args.txt
```

## Reference
