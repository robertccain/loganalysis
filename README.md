README

Welcome to the Web Log Analysis Project. logsanalysis.sql houses the sql statements for this project, while news.py holds the python2 program.

There are three questions being addressed:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

In the SQL file there are extra select statements not used in the python program that can be run individually if desired for testing purposes.


The data for this can be found at the following link.
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

You can run this python progrma locally by running
  $ psql -d news -f

  you can explore the table by running
  psql news
  \dt
  \d table_name [pick any of the table names you see from \dt]

sample.txt holds samples of the data from running the sql statements:

Question # 1
Path                     	     Num   
/article/candidate-is-jerk  	 338647
/article/bears-love-berries 	 253801
/article/bad-things-gone    	 170098

Question # 2
 Name              	       Num   
 Ursula La Multa        	 507594
 Rudolf von Treppenwitz 	 423457
 Anonymous Contributor  	 170098
 Markoff Chaney         	 84557

Question #3
status_fail  	 time_fail   Test       
404 NOT FOUND  2016-07-17  2.315068995

The following views are used to build the last query:

create view dateco as
  select path, ip, method, status, id, cast(time as date) from log;

create view statcounta as
  select status, time, count(*) as total from dateco
  group by status, time
  order by time;

create view statcountb as
  select status as status_fail, time as time_fail, count(*) as fail from dateco
  where status != '200 OK'
  group by status_fail, time_fail
  order by time_fail;
