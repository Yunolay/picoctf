# Glitch Cat

Tags:

| Author | Point    |
| ------ | -------- |
| LT 'SYREAL' JONES | 100 points |

## Description

Our flag printing service has started glitching!
$ nc saturn.picoctf.net 64817

## Solve

If we connect with nc, the middle of the flag and ASCII will be given.

```bash
$ nc saturn.picoctf.net 64817
'picoCTF{gl17ch_m3_n07_' + chr(0x61) + chr(0x34) + chr(0x33) + chr(0x39) + chr(0x32) + chr(0x64) + chr(0x32) + chr(0x65) + '}'
```

Convert to character with python oneliner.

```
python3 -c 'print(chr(0x61) + chr(0x34) + chr(0x33) + chr(0x39) + chr(0x32) + chr(0x64) + chr(0x32) + chr(0x65))'
********
```

## Flag

```
picoCTF{gl17ch_m3_n07_********}
```

