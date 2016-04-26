#!/usr/bin/python

import MySQLdb
import cgi

print "Content-type:text/html\r\n\r\n"

db = MySQLdb.connect('localhost','root','1315','quiz', unix_socket="/opt/lampp/var/mysql/mysql.sock")
cursor = db.cursor()

sql = "SELECT DISTINCT subject FROM teacher ORDER BY subject"
cursor.execute(sql)
var = cursor.fetchall()

print r"""
<!doctype html>
<html>

<head>
	<meta name="viewport" content="width=device-width, initial-scale=1" />
	<link rel = "stylesheet" href = "/css/materialize.css" />
	<script src = "/js/jquery-1.12.2.js"></script>
	<script src = "/js/materialize.js"></script>
</head>

<body class =  "grey">
  <div class="row">
	  <div class="card-panel col s4 offset-s4" style="margin-top:15%">
	      <div class = "row">
					<form class = "col s12" action = "\cgi-bin\scripts\questions.py" method = "post">
				      	<h4 class="center-align">Subject</h4>
				      	<div class="input-field col s12">
							<select name = "subject" required>
								<option value="" disabled selected>Choose your option</option>"""

for i in var:
	print """<option value=%s>%s</option>""" %(i[0],i[0])
print"""
								<option value="maths">maths</option>
								<option value="">sps</option>
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
