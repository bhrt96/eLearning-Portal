#!/usr/bin/python

import MySQLdb
import cgi

print "Content-type:text/html\r\n\r\n"

print'<html>'
print'<title>Register</title>'
print'<head></head>'
print'<body>'

db = MySQLdb.connect('localhost','root','1315','quiz', unix_socket="/opt/lampp/var/mysql/mysql.sock")
cursor = db.cursor()

sql = "SELECT DISTINCT subject FROM teacher ORDER BY subject"
cursor.execute(sql)
var = cursor.fetchall()

print r"""<form action ="\cgi-bin\elearning\questions.py" method="POST">"""
print '<select name = "dropdown">'
for i in var:
    print '<option value=%s>%s</option>' % (i[0], i[0])
print '</select>'

print '<input type="submit" value="submit">'

#print "Location: /cgi-bin/signinform.html\r\n" 

print'</body>'
print'</html>'
