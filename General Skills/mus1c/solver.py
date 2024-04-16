nums = [114, 114, 114, 111, 99, 107, 110, 114, 110, 48, 49, 49, 51, 114]

flag =''

for num in nums:
    flag += chr(num)

print(f"picoCTF{{{flag}}}")