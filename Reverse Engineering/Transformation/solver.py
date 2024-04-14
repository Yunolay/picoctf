enc = open("enc").read()
flag = ''

for i in range(0, len(enc)):
    c1 = chr((ord(enc[i]) >> 8))
    flag += c1

    c2 = chr(enc[i].encode('utf-16be')[-1])
    flag += c2

print(flag)