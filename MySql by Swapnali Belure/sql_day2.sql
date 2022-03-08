-- constraints in SQL
-- constraints are used to set some rules on your table data

-- NOT NULL : you can not have NULL value in that column,empid
use db_nov;
desc emp;
create table emp_not_null(empid int NOT NULL,fname varchar(10),lname varchar(10));
desc emp_not_null;
insert into emp_not_null values(1001,'sneha','B');
select * from emp_not_null;
insert into emp_not_null values(NULL,'snehal','S');

insert into emp_not_null (fname,lname) values('abhi','mehra');

alter table emp modify empid int NOT NULL;

-- UNIQUE constraint: every value should be different/unique,duplicates are not allowed,NULL allowed
create table emp_unq (empid int ,fname varchar(10),unique (empid));
desc emp_unq;
insert into emp_unq values(1001,'vaibhavi'); -- if you will try to insert same empid again, you will get an error
select * from emp_unq;

insert into emp_unq values(NULL,'vaibhavi');

alter table emp ADD CONSTRAINT my_unq unique(empid);
-- alter table <tbl_name> ADD CONSTRAINT <constraint_name> unique(col_name)

-- CHECK constraint : you can specify a condition on any column 
create table emp_chk (empid int,fname varchar(10),age int,CHECK (age>20));
desc emp_chk;
insert into emp_chk values(1001,'snehal',25);
select * from emp_chk;

insert into emp_chk values(1001,'snehal',18);

alter table emp ADD CONSTRAINT my_unq unique(empid);
alter table emp ADD CONSTRAINT my_chk check(age>20);
desc emp;

-- primary key: this identifies a row uniquely,duplicates are not allowed,NULL are also not allowed
-- primary key can consist of more than one column,you can call it as composite key
create table emp_pk (empid int,fname varchar(10),primary key (empid));
desc emp_pk;
insert into emp_pk values(1001,'Guru');
select * from emp_pk;

insert into emp_pk values(1001,'Gauri');

insert into emp_pk values(null,'Gauri');

alter table emp add constraint my_pk primary key (empid);
desc emp;

-- 
/* NOT NULL : NULL value not allowed
unique : dups not allowed but NULL values are allowed
primary key : dups and NULL both are not allowed */

-- create a backup table
create table emp_bkp as select * from emp;
select * from emp;
select * from emp_bkp;

-- Default : default arguments
create table emp_df(empid int,fname varchar(10),dept varchar(10) DEFAULT 'Bench');
desc emp_df;
insert into emp_df (empid,fname) values (1001,'sushil');
select * from emp_df;

insert into emp_df (empid,fname,dept) values (1001,'sushil','HR');

alter table emp alter empid set default 1001;
desc emp;

-- drop constraint 
-- alter table emp DROP CONSTRAINT <constraint_name>;

-- CASE STATEMENT : if else
select * from emp;
select empid,fname,lname,age ,
CASE 
WHEN AGE >25 THEN 'SR PROFILE'
WHEN AGE=25 THEN 'MID EXP'
ELSE 'FRESHER'
END 
AS ELIGIBILTY
FROM EMP;

alter table emp add column contact varchar(10);

INSERT INTO EMP VALUES (1007,'swap','k',21,40000,'pune');

update emp set contact = 
CASE empid
WHEN  1004 then 9876756785
WHEN  1005 then 7898765678
WHEN  1006 then 9876756788
WHEN  1007 then 9845678534
END;

select * from emp;

-- Auto increment: generate unique value for each entry,auto increment key should be defined as primary key
create table emp_AI(empid int AUTO_INCREMENT,fname varchar(10),primary key (empid));
insert into emp_AI (fname) values('swarup');
select * from emp_AI;
insert into emp_AI (fname) values('swarupa');

alter table emp_AI AUTO_INCREMENT =1001;

alter table emp modify column empid varchar(10);
insert into emp_AI (fname) values('dhiraj');
alter table emp_AI AUTO_INCREMENT ='A001'; -- char are not allowed in auto increment column

insert into emp_AI (fname) values('niraj');

-- limit : limits the row count of your result set
select * from emp limit 2;
select * from emp order by salary limit 2;

-- primary key and foreign key: used to define. arelationship between two tables
-- foreign key is the column which references primary key of another table

/* student : rollno,name,address 
course : courseid,coursename,rollno */

create table student (rollno int,name varchar(10),primary key (rollno));
desc student; -- parent table, referenced table

create table course (courseid int,coursename varchar(10),primary key (courseid),
rollno int,
foreign key (rollno) references student(rollno));
desc course;  -- child table, referencing table

-- you will not be able to add a value in your child table which is not present in parent table
insert into student values (101,'vishal');
select * from student;
insert into course values (10,'testing',101);

insert into course values (20,'DS',102); -- will not be allowed

-- you will not be able to delete a row from parent table directly
delete from student where rollno=101; -- this will not work
delete from course where rollno=101;

delete from student where rollno=101;

-- Group by : to create groups on the basis of some column
select * from emp;
select loc from emp group by loc ; -- to fetch distinct values from ur column
select distinct loc from emp;

select loc,count(1) from emp group by loc; -- columns in select hould alwys be present in group by

select loc,count(1) from emp group by loc,empid; 

-- write a query to find duplicates

select loc ,count(1) from emp group by loc where count(1)>1; -- cant use where with group by
select loc ,count(1) from emp group by loc having count(1)>1;










