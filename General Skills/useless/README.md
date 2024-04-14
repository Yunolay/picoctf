# useless

Tags: picoCTF 2023, General Skills, man

| Author | Point    |
| ------ | -------- |
|  |  points |

## Description

There's an interesting script in the user's home directory  
The work computer is running SSH. We've been given a script which performs some basic calculations, explore the script and find a flag.  
Hostname: saturn.picoctf.net  
Port:     54014  
Username: picoplayer  
Password: password  

## Solve

When connecting via ssh, a suspicious shell script called useless owned by root is placed in the home directory.

```bash
$ ssh picoplayer@saturn.picoctf.net -p 54014

[snip]

picoplayer@challenge:~$ ls -al
total 16
drwxr-xr-x 1 picoplayer picoplayer   20 Apr 14 16:32 .
drwxr-xr-x 1 root       root         24 Aug  4  2023 ..
-rw-r--r-- 1 picoplayer picoplayer  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 picoplayer picoplayer 3771 Feb 25  2020 .bashrc
drwx------ 2 picoplayer picoplayer   34 Apr 14 16:32 .cache
-rw-r--r-- 1 picoplayer picoplayer  807 Feb 25  2020 .profile
-rwxr-xr-x 1 root       root        517 Mar 16  2023 useless
```

The inside of the script looks like a calculator.

```bash
picoplayer@challenge:~$ cat useless 
#!/bin/bash
# Basic mathematical operations via command-line arguments

if [ $# != 3 ]
then
  echo "Read the code first"
else
        if [[ "$1" == "add" ]]
        then 
          sum=$(( $2 + $3 ))
          echo "The Sum is: $sum"  

        elif [[ "$1" == "sub" ]]
        then 
          sub=$(( $2 - $3 ))
          echo "The Substract is: $sub" 

        elif [[ "$1" == "div" ]]
        then 
          div=$(( $2 / $3 ))
          echo "The quotient is: $div" 

        elif [[ "$1" == "mul" ]]
        then
          mul=$(( $2 * $3 ))
          echo "The product is: $mul" 

        else
          echo "Read the manual"
         
        fi
fi
```

In case of an exception, “Read the manual” is output. When I looked at the manual, there was a flag.

```bash
picoplayer@challenge:~$ man useless 

useless
     useless, — This is a simple calculator script

SYNOPSIS
     useless, [add sub mul div] number1 number2

DESCRIPTION
     Use the useless, macro to make simple calulations like addition,subtraction, multiplication and division.

Examples
     ./useless add 1 2
       This will add 1 and 2 and return 3

     ./useless mul 2 3
       This will return 6 as a product of 2 and 3

     ./useless div 6 3
       This will return 2 as a quotient of 6 and 3

     ./useless sub 6 5
       This will return 1 as a remainder of substraction of 5 from 6

Authors
     This script was designed and developed by Cylab Africa

     picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_****}
```

## Flag

```
picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_****}
```