import pandas as pd
import numpy as np
s=pd.Series(['丁一','王二','张三'])
print(s)

t=pd.DataFrame([[1,2],[3,4],[5,6]],columns=['date','score'],index=['A','B','C'])
print(t)

#先创建空的DataFrame，然后再填充
a=pd.DataFrame()
date=[1,3,5]
score=[2,4,6]
a['date']=date
a['score']=score
print(a)

#从字典创建DataFrame，键默认是列名
b=pd.DataFrame({'a':[1,3,5],'b':[2,4,6]},index=['x','y','z'])
print(b)

#让字典的键成为行索引
c=pd.DataFrame.from_dict({'a':[1,3,5],'b':[2,4,6]},orient='index')
print(c)

#通过二维数组创建
a1=np.arange(12).reshape(3,4)
print(a1)
b1=pd.DataFrame(a1,index=[1,2,3],columns=['A','B','C','D'])
print(b1)

#修改行列索引名，这里只有修改内容与原内容一一匹配才能修改成功
c1=t.rename(index={'A':'万科','B':'阿里','C':'百度'},columns={'date':'日期','score':'分数'})
c1.index.name='公司'
print(c1)
c1=c1.reset_index()
print(c1)

#将日期列改为索引列，没有inplace会报错，得替换原有的DataFrame
c1.set_index('日期',inplace=True)
print(c1)