# First Grep

Tags: picoCTF 2019, General Skills

| Author | Point    |
| ------ | -------- |
| ALEX FULTON/DANNY TUNITIS | 100 points |

## Description

Can you find the flag in file? This would be really tedious to look through manually, something tells me there is a better way.

## Solve

Just grep.

```bash
$ cat file | grep pico
picoCTF{grep_is_good_to_find_things_******}
```