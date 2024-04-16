# file-run1

Tags: picoCTF 2022, Reverse Engineering

| Author | Point    |
| ------ | -------- |
| WILL HONG | 100 points |

## Description

A program has been provided to you, what happens if you try to run it on the command line?  
Download the program here.

## Hints

1. To run the program at all, you must make it executable (i.e. $ chmod +x run)
2. Try running it by adding a '.' in front of the path to the file (i.e. $ ./run)

## Solve

Check the file using the file command.  
We can see that the result is ELF 64-bit.

```bash                                                        20:15:01
$ file run      
run: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=4d8e230e54db29e0879e7ed9f2b2231eb8c60032, for GNU/Linux 3.2.0, not stripped
```

Extract the flag string using the strings command.

```bash
$ strings run | grep pico       
picoCTF{U51N6_Y0Ur_F1r57_F113_********}
```

## Flag

```
picoCTF{U51N6_Y0Ur_F1r57_F113_********}
```