import pandas as pd

#数据选取
data=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],index=['r1','r2','r3'],columns=['c1','c2','c3'])
print(data)

#c1列数据，带信息
a=data['c1']

#c1列数据，不带信息
b=data[['c1']]

#c1和c3两列数据
c=data[['c1','c3']]

#第2至3行数据，从0行开始，左闭右开，加iloc是避免混淆
d=data.iloc[1:3]

#选倒数第一行数据
e=data.iloc[-1]

#选指定两行
f=data.loc[['r2','r3']]

#选择头n行，不写参数默认5行
g=data.head(2)

#选c1和c3前两行，先选列再选行
h=data[['c1','c3']][0:2]

#先选行再选列，不容易混淆
i=data.iloc[0:2][['c1','c3']]

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)