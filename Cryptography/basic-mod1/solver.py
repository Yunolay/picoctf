num = open('./message.txt', 'r')
nums = num.read().split()

flag = ''
for i in nums:
    mod_val = int(i) % 37
    if 0 <= mod_val <= 25:
        # Map 0-25 to 'A'-'Z'
        flag += chr(mod_val + 65)
    elif 26 <= mod_val <= 35:
        # Map 26-35 to '0'-'9'
        flag += chr(mod_val + 22)  # 22 = 48 (ASCII code for '0') - 26
    elif mod_val == 36:
        # Map 36 to '_'
        flag += '_'

print(f'picoCTF{{{flag}}}')