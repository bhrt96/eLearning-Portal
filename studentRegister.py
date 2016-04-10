#!/usr/bin/python
 
import MySQLdb
import cgi

    
form = cgi.FieldStorage()
#S.no=1
username =form.getvalue('username')
password =form.getvalue('password')
sel =form.getvalue('sel')

try:
    db = MySQLdb.connect('localhost','root','','quiz', unix_socket="/opt/lampp/var/mysql/mysql.sock")

    cursor = db.cursor()
    
    if sel == 'student':
        cursor.execute("""insert into studentRegister (username, password) values (%s,%s)""", (username,password))
    else:
        cursor.execute("""insert into teacherRegister (username, password) values (%s,%s)""", (username,password))
    db.commit()
    #print_header()
    print "data inserted successfully"
    #print_close()

except:
         #print_header()
         print "Error: unable to insert data"
         #print_close()
    
#data = cursor.fetchone()

#print "Database version : %s " % data

db.close()