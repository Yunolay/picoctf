# basic-mod1

Tags: picoCTF 2022, Cryptography

| Author | Point    |
| ------ | -------- |
| WILL HONG | 100 points |

## Description

We found this weird message being passed around on the servers, we think we have a working decryption scheme.
Download the message here.  
Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.  
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})  

## Hints

1. Do you know what mod 37 means?
2. mod 37 means modulo 37. It gives the remainder of a number after being divided by 37.

## Solve

message.txt will be given.

```bash
$ cat message.txt         
128 322 353 235 336 73 198 332 202 285 57 87 262 221 218 405 335 101 256 227 112 140
```

Calculate using a python script according to the problem statement.

```python
num = open('./message.txt', 'r')
nums = num.read().split()

flag = ''
for i in nums:
    mod_val = int(i) % 37
    if 0 <= mod_val <= 25:
        # Map 0-25 to 'A'-'Z'
        flag += chr(mod_val + 65)
    elif 26 <= mod_val <= 35:
        # Map 26-35 to '0'-'9'
        flag += chr(mod_val + 22)  # 22 = 48 (ASCII code for '0') - 26
    elif mod_val == 36:
        # Map 36 to '_'
        flag += '_'

print(f'picoCTF{{{flag}}}')
```

Run it and we will get the flag.

```bash
$ python3 solver.py
picoCTF{R0UND_N_R0UND_********}
```

## Flag

```
picoCTF{R0UND_N_R0UND_********}
```