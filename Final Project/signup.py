#!/usr/bin/python3

import cgi, cgitb 

form = cgi.FieldStorage() 

first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')
email = form.getvalue('email')
phone = form.getvalue('phone')

if form.getvalue('news'):
   news_flag = "YES"
else:
   news_flag = "NO"

if form.getvalue('updates'):
   updates_flag = "YES"
else:
   updates_flag = "NO"
   
if form.getvalue('scores'):
    scores_flag = "YES"
else:
    scores_flag = "NO"
    
if form.getvalue('trades'):
    trades_flag = "YES"
else:
    trades_flag = "NO"

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2>Hello %s %s</h2>" % (first_name, last_name))
print ("<h2>The following will be sent to %s %s</h2>" % (email, phone))
print ("<h2>Get notifications for latest news? %s</h2>" % news_flag)
print ("<h2>Get notifications for latest updates? %s</h2>" % updates_flag)
print ("<h2>Get notifications for daily scores? %s</h2>" % scores_flag)
print ("<h2>Get notifications for new trades? %s</h2>" % trades_flag)

print ("</body>")
print ("</html>")
