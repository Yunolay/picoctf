# Title

Tags: picoCTF 2024, General Skills, shell, ssh, browser_webshell_solvable

| Author | Point    |
| ------ | -------- |
| JEFFERY JOHN |  25 points |

## Description

Using a Secure Shell (SSH) is going to be pretty important.  
Can you ssh as ctf-player to titan.picoctf.net at port 51510 to get the flag?  
You'll also need the password 1db87a14. If asked, accept the fingerprint with yes.  
If your device doesn't have a shell, you can use: https://webshell.picoctf.org  
If you're not sure what a shell is, check out our Primer: https://primer.picoctf.com/#_the_shell

## Hints

1. https://linux.die.net/man/1/ssh
2. You can try logging in 'as' someone with <user>@titan.picoctf.net
3. How could you specify the port?
4. Remember, passwords are hidden when typed into the shell

## Solve

Just connect with ssh using the credentials given.

```bash
$ ssh ctf-player@titan.picoctf.net -p 51510
The authenticity of host '[titan.picoctf.net]:51510 ([3.139.174.234]:51510)' can't be established.
ED25519 key fingerprint is SHA256:4S9EbTSSRZm32I+cdM5TyzthpQryv5kudRP9PIKT7XQ.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:8: [titan.picoctf.net]:49226
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[titan.picoctf.net]:51510' (ED25519) to the list of known hosts.
ctf-player@titan.picoctf.net's password:
Welcome ctf-player, here's your flag: picoCTF{s3cur3_c0nn3ct10n_********}
Connection to titan.picoctf.net closed.
```

## Flag

```
picoCTF{s3cur3_c0nn3ct10n_********}
```