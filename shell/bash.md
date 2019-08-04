---
title: Bash
---

## Bash

#### Here string

```
bc <<< 4*5
# equivalent
echo "4*5" | bc
```

## Tips

### interactive shell vs non-interactive shell
* [Interactive and non-interactive shells and scripts](https://www.tldp.org/LDP/abs/html/intandnonint.html)

* A shell running a script is always a non-interactive shell

### /etc/profile /etc/profile.d
* [bash - What do the scripts in /etc/profile.d do? - Unix & Linux Stack Exchange](https://unix.stackexchange.com/questions/64258/what-do-the-scripts-in-etc-profile-d-do)
* [bash - Scripts in /etc/profile.d Being Ignored? - Ask Ubuntu](https://askubuntu.com/questions/438150/scripts-in-etc-profile-d-being-ignored)
* [Understanding a little more about /etc/profile and /etc/bashrc | Benjamin Cane](http://bencane.com/2013/09/16/understanding-a-little-more-about-etcprofile-and-etcbashrc/)

interactive shellかどうかなどで読み込まれるかどうかがかわる。


* /etc/profile
    * Bash shellの開始時に 環境変数をset
    * system wide version of `.bash_profile`
* /etc/profile.d
    * bash shellの開始時に読み込まれる
    * application固有のenvironment variableをset
    * is executed for interactive shell
* `/etc/bashrc`
* `/etc/bash.bashrc`
    * ubuntu
    * is executed for both interactive and non-interactive

## Shell Parameter Expansion
* [【シェル芸人への道】Bashの変数展開と真摯に向き合う - Qiita](https://qiita.com/t_nakayama0714/items/80b4c94de43643f4be51)


## Precedence
* [bash - Precedence of the shell logical operators &&, || - Unix & Linux Stack Exchange](https://unix.stackexchange.com/questions/88850/precedence-of-the-shell-logical-operators)

* &&, ||
    * same precedence
    * left associative

## Bash variablaes
* [Bash Reference Manual: Bash Variables](https://www.gnu.org/software/bash/manual/html_node/Bash-Variables.html)


* BASH_SOURCE
    * array
    * source filename `${FUNCNAME[$i]}`
    * corresponding shell function name in FUNCNAME array
    * `${FUNCNAME[$i]}` is defined in `${BASH_SOURCE[$i]}`
    * `${FUNCNAME[$i]}` is called from `${BASH_SOURCE[$i+1]}`
    * `$0`は`source`で変更されないが、`BASH_SOURCE`はsourceされるとsource先が0番目にpushされる

## Conditoinal expressions

* `[[ expression ]]`
    * `=`, `==` は同じいみ
    * `==`, `!=`
        * 右辺を [Pattern-maching](https://tiswww.case.edu/php/chet/bash/bashref.html#Pattern-Matching)として評価
    * `=~`を含むかどうか
        * 右辺をregex3で評価

## Prompt
- [Bash/Prompt customization \- ArchWiki](https://wiki.archlinux.org/index.php/Bash/Prompt_customization)
- [ANSI escape code \- Wikipedia](https://en.wikipedia.org/wiki/ANSI_escape_code)

- `\u`
    - current user
- `\A`
    - current time
* `\a`
    * an ASCII bell character (07)
* `\d`
    * the date in "Weekday Month Date" format (e.g., "Tue May 26")
* `\D{format}`
    * the  format  is passed to strftime(3) and the result is inserted into the prompt string; an empty format results in a locale-specific time representation.  The braces are required
* `\e`
    * an ASCII escape character (033)
* `\h`
    * the hostname up to the first `.`
* `\H`
    * the hostname
* `\j`
    * the number of jobs currently managed by the shell
* `\l`
    * the basename of the shell's terminal device name
* `\n`
    * newline
* `\r`
    * carriage return
* `\s`
    * the name of the shell, the basename of `$0` (the portion following the final slash)
* `\t`
    * the current time in 24-hour HH:MM:SS format
* `\T`
    * the current time in 12-hour HH:MM:SS format
* `\@`
    * the current time in 12-hour am/pm format
* `\A`
    * the current time in 24-hour HH:MM format
* `\u`
    * the username of the current user
* `\v`
    * the version of bash (e.g., 2.00)
* `\V`
    * the release of bash, version + patch level (e.g., 2.00.0)
* `\w`
    * the current working directory, with `$HOME` abbreviated with a tilde
* `\W`
    * the basename of the current working directory, with `$HOME` abbreviated with a tilde
* `\!`
    * the history number of this command
* `\#`
    * the command number of this command
* `\$`
    * if the effective UID is 0, a #, otherwise a `$`
* `\nnn`
    * the character corresponding to the octal number nnn
* `\\`
    * a backslash
* `\[`
    * begin a sequence of non-printing characters, which could be used to embed a terminal control sequence into the prompt
* `\]`
    * end a sequence of non-printing characters

- `PS1`
    - is the primary prompt which is displayed before each command, thus it is the one most people customize.
- `PS2`
    - is the secondary prompt displayed when a command needs more input (e.g. a multi-line command).
- `PS3`
    - is not very commonly used. It is the prompt displayed for Bash's select built-in which displays interactive menus. Unlike the other prompts, it does not expand Bash escape sequences. Usually you would customize it in the script where the select is used rather than in your .bashrc.
- `PS4`
    - is also not commonly used. It is displayed when debugging bash scripts to indicate levels of indirection. The first character is repeated to indicate deeper levels.


```shell
# show list of supported background color
for C in {0..255}; do
    tput setab $C
    echo -n "$C "
done
tput sgr0
echo
```

```shell
# show list of supported foreground color
for C in {0..255}; do
    tput setaf $C
    echo -n "$C "
done
tput sgr0
echo
```

## Tips

#### bash with spaces
[shell \- Passing an array with spaces to a Bash function to act as its list of arguments \- Stack Overflow](https://stackoverflow.com/questions/18981748/passing-an-array-with-spaces-to-a-bash-function-to-act-as-its-list-of-arguments)
[Bash array with spaces in elements \- Stack Overflow](https://stackoverflow.com/questions/9084257/bash-array-with-spaces-in-elements)

```bash
function foobar() {
  local FILES=("$@")
  for ((i = 0; i < ${#FILES[@]}; i++))
  do
    echo "${FILES[$i]}"
  done
}
FILELIST=(
"envs/osx/.bin" ".bin"
"envs/osx/.tmux.conf.env" ".tmux.conf.env"
"envs/osx/.zshrc.env" ".zshrc.env"
"vscode/Code" "Library/Application Support/Code"
)
foobar "${FILELIST[@]}"
```

#### shopt
- https://www.gnu.org/software/bash/manual/html_node/The-Shopt-Builtin.html

## Reference
* [bash\(1\): GNU Bourne\-Again SHell \- Linux man page](https://linux.die.net/man/1/bash)
