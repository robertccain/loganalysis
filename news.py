# Python Project Logs Analysis
# !/usr/bin/env python
for python2
# Import psycopg2 tool
import psycopg2
DBNAME = "news"
# connect  to db
connect = psycopg2.connect(database=DBNAME)
# Open a cursor to perform database operations
cur = connect.cursor()
# Execute a command: this creates a new table
# question 1
cur.execute("select * from popauth;)"
# 1. What are the most popular three articles of all time?
# Query the database and obtain data as Python objects
news_fetch_art=cur.fetchall()
# Output returns from Query on sepeate lines
for top_articles in news_fetch_art:
    print(top_articles)
connect.close()
#        --- Insert a blank line between each question ---
# question 2
cur = connect.cursor()
cur.execute("select * from popart;)"
# 2. Who are the most popular article authors of all time?
# Query the database and obtain data as Python objects
news_fetch_auth=cur.fetchall()
# output returns from Query on sepeate lines
for top_auth in news_fetch_auth:
    print(top_auth)
connect.close()
#           --- Insert a blank line between each question ---
# Question 3
# 3. On which days did more than 1% of requests lead to errors?
cur = connect.cursor()
cur.execute("select * from final_output;")
# Query the database and obtain data as Python objects
news_fetch_error=cur.fetchall()
# Output returns from Query on sepeate lines
for Perrors in news_fetch_error:
    print(Perrors)
connect.close()
#            --- Insert a blank line ---

