#Python Project Logs Analysis
import psycopg2

DBNAME = "news"

#connect  to db
connect = psycopg2.connect(database=DBNAME)
# Open a cursor to perform database operations
cur = connect.cursor()
# Execute a command: this creates a new table

#question 1
cur.execute("select * from log")

# Query the database and obtain data as Python objects
news_fetch = cur.fetchall()
#output returns from Query on sepeate lines
for new_entry in news_fetch:
    print(new_entry)
