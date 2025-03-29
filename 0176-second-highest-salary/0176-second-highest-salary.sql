# Write your MySQL query statement below
select max(distinct(salary)) as SecondHighestSalary
from Employee
where salary < all(select max(distinct(salary))
from Employee) 