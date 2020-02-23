import xlrd
from xlwt import *

def read_excel(fileName):
    bk=xlrd.open_workbook(fileName)
    shxrange=range(bk.nsheets)
    try:
        sh=bk.sheet_by_name('Sheet1')
            #根据sheet1名字确定表格内容
    except Exception as e:
        print(e)
    nrows=sh.nrows#获取行数
    li=[]
    #定义一个空列表，以存储第二列的数据（哪一行都行，只要它具有唯一性）
    for i in range(1,nrows):
        #对表格用行数进行遍历，存储到刚刚定义的li列表中，并返回它
        row_data=sh.row_values(i)
        ctype = sh.cell(i, 1).ctype  # 表格的数据类型
        value=sh.cell_value(i,1)
        if ctype == 2 and value % 1 == 0.0:  # ctype为2且为浮点
            value = int(value)  # 浮点转成整型

        li.append(value)
    return li

classmate=nameList=absence=[]
classmate=read_excel('classmate.xlsx')
nameList=read_excel('nameList.xlsx')
answer=0
for i in classmate:
        if i not in nameList:
           absence.append(i)

print(absence)
print(classmate)
print(nameList)