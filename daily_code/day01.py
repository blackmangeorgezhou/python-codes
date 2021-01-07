'''
函数 => 可变参数
e.g. 多个数相加
'''
# def add(*args):
#   total = 0
#   for i in args:
#     total += i
#   print(total)

# if __name__ == "__main__":
#   add(1)
#   add(1,2)
#   add(1,2,3)

def foo():
    b = 'hello'

    # Python中可以在函数内部再定义函数
    def bar():
        c = True
        print(a)
        print(b)
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined

'''
* if __name__ == '__main__'的变量属于全局作用域
* global关键字可在函数内声明全局变量
'''
if __name__ == '__main__':
    a = 100 # 
    # print(b)  # NameError: name 'b' is not defined
    foo()