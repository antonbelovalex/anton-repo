USE vk;

-- Второе задание 
SELECT user_id from friendship WHERE friend_id IN (

SELECT from_user_id FROM messages WHERE to_user_id = 9
UNION ALL 
SELECT to_user_id FROM messages  WHERE from_user_id = 9;


-- Третье задание 

SELECT COUNT(id) as kolvo_likes 
  FROM likes 
  WHERE user_id IN (
  SELECT * FROM (
    SELECT user_id FROM profiles ORDER BY birthday LIMIT 10
  ) AS youngest
);

-- Четвертое задание 

SELECT 'men', COUNT(id)  as kolvo_likes FROM likes WHERE user_id IN (SELECT user_id FROM profiles WHERE sex = 'm')
 UNION ALL  
SELECT 'women', COUNT(id) as kolvo_likes FROM likes WHERE user_id IN (SELECT user_id FROM profiles WHERE sex = 'f');


-- Пятое задание 
SELECT user, total FROM (SELECT id AS user, 0 AS total 
FROM users 
 WHERE id NOT IN (SELECT user_id AS user 
 FROM media 
  UNION ALL 
SELECT user_id AS user 
FROM likes 
  UNION ALL 
  SELECT from_user_id AS user 
  FROM messages
  ) 
 UNION 
 SELECT  user, COUNT(*) AS total 
FROM 
     (SELECT user_id AS user 
    FROM media 
  UNION ALL 
  SELECT user_id AS user 
    FROM likes 
  UNION ALL 
  SELECT from_user_id AS user 
  FROM messages) a GROUP BY user) b 
ORDER BY total 
  LIMIT 10;
 

 
 
  