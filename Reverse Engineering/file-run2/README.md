# file-run2

Tags: picoCTF 2022, Reverse Engineering

| Author | Point    |
| ------ | -------- |
| WILL HONG | 100 points |

## Description

## Hints

1. Try running it and add the phrase "Hello!" with a space in front (i.e. "./run Hello!")

## Solve

Check the file using the file command.  
We can see that the result is ELF 64-bit.

```bash
$ file run
run: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=106bb01c6a4466da1f636e31c9167e8a3d18c89a, for GNU/Linux 3.2.0, not stripped
```

Extract the flag string using the strings command.

```bash
strings run | grep pico
picoCTF{F1r57_4rgum3n7_********}
```

## Flag

```
picoCTF{F1r57_4rgum3n7_********}
```