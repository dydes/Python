# -*- coding: utf-8 -*-

import xlwings as xw
wb=xw.Book("/Users/htuser-7/1/testxlwings.xlsx") #连接到excel，提前建好放到了D盘
sht=wb.sheets[0]
sht.range('a1').value="我是通过python写入的"  #写入单元格值