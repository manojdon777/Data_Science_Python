-- Mathematical operations
select * from emp;
select sum(salary) from emp;
select avg(salary) from emp;
select min(salary) from emp;
select max(salary) from emp;

-- group by 
-- query to display the count of employees from each location
-- select list should always be a part of your group by clause
select loc,count(1) from emp group by loc;

-- import csv file into database
select count(*) from emp_data;
select count(*) from dept;
select count(1) from dept; -- 1 is like index of your first column

-- write a query to display avg salary of emp from each dept
select * from emp_data;
select distinct dept_id from emp_data;
select avg(salary),dept_id from emp_data group by dept_id; -- we can use diff column with aggregate function

-- write a query display sum of salaries for each gender
select distinct gender from emp_data;
select sum(salary),gender from emp_data group by gender;

-- write a query to display sum of salaries for each dept ,salary should be greater than 5000

select sum(salary),dept_id from emp_data where salary>5000 group by dept_id;

-- display the cound of emp from each loc
select loc,count(1) from emp_data group by loc;

-- what is the sequence of sql commands in sql query
  -- select from where group by having order by limit 
-- the sequence in which it actually gets executed
 -- from where group by having select order by limit
 
-- replace
select * from emp;
-- select replace(col name/string,'sub_string to be replaced','new_string')
select replace(fname,'a','@') from emp;
select replace('python','th','@');

-- padding : it pads some spl charecters to your string to maintain its length
-- rpad: right padding  and lpad: left padding

-- rpad(string,required length,char for padding)
select rpad('sql tutorial',20,'*');
select lpad('sql tutorial',20,0);
select lpad('sql tutorial',20,' ');

-- substring
-- select substr(string,start_index,length required for output)
/* p  y  t h o n
1     2  3 4 5 6
-6   -5 -4     -1*/
select substr('python',2,2); -- yt

select substr('python',-4,3); -- tho
select substr('python',-1,2);
select substr('python',3); 
select reverse('python'); -- reverse string

-- trim : this trims the extra spaces 
select trim('   sql tutorial  ') as trimmed_string;

-- write a query to find first 5 char from your fname
select substr(fname,1,5) from emp;

-- mask your data
-- PII columns: personal information
select * from emp;
select replace(contact,substr(contact,7,4),'****') from emp;

-- subquery : query within query
-- query to display empid having salary < max salary
select empid from emp where salary<max(salary);-- wrong,will not work
select empid from emp where salary < (select max(salary) from emp);
select empid from emp where salary < (select max(salary) as max_sal from emp);

-- second highest salary
select max(salary) from emp;
select salary from emp where salary < (select max(salary) as max_sal from emp)
 order by salary desc;
 
 select max(salary) from emp where salary < (select max(salary) as max_sal from emp)
 order by salary desc;
 
 -- nth highest salary
 -- select min(salary) from (select salary from emp order by salary desc limit n) as em;
 
 select min(salary) from (select salary from emp order by salary desc limit 4) as em;
 /* 80 
 60
 50
 40
 30
 20 */
 
 select min(salary) from (select distinct salary from emp order by salary desc limit 4) as em;

-- joins
/* 1. inner join : gives you all the mathcing records, its like an intersection
2. left join  : will give u all rows from left table and only matching rows from ur right table
3. right join.: vice versa of left join, gives you all rows from right table and only matching rows from left table 
4. self join : joining a table with itself*/

-- select col_list from tbl1 join tbl2 on tbl1.col=tbl2.col

-- inner join
select * from table1;
/* a.    a.   aa,aa,aa,aa,bb,dd
   a.    a
   b.    b
   c     d
   null. f
   d     null  */
   
select * from table2;
select t1.col1,t2.col2 from table1 t1 inner join table2 t2 on t1.col1=t2.col2;

-- left join 

select t1.col1,t2.col2 from table1 t1 left join table2 t2 on t1.col1=t2.col2;

-- right join 

select t1.col1,t2.col2 from table1 t1 right join table2 t2 on t1.col1=t2.col2;

select * from emp_data;

-- self join
-- display the list of employees who are managers
select e.empid,d.mgr_id from emp_data e join emp_data d on e.empid=d.mgr_id;

select * from emp;
-- limit offset(skip rows),row count
select * from emp limit 2,3;

-- library used for database connection
-- pip install mysql-connector-python

-- create view : it will be created on top of any table
create view nov_view as select empid,fname from emp;
select * from nov_view;















 






