import pyodbc
server='HYDTRNG9\SQLEXPRESS'
database='python'
username='sa'
password='admin@23'
cxcn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)


mycursor=cxcn.cursor()
res=mycursor.execute("select * from Table_1")
myrecs=res.fetchall();
print(myrecs)