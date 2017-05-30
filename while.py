import random
import time

while True:
    print("正在生成随机数...")
    time.sleep(1)
    number=3
    ran=random.randint(1,10)

    if number==ran:
        print("找到相同数字")
        print("即将跳出")
        time.sleep(3)
        break
    elif number>ran:
        print("number为{},ran为{}".format(number,ran))
        print("number比较大，继续生成...")
    else:
        print("number为{},ran为{}".format(number,ran))
        print("number比较小，继续生成...")