# Static ain't always noise

Tags: picoCTF 2021, General Skills

| Author | Point    |
| ------ | -------- |
| SYREAL | 20 points |

## Description

Can you look at the data in this binary: static? This BASH script might help!

## Solve

Find out what the file is using the file command.

```bash
$ file static                   
static: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=9f1762ab580608bef0d251f5fdfaad3d19ae0963, not stripped
```

Look at the given shell script.

Executes the strings command and outputs what is passed as an argument to "$1.ltdis.x86_64.txt".

```sh
#!/bin/bash



echo "Attempting disassembly of $1 ..."


#This usage of "objdump" disassembles all (-D) of the first file given by 
#invoker, but only prints out the ".text" section (-j .text) (only section
#that matters in almost any compiled program...

objdump -Dj .text $1 > $1.ltdis.x86_64.txt


#Check that $1.ltdis.x86_64.txt is non-empty
#Continue if it is, otherwise print error and eject

if [ -s "$1.ltdis.x86_64.txt" ]
then
	echo "Disassembly successful! Available at: $1.ltdis.x86_64.txt"

	echo "Ripping strings from binary with file offsets..."
	strings -a -t x $1 > $1.ltdis.strings.txt
	echo "Any strings found in $1 have been written to $1.ltdis.strings.txt with file offset"



else
	echo "Disassembly failed!"
	echo "Usage: ltdis.sh <program-file>"
	echo "Bye!"
fi
```

Extract the strings in the binary using the strings command.  
Use the grep command to output only strings containing flags.

```bash
$ strings static | grep pico
picoCTF{d15a5m_t34s3r_********}
```