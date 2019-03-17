#Python Project Logs Analysis
import psycopg2

DBNAME = "news"

#connect  to db
connect = psycopg2.connect(database=DBNAME)
# Open a cursor to perform database operations
cur = connect.cursor()
# Execute a command: this creates a new table

--question 1
cur.execute(SELECT log.path, COUNT(*) as num
from log
group by log.path
HAVING log.path = '/article/bad-things-gone' or
       log.path = '/article/balloon-goons-doomed' or
       log.path = '/article/bears-love-berries' or
       log.path = '/article/candidate-is-jerk' or
       log.path = '/article/goats-eat-googles' or
       log.path = '/article/media-obsessed-with-bears' or
       log.path = '/article/trouble-for-troubled' or
       log.path = '/article/so-many-bears'
order by num desc
limit 3;),

--question 2
cur.execute(create view popauth as
    SELECT name, count(*) as num FROM authors
    INNER JOIN articles ON (authors.id = articles.author)
    JOIN log ON (REPLACE(log.path, '/article/', '')=articles.slug)
    group by name
    order by num desc;),

-- question 3
cur.execute(create view statcounta as
  select status as status_fail, time as time_fail, count(*) as errors from log
  where status = '404 NOT FOUND'
  group by status, time
  order by time;

--build ok
create view statcountb as
  select status as status_ok, time as time_ok, count(*) as pass from log
  where status = '200 OK'
  group by status, time
  order by time;

--build combo view

create view statjoin as
  select * from statcounta
  join statcountb on (statcounta.time_fail = statcountb.time_ok)
  group by statcounta.status_fail, statcounta.time_fail,
  statcounta.errors, statcountb.status_ok, statcountb.time_ok, statcountb.pass
  order by statcounta.time_fail;

-- final statement to create percentage calculation
select status_fail, time_fail,
  (select
    (statjoin.errors::float*100)/statjoin.pass::float as percentage) as test
    from statjoin
    group by status_fail, time_fail, test
    order by test;),


# Query the database and obtain data as Python objects
news_fetch = cur.fetchall()
#output returns from Query on sepeate lines
for new_entry in news_fetch:
    print(new_entry)
