#!/usr/bin/python

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

    db = MySQLdb.connect('localhost','root','1315','quiz', unix_socket="/opt/lampp/var/mysql/mysql.sock")
    cur=db.cursor()

    if sel=='student':
        sql="select * from studentRegister"
        cur.execute(sql)
        var=cur.fetchall()

        for var2 in var:
            if var2[2] == password and var2[1]==username:
                 print "student login success"


    elif sel=='teacher':
        sql="select * from teacherRegister"
        cur.execute(sql)
        var=cur.fetchall()

        for var2 in var:
            if var2[2] == password and var2[1]==username:
                sql="""select subject from teacher as t join teacherRegister as tr on t.TeacherId=tr.TeacherId where tr.username=%s""" % username
                print "teacher login success";


    db.close()  
    print"<h1> Successful</h1>"

except:
    print"<h1>Error</h1>"

print '</body>'
print '</html>'
