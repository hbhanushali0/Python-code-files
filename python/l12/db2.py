# wapp to connect and disconnect from oracle db

import pymysql
import mysql

con = None

try:
	con = pymysql.connect("localhost", "root", "sochosocho", "student")
	print("connected")
	rno = int(input("enter roll no "))
	name = input("enter name ")
	args = (rno, name)
	cursor = con.cursor()
	sql = "insert into student_thane_jan20 values ('%d', '%s')"
	cursor.execute(sql % args)
	con.commit()
	print(cursor.rowcount, "records inserted")

except Error as e:
	print("issue", e)
	con.rollback()

finally:
	if con is not None:
		con.close()
		print("disconnected")
