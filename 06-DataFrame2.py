import pandas as pd

#数据筛选
data=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],index=['r1','r2','r3'],columns=['c1','c2','c3'])
print(data)

#c1列数据大于1的行
a=data[data['c1']>1]

#c1列数字大于1且c2列数字等于5的行
b=data[(data['c1']>1) & (data['c2']==5)]

print(a)
print(b)

#数据的排序
#按列排序，ascending=False降序排列，ascending=True升序排列
c=data.sort_values(by='c2',ascending=False)
print(c)

#按索引进行排序，类似Excel里面用数字辅助列来恢复默认排序
d=c.sort_index()
print(d)
