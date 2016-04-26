#!/usr/bin/python

import cgi
import MySQLdb

print "Content-type:text/html\r\n\r\n"
print """
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
			<h4><a >Quiz</a></h4>
		</div>

		<div class = "row">
			<div class = "card-panel col s10 offset-s1" style="padding-top:10px;">
				<div class = "row">
					<form class = "col s12" action = "/cgi-bin/scripts/result.py" method = "post">
						<div id="quiz" class="col s12" style="padding-top:30px;">"""


form=cgi.FieldStorage()
subject =form.getvalue('subject')

try:
	db = MySQLdb.connect('localhost','root','1315','quiz', unix_socket="/opt/lampp/var/mysql/mysql.sock")
	cursor = db.cursor()

	sql = "select questionId,question,optionA,optionB,optionC,optionD from questionBank where subject='%s'" % subject
	cursor.execute(sql)
	var = cursor.fetchall()
	j=cursor.rowcount
	k=1


	for i in var:
		print"""<table>
					<thead>
		            	<tr class="row">
    						<th class="col s1">%d :</th>
				            <th class="col s11">%s</th> <!--question-->
			            </tr>  
			        </thead>
				            <input type="text" name="qid[%d]" value="%d" hidden> 
			        <tbody> 
			            <tr class="row">
				            <td class="input-field col s3"><input type="radio" name="q[%d]" id="a%d" value="a"><label for="a%d">A: %s</label></td> 
				            <td class="input-field col s3"><input type="radio" name="q[%d]" id="b%d" value="b"><label for="b%d">B: %s</label></td> 
				            <td class="input-field col s3"><input type="radio" name="q[%d]" id="c%d" value="c"><label for="c%d">C: %s</label></td> 
				            <td class="input-field col s3"><input type="radio" name="q[%d]" id="d%d" value="d"><label for="d%d">D: %s</label></td> 
				            
			            </tr>
    				</tbody>
    			</table><br><br>"""	% (k,i[1],k,i[0],k,k,k,i[2],k,k,k,i[3],k,k,k,i[4],k,k,k,i[5])	
		k=k+1
	print """<div class = "row center">
				<button class="btn waves-effect waves-light" type="submit" >
					Submit
				</button>
			</div></div>
	            	</form>
	            </div>
	        </div>
	    </div>"""
	db.close()

except:
	print "<script>window.alert('Error')</script>"

print"""
	    </body>
	    </html>"""
