import pandas as pd

#读取Excel工作簿指定工作表
data=pd.read_excel('d:\\python\\01\\测试.xlsx',sheet_name=0)
print(data)

data1=pd.DataFrame([[1,2],[3,4],[5,6]],columns=['A列','B列'])
data1.to_excel('d:\\python\\01\\测试pandas.xlsx',columns=['A列'],index=False)

