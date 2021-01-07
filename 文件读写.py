# f = open('E://zhoumeng.txt', 'w')
# f.write('Hello World !')
# f.close()

# f = open('E://zhoumeng.txt','r')
# s = f.read()
# print(s)
# f.close()

with open('E://img.png', 'rb') as p:
    pic = p.read()
with open('E://img_back.png', 'wb') as p2:
    p2.write(pic)
