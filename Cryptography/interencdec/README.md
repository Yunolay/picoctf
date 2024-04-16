# interencdec

Tags: picoCTF 2024, Cryptography, base64, browser_webshell_solvable, caesar

| Author | Point    |
| ------ | -------- |
| NGIRIMANA SCHADRACK | 50 points |

## Description

## Hints

1. Engaging in various decoding processes is of utmost importance

## Solve

Looks like a base64 encoded string.

```bash
$ cat enc_flag 
YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgyeG9OakJzTURCcGZRPT0nCg==

$cat enc_flag | base64 -d  
b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2xoNjBsMDBpfQ=='

$ echo d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2xoNjBsMDBpfQ== | base64 -d
wpjvJAM{jhlzhy_k3jy9wa3k_lh60l00i}%   
```

Looks like a caesar cipher.

https://cyberchef.io/#recipe=ROT13(true,true,false,19)&input=d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2xoNjBsMDBpfQ

## Flag

```
picoCTF{caesar_d3cr9pt3d_********}
```

