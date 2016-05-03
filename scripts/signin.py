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
# print '<html>'
# print '<body>'
# print """<form name="form1" method="POST" action="\cgi-bin\scripts\signin.py">

# Username: <input type="text" name="username" id="username" required><br><br>
# Password: <input type="password" name="password" id="password" required><br><br>
# <input type="radio" name="sel" value="student">student
# <input type="radio" name="sel" value="teacher">teacher
# <br><br>
# <input type="submit"  value="Sign-In" >

# </form>"""
print r"""
<!doctype html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel = "stylesheet" href = "/css/materialize.css" />
    <script src = "/js/jquery-1.12.2.js"></script>
    <script src = "/js/materialize.js"></script>
</head>
<body background="/elearning/books2.jpg" class ="" >

    <div class = "row " style="padding-top:8%">
        <div class = "row">
            <div class = "card-panel col s4 offset-s1 " >
                <div class = "row">
                    <form class = "col s12" action = "\cgi-bin\scripts\signin.py" method = "post">
                        <div class="row">
                            <div class = "center-align">
                                <h4><a >Log In</a></h4>
                            </div>
                            <div class="input-field col s6">
                                <p>
                                  <input class="with-gap" name="sel" type="radio" value="teacher" id="teacher"  checked/>
                                  <label for="teacher">Teacher</label>
                                </p>
                            </div>
                            <div class="input-field col s6">
                                <p>
                                  <input class="with-gap" name="sel" type="radio" value="student" id="student"  />
                                  <label for="student" >Student</label>
                                </p>
                            </div>
                        </div>
                        <div class = "row">
                            <div class = "input-field col s12 ">
                                <input name = "username" id = "username" type = "text" required>
                                <label for="username">Username</label>
                            </div>
                            <div class = "input-field col s12 ">
                                <input name = "password" id = "password" type = "password" required>
                                <label for="password">Password</label>
                            </div>
                        </div>
                        <div class = "row">
                            <button class="btn waves-effect waves-light" type="submit" >
                                Submit
                            </button>
                        </div>
                    </form>
                        <div class="row right">
                            <a class="blue-text" href="/cgi-bin/scripts/register.py">New user? Click here to register</a>
                        <div>
                </div>
            </div>
        </div>

    </div>"""


form=cgi.FieldStorage()
username =form.getvalue('username')
password =form.getvalue('password')
sel = form.getvalue('sel')

db = MySQLdb.connect('localhost','root','1315','quiz', unix_socket="/opt/lampp/var/mysql/mysql.sock")
cur=db.cursor()

cur.execute("""delete from session where sessionId= '%s'"""% cookie["session"].value)
db.commit()
try:


    if sel=='student':
        sql="select * from studentRegister"
        cur.execute(sql)
        var=cur.fetchall()

        for var2 in var:
            if var2[2] == password and var2[1]==username:
                cookie["username"]= username
                cookie["password"]= password
                cur.execute("""delete from session where username = %s""" , cookie["username"].value)
                cur.execute("""insert into session values (%s, %s)""", (cookie["session"].value,cookie["username"].value))
                print "<script>window.location.assign('/cgi-bin/scripts/choosesubject.py');</script>"
                break
        else :
            print "<script>window.alert('Invalid credentials');</script>"


    elif sel=='teacher':
        sql="select * from teacherRegister"
        cur.execute(sql)
        var=cur.fetchall()

        for var2 in var:
            if var2[2] == password and var2[1]==username:
                sql="""select subject from teacher as t join teacherRegister as tr on t.TeacherId=tr.TeacherId where tr.username=%s""" % username
                cookie["username"]=username
                cookie["password"]= password
                cur.execute("""delete from session where username = %s""" , cookie["username"].value)
                cur.execute("""insert into session values (%s, %s)""", (cookie["session"].value,cookie["username"].value))
                print "<script>window.location.assign('/cgi-bin/scripts/teacher.py');</script>"
                break
        else :
            print "<script>window.alert('Invalid credentials');</script>"

    db.commit()        
    db.close()  

except:
    print"<h1>Error</h1>"

print '</body>'
print '</html>'
