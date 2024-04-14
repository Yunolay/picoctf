import subprocess

inputs = ["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"]

for input_str in inputs:
    process = subprocess.Popen(['python3', 'level3.py'], stdin=subprocess.PIPE, text=True)
    process.stdin.write(input_str + "\n")
    process.stdin.flush()

process.stdin.close()

process.wait()