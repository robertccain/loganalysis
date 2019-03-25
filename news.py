# Python Project Logs Analysis
# !/usr/bin/env python
# Import psycopg2 tool
import psycopg2
DBNAME = "news"
# connect  to db
connect = psycopg2.connect(database=DBNAME)
# Open a cursor to perform database operations
query_1 = connect.cursor()
# Execute a command: this creates a new table
# question 1
query_1.execute("select * from popauth;")
# 1. What are the most popular three articles of all time?
# Query the database and obtain data as Python objects
news_fetch = query_1.fetchall()
for topArticles in news_fetch:
    print(news_fetch)
connect.close()
# --- Insert a blank line between each question ---
query_2 = connect.cursor()
query_2.execute("select * from popart;")
# 2.Who are the most popular article authors of all time?
# Query the database and obtain data as Python objects
news_fetch_auth = query_2.fetchall()
# output returns from Query on sepeate lines
for TopAuthors in news_fetch_auth:
    print(news_fetch_auth)
connect.close()
# --- Insert a blank line between each question ---
query_3 = connect.cursor()
query_3.execute("select * from final_output;")
# 3. On which days did more than 1% of requests lead to errors?
# Query the database and obtain data as Python objects
news_fetch_error = query_3.fetchall()
# Output returns from Query on sepeate lines
for Perrors in news_fetch_error:
    print(Perrors)
connect.close()
