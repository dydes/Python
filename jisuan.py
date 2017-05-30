a=9
b=2

print(a+b)
print(a-b)
print(a*b)
print(a/b)

#a的平方
print(a**2)

#a的平方根
print(a**0.5)

#a的立方根
print(a**(1/3))

#a除以b的商
print(a//b)

#a除以b的余数
print(a%b)

#排座位
row=8
id=36

print("学号为{}的小朋友，坐在第{}排第{}座".format(id,id//row+1,id%row))