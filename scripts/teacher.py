#!/usr/bin/python

import cgi
import MySQLdb
import Cookie
import os

print "Content-type: text/html\r\n\r\n"

form = cgi.FieldStorage()
if form.getvalue('question'):
   question = form.getvalue('question')
else:
   question = "Not entered" 
answer=form.getvalue('answer')
optionA=form.getvalue('optionA')
optionB=form.getvalue('optionB')
optionC=form.getvalue('optionC')
optionD=form.getvalue('optionD')
qid= form.getvalue('qid')

if 'HTTP_COOKIE' in os.environ :
    cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
else :
    print "error"

db = MySQLdb.connect('localhost','root','1315','quiz', unix_socket="/opt/lampp/var/mysql/mysql.sock")
cur=db.cursor()

cur.execute("""select username from session where sessionId= '%s'"""% cookie["session"].value)
username = cur.fetchone()
if username == None:
    print "<script>window.alert('Please login to continue');</script>"
    print "<script>window.location.assign('/cgi-bin/scripts/signin.py')</script>"
# print cookie['session'].value


if(question!= 'Not entered'):

            cur.execute("""select teacherId from teacherRegister where username ='%s'"""%username)
            teacherId=cur.fetchone()

            cur.execute("""select name, subject from teacher where teacherId='%d'"""% teacherId[0])
            var= cur.fetchone()
            cur.execute("""insert into questionBank (question, answer , optionA, optionB, optionC, optionD, subject, setBy) values ('%s', '%s','%s','%s','%s','%s','%s','%s' )""" %(question, answer , optionA, optionB, optionC, optionD, var[1], username[0]))
            db.commit()

if(qid!='None'):
            cur.execute("""delete from questionBank where questionId='%s'"""%qid)
            db.commit()

sql = "select * from questionBank where setBy='%s'" % username
cur.execute(sql)
var = cur.fetchall()
j=cur.rowcount
k=1

print """
<!doctype html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link rel = "stylesheet" href = "/css/materialize.css" />
    <script src = "/js/jquery-1.12.2.js"></script>
    <script src = "/js/materialize.js"></script>
</head>
<body class =  "">

    <div class = "row">

        <div class = "row center-align site-name">
            <h4><a >QuestionBank</a></h4>
        </div>
        <div class="col s12">
            <div class="row">
                <div class="col s8">"""


cur.execute("""select teacherId from teacherRegister where username ='%s'"""%username)
stId=cur.fetchone()

cur.execute("""select name from teacher where teacherId='%d'"""% stId[0])
name= cur.fetchone()

print"""     <h5>%s</h5>"""% name[0]
print"""     
            </div>
            <div class = " col s2" id = "page-controls">
                <p class = "right-align" style="margin-right:-200px">
                    <a href = "/cgi-bin/scripts/signin.py" class = " tooltipped " data-position="bottom" data-delay="50" data-tooltip="Logout" style="cursor:pointer">
                        <i class = "material-icons">power_settings_new</i>
                    </a> 
                </p>
            </div>
        </div>
        </div>
        <div class = "row">
        <div class = "card-panel col s6" style="padding-top:15px;">
                <h5>Added Questions</h5>"""

for i in var:
    print """
                    <table>
                        <thead>
                            <tr>
                                <th>Ques id: %d ::</th>
                                <th>%s</th> <!--question-->
                            </tr>  
                        </thead>
                        <tbody> 
                            <tr>
                                <td>A: %s</td> 
                                <td>B: %s</td> 
                                <td>C: %s</td> 
                                <td>D: %s</td>
                            </tr>
                            <tr>
                                <td>Answer: %s</td>
                            </tr>
                            <br>
                        </tbody>
                    </table>
                """  % (i[0],i[1],i[3],i[4],i[5],i[6],i[2]) 
    k=k+1
print "</div>"

print r"""<div class ="card-panel col s6" style="padding-top:10px;">
                <h5>Add Question</h5>
                    <form name="addqform" method="POST" action="/cgi-bin/scripts/teacher.py" >
                    Question: <textarea class="materialize-textarea" name="question"></textarea><br><br>
                    Correct Answer: <input type="text" name="answer" id="answer"><br><br>
                    Option A: <input type="text" name="optionA" >
                    Option B: <input type="text" name="optionB" >
                    Option C: <input type="text" name="optionC" >
                    Option D: <input type="text" name="optionD" ><br><br>
                    <div class = "row ">
                        <button class="btn waves-effect waves-light" type="submit" target="/cgi-bin/scripts/teacher.py">
                            Submit
                        </button>
                    </div>
                    </form><br><br>
                    <h5>Delete Question</h5>
                    <form name="delqform" method="get" action="/cgi-bin/scripts/teacher.py" >
                    Question ID : <input type="text" name="qid" >
                    <div class = "row ">
                        <button class="btn waves-effect waves-light" type="submit" target="/cgi-bin/scripts/teacher.py">
                            Submit
                        </button>
                    </div>
                    </form>
            </div>
        </div>
    </div>
</body>
</html>"""

db.close()