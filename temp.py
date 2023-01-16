import xlwings as xw

app = xw.App(visible=True, add_book=False)
wb = app.books.open(f'd:\\python\\01\\03.xlsx')