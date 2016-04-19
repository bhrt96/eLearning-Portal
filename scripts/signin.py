#!/usr/bin/python

import cgi
import MySQLdb
import Cookie
import datetime
import random

cookie = Cookie.SimpleCookie() 
cookie["session"] = random.randint(1,1000000)
expires = datetime.datetime.now() + datetime.timedelta(days=1)
cookie["session"]["expires"] = expires.strftime('%a, %d %b %Y %H:%M:%S') # Wdy, DD-Mon-YY HH:MM:SS GMT
print cookie


print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<body>'
print """<form name="form1" method="POST" action="\cgi-bin\elearning\signin.py">

Username: <input type="text" name="username" id="username" required><br><br>
Password: <input type="password" name="password" id="password" required><br><br>
<input type="radio" name="sel" value="student">student
<input type="radio" name="sel" value="teacher">teacher
<br><br>
<input type="submit"  value="Sign-In" >

</form>"""

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
                cookie["username"]= username
                cookie["password"]= password
                break
        else :
            print "invalid credentials"


    elif sel=='teacher':
        sql="select * from teacherRegister"
        cur.execute(sql)
        var=cur.fetchall()

        for var2 in var:
            if var2[2] == password and var2[1]==username:
                sql="""select subject from teacher as t join teacherRegister as tr on t.TeacherId=tr.TeacherId where tr.username=%s""" % username
                print "teacher login success";
                cookie["username"]=username
                cookie["password"]= password
                cur.execute("""delete from session where username = %s""" , cookie["username"].value)
                cur.execute("""insert into session values (%s, %s)""", (cookie["session"].value,cookie["username"].value))
                print cookie["username"].value
                break
        else :
            print "invalid credentials"

    db.commit()        
    db.close()  

except:
    print"<h1>Error</h1>"

print '</body>'
print '</html>'
