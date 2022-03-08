-- mysql is a database,mysql workbench is UI to connect to a database using SQL language
-- you can query different databases like oracle,postgres,sql server ,mysql using SQL 
-- your sql commands are called as queries
-- mysql is called as relational database
-- our data is stored in the formt of table: rows and columns

/* emp empid,fname,lname,salary,loc,age-- column/attributes
    1,'a','b',1000,'pune',25. -- row
    
emp dept
one-to-one -- one emp belongs to single dept
one-to-many -- one emp is working on multiple projects
many-to-one -- multiple employees are working on a single project */

-- comments in sql
-- : used to give single line comment 
/* multiline 
comment */

-- Create database
create database db_nov; -- d1,t1,p1
-- development,test,production

-- show database
show databases;

-- use database
use db_nov;

-- show tables
show tables;

-- Create a table
-- create table <tbl_name> (col1 datatype,col2 datatype,col3 datatype.....coln datatype)

create table emp (empid int,fname varchar(10),lname varchar(10),
age int,salary int,loc varchar(10));

/* char(size): fixed length,will occupy the exact bytes of memory into your system regardless of your data
varchar(size) : variable length,will occupy the memory space as per ur data */

-- select : only used to retrive /see the data
select * from emp;
select empid from emp; 
select `emp id` from emp;

-- insert data
-- insert into emp <column_list> values <row1>;
insert into emp values(1001,'snehal','more',25,40000,'pune');
select * from emp;
insert into emp (empid,fname,lname,age,salary,loc) 
values(1007,'mayur','abole',24,50000,'pune');

-- insert single value
insert into emp (empid,fname,lname,age,salary) values(1002,'sneha','biradar',26,40000);
-- insert multiple values using single insert statement
insert into emp values(1004,'mayura','namjoshi',28,80000,'mumbai'),
					  (1005,'saurabh','joshi',29,60000,'mumbai'),
                      (1006,'swapnil','kendre',24,30000,'mumbai');
                    
select * from emp;

-- describe table
desc emp;

-- alter
-- add column
alter table emp add column contact varchar(10);
desc emp;
select * from emp;

-- delete column
alter table emp drop column contact;

-- modify column
alter table emp modify column contact int;

-- where : to filter out your result set
select * from emp;
select * from emp where empid=1001;
select empid,fname from emp where empid=1001;

select * from emp where empid in (1001,1002);
select * from emp where empid not in (1001,1002);
select * from emp where empid in (1006,1007);

select * from emp where salary <50000;

select * from emp where loc is null;

select * from emp where loc is not null;
select * from emp where fname='mayur' and lname='gaonkar';
select * from emp;
select * from emp where fname='mayur' or fname='mayura';

select * from emp where not age=24;
select * from emp where salary between 40000 and 65000;
select * from emp where salary not between 40000 and 65000;

-- count : row count
select count(*) from emp;
select count(1) from emp;
select count(empid) from emp;

-- distinct : distinct values present in ur column
select distinct fname from emp;

-- alias : dummy name to your table or column
select fname as first_name from emp;
select * from emp e;

/* import pandas as pd
pandas.read_csv
pd.read_csv */

-- like operator
/* % -- 0 or more charecters
_ -- single charecter */
select * from emp;
select * from emp where empid=1001;
select * from emp where fname like 'm%';
select * from emp where fname like '_a%';

-- delete : will delete all the data from table ,if where condition is not given
-- truncate : it will delete all data from your table
-- drop   : it will delete data as well as your table structue

select * from emp;
delete from emp where loc is null;
delete from emp; -- deletes whole data
truncate table emp; -- will delete whole data
drop table emp; -- delete data as well as structure

drop database db_new; 

-- database is simillar to schema
create database db_new;
create schema db_new;

-- update
select * from emp;
update emp set age=25 where empid=1006;

-- order by : default order is ascending
select * from emp order by age;
select * from emp order by salary;
select * from emp order by age,salary;
select * from emp order by age desc;

 
/* database
create db
create table
insert
select
alter
like
alias
count
comments: single line,multiline
where
desc
delete
truncate
drop
is null
is not null
in 
not in
update
distinct
between
and,or,not,>,<,>=,<=
order by */

/* database -- d1,t1,p1 -- database objects --
-- stores large amount of data
-- relation between different objects */

create table details (command varchar(20),description varchar(100),syntax varchar(50));












    
