# wapp to connect and disconnect from db

import mysql.connector
from mysql.connector import Error
import pymysql
 

con = None
try:
	con = pymysql.connect(user = 'root', password = 'sochosocho')
	print("connected")
	

except Error as e:
	print("issue", e)

finally:
	if con is not None:
		con.close()
		print("disconnected")



	