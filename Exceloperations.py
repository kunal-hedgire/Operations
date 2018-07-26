import xlrd as read
import xlwt as write



class ExcelOperation :

    filePath ='C:\PythonProjects\DB2\\uset1.xls'
    listOfLines = []
    readExcelDataList=[]

    def getDataFromFile(self):
        file = open('C:\PythonProjects\DB2\Info.txt')
        for line in file.readlines():
            ExcelOperation.listOfLines.append(line.strip())

    def writeIntoExcel(self):
        workBook = write.Workbook()
        userInfoSheet = workBook.add_sheet('UserInfo')
        count = 0
        cols = []
        for item in ExcelOperation.listOfLines:
            for words in item.split(','):
                cols.append(words)

        for num in range(ExcelOperation.listOfLines.__len__()):
            row = userInfoSheet.row(num)
            for item in range(3):
                row.write(item,cols.__getitem__(count))
                count+=1

        workBook.save(ExcelOperation.filePath)


    def readDataFromExcel(self):
        workbook = read.open_workbook(ExcelOperation.filePath)
        userinfosheet = workbook.sheet_by_name("UserInfo")

        for rindex in range(0,userinfosheet.nrows):
            for cindex in range(0,userinfosheet.ncols):
                ExcelOperation.readExcelDataList.append(userinfosheet.cell(rindex,cindex).value)
        print(ExcelOperation.readExcelDataList)
        return ExcelOperation.readExcelDataList



if __name__ == '__main__':
    ob = ExcelOperation()
    ob.getDataFromFile()
    print(ExcelOperation.listOfLines)
    ob.writeIntoExcel()
    ob.readDataFromExcel()
    print(ExcelOperation.readExcelDataList)