#!/usr/bin/python

import MySQLdb
import cgi

print "Content-type:text/html\r\n\r\n"
print r"""
<!doctype html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel = "stylesheet" href = "/css/materialize.css" />
    <script src = "/js/jquery-1.12.2.js"></script>
    <script src = "/js/materialize.js"></script>
</head>
<body class =  "">

    <div class = "row full-height">

        <div class = "row center-align site-name">
            <h4><a >Registration</a></h4>
        </div>

        <div class = "row">
            <div class = "card-panel col s6 offset-s3" style="padding-top:10px;">
                <div class = "row">
                    <form class = "col s12" action = "\cgi-bin\scripts\register.py" method = "post">
                        <div class="row">
                            <div class="input-field col s6">
                                <p>
                                  <input class="with-gap" name="sel" type="radio" value="teacher" id="teacher" onClick="nfunc()" checked/>
                                  <label for="teacher">Teacher</label>
                                </p>
                            </div>
                            <div class="input-field col s6">
                                <p>
                                  <input class="with-gap" name="sel" type="radio" value="student" id="student" onClick="func()"  />
                                  <label for="student" >Student</label>
                                </p>
                            </div>
                        </div>
                        <div class = "row">
                            <div class = "input-field col s12 m12">
                                <input name = "name" id = "first_name" type = "text" required>
                                <label for = "name" class ="">Name</label>
                            </div>
                        </div>
                        <div class = "row" >
                            <div class = "input-field col s12 m12" >
                                <input name = "subject" id = "subject" type = "text" required>
                                <label for="subject">Subject</label>
                            </div>
                        </div>

                        <div class = "row">
                            <div class = "input-field col s12 m12" required>
                                <input name = "college" id = "college" type = "text">
                                <label for="college">College</label>
                            </div>
                        </div>
                        <div class = "row">
                            <div class = "input-field col s12 m6">
                                <input name = "username" id = "username" type = "text" required>
                                <label for="username">Username</label>
                            </div>
                            <div class = "input-field col s12 m6">
                                <input name = "password" id = "password" type = "password" required>
                                <label for="password">Password</label>
                            </div>
                        </div>

                        <div class = "row center">
                            <button class="btn waves-effect waves-light" type="submit" >
                                Submit
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>

    </div>
    
<script>
function func() {
    document.getElementById("subject").disabled = true;
    document.getElementById("subject").value= null;
}
</script>
<script>
function nfunc() {
    document.getElementById("subject").disabled = false;
}
</script>
"""

form = cgi.FieldStorage()
name =form.getvalue('name')
username =form.getvalue('username')
password =form.getvalue('password')
college=form.getvalue('college')
sel = form.getvalue('sel')

if sel=='student' or sel=='teacher':
    try:
        db = MySQLdb.connect('localhost','root','1315','quiz', unix_socket="/opt/lampp/var/mysql/mysql.sock")
        cursor = db.cursor()

        if sel=='teacher':
            sub=form.getvalue('subject')
            cursor.execute("""insert into teacher(name,subject,college) values(%s,%s,%s)""",(name,sub,college))
            cursor.execute("""insert into teacherRegister values(LAST_INSERT_ID(), '%s','%s')""" % ( username,password))
            print "<script>window.alert('Hello: %s');</script>"% name
            print "<script>window.location.assign('http://localhost/cgi-bin/scripts/signin.py');</script>"


        else:
            cursor.execute("""insert into student(name,college) values(%s,%s)""",(name,college))
            cursor.execute("""insert into studentRegister values(LAST_INSERT_ID(), '%s', '%s')""" % (username, password))
            print "<script>window.alert('Hello: %s');</script>"% name
            print "<script>window.location.assign('http://localhost/cgi-bin/scripts/signin.py');</script>"

        db.commit()

    except:
        print "<script>window.alert('Username already exists');</script>" 
        db.rollback()

    db.close()

print '</body>'
print '</html>'