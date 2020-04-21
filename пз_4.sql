USE orders;
SELECT * FROM orders.`orders_20190822-1` LIMIT 5;
 
  -- Первый пункт задания 
 CREATE TABLE user_n_2016
SELECT user_id,COUNT(id_o) AS n
FROM orders.`orders_20190822-1`
  WHERE YEAR(o_date) = '2016' AND MONTH(o_date) = '12'
  GROUP BY user_id;
  
 SELECT n,COUNT(user_id) AS n_users
  FROM user_n_2016
  GROUP BY n
 	ORDER BY n;
 	
 -- Количество заказов на каждого пользователя до январь 2017 года 
CREATE TABLE user_n
SELECT user_id,COUNT(id_o) AS n
FROM orders.`orders_20190822-1`
  WHERE date(o_date)< date('2017-01-01')
  GROUP BY user_id;

 SELECT n,COUNT(user_id) AS n_users
  FROM user_n
  GROUP BY n
 	ORDER BY n;
  

 