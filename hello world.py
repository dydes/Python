import xlwings as xw

app = xw.App(visible=True, add_book=False)

for i in range(1,3):
    wb=app.books.add()
    wb.save(f'd:\\python\\01\\测试{i}.xlsx')
    wb.close()
app.quit()