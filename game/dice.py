# 摇骰子
import random
import time

point = 0

date = 0
while date < 3:
    print('摇骰子中...')
    time.sleep(1)
    date = date + 1
    point = point + random.randrange(1, 7)

msg = input('买大买小：')
if msg == '大' and 11 <= point <= 18:
    print('结果是大，恭喜你猜对了')
elif msg == '小' and 3 <= point <= 10:
    print('结果是小，恭喜你猜对了')
else:
    print('猜错了')
