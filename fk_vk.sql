USE vk;

DESC profiles;

ALTER TABLE profiles
  ADD CONSTRAINT profiles_user_id_fk 
    FOREIGN KEY (user_id) REFERENCES users(id)
      ON DELETE CASCADE,
  ADD CONSTRAINT profiles_photo_id_fk
    FOREIGN KEY (photo_id) REFERENCES media(id)
      ON DELETE SET NULL;
     
     
     
 DESC messages;

ALTER TABLE messages
  ADD CONSTRAINT messages_from_user_id_fk 
    FOREIGN KEY (from_user_id) REFERENCES users(id)
    	ON DELETE SET NULL,
  ADD CONSTRAINT messages_to_user_id_fk 
    FOREIGN KEY (to_user_id) REFERENCES users(id)
   		ON DELETE SET NULL;
   
   
 DESC communities;

ALTER TABLE communities
	ADD CONSTRAINT communities_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users(id);
 
 DESC communities_users;

ALTER TABLE communities_users
	ADD CONSTRAINT communities_users_community_id_fk
		FOREIGN KEY (community_id) REFERENCES communities(id)
			ON DELETE CASCADE,
	ADD CONSTRAINT user_id_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users(id);
			

 DESC friendship;

 ALTER TABLE friendship
	ADD CONSTRAINT user_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users(id),
	ADD CONSTRAINT friend_id_user_id_fk
		FOREIGN KEY (friend_id) REFERENCES users(id),
	ADD CONSTRAINT status_id_friendship_statuses_fk
		FOREIGN KEY (status_id) REFERENCES friendship_statuses(id);
	
DESC likes;


ALTER TABLE likes
	ADD CONSTRAINT user_like_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users(id),
	ADD CONSTRAINT target_id_media_id_fk
		FOREIGN KEY (target_id) REFERENCES media(id)
			ON DELETE CASCADE,
	ADD CONSTRAINT target_type_id_target_type_id_fk
		FOREIGN KEY (target_type_id) REFERENCES target_types(id)
			ON DELETE CASCADE,
	ADD CONSTRAINT like_type_id_like_types_id_fk
		FOREIGN KEY (like_type_id) REFERENCES like_types(id)
			ON DELETE CASCADE;

DESC posts;

ALTER TABLE posts
	ADD CONSTRAINT post_user_id_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users(id);
	
DESC media;

ALTER TABLE media
	ADD CONSTRAINT media_media_type_id_media_types_id_fk
		FOREIGN KEY (media_type_id) REFERENCES media_types(id)
			ON DELETE SET NULL,
	ADD CONSTRAINT media_user_id_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users(id)
			ON DELETE CASCADE;
	
	
	
DESC photo;

ALTER TABLE photo
	ADD CONSTRAINT photo_media_type_id_media_type_id_fk
		FOREIGN KEY (media_type_id) REFERENCES media_types(id)
			ON DELETE SET NULL,
	ADD CONSTRAINT photo_user_id_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users(id);
	

DESC relations;

ALTER TABLE relations
	ADD CONSTRAINT relations_user_id_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users(id),
	ADD CONSTRAINT relative_id_user_id_fk
		FOREIGN KEY (relative_id) REFERENCES users(id),
	ADD CONSTRAINT relations_status_id_relation_statuses_fk
		FOREIGN KEY (relation_status_id) REFERENCES relation_statuses(id);
	
-- ЗАДАНИЕ ПРО JOIN
	
	-- 2.Пусть задан некоторый пользователь. 
-- Из всех друзей этого пользователя найдите человека, который больше всех общался с нашим 
-- пользоваетелем.

SELECT (SELECT CONCAT(first_name, ' ', last_name) FROM users WHERE id = from_user_id) AS friend,
  COUNT(*) AS total_messages 
  FROM messages 
    WHERE to_user_id = 52 
      AND from_user_id IN (
        SELECT friend_id AS id 
          FROM friendship 
            WHERE user_id = messages.to_user_id
        UNION
        SELECT user_id AS id 
          FROM friendship 
            WHERE friend_id = messages.to_user_id    
        )
    GROUP BY messages.from_user_id
    ORDER BY total_messages DESC
    LIMIT 1
;
-- С помощью JOIN 

SELECT users.first_name, COUNT(*) AS total_messages
  FROM users
    JOIN messages
  ON users.id = 
  GROUP BY orders.user_id
  ORDER BY total_orders;
  
 
 
 
 -- 3. Подсчитать общее количество лайков, которые получили 10 самых молодых пользователей.

SELECT
  user_id,
  (SELECT CONCAT(first_name, ' ', last_name) FROM users WHERE id = p.user_id) AS name, 
  birthday, 
  (SELECT COUNT(target_id) FROM likes WHERE target_id in (
      SELECT id FROM media WHERE user_id = p.user_id)
  ) AS total_like 
  FROM profiles p
  ORDER BY birthday DESC
  LIMIT 10;
 
-- C помощью JOIN 

 SELECT profiles.user_id, users.first_name, users.last_name, profiles.birthday
 	FROM users 
 		JOIN profiles
 			ON users.id = profiles.user_id
 	ORDER BY birthday DESC
 	LIMIT 10;

