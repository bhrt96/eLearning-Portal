 #!/Python27/python
 
import cgi
import mysql
import MySQLdb

print "Content-type: text/html\n"
form = cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('password')
select = form.getvalue('select')

try:
	db = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '', db = 'project')

	cursor = db.cursor()
	
	if select == 'student':
		cursor.execute("insert into student_registration(username,password,select) values(username,password,'student')")
	
	else:
		cursor.execute("insert into teacher_registration(username,password,select) values(username,password,'teacher')")
	
	
	print "data inserted successfully"

except:
		 print "Error: unable to insert data"
	
#data = cursor.fetchone()

#print "Database version : %s " % data

db.close()

