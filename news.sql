--1. What are the most popular three articles of all time?
--
SELECT log.path, COUNT(*) as num
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
limit 3;


--2. Who are the most popular article authors of all time?

create view popauth as
    SELECT name, count(*) as num FROM authors
    INNER JOIN articles ON (authors.id = articles.author)
    JOIN log ON (REPLACE(log.path, '/article/', '')=articles.slug)
    group by name
    order by num desc;



--3. On which days did more than 1% of requests lead to errors?
-- build errors

create view dateco as
  select path, ip, method, status, id, cast(time as date) from log;

create view statcounta as
  select status as status_fail, time as time_fail, count(*) as errors from dateco
  where status = '404 NOT FOUND'
  group by status, time
  order by time;
--build ok
create view statcountb as
  select status as status_ok, time as time_ok, count(*) as pass from dateco
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
    order by test
    where test > 1.0;



"""
-- Every thing in this qoute block was used to during development and testing to build the statements above


-- for reference Testing tables--
-- created view to link authors to titles--
create view countofrecords as
  select articles.author, authors.name, articles.slug
  from authors, articles
  where authors.id = articles.author
  group by authors.name, articles.slug, articles.author
  order by articles.author;

  --individual statements for testing

      select log.path as name, count(*) as Num from log where path = '/article/bad-things-gone' group by name;   
      -- 170098     
      select log.path as name, count(*) as Num from log where path = '/article/balloon-goons-doomed' group by name;
      -- 84557
      select log.path as name, count(*) as Num from log where path = '/article/bears-love-berries' group by name;
      -- 253801
      select log.path as name, count(*) as Num from log where path = '/article/candidate-is-jerk' group by name;
      -- 338647
      select log.path as name, count(*) as Num from log where path = '/article/goats-eat-googles' group by name;
      -- 84906
      select log.path as name, count(*) as Num from log where path = '/article/media-obsessed-with-bears' group by name;
      -- 84383
      select log.path as name, count(*) as Num from log where path = '/article/trouble-for-troubled' group by name;
      -- 84810
      select log.path as name, count(*) as Num from log where path = '/article/so-many-bears' group by name;
      -- 84504   


--gives top author by articles, test table
create view popauth as
      SELECT name, log.path, count(*) as num FROM authors
      INNER JOIN articles ON (authors.id = articles.author)
      JOIN log ON (REPLACE(log.path, '/article/', '')=articles.slug)
      group by log.path, name
      order by num desc;

-- used to view log tables status--
select status, time from log
where status <> '200 OK'
group by status, time;

"""
