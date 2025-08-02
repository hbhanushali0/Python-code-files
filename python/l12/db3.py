# wapp to connect and disconnect from database

import mysql
import pymysql

con = None
try:
	con = pymysql.connect("localhost", "root", "sochosocho", "student")
	print("connected")
	cursor = con.cursor()
	sql = "select rno, name from student_thane_jan20"
	cursor.execute(sql)
	data = cursor.fetchall()
	for d in data:
		print("rno = ", d[0], "name = ", d[1])

except Exception as e:
	print("issue", e)
	
finally:
	if con is not None:
		con.close()
		print("disconnected")

