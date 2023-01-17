import  xlwings as xw

#创建工作簿
app= xw.App(visible=True, add_book=False)
wb=app.books.add()

#工作表改名
ws=wb.sheets.add('产品统计表')

#写入值
ws.range('A1').value='编号'

#保存工作簿
wb.save(f'd:\\python\\01\\03.xlsx')

#关闭工作簿
wb.close()
app.quit()