USE orders;
SELECT * FROM order_one;

-- Второе задание 
SELECT MAX(o_date) FROM order_one;
SELECT MIN(o_date) FROM order_one;
-- Наблюдаемый периуд с 2001 по 2031

-- Третье задание 
SELECT COUNT(DISTINCT(user_id)) AS users FROM order_one; -- количество пользлвателей 28,938
SELECT COUNT(*) FROM order_one; -- количество строк 37,714
SELECT COUNT(DISTINCT(order_id)) AS users FROM order_one; -- количество заказов 37,714

-- Четвертое задание 
SELECT AVG(price) FROM order_one WHERE YEAR(o_date) = '2001';
SELECT AVG(price) FROM order_one WHERE YEAR(o_date) = '2002';
SELECT AVG(price) FROM order_one WHERE YEAR(o_date) = '2003';
SELECT AVG(price) FROM order_one WHERE YEAR(o_date) = '2004';
SELECT AVG(price) FROM order_one WHERE YEAR(o_date) = '2005';
SELECT AVG(price) FROM order_one WHERE YEAR(o_date) = '2006';
SELECT AVG(price) FROM order_one WHERE YEAR(o_date) = '2007';
SELECT AVG(price) FROM order_one WHERE YEAR(o_date) = '2008';
SELECT AVG(price) FROM order_one WHERE YEAR(o_date) = '2009';
SELECT AVG(price) FROM order_one WHERE YEAR(o_date) = '2010';
SELECT AVG(price) FROM order_one WHERE YEAR(o_date) = '2011';
SELECT AVG(price) FROM order_one WHERE YEAR(o_date) = '2012';
SELECT AVG(price) FROM order_one WHERE YEAR(o_date) = '2013';
SELECT AVG(price) FROM order_one WHERE YEAR(o_date) = '2014';
SELECT AVG(price) FROM order_one WHERE YEAR(o_date) = '2015';
SELECT AVG(price) FROM order_one WHERE YEAR(o_date) = '2016';
SELECT AVG(price) FROM order_one WHERE YEAR(o_date) = '2017';
SELECT AVG(price) FROM order_one WHERE YEAR(o_date) = '2018';