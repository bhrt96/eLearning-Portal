#!/usr/bin/python

import cgi
import MySQLdb
import Cookie
import os

print "Content-type:text/html\r\n\r\n"

if 'HTTP_COOKIE' in os.environ :
    cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
else :
    print "Please login to continue"

db = MySQLdb.connect('localhost','root','1315','quiz', unix_socket="/opt/lampp/var/mysql/mysql.sock")
cursor = db.cursor()

cursor.execute("""select username from session where sessionId= '%s'"""% cookie["session"].value)
username = cursor.fetchone()
if username == None:
    print "<script>window.alert('Please login to continue');</script>"
    print "<script>window.location.assign('/cgi-bin/scripts/signin.py')</script>"


cursor.execute("""select StudentId from studentRegister where username ='%s' """%username)
StudentId=cursor.fetchone()
#StudentId=int(studentid)

form=cgi.FieldStorage()

k=int(form.getvalue('rows'))




#inserting values in studentAnswer table from form
for i in range(1,k):
	sql="""insert into studentAnswer(StudentId,questionId,answer) values ( %d,'%d','%s')""" % ((StudentId[0]),int(form.getvalue('qid[%d]'%i)) ,form.getvalue('q[%d]'%i))
	cursor.execute(sql)
	db.commit()


#setting points to 4 for correct answer in studentAnswer table
sql2="""update studentAnswer as sa 
		join questionBank as qb on sa.questionId=qb.questionId and sa.answer=qb.answer
		set sa.points = %d """ % (4)
cursor.execute(sql2)
db.commit()

#setting points to 4 for correct answer in studentAnswer table
sql3= "update studentAnswer set points=0 where answer='none' "
cursor.execute(sql3)
db.commit()             

sql4= """select subject from questionBank where questionId=%d"""%int(form.getvalue('qid[1]'))
cursor.execute(sql4)
sub=cursor.fetchone()

#obtaining marks scored
sql5="""select sum(points) from studentAnswer as sa join questionBank as qb on sa.questionId=qb.questionId where StudentId=%d and subject='%s'"""%(StudentId[0],sub[0])
cursor.execute(sql5)
marks=cursor.fetchone()

#obtaining max marks
sql6="""select * from studentAnswer as sa join questionBank as qb on sa.questionId=qb.questionId where StudentId=%d and subject='%s' """%(StudentId[0],sub[0])
cursor.execute(sql6)
mm1=cursor.rowcount
mm=4*mm1

perc=(marks[0]/mm)*100

if(perc > 33.0):
	result="pass"
else:
	result="fail"

#inserting values in result table
sql8= """insert into result(StudentId,subject,marks,max_marks,percent,result) values(%d,'%s','%d','%d','%f','%s')"""%(StudentId[0],sub[0],marks[0],mm,perc,result)
cursor.execute(sql8)
db.commit()

#calculating number of correct answers
sql9="""select * from studentAnswer as sa join questionBank as qb on sa.questionId=qb.questionId where StudentId=%d and points=%d and subject='%s' """%(StudentId[0],4,sub[0])
cursor.execute(sql9)
correct=cursor.rowcount

#calculating number of unattempted questions
sql9="""select * from studentAnswer as sa join questionBank as qb on sa.questionId=qb.questionId where StudentId=%d and points=%d and subject='%s' """%(StudentId[0],0,sub[0])
cursor.execute(sql9)
not_att=cursor.rowcount

#calculating number of wrong answers
sql10="""select * from studentAnswer as sa join questionBank as qb on sa.questionId=qb.questionId where StudentId=%d and points=%d and subject='%s' """%(StudentId[0],-1,sub[0])
cursor.execute(sql10)
wrong=cursor.rowcount

print"""
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

		<div class = "row full-height">
"""



print """<div class="col s12  grey lighten-2">
            <div class="row ">
                <div class="col s8">"""


cursor.execute("""select studentId from studentRegister where username ='%s'"""%username)
stId=cursor.fetchone()

cursor.execute("""select name from student where studentId='%d'"""% stId[0])
name= cursor.fetchone()

print"""     <h5>%s</h5>"""% name[0]
print""" <h6 style="text-transform:uppercase;">RESULT : <b>%s</b></h6>"""% result
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
        </div><br>"""

print"""<div class = "row">
        <div class = "card-panel col s4" style="padding-top:15px;">
                    <table class="centered striped">
                        <thead>
                            <tr>
                                <th>Your Response</th>
                                <th>Correct Response</th>
                            </tr>  
                        </thead>
                        <tbody> """
        
sql11= """select qb.answer,sa.answer from questionBank as qb join studentAnswer as sa on qb.questionId=sa.questionId where StudentId=%d and subject='%s' """%(StudentId[0],sub[0])
cursor.execute(sql11)
var=cursor.fetchall()

k=0

for var2 in var:
    print """
                            <tr>
                                <td>%s</td> 
                                <td>%s</td> 
                            </tr>
                """  % (var2[1],var2[0]) 
    k=k+1
print "</tbody></table></div>"
print """<div class="col s8 " id="piechart" style="width: 800px; height: 500px; margin-left:50px"></div>"""

print"""<div class = "row">
        <div class = "card-panel col s12" style="padding-top:15px;">
        <h4 class="center-align teal-text ">Previous Quizzes</h4>
                    <table class="centered striped">
                        <thead>
                            <tr>
                                <th>Subject</th>
                                <th>Marks Obtained</th>
                                <th>Maximum Marks</th>
                                <th>Percentage</th>
                                <th>Result</th>
                            </tr>  
                        </thead>
                        <tbody> """
        
sql12="""select * from result where StudentId=%d"""%(StudentId[0])
cursor.execute(sql12)
history=cursor.fetchall()


for var2 in history:
    print """
                            <tr>
                                <td>%s</td>
                                <td>%s</td>
                                <td>%s</td>
                                <td>%s</td> 
                                <td style="text-transform:uppercase;">%s</td> 
                            </tr>
                """  % (var2[1],var2[2],var2[3],var2[4],var2[5]) 
    k=k+1
print "</tbody></table></div>"


# print "<table border='1'>"
# print "<th>your Response: </th>"
# print "<th>Correct Answer: </th>"
# for var2 in var:
# 	print "<tr>"
# 	print "<td>"
# 	print var2[1]
# 	print "</td>"
# 	print "<td>"
# 	print var2[0]
# 	print "</td>"
# 	print "</tr>"
# print "<p>Student exam history</p>"


# print "<table border='1'>"
# print "<th> Subject</th>"
# print "<th>Marks</th>"
# print "<th>Total</th>"
# print "<th>Percentage</th>"
# print "<th>Result</th>"

# for var2 in history:
# 	print "<tr>"
# 	print "<td>"
# 	print var2[1]
# 	print "<td>"
# 	print var2[2]
# 	print "<td>"
# 	print var2[3]
# 	print "<td>"
# 	print var2[4]
# 	print "<td>"
# 	print var2[5]
# 	print "</tr>"

print "<div></body>"
#script for pie chart
print """<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);
      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          ['Response', 'Number'],
          ['Correct',%d],
          ['Not attempted',%d],
          ['Wrong',%d]
        ]);

        var options = {
          title: 'Detailed Marksheet'
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart'));

        chart.draw(data, options);
      }
    </script>"""% (correct,not_att,wrong)
print "</html>"