#!/Python27/python

import cgi
import MySQLdb

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<body>'


db = MySQLdb.connect('localhost','root','','quiz')  # Your DB details here
cursor = db.cursor()

form=cgi.FieldStorage()

k=int(form.getvalue('rows'))

for i in range(1,k):
	print int(form.getvalue('qid[%d]'%i))
	print form.getvalue('q[%d]'%i)
	sql="""insert into studentanswer(studentId,questionId,answer) values (%d,'%d','%s')""" % (14,int(form.getvalue('qid[%d]'%i)) ,form.getvalue('q[%d]'%i))
	cursor.execute(sql)
	db.commit()	

sql2="""update studentanswer as sa 
		join questionbank as qb on sa.questionId=qb.questionId and sa.answer=qb.answer
		set sa.points = %d """ % (4)

sql3= "update studentanswer set points=0 where answer='none' "



cursor.execute(sql2)
cursor.execute(sql3)
db.commit()	
