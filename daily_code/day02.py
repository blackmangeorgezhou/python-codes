'''
字符串相关内置函数
'''

if __name__ == '__main__':
  str1 = 'hello world !'

  # 字符串 【首字母大写的拷贝】
  print(str1.capitalize())
  # 字符串 【每个单词首字母大写的拷贝】
  print(str1.title())

  str1.upper()
  str1.lower()
  '''
  substr不存在， find => -1; index => 报错
  '''
  print(str1.find('hel'), str1.index('hel'))

  '''
  判断字符串是否由数字组成 *isdigit*
  判断字符串是否由字母组成 *isalpha*
  '''
  str1.isdigit()
  str1.isalpha()

  str1.startswith('world')
  str1.endswith('world')

  print(str1.center(20,'*'))
  print(str1.rjust(50, '*'))

  '''
  占位符写法
  '%d',%d,%d%(变量1,变量2,变量3)

  '{0} + {1} = {2}'.format(a, b, a+b)

  f'{a} * {b} = {a*b}' > python3.6 语法糖
  '''

  # 列表 List
  list1 = ['hello'] * 3
  '''
  * 遍历
    1. for i in range(len(list1)):
    2. for elem in list1:
    3. for index,elem in enumerate(list1):
  * 方法
    append(elem);
    insert(index, elem);
    += => extend(elem<List>);
    pop(index)
    remove(elem)
    clear()
    sort(reverse = True)
    ** sorted(elem<List>, reverse = True)
  '''


print([x for x in range(10)])
  