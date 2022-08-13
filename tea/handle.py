output = 'R;crc75ihl`cNYe`]m%50gYhugow~34i'

a = ''
count = 0
while count<32:
    v14 = output[count:]
    v14 += output[0:count]
    dest = ''
    src = ''
    for i in range(16,32):
        dest += chr(ord(v14[i]) - 3*((i-17)//(-2)))
    for i in range(16):
        src += chr(ord(v14[i]) - (i+16)//6)
    flag = ''
    for i in range(16):
        flag+=src[i]
        flag+=dest[i]
    count+=1
    print(flag)
