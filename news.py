--1. What are the most popular three articles of all time?--
create view popart as
  SELECT title, count(*) as num FROM articles
  INNER JOIN authors ON (authors.id = articles.author)
  JOIN log ON (REPLACE(log.path, '/article/', '')=articles.slug)
  group by title
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
create view dateco as
  select path, ip, method, status, id, cast(time as date) from log;

create view stat_all as
  select status, time as date, count(*) as total from dateco
  group by status, date
  order by date;
--build ok
create view stat_fail as
  select status as status_fail, time as date_fail, count(*) as fail from dateco
  where status != '200 OK'
  group by status_fail, date_fail
  order by date_fail;

-- final statement to create percentage calculation
create view final_output as
select stat_fail.status_fail as status, stat_fail.date_fail as date,
  (select
    (((stat_fail.fail::float)/stat_all.total::float)*100) as percentage) as test
    from stat_fail
    join stat_all on stat_all.date = stat_fail.date_fail
    group by stat_fail.status_fail, stat_fail.date_fail, test
    order by test;
