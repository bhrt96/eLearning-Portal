#!/Python27/python

import cgi
import MySQLdb

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<body>'

form=cgi.FieldStorage()
username =form.getvalue('username')
password =form.getvalue('password')
sel = form.getvalue('sel')

try:

	db=MySQLdb.connect('loacalhost','root','','quiz')
	cur=db.cursor()

	if sel=='student':
		sql="select * from studentregister"
		cur.execute(sql)
		var=cur.fetchall()

		for var2 in var:
			if var2['password'] == password and var2['username']==username:
				 print "Location: choosesub.php\r\n";
	
	elif sel=='teacher':
		sql="select * from teacherregister"
		cur.execute(sql)
		var=cur.fetchall()

		for var2 in var:
			if var2['password'] == password and var2['username']==username:
				sub="""select subject from teacher where name=%s""" % username
				 print "Location: subject.php\r\n";
				 
				 
	else:
		print "<h2>Enter correct username or password"

				
	db.close()	
	print"<h1> Successful</h1>"

except:
	print"<h1>Error</h1>"

print '</body>'
print '</html>'
	