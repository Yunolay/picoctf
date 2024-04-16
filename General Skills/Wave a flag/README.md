# Wave a flag

Tags: picoCTF 2021, General Skills

| Author | Point    |
| ------ | -------- |
| SYREAL | 10 points |

## Description

Can you invoke help flags for a tool or binary? This program has extraordinarily helpful information...

## Hints

1. This program will only work in the webshell or another Linux computer.
2. To get the file accessible in your shell, enter the following in the Terminal prompt: $ wget https://mercury.picoctf.net/static/f95b1ee9f29d631d99073e34703a2826/warm
3. Run this program by entering the following in the Terminal prompt: $ ./warm, but you'll first have to make it executable with $ chmod +x warm
4. -h and --help are the most common arguments to give to programs to get more information from them!
5. Not every program implements help features like -h and --help.

## Solve

Find out what the file is using the file command.

```bash
$ file warm
warm: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=01b148cdedfc38125cac0d87e0537466d47927b1, with debug_info, not stripped
```

This is an ELF 64-bit binary file.


Extract the strings in the binary using the strings command.  
Use the grep command to output only strings containing flags.

```bash
$ strings warm | grep pico
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_********}
```

## Flag

```
picoCTF{b1scu1ts_4nd_gr4vy_********}
```