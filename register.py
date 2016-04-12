#!/Python27/python

import MySQLdb
import cgi

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<body>'


form = cgi.FieldStorage()
username =form.getvalue('username')
password =form.getvalue('password')
sel = form.getvalue('sel')

try:
	db = MySQLdb.connect('localhost','root','','quiz')

	cursor = db.cursor()

	if sel == 'student':
		cursor.execute("""insert into studentregister(username,password) values(%s,%s)""",(username,password))

	else:
		cursor.execute("""insert into teacherregister(username,password) values (%s,%s)""", (username,password))

	db.commit()
	print "<h1>data inserted successfully</h1>"

except:
	print "<p>Error: unable to insert data</p>"

db.close()

print '</body>'
print '</html>'