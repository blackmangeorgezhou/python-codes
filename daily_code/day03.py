'''
yield 关键字
'''
def foo():
  print("starting...")
  while True:
    res = yield 4
    print("res:",res)

def fib(n):
  a, b = 0, 1
  for _ in range(n):
    a, b = b, a + b
    yield a


def main():
  for val in fib(20):
    print(val)

if __name__ == "__main__":
  # g = foo()
  # print(next(g))
  # print('*' * 20)
  # print(next(g))
  print(sys.getsizeof([1,2]))
    