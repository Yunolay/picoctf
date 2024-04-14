import subprocess

with open("./dictionary.txt", "r") as file:
    for input_str in file:
        input_str = input_str.rstrip()
        process = subprocess.Popen(['python3', 'level5.py'], stdin=subprocess.PIPE, text=True)
        process.stdin.write(input_str + "\n")
        process.stdin.flush()

process.stdin.close()

process.wait()