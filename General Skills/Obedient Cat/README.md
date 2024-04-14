# Obedient Cat

Tags: picoCTF2021, General Skills

| Author | Point    |
| ------ | -------- |
| SYREAL | 5 points |

## Description

This file has a flag in plain sight (aka "in-the-clear"). Download flag.

## Hints

1. Any hints about entering a command into the Terminal (such as the next one), will start with a '$'... everything after the dollar sign will be typed (or copy and pasted) into your Terminal.

2. To get the file accessible in your shell, enter the following in the Terminal prompt: $ wget https://mercury.picoctf.net/static/0e428b2db9788d31189329bed089ce98/flag

3. $ man cat

## Solve

Find out what the file is using the file command.

```bash
$ file flag
flag: ASCII text
```

Read the text of the file using the cat command.

```bash
$ cat flag
picoCTF{s4n1ty_v3r1f13d_********}
```
