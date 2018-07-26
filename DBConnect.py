import pymysql
import xlrd

conn= pymysql.connect(host='localhost',port=3306,user='root',passwd='tiger',db='testdb')

cur=conn.cursor()

cur.execute('CREATE TABLE employees12(id INT(2) AUTO_INCREMENT PRIMARY KEY,firstname VARCHAR(30) NOT NULL,lastname VARCHAR(30) NOT NULL)')

cur.execute('insert into employees12 values(1,\'kunal\',\'hedgire\')')

cur.execute('select * from employees')
print(cur.fetchall())

conn.commit()
cur.close()
conn.close()
