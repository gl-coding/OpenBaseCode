#encoding=utf8
import xlrd
import sys

reload(sys);
sys.setdefaultencoding("utf8")

def read_xlrd(filepath):
    data = xlrd.open_workbook(filepath)
    table_name = data.sheet_names()
    table = data.sheets()[1]

    nrows = table.nrows
    ncols = table.ncols

    for j in range(nrows):
        line = ""
        for i in range(1, 5):
            if i == 5:
                continue
            line += "\t" + table.cell_value(j, i).encode("utf8")
