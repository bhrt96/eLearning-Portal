#!/usr/bin/python

import MySQLdb
import cgi
import Cookie
import os

if 'HTTP_COOKIE' in os.environ :
    cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
else :
    print "error"


print "Content-type:text/html\r\n\r\n"

db = MySQLdb.connect('localhost','root','1315','quiz', unix_socket="/opt/lampp/var/mysql/mysql.sock")
cursor = db.cursor()

cursor.execute("""select username from session where sessionId= '%s'"""% cookie["session"].value)
username = cursor.fetchone()
if username == None:
    print "<script>window.alert('Please login to continue');</script>"
    print "<script>window.location.assign('/cgi-bin/scripts/signin.py')</script>"

sql = "SELECT DISTINCT subject FROM teacher ORDER BY subject"
cursor.execute(sql)
var = cursor.fetchall()


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

<body background="/elearning/books2.jpg"  class ="">
  <div class="row">
  	 	<div class="white col s12" style="margin:auto">
  	 		<div class="row">
  	 			<div class="col s8">"""


cursor.execute("""select studentId from studentRegister where username ='%s'"""%username)
stId=cursor.fetchone()

cursor.execute("""select name from student where studentId='%d'"""% stId[0])
name= cursor.fetchone()

print"""  	 <h5 class="teal-text">%s</h5>"""% name[0]
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
	  <div class="card-panel col s4 offset-s1" style="margin-top:10%">
	      <div class = "row">
					<form class = "col s12" action = "/cgi-bin/scripts/questions.py" method = "post">
				      	<h4 class="center-align">Subject</h4>
				      	<div class="input-field col s12">
							<select name = "subject" required>
								<option value="" disabled selected>Choose your option</option>""" 

for i in var:
	print """<option value=%s>%s</option>""" %(i[0],i[0])
print"""
							</select>
						</div>
	      				<div class = "row center">
							<button class="btn waves-effect waves-light" type="submit" name="docregister">
								Submit
  							</button>
  						</div>
					</form>
			</div>
		</div>
	</div>
</body>

<script>
$(document).ready(function() {
    $('select').material_select();
  });
</script>
 </html>"""
db.close()
