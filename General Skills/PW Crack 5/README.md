# PW Crack 5

Tags: Beginner picoMini 2022, General Skills, password_cracking, hashing

| Author | Point    |
| ------ | -------- |
| LT 'SYREAL' JONES | 100 points |

## Description

Can you crack the password to get the flag?  
Download the password checker here and you'll need the encrypted flag and the hash in the same directory too. Here's a dictionary with all possible passwords based on the password conventions we've seen so far.

## Solve

dictionary.txt is given.

```python
import hashlib

### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################

flag_enc = open('level5.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level5.hash.bin', 'rb').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


def level_5_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_5_pw_check()
```

Create a simple solver and send a list of passwords in order to standard input.

```python
import subprocess

with open("./dictionary.txt", "r") as file:
    for input_str in file:
        input_str = input_str.rstrip()
        process = subprocess.Popen(['python3', 'level5.py'], stdin=subprocess.PIPE, text=True)
        process.stdin.write(input_str + "\n")
        process.stdin.flush()

process.stdin.close()

process.wait()
```

As a result, a flag will be displayed when the correct password is entered.

```bash
$ python3 solver.py | grep pico
picoCTF{h45h_sl1ng1ng_********}
```