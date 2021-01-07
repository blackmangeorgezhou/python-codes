'''
  输入圆的半径，求周长和面积
'''
def calculate_circle_area_and_circumference(radius = 5):
  print(radius)
  PI = 3.1415926
  area = 0
  circumference = 0

  if radius == 0:
    radius = float(input('半径：'))

  area = radius ** 2 * PI
  circumference = 2 * PI * radius
  print(f'面积：{area:.2f};周长：{circumference:.2f}')

'''
  判断年份是否是闰年
'''
def year_is_leap(year=0):
  try:
    year = int(year)
  except:
    print('年份错误')
    return
  flag = year % 4 == 0 and year % 100 == 0 or year % 400 == 0
  if flag:
    print('%d 是闰年！'%year)
  else:
    print('%d 不是闰年！'%year)


'''
判断是否是素数
公约数只有 1 和 其本身
'''
def num_is_prime (num):
  is_prime = True
  for i in range(2, num):
    if num % i == 0:
      is_prime = False
      break
  
  if is_prime and num != 1:
    print('%d 是素数！'%num)
  else:
    print('%d 不是素数！'%num)

def max_divider_and_min_multiply (num1, num2):
  if num1 > num2:
    num1,num2 = num2, num1
  for i in range(num1, 0, -1):
    if num1 % i == 0 and num2 % i == 0:
      print('%d,%d最大公约数：%d；最小公倍数：%d!'%(num1, num2, i, num1 * num2 // i))
      break

'''
  百钱百鸡问题
  公鸡：￥5/只；母鸡：￥3/只；小鸡：1￥/只
'''
def use_hundred_buy_chicken():
  MALE = 5
  FEMALE = 3
  for i in range(100//MALE):
    for j in range(100//FEMALE):
      if 100 == i * MALE + j * FEMALE + (100 - i - j):
        print('%d只公鸡，%d只母鸡，%d只小鸡。'%(i, j , 100-i-j))

'''
  CRAPS赌博游戏
  说明：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，
  玩家通过摇两粒骰子获得点数进行游戏。简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
  玩家第一次如果摇出2点、3点或12点，庄家胜；其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
  如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。
'''
from random import randint
def craps_games(money = 0):
  print(money)
  while money > 0:
    print('您的当前资产：%d'%money)
    debt = int(input('请下注：'))
    need_go_on = False
    if 0 < debt <= money:
      break
  first = randint(1,6) + randint(1,6)
  if first in [7, 11]:
    money += debt
  elif first in [1, 3, 12]:
    money -= debt
  else:
    need_go_on = True

  while need_go_on:
    current = randint(1,6) + randint(1,6)
    if current == 7:
      money += debt
      need_go_on = False
    elif current == first:
      money -= debt
      need_go_on = False
    else:
      need_go_on = True
  print('您当前筹码不足，游戏结束！')

'''
生成斐波那契数列
前两个数为1， 从第三个数开始，每个数为前两个之和
'''
def generate_fibonacci_sequence (count=3):
  fibonacci_sequence = [1,1]

  for i in range(count-2):
    current_index = len(fibonacci_sequence)
    current_num = fibonacci_sequence[current_index - 1] + fibonacci_sequence[current_index - 2]
    fibonacci_sequence.append(current_num)

  print(fibonacci_sequence)

'''
算出完美数
其所有真因子（除了自身以外的因子）的和正好等于其本身
'''
def is_perfect_num (num):
  total = 0
  for i in range(1,num):
    if num % i == 0:
      total += i
  return total == num

def perfect_num (end=100):
  perfect_num_list = []
  for num in range(1, end):
    if is_perfect_num(num):
      perfect_num_list.append(num)
  
  print('1 ~ %d之间的完美数：'%end, perfect_num_list)

if __name__ == '__main__':
  perfect_num(1000)