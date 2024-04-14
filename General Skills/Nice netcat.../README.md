# Nice netcat...

Tags: picoCTF2021, General Skills

| Author | Point    |
| ------ | -------- |
| SYREAL | 15 points |

## Description

There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 21135, but it doesn't speak English...

## Solve

```bash
$ nc mercury.picoctf.net 21135
112
105
99
111
67
84
70
123
103
48
48
100
95
107
49
116
116
121
33
95
110
49
99
51
95
107
49
116
116
121
33
95
97
102
100
53
102
100
97
52
125
10
```

This looks like an ASCII character code. Write a simple solver in python.

```python
num =[112, 105, 99, 111, 67, 84, 70, 123, 103, 48, 48, 100, 95, 107, 49, 116, 116, 121, 33, 95, 110, 49, 99, 51, 95, 107, 49, 116, 116, 121, 33, 95, 97, 102, 100, 53, 102, 100, 97, 52, 125, 10]

print(''.join(chr(i) for i in num))
```

Run the script and we will get the flag.

```bash
$ python3 solve.py        
picoCTF{g00d_k1tty!_n1c3_k1tty!_********}
```