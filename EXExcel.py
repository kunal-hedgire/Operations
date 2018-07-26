import xlrd as read
import xlwt as write

class Excel:
        filepath = 'C:\PythonProjects\DB2\\useit.xls'
        list1=[]
     def GetData(self):
        file=open('C:\PythonProjects\DB2\Info.txt')
        msg=file.read()
        print(msg)
        for items in file.readlines():
            Excel.list1.append(items.strip())
     def WritrData(self):
         workBook=write.workbook()
         sheet=workBook.add_sheet('info')
         count=0
         cols=[]
        for line in Excel.list1:
            for words in item.split(','):
                 cols.append(words)

            for num in range(ExcelO.listOfLines.__len__()):
                row = sheet.row(num)
                for item in range(3):
                    row.write(item, cols.__getitem__(count))
                    count += 1

            workBook.save(Excel.filePath)










