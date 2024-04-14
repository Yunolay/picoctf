# Collaborative Development

Tags: picoCTF 2024, General Skills, browser_webshell_solveable, git

| Author | Point    |
| ------ | -------- |
| JEFFERY JOHN | 75 points |

## Description

My team has been working very hard on new features for our flag printing program! I wonder how they'll work together?  
You can download the challenge files here:

## Solve

Unzip the given zip file using the unzip command.

```bash
$ unzip challenge.zip
Archive:  challenge.zip
   creating: drop-in/
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
 extracting: drop-in/.git/refs/heads/main  
   creating: drop-in/.git/refs/heads/feature/
 extracting: drop-in/.git/refs/heads/feature/part-1  
  inflating: drop-in/.git/refs/heads/feature/part-2  
 extracting: drop-in/.git/refs/heads/feature/part-3  
   creating: drop-in/.git/refs/tags/
 extracting: drop-in/.git/HEAD       
  inflating: drop-in/.git/config     
   creating: drop-in/.git/objects/
   creating: drop-in/.git/objects/pack/
   creating: drop-in/.git/objects/info/
   creating: drop-in/.git/objects/77/
 extracting: drop-in/.git/objects/77/d6ceca6fe23b57d88cf16f20003e10d6715690  
   creating: drop-in/.git/objects/b9/
 extracting: drop-in/.git/objects/b9/32e8c048154a46d224cd7691c99dc8cb88164a  
   creating: drop-in/.git/objects/54/
 extracting: drop-in/.git/objects/54/c7842e34d03976ddc080a9dd76742751024358  
   creating: drop-in/.git/objects/6e/
 extracting: drop-in/.git/objects/6e/17fb3a35364b4f9bb8bef8b5e6a5af2d3e7dfa  
   creating: drop-in/.git/objects/43/
 extracting: drop-in/.git/objects/43/e44dd37ba0c0adc3d78d0b85d699859ec8d75c  
   creating: drop-in/.git/objects/f6/
 extracting: drop-in/.git/objects/f6/5544e4f1511fe1d1dfff03c4d65869da039b8e  
   creating: drop-in/.git/objects/7a/
 extracting: drop-in/.git/objects/7a/b4e25c0cd108374b2275fdb1fcdf635e591833  
   creating: drop-in/.git/objects/d1/
 extracting: drop-in/.git/objects/d1/f3407cee4479c075997b497fa290ca636fe258  
   creating: drop-in/.git/objects/d3/
 extracting: drop-in/.git/objects/d3/563a2c62ab2c95c5c13f3377cc6d79b2411c22  
   creating: drop-in/.git/objects/45/
 extracting: drop-in/.git/objects/45/6656eef7d5d6b8b7d49dc4f7fe6ff456c0bb91  
   creating: drop-in/.git/objects/0a/
 extracting: drop-in/.git/objects/0a/e601af6790d90cf89319f9a6520b4e2f15db35  
   creating: drop-in/.git/objects/5c/
 extracting: drop-in/.git/objects/5c/00b43f48516d7cc81ea1f497b4d43ae6a84c4c  
  inflating: drop-in/.git/index      
 extracting: drop-in/.git/COMMIT_EDITMSG  
   creating: drop-in/.git/logs/
  inflating: drop-in/.git/logs/HEAD  
   creating: drop-in/.git/logs/refs/
   creating: drop-in/.git/logs/refs/heads/
  inflating: drop-in/.git/logs/refs/heads/main  
   creating: drop-in/.git/logs/refs/heads/feature/
  inflating: drop-in/.git/logs/refs/heads/feature/part-1  
  inflating: drop-in/.git/logs/refs/heads/feature/part-2  
  inflating: drop-in/.git/logs/refs/heads/feature/part-3  
  inflating: drop-in/flag.py
```

There are 3 branches in the git repository.

```bash
$ git branch                  
  feature/part-1
  feature/part-2
  feature/part-3
* main
```

Check out each branch and see flag.py.

```bash
$ git checkout feature/part-1
Switched to branch 'feature/part-1'

$ cat flag.py 
print("Printing the flag...")
print("picoCTF{t3@mw0rk_", end='')

$ git checkout feature/part-2
Switched to branch 'feature/part-2'
                                                                                                                                                                                                          21:36:53
$ cat flag.py 
print("Printing the flag...")
print("m@k3s_th3_dr3@m_", end='')

$ git checkout feature/part-3

$ cat flag.py                
print("Printing the flag...")

print("w0rk_********}")
```

## Flag

```
picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_********}
```