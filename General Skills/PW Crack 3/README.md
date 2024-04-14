# PW Crack 3

Tags: Beginner picoMini 2022, General Skills, password_cracking, hashing

| Author | Point    |
| ------ | -------- |
| LT 'SYREAL' JONES | 100 points |

## Description

Can you crack the password to get the flag?  
Download the password checker here and you'll need the encrypted flag and the hash in the same directory too.  
There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.  

## Solve

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

flag_enc = open('level3.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level3.hash.bin', 'rb').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


def level_3_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_3_pw_check()


# The strings below are 7 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"]
```

The password is apparently one of "8799", "d3ab", "1ea2", "acaf", "2295", "a9de", or "6f3d".

Create a simple solver and send a list of passwords in order to standard input.

```python
import subprocess

inputs = ["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"]

for input_str in inputs:
    process = subprocess.Popen(['python3', 'level3.py'], stdin=subprocess.PIPE, text=True)
    process.stdin.write(input_str + "\n")
    process.stdin.flush()

process.stdin.close()

process.wait()
```

```bash
$ python3 solver.py
'Please enter correct password for flag: That password is incorrect
Please enter correct password for flag: That password is incorrect
Please enter correct password for flag: That password is incorrect
Please enter correct password for flag: That password is incorrect
Please enter correct password for flag: Welcome back... your flag, user:
picoCTF{m45h_fl1ng1ng_********}
Please enter correct password for flag: That password is incorrect
Please enter correct password for flag: That password is incorrect
```

## Flag

```
picoCTF{m45h_fl1ng1ng_********}
```
