# Python Wrangling

Tags: picoCTF 2021, General Skills

| Author | Point    |
| ------ | -------- |
| SYREAL | 10 points |

## Description

Python scripts are invoked kind of like programs in the Terminal... Can you run this Python script using this password to get the flag?

ende.py
```python
import sys
import base64
from cryptography.fernet import Fernet



usage_msg = "Usage: "+ sys.argv[0] +" (-e/-d) [file]"
help_msg = usage_msg + "\n" +\
        "Examples:\n" +\
        "  To decrypt a file named 'pole.txt', do: " +\
        "'$ python "+ sys.argv[0] +" -d pole.txt'\n"



if len(sys.argv) < 2 or len(sys.argv) > 4:
    print(usage_msg)
    sys.exit(1)



if sys.argv[1] == "-e":
    if len(sys.argv) < 4:
        sim_sala_bim = input("Please enter the password:")
    else:
        sim_sala_bim = sys.argv[3]

    ssb_b64 = base64.b64encode(sim_sala_bim.encode())
    c = Fernet(ssb_b64)

    with open(sys.argv[2], "rb") as f:
        data = f.read()
        data_c = c.encrypt(data)
        sys.stdout.write(data_c.decode())


elif sys.argv[1] == "-d":
    if len(sys.argv) < 4:
        sim_sala_bim = input("Please enter the password:")
    else:
        sim_sala_bim = sys.argv[3]

    ssb_b64 = base64.b64encode(sim_sala_bim.encode())
    c = Fernet(ssb_b64)

    with open(sys.argv[2], "r") as f:
        data = f.read()
        data_c = c.decrypt(data.encode())
        sys.stdout.buffer.write(data_c)


elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print(help_msg)
    sys.exit(1)


else:
    print("Unrecognized first argument: "+ sys.argv[1])
    print("Please use '-e', '-d', or '-h'.")
```

We will be given a text file containing the encrypted flag and password.

```bash
$ cat pw.txt
ac9bd0ffac9bd0ffac9bd0ffac9bd0ff
                                                                                                                                                                         15:39:02
$ cat flag.txt.en
gAAAAABgUAIWIvSiR0W23DAHIK5DX6Y4BvwES94M_XdDcNAquhp-A0D2z8n812YEXaSD9WhoweBh2cm5Wa0cqzuW0Kc7fOct0OJnpOmVF8A91j0Hx4dKtvk3l5ghPT71Y7GxErPRyJUs%
```

Check the usage of python script.

```bash
$ python3 ende.py
Usage: ende.py (-e/-d) [file]
```

We can encrypt and decrypt using this python script.  
Decrypt using the password provided in pw.txt.

```bash
$ python3 ende.py -d flag.txt.en
Please enter the password:ac9bd0ffac9bd0ffac9bd0ffac9bd0ff
picoCTF{4p0110_1n_7h3_h0us3_********}
```