import random

number=3
ran=random.randint(1,6)

print(ran)

if number==ran:
    print("相等")
elif number>ran:
    print("{}更大".format(number))
else:
    print("{}更大".format(ran))

if(ran>=1 and ran<3):
    print(ran)
    print("ran 为1或2")
elif(ran>3):
    print(ran)
    print("ran为4到6")