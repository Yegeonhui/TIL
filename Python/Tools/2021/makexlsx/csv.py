from openpyxl import Workbook
import os

route = os.getcwd()

write_wb = Workbook()

write_ws = write_wb.active
write_ws.append([1,2,3])
write_ws.append([1, 2, 3])
write_ws.cell(5,5,'5행 5열')

write_wb.save("./test.xlsx")