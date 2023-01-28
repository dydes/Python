import pandas as pd

#数据运算
data=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],index=['r1','r2','r3'],columns=['c1','c2','c3'])
print(data)

#列运算，生成新列
data['c4']=data['c3']-data['c1']
print(data)

#数据删除
#删除c1列，inplace参数默认为False，不替换原有的DataFrame
a=data.drop(columns='c1')
print(a)

#删除c1和c3两列
b=data.drop(columns=['c1','c3'])
print(b)

#删除r1和r3两行
c=data.drop(index=['r1','r3'])
print(c)