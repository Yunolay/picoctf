# Big Zip

Tags: picoGym Exclusive, General Skills

| Author | Point    |
| ------ | -------- |
| LT 'SYREAL' JONES | 100 points |

## Description

Unzip this archive and find the flag.

## Solve

Unzip the given zip file using the unzip command.

```bash
unzip big-zip-files.zip

[snip]
```

Search for the string pico recursively using the grep command.

```bash
$ grep -r pico ./              
.//big-zip-files/folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt:information on the record will last a billion years. Genes and brains and books encode picoCTF{gr3p_15_m4g1c_********}
```

## Flag

```
picoCTF{gr3p_15_m4g1c_********}
```