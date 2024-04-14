# Obedient Cat

Tags: picoCTF2021, General Skills

| Author | Point    |
| ------ | -------- |
| SYREAL | 5 points |

## Description

This file has a flag in plain sight (aka "in-the-clear"). Download flag.

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
