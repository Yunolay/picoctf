# strings it

Tags: picoCTF 2019, General Skills

| Author | Point    |
| ------ | -------- |
| SANJAY C/DANNY TUNITIS | 100 points |

## Description

Can you find the flag in file without running it?

## Solve

Find out what the file is using the file command.

```bash
$ file strings                                                                                                                     
strings: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=047a5079a5f563cd0e540d28f42a37161093ffda, not stripped
```

Extract the strings in the binary using the strings command.  
Use the grep command to output only strings containing flags.

```bash
$ strings strings | grep pico
picoCTF{5tRIng5_1T_********}
```