# 猜数字小游戏
import random

# 竞猜次数
count = 0

# 随机生成一个1-500的随机数
number = random.randrange(1, 500)

while True:
    count = count + 1
    user_guess_number = int(input('输入你猜的数字：'))
    if user_guess_number == number:
        print('恭喜你猜对了，一共猜了{}次'.format(count))
        break
    elif user_guess_number > number:
        print('猜的数字大了哦')
    else:
        print('猜的数字小了哦')
