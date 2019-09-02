--rank scores

SELECT Score , (SELECT COUNT(DISTINCT Score) FROM Scores WHERE score >a.Score)+1 as Rank
FROM
Scores a

Order by 1 desc

--running totals
select
    a.date,
    sum(b.sales) as cumulative_sales
from sales_table a
join sales_table b on a.date >= b.date
group by a.date
order by a.date;


--cummulative salarys
select a.Id Id, a.Month Month, sum(b.Salary) Salary
from Employee a left join Employee b
on a.Id=b.Id
where b.Month<=a.Month and (a.Id,a.Month) not in(
select Id, max(Month) renctmonth
from Employee
group by Id)
and
abs(b.Month-a.Month)<=2
group by a.Id, A.Month
order by Id asc, Month desc

--2nd highest salary

SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee E1
WHERE
Salary <(SELEcT MAX(Salary) FROM Employee E2);



--Nth highest salary
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      DECLARE M = N-1;
      SELECT Salary
      FROM Employee
      GROUP BY Salary
      ORDER BY Salary DESC
      LIMIT 1 OFFSET N
  );
END

---rank scores
SELECT Score , (SELECT COUNT(DISTINCT Score) FROM Scores WHERE score >a.Score)+1 as Rank
FROM Scores a
Order by 1 desc


--product price on given date
SELECT p.product_id
	,CASE
		WHEN change_date <= '2019-08-16'
			THEN new_price
		ELSE 10
		END AS price
FROM Products p
JOIN (
	SELECT product_id
		,max(change_date) AS dt
	FROM Products p
	WHERE change_date <= '2019-08-16'
	GROUP BY product_id

	UNION

	SELECT product_id
		,min(change_date) AS dt
	FROM Products p
	GROUP BY product_id
	HAVING MIN(change_date) > '2019-08-16'
	) a ON a.product_id = p.product_id
	AND a.dt = p.change_date;

--Market Analysis I orders by each user
SELECT u.user_id AS buyer_id
	,u.join_date
	,ifnull(t.orders_in_2019, 0) AS orders_in_2019
FROM Users u
LEFT JOIN (
	SELECT buyer_id AS user_id
		,count(buyer_id) AS orders_in_2019
	FROM Orders
	WHERE year(order_date) = 2019
	GROUP BY buyer_id
	) t ON u.user_id = t.user_id


--average sessions per user
SELECT IFNULL(ROUND(COUNT(DISTINCT session_id) / count(DISTINCT user_id), 2), 0.0) AS average_sessions_per_user
FROM Activity
WHERE DATE_ADD(activity_date, INTERVAL 30 DAY) >= '2019-07-27'


--most active business
select
    business_id
from events as a
left join
    (
    select event_type, avg(occurences) as av
    from events
    group by event_type
    ) as b
on a.event_type = b.event_type
where a.occurences > b.av
group by business_id
having count(*)>1;


-- highest grade for each student
SELECT student_id
	,MIN(course_id) AS course_id
	,grade
FROM Enrollments
WHERE (
		grade
		,student_id
		) IN (
		SELECT MAX(grade) AS grade_max
			,student_id
		FROM Enrollments
		GROUP BY student_id
		)
GROUP BY student_id
	,grade
ORDER BY 1
	,2

--daily users count
SELECT login_date
	,count(1) AS user_count
FROM (
	SELECT min(activity_date) AS login_date
		,user_id
	FROM Traffic
	WHERE activity_date <= '2019-06-30' #login_date BETWEEN date_add('2019-06-30', interval - 90 day)
			AND '2019-06-30'
		AND activity = 'login'
	GROUP BY user_id
	) a
WHERE login_date BETWEEN date_add('2019-06-30', interval - 90 day)
		AND '2019-06-30'
GROUP BY login_date

--game play install and retention

SELECT a1.event_date AS install_dt
	,COUNT(DISTINCT a1.player_id) AS installs
	,round(sum(CASE
				WHEN a2.event_date IS NOT NULL
					THEN 1
				ELSE 0
				END) / count(DISTINCT a1.player_id), 2) AS Day1_Retention
FROM (
	SELECT player_id
		,min(event_date) AS event_date
	FROM Activity
	GROUP BY player_id
	) a1
LEFT JOIN Activity a2 ON a1.player_id = a2.player_id
	AND a1.event_date = a2.event_date - 1
GROUP BY install_dt;


--game play users logged in next day
--# Write your MySQL query statement below
SELECT ROUND(COUNT(a2.player_id)/COUNT(a1.player_id),2) as fraction
FROM

(
  SELECT MIN(event_date) as d1 , player_id
  FROM
  Activity
  GROUP BY player_id
)a1
LEFT JOIN
Activity a2 ON a1.d1+1 = a2.event_date
AND a2.player_id = a1.player_id;

--game play games played so far
select a1.player_id, a1.event_date, sum(a2.games_played) as games_played_so_far
from Activity as a1
inner join Activity as a2
on a1.event_date >= a2.event_date
and a1.player_id = a2.player_id
group by  a1.player_id, a1.event_date


--game platy 1st login day

SELECT a1.player_id, a1.device_id
FROM Activity a1
JOIN
(
select player_id , min(event_date) as first_login
from
Activity
GROUP By player_id
) a2
ON a1.player_id = a2.player_id
AND a1.event_date = a2.first_login


--distinct products sold between dates
select  p.product_id , p.product_name
from
Sales s
join
Product p on p.product_id = s.product_id

GROUP BY p.product_id ,p.product_name
HAVING MIN(sale_date) >= '2019-01-01'
AND MAX(sale_date)<='2019-03-31'

-- Sales Analysis II
-- customers bought one product not other
SELECT buyer_id
FROM Product p
JOIN Sales s ON p.product_id = s.product_id
GROUP BY buyer_id
HAVING SUM(CASE
			WHEN p.product_name = 'S8'
				THEN 1
			ELSE 0
			END) >= 1
	AND SUM(CASE
			WHEN p.product_name = 'iPhone'
				THEN 1
			ELSE 0
			END) = 0


--best seller by sales price
SELECT seller_id
FROM Sales
GROUP BY seller_id
HAVING sum(price) = (
		SELECT SUM(price) AS s
		FROM Sales
		GROUP BY seller_id
		ORDER BY 1 DESC LIMIT 1
		)

-- Project Employees
--most experienced employees

SELECT p.project_id, e.employee_id
FROM
Project p
JOIN
Employee e ON e.employee_id = p.employee_id
JOIN
  (
    SELECT
    p.project_id,  MAX(e.experience_years) yrs
  FROM Project p
  JOIN Employee e ON e.employee_id = p.employee_id
  GROUP BY p.project_id
  ) t
  ON t.project_id = p.project_id AND e.experience_years = t.yrs

  --average experience
  select
    p.project_id, ROUND(avg(e.experience_years),2) AS average_years
from
Project p
join
Employee e
ON p.employee_id = e.employee_id
GROUP BY  p.project_id



--Product Sales
-- products sold in 1st year

SELECT s.product_id, m.first_year, s.quantity, s.price
FROM
Sales s
JOIN
(
SELECT
product_id, MIN(year) AS first_year#, quantity, price
FROM
Sales
GROUP BY product_id#, quantity, price
    ) m
 ON s.product_id = m.product_id AND s.year = m.first_year


--custoners who brought all products
Select
      customer_id
FROM
    Customer
WHERE
    product_key IN (SELECT DISTINCT product_key FROM Product)
GROUP BY customer_id
HAVING COUNT(distinct product_key) = (SELECT COUNT(DISTINCT product_key) FROM Product)


--consecutive seats

select distinct a.seat_id
from cinema a
join cinema b
on abs(a.seat_id - b.seat_id) = 1
and a.free=true and b.free=true
order by a.seat_id;

--consective numbers
SELECT T.Num AS ConsecutiveNums
FROM (
	SELECT DISTINCT A.Num
	FROM Logs A
	LEFT JOIN Logs B ON A.Id = B.Id - 1
	LEFT JOIN Logs C ON A.Id = C.Id - 2
	WHERE A.Num = B.Num
		AND A.Num = C.Num
	) T;

--3 or more consective rows
--https://leetcode.com/problems/human-traffic-of-stadium/

SELECT t.* FROM stadium t
    LEFT JOIN stadium p1 ON t.id - 1 = p1.id
    LEFT JOIN stadium p2 ON t.id - 2 = p2.id
    LEFT JOIN stadium n1 ON t.id + 1 = n1.id
    LEFT JOIN stadium n2 ON t.id + 2 = n2.id
WHERE (t.people >= 100 AND p1.people >= 100 AND p2.people >= 100)
     OR (t.people >= 100 AND n1.people >= 100 AND n2.people >= 100)
     OR (t.people >= 100 AND n1.people >= 100 AND p1.people >= 100)
ORDER BY id;


--customers placing largest no of orders

SELECT customer_number
FROM(
SELECT COUNT(1) as cnt, customer_number
FROM
orders
GROUP BY customer_number
ORDER BY 1 DESC
LIMIT 1
    )a


--students per dept
SELECT
d.dept_name , SUM(CASE WHEN student_id IS NULL THEN 0 ELSE 1 END ) as student_number
FROM
department d
LEFT JOIN
student s
ON
s.dept_id = d.dept_id
GROUP BY d.dept_name
ORDER BY 2 DESC,1


--atleast 5 direct reports
SELECT Name FROM Employee
WHERE Id in
    (select ManagerId FROM  Employee
    GROUP BY ManagerId
    HAVING COUNT(DISTINCT Id) >=5
     )


--cancellation rate
--
SELECT t.Request_at AS Day
	,ROUND((
			SUM(CASE
					WHEN t.STATUS LIKE '%cancelled%'
						THEN 1
					ELSE 0
					END) / count(1)
			), 2) AS "Cancellation Rate"
FROM Trips t
WHERE EXISTS (
		SELECT *
		FROM Users u
		WHERE u.Users_Id = t.Client_Id
			AND u.Banned = 'No'
			AND t.Request_at BETWEEN '2013-10-01'
				AND '2013-10-03'
		)
GROUP BY t.Request_at


-----Department
--top 3 salaries


SELECT
    d.Name AS Department,
    e1.Name as Employee,
    e1.Salary
FROM
Employee e1
JOIN
Department d ON e1.DepartmentID = d.Id
WHERE
    (
    SELECT COUNT(DISTINCT e2.Salary)
    FROM
        Employee e2
    WHERE
        e1.Salary <=e2.Salary
    AND e1.DepartmentID = e2.DepartmentID
    ) <=3

 ORDER BY 1, 3 desc


--highest salary

SELECT d.Name AS Department
	,e1.Name AS Employee
	,e1.Salary
FROM Employee e1
JOIN Department d ON d.Id = e1.DepartmentId
WHERE 1 = (
		SELECT COUNT(DISTINCT e2.Salary)
		FROM Employee e2
		WHERE e2.DepartmentId = e1.DepartmentId
			AND e1.Salary <= e2.Salary
		)
	/*
joins and having
SELECT
    d.Name AS Department,
    e1.Name AS Employee,
    e1.Salary
FROM
    Employee e1
JOIN
    Department d ON d.Id = e1.DepartmentId
LEFT JOIN
    Employee e2 ON e2.DepartmentId = e1.DepartmentId
    AND e1.Salary <=e2.Salary
GROUP BY d.Name, e1.Name, e1.Salary
HAVING COUNT(DISTINCT e2.Salary) =1
*/



--delete duplicate email s

DELETE p
FROM Person p
LEFT JOIN
(
  SELECT  Email, MIN(Id) as Id
  FROM
  Person
  GROUP BY Email
  #HAVING COUNT(1)> 1
) a
ON p.Email = a.Email
AND p.Id = a.Id
WHERE
  a.Id is NULL




