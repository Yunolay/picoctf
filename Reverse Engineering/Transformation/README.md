# Transformation

Tags: picoCTF 2021, Reverse Engineering

| Author | Point    |
| ------ | -------- |
| MADSTACKS | 20 points |

## Description

I wonder what this really is... enc ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

## Hint

1. You may find some decoders online  
-> http://guanine.evolbio.mpg.de/cgi-bin/bwt/bwt.cgi.pl

## Solve

```bash
$ file enc
enc: Unicode text, UTF-8 text, with no line terminators

$ cat enc    
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽
```

solver.py

```python
enc = open("enc").read()
flag = ''

for i in range(0, len(enc)):
    c1 = chr((ord(enc[i]) >> 8))
    flag += c1

    c2 = chr(enc[i].encode('utf-16be')[-1])
    flag += c2

print(flag)
```

```bash
$ python3 solver.py                                                                                                
picoCTF{16_bits_inst34d_of_8_********}
```

## Flag

```
picoCTF{16_bits_inst34d_of_8_********}
```