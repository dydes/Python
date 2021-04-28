#引入包
import xlwings as xw

app = xw.App(visible=True, add_book=False)
app.display_alerts = True    # 关闭一些提示信息，可以加快运行速度。 默认为 True。
app.screen_updating = True    # 更新显示工作表的内容。默认为 True。关闭它也可以提升运行速度。

# 新建工作簿。
wb = app.books.add()

# 获取当前活动工作表
sht = wb.sheets.active