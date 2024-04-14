# money-ware

Tags: picoCTF 2023, General Skills, osint

| Author | Point    |
| ------ | -------- |
| JUNI19 | 100 points |

## Description

Flag format: picoCTF{Malwarename}  
The first letter of the malware name should be capitalized and the rest lowercase.  
Your friend just got hacked and has been asked to pay some bitcoins to 1Mz7153HMuxXTuR2R1t78mGSdzaAtNbBWX. He doesn’t seem to understand what is going on and asks you for advice. Can you identify what malware he’s being a victim of?  

## Solve

Google “1Mz7153HMuxXTuR2R1t78mGSdzaAtNbBWX”.  
The following articles were found.

[Hackers have made just 3.7 bitcoin – or less than $10,000 – with the latest cyberattack
](https://www.cnbc.com/2017/06/28/ransomware-cyberattack-petya-bitcoin-payment.html)

This is an article about Petya, a malware.

So the flags are:

## Flag
```
picoCTF{petya}
```
