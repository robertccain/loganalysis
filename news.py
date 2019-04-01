# !/usr/bin/env python
# Import psycopg2 tool
import psycopg2
import datetime

DBNAME = "news"
# connect  to db
print('-----------------------START OF REPORT--------------------------------')
print('')
try:
    connect = psycopg2.connect(database=DBNAME)
except psycopg2.Error as e:
    print "Unable to connect!"
    print (e.pgerror)
    print (e.diag.message_detail)
    sys.exit(1)
else:
    print ("Connected!")
# Open a cursor to perform database operations
q1 = connect.cursor()
# Execute a command: this creates a new table
# question 1
q1.execute("select * from popart;")
query1 = "What are the most popular three articles of all time?"
print(query1)
# Query the database and obtain data as Python objects
news_fetch = q1.fetchall()
for title, num in news_fetch:
    print("{} -- {} views".format(title, num))
#    print query1.format(title, num)
connect.close()
# --- Insert a blank line between each question ---
print('')
try:
    con = psycopg2.connect(database=DBNAME)
except psycopg2.Error as e:
    print ("Unable to connect!")
    print (e.pgerror)
    print (e.diag.message_detail)
    sys.exit(1)
else:
    print "Connected!"
q2 = con.cursor()
q2.execute("select * from popauth;")
query2 = "Who are the most popular article authors of all time?"
print(query2)
# Query the database and obtain data as Python objects
news_fetch_auth = q2.fetchall()
# output returns from Query on sepeate lines
for name, num in news_fetch_auth:
    print("{} -- {} views".format(name, num))
con.close()
# --- Insert a blank line between each question ---
print('')
try:
    c = psycopg2.connect(database=DBNAME)
except psycopg2.Error as e:
    print "Unable to connect!"
    print (e.pgerror)
    print (e.diag.message_detail)
    sys.exit(1)
else:
    print ("Connected!")
q3 = c.cursor()
q3.execute("select * from final_output where (test > 1.0 AND test < 99);")
query3 = "On which days did more than 1% of requests lead to errors? {}, {}%"
# Query the database and obtain data as Python
# objects  final_output where test > 1.0
news_fetch_error = q3.fetchall()
# Output returns from Query on sepeate lines
for status, date, test in news_fetch_error:
    print(query3.format(date, test))
c.close()
print('')
curtime = datetime.datetime.now()
print('Report as of {}').format(curtime)
print('')
print('-----------------------END OF REPORT--------------------------------')
