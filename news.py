# !/usr/bin/env python
# Import psycopg2 tool
import psycopg2
DBNAME = "news"
# connect  to db
connect = psycopg2.connect(database=DBNAME)
# Open a cursor to perform database operations
q1 = connect.cursor()
# Execute a command: this creates a new table
# question 1
q1.execute("select * from popart;")
query1 = "What are the most popular three articles of all time? {}, {} views."
# Query the database and obtain data as Python objects
news_fetch = q1.fetchall()
for title, num in news_fetch:
    print query1.format(title, num)
connect.close()
# --- Insert a blank line between each question ---
print''
con = psycopg2.connect(database=DBNAME)
q2 = con.cursor()
q2.execute("select * from popauth;")
query2 = "2.Who are the most popular article authors of all time?{}, {} views."
# Query the database and obtain data as Python objects
news_fetch_auth = q2.fetchall()
# output returns from Query on sepeate lines
for name, num in news_fetch_auth:
    print query2.format(name, num)
con.close()
# --- Insert a blank line between each question ---
print''
c = psycopg2.connect(database=DBNAME)
q3 = c.cursor()
q3.execute("select * from final_output where test > 1.0;")
query3 = "3. On which days did more than 1% of requests lead to errors? {},{}%"
# Query the database and obtain data as Python
# objects  final_output where test > 1.0
news_fetch_error = q3.fetchall()
# Output returns from Query on sepeate lines
for status, date, test in news_fetch_error:
    print query3.format(date, test)
c.close()
