# PW Crack 2

Tags: Beginner, General Skills, password_cracking

| Author | Point    |
| ------ | -------- |
| LT 'SYREAL' JONES | 100 points |

## Description

Can you crack the password to get the flag?  
Download the password checker here and you'll need the encrypted flag in the same directory too.

## Solve

The password is clearly chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39).

```python
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

flag_enc = open('level2.flag.txt.enc', 'rb').read()



def level_2_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39) ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_2_pw_check()
```

Outputs chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39) as a string.

```bash
python3 -c 'print(chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39))'
4ec9
```

Use "4ec9" for password.

```bash
python3 level2.py            
Please enter correct password for flag: 4ec9
Welcome back... your flag, user:
picoCTF{tr45h_51ng1ng_********}
```

