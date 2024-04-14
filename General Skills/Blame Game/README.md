# Blame Game

Tags: picoCTF 2024, General Skills, browser_webshell_solveable, git

| Author | Point    |
| ------ | -------- |
| JEFFERY JOHN | 75 points |

## Description

Someone's commits seems to be preventing the program from working. Who is it?  
You can download the challenge files here:

## Solve

Unzip the given zip file using the unzip command.

```bash
unzip challenge.zip 
Archive:  challenge.zip
   creating: drop-in/
 extracting: drop-in/message.py      
   creating: drop-in/.git/
   creating: drop-in/.git/branches/
  inflating: drop-in/.git/description  
   creating: drop-in/.git/hooks/
  inflating: drop-in/.git/hooks/applypatch-msg.sample  
  inflating: drop-in/.git/hooks/commit-msg.sample  
  inflating: drop-in/.git/hooks/fsmonitor-watchman.sample  
  inflating: drop-in/.git/hooks/post-update.sample  
  inflating: drop-in/.git/hooks/pre-applypatch.sample  
  inflating: drop-in/.git/hooks/pre-commit.sample  
  inflating: drop-in/.git/hooks/pre-merge-commit.sample  
  inflating: drop-in/.git/hooks/pre-push.sample  
  inflating: drop-in/.git/hooks/pre-rebase.sample  
  inflating: drop-in/.git/hooks/pre-receive.sample  
  inflating: drop-in/.git/hooks/prepare-commit-msg.sample  
  inflating: drop-in/.git/hooks/update.sample  
   creating: drop-in/.git/info/
  inflating: drop-in/.git/info/exclude  
   creating: drop-in/.git/refs/
   creating: drop-in/.git/refs/heads/
 extracting: drop-in/.git/refs/heads/master  
   creating: drop-in/.git/refs/tags/
 extracting: drop-in/.git/HEAD       
  inflating: drop-in/.git/config     
   creating: drop-in/.git/objects/
   creating: drop-in/.git/objects/pack/
   creating: drop-in/.git/objects/info/
   creating: drop-in/.git/objects/7d/

[snip]

  inflating: drop-in/.git/index      
 extracting: drop-in/.git/COMMIT_EDITMSG  
   creating: drop-in/.git/logs/
  inflating: drop-in/.git/logs/HEAD  
   creating: drop-in/.git/logs/refs/
   creating: drop-in/.git/logs/refs/heads/
  inflating: drop-in/.git/logs/refs/heads/master
```

I checked all the git logs using the "git log --all" command.  
A user with username flag was committing.

```bash
$ git log --all

[snip]

commit 5241c8d33658ddbc1410eae9eedb9713d4b996fd
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:09:11 2024 +0000

    important business work

commit fadeca9476b6713ec8cdda633aca9e9aebffc698
Author: picoCTF{@sk_th3_1nt3rn_********} <ops@picoctf.com>
Date:   Sat Mar 9 21:09:11 2024 +0000

    optimize file size of prod code

commit 2dd46769e2d65656bb14aed0ff5d3237daaa7d9d
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:09:11 2024 +0000

    create top secret project
```

## Flag

```
picoCTF{@sk_th3_1nt3rn_********}
```