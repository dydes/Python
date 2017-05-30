import random

for i in range(1,20):
    ran=random.randint(1,20)

    if i==ran:
        pass
        print("相等跳过")
    elif i>ran:
        print("i比较大")
    else:
        print("i比较小")