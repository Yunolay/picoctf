# convertme.py

Tags: picoMini 2022, General Skills, base, Python

| Author | Point    |
| ------ | -------- |
| LT 'SYREAL' JONES | 100 points |

## Description

Run the Python script and convert the given number from decimal to binary to get the flag.

## Solve

If we look at the script, it's clearly xored with "enkidu".

```python
import random

def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])


flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x5f) + chr(0x05) + chr(0x08) + chr(0x2a) + chr(0x1c) + chr(0x5e) + chr(0x1e) + chr(0x1b) + chr(0x3b) + chr(0x17) + chr(0x51) + chr(0x5b) + chr(0x58) + chr(0x5c) + chr(0x3b) + chr(0x4c) + chr(0x06) + chr(0x5d) + chr(0x09) + chr(0x5e) + chr(0x00) + chr(0x41) + chr(0x01) + chr(0x13)


num = random.choice(range(10,101))

print('If ' + str(num) + ' is in decimal base, what is it in binary base?')

ans = input('Answer: ')

try:
  ans_num = int(ans, base=2)
  
  if ans_num == num:
    flag = str_xor(flag_enc, 'enkidu')
    print('That is correct! Here\'s your flag: ' + flag)
  else:
    print(str(ans_num) + ' and ' + str(num) + ' are not equal.')
    flag = str_xor(flag_enc, 'enkidu')
    print('Here\'s your flag: ' + flag)
  
except ValueError:
  print('That isn\'t a binary number. Binary numbers contain only 1\'s and 0\'s')
```

Rewrite the script to call flag = str_xor(flag_enc, 'enkidu') even if you enter a wrong answer.

```python
try:
  ans_num = int(ans, base=2)
  
  if ans_num == num:
    flag = str_xor(flag_enc, 'enkidu')
    print('That is correct! Here\'s your flag: ' + flag)
  else:
    print(str(ans_num) + ' and ' + str(num) + ' are not equal.')
    flag = str_xor(flag_enc, 'enkidu') # Add
    print('Here\'s your flag: ' + flag) # Add 
```

Enter 1 because you do not want to include except.

```bash
$ python3 convertme.py
If 69 is in decimal base, what is it in binary base?
Answer: 1
1 and 69 are not equal.
Here's your flag: picoCTF{4ll_y0ur_b4535_********}
```

## Flag

```
picoCTF{4ll_y0ur_b4535_********}
```

