---
title: gdb command
---

## gdb command

```
file <filename>
```

* read symbol from filename


## breakpoints
```
break
```

```
(gdb) info breakpoints
Num     Type           Disp Enb Address    What
1       breakpoint     keep y   <PENDING>  dbqagse
2       breakpoint     keep y   <PENDING>  dqagse
3       breakpoint     keep y   <PENDING>  dqagse*
```

* Num
    * Breakpoint Numbers
* Type
    * Breakpoint, watchpoint, or catchpoint.
* Disposition
    * Whether the breakpoint is marked to be disabled or deleted when hit.
* Enb
    * Enabled or Disabled
    * `y` or `n`
* Address
    * Where the breakpoint is in your program, as a memory address.
* What
    * Where the breakpoint is in the source for your program, as a file and line number.


## Reference
[Debugging with GDB \- GDB Files](https://ftp.gnu.org/old-gnu/Manuals/gdb/html_chapter/gdb_14.html)
[Debugging with GDB \- Set Breaks](ftp://ftp.gnu.org/old-gnu/Manuals/gdb/html_node/gdb_28.html#SEC29)
