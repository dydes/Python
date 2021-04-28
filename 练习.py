#引入包
import xlwings as xw

app = xw.App(visible=True, add_book=False)
app.display_alerts = True   #关闭一些提示信息，可以加快运行速度。 默认为 True。
app.screen_updating = True   #更新显示工作表的内容。默认为 True。关闭它也可以提升运行速度。

#新建工作簿。
wb = app.books.add()

#获取当前活动工作表
sht = wb.sheets.active

#保存文件，不改名直接保存在当前目录用.save(path=None)
wb.save(r'D:\python\测试.xlsx')

#单元格写入内容
sht.range('A1').value = 1
sht.range('A2').value = [1,2,3]   #等同于('A2:C2')
sht.range('A3').options(transpose=True).value=[1,2,3]   #按列写入值
sht.range('A4').options(expand='table').value=[[1,2],[3,4]]