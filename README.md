# README
===============================================================================
## Welcome to the Web Log Analysis Project.
-------------------------------------------------------------------------------
news.sql houses the sql statements for this project, while news.py holds the python2 program.

There are three questions being addressed:  
  1. What are the most popular three articles of all time?  
  2. Who are the most popular article authors of all time?  
  3. On which days did more than 1% of requests lead to errors?  

The data for this can be found at the following link:
  * [DBFile](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)  

To properly run this program you will need to a working **Virtual Machine**
  * [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
  and a working Vagrant client
  * [Vagrant](https://www.vagrantup.com/downloads.html)
  as well as the following **Vagrant** File loaded into the working directory you are using for this exercise.
  * [VagrantFile](https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile) Put this file in the working directory with news.py and the other files. This is **_VERY important_**. If you do not have this file in the correct directory your Vagrant machine will not work properly... this will results in needless headaches.

Once you have installed your **VirtualBox**, Complete the following tasks:
  * Open a new terminal
  * Change Directory (cd) to your working Directory
  * Execute 'vagrant up'
  * Execute 'vagrant provision'
  * Execute 'vagrant ssh'
  * Execute 'cd /vagrant'
  * This should put you into the correct directory to run the rest of the program
  * If not, you may have nested your copies into another directory and you will need to CD into the correct working directory before proceeding. use 'ls' to list the contents of the directory to check if the data you downloaded above is in the working directory as you expected.

Before you can execute the python **news.py** program locally you first have to run a vagrant session:
  *  $ psql -d news -f newsdata.sql
  *  $ psql -d news -f

You can explore the tables by running:
  * psql news -- this will open a session to explore newsdata.sql
  * \dt  -- This will list the tables in newdata.sql
  * \d table_name [pick any of the table names you see in \dt]

I used views to call the first two queries:
  * create view popart as
      SELECT title, count(* ) as num FROM articles
      INNER JOIN authors ON (authors.id = articles.author)
      JOIN log ON (REPLACE(log.path, '/article/', '')=articles.slug)
      group by title
      order by num desc
      limit 3;

  * create view popauth as
      SELECT name, count(* ) as num FROM authors
      INNER JOIN articles ON (authors.id = articles.author)
      JOIN log ON (REPLACE(log.path, '/article/', '')=articles.slug)
      group by name
      order by num desc;

This was not a requirement. However, I found it made the python sheet cleaner
and easier to manage. It was a personal choice.  

The following views are used to build the last query:
  * create view dateco as
      select path, ip, method, status, id, cast(time as date) from log;

  * create view statcounta as
      SELECT status, time, count(* ) as total from dateco
      GROUP BY status, time
      ORDER BY time;

  * create view statcountb as
      select status as status_fail, time as time_fail, count(* ) as fail from dateco
      WHERE status != '200 OK'
      GROUP BY status_fail, time_fail
      ORDER BY time_fail;

Once these views have been created in psql, leave psql and return to your shell. Now execute **python news.py** and you should return the results. If you do not, there is either a missing view, or again check you working directory.

The results will be in sentence form, but they should match the results below.  

sample.txt holds samples of the data from running the sql statements:
  * Question # 1
    |Path |Num |
    |---|---|
    |Candidate is jerk, alleges rival|338647 |
    |Bears love berries, alleges bear |253801 |
    |Bad things gone, say good people |170098 |
  * Question # 2
    |Name |Num |
    |---|---|
    |Ursula La Multa |507594 |
    |Rudolf von Treppenwitz |423457 |
    |Anonymous Contributor |170098 |
    |Markoff Chaney |84557 |
  * Question # 3
    |status_fail |time_fail |Test |
    |---|---|---|
    |404 NOT FOUND |2016-07-17 |2.31506899455% |
