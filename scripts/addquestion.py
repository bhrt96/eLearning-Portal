#!/usr/bin/python

import cgi
import MySQLdb
import Cookie
import os

print "Content-type: text/html\r\n\r\n"
print "<html>"
print "<body>"
print r"""<form name="addqform" method="POST" action="\cgi-bin\elearning\addquestion.py">

Question: <textarea name="question" cols="40" rows="4"></textarea><br><br>
Correct Answer:<input type="text" name="answer" id="answer"><br><br>
Option A: <input type="text" name="optionA" >
Option B: <input type="text" name="optionB" >
Option C: <input type="text" name="optionC" >
Option D: <input type="text" name="optionD" ><br><br>
<input type="submit"  value="Submit" >

</form>"""

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

if(question!= 'Not entered'):

        try:
            if 'HTTP_COOKIE' in os.environ :
                cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
            else :
                print "Please login to continue"

            db = MySQLdb.connect('localhost','root','1315','quiz', unix_socket="/opt/lampp/var/mysql/mysql.sock")
            cur=db.cursor()

            cur.execute("""select username from session where sessionId= %s"""% cookie["session"].value)
            username = cur.fetchone()

            cur.execute("""select teacherId from teacherRegister where username =%s"""%username)
            teacherId=cur.fetchone()

            cur.execute("""select name, subject from teacher where teacherId='%d'"""% teacherId[0])
            var= cur.fetchone()
            cur.execute("""insert into questionBank (question, answer , optionA, optionB, optionC, optionD, subject, setBy) values ('%s', '%s','%s','%s','%s','%s','%s','%s' )""" %(question, answer , optionA, optionB, optionC, optionD, var[1], username[0]))
            print "added successfully"
            db.commit()
        except:
            print "error"

else :
        print "please fill the fields"
print "</body>"
print "</html>"