import datetime
import json

import torch


# import sys
# sys.path.append('E:\\softwares\\python\\SRC\\utils')

# import mac as M
# import SRC.utils.mac as M # 绝对路径引入
# from ..utils.mac import sayHi

# 数据类型
'''
  文本类型 str
  数值类型 int float complex
  序列类型 list tuple range
  映射类型 dict (词典 dictionary)
  集合类型 set frozenset
  布尔类型 bool
  二进制类型 bytes, bytearray, memoryview

  *注
  a. 强类型转化 value = (str|int|float|complex) oldValue
  b. 列表、元组、集合、词典的区别
    列表 - list：有序、可更改的集合；允许有重复的元素；[ 允许为 “负索引”，-1 表示 倒数第一个元素 ]
    元组 - tuple：有序、不可更改的集合；允许有重复的元素；[ 不可更改，tuple => list; 可进行更改 ]
    集合 - set：无序、无索引的集合；没有重复的元素；
    词典 - dictionary：类 JSON Object，[ key 必须加 '', 为str 类型 ]无序、可变、有索引的集合，没有重复的元素
    e.g. 
      list: theList = ['tom', 'jerry', 'tom', 'jerry']
      tuple: theTuple = ('tom', 'jerry', 'tom', 'jerry')
      set: theSet = { 'tom', 'jerry' }
      dictionary: theDictionary = {
        'tom': 'i am tom',
        'jerry': 'i am jerry'
      }
'''

class DictType:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def createDict (self):
    theDictionary = dict(name=self.name, age=self.age)
    print(theDictionary.items())
    items = theDictionary.items()
    for item, i in items:
      print(item, end='')
      print("======", end='')
      print(i)
    print(theDictionary.keys())
    print(theDictionary.values())
    

# 类定义：class
class Person:
  # 构造函数
  def __init__(self, name, age):
    self.name= name
    self.age = age
  # 私有函数
  def say(self):
    print('my name is {}, my age is {}.'.format(self.name, self.age))
  def personSay(self):
    print('{} say: i am a person'.format(self.name))

# 继承
class Student(Person):
  def __init__(self, name, age, classCode):
    # Person(name, age)
    # self.name = name
    # self.age = age
    super().__init__(name, age)
    self.classCode = classCode
  def studentSay(self):
    print('{} say: i am a student, classCode is {}'.format(self.name, self.classCode))


if __name__ == "__main__":
  # current = datetime.datetime.now()
  # print(current.year)
  # print(current.strftime('%B'), current.strftime('%y'),sep=',') strptime: datetime string => DateTime
  
  # theTuple = ('tom', 'jack', 'allen')
  # tupleIterator = iter(theTuple)
  # for i in range(len(theTuple)):
  #   print(next(tupleIterator))

  # jsonString = '{"name":"tom","age":20}'
  # jsonDic = json.loads(jsonString)
  # print(jsonDic)
  # print(json.dumps(jsonDic))
  print(12343)
  print(torch.__version__, torch.version.cuda, torch.cuda.is_available())