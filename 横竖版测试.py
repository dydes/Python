# -*- coding: utf-8 -*-

import xlwings as xw

#启动Excel程序窗口，但不新建工作簿
app = xw.App(visible = True, add_book= False) 

#打开指定路径工作簿
wb = app.books.open('/Users/htuser-7/会通/github/VBA/横竖版/1.xlsx') 

#在指定工作表后新建一个工作表
sht = wb.sheets.add(after='Sheet1') 

#激活指定的工作表
wb.sheets['Sheet1'].activate()

#获取激活工作表的最大行数
rowmax=wb.sheets['Sheet1'].used_range.last_cell.row

#写入值
wb.sheets['Sheet2'].range('A1').value=rowmax

#切换工作表
wb.sheets['Sheet1'].activate()

#排序
sht1=wb.sheets('Sheet1')
sht1.range('B2:G2').api.Sort(Key1=sht1.range('B2').api,sorted=1)