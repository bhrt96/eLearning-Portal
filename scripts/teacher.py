#!/usr/bin/python

import cgi
import MySQLdb
import Cookie
import os

print "Content-type: text/html\r\n\r\n"
print "<html>"
print "<body>"

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
    print "Please login to continue"

db = MySQLdb.connect('localhost','root','1315','quiz', unix_socket="/opt/lampp/var/mysql/mysql.sock")
cur=db.cursor()

cur.execute("""select username from session where sessionId= '%s'"""% cookie["session"].value)
username = cur.fetchone()

if(question!= 'Not entered'):

            cur.execute("""select teacherId from teacherRegister where username ='%s'"""%username)
            teacherId=cur.fetchone()

            cur.execute("""select name, subject from teacher where teacherId='%d'"""% teacherId[0])
            var= cur.fetchone()
            cur.execute("""insert into questionBank (question, answer , optionA, optionB, optionC, optionD, subject, setBy) values ('%s', '%s','%s','%s','%s','%s','%s','%s' )""" %(question, answer , optionA, optionB, optionC, optionD, var[1], username[0]))
            print "added successfully"
            db.commit()

if(qid!='None'):
            cur.execute("""delete from questionBank where questionId='%s'"""%qid)
            db.commit()

sql = "select * from questionBank where setBy='%s'" % username
cur.execute(sql)
var = cur.fetchall()
j=cur.rowcount
k=1


for i in var:   
    print """<table><form action="" method="">                                                                                                                                                      
            <tr>
            <th>Ques id:%d </th>
            <th>Question: %s</th>
            </tr>   
            <tr>
            <td>A: %s<!--input type="text" name="" value="a"--></td> 
            <td>B: %s<!--input type="text" name="" value="b"--></td> 
            <td>C: %s<!--input type="text" name="" value="c"--></td> 
            <td>D: %s<!--input type="text" name="" value="d"--></td>
            </tr>
            <tr>
            <td>Answer: %s<!--input type="text" name="" value=""--></td>
            </tr></table>""" % (i[0],i[1],i[3],i[4],i[5],i[6],i[2])
    print '<br>'
    k=k+1

print r"""<h4>Add Question</h4>
<form name="addqform" method="POST" action="\cgi-bin\elearning\addquestion.py" >
Question: <textarea name="question" cols="100" rows="2"></textarea><br><br>
Correct Answer: <input type="text" name="answer" id="answer"><br><br>
Option A: <input type="text" name="optionA" >
Option B: <input type="text" name="optionB" >
Option C: <input type="text" name="optionC" >
Option D: <input type="text" name="optionD" ><br><br>
<input type="submit"  value="Submit" target="\cgi-bin\elearning\addquestion.py">
</form>"""

print r"""<h4>Delete Question</h4>
<form name="delqform" method="get" action="\cgi-bin\elearning\addquestion.py" >
Question ID : <input type="text" name="qid" >
<input type="submit"  value="Submit" target="\cgi-bin\elearning\addquestion.py">
</form>"""

db.close()

print "</body>"
print "</html>"