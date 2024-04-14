# chrono

Tags: picoCTF 2023, General Skills, linux

| Author | Point    |
| ------ | -------- |
| MUBARAK MIKAIL | 100 points |

## Description

How to automate tasks to run at intervals on linux servers?  
Use ssh to connect to this server:  
Server: saturn.picoctf.net  
Port: 50691  
Username: picoplayer   
Password: H9RmN0m18U  

## Solve

Connect to the server using ssh and run the following command to view the cron jobs.

```bash
$ ssh picoplayer@saturn.picoctf.net -p 50691

[snip]

picoplayer@challenge:~$ cat /etc/crontab
# picoCTF{Sch3DUL7NG_T45K3_L1NUX_********}
```

## Flag

```
picoCTF{Sch3DUL7NG_T45K3_L1NUX_********}
```
