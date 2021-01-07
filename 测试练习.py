# i=['a','b']
# l=[1,2]
# print(dict([i, l]))

# text = ''
# with open('E:/1.txt') as f1:
#     text = text.join(f1.read())
# with open('E:/2.txt') as f2:
#     text = text.join(f2.read())
# l = list(text)
# l.sort()

# newText = ''
# newText = newText.join(l)
# print(newText)
# with open('E:/zhoumeng.txt', 'w') as f2:
#     f2.write(newText)

s1 = input('输入字符串：')
s2 = input('输入子字符串：')
count = s1.count(s2)
print(count)