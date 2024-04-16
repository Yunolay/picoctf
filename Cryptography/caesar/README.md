# caesar

Tags: picoCTF 2019, cryptography

| Author | Point    |
| ------ | -------- |
| SANJAY C/DANIEL TUNITIS | 100 points |

## Description

Decrypt this message.

## Hints

1. caesar cipher tutorial

## Solve

```bash
$ cat ciphertext
picoCTF{dspttjohuifsvcjdpoabrkttds}
```

Decrypt with rot25 using cyberchef.

https://cyberchef.io/#recipe=ROT13(true,true,false,25)&input=ZHNwdHRqb2h1aWZzdmNqZHBvYWJya3R0ZHM

## Flag

```
picoCTF{crossingtherubiconza*****}
```