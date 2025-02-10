#Ví dụ 1
import mysql.connector 
myconn = mysql.connector.connect(host = "localhost", user = "root",  
    passwd = "") 
     
print(myconn)

#Ví dụ 2
import mysql.connector 
    
# tạo đối tượng connection 
myconn = mysql.connector.connect(host = "localhost", user = "root",  
    passwd = "") 
    
# in đối tượng connection ra màn hình 
print(myconn) 

#Ví dụ 3

import mysql.connector 
# tạo đối tượng connection 
myconn = mysql.connector.connect(host = "localhost", user = "root",  
passwd = "", database = "student_db") 
# in đối tượng connection ra màn hình 
print(myconn)

#Ví dụ 4
import mysql.connector 
# tạo đối tượng connection  
myconn = mysql.connector.connect(host = "localhost", user = "root",  
passwd = "", database = "student_db") 
# in đối tượng connection ra màn hình 
print(myconn) 
# tạo đối tượng cursor 
cur = myconn.cursor() 
# in đối tượng cursor ra màn hình 
print(cur) 

#Ví dụ 5
import mysql.connector 
    
# tạo đối tượng connection 
myconn = mysql.connector.connect(host = "localhost", user = "root",  
    passwd = "") 
  
# tạo đối tượng cursor 
cur = myconn.cursor() 
  
try: 
    dbs = cur.execute("show databases") 
except: 
    myconn.rollback() 
for x in cur: 
    print(x) 
myconn.close() 

#Ví dụ 6
import mysql.connector 
    
# tạo đối tượng connection 
myconn = mysql.connector.connect(host = "localhost", user = "root",  
    passwd = "") 
  
# tạo đối tượng cursor 
cur = myconn.cursor() 

try: 
    cur.execute("create database PythonDB") 
    dbs = cur.execute("show databases") 
except: 
    myconn.rollback() 
for x in cur: 
    print(x) 
myconn.close()